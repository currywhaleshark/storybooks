# Handoff To Next Thread - Batch 4 Final QA - 2026-06-09

## Current Status

- Episode: `루루야, 약속했잖아`
- Work root: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07`
- Batch 4 folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/batch_4`
- Final folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final`
- Important: always open Korean markdown with UTF-8.

## User Direction Override

- The earlier batch 4 starter handoff said to generate `reference_assets/promise_heart_shell_ref.png` before page 11.
- User later overrode this: the heart shell appears on only one page, so do not make a separate prop reference. Page 11 already includes the small shell directly in the page image.
- Page 12 source typo was corrected during generation from `새끼 손가락를` to `새끼 손가락을`.

## Approved And Final-Promoted

- Pages 00-09 were already user-approved and final-promoted before batch 4.
- Page 10 was generated in this thread and user accepted it as good enough to pass.
- Final-promoted this thread:
  - `batch_4/10_candidate_text_v1.png` -> `final/10_페이지.png`

## Current Batch 4 Candidate Files

- `batch_4/10_candidate_text_v1.png`
  - Status: user approved / final promoted.
  - Size: `1054x1492`.
  - Note: text has minor generated drift, but user accepted it.
- `batch_4/11_candidate_text_v1.png`
  - Status: current page 11 QA candidate, not final promoted.
  - Size: `1054x1492`.
  - Scene: clean classroom, Mari teacher shows a tiny soft heart shell in her palm, Lulu and Jun-i share apology/acceptance.
  - Assistant QA: candidate pass for scene, heart-shell scale, clean classroom mood, no worn bags, and character staging. Needs final user QA.
- `batch_4/12_candidate_text_v1.png`
  - Status: held.
  - Reason: indoor children had worn bags, especially Popo.
- `batch_4/12_candidate_text_v2.png`
  - Status: superseded.
  - Reason: bags corrected, but user said Lulu and Jun-i were too large and foreground friends looked too small.
- `batch_4/12_candidate_text_v3.png`
  - Status: current preferred page 12 QA candidate, not final promoted.
  - Size: `1054x1492`.
  - Scene: ending promise, Lulu and Jun-i reduced closer to Mari teacher's visual scale, foreground friends are more readable.
  - Text uses corrected `새끼 손가락을`.

## Next Thread First Actions

1. Read this handoff, then read:
   - `episode_worklog.md`
   - `page_plan.md`
   - `batch_4/batch_4_prompt_plan.md`
   - `series/coral-town-daycare/docs/episodes/루루야_약속했잖아.md`
   - `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
2. Verify `final/00_표지.png` through `final/10_페이지.png` exist.
3. Visually QA:
   - `batch_4/11_candidate_text_v1.png`
   - `batch_4/12_candidate_text_v3.png`
4. If user approves:
   - Promote `batch_4/11_candidate_text_v1.png` to `final/11_페이지.png`.
   - Promote `batch_4/12_candidate_text_v3.png` to `final/12_페이지.png`.
5. If user wants mobile QA first, create a review deck from:
   - `final/10_페이지.png`
   - `batch_4/11_candidate_text_v1.png`
   - `batch_4/12_candidate_text_v3.png`

## Final QA Focus

- Page 11:
  - Heart shell should stay tiny, gentle, and warm in Mari teacher's palm.
  - It must not read as neon, jewel-like, dramatic magic, or a lamp.
  - Check exact Korean readability and spacing in the text panel.
  - Confirm Lulu, Jun-i, Banguli, and Mari teacher match official references.
- Page 12:
  - Confirm user-requested scale fix: Lulu and Jun-i should not dominate; foreground friends should not look tiny.
  - Confirm no worn bags on indoor children.
  - Confirm `새끼 손가락을` appears, not `새끼 손가락를`.
  - Confirm Aru remains one pufferfish body only, Popo has hidden/barely visible eyes, Sua keeps official purple seahorse design, and Banguli has no hands/arms/legs.

## Carried-Forward Locks

- Official character sheets are visual truth. Do not rely on prose-only character descriptions.
- All child characters keep small black button eyes.
- Lulu keeps small black button eyes plus one subtle eyelash line on the visible eye.
- Lulu's reference outfit is locked: cream sailor top, pink/mauve collar and scarf, shell patch/name tag, mauve pleated skirt, translucent pink fin, curled tail, spiny ridge, dotted texture, long tube snout.
- Sua must keep the official purple slender seahorse design: long tube snout, small black button eyes, spiny dotted head ridge, blue sailor collar/skirt, small translucent fin, curled tail, and no worn bag in indoor classroom scenes.
- No worn bags in indoor classroom scenes. If a bag appears, it belongs in muted background storage, not on a child's body.
- Banguli must stay droplet-like with side bubbles and no hands/arms/legs.
- Aru must remain one pufferfish body only with scarf; no human torso, legs, feet, or separate body.
- Popo should keep hidden or barely visible eyes unless a special expression is needed.
- Use user-approved pages only as continuity references. Do not use held or superseded candidates except to understand what was rejected.

## Do Not Do

- Do not generate `promise_heart_shell_ref.png` unless the user explicitly changes direction again.
- Do not promote pages 11 or 12 to final before user QA approval.
- Do not replace `final/10_페이지.png`; it is already user-accepted and final-promoted.

## Final QA Completed - 2026-06-09

- User approved page 11 and page 12 after manually correcting Aru's scarf on `batch_4/12_candidate_text_v3.png`.
- Final-promoted:
  - `batch_4/11_candidate_text_v1.png` -> `final/11_페이지.png`
  - user-corrected `batch_4/12_candidate_text_v3.png` -> `final/12_페이지.png`
- The episode final folder now contains cover plus pages 01-12.
