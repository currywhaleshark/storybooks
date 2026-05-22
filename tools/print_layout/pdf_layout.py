from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
A4_PORTRAIT = A4
A4_LANDSCAPE = landscape(A4)
MARGIN = 24
GUTTER = 18
LAYOUTS = {"landscape", "portrait"}


def leading_number(path: Path) -> int | None:
    match = re.match(r"^(\d+)", path.name)
    return int(match.group(1)) if match else None


def is_image(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def discover_book_images(folder: Path) -> dict[str, Any]:
    images = [path for path in folder.iterdir() if is_image(path)]
    numbered = [(leading_number(path), path) for path in images]
    numbered = [(number, path) for number, path in numbered if number is not None]
    numbered.sort(key=lambda item: (item[0], item[1].name))

    cover = next((path for number, path in numbered if number == 0), None)
    body_pages = [path for number, path in numbered if number and number > 0]

    return {"cover": cover, "body_pages": body_pages}


def pair_body_pages(pages: list[Path]) -> list[tuple[Path, Path | None]]:
    pairs = []
    for index in range(0, len(pages), 2):
        left = pages[index]
        right = pages[index + 1] if index + 1 < len(pages) else None
        pairs.append((left, right))
    return pairs


def draw_image_contained(pdf: canvas.Canvas, image_path: Path, box: tuple[float, float, float, float]) -> None:
    x, y, width, height = box
    with Image.open(image_path) as image:
        image_width, image_height = image.size
    scale = min(width / image_width, height / image_height)
    draw_width = image_width * scale
    draw_height = image_height * scale
    draw_x = x + (width - draw_width) / 2
    draw_y = y + (height - draw_height) / 2
    pdf.drawImage(
        str(image_path),
        draw_x,
        draw_y,
        draw_width,
        draw_height,
        preserveAspectRatio=True,
        mask="auto",
    )


def body_page_size(layout: str) -> tuple[float, float]:
    return A4_PORTRAIT if layout == "portrait" else A4_LANDSCAPE


def body_slots(layout: str) -> list[tuple[float, float, float, float]]:
    page_width, page_height = body_page_size(layout)
    if layout == "portrait":
        slot_width = page_width - MARGIN * 2
        slot_height = (page_height - MARGIN * 2 - GUTTER) / 2
        return [
            (MARGIN, MARGIN + slot_height + GUTTER, slot_width, slot_height),
            (MARGIN, MARGIN, slot_width, slot_height),
        ]

    slot_width = (page_width - MARGIN * 2 - GUTTER) / 2
    slot_height = page_height - MARGIN * 2
    return [
        (MARGIN, MARGIN, slot_width, slot_height),
        (MARGIN + slot_width + GUTTER, MARGIN, slot_width, slot_height),
    ]


def draw_body_pages(pdf: canvas.Canvas, body_pages: list[Path], layout: str) -> int:
    pairs = pair_body_pages(body_pages)
    slots = body_slots(layout)
    for left, right in pairs:
        draw_image_contained(pdf, left, slots[0])
        if right is not None:
            draw_image_contained(pdf, right, slots[1])
        pdf.showPage()
    return len(pairs)


def generate_cover_pdf(cover: Path, output_path: Path) -> None:
    pdf = canvas.Canvas(str(output_path), pagesize=A4_PORTRAIT)
    page_width, page_height = A4_PORTRAIT
    draw_image_contained(pdf, cover, (MARGIN, MARGIN, page_width - MARGIN * 2, page_height - MARGIN * 2))
    pdf.showPage()
    pdf.save()


def generate_body_pdf(body_pages: list[Path], output_path: Path, layout: str) -> int:
    pdf = canvas.Canvas(str(output_path), pagesize=body_page_size(layout))
    sheet_count = draw_body_pages(pdf, body_pages, layout)
    pdf.save()
    return sheet_count


def generate_combined_pdf(cover: Path, body_pages: list[Path], output_path: Path, layout: str) -> int:
    pdf = canvas.Canvas(str(output_path), pagesize=A4_PORTRAIT)
    page_width, page_height = A4_PORTRAIT
    draw_image_contained(pdf, cover, (MARGIN, MARGIN, page_width - MARGIN * 2, page_height - MARGIN * 2))
    pdf.showPage()
    pdf.setPageSize(body_page_size(layout))
    sheet_count = draw_body_pages(pdf, body_pages, layout)
    pdf.save()
    return sheet_count


def generate_pdfs(folder: Path, output_dir: Path, target: str, layout: str = "landscape") -> dict[str, Any]:
    if layout not in LAYOUTS:
        raise ValueError("layout은 landscape 또는 portrait 여야 합니다.")

    book = discover_book_images(folder)
    cover = book["cover"]
    body_pages = book["body_pages"]
    output_dir.mkdir(parents=True, exist_ok=True)

    result: dict[str, Any] = {
        "folder": str(folder),
        "output_dir": str(output_dir),
        "layout": layout,
        "body_page_count": len(body_pages),
        "body_sheet_count": len(pair_body_pages(body_pages)),
    }

    if target == "cover":
        if cover is None:
            raise ValueError("표지 이미지를 찾을 수 없습니다.")
        cover_pdf = output_dir / "cover.pdf"
        generate_cover_pdf(cover, cover_pdf)
        result["cover_pdf"] = str(cover_pdf)

    if target == "body":
        if not body_pages:
            raise ValueError("본문 페이지를 찾을 수 없습니다.")
        body_pdf = output_dir / f"body-a4-{layout}-2up.pdf"
        generate_body_pdf(body_pages, body_pdf, layout)
        result["body_pdf"] = str(body_pdf)

    if target == "both":
        if cover is None:
            raise ValueError("표지 이미지를 찾을 수 없습니다.")
        if not body_pages:
            raise ValueError("본문 페이지를 찾을 수 없습니다.")
        combined_pdf = output_dir / f"print-ready-combined-{layout}.pdf"
        generate_combined_pdf(cover, body_pages, combined_pdf, layout)
        result["combined_pdf"] = str(combined_pdf)

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--output", default=None)
    parser.add_argument("--target", choices=["cover", "body", "both"], default="both")
    parser.add_argument("--layout", choices=sorted(LAYOUTS), default="landscape")
    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    output_dir = Path(args.output).resolve() if args.output else folder / "print-output"
    result = generate_pdfs(folder, output_dir, args.target, args.layout)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
