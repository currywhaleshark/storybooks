# Episode Worklog - 몽글이의 식탁 춤

## Source

- Drive source: `https://drive.google.com/file/d/1-X0NirjhHy9w9EqpJYtqmiScTwibZ6UP/view?usp=drivesdk`
- Downloaded local copy: `monggle table manners prompts.md`
- Series script copy: `series/coral-town-daycare/docs/episodes/몽글이의_식탁_춤.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Page plan: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21/page_plan.md`
- Work root: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21`
- Final folder: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/final`

## Script Intake - 2026-06-21

- File title: `monggle table manners prompts.md`
- Episode title: `몽글이의 식탁 춤`
- Subtitle: `밥 먹을 땐 다리를 가지런히`
- Structure: cover + 12 story pages.
- Core story: Mongle's lively legs cause a small mealtime spill; Mari teacher validates the energy, then teaches that legs gather during meals and dance freely afterward.
- Exact page text extracted into `page_plan.md`.

## Reference Audit

- Official references available:
  - `series/coral-town-daycare/references/배경_식당.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/포포.png`
- Missing required references: none for the current script.
- No episode-specific prop reference is required before generation. Rice balls, soup bowl, water cup, cloth, and shell table can be generated from the dining-room rulebook plus prompt.

## User QA Locks

- Use `산호마을 어린이집 이미지 규칙서` above the source prompt whenever they conflict.
- Do not use prior generated images from other episodes as visual references.
- Dining-room pages should not show children wearing bags. The source prompt includes bag descriptions in some character blurbs, but the official rulebook says indoor eating scenes omit worn bags unless explicitly needed.
- The spill is small, safe, and not frightening. Nobody is hurt.
- Mongle's liveliness is not framed as bad behavior. Mari validates the energy before giving the table-manners rule.
- Korean text must be exact and readable. If the generator fails the text but the illustration is good, preserve the illustration candidate for text repair instead of silently replacing it.

## Batch Status

- Script copied into series docs:
  - `series/coral-town-daycare/docs/episodes/몽글이의_식탁_춤.md`
- Work folder created:
  - `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21`
- Final folder created:
  - `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/final`
- Page plan prepared:
  - `work_2026-06-21/page_plan.md`
- Batch 1 prepared:
  - `work_2026-06-21/batch_1/batch_1_prompt_plan.md`
- Generation status:
  - Not started.

## Next Step

- Start Batch 1 one page at a time: cover, page 01, page 02, page 03.
- Before each generation, attach the actual official references listed in the batch plan.
- QA each candidate for character identity, exact Korean text, indoor no-bag lock, safe mealtime tone, and no contamination from old generated images.

## Batch 1 Cover Candidate

- Generated:
  - `work_2026-06-21/batch_1/00_cover_candidate_v1.png`
- QA:
  - Current review candidate.
  - Mongle keeps the official purple octopus identity, yellow beret, sailor collar, and visible excited tentacle motion.
  - Banguli remains a pale transparent droplet with small companion bubbles.
  - Dining-room background reads as Coral Town Daycare and no child is wearing a bag indoors.
  - Korean title/subtitle are readable and close to the approved cover text. User visual QA should still check the bottom subtitle at mobile size before final promotion.

## Batch 1 Page 01 Candidates

- Generated:
  - `work_2026-06-21/batch_1/01_candidate_text_v1.png`
  - `work_2026-06-21/batch_1/01_candidate_text_v2.png`
  - `work_2026-06-21/batch_1/01_candidate_text_v2_textfix_v1.png`
  - `work_2026-06-21/batch_1/01_candidate_text_v2_textfix_v2.png`
  - `work_2026-06-21/batch_1/01_candidate_text_v2_textfix_v2_preview.jpg` (QA preview only)
- QA:
  - `01_candidate_text_v1.png`: hold/reject for text; first line rendered as `정심 시간이에요.` instead of `점심 시간이에요.`.
  - `01_candidate_text_v2.png`: hold for text repair; stronger composition and character fidelity than v1, but first line still rendered as `정심 시간이에요.`.
  - `01_candidate_text_v2_textfix_v1.png`: reject; exact text overlay was too large and covered Mongle's face/hat area, with ghosted old text still visible.
  - `01_candidate_text_v2_textfix_v2.png`: current review candidate. First line was locally repaired to `점심 시간이에요.` while preserving v2's composition. Remaining text appears readable and story-correct.
  - Visual notes: Mongle remains central with visible excited legs, Mari teacher is warm and on-reference enough, Banguli remains a droplet, supporting children are not wearing bags indoors.

## Batch 1 Page 02 Candidate

- Generated:
  - `work_2026-06-21/batch_1/02_candidate_text_v1.png`
- QA:
  - Current review candidate.
  - Text is readable and appears story-correct.
  - Mongle's one leg reaches toward the table, another taps the chair, and the body language reads as delighted restlessness.
  - Dining-room setting and no-body-worn-bags lock are respected.

## Batch 1 Page 03 Candidate

- Generated:
  - `work_2026-06-21/batch_1/03_candidate_text_v1.png`
- QA:
  - Current review candidate.
  - Text is readable and appears story-correct.
  - Food-play action reads clearly: rice ball rolling and seaweed soup being stirred.
  - The actual spill is not shown yet, preserving page 04 continuity.
  - Mari approaches gently; Aru/Sua react with concern, not shame.
  - No body-worn bags indoors.

## Batch 1 Current Review Set

- Cover: `00_cover_candidate_v1.png`
- Page 01: `01_candidate_text_v2_textfix_v2.png`
- Page 02: `02_candidate_text_v1.png`
- Page 03: `03_candidate_text_v1.png`

## User QA - Batch 1 Rework Direction

- Cover accepted: keep `00_cover_candidate_v1.png`.
- Do not add local text panels or post-generation text overlays for this pass. User will QA text.
- Page 01 issues:
  - Aru became snowman-like instead of one round pufferfish body.
  - Sua and Lulu drifted from official references.
- Page 02 issues:
  - Dining table layout changed from page 01.
  - Aru gained hands.
  - Lulu details drifted from official reference.
- Page 03 issues:
  - Aru gained hands.
  - Sua details drifted from official reference.
- Rework focus:
  - Character reference fidelity first, especially Aru/Sua/Lulu.
  - Table placement and dining setup consistency across pages 01-03.
  - Keep indoor no-bag lock.
- Rework plan:
  - `work_2026-06-21/batch_1/batch_1_rework_prompt_plan.md`
  - New candidates should use suffix `_reflock`.

## Rework Generation Results - 2026-06-21

- `01_candidate_text_v3_reflock.png`: generated; hold. Aru/Sua/Lulu improved, but several children still wore reference-derived bags in the dining-room scene.
- `01_candidate_text_v4_reflock_nobag.png`: current page 01 review candidate. No visible worn bags; Aru remains a round pufferfish body without hands; Sua/Lulu retain seahorse silhouettes.
- `02_candidate_text_v2_reflock.png`: current page 02 review candidate. Table setup simplified and stable; Aru has no hands; Lulu is closer to official seahorse reference.
- `03_candidate_text_v2_reflock.png`: current page 03 review candidate. Same central table direction; Aru has no hands; Sua is closer to official seahorse reference.
- Text QA intentionally deferred to user. No local text panel overlays were added.

## No-Bag Reference Rework Stop Notes - 2026-06-22

- Session stopped because the image-generation context began drifting/contaminating page 03. Do not continue from the last generated context; restart a fresh generation context for the next attempt.
- New no-bag indoor references were prepared under `series/coral-town-daycare/references/characters/no_bag/`, including the reworked eyeless Popo reference.
- Saved no-bag-reference candidates:
  - `01_candidate_text_v5_nobagref_v1.png`: hold/review. Character references improved, but Mongle is already up on/over the table from page 01. Next page 01 attempt should keep Mongle entering, beside the table, or at the chair rather than already climbing onto the tabletop.
  - `02_candidate_text_v3_nobagref_v1_hold_aru_spoon.png`: hold/reject. Aru appears to hold a spoon/utensil, reintroducing a hand-like failure.
  - `02_candidate_text_v3_nobagref_v2.png`: hold/review. Aru is improved, but Mari teacher appears seated/eating with the children. For page 02, Mari should not be seated at the dining place or eating with the class; she should be absent from the seats, supervising, serving, or off-frame.
  - `03_candidate_text_v3_nobagref_v1_hold_popo_eyes.png`: hold/reject. Popo gained visible eyes, which breaks the eyeless Popo reference. The issue is Popo's reference drift, not Popo's presence.
- Continuity correction from user: page 01 establishes all friends seated at the dining table. Pages 02 and 03 continue the same mealtime scene, so all friends should remain seated at their places in both pages, even when the page-specific prompt only names Aru/Sua/Lulu for reference QA. Do not remove Popo or any other seated friend solely because they are not named in the page text.
- Next attempt should restart batch 1 in a clean image-generation context, using no-bag references positively and treating the seated-friends layout as continuous across pages 01, 02, and 03, while fixing Mongle's page 01 table position and Mari's page 02 placement.

## Batch 1 Continuity Rework Results - 2026-06-22

- Fresh generation context used with the actual dining-room reference and no-bag indoor character reference sheets shown in-session before generation.
- Cover kept:
  - `work_2026-06-21/batch_1/00_cover_candidate_v1.png`
- New continuity candidates generated and saved:
  - `work_2026-06-21/batch_1/01_candidate_text_v6_nobagref_continuity_v1.png`
  - `work_2026-06-21/batch_1/02_candidate_text_v4_nobagref_continuity_v1.png`
  - `work_2026-06-21/batch_1/03_candidate_text_v4_nobagref_continuity_v1.png`
- QA notes:
  - Page 01: all friends are seated at the table; Mongle is kept at/near his place instead of on the tabletop. User should still QA exact Korean text and whether Mongle reads clearly enough as arriving/settling beside his seat.
  - Page 02: all friends remain seated; Mari teacher is standing/serving/supervising rather than seated and eating with the children.
  - Page 03: all friends remain seated, including Popo. Popo presence is allowed; QA focus is avoiding visible black eyes and preserving the eyeless translucent moon-jelly reference.
  - Text QA remains deferred to user. No local text panels or post-generation opaque overlays were added.
- Google Drive mobile review folder:
  - `https://drive.google.com/drive/folders/1xdFFOmV_AqLSOWAxYiCinQDDpq7Fg1Xy`
- Uploaded files:
  - Cover: `https://drive.google.com/file/d/10_8AbLU5TdsJ_b_zNERsWw1jbS_5xqQg/view?usp=drivesdk`
  - Page 01: `https://drive.google.com/file/d/1UtlCbABzsG_0xRnmxtb6Xlyp0bRrjx2c/view?usp=drivesdk`
  - Page 02: `https://drive.google.com/file/d/1Fg6B7NgEt2Tg-y1vYUYYIHaHPvEQUzas/view?usp=drivesdk`
  - Page 03: `https://drive.google.com/file/d/1zB2puObiC3kFZ1J5h6gC936iImtCTgte/view?usp=drivesdk`
## User QA - Fixed Seating Problem - 2026-06-22

- User QA: reference fidelity is good, but children change seats from page to page.
- Diagnosis: the previous continuity pass improved no-bag/reference fidelity but did not lock table blocking strongly enough.
- New fixed seating map created:
  - `work_2026-06-21/batch_1/batch_1_fixed_seating_map_v1.png`
- Fixed seat assignments for pages 01-03:
  - Mongle: front-left seat, closest to reader.
  - Aru: front-right seat.
  - Lulu: right-middle seat.
  - Sua: back-right seat.
  - Popo: back-center seat.
  - Jun-i: back-left seat.
  - Tori: left-middle seat.
  - Banguli: floating near Mongle, no seat.
  - Mari teacher: standing/serving/supervising near the back/right service area, not seated with children.
- Rework plan:
  - `work_2026-06-21/batch_1/batch_1_fixed_seating_rework_prompt_plan.md`
- Next generation should preserve the good reference fidelity from the previous pass, but lock the seat map across page 01, page 02, and page 03.
## Batch 1 Fixed-Seating Rework Results - 2026-06-22

- User flagged that reference fidelity was good, but children changed seats page by page.
- A fixed seating map was created first:
  - `work_2026-06-21/batch_1/batch_1_fixed_seating_map_v1.png`
- New local candidates saved:
  - `work_2026-06-21/batch_1/01_candidate_text_v7_fixedseats_v1.png`
  - `work_2026-06-21/batch_1/02_candidate_text_v5_fixedseats_v1.png`
  - `work_2026-06-21/batch_1/03_candidate_text_v5_fixedseats_v1_fail_seat_drift.png`
  - `work_2026-06-21/batch_1/03_candidate_text_v6_fixedseats_page02edit_v1.png`
- QA notes:
  - Page 01 and page 02 now share a much more stable practical seating order: Mongle front/near side, Tori left/front, Aru right/front, Jun-i back-left, Popo back-center, Sua back-right, Lulu right side, Mari standing at the back/right service area.
  - `03_candidate_text_v5_fixedseats_v1_fail_seat_drift.png` failed because Jun-i moved to the front and the seating order drifted again. It is saved for process history only and was not uploaded for review.
  - `03_candidate_text_v6_fixedseats_page02edit_v1.png` was created by editing the page 02 candidate so the table, camera, and seating order are preserved while changing the action/text toward page 03.
  - Text QA is still needed. Page 02 has visible text issues from generation; do not promote to final without user text approval or a later text repair pass.
- Google Drive mobile review folder for fixed-seat candidates:
  - `https://drive.google.com/drive/folders/199G9BFTj3v7Nggat1ealPRvPShEa3dUr`
- Uploaded files:
  - Cover: `https://drive.google.com/file/d/1iONAXtorcc2ub1Kv04RuyEr9Hnpq_Z8E/view?usp=drivesdk`
  - Page 01: `https://drive.google.com/file/d/12HhFUDtMsg7jJm-Dygm6GOUziiQayW6o/view?usp=drivesdk`
  - Page 02: `https://drive.google.com/file/d/19m0tM3UiaaVd6Ss8MC7AIzIIkJsPuQnJ/view?usp=drivesdk`
  - Page 03: `https://drive.google.com/file/d/1cd1APGhVsa9kyKbT966KcPj-MokJOA4i/view?usp=drivesdk`
## User QA - Popo Eyes, Tentacles, Spoon Prop - 2026-06-22

- User QA: pages 01 and 03 still have issues with Popo's eye depiction and hand-like anatomy.
- Lock correction:
  - Popo should remain an essentially eyeless translucent moon jellyfish. Avoid black dot eyes, pupils, anime eyes, or a humanlike face. Expression should come from a tiny mouth, blush, dome tilt, or internal markings.
  - Any appendages on Popo should read as soft jellyfish tentacles/frills, not hands, fingers, arms, or mitten shapes.
- Spoon/utensil note:
  - The spoon shape is high risk when it is tiny or held by a tentacle; the generator tends to collapse it into a hand-like shape, stick, or malformed utensil.
  - Preferred next-pass solution: do not make any child or tentacle hold a spoon. Put spoons as simple, larger, clearly separate table props: resting beside bowls, lying on shell plates, or leaning inside the soup bowl.
  - For page 03, Mongle can stir soup directly with a tentacle tip or nudge a spoon that is already resting in the bowl; avoid a gripping pose.
  - If a visible spoon is mandatory, create a simple spoon prop reference first and use it as a separate visual reference, then QA the prop in a small edit pass.
- Do not treat spoon distortion as unavoidable, but treat held utensils as a separate prop/anatomy risk rather than a normal page-generation detail.
## Batch 1 A5 No-Held-Spoon Rework Results - 2026-06-22

- User correction before this pass:
  - Do not use local text-overlay/text-panel compositing. Prior local text overlays have not worked well enough.
  - Include the Korean story text directly in the generated image, as in prior usable candidates.
  - Restore A5 portrait page ratio and avoid landscape/subtitle-style layout.
- New generation constraints applied:
  - A5 portrait page ratio, approximately 1054 x 1492.
  - Generated in-image Korean story text included from the first pass.
  - Text requested as an integrated cream/white picture-book narration panel, not a subtitle strip.
  - One same round shell table and the fixed seating order carried across pages 01, 02, and 03.
  - No child, fin, tentacle, frill, hand, or arm holds a spoon/utensil. Utensils may be omitted or appear only as separate resting table props.
  - Popo locked as an essentially eyeless translucent moon jellyfish with soft tentacles/frills only; no black dot eyes, pupils, hands, fingers, arms, or mitten shapes.
- New local candidates saved:
  - `work_2026-06-21/batch_1/01_candidate_text_v8_a5_noheldspoon_v1.png`
  - `work_2026-06-21/batch_1/02_candidate_text_v6_a5_noheldspoon_v1.png`
  - `work_2026-06-21/batch_1/03_candidate_text_v7_a5_noheldspoon_v1.png`
- Technical verification:
  - All three new page candidates are 1054 x 1492 px.
  - Google Drive folder readback confirmed four uploaded PNG files: cover plus pages 01-03.
- QA notes:
  - This pass corrects the previous aborted landscape/subtitle-style failure.
  - Text is generated in-image and still needs visual Korean text QA by the user before promotion.
  - Spoon shape cleanup is intentionally deferred unless a later edit/prop-reference pass becomes necessary.
- Google Drive mobile review folder:
  - `https://drive.google.com/drive/folders/15fAD17A96yF-_GMhTtGcYf1uo5elNjBP`
- Uploaded files:
  - Cover: `https://drive.google.com/file/d/1c7Dit2IKwDg1S0L9NKwAh7nNf26l5bZZ/view?usp=drivesdk`
  - Page 01: `https://drive.google.com/file/d/1xTi6asael4gCTGCoXnLc6r-WdGYe3Uh8/view?usp=drivesdk`
  - Page 02: `https://drive.google.com/file/d/1ZkgXL8AdrjjmjlVMZqYoQ9GHO5-YHQX8/view?usp=drivesdk`
  - Page 03: `https://drive.google.com/file/d/13ktmA2iKgZ0gRMi_zczHrJ5MsF6X97gN/view?usp=drivesdk`
## Page 03 Targeted Correction - Mongle Hat and Aru Hands - 2026-06-22

- User QA after A5 no-held-spoon pass:
  - Pages 01 and 02 are good.
  - Page 03 table shape had drifted from the round table in one attempt.
  - Follow-up correction: Mongle's hat changed, and Aru's hand-like appendages should be removed. Fix only those details.
- Targeted edit constraints:
  - Preserve page 03 composition, A5 portrait ratio, round table, seating, food-play action, narration panel, and text.
  - Restore Mongle's official small yellow beret.
  - Remove Aru's hand/arm/finger-like shapes; keep Aru as a round pufferfish with fins only.
- New local candidate saved:
  - `work_2026-06-21/batch_1/03_candidate_text_v8_a5_noheldspoon_roundtable_hat_aru_v1.png`
- Technical verification:
  - New page 03 candidate is 1054 x 1492 px.
  - Google Drive folder readback confirmed the uploaded new page 03 file.
- Google Drive upload:
  - Page 03 corrected: `https://drive.google.com/file/d/1TnF09eKfTFziWqkpEgbvdgV-LYr7Brd6/view?usp=drivesdk`
## Batch 2 Handoff Prepared - 2026-06-22

- Handoff file created:
  - `work_2026-06-21/batch_2/batch_2_handoff.md`
- Batch 1 carry-forward review state:
  - Cover candidate kept: `work_2026-06-21/batch_1/00_cover_candidate_v1.png`
  - User said pages 01 and 02 are good:
    - `work_2026-06-21/batch_1/01_candidate_text_v8_a5_noheldspoon_v1.png`
    - `work_2026-06-21/batch_1/02_candidate_text_v6_a5_noheldspoon_v1.png`
  - Latest page 03 candidate after targeted correction:
    - `work_2026-06-21/batch_1/03_candidate_text_v8_a5_noheldspoon_roundtable_hat_aru_v1.png`
- Batch 2 scope:
  - Page 04: small safe spill when Mongle bumps the soup bowl.
  - Page 05: everyone pauses; Mongle shrinks inward; Mari checks whether anyone is hurt.
  - Page 06: Mari and Mongle clean together; friends help gently.
- Carry-forward locks for batch 2:
  - A5 portrait, generated in-image Korean text, no local text overlay.
  - One same round shell table; no table-shape drift or multiple tables.
  - Use no-bag indoor references and preserve fixed seating continuity from pages 01-03.
  - Mongle must keep the yellow beret and eight soft tentacles; no human feet or hand-like tentacles.
  - Aru must remain fins-only with no hand/arm/finger-like appendages.
  - Popo must remain essentially eyeless with jellyfish tentacles/frills only.
  - No held utensils; batch 2 does not need visible spoons.
  - Spill is cute/safe/small; no injuries, scary splash, dirty mess, scolding, or shaming.
- First next action:
  - Start batch 2 in a fresh image-generation context, attach the actual reference images, and generate page 04 first with exact text included.
## Batch 2 Seat-Locked Generation Results - 2026-06-22

- Batch 2 generated locally for pages 04-06 using the actual official references, the fixed seating map, and the accepted/active pages 01-03 as layout-only continuity references.
- User caught an early page 04 issue:
  - The first generation changed the seating arrangement.
  - Root-cause note: generating page 04 from scratch caused the model to reconstruct the table layout despite the seating map.
  - Correction: page 04 and later pages were made by editing the previous accepted page image so camera, table, and seats stayed locked.
- Failed or superseded page 04 candidates kept for process history only:
  - `work_2026-06-21/batch_2/04_candidate_text_v1_fail_seat_drift.png`
  - `work_2026-06-21/batch_2/04_candidate_text_v2_fail_seat_drift.png`
  - `work_2026-06-21/batch_2/04_candidate_text_v3_page03edit_seatlock_v1.png` - seat lock improved, but text needed correction.
  - `work_2026-06-21/batch_2/04_candidate_text_v4_page03edit_seatlock_textfix_v1.png` - superseded by a clearer text correction.
- Current local review candidates:
  - `work_2026-06-21/batch_2/04_candidate_text_v5_page03edit_seatlock_textfix_v2.png`
  - `work_2026-06-21/batch_2/05_candidate_text_v1_page04edit_seatlock_v1.png`
  - `work_2026-06-21/batch_2/06_candidate_text_v1_page05edit_seatlock_v1.png`
- Technical verification:
  - Pages 04, 05, and 06 current review candidates are all 1054 x 1492 px.
- QA notes:
  - Seating continuity is much stronger after switching to previous-page edit workflow.
  - Page 04 keeps the same round table and small safe spill; `국그릇을 / 툭!` and `물컵도 / 톡!` were explicitly corrected.
  - Page 05 keeps the spill aftermath small and non-scolding; Mari checks safety first.
  - Page 06 shows warm cleanup with soft cloths/towels; no held utensils are intended.
  - Aru remains fins-only enough for review, Popo remains essentially eyeless, and Mongle keeps the yellow beret.
  - Final Korean text QA by the user is still needed before promotion to `final`.
- Google Drive:
  - Not uploaded yet in this session. Upload the three current local review candidates only after user approval to send them to Drive.
- Next handoff:
  - `work_2026-06-21/batch_3/batch_3_handoff.md`
