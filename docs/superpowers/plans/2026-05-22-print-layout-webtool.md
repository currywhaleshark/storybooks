# Print Layout Web Tool Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local web tool that previews completed picture-book pages and generates separate cover and A4-landscape 2-up body PDFs without cropping images.

**Architecture:** Use a small Node.js HTTP server for folder discovery, preview metadata, static UI serving, and invoking the PDF generator. Use a Python PDF generator for deterministic A4 layout with Pillow for image sizing and ReportLab for PDF output. Keep the browser UI static and practical.

**Tech Stack:** Node.js built-in `http`, `fs`, and `child_process`; browser HTML/CSS/JavaScript; bundled Python with `Pillow` and `reportlab`; PowerShell verification commands.

---

### Task 1: PDF Layout Core

**Files:**
- Create: `tools/print_layout/__init__.py`
- Create: `tools/print_layout/pdf_layout.py`
- Create: `tools/print_layout/tests/test_pdf_layout.py`

- [ ] **Step 1: Write tests for page discovery and spread pairing**

Create `tools/print_layout/tests/test_pdf_layout.py`:

```python
import json
from pathlib import Path

from tools.print_layout import pdf_layout


def touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"not an image")


def test_discover_book_images_sorts_by_leading_number(tmp_path):
    touch(tmp_path / "10_10페이지.png")
    touch(tmp_path / "02_2페이지.png")
    touch(tmp_path / "00_표지.png")
    touch(tmp_path / "01_1페이지.png")

    book = pdf_layout.discover_book_images(tmp_path)

    assert book["cover"].name == "00_표지.png"
    assert [page.name for page in book["body_pages"]] == [
        "01_1페이지.png",
        "02_2페이지.png",
        "10_10페이지.png",
    ]


def test_pair_body_pages_leaves_blank_for_odd_count(tmp_path):
    pages = [tmp_path / "01.png", tmp_path / "02.png", tmp_path / "03.png"]

    assert pdf_layout.pair_body_pages(pages) == [
        (pages[0], pages[1]),
        (pages[2], None),
    ]
```

- [ ] **Step 2: Run tests and verify they fail**

Run:

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tools.print_layout.tests.test_pdf_layout -v
```

Expected: FAIL because `tools.print_layout.pdf_layout` does not exist.

- [ ] **Step 3: Implement discovery and pairing**

Create `tools/print_layout/pdf_layout.py`:

```python
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def leading_number(path: Path) -> int | None:
    match = re.match(r"^(\d+)", path.name)
    return int(match.group(1)) if match else None


def is_image(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def discover_book_images(folder: Path) -> dict[str, object]:
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
```

- [ ] **Step 4: Run tests and verify they pass**

Run the same pytest command.

Expected: PASS.

### Task 2: PDF Generation Commands

**Files:**
- Modify: `tools/print_layout/pdf_layout.py`
- Modify: `tools/print_layout/tests/test_pdf_layout.py`

- [ ] **Step 1: Add tests for PDF file creation**

Append tests that create tiny valid PNGs and assert both PDFs exist:

```python
from PIL import Image


def make_png(path: Path, size=(320, 240), color=(200, 80, 120)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, color).save(path)


def test_generate_cover_and_body_pdfs(tmp_path):
    make_png(tmp_path / "00_표지.png")
    make_png(tmp_path / "01_1페이지.png")
    make_png(tmp_path / "02_2페이지.png")
    make_png(tmp_path / "03_3페이지.png")
    output_dir = tmp_path / "print-output"

    result = pdf_layout.generate_pdfs(tmp_path, output_dir, "both")

    assert Path(result["cover_pdf"]).exists()
    assert Path(result["body_pdf"]).exists()
    assert result["body_sheet_count"] == 2
```

- [ ] **Step 2: Run tests and verify failure**

Expected: FAIL because `generate_pdfs` does not exist.

- [ ] **Step 3: Implement contain drawing and PDF generation**

Add to `pdf_layout.py`:

```python
A4_PORTRAIT = A4
A4_LANDSCAPE = landscape(A4)
MARGIN = 24
GUTTER = 18


def draw_image_contained(pdf: canvas.Canvas, image_path: Path, box: tuple[float, float, float, float]) -> None:
    x, y, width, height = box
    with Image.open(image_path) as image:
        image_width, image_height = image.size
    scale = min(width / image_width, height / image_height)
    draw_width = image_width * scale
    draw_height = image_height * scale
    draw_x = x + (width - draw_width) / 2
    draw_y = y + (height - draw_height) / 2
    pdf.drawImage(str(image_path), draw_x, draw_y, draw_width, draw_height, preserveAspectRatio=True, mask="auto")


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


def generate_pdfs(folder: Path, output_dir: Path, target: str) -> dict[str, object]:
    book = discover_book_images(folder)
    cover = book["cover"]
    body_pages = book["body_pages"]
    output_dir.mkdir(parents=True, exist_ok=True)

    result: dict[str, object] = {
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
```

- [ ] **Step 4: Add CLI entrypoint**

Add:

```python
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
```

- [ ] **Step 5: Run tests**

Expected: PASS.

### Task 3: Local Web Server

**Files:**
- Create: `tools/print-layout/server.js`
- Create: `tools/print-layout/package.json`

- [ ] **Step 1: Implement server**

Create a Node server that:

- serves files from `tools/print-layout/public`
- lists valid book folders under `series`
- serves image files through `/image?path=...`
- invokes Python CLI through `/api/generate`

Use repository-root-relative paths and reject paths outside the repository.

- [ ] **Step 2: Add npm scripts**

Create `tools/print-layout/package.json`:

```json
{
  "scripts": {
    "start": "node server.js",
    "test": "node --test tests/*.test.js"
  },
  "dependencies": {},
  "devDependencies": {}
}
```

- [ ] **Step 3: Smoke test API**

Run:

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' tools/print-layout/server.js
```

Expected: server prints a local URL.

### Task 4: Browser UI

**Files:**
- Create: `tools/print-layout/public/index.html`
- Create: `tools/print-layout/public/styles.css`
- Create: `tools/print-layout/public/app.js`

- [ ] **Step 1: Build UI shell**

Create a practical single-screen app with:

- top toolbar
- book selector
- cover preview panel
- body spread preview panel
- previous/next controls
- PDF generation buttons
- status area

- [ ] **Step 2: Load detected books**

Call `/api/books`, populate the selector, and display the first available book.

- [ ] **Step 3: Render previews**

Use image URLs from `/image?path=...`. Render the cover and current body spread. If the final spread has no right page, render an empty slot.

- [ ] **Step 4: Generate PDFs**

Call `/api/generate` with `target` as `cover`, `body`, or `both`. Show generated output paths in the status area.

### Task 5: Verification

**Files:**
- Modify: `tools/print-layout/README.md`

- [ ] **Step 1: Run unit tests**

Run:

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tools.print_layout.tests.test_pdf_layout -v
```

Expected: PASS.

- [ ] **Step 2: Generate sample PDFs**

Run:

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m tools.print_layout.pdf_layout series/sanho-village-daycare/images --target both
```

Expected: `cover.pdf` and `body-a4-landscape-2up.pdf` are created under `series/sanho-village-daycare/images/print-output`.

- [ ] **Step 3: Start web server**

Run the server and open the printed local URL.

Expected: detected books render, previews show visible images, and buttons generate PDFs.

- [ ] **Step 4: Document usage**

Create `tools/print-layout/README.md` with start and PDF-generation instructions.
