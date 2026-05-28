# Booklet Printing Design

## Goal

Add a new print option that creates a booklet-imposed PDF from an episode image folder. The PDF should be printable with duplex printing, then folded in half to produce a booklet.

## Page Model

- `00_표지.png` is page 1, the front cover.
- Page 2 is intentionally blank, representing the inside front cover.
- Numbered body images start on page 3 in their natural order: `01_...`, `02_...`, and so on.
- The generator pads the final page list with blank pages until the total page count is a multiple of 4.

## Booklet Imposition

The booklet output uses A4 landscape sheets with two logical pages per side. For each physical sheet:

- front side: last remaining page on the left, first remaining page on the right
- back side: next first page on the left, next last page on the right

For 16 total booklet pages, the first sheet is:

```text
front: 16 | 1
back:   2 | 15
```

This order lets the user print duplex, fold the stack in half, and read pages in order.

## User Interface

Keep the existing cover/body/combined PDF buttons unchanged. Add a new `책자 PDF` option that generates the booklet-imposed PDF.

## Command Line

Add `--target booklet` to `tools.print_layout.pdf_layout`. The output file should be named `booklet-a4-landscape.pdf` and saved under the selected folder's `print-output` directory.

## Testing

Add unit tests for:

- booklet page sequence generation, including cover, inside-cover blank, body pages, and padding
- booklet sheet pairing order
- PDF generation with the new `booklet` target
