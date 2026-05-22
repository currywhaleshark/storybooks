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

            result = pdf_layout.generate_pdfs(folder, output_dir, "both")

            self.assertTrue(Path(result["cover_pdf"]).exists())
            self.assertTrue(Path(result["body_pdf"]).exists())
            self.assertEqual(result["body_sheet_count"], 2)

            cover_reader = PdfReader(result["cover_pdf"])
            body_reader = PdfReader(result["body_pdf"])
            cover_page = cover_reader.pages[0].mediabox
            body_page = body_reader.pages[0].mediabox

            self.assertEqual(len(cover_reader.pages), 1)
            self.assertEqual(len(body_reader.pages), 2)
            self.assertGreater(float(cover_page.height), float(cover_page.width))
            self.assertGreater(float(body_page.width), float(body_page.height))


if __name__ == "__main__":
    unittest.main()
