# Reference Asset Plan - 루루야, 약속했잖아

## Purpose

This episode needs two episode-specific visual references before main page generation:

- Lulu's favorite picture book, used as the same recurring prop on pages 2, 3, and 4.
- The messy art-time state, used as the same recurring classroom condition on pages 5 through 9 and partially cleaned on page 10.

Do not use previous episode final images as visual references. Prior episode images may contain unrelated story details and should not contaminate this episode.

## Asset 01 - Lulu's Favorite Picture Book

### Target Path

`series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

### Role

Recurring prop reference for pages 2, 3, and 4.

### Visual Locks

- A small toddler board-book style picture book with rounded corners and thick pages.
- Pastel seafoam/aqua cover so it reads clearly against Lulu's coral-pink body and Jun-i's blue body.
- Pink coral border and one large warm yellow shell emblem on the cover.
- A small pink ribbon bookmark or shell-shaped tab may peek out.
- Cream-colored page edges, soft watercolor and colored-pencil texture.
- No readable letters, no pseudo-writing, no episode title, no random signs.
- It should look cherished and gently handled, not dirty, damaged, torn, or dramatic.

### Generation Prompt

Create a clean prop reference image for a Korean toddler picture-book episode. The subject is Lulu's favorite picture book: a small rounded-corner board book for preschoolers, pastel seafoam/aqua cover, pink coral border, one large warm yellow shell emblem centered on the cover, cream page edges, and a small pink ribbon bookmark or shell-shaped tab peeking out. Show the closed front cover and a slightly open angled view in the same image like a simple prop reference sheet. Soft watercolor and colored-pencil texture, warm paper feel, low-saturation pastel colors. No characters. No readable text, no pseudo-writing, no title, no labels, no watermark. Plain warm off-white background.

## Asset 02 - Messy Art-Time State

### Target Path

`series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/messy_art_time_state_ref.png`

### Role

Recurring scene-state reference for pages 5, 6, 7, 8, 9, and the cleanup transition on page 10.

### Visual Locks

- Same Coral Town Daycare classroom feeling as `배경_교실.png`: rounded windows, shell shelves, soft underwater daycare mood.
- Low toddler-height art tables and floor area.
- Joyfully messy but safe: color paper scraps, round paint pots, soft brushes, coral-powder paint bowls, shell decorations, small toy pieces.
- No sharp scissors, broken glass, dangerous tools, dark stains, spilled puddles that look like injury, or scary chaos.
- The mess should be readable as "many things to clean up" while still leaving clear walkable space.
- No story text, no labels, no pseudo-writing.

### Generation Prompt

Create an environment-state reference image for a Korean toddler picture-book episode. The setting is the Coral Town Daycare classroom art corner after lively preschool art play. Show rounded windows, shell-shaped shelves, soft underwater daycare decor, low toddler art tables, and a warm pastel classroom mood. On the tables and floor are scattered color paper scraps, soft brushes, round paint pots, coral-powder paint bowls, shell decorations, safe craft pieces, and a few small toys. The scene should feel joyfully messy but safe and gentle, with clear walkable space and no scary chaos. No characters. No readable text, no labels, no pseudo-writing, no watermark. Soft watercolor and colored-pencil texture, low-saturation pastel colors, warm paper feel.

## QA

- The picture book must be recognizable at small size and remain the same object when handed, dropped on the floor, and returned.
- The messy art-time state must be consistent enough that pages 5 through 9 feel like one continuing cleanup problem.
- Both references must avoid text because later page text should come only from the script.

## Generated Assets

- `lulu_favorite_picture_book_ref.png`: accepted as the current prop reference. It has no readable text, a clear seafoam cover, pink coral frame, yellow shell emblem, cream pages, and pink shell/ribbon tab.
- `messy_art_time_state_ref.png`: restored/regenerated in the current checkout on 2026-06-08 with the official classroom reference used as the strict spatial source. It preserves the same classroom space and watercolor/colored-pencil style, and clearly shows a safe but significant art-time mess that should read to a child as needing cleanup. For main page prompts, keep the same mess identity but request slightly clearer child walkable space when characters are present.
