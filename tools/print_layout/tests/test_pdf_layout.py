import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

from tools.print_layout import pdf_layout

TEST_TEMP_ROOT = Path(".tmp/print-layout-tests")


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


class PdfLayoutTest(unittest.TestCase):
    def test_discover_book_images_sorts_by_leading_number(self):
        with test_temp_dir() as folder:
            touch(folder / "10_10페이지.png")
            touch(folder / "02_2페이지.png")
            touch(folder / "00_표지.png")
            touch(folder / "01_1페이지.png")

            book = pdf_layout.discover_book_images(folder)

            self.assertEqual(book["cover"].name, "00_표지.png")
            self.assertEqual(
                [page.name for page in book["body_pages"]],
                ["01_1페이지.png", "02_2페이지.png", "10_10페이지.png"],
            )

    def test_pair_body_pages_leaves_blank_for_odd_count(self):
        with test_temp_dir() as folder:
            pages = [folder / "01.png", folder / "02.png", folder / "03.png"]

            self.assertEqual(
                pdf_layout.pair_body_pages(pages),
                [(pages[0], pages[1]), (pages[2], None)],
            )

    def test_generate_cover_and_body_pdfs(self):
        with test_temp_dir() as folder:
            make_png(folder / "00_표지.png")
            make_png(folder / "01_1페이지.png")
            make_png(folder / "02_2페이지.png")
            make_png(folder / "03_3페이지.png")
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
            make_png(folder / "00_표지.png")
            make_png(folder / "01_1페이지.png")
            make_png(folder / "02_2페이지.png")
            make_png(folder / "03_3페이지.png")
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
            make_png(folder / "00_표지.png")
            make_png(folder / "01_1페이지.png")
            make_png(folder / "02_2페이지.png")
            output_dir = folder / "print-output"

            result = pdf_layout.generate_pdfs(folder, output_dir, "body", "portrait")

            reader = PdfReader(result["body_pdf"])
            page = reader.pages[0].mediabox

            self.assertEqual(result["layout"], "portrait")
            self.assertTrue(result["body_pdf"].endswith("body-a4-portrait-2up.pdf"))
            self.assertGreater(float(page.height), float(page.width))


if __name__ == "__main__":
    unittest.main()
