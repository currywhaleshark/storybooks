# Batch 1 Prompt Plan - Popo Naptime Story

## Scope

- Episode: `포포는 안 졸려!`
- Batch: cover + pages 1-3 only
- Script: `series/coral-town-daycare/docs/episodes/popo_naptime_story_prompts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work folder: `series/coral-town-daycare/images/episodes/포포는_안_졸려/work_2026-06-01/batch_1`
- Final folder: `series/coral-town-daycare/images/episodes/포포는_안_졸려/final`

Do not generate Batch 2 in this session. Stop after Batch 1 QA and user review/handoff.

## Required References

- Character: `series/coral-town-daycare/references/characters/포포.png`
- Character: `series/coral-town-daycare/references/characters/방울이.png`
- Character: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Character: `series/coral-town-daycare/references/characters/준이.png`
- Character: `series/coral-town-daycare/references/characters/아루.png`
- Character: `series/coral-town-daycare/references/characters/루루.png`
- Character: `series/coral-town-daycare/references/characters/몽글이.png`
- Character: `series/coral-town-daycare/references/characters/수아.png`
- Character: `series/coral-town-daycare/references/characters/토리.png`
- Background: `series/coral-town-daycare/references/배경_낮잠방.png`

Before every generation, attach/pass the actual visible character and background reference image files. Prompt text is not a substitute for the images.

Nap room reference note: `배경_낮잠방.png` was updated on 2026-06-01 to be character-free. Use this current file as the official nap room background. Do not use `배경_낮잠방_backup_before_characterless_2026-06-01.png` for generation unless the user explicitly requests comparison or rollback.

## Batch Locks

- A5 portrait page proportion, about `1:1.414`, not square and not extra-tall poster.
- Include the exact page text in the generated image from the first pass.
- Keep text in a clean storybook text panel or clean reserved text area, following the series style.
- Popo keeps the official moon-jellyfish form: translucent pale-blue bell, hidden or mostly hidden eyes, visible moon-jellyfish pattern, scalloped bell edge, soft tentacles, small mouth expression.
- Banguli remains a tiny separate water droplet mascot, not a jellyfish.
- Nap room stays cozy and warm: shell beds/cushions, warm lamps, soft curtains, rounded windows, pastel watercolor texture. Not scary, dark, neon, or deep-sea.
- The nap room background must remain character-free in prompts; add current official characters only from the official character reference files required for each page.
- Avoid extra signs, pseudo-writing, random labels, speech bubbles, unrelated previous-episode details, hard glass shine, or glossy 3D toy texture.

## 00 Cover Prompt

Output candidate: `00_candidate_text_v1.png`

Input images:

- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/배경_낮잠방.png`

Prompt:

Create the cover page of the Korean toddler storybook `포포는 안 졸려!` in the Coral Town Daycare series. A5 portrait page proportion, about 1:1.414. Use the official reference images as visual truth.

Scene: a softly dim but warm and cozy nap room with shell beds, puffy nap blankets, cushions, rounded window light, soft seaweed curtains, and gentle warm lamps. Popo, the pale sky-blue translucent moon-jellyfish child, floats slightly above the center, awake and excited while other friends sleep under blankets below as soft rounded silhouettes. Popo's eyes are hidden or mostly hidden under the translucent bell; emotion comes from a small round open happy mouth, a plump lifted bell, and soft tentacles lightly spreading. The moon-jellyfish pattern inside the bell is visible. Popo wears the sailor collar and small beige bag from the official reference. Banguli floats beside Popo, sleepy and winking, with two or three tiny water droplets.

Text:

```text
포포는 안 졸려!

— 낮잠은 신나게 놀 힘을
모으는 시간 —
```

Avoid: no visible human arms or legs on Popo, no droplet-shaped Popo, no hard glass orb, no scary dark room, no neon, no extra signage or pseudo-writing.

## 01 Page Prompt

Output candidate: `01_candidate_text_v1.png`

Input images:

- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/배경_낮잠방.png`

Prompt:

Create page 1 of the Korean toddler storybook `포포는 안 졸려!`. A5 portrait page proportion, about 1:1.414. Use the official reference images as visual truth.

Scene: after lunch in the official Coral Town Daycare nap room. Mari teacher gently announces nap time while holding or softly shaking a small shell instrument. The friends settle into their own shell beds, blankets, or cushions in varied gentle poses: Jun, Aru, Lulu, Mongle, Sua, and Tori. Popo settles lightly onto Popo's own cushion, still calm. The room is warm, cozy, and quiet, with rounded windows, soft curtains, shell beds, cushions, warm lamps, and pastel watercolor texture. Use a wide middle-distance composition that shows the nap room clearly.

Text:

```text
점심을 먹고 나면
낮잠 시간이에요.

마리 선생님이
조개 악기를 살랑.

딸랑— 딸랑—

친구들이 하나, 둘
이불 속으로 쏙.

"잘 자, 친구들아."

방 안이
포근하고 조용해졌어요.
```

Avoid: no copied identical sleeping faces, no bags emphasized as active props in bed, no cluttered room, no scary darkness, no extra text.

## 02 Page Prompt

Output candidate: `02_candidate_text_v1.png`

Input images:

- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_낮잠방.png`

Prompt:

Create page 2 of the Korean toddler storybook `포포는 안 졸려!`. A5 portrait page proportion, about 1:1.414. Use the official reference images as visual truth.

Scene: everyone is asleep in the quiet nap room, and Popo alone is awake on a cushion. Popo is not a droplet: keep the official moon-jellyfish bell, hidden or mostly hidden eyes, small mouth, moon pattern, scalloped edge, and soft tentacles. Popo's bell is gently wiggling and the tentacles are quietly fidgeting, showing that sleep is not coming. Banguli floats close with a sleepy kind expression and a small wink, inviting Popo to rest together. In the background, sleeping friends are only soft blanket silhouettes. Keep the mood gentle and curious, not disobedient or scolded.

Text:

```text
그런데 포포는
잠이 안 왔어요.

갓이 들썩들썩.
촉수가 꼼지락꼼지락.

"나는 안 졸려!"

방울이가
졸린 눈으로 윙크했어요.

'같이 자자—'

하지만 포포는
살래살래.

살금살금
떠올랐어요.
```

Avoid: no visible eyes on Popo unless hidden under the bell, no harsh refusal, no speech bubbles outside the story text panel, no extra labels.

## 03 Page Prompt

Output candidate: `03_candidate_text_v1.png`

Input images:

- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_낮잠방.png`

Prompt:

Create page 3 of the Korean toddler storybook `포포는 안 졸려!`. A5 portrait page proportion, about 1:1.414. Use the official reference images as visual truth.

Scene: Popo quietly plays alone in the cozy nap room while everyone else sleeps. Popo floats softly through the air and gently touches a shell mobile with thin jellyfish tentacles, making it sway slightly, and rolls a tiny water droplet. Popo's mouth is round and excited, bell lifted and plump, but the play is silent and careful because this is still nap time. Banguli is already sleeping on or near a cushion in the background, with two or three small droplets drifting upward as a sleep sign. Sleeping friends remain soft blanket silhouettes. Keep the room warm and cozy, not dark or spooky.

Text:

```text
포포는 둥실둥실
떠다녔어요.

촉수로 모빌을 살짝— 살짝—
물방울을
또르르 또르르.

"낮잠 안 자고 노니까 정말 재밌다!"

친구들은 쌔근쌔근.
방울이도 쌔근쌔근.

포포만 혼자 둥실둥실.
```

Avoid: no loud chaotic play, no waking friends, no scary dark room, no extra signs, no random typography, no hard-glass Popo.

## Batch 1 QA Checklist

- Popo matches official moon-jellyfish reference and does not become Banguli/droplet-shaped.
- Popo's eyes remain hidden or mostly hidden; emotion reads through mouth, bell, and tentacles.
- Banguli remains a separate small water droplet mascot.
- Nap room matches the official reference and stays warm, cozy, and safe.
- Text is present, readable, and close to the exact approved Korean text.
- No extra signage, pseudo-writing, speech bubbles, or unrelated previous-episode content appears.
- Candidate status is recorded in `docs/episode_worklog_2026-06-01_popo_naptime.md` before any final promotion.
