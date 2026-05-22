# Print Layout Web Tool Design

## Goal

Build a local web tool for preparing completed picture-book images for printing. The tool should make it easy to preview the print layout and generate separate PDFs for the cover and the body.

## Source Structure

The tool targets the current repository layout:

- `series/<series-name>/images/00_표지.png`
- `series/<series-name>/images/01_1페이지.png`
- `series/<series-name>/images/02_2페이지.png`
- Additional numbered body pages in the same folder

It should also support episode folders with the same naming pattern, such as:

- `series/<series-name>/images/episodes/<episode-name>/00_표지.png`
- `series/<series-name>/images/episodes/<episode-name>/01_페이지.png`

## User Workflow

1. The user opens the local web tool.
2. The tool lists detected picture-book image folders.
3. The user selects one book folder.
4. The tool shows a cover preview and body preview.
5. The user can generate:
   - cover PDF
   - body PDF
   - both PDFs

## Print Layout

### Cover

- The cover is exported separately from the body.
- The cover PDF contains only `00_표지.png`.
- The cover image is scaled to fit the page without cropping.
- The cover is centered and keeps its original aspect ratio.

### Body

- The body PDF uses A4 landscape pages.
- Each A4 sheet contains two book pages, arranged left and right.
- Body pages start from the first numbered page after the cover.
- Pages are sorted by their leading number, not by raw filename text.
- Each book page is scaled with `contain` behavior: the full image must always be visible.
- Images keep their original aspect ratio and are centered inside their half-page area.
- If the body has an odd number of pages, the final right-side slot is left blank.

## Interface

The web tool should have a practical, print-focused interface:

- folder/book selector
- cover preview
- body spread preview with previous/next navigation
- page count and sheet count
- PDF generation buttons for cover, body, and both
- clear status messages for loading, generating, success, and errors

The first screen should be the usable tool itself, not a marketing or landing page.

## PDF Generation

PDF output should be deterministic and print-friendly:

- A4 page size
- landscape orientation for body
- no cropping
- predictable margins
- generated files saved under an output folder near the selected book, such as `print-output/`

Suggested filenames:

- `cover.pdf`
- `body-a4-landscape-2up.pdf`

## Error Handling

The tool should explain common problems in plain Korean:

- no image folders found
- no cover image found
- no body pages found
- image failed to load
- PDF generation failed

Missing optional pages should not crash the tool. A folder without a valid cover or body should be shown as unavailable with a reason.

## Testing

Verification should cover:

- `series/sanho-village-daycare/images`
- `series/sherlock-fin-deep-city/images/episodes/거꾸로_도서관의_다정한_비밀`
- numeric page sorting
- odd page count blank right slot
- no-crop image scaling
- cover and body PDF creation

Browser verification should include at least one desktop viewport and confirm that previews render visible images without overlap.
