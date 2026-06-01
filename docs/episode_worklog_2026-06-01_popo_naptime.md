# Episode Worklog - Popo Naptime Story

## Purpose

Continue the episode across sessions without carrying generated images in chat history. Record file paths, candidate status, QA notes, rejected files, and next steps only.

## Source Script

- Script: `series/coral-town-daycare/docs/episodes/popo_naptime_story_prompts.md`
- Series: `series/coral-town-daycare`
- Episode title: `포포는 안 졸려!`
- Subtitle/theme: `낮잠은 신나게 놀 힘을 모으는 시간`
- Core message: `잘 쉬니까 더 신나게 놀 수 있어요`

## Official References

Use actual image files as visual truth. Do not infer character, location, text-panel, or prop appearance from prose alone when a reference exists.

- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Character references:
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/토리.png`
- Background references:
  - `series/coral-town-daycare/references/배경_낮잠방.png`
  - `series/coral-town-daycare/references/배경_교실.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`

## Output Plan

- Work folder: `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01`
- Final folder: `series/coral-town-daycare/images/episodes/포포는_안_졸려/final`
- Final naming:
  - `00_표지.png`
  - `01_페이지.png` through `12_페이지.png`
- Candidate naming:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`, etc.

## Page Plan

| File | Page | Scene | Main refs |
| --- | --- | --- | --- |
| `00_표지.png` | Cover | Popo awake and excited in the cozy nap room while friends sleep | Popo, Banguli, nap room |
| `01_페이지.png` | 1 | Lunch is over; Mari teacher begins nap time and friends settle in | Mari, all children, nap room |
| `02_페이지.png` | 2 | Popo cannot sleep; Banguli gently invites Popo to rest | Popo, Banguli, nap room |
| `03_페이지.png` | 3 | Popo quietly plays alone in the nap room | Popo, Banguli, nap room |
| `04_페이지.png` | 4 | Nap time ends; friends wake refreshed while Popo acts energetic | Mari, all children, nap room |
| `05_페이지.png` | 5 | Afternoon floating game begins brightly | Mari, all children, classroom/playground |
| `06_페이지.png` | 6 | Popo gradually becomes sleepy during play | Popo, friends, classroom/playground |
| `07_페이지.png` | 7 | Popo cannot float highest like usual | Popo, friends, classroom/playground |
| `08_페이지.png` | 8 | Mari teacher notices Popo is struggling | Mari, Popo, Banguli |
| `09_페이지.png` | 9 | Mari explains that naps gather strength for afternoon play | Mari, Popo, Banguli |
| `10_페이지.png` | 10 | Popo rests softly on the cushion with Banguli nearby | Mari, Popo, Banguli, nap room |
| `11_페이지.png` | 11 | Next day, Popo chooses to settle first for nap | Popo, Banguli, Mari, nap room |
| `12_페이지.png` | 12 | After a good nap, Popo floats highest and shines gently | Popo, friends, Mari, Banguli, classroom/playground |

## Production Batches

- Batch 1: reference QA, output folder setup, cover + pages 1-3.
- Batch 2: pages 4-7.
- Batch 3: pages 8-12 and final QA.

Work one batch at a time. Do not generate Batch 2 until Batch 1 has QA notes and user approval or targeted retry instructions.

## Carry-Forward Visual Locks

- Popo must follow the official moon-jellyfish reference: pale sky-blue translucent rounded bell, moon-jellyfish flower pattern inside the bell, scalloped bell edge, soft thin tentacles, sailor collar, beige bag only when the scene calls for it.
- Popo's translucent bell itself is Popo's face. Do not draw a separate head, face, or body under the bell. A small mouth belongs on the front of the bell; eyes are hidden or barely visible through the bell.
- Popo's eyes should stay hidden or mostly hidden under the bell. Express emotion through the small mouth, bell height/roundness, and tentacle movement.
- Do not turn Popo into Banguli, a simple droplet, a hard glass orb, a child with hair, or a character with human arms/legs.
- Banguli must remain a separate tiny pale-blue water droplet mascot with a simple face and two or three small water droplets.
- The nap room must stay warm and cozy, not dark, scary, deep-sea, or overly blue. Keep shell beds/cushions, soft curtains, warm lamps, rounded windows, and pastel watercolor texture.
- Do not shame Popo. Sleepiness and frustration should stay gentle, warm, and age-appropriate.
- Avoid extra signage, pseudo-writing, random labels, speech bubbles, neon highlights, or glossy 3D toy rendering.
- Bags should appear only when appropriate to the scene; in sleeping/resting pages, avoid drawing bags as active props unless they are part of the official character reference and unobtrusive.

## Current Status

- Script inspected.
- Official character and background reference files found.
- Popo, Banguli, Mari teacher, and nap room references visually inspected.
- Updated the official nap room reference to remove old-version sleeping characters:
  - Backup of previous version: `series/coral-town-daycare/references/배경_낮잠방_backup_before_characterless_2026-06-01.png`
  - Current official version: `series/coral-town-daycare/references/배경_낮잠방.png`
  - QA note: current version is a character-free nap room background with empty shell beds/cushions, warm lamps, curtains, shelves, and no sleeping children or character-like toys.
- Episode work and final folders created.
- Batch 1 prompt/reference plan created:
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_1/batch_1_prompt_plan.md`

## Next Session Handoff

- Batch 1 is user approved and promoted to `final`.
- Approved final files:
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/00_표지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/01_페이지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/02_페이지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/03_페이지.png`
- Batch 2 should start in a fresh session with pages 4-7 only.
- Read the Batch 2 handoff first:
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_2_handoff.md`
- Do not use local text-panel repair candidates for final promotion. The user requested text to be generated in-image, not added afterward.
- Critical Popo lock: Popo's bell itself is the face. No separate face/head/body under the bell; no bag in nap-room or activity scenes unless explicitly needed.

## 2026-06-01 Batch 1 Generation

Generated Batch 1 candidates and saved them into:

`series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_1`

| File | Scene | QA judgment | Notes |
| --- | --- | --- | --- |
| `00_candidate_text_v1.png` | Cover | Fail / do not use | Text was readable, but sleeping friends appeared as visible old-version character faces. |
| `00_candidate_text_v2.png` | Cover | Candidate pass | Character-free nap room is used cleanly; Popo keeps moon-jellyfish body; Banguli is separate. Text is readable. Needs user visual approval. |
| `01_candidate_text_v1.png` | Page 1 nap time starts | Hold / text repair source | Visual composition is usable, but generated Korean text contained errors such as `낫잠`. |
| `01_candidate_text_v2.png` | Page 1 retry | Fail / do not use | Text still rendered `낫잠`, and visible old-version sleeping-character drift increased. |
| `01_candidate_text_panel_v3.png` | Page 1 local text-panel repair | Superseded / do not use | User rejected post-added text panels for this batch because panels can cover the illustration. |
| `01_candidate_text_v3.png` | Page 1 retry | Hold / do not promote | Better on scene logic: Popo is in bed, no Popo bag, sleeping friends visible, Aru has fins not hands. Still should be regenerated from stable nap-room references after the bed-map refs are approved. |
| `02_candidate_text_v1.png` | Page 2 Popo cannot sleep | Fail / do not use | User rejected because sleeping friends disappeared and Popo carried a bag. |
| `02_candidate_text_v2.png` | Page 2 retry | Hold / do not promote | Better on scene logic: sleeping friends visible, no Popo bag, empty Popo bed visible. Still should be regenerated from stable nap-room references after the bed-map refs are approved. |
| `03_candidate_text_v1.png` | Page 3 Popo plays alone | Hold / text repair source | Visual is useful, but generated text had errors such as `둥실동실`. |
| `03_candidate_text_panel_v2.png` | Page 3 local text-panel repair | Superseded / do not use | User rejected post-added text panels for this batch because panels can cover the illustration. |
| `03_candidate_text_v2.png` | Page 3 retry | Fail / reference only | Scene logic improved: sleeping friends visible, Banguli asleep, empty Popo bed visible, no Popo bag. Text has major errors such as `동실동실`; do not promote. |
| `batch_1_contact_sheet.png` | Review sheet | Superseded | Contains an outdated review set with panel repairs. Rebuild only after new reference-based page retries. |
| `01_candidate_text_v4_ref.png` | Page 1 reference-based retry | Candidate pass | Uses approved sleeping-children reference v2; Popo is in aqua bed with bell-as-face structure and no bag; sleeping friends and bed map are stable. User confirmed the generated `낮잠` text is acceptable. |
| `02_candidate_text_v3_ref.png` | Page 2 reference-based retry | Hold / superseded by v5 | Uses empty-Popo-bed reference v2 and has good Popo/empty-bed continuity, but Banguli can read as duplicated. |
| `02_candidate_text_v4_ref.png` | Page 2 reference-based retry | Hold / superseded by v5 | Removes most Banguli duplication but Banguli could be sleepier. |
| `02_candidate_text_v5_ref.png` | Page 2 reference-based retry | Candidate pass | Banguli is a single sleepy-eyed droplet near Popo; Popo has no bag, bell-as-face structure is preserved, and Popo's aqua bed is visibly empty. |
| `03_candidate_text_v3_ref.png` | Page 3 reference-based retry | Hold | Good reference-based room continuity, Popo has no bag, empty Popo bed visible, sleeping friends remain. Assistant initially flagged `둥실둥실`, but user said the text is not a problem; keep for user review unless a separate visual issue is found. |
| `03_candidate_text_v4_ref.png` | Page 3 reference-based retry | Superseded / do not use | Aru's yellow bed moved forward compared with page 2, breaking layout continuity. |
| `03_candidate_text_v5_ref_layout.png` | Page 3 layout retry | Candidate pass | Aru's yellow bed stays in the back/middle-right like page 2; Popo's aqua bed remains empty in front/right; Popo has no bag and keeps bell-as-face structure. |

Current Batch 1 review state:

- Cover: `00_candidate_text_v2.png` was user approved and promoted to `final/00_표지.png`.
- Page 1: `01_candidate_text_v4_ref.png` was user approved and promoted to `final/01_페이지.png`.
- Page 2: `02_candidate_text_v5_ref.png` was user approved and promoted to `final/02_페이지.png`.
- Page 3: `03_candidate_text_v5_ref_layout.png` was user approved and promoted to `final/03_페이지.png`.

Do not replace final Batch 1 files unless the user explicitly requests a revision.

## 2026-06-01 Nap-Room Reference Retry

- User identified the root problem: page generation changes the bed layout and sleeping-character placement slightly from page to page.
- New plan: prepare two stable reference images before regenerating pages 1-3:
  - `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스.png`
  - `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스.png`
- The first generated sleeping reference is rejected as a standard because Popo's sleeping form does not match the official reference: the bell no longer reads as Popo's face and a separate small face/body impression appears. Regenerate it before use.
- Corrected reference candidates:
  - `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
    - Candidate hold: Popo is closer to the official lock because the translucent bell itself reads as the face, with only a small mouth on the bell and no separate head/body below it.
    - QA note: inspect before approval; Popo's tentacles are still partially tucked/simplified by the blanket, but the main face structure is correct.
  - `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
    - Candidate hold: uses a very similar bed map and keeps Popo's aqua bed empty, with no Popo and no bag.
    - QA note: Banguli is visible near the empty Popo bed; avoid duplicating Banguli in later page prompts because Jun-i's bed also includes a small blue comfort object that could be visually confused with a droplet.
- Do not regenerate pages 1-3 until the user approves or revises these two reference candidates.

## 2026-06-01 Batch 2 Preparation

- Read and cross-checked:
  - `docs/episode_worklog_2026-06-01_popo_naptime.md`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_2_handoff.md`
- Verified approved Batch 1 final files exist and should not be replaced:
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/00_표지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/01_페이지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/02_페이지.png`
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/final/03_페이지.png`
- Verified `work_2026-06-01/batch_2/` exists and is ready for page 4-7 candidates.
- Created Batch 2 prompt/reference plan:
  - `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_2/batch_2_prompt_plan.md`
- Batch 2 generation scope remains pages 4-7 only.
- Page 4 should use the nap-room continuity references:
  - `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
  - `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
- Pages 5-7 should use the official playground/exterior reference unless the user requests classroom activity instead:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- First concrete next action: generate `04_candidate_text_v1.png` with the actual reference images attached, then QA before moving to page 5.

## 2026-06-01 Batch 2 Generation

Generated Batch 2 candidates and saved them into:

`series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_2`

| File | Scene | QA judgment | Notes |
| --- | --- | --- | --- |
| `04_candidate_text_v1.png` | Page 4 nap time ends | Fail / do not use | Scene and Popo are usable, but Lulu/Sua drifted into coral-headed sea-creature shapes and Aru showed hand-like gestures. |
| `04_candidate_text_v2.png` | Page 4 nap time ends, seahorse identity retry | Candidate pass | Lulu and Sua return to official seahorse structure with tube snouts and curled tails. Aru is a round pufferfish without human hands. Text appears readable. Keep for user review before final promotion. |
| `05_candidate_text_v1.png` | Page 5 afternoon floating game begins | Candidate pass | Playground/exterior setting is clear. Lulu and Sua retain seahorse silhouettes; Aru is round without human hands. User said the `둥실` text issue can be accepted and to move on. |
| `06_candidate_text_v1.png` | Page 6 Popo becomes sleepy during play | Candidate pass | Popo is the emotional center with drooping bell/tentacles and yawning mouth. Height contrast with friends is clear. Lulu remains a seahorse. Text has minor generated variation but is acceptable under current user direction. |
| `07_candidate_text_v1.png` | Page 7 Popo cannot float highest | Candidate pass | Strong vertical contrast: friends high, Popo low and gently disappointed. Lulu/Aru/Mongle identities are readable and friends are not teasing. Text is readable with minor generated variation. |
| `batch_2_contact_sheet.png` | Batch 2 review sheet | Review aid | Contact sheet showing current preferred candidates for pages 4-7. |
| `04_candidate_text_v3.png` | Page 4 nap time ends, no-bag/Jun-i retry | Candidate for user review | Regenerated because Jun-i in v2 had glove-like raised arms and a slightly drifted look. This version removes child bags for the nap-room scene and keeps Jun-i closer to the official blue shark body. QA note: Jun-i's raised fins may still read a little arm-like because the script says he stretches, but no separate gloves or bag are visible. |
| `05_candidate_text_v2.png` | Page 5 floating game, Aru scarf retry | Candidate for user review | Regenerated because Aru's scarf was missing in v1. This version shows Aru's red-and-white sailor scarf clearly and keeps Aru round with side fins, no human hands. |
| `06_candidate_text_v2.png` | Page 6 Popo gets sleepy, Aru scarf retry | Candidate for user review | Regenerated because Aru's scarf was missing in v1. This version shows Aru's red-and-white sailor scarf clearly while keeping Popo centered and sleepy. |
| `07_candidate_text_v2.png` | Page 7 Popo cannot float highest, Aru scarf retry | Candidate for user review | Regenerated because Aru's scarf was missing in v1. This version shows Aru's red-and-white sailor scarf clearly and preserves the vertical contrast with Popo low and friends high. |
| `04_candidate_text_v4.png` | Page 4 nap time ends, bed-map continuity retry | Candidate for user review | Regenerated because v3 changed the nap-room and bed layout too far from final pages 1-3. This version restores the familiar left text panel, Lulu red bed at lower left/front, Jun-i blue bed at lower center-left, Mongle purple bed at lower center/front, Aru yellow bed at upper center-right/back, and Popo's empty aqua bed at front/right. QA note: bed coordinates are closer to pages 1-3 but not pixel-identical; no child bags are visible, and Jun-i has raised shark fins rather than gloves. |

Current Batch 2 review state:

- Page 4: `04_candidate_text_v4.png` is the current preferred candidate after the bed-map continuity retry.
- Page 5: `05_candidate_text_v2.png` is user-approved.
- Page 6: `06_candidate_text_v2.png` is user-approved.
- Page 7: `07_candidate_text_v2.png` is user-approved.
- Do not promote to `final/04_페이지.png` through `final/07_페이지.png` until the user approves the Batch 2 candidate set or requests targeted retries.
