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


def generate_cover_pdf(cover: Path, output_path: Path) -> None:
    pdf = canvas.Canvas(str(output_path), pagesize=A4_PORTRAIT)
    page_width, page_height = A4_PORTRAIT
    draw_image_contained(pdf, cover, (MARGIN, MARGIN, page_width - MARGIN * 2, page_height - MARGIN * 2))
    pdf.showPage()
    pdf.save()


def generate_body_pdf(body_pages: list[Path], output_path: Path) -> int:
    pdf = canvas.Canvas(str(output_path), pagesize=A4_LANDSCAPE)
    page_width, page_height = A4_LANDSCAPE
    slot_width = (page_width - MARGIN * 2 - GUTTER) / 2
    slot_height = page_height - MARGIN * 2
    pairs = pair_body_pages(body_pages)
    for left, right in pairs:
        draw_image_contained(pdf, left, (MARGIN, MARGIN, slot_width, slot_height))
        if right is not None:
            draw_image_contained(pdf, right, (MARGIN + slot_width + GUTTER, MARGIN, slot_width, slot_height))
        pdf.showPage()
    pdf.save()
    return len(pairs)


def generate_pdfs(folder: Path, output_dir: Path, target: str) -> dict[str, Any]:
    book = discover_book_images(folder)
    cover = book["cover"]
    body_pages = book["body_pages"]
    output_dir.mkdir(parents=True, exist_ok=True)

    result: dict[str, Any] = {
        "folder": str(folder),
        "output_dir": str(output_dir),
        "body_page_count": len(body_pages),
        "body_sheet_count": len(pair_body_pages(body_pages)),
    }

    if target in {"cover", "both"}:
        if cover is None:
            raise ValueError("표지 이미지를 찾을 수 없습니다.")
        cover_pdf = output_dir / "cover.pdf"
        generate_cover_pdf(cover, cover_pdf)
        result["cover_pdf"] = str(cover_pdf)

    if target in {"body", "both"}:
        if not body_pages:
            raise ValueError("본문 페이지를 찾을 수 없습니다.")
        body_pdf = output_dir / "body-a4-landscape-2up.pdf"
        generate_body_pdf(body_pages, body_pdf)
        result["body_pdf"] = str(body_pdf)

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--output", default=None)
    parser.add_argument("--target", choices=["cover", "body", "both"], default="both")
    args = parser.parse_args()

    folder = Path(args.folder).resolve()
    output_dir = Path(args.output).resolve() if args.output else folder / "print-output"
    result = generate_pdfs(folder, output_dir, args.target)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
