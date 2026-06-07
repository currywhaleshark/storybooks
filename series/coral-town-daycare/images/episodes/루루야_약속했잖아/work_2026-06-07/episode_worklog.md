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
