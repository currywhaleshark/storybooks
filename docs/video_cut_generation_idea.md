# Video-Friendly Cut Generation Idea

## Idea

For narrated videos, do not always use the finished storybook page as a static frame. Instead, generate 1-3 video-friendly images per storybook page based on:

- the original finished page,
- the page script,
- official character and location references,
- and the intended narration flow.

This turns the output from a simple page-flip TTS video into a light animated-storyboard style video.

## Recommended Direction

Keep the print/storybook page as the source of truth, then derive separate video cuts.

Example per-page cut patterns:

- Quiet setup page: 1 cut.
- Emotion change page: 2 cuts.
- Action, clue, or reveal page: 3 cuts.

Possible structure:

```text
Original page
→ cut plan
→ cut-specific prompts
→ generated video images
→ narration segment mapping
→ rendered video
```

## Notes

- Video images should usually avoid embedded story text. Narration or separate subtitles can carry the text.
- Final video should support bottom subtitles. The subtitle layer should be added during video rendering, not baked into generated images, so timing, line breaks, font size, and wording can be adjusted without regenerating art.
- Character and location consistency will need strict reference use and QA.
- This should be piloted on 2-3 pages first before applying to a full episode.
- Keep these assets separate from final print pages.

## Status

Recorded as a future idea only. No implementation planned yet.
