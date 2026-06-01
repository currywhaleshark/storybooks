# Batch 3 Handoff - Popo Naptime Story

## Status

Batch 1 and Batch 2 are promoted to final.

Do not regenerate or replace final pages 0-7 without an explicit user request:

- `final/00_표지.png`
- `final/01_페이지.png`
- `final/02_페이지.png`
- `final/03_페이지.png`
- `final/04_페이지.png` from `batch_2/04_candidate_text_v6.png`
- `final/05_페이지.png` from `batch_2/05_candidate_text_v2.png`
- `final/06_페이지.png` from `batch_2/06_candidate_text_v2.png`
- `final/07_페이지.png` from `batch_2/07_candidate_text_v2.png`

## Batch 3 Scope

Generate pages 8-12 only:

- Page 8: Mari teacher notices Popo is struggling and meets Popo at eye level.
- Page 9: Mari explains naps gather strength for afternoon play.
- Page 10: Popo rests on a cushion with Banguli nearby.
- Page 11: Next day, Popo chooses to settle first for nap.
- Page 12: After resting well, Popo floats highest.

Stop after Batch 3 QA and user review. Do not overwrite final pages until the user approves the candidate set or gives targeted retry instructions.

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
- Nap room continuity:
  - `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
  - `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
- Playground/exterior:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`

## Carry-Forward Visual Locks

- Popo's translucent jellyfish bell itself is Popo's face. Do not draw a separate head, face, body, cheeks, human limbs, or hair under the bell.
- Popo has a pale sky-blue translucent scalloped bell, white moon-jellyfish flower pattern inside the bell, small mouth on the bell, hidden or barely visible eyes, soft thin tentacles, and small sailor collar.
- Do not add Popo's bag in rest, nap-room, or activity pages unless the user explicitly requests it.
- Banguli is a separate tiny pale-blue water droplet mascot. Do not duplicate Banguli.
- Aru is a round orange pufferfish with side fins only. No human hands, fingers, arms, or gloves.
- For playground pages, Aru's red-and-white sailor scarf should be visible.
- For nap-room pages, avoid child bags unless the script clearly requires them.
- Keep the emotional tone warm. Popo is tired and learning, not being shamed.
- Avoid pseudo-writing, extra signs, random labels, speech bubbles, neon highlights, glossy 3D, scary darkness, and unrelated prior-episode details.
- Generate story text in-image. Do not use local post-added text panels unless the user explicitly changes the rule.

## Batch 2 Lessons To Preserve

- Page 4 required several corrections:
  - no bags in the nap room;
  - Jun-i should not have glove-like hands;
  - the page 1-3 bed map must stay stable;
  - Sua belongs below/in front of Jun-i, not Mongle;
  - Sua's bed should be purple/lavender, while Popo's empty bed is aqua/teal.
- Pages 5-7 passed after Aru's scarf was restored.
- For future group scenes, place character identity and fixed clothing in the prompt as explicit locks, not just prose context.

## Page-Specific Notes

- Page 8 returns emotionally to Popo and Mari. Use the playground/exterior unless the composition works better with a simplified activity-area backdrop. Mari should bend or lower herself to Popo's eye level; she must not scold.
- Page 9 can stay close on Mari, Popo, and Banguli. The visual center should be Mari's gentle round-hand gesture showing strength gathering.
- Page 10 should move back to a warm rest/nap-room cushion. Popo rests without resisting; Banguli sleeps beside Popo. No Popo bag.
- Page 11 is next day nap time. Preserve the established nap-room bed map. Popo should choose the aqua bed/cushion first, calm and willing.
- Page 12 returns to the bright playground/exterior. Popo floats highest, fully energized; friends look up warmly, not competitively or mockingly.

## First Action Next Session

1. Read this handoff and `docs/episode_worklog_2026-06-01_popo_naptime.md`.
2. Inspect final pages 4-7, especially `final/04_페이지.png`, for continuity before planning page 8.
3. Create `work_2026-06-01/batch_3/batch_3_prompt_plan.md` for pages 8-12.
4. Generate page 8 first, then QA before moving on.
5. Keep all new candidates under `work_2026-06-01/batch_3/` with stable names such as `08_candidate_text_v1.png`.
