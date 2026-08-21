import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

from tools.print_layout import pdf_layout

TEST_TEMP_ROOT = Path("C:/tmp/print-layout-tests")


@contextmanager
def test_temp_dir():
    TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as temp_dir:
        yield Path(temp_dir)


def touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"not an image")


def make_png(path: Path, size=(320, 240), color=(200, 80, 120)) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", size, color).save(path)


class RecordingPdf:
    def __init__(self):
        self.calls = []

    def saveState(self):
        self.calls.append(("saveState",))

    def setStrokeColorRGB(self, red, green, blue):
        self.calls.append(("setStrokeColorRGB", red, green, blue))

    def setLineWidth(self, width):
        self.calls.append(("setLineWidth", width))

    def setDash(self, pattern, phase):
        self.calls.append(("setDash", pattern, phase))

    def line(self, x1, y1, x2, y2):
        self.calls.append(("line", x1, y1, x2, y2))

    def restoreState(self):
        self.calls.append(("restoreState",))


class PdfLayoutTest(unittest.TestCase):
    def test_discover_book_images_sorts_by_leading_number(self):
        with test_temp_dir() as folder:
            touch(folder / "10_page.png")
            touch(folder / "02_page.png")
            touch(folder / "00_cover.png")
            touch(folder / "01_page.png")

            book = pdf_layout.discover_book_images(folder)

            self.assertEqual(book["cover"].name, "00_cover.png")
            self.assertEqual(
                [page.name for page in book["body_pages"]],
                ["01_page.png", "02_page.png", "10_page.png"],
            )

    def test_pair_body_pages_keeps_title_page_alone_then_pairs_spreads(self):
        with test_temp_dir() as folder:
            pages = [folder / "01.png", folder / "02.png", folder / "03.png"]

            self.assertEqual(
                pdf_layout.pair_body_pages(pages),
                [(None, pages[0]), (pages[1], pages[2])],
            )

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

    def test_generate_cover_and_body_pdfs(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_cover.png")
            make_png(folder / "01_page.png")
            make_png(folder / "02_page.png")
            make_png(folder / "03_page.png")
            output_dir = folder / "print-output"

            cover_result = pdf_layout.generate_pdfs(folder, output_dir, "cover")
            body_result = pdf_layout.generate_pdfs(folder, output_dir, "body", "landscape")

            self.assertTrue(Path(cover_result["cover_pdf"]).exists())
            self.assertTrue(Path(body_result["body_pdf"]).exists())
            self.assertEqual(body_result["body_sheet_count"], 2)

            cover_reader = PdfReader(cover_result["cover_pdf"])
            body_reader = PdfReader(body_result["body_pdf"])
            cover_page = cover_reader.pages[0].mediabox
            body_page = body_reader.pages[0].mediabox

            self.assertEqual(len(cover_reader.pages), 1)
            self.assertEqual(len(body_reader.pages), 2)
            self.assertGreater(float(cover_page.height), float(cover_page.width))
            self.assertGreater(float(body_page.width), float(body_page.height))

    def test_generate_combined_pdf_for_both_target(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_cover.png")
            make_png(folder / "01_page.png")
            make_png(folder / "02_page.png")
            make_png(folder / "03_page.png")
            output_dir = folder / "print-output"

            result = pdf_layout.generate_pdfs(tmp_path := folder, output_dir, "both", "landscape")

            self.assertNotIn("cover_pdf", result)
            self.assertNotIn("body_pdf", result)
            self.assertTrue(Path(result["combined_pdf"]).exists())

            reader = PdfReader(result["combined_pdf"])
            cover_page = reader.pages[0].mediabox
            first_body_page = reader.pages[1].mediabox

            self.assertEqual(result["folder"], str(tmp_path))
            self.assertEqual(len(reader.pages), 3)
            self.assertGreater(float(cover_page.height), float(cover_page.width))
            self.assertGreater(float(first_body_page.width), float(first_body_page.height))

    def test_generate_portrait_body_pdf_uses_vertical_slots(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_cover.png")
            make_png(folder / "01_page.png")
            make_png(folder / "02_page.png")
            output_dir = folder / "print-output"

            result = pdf_layout.generate_pdfs(folder, output_dir, "body", "portrait")

            reader = PdfReader(result["body_pdf"])
            page = reader.pages[0].mediabox

            self.assertEqual(result["layout"], "portrait")
            self.assertTrue(result["body_pdf"].endswith("body-a4-portrait-2up.pdf"))
            self.assertGreater(float(page.height), float(page.width))

    def test_generate_booklet_pdf_includes_cover_blank_inside_cover_and_padding(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_cover.png")
            make_png(folder / "01_page.png")
            make_png(folder / "02_page.png")
            make_png(folder / "03_page.png")
            output_dir = folder / "print-output"

            result = pdf_layout.generate_pdfs(folder, output_dir, "booklet", "landscape")

            self.assertTrue(Path(result["booklet_pdf"]).exists())
            self.assertEqual(result["booklet_page_count"], 8)
            self.assertEqual(result["booklet_sheet_count"], 2)
            self.assertTrue(result["booklet_pdf"].endswith("booklet-a4-landscape.pdf"))
            self.assertEqual(len(PdfReader(result["booklet_pdf"]).pages), 4)

    def test_draw_binding_guide_marks_center_fold_line(self):
        pdf = RecordingPdf()

        pdf_layout.draw_binding_guide(pdf)

        center_x = pdf_layout.A4_LANDSCAPE[0] / 2
        page_height = pdf_layout.A4_LANDSCAPE[1]
        self.assertIn(("setStrokeColorRGB", 0.55, 0.55, 0.55), pdf.calls)
        self.assertIn(("setLineWidth", 0.6), pdf.calls)
        self.assertIn(("setDash", [4, 4], 0), pdf.calls)
        self.assertIn(("line", center_x, pdf_layout.MARGIN, center_x, page_height - pdf_layout.MARGIN), pdf.calls)

    def test_generate_body_pdf_excludes_selected_pages(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_cover.png")
            page1 = folder / "01_page.png"
            page2 = folder / "02_page.png"
            page3 = folder / "03_page.png"
            make_png(page1)
            make_png(page2)
            make_png(page3)
            output_dir = folder / "print-output"

            result = pdf_layout.generate_pdfs(folder, output_dir, "body", "landscape", excluded_pages={page2})

            self.assertEqual(result["body_page_count"], 2)
            self.assertEqual(result["excluded_page_count"], 1)
            self.assertEqual(result["body_sheet_count"], 2)
            self.assertEqual(len(PdfReader(result["body_pdf"]).pages), 2)


if __name__ == "__main__":
    unittest.main()
