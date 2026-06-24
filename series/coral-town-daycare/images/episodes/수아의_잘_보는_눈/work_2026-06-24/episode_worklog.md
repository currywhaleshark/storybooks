# Episode Worklog - 수아의 잘 보는 눈

## Source

- Full script/prompt set: `series/coral-town-daycare/sua-different-is-good/script/main.md`
- Current page plan: `series/coral-town-daycare/sua-different-is-good/script/pages.json`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24`
- Batch 1 folder: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/batch_1`
- Final folder: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/final` (not created yet)

## Reference Audit

- Official rulebook path is identified.
- Official reference files verified present this turn:
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/배경_교실.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Before any actual image generation, attach or visually inspect the official reference images listed for each page. Do not rely on prose descriptions alone.

## Batch 1 Status

- Batch 1 scope: cover/page 00 through page 03.
- Prepared files:
  - `batch_1/batch_1_prompt_plan.md`
  - `batch_1/00_표지.md`
  - `batch_1/01_루루는_반짝반짝.md`
  - `batch_1/02_나도_루루처럼_되면_좋겠다.md`
  - `batch_1/03_수아도_예뻐가_안_들려요.md`
- Candidate filenames planned in `batch_1_prompt_plan.md`:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`
- No batch 1 image candidates are present yet. Generation was blocked before image output.
- `series/coral-town-daycare/sua-different-is-good/image-prompts` currently exists but contains no files.

## Preparation QA - 2026-06-24

- Overall status: batch 1 is mostly ready, but there is one blocking inconsistency if the per-page markdown files are used directly.
- Strong points:
  - `batch_1_prompt_plan.md` identifies the script, rulebook, work folder, output filenames, official reference paths, and A5 portrait format.
  - It includes hard locks for official-reference fidelity, no human legs/feet, no unrelated previous-episode contamination, no worn bags in non-arrival scenes, and readable Korean text space.
  - Page 01-03 text in the batch plan matches the script text.
  - Page 01-03 per-page prompt files also match the script text and scene intent closely.
- Blocking inconsistency:
  - `batch_1/00_표지.md` does not match the script or `batch_1_prompt_plan.md`.
  - It uses the subtitle `— 다른 건 좋아 —` instead of `— 다 똑같지 않아서 좋아요 —`.
  - It changes the cover scene into a classroom/group shell-comparison scene, while the script and batch plan use Sua quietly finding a small shell or pink coral fragment near the playground/sand.
  - Do not generate the cover from `00_표지.md` as-is. Use the cover section inside `batch_1_prompt_plan.md` as the authoritative prompt, or correct `00_표지.md` before generation.
- Minor issue:
  - `batch_1_prompt_plan.md` has a harmless typo in page 01: `Text (verbmat)` should read `Text (verbatim)`.
- Planning caveat:
  - `script/pages.json` currently covers only pages 00-03. This is enough for batch 1, but it is not a full-episode page plan for all 13 pages.
- Text workflow risk:
  - The plan asks for illustration and exact Korean story text together. If the generator misspells or invents text, treat the page as failed or repair the text panel separately. Final pages must include the exact script text unless the user explicitly asks for illustration-only candidates.

## Next Step

- Fix or ignore `batch_1/00_표지.md`; do not use it as-is.
- Use `batch_1/batch_1_prompt_plan.md` as the current source of truth for batch 1 generation.
- Before generation, load/attach the official reference images for each page from the `References To Load` lists.
- Save outputs in `batch_1` with the planned stable filenames.
- QA each candidate for character identity, exact Korean text, A5 portrait proportion, no worn bags unless explicitly called for, no prior-episode contamination, and cover subtitle accuracy.

## Correction Applied - 2026-06-24

- Corrected `batch_1/00_표지.md` so the cover now matches the script and `batch_1_prompt_plan.md`:
  - Subtitle is now `— 다 똑같지 않아서 좋아요 —`.
  - Scene is now Sua quietly inspecting a small shell or pink coral fragment in the sand/playground-edge setting, with Banguli nearby and Lulu softly in the background.
  - Removed the off-script classroom/group shell-comparison setup.
- Corrected the page 01 typo in `batch_1_prompt_plan.md` from `Text (verbmat)` to `Text (verbatim)`.
- Current batch 1 preparation status: ready for generation prep, provided the official reference images listed per page are loaded/attached before generating.

## Reference Asset Prep - 2026-06-24

- User approved changing Lulu's episode ornament away from pink so it reads clearly against Lulu's pink body.
- Approved design direction: a special one-day mint/aqua coral hairpin with a cream star-shell and two or three pale-yellow bead nubs.
- Generated and saved reference assets:
  - `reference_assets/special_coral_hairpin_ref_v1.png`
  - `reference_assets/lulu_wearing_special_coral_hairpin_ref_v1.png`
- Added `reference_assets/reference_asset_plan.md` with usage locks.
- Updated batch 1 prep files so page 00, page 01, and page 03 use the special hairpin rather than Lulu's ordinary/default ornament.
- Earlier pink coral ornament draft is rejected/unused because it blended with Lulu's body color and did not create enough story-specific contrast.
- Follow-up correction: added the special hairpin and Lulu-wearing-special-hairpin files to page 00, page 01, and page 03 `References To Load` lists in `batch_1_prompt_plan.md`.

## Reference Asset Correction - 2026-06-24

- User QA rejected `reference_assets/lulu_wearing_special_coral_hairpin_ref_v1.png` because Lulu drifted far from the official reference.
- Root cause: the rejected file was generated as a new character image instead of editing/compositing the official Lulu reference.
- Corrective action: created official-reference-based composites by placing the special hairpin onto the existing Lulu reference images:
  - `reference_assets/lulu_official_no_bag_special_hairpin_composite_v1.png` from `references/characters/no_bag/루루_no_bag.png`
  - `reference_assets/lulu_official_special_hairpin_composite_v1.png` from `references/characters/루루.png`
  - `reference_assets/lulu_special_hairpin_composite_contact_sheet_v1.png` for QA comparison
- Updated `batch_1_prompt_plan.md` to use `lulu_official_no_bag_special_hairpin_composite_v1.png` instead of the rejected generated Lulu file.
- Rejected/unused: `reference_assets/lulu_wearing_special_coral_hairpin_ref_v1.png`.

## Reference-Image Generation Retry - 2026-06-24

- User feedback: local composite looked awkward; preferred generating with the official Lulu reference image uploaded/visible as input reference.
- Generated a new candidate using the official Lulu no-bag reference as the identity/source image and the special hairpin image as the prop/source image.
- Saved candidate:
  - `reference_assets/lulu_refimage_special_hairpin_candidate_v1.png`
- Status: candidate only, not promoted to batch plan yet. User QA needed because model-based generation can still drift from official Lulu even when reference-guided.
- Current batch plan still points to the official-base composite until user approves this candidate or requests another retry.

## Reference Strategy Adjustment - 2026-06-24

- User observed that today's generation is not respecting reference images well enough.
- Decision: stop chasing a pre-made Lulu-wearing-hairpin reference for now.
- Batch 1 plan now uses official Lulu/no-bag Lulu plus the standalone `special_coral_hairpin_ref_v1.png` as separate inputs instead of relying on generated or composite wearing-Lulu references.
- Wearing-Lulu generated/composite files remain preserved as history only; do not use them as source-of-truth without explicit user approval.
- Cleanup correction: removed all pre-made wearing-Lulu reference paths from `batch_1_prompt_plan.md`; generation inputs now rely on official Lulu/no-bag Lulu plus the standalone hairpin only.

## Batch 1 Cover Candidate - 2026-06-24

- Generated cover candidate with built-in image generation:
  - `batch_1/00_candidate_text_v1.png`
- Prompt used official-character locks by prose plus standalone special hairpin reference design; no pre-made wearing-Lulu reference was used.
- Initial assistant QA from visible output:
  - Text appears close/readable: `수아의 잘 보는 눈` and `— 다 똑같지 않아서 좋아요 —`.
  - Special hairpin reads as a mint/cream loose prop in the sand.
  - Needs user QA for Sua/Lulu official-reference fidelity before any final promotion.
- Status: candidate only, not final-promoted.

## Reference Input Clarification - 2026-06-24

- Important correction: the built-in `image_gen` calls in this thread only received a text prompt. Local reference image paths were listed in prompt plans and some images were displayed in chat, but the image generation tool call itself did not include a separate structured image-input attachment field.
- Therefore `00_candidate_text_v1.png` should be treated as generated from prose locks and weak/ambient visible context, not as a fully reference-attached generation from the official PNG files.
- Next attempt should not claim official reference fidelity unless the actual reference images are attached through a generation path that supports image inputs, or the result is manually QAed against the official PNGs.

## Node-Emitted Reference Retry - 2026-06-24

- Correction: for this retry, the official Lulu no-bag PNG and standalone special hairpin PNG were emitted into the chat context with `nodeRepl.emitImage` before calling the built-in `image_gen` tool.
- Generated and saved candidate:
  - `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- Source references emitted:
  - `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
  - `reference_assets/special_coral_hairpin_ref_v1.png`
- File check: 1122x1402 RGB PNG, 1,990,211 bytes.
- Assistant QA: much closer to official Lulu than the rejected generated/composite attempts; hairpin reads as mint/aqua coral with cream star-shell and pale-yellow beads.
- Status: candidate only, not promoted to batch plan or final use until user QA approves it.

## User Approval - Lulu Wearing Hairpin - 2026-06-24

- User approved `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png` with feedback: "아 이거거든 / 바로이거다".
- Promoted this file from QA candidate to approved Lulu-wearing-special-hairpin reference.
- Updated batch 1 cover planning to generate a new cover candidate as `batch_1/00_candidate_text_v2.png`, using node-emitted references before generation.

## Batch 1 Cover Candidate v2 - 2026-06-24

- Generated cover candidate after user approved `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png` as the Lulu-wearing-special-hairpin reference.
- Before generation, emitted actual reference PNGs into chat context with `nodeRepl.emitImage`:
  - official Sua: `series/coral-town-daycare/references/characters/수아.png`
  - approved Lulu wearing hairpin: `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
  - standalone loose hairpin: `reference_assets/special_coral_hairpin_ref_v1.png`
  - official Banguli: `series/coral-town-daycare/references/characters/방울이.png`
  - official playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Saved candidate:
  - `batch_1/00_candidate_text_v2.png`
- File check: 1055x1491 RGB PNG, 2,869,832 bytes.
- Assistant visual QA from generated output: A5 portrait cover composition, Sua foreground focus, Lulu secondary, loose mint/cream hairpin visible in sand, title/subtitle appear readable and close to exact.
- Status: candidate only; needs user QA before final promotion.

## Cover Continuity Correction - 2026-06-24

- User QA caught a major continuity issue in `batch_1/00_candidate_text_v2.png`: Lulu was still wearing the special hairpin while the same hairpin also appeared loose in the sand.
- Root cause: the approved Lulu-wearing reference was included for the cover, causing duplicate special hairpins.
- Corrective plan for v3: do not emit/use the approved Lulu-wearing reference for the cover. Use official Lulu/no-bag only for identity, and lock the special mint/aqua star-shell hairpin as a single loose foreground prop in sand.
- Planned new candidate: `batch_1/00_candidate_text_v3.png`.

## Batch 1 Cover Candidate v3 - 2026-06-25

- Generated continuity-fix cover candidate after user QA flagged duplicate hairpin logic in v2.
- Rejected/hold: `batch_1/00_candidate_text_v2.png` because Lulu wore the special hairpin while the same hairpin appeared loose in the sand.
- For v3, emitted actual references with `nodeRepl.emitImage` and intentionally did not emit the approved Lulu-wearing reference:
  - official Sua: `series/coral-town-daycare/references/characters/수아.png`
  - official Lulu no-bag for identity only: `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
  - standalone special hairpin as the only lost prop: `reference_assets/special_coral_hairpin_ref_v1.png`
  - official Banguli: `series/coral-town-daycare/references/characters/방울이.png`
  - official playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Saved candidate:
  - `batch_1/00_candidate_text_v3.png`
- File check: 1054x1492 RGB PNG, 2,915,604 bytes.
- Assistant visual QA from generated output: the loose special hairpin appears once in the foreground sand; Lulu is secondary and does not visibly wear the special mint/aqua star-shell hairpin; title/subtitle appear readable.
- Status: candidate only; needs user QA before final promotion.

## Page 01 Candidate v1 Rejected - 2026-06-25

- User QA caught a rulebook violation in `batch_1/01_candidate_text_v1.png`: Aru was drawn with a human-like body, hands, and feet.
- This violates the Aru rule: keep Aru as a round pufferfish body and do not add human hands, human feet, or a separate body/torso.
- Rejected/hold: `batch_1/01_candidate_text_v1.png`.
- Corrective plan for v2: remove Aru from page 01 because the page text only says friends gathered and does not name Aru. Use Jun-i, Mongle, and Tori around Lulu instead.
- Planned new candidate: `batch_1/01_candidate_text_v2.png`.

## Page 01 Candidate v2 Held - 2026-06-25

- Saved `batch_1/01_candidate_text_v2.png` after removing Aru.
- Assistant QA caught another batch-rule issue before promotion: classroom/free-play characters still appeared to wear bags/straps, especially around Mongle/Tori.
- Hold: `batch_1/01_candidate_text_v2.png`.
- Corrective plan for v3: use no-bag references for Sua, Jun-i, Mongle, and Tori; continue using approved Lulu-with-special-hairpin reference; keep Aru excluded; lock all child-worn bags/straps out of the scene.
- Planned new candidate: `batch_1/01_candidate_text_v3.png`.

## Page 01 Candidate v3 - 2026-06-25

- Generated no-bag retry for page 01 after v1 failed Aru anatomy and v2 showed child-worn bags/straps.
- References emitted with `nodeRepl.emitImage` before generation:
  - approved Lulu wearing special hairpin: `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
  - no-bag Sua: `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
  - no-bag Jun-i: `series/coral-town-daycare/references/characters/no_bag/준이_no_bag.png`
  - no-bag Mongle: `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
  - no-bag Tori: `series/coral-town-daycare/references/characters/no_bag/토리_no_bag.png`
  - Banguli: `series/coral-town-daycare/references/characters/방울이.png`
  - classroom: `series/coral-town-daycare/references/배경_교실.png`
- Saved candidate:
  - `batch_1/01_candidate_text_v3.png`
- File check: 1054x1492 RGB PNG, 2,861,058 bytes.
- Assistant visual QA from generated output: Aru/pufferfish child is absent; no obvious child-worn bags/straps; Lulu's special hairpin appears on Lulu only; needs user QA for exact Korean text and character fidelity before promotion.
- Status: candidate only.

## Page 01 Candidate v3 Held - 2026-06-25

- User QA caught that the bag/prop ban in v3 over-applied and removed fixed character clothing/accessories: Mongle lost his yellow beret and Tori lost his yellow hat.
- Hold: `batch_1/01_candidate_text_v3.png`.
- Root cause: prompt phrasing treated worn props too broadly; model removed fixed hats while following the bag ban.
- Corrective plan for v4: narrow the ban to bags/straps only, and explicitly preserve Mongle's yellow beret and Tori's yellow hat/helmet and turtle shell.
- Planned new candidate: `batch_1/01_candidate_text_v4.png`.

## Page 01 Candidate v4 - 2026-06-25

- Generated and saved `batch_1/01_candidate_text_v4.png` after user QA caught that the v3 bag/prop ban removed fixed character hats.
- A first v4 generation attempt drifted into an unrelated infographic/reference-sheet direction and was not saved as a candidate.
- Corrective generation approach: reduced the reference set and used a shorter prompt focused on a single storybook scene, not a reference sheet or infographic.
- References emitted with `nodeRepl.emitImage` before the successful generation:
  - approved Lulu wearing special hairpin: `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
  - no-bag Sua: `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
  - no-bag Mongle: `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
  - no-bag Tori: `series/coral-town-daycare/references/characters/no_bag/토리_no_bag.png`
  - Banguli: `series/coral-town-daycare/references/characters/방울이.png`
  - classroom: `series/coral-town-daycare/references/배경_교실.png`
- File check: 1024x1536 RGB PNG, 3,148,897 bytes.
- Assistant visual QA from saved output: Aru/pufferfish child is absent; Mongle keeps the yellow beret and sailor collar; Tori keeps the yellow hat/helmet and turtle shell; no obvious child-worn bag straps on Sua/Lulu/Mongle; Lulu's special hairpin appears once on Lulu's head and not loose elsewhere; Korean story text appears readable and close to exact.
- Status: candidate only; needs user QA before final promotion.
