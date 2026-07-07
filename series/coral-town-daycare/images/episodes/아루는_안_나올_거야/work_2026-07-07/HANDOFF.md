# Handoff - 아루는 안 나올 거야

Date: 2026-07-07

## Why This Handoff Exists

Batch 3 page 09 generation appears session-contaminated. Multiple attempts drifted away from the episode into unrelated educational, diagram, greenhouse, market, or abstract content, and one attempt hit a safety filter. Continue page 09 in a fresh session/context. Do not try to recover page 09 from the failed images in this session.

## Must Read First In New Session

1. `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/episode_worklog.md`
2. `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/page_plan.md`
3. `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/batch_3/batch_3_prompt_plan.md`
4. `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`

If Korean text or paths appear garbled, re-read the file explicitly as UTF-8 before acting.

## Current Episode State

- Final approved pages exist for cover through page 06:
  - `final/00_표지.png`
  - `final/01_진흙놀이.png`
  - `final/02_씻을_시간.png`
  - `final/03_안_씻을래.png`
  - `final/04_바뀌는_건_어렵지.png`
  - `final/05_방울이가_먼저_첨벙.png`
  - `final/06_어_따뜻하고_좋네.png`
- Batch 3 pages 07-08 have review candidates only. They have not been promoted to `final`.
- Batch 3 page 09 has no usable candidate.
- Do not start Batch 4 until page 09 is successfully regenerated and the user approves the Batch 3 path.

## Batch 3 Review Candidates

- Page 07 generated-text option:
  - `work_2026-07-07/batch_3/07_candidate_text_v2.png`
  - QA: visually strong; generated text looked exact on inspection.
- Page 07 text-safe option:
  - `work_2026-07-07/batch_3/07_candidate_text_v4_local_text_panel.png`
  - QA: exact local Korean text panel, no old text remnant; panel is flatter than generated watercolor texture.
- Page 08:
  - `work_2026-07-07/batch_3/08_candidate_text_v1.png`
  - QA: candidate pass. Aru resists leaving with round body only; no limbs; Mari is warm and non-forcing; text looked exact.

## Do Not Use As Visual References

Do not use any failed page 09 outputs from this contaminated session as references, candidates, or style anchors. They were intentionally not copied into the batch candidate folder.

Known failed/drifted page 09 source files in the default generated-image folder:

- `C:/Users/yurib/.codex/generated_images/019f3b9c-22fc-71f1-8300-b00cb7021f71/ig_0ac4d0de750c9d44016a4cd46cafc88191b0e03341ab90880b.png`
- `C:/Users/yurib/.codex/generated_images/019f3b9c-22fc-71f1-8300-b00cb7021f71/ig_0afd2fad4d1e2550016a4cd662319c8191ac505e8b1227b82a.png`
- `C:/Users/yurib/.codex/generated_images/019f3b9c-22fc-71f1-8300-b00cb7021f71/ig_0afd2fad4d1e2550016a4cd6fe71248191ad8df2276e0819c6.png`
- `C:/Users/yurib/.codex/generated_images/019f3b9c-22fc-71f1-8300-b00cb7021f71/ig_0afd2fad4d1e2550016a4cd7a516448191961985edf0cbd363.png`

Also do not use held/superseded page 07 repair attempts as reference truth:

- `work_2026-07-07/batch_3/07_candidate_text_v1_hold_text.png`
- `work_2026-07-07/batch_3/07_candidate_text_v3_local_text_panel.png`

## Locks To Preserve

- Official references and rulebook outrank generated attempts.
- Use actual reference images with `view_image` before any generation.
- Aru:
  - soft cream-yellow pufferfish body
  - muted tan-olive top shading
  - darker brown top spots
  - warm beige fins
  - red-white sailor scarf
  - no hands, feet, legs, arms, human torso, separate lower body, or school bag
- Water tub:
  - `work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
  - low toddler-safe shell basin, shallow warm clean water, peach-coral scalloped rim, cream/sand shell body
  - no sink, bathtub, bathroom fixtures, deep pool, or cold/unsafe water
- Mari:
  - warm, patient, non-forcing
  - no scolding, grabbing, dragging, pulling, shaming, or lesson-explaining on page 09
- Page 09:
  - realization belongs to Aru, not Mari
  - gentle self-awareness: changing states is hard
  - Banguli may watch quietly
  - Mari absent or very small/background only

## Page 09 Exact Text

Render exactly:

```text
그러다
아루는

멈칫—

"어?"

"아까는
씻기 싫다고
했는데……"

"지금은
나오기 싫네?"

아루는 눈을
동그랗게 떴어요.

"내 마음이
바뀌기 어려웠나 봐."
```

## Recommended Fresh-Session Strategy For Page 09

1. Open this handoff and the worklog.
2. Inspect only the official refs and approved final continuity refs:
   - `work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
   - `references/characters/no_bag/아루_no_bag.png`
   - `references/characters/no_bag/방울이_no_bag.png`
   - `references/characters/아루.png`
   - `references/characters/방울이.png`
   - `final/06_어_따뜻하고_좋네.png`
3. Avoid loading failed page 09 outputs into the visual context.
4. Try page 09 as a single quiet picture-book close-up. Keep prompt shorter than the previous failed attempts:
   - "Aru pauses in the shallow shell tub, thoughtful `어?` expression, Banguli quietly nearby, Mari absent."
   - "Korean toddler watercolor storybook page, clean cream text panel."
   - Include the exact Korean text above.
5. If generated Korean text fails but the art is correct, save the art as `09_candidate_text_v1_hold_text.png` and make a separate local text-panel repair candidate.
6. If page 09 drifts again, stop immediately and create a fresh page 09-only prompt plan instead of continuing in the same context.

## Suggested Output Names

- First good page 09 art with generated text:
  - `work_2026-07-07/batch_3/09_candidate_text_v1.png`
- Good art with bad generated text:
  - `work_2026-07-07/batch_3/09_candidate_text_v1_hold_text.png`
- Local repaired text version:
  - `work_2026-07-07/batch_3/09_candidate_text_v2_local_text_panel.png`

## Git / Workspace Notes

- Current storybook work changed/added under:
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/`
- Unrelated modified files exist under:
  - `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/`
- Do not revert unrelated user changes.
