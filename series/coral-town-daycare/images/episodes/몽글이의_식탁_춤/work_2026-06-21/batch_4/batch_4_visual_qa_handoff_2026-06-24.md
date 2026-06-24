# Batch 4 Visual QA Handoff - 몽글이의 식탁 춤 - 2026-06-24

## Stop Reason

- Current image-generation context is contaminated.
- User stopped the session after two failed page 03 edit attempts drifted away from the target page.
- Do not continue visual edits in the current image context.
- Start a fresh session before any further image generation or editing.
- The failed edit attempts were not copied into the project workspace. Do not use recent `.codex/generated_images` outputs from this contaminated session as references.

## User QA Summary

- Text QA: all text is acceptable. Do not change text.
- Do not run local text overlays or local text-panel compositing.
- Preserve existing approved/generated Korean text exactly during visual edits.
- Visual fixes needed:
  - Pages 07-08: Mongle's eyes should match the reference button-like black eyes. Current candidates show visible white sclera.
  - Pages 09-12: Aru's face differs noticeably from the original/reference. Fix Aru's face toward the official reference.
  - Pages 03, 04, and 09: Sua/Lulu head ridges protrude too much and make their impression differ from the references. Soften and compact the seahorse head ridges.

## Current Review Candidate Set

- Cover:
  - `work_2026-06-21/batch_1/00_cover_candidate_v1.png`
- Page 01:
  - `work_2026-06-21/batch_1/01_candidate_text_v8_a5_noheldspoon_v1.png`
- Page 02:
  - `work_2026-06-21/batch_1/02_candidate_text_v6_a5_noheldspoon_v1.png`
- Page 03:
  - `work_2026-06-21/batch_1/03_candidate_text_v8_a5_noheldspoon_roundtable_hat_aru_v1.png`
  - Needs visual QA fix: Sua/Lulu head ridges too spiky/protruding.
- Page 04:
  - `work_2026-06-21/batch_2/04_candidate_text_v5_page03edit_seatlock_textfix_v2.png`
  - Needs visual QA fix: Sua/Lulu head ridges too spiky/protruding.
- Page 05:
  - `work_2026-06-21/batch_2/05_candidate_text_v1_page04edit_seatlock_v1.png`
- Page 06:
  - `work_2026-06-21/batch_2/06_candidate_text_v1_page05edit_seatlock_v1.png`
- Page 07:
  - `work_2026-06-21/batch_3/07_candidate_text_v2_focus_mari_mongle_v1.png`
  - Needs visual QA fix: Mongle eyes should be black button eyes, no visible white sclera.
- Page 08:
  - `work_2026-06-21/batch_3/08_candidate_text_v4_fresh_chairfix_v1.png`
  - Needs visual QA fix: Mongle eyes should be black button eyes, no visible white sclera.
- Page 09:
  - `work_2026-06-21/batch_3/09_candidate_text_v8_groupmeal_mongle_on_chair_v1.png`
  - Needs visual QA fix: Aru face closer to reference; Sua/Lulu head ridges softer/less protruding.
- Page 10:
  - `work_2026-06-21/batch_4/10_candidate_text_v1_page09edit_transition_v1.png`
  - Needs visual QA fix: Aru face closer to reference.
- Page 11:
  - `work_2026-06-21/batch_4/11_candidate_text_v1_yard_dance_v1.png`
  - Needs visual QA fix: Aru face closer to reference.
- Page 12:
  - `work_2026-06-21/batch_4/12_candidate_text_v1_yard_ending_v1.png`
  - Needs visual QA fix: Aru face closer to reference.

## Existing Review Sheet

- Complete 00-12 contact sheet with current candidates:
  - `work_2026-06-21/review_contact_sheets/mongle_table_dance_current_candidates_00_12_complete_2026-06-24.png`

## Required Official References For Next Session

- Rulebook:
  - `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Script:
  - `series/coral-town-daycare/docs/episodes/몽글이의_식탁_춤.md`
- Page plan:
  - `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21/page_plan.md`
- Mongle reference for pages 07-08 eye repair:
  - `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
  - Optional original reference if needed: `series/coral-town-daycare/references/characters/몽글이.png`
- Aru reference for pages 09-12 face repair:
  - `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
  - Optional original reference if needed: `series/coral-town-daycare/references/characters/아루.png`
- Sua/Lulu references for pages 03, 04, and 09:
  - `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
  - `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
  - Optional originals if needed:
    - `series/coral-town-daycare/references/characters/수아.png`
    - `series/coral-town-daycare/references/characters/루루.png`
- Background references only if the edit flow needs broader grounding:
  - Dining room for pages 03-04 and 09-10: `series/coral-town-daycare/references/배경_식당.png`
  - Yard/playground for pages 11-12: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - Coral tunnel for yard continuity: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`

## Recommended Fresh-Session Repair Strategy

1. Start in a fresh image-generation context.
2. For each page, emit only:
   - the current candidate as the edit target;
   - the official reference image(s) for the specific character(s) being fixed;
   - the location reference only if the generator needs broader grounding.
3. Keep every edit as a minimal visual repair. Preserve:
   - all Korean text exactly;
   - text panel placement and style;
   - composition, camera, seating, table/background, and story action;
   - other characters not named in the fix.
4. Do not use the failed page 03 edit attempts from the contaminated session.
5. Save revised candidates with new filenames, do not overwrite originals.

## Suggested Output Filenames

- Page 03:
  - `work_2026-06-21/batch_1/03_candidate_text_v9_visualqa_sualulu_ridgefix_v1.png`
- Page 04:
  - `work_2026-06-21/batch_2/04_candidate_text_v6_visualqa_sualulu_ridgefix_v1.png`
- Page 07:
  - `work_2026-06-21/batch_3/07_candidate_text_v3_visualqa_mongle_buttoneyes_v1.png`
- Page 08:
  - `work_2026-06-21/batch_3/08_candidate_text_v5_visualqa_mongle_buttoneyes_v1.png`
- Page 09:
  - `work_2026-06-21/batch_3/09_candidate_text_v9_visualqa_aru_sualulu_v1.png`
- Page 10:
  - `work_2026-06-21/batch_4/10_candidate_text_v2_visualqa_aru_face_v1.png`
- Page 11:
  - `work_2026-06-21/batch_4/11_candidate_text_v2_visualqa_aru_face_v1.png`
- Page 12:
  - `work_2026-06-21/batch_4/12_candidate_text_v2_visualqa_aru_face_v1.png`

## Page-Specific Prompt Notes

### Pages 07-08 - Mongle Eyes

- Edit target: current page 07 or page 08 candidate.
- Reference: Mongle official no-bag reference.
- Change only Mongle's eyes.
- Replace visible white-sclera eyes with the official simple black button-like eyes.
- Preserve Mongle's yellow beret, sailor collar, body, tentacles, expression, and pose.
- Preserve Mari, Banguli, text, background, and composition.

### Pages 03, 04, 09 - Sua/Lulu Head Ridges

- Edit target: current page candidate.
- References: Sua and Lulu official no-bag references.
- Change only Sua/Lulu head ridges.
- Make ridges shorter, softer, rounder, and closer to the official references.
- Do not make ridges sharper, taller, more coral-like, or more spiky.
- Preserve their long snouts, curled tails, fins, clothing, and facial expressions.
- Preserve all text and unrelated characters.

### Pages 09-12 - Aru Face

- Edit target: current page candidate.
- Reference: Aru official no-bag reference, optionally original Aru reference too.
- Change only Aru's face toward the official round pufferfish reference:
  - round pufferfish face/body;
  - small dark eyes in the reference style;
  - correct small pursed pufferfish mouth;
  - calm toddler expression;
  - fins only, no human hands/fingers/arms.
- Preserve Aru's body silhouette, spikes, scarf, position, and pose as much as possible.
- Preserve text and all other characters.

## Next Concrete Action

In the new session:

1. Read this handoff first.
2. Emit page 07 target and Mongle reference only.
3. Generate `07_candidate_text_v3_visualqa_mongle_buttoneyes_v1.png`.
4. Verify A5 size and no text changes.
5. Continue page 08 with the same eye-only repair.


## Continuation Notes - 2026-06-24

- Page 07 generated candidate pass:
  - `work_2026-06-21/batch_3/07_candidate_text_v3_visualqa_mongle_buttoneyes_v1.png`
  - QA: Mongle eyes changed to black button-like eyes; A5 size preserved at 1054x1492.
- Page 08 failed candidate:
  - `work_2026-06-21/batch_3/08_candidate_text_v5_visualqa_mongle_buttoneyes_v1.png`
  - Status: fail / do not use. Mongle eyes improved, but Mari teacher's eyes were also simplified toward button eyes.
- Page 08 retry candidate pass:
  - `work_2026-06-21/batch_3/08_candidate_text_v6_visualqa_mongle_buttoneyes_marilock_v1.png`
  - QA: Mongle eyes changed to black button-like eyes; Mari teacher retains human eyes; A5 size preserved at 1054x1492.
- Rejected local patch attempts were kept only in `C:\tmp\mongle_visualqa` and should not be used as page candidates.

## Continuation Notes - 2026-06-24, Later Pass

- Page 03 generated candidate pass:
  - `work_2026-06-21/batch_1/03_candidate_text_v9_visualqa_sualulu_ridgefix_v1.png`
  - QA: Sua/Lulu head ridges softened; A5 size preserved at 1054x1492.
- Page 04 generated candidate pass:
  - `work_2026-06-21/batch_2/04_candidate_text_v6_visualqa_sualulu_ridgefix_v1.png`
  - QA: Sua/Lulu head ridges softened; A5 size preserved at 1054x1492.
- Page 09 generated attempts hold / do not use:
  - First attempt changed/contaminated text with another page's copy.
  - Text-lock retry preserved the page 09 copy better but shifted panel/composition too much.
  - No page 09 retry was copied into the project workspace.
- Page 10 generated candidate pass:
  - `work_2026-06-21/batch_4/10_candidate_text_v2_visualqa_aru_face_v1.png`
  - QA: Aru face closer to official pufferfish reference; A5 size preserved at 1054x1492.
- Page 11 generated candidate pass:
  - `work_2026-06-21/batch_4/11_candidate_text_v2_visualqa_aru_face_v1.png`
  - QA: Aru face closer to official pufferfish reference; A5 size preserved at 1054x1492.
- Page 12 generated candidate pass:
  - `work_2026-06-21/batch_4/12_candidate_text_v2_visualqa_aru_face_v1.png`
  - QA: Aru face closer to official pufferfish reference; A5 size preserved at 1054x1492. First page 12 attempt used page 11 copy and was not saved.
- Remaining visual QA item after this pass:
  - Page 09 still needs a fresh, more constrained repair for Aru face and Sua/Lulu ridges without text/panel drift.
