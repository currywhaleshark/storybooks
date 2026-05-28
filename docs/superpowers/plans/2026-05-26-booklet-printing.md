# Booklet Printing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a new booklet PDF target that includes the cover, inserts a blank inside-front-cover page, imposes pages for duplex folding, and exposes it in the web tool.

**Architecture:** Extend the existing Python PDF generator with small, testable booklet page-order helpers and a new `generate_booklet_pdf` function. Keep existing sequential cover/body/combined output unchanged. Update the Node server target allowlist and static web UI to call the new target.

**Tech Stack:** Python, Pillow, ReportLab, pypdf, Node.js static HTTP server.

---

## File Structure

- `tools/print_layout/pdf_layout.py`: add booklet page model helpers, sheet-pairing helpers, PDF drawing, target handling, and CLI target choice.
- `tools/print_layout/tests/test_pdf_layout.py`: add focused tests for page model, imposition order, and generated PDF page count.
- `tools/print-layout/server.js`: allow the `booklet` target in `/api/generate`.
- `tools/print-layout/public/index.html`: add a `책자 PDF` button.
- `tools/print-layout/public/app.js`: wire the new button and display the resulting path.
- `tools/print-layout/README.md`: document the new output file and CLI target.

### Task 1: Booklet Ordering Core

**Files:**
- Modify: `tools/print_layout/pdf_layout.py`
- Test: `tools/print_layout/tests/test_pdf_layout.py`

- [ ] **Step 1: Write failing tests**

Add tests that use path sentinels to verify:

```python
def test_booklet_pages_include_cover_inside_blank_body_and_padding(self):
    with test_temp_dir() as folder:
        cover = folder / "00_cover.png"
        pages = [folder / f"{number:02}.png" for number in range(1, 4)]

        booklet_pages = pdf_layout.booklet_pages(cover, pages)

        self.assertEqual(booklet_pages, [cover, None, pages[0], pages[1], pages[2], None, None, None])

def test_pair_booklet_sheets_orders_front_and_back_for_folding(self):
    with test_temp_dir() as folder:
        pages = [folder / f"{number:02}.png" for number in range(1, 17)]

        sheets = pdf_layout.pair_booklet_sheets(pages)

        self.assertEqual(sheets[0], ((pages[15], pages[0]), (pages[1], pages[14])))
        self.assertEqual(sheets[1], ((pages[13], pages[2]), (pages[3], pages[12])))
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tools.print_layout.tests.test_pdf_layout -v
```

Expected: fail because `booklet_pages` and `pair_booklet_sheets` do not exist.

- [ ] **Step 3: Implement helpers**

Add:

```python
BookletSlot = Path | None
BookletSide = tuple[BookletSlot, BookletSlot]
BookletSheet = tuple[BookletSide, BookletSide]

def booklet_pages(cover: Path, body_pages: list[Path]) -> list[BookletSlot]:
    pages: list[BookletSlot] = [cover, None, *body_pages]
    while len(pages) % 4:
        pages.append(None)
    return pages

def pair_booklet_sheets(pages: list[BookletSlot]) -> list[BookletSheet]:
    sheets = []
    left = 0
    right = len(pages) - 1
    while left < right:
        front = (pages[right], pages[left])
        back = (pages[left + 1], pages[right - 1])
        sheets.append((front, back))
        left += 2
        right -= 2
    return sheets
```

- [ ] **Step 4: Run tests**

Expected: new ordering tests pass.

### Task 2: Booklet PDF Generation

**Files:**
- Modify: `tools/print_layout/pdf_layout.py`
- Test: `tools/print_layout/tests/test_pdf_layout.py`

- [ ] **Step 1: Write failing PDF generation test**

Add a test that creates one cover and three body PNGs, calls `generate_pdfs(..., "booklet", "landscape")`, and asserts:

```python
self.assertTrue(Path(result["booklet_pdf"]).exists())
self.assertEqual(result["booklet_page_count"], 8)
self.assertEqual(result["booklet_sheet_count"], 2)
self.assertTrue(result["booklet_pdf"].endswith("booklet-a4-landscape.pdf"))
self.assertEqual(len(PdfReader(result["booklet_pdf"]).pages), 4)
```

- [ ] **Step 2: Run tests to verify failure**

Expected: fail because `booklet` is not an accepted target.

- [ ] **Step 3: Implement drawing and target handling**

Add `draw_booklet_pages` and `generate_booklet_pdf`, drawing both sides of every booklet sheet with blanks skipped. Update `generate_pdfs` to accept `target == "booklet"`, require both cover and body pages, and return `booklet_pdf`, `booklet_page_count`, and `booklet_sheet_count`.

- [ ] **Step 4: Run tests**

Expected: all Python PDF layout tests pass.

### Task 3: Web Tool Option

**Files:**
- Modify: `tools/print-layout/server.js`
- Modify: `tools/print-layout/public/index.html`
- Modify: `tools/print-layout/public/app.js`
- Modify: `tools/print-layout/README.md`

- [ ] **Step 1: Update server target allowlist**

Change the target validation to include `booklet`:

```javascript
const target = ["cover", "body", "both", "booklet"].includes(body.target) ? body.target : "both";
```

- [ ] **Step 2: Add and wire UI button**

Add a `bookletButton`, disable it with the other generation buttons, call `generate("booklet")` on click, and display `result.booklet_pdf` as `책자`.

- [ ] **Step 3: Update README**

Document `booklet-a4-landscape.pdf` and `--target booklet`.

- [ ] **Step 4: Run verification**

Run Python tests and generate a sample booklet PDF from an existing episode folder.
