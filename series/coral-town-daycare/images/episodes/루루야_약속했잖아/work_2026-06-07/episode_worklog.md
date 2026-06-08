# Episode Worklog - 루루야, 약속했잖아

## Source

- Full prompt/script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아.md`
- TTS narration script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아_tts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07`
- Final folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final`

## Reference Audit

- Inspected this turn:
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/배경_교실.png`
- Known official references available:
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
- Missing episode-specific references identified by user:
  - Lulu's favorite picture book for pages 2 through 4.
  - Messy art-time state for pages 5 through 10.
- Reference asset plan added:
  - `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/reference_asset_plan.md`

## User QA Locks

- Lulu and Sua often lose reference-image detail. Treat their actual PNG references as visual truth.
- The Coral Town Daycare series must preserve the delicate reference-image painting style. Do not simplify all characters into generic round sea-animal children.
- Lulu must keep her detailed coral-pink seahorse structure, head ridge, coral head ornament, sailor outfit, translucent back fin, and curled tail.
- Sua must keep her purple seahorse structure, dotted/spiny head ridge, blue sailor outfit, and curled tail even when she appears small.
- Aru must keep the reference pufferfish body and sailor scarf. Never give Aru human hands, feet, legs, or a human-like body.
- Bags are worn only for arrival/departure or when explicitly mentioned. Otherwise omit them from bodies or park them in the classroom storage/background.

## Batch Status

- Episode-specific references generated:
  - `work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`
  - `work_2026-06-07/reference_assets/messy_art_time_state_ref.png`
- Reference QA:
  - Picture book passes for recurring prop use: no text, clear seafoam cover, pink coral border, yellow shell emblem, cream pages, pink shell/ribbon tab.
  - Messy art-time state passes for later continuity use. It is intentionally quite cluttered; later page prompts should preserve the same art mess but leave visible child walkable space.
- Batch 1 prepared: `work_2026-06-07/batch_1/batch_1_prompt_plan.md`
- Batch 1 scope: `00_표지.png` through `03_페이지.png`
- Batch 1 v1 generated and held:
  - `work_2026-06-07/batch_1/00_candidate_text_v1.png`
  - `work_2026-06-07/batch_1/01_candidate_text_v1.png`
  - `work_2026-06-07/batch_1/02_candidate_text_v1.png`
  - `work_2026-06-07/batch_1/03_candidate_text_v1.png`
- Batch 1 v1 QA: hold / regenerate. Text is acceptable, but the visual direction fails current locks because bags are worn in non-arrival scenes, page 1 simplifies Aru and Popo away from their references, and several characters lose the delicate reference-image detail.
- Batch 1 v2/v3 generated:
  - `work_2026-06-07/batch_1/00_candidate_text_v2.png`
  - `work_2026-06-07/batch_1/00_candidate_text_v3.png`
  - `work_2026-06-07/batch_1/01_candidate_text_v2.png`
  - `work_2026-06-07/batch_1/02_candidate_text_v2.png`
  - `work_2026-06-07/batch_1/03_candidate_text_v2.png`
- Batch 1 v2 QA:
  - `00_candidate_text_v2.png`: improved, no worn bags, Lulu detail strong; hold for user choice against v3.
  - `00_candidate_text_v3.png`: improved close-medium variant, no worn bags, Lulu detail strong; hold for user choice against v2.
  - `01_candidate_text_v2.png`: much improved. No worn bags, Aru keeps pufferfish body and sailor scarf, Popo keeps recognizable moon-jellyfish body, Lulu/Sua details are stronger.
  - `02_candidate_text_v2.png`: improved. No worn bags on characters, same picture book prop is clear, Lulu detail is strong.
  - `03_candidate_text_v2.png`: improved. No worn bags on characters, same picture book prop appears on the floor, Lulu's disappointed expression and details are strong.
- User QA update on 2026-06-08: batch 1 v2/v3 is still not acceptable. Overall characters became too round compared with the official references. Aru still gained a separate attached body/torso instead of remaining only the pufferfish body with scarf. Popo was drawn with visible eyes; unless the page has a special instruction, Popo should not have visible eye expression.
- Current status: stop generation, record QA, commit/push. Resume tomorrow with stricter reference-silhouette prompts.
- Next retry locks:
  - Preserve official-reference silhouettes over extra cuteness; do not over-round characters.
  - Aru must be one true pufferfish body only, with small fins/spikes and sailor scarf; no separate body, torso, hands, feet, legs, or clothing-like lower half.
  - Popo's eyes are hidden or barely visible by default; emotion comes from mouth, dome tilt, and tentacles unless the script specifically asks for eyes.
  - Continue no worn bags in non-arrival classroom scenes.
- Picture book reference is connected to pages 2 and 3 in the batch 1 prompt plan.
- Messy art-time reference is reserved for pages 5 through 10.

## Next Step

- Regenerate batch 1 one page at a time with the updated locks: no worn bags in indoor scenes, preserve the delicate reference style, keep Aru as a true pufferfish with scarf and no human body parts, keep Popo as the full moon-jellyfish child, and protect Lulu/Sua fine detail.
- Before generation, attach/inspect the actual official reference images listed in the batch plan.
- Save candidates in `work_2026-06-07/batch_1` with stable names such as `00_candidate_text_v1.png`.
- QA must check character identity, exact Korean text, A5 portrait proportion, no contamination from previous episodes, and no Lulu/Sua detail loss.

## Resume Note - 2026-06-08

- Re-read the worklog, page plan, batch 1 prompt plan, reference asset plan, script, and rulebook with UTF-8 after mojibake appeared in console output.
- Current workspace inventory shows only markdown planning files under this episode work folder. The PNG reference assets and batch 1 candidates mentioned above are not present in the current folder checkout.
- Added `rework_prep_2026-06-08.md` with the corrected current inventory, missing asset list, retry locks, and first regeneration packet.
- Next concrete action: restore or regenerate `reference_assets/lulu_favorite_picture_book_ref.png` before any page 00 regeneration, because the cover prompt references it and pages 2 through 4 need the same prop continuity.

## Batch 1 Rework - 2026-06-08

- Generated and saved:
  - `work_2026-06-07/batch_1/00_candidate_text_v4.png`
  - `work_2026-06-07/batch_1/00_candidate_text_v5.png`
  - `work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`
  - `work_2026-06-07/batch_1/01_candidate_text_v3.png`
  - `work_2026-06-07/batch_1/02_candidate_text_v3.png`
  - `work_2026-06-07/batch_1/03_candidate_text_v3.png`
- Page 00 QA:
  - `00_candidate_text_v4.png`: hold/fail. Lulu detail is strong, but the title appears as `약속 했잖아` with an extra space, Jun-i has too much human-like lower body/leg structure, and background bags draw attention.
  - `00_candidate_text_v5.png`: current preferred candidate. Better title spacing, stronger Jun-i shark silhouette and tail, no worn bags, and Lulu detail remains strong. User review still needed before promotion.
- Page 01 QA:
  - `01_candidate_text_v3.png`: current preferred candidate. Text is readable, Lulu keeps detail, Aru remains a single pufferfish body with scarf and no human torso, Popo has hidden/barely visible eyes, and no characters wear bags.
- Page 02 QA:
  - `02_candidate_text_v3.png`: current preferred candidate. Text is readable, Lulu and Jun-i are close to their references, Jun-i avoids human legs, and the favorite picture book is clear between them.
- Page 03 QA:
  - `03_candidate_text_v3.png`: current preferred candidate. Text is readable, Lulu's gentle disappointment is clear, Jun-i is friendly and unaware in block play, and the same favorite picture book lies safely on the floor.
- Size check:
  - Page candidates are A5 portrait-like: `00` files are `1055x1491`, `01`-`03` files are `1054x1492`.
- Batch 1 status: candidates generated, not final promoted. Await user QA before final folder promotion or targeted retries.

## Mobile Review Upload - 2026-06-08

- Uploaded a Google Slides mobile review deck to Drive:
  - `루루야, 약속했잖아 - 배치1 후보 모바일 확인용 2026-06-08`
  - `https://docs.google.com/presentation/d/1LWs-bWQd8bbWdNXnbZ2xiLqg9SEurbh2UbaBgiMW7sA/edit?usp=drivesdk`
- Deck contents:
  - Slide 1: `00_candidate_text_v5.png`
  - Slide 2: `01_candidate_text_v3.png`
  - Slide 3: `02_candidate_text_v3.png`
  - Slide 4: `03_candidate_text_v3.png`
  - Slide 5: `lulu_favorite_picture_book_ref.png`
- Drive readback confirmed 5 slides in the presentation. This is for mobile QA only; no files were promoted to `final`.

## User Approval And Batch 2 Handoff - 2026-06-08

- User QA: "오 아주 좋아 모두 통과".
- Batch 1 approved candidates promoted to final:
  - `final/00_표지.png` from `batch_1/00_candidate_text_v5.png`
  - `final/01_페이지.png` from `batch_1/01_candidate_text_v3.png`
  - `final/02_페이지.png` from `batch_1/02_candidate_text_v3.png`
  - `final/03_페이지.png` from `batch_1/03_candidate_text_v3.png`
- Added batch 2 preparation files:
  - `work_2026-06-07/batch_2/batch_2_prompt_plan.md`
  - `work_2026-06-07/handoff_to_next_thread_batch_2.md`
- Batch 2 scope: pages 04-06.
- Next-thread first concrete action: re-read UTF-8 handoff and regenerate or restore `reference_assets/messy_art_time_state_ref.png` before pages 05-06. Page 04 may be generated first because it only needs the picture book prop, classroom, Lulu, Jun-i, Banguli, and Mari teacher.
- Stop gate: after batch 2 candidates and QA, return to user for approval before batch 3.

## Batch 2 Reference Prep - 2026-06-08

- Regenerated the missing messy art-time state reference:
  - `work_2026-06-07/reference_assets/messy_art_time_state_ref.png`
- Method note: built-in image generation initially failed with a server error. A grounded composite backup was made first as `reference_assets/messy_art_time_state_ref_composite_v1.png`. A later built-in generated version was rejected because it changed the classroom space, and was preserved only as `reference_assets/messy_art_time_state_ref_off_reference_room_v1.png`. The accepted main reference was then regenerated with the official classroom reference visible as the strict spatial source; the overpainted composite was preserved only as `reference_assets/messy_art_time_state_ref_overpaint_v1.png`.
- QA: accepted main reference passes as a reusable state reference for pages 05-10. It keeps the official classroom layout and watercolor/colored-pencil style, has no characters, no text, no labels, no worn bags, no sharp scissors, no broken glass, no dark stains, and leaves a visible walkable route while showing enough safe art-play clutter that a child can read it as needing cleanup.

## Batch 2 Generation - 2026-06-08

- Page 04:
  - `batch_2/04_candidate_illustration_v1.png`: built-in generated illustration candidate; strong visual candidate with a blank text panel.
  - `batch_2/04_candidate_text_v1.png`: hold. Codex-added local text pass; text overflows/does not match prior page lettering well enough.
  - `batch_2/04_candidate_text_v2.png`: current preferred page 04 candidate. This is a user-provided text composite based on `04_candidate_illustration_v1.png`, made to match the approved page lettering/panel feel more closely.
- Page 05:
  - `batch_2/05_candidate_text_v1.png`: built-in generated text-in-image candidate. Initial QA: text is contained inside the panel and appears close to the approved storybook lettering style; characters and art mess still need user QA before final promotion.
- Page 06:
  - Not yet generated. Multiple built-in text-in-image attempts failed with server errors. Do not fall back to Codex local text overlay unless the user explicitly asks; next attempt should generate the illustration and exact Korean text together, using page 04 v2 lettering/panel feel and page 05/messy-art continuity as references.

## Batch 2 Page 06 Retry - 2026-06-08

- User confirmed the interrupted target is page 06 / `06_candidate_text_v1.png`.
- Reconfirmed required references are present:
  - `references/characters/루루.png`
  - `references/characters/방울이.png`
  - `references/characters/마리_선생님.png`
  - `references/characters/몽글이.png`
  - `references/characters/아루.png`
  - `references/배경_교실.png`
  - `work_2026-06-07/reference_assets/messy_art_time_state_ref.png`
  - continuity/style references `batch_2/05_candidate_text_v1.png` and `batch_2/04_candidate_text_v2.png`
- Built-in image generation retry attempts:
  - Attempt 1: full structured text-in-image prompt, failed with `ServerError`.
  - Attempt 2: shortened text-in-image prompt with same hard locks, failed with `ServerError`.
- No `06_candidate_text_v1.png` file was produced.
- Next retry should remain built-in text-in-image generation if the server recovers. Do not use local text overlay unless the user explicitly requests it. CLI fallback is available only if the user explicitly chooses it and `OPENAI_API_KEY` is configured.
- Additional user-requested retry:
  - Attempt 3: shortened built-in text-in-image prompt for page 06, failed with `ServerError`.
  - Attempt 4: illustration-first prompt with a blank text panel allowed to reduce text-rendering load, failed with `ServerError`.
  - No page 06 candidate was produced.
- Later user-requested retry after waiting about two hours:
  - Attempt 5: built-in page 06 text-in-image prompt with page 04/05 continuity and official character locks, failed with `ServerError`.
  - Attempt 6: built-in page 06 illustration-first prompt allowing a clean blank text panel if Korean text rendering fails, failed with `ServerError`.
  - No `batch_2/06_candidate_text_v1.png` file was produced.
- Later retry after waiting about four more hours:
  - Attempt 7: built-in page 06 text-in-image prompt, failed with `ServerError`.
  - Attempt 8: shortened built-in page 06 text-in-image prompt succeeded.
  - Saved generated output to `batch_2/06_candidate_text_v1.png`.
  - Size check: `1054x1492`, A5 portrait-like.
  - Initial assistant QA noted possible text concern, but user QA corrected this: text is acceptable.
  - User requested composition improvement: Lulu should look toward Mari teacher while raising her hand/fin.
  - Attempt 9: regenerate as `06_candidate_text_v2.png` with Lulu looking at Mari teacher, failed with `ServerError`.
  - Attempt 10: shortened regenerate prompt with the same composition change, failed with `ServerError`.
  - Attempt 11: edit-style prompt using existing v1, preserving all text and changing only Lulu's gaze/body direction toward Mari teacher, failed with `ServerError`.
  - Current available page 06 candidate remains `batch_2/06_candidate_text_v1.png`; no v2 file was produced.

## Batch 2 Page 06 Composition Retry - 2026-06-08

- User QA clarified that the page 06 text in `06_candidate_text_v1.png` is acceptable.
- User requested a composition improvement: Lulu should look toward Mari teacher while raising her hand/fin.
- Retry attempts:
  - Attempt 12: built-in regenerate prompt for `06_candidate_text_v2.png`, failed with `ServerError`.
  - Attempt 13: shortened regenerate prompt, failed with `ServerError`.
  - Attempt 14: edit-style prompt using the visible v1 candidate, preserving the text panel and changing Lulu's staging toward Mari teacher, succeeded.
- Saved generated output to `batch_2/06_candidate_text_v2.png`.
- Size check: `1054x1492`, A5 portrait-like.
- Assistant QA: `06_candidate_text_v2.png` improves the requested interaction because Lulu now turns her face/body toward Mari teacher while raising her hand/fin. Text panel remains readable and in the same style. Character structures, safe art mess, and no-worn-bag lock remain acceptable for user review.
- User QA note: Banguli gained a small hand/arm-like appendage in `06_candidate_text_v2.png`; user wants it removed while keeping the rest of v2.
- Banguli correction attempts:
  - Attempt 15: minimal edit prompt preserving all content and removing only Banguli's hand/arm-like appendage, failed with `ServerError`.
  - Attempt 16: shortened minimal edit prompt, failed with `ServerError`.
  - No `06_candidate_text_v3.png` file was produced.
