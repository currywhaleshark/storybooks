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

- Start with Batch 1 only: cover + pages 1-3.
- Before generation, load the image generation skill and attach/pass the actual official references listed in the Batch 1 prompt plan.
- Use the updated character-free `배경_낮잠방.png`; do not use the backup as a generation reference unless explicitly requested.
- Generate exactly these candidates first:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`
- Save outputs into `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_1`.
- QA and record only file paths plus status in this worklog before promoting anything to `final`.
