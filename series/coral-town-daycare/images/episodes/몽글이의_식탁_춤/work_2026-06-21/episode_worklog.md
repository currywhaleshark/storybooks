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
  - `03_candidate_text_v3_nobagref_v1_hold_popo_eyes.png`: hold/reject. Popo was pulled into the scene and gained visible eyes; page 03 should not include Popo unless explicitly needed.
- Continuity note from user: because all friends are seated in page 01, later dining-room pages should naturally keep the friends seated at the table even when every friend's name is not listed in the page-specific prompt. Do not remove seated friends solely because the prompt only names Aru/Sua/Lulu for reference QA.
- Next attempt should restart batch 1 in a clean image-generation context, using no-bag references positively and treating page 01's seated-friends layout as continuity, while fixing Mongle's page 01 table position and Mari's page 02 placement.
