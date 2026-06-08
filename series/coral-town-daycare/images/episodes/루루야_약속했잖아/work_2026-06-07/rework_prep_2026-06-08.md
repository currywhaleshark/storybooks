# Rework Prep - 루루야, 약속했잖아 - 2026-06-08

## UTF-8 Readback

- `episode_worklog.md`, `page_plan.md`, `batch_1/batch_1_prompt_plan.md`, `reference_assets/reference_asset_plan.md`, episode script, and rulebook were re-read with UTF-8.
- Do not rely on earlier mojibake console output.

## Current Workspace Inventory

Present files under `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07`:

- `episode_worklog.md`
- `page_plan.md`
- `batch_1/batch_1_prompt_plan.md`
- `reference_assets/reference_asset_plan.md`

Not present in the current workspace, despite being mentioned in the worklog:

- `reference_assets/lulu_favorite_picture_book_ref.png`
- `reference_assets/messy_art_time_state_ref.png`
- `batch_1/00_candidate_text_v1.png`
- `batch_1/01_candidate_text_v1.png`
- `batch_1/02_candidate_text_v1.png`
- `batch_1/03_candidate_text_v1.png`
- `batch_1/00_candidate_text_v2.png`
- `batch_1/00_candidate_text_v3.png`
- `batch_1/01_candidate_text_v2.png`
- `batch_1/02_candidate_text_v2.png`
- `batch_1/03_candidate_text_v2.png`

Before main page regeneration, restore or regenerate the missing episode-specific references.

## Official Reference Checklist

Use actual image files as visual truth:

- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`

## Rework Order

1. Restore or regenerate `lulu_favorite_picture_book_ref.png`.
2. Restore or regenerate `messy_art_time_state_ref.png`.
3. Regenerate batch 1 one page at a time, starting with page 00.
4. QA each candidate before generating the next page.
5. Promote nothing to `final` until user approval.

## Hard Retry Locks

- Preserve official-reference silhouettes over extra cuteness.
- Do not over-round any character beyond the official reference.
- No worn bags in indoor classroom scenes.
- Lulu must keep the head ridge, bead tips, dotted/ridged texture, long snout, coral head ornament, sailor outfit, translucent back fin, and curled tail.
- Sua must keep the purple seahorse body, dotted/spiny head ridge, long snout, blue sailor outfit, and curled tail even when small.
- Aru must be one true pufferfish body only, with small fins/spikes and sailor scarf. No separate body, torso, hands, feet, legs, or clothing-like lower half.
- Popo's eyes are hidden or barely visible by default. Emotion should come from mouth, dome tilt, and tentacles unless the script specifically asks for eyes.
- Keep exact Korean text when possible. If text cannot be rendered cleanly, leave a clean blank text area instead of inventing wrong text.
- Avoid prior-episode contamination, extra signs, pseudo-writing, harsh conflict expressions, neon colors, plastic 3D texture, and dense background clutter.

## First Regeneration Packet - Page 00

Output candidate:

- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/batch_1/00_candidate_text_v4.png`

Attach references:

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

Exact text:

```text
루루야, 약속했잖아

— 지킨 약속은 반짝반짝 —
```

Prompt focus:

- Warm classroom promise moment.
- Lulu and Jun-i centered, facing each other, making a pinky-promise gesture.
- Banguli floats beside them and nods happily.
- A5 portrait.
- Clean title space at top and subtitle space near bottom.
- Preserve official silhouettes and fine details first; do not make the characters generically rounder or simpler.

QA after generation:

- Lulu reference fidelity.
- Jun-i shark structure, white belly, fins, tail, small teeth, sailor outfit.
- Banguli droplet body and tiny companion droplets.
- No worn bags.
- A5 portrait proportion.
- Exact Korean title/subtitle, or clean blank title/subtitle areas.
- No unrelated previous episode details or pseudo-writing.

