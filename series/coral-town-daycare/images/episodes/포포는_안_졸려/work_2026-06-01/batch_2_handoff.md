# Batch 2 Handoff - Popo Naptime Story

## Status

Batch 1 is user approved and promoted to final:

- `final/00_표지.png` from `batch_1/00_candidate_text_v2.png`
- `final/01_페이지.png` from `batch_1/01_candidate_text_v4_ref.png`
- `final/02_페이지.png` from `batch_1/02_candidate_text_v5_ref.png`
- `final/03_페이지.png` from `batch_1/03_candidate_text_v5_ref_layout.png`

Do not regenerate or replace these without explicit user request.

## Batch 2 Scope

Generate pages 4-7 only:

- Page 4: nap time ends; Mari wakes the children; Popo acts energetic.
- Page 5: afternoon floating game begins.
- Page 6: Popo becomes sleepy during play.
- Page 7: Popo cannot float highest like usual.

Stop after Batch 2 QA and user review. Do not start pages 8-12 in the same session unless the user explicitly changes the plan.

## Required References

Use actual image files as visual truth:

- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- For page 4 nap-room continuity:
  - `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
  - `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
- For pages 5-7, use the official classroom/playground/background references after inspecting the current docs and available files.

## Visual Locks

- Popo's translucent jellyfish bell itself is Popo's face. Do not draw a separate head, face, body, cheeks, or little creature under the bell.
- Popo has a pale sky-blue translucent scalloped bell, white moon-jellyfish flower pattern inside the bell, a small mouth on the bell, hidden or barely visible eyes, soft thin tentacles, and a small sailor collar.
- Do not add Popo's bag in nap/rest or activity pages unless the story explicitly needs it. Batch 2 should avoid Popo's bag.
- Banguli is a separate tiny pale-blue water droplet mascot. Do not duplicate Banguli.
- Aru is a round orange pufferfish with tiny fins only. No human hands, fingers, or arms.
- Avoid post-added text panels for final candidates. Generate the text in-image.
- Avoid pseudo-writing, random labels, extra signs, old-version character drift, glossy 3D, neon, or scary darkness.

## Page-Specific Notes

- Page 4 should transition from the fixed nap-room bed map. If beds are visible, keep the same approximate positions as Batch 1: Popo's aqua bed front/right, Aru's yellow bed back/middle-right, Jun-i lower/center-left, Lulu left/front, Mongle right/back, Sua lower area, Tori back/left.
- Page 4 Popo can be floating/awake and confident, but no bag. Tentacle tips may begin to droop very slightly as foreshadowing.
- Pages 5-7 move to afternoon play. Maintain Popo's bell-as-face identity while showing a gradual arc: normal-ish participation, then sagging bell/tentacles and yawning, then low floating and disappointment.
- Keep the emotional tone warm. Do not shame Popo.

## First Action Next Session

1. Read this handoff and `docs/episode_worklog_2026-06-01_popo_naptime.md`.
2. Inspect final Batch 1 files and the background refs.
3. Inspect available classroom/playground background references and choose the correct setting for pages 5-7.
4. Generate Batch 2 candidates one page at a time, saving them under `work_2026-06-01/batch_2/`.
5. QA each candidate before moving to the next page.
