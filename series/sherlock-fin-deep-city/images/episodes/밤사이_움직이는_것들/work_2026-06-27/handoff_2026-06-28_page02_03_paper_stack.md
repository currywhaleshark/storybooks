# Handoff - Sherlock Fin / 밤사이 움직이는 것들 / Page 02-03 Paper Stack Rework

Date: 2026-06-28
Reason for handoff: Current session showed image-generation contamination after the user's latest QA note. Stop generation/editing in this session and continue from a clean session.

## User QA To Address

Latest user feedback:

> 2,3페이지에서 책상 위의 서류뭉치는 그대로인데 바닥에만 추가로 흩뿌려진 모양이네
> 책상 위의 서류도 줄어들고 여기저기 흩어져야하지 않을까

Interpretation:
- Pages 02 and 03 currently look as if the original desk paper stack stayed intact and extra papers were merely added to the floor.
- The desk paper bundle must visibly shrink and break apart.
- Some of the same thin papers should remain askew on the desk, some should be sliding/falling from the desk edge, and some should be scattered on the floor/rug.
- Heavy desk objects must stay fixed.

## Current Scope

Cover is excluded.
Page 01 is likely acceptable as the stable before-state.
Pages 02 and 03 need clean-session regeneration or a carefully QA-confirmed edit.

## Key References

Script:
- `series/sherlock-fin-deep-city/docs/episodes/밤사이_움직이는_것들.md`

Worklog:
- `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/episode_worklog.md`

Batch prompt plan:
- `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1/batch_1_prompt_plan.md`

Primary visual references:
- `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

Use page 01 as the scene anchor:
- `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1/01_candidate_text_v3_desk_lock.png`

## Candidate Status

Likely OK / keep as anchor:
- `batch_1/01_candidate_text_v3_desk_lock.png`
  - Tidy before-state.
  - Desk placement and heavy objects should be used as the continuity anchor.

Needs rework:
- `batch_1/02_candidate_text_v4_desk_lock_door_fan.png`
  - Door-centered floor scatter direction is useful.
  - Problem: desk document pile still appears full/intact; floor papers feel added rather than displaced.

Needs rework:
- `batch_1/03_candidate_text_v5_desk_lock_door_right_handle.png`
  - Door handle correction is useful: handle/latch on viewer-right closing edge, hinges on viewer-left.
  - Problem: same paper-stack issue as page 02.

Rejected / do not use:
- `batch_1/03_candidate_text_v3_desk_lock_door_fan_reject_duplicate_feather.png`
  - Duplicate feather pen issue.
- `batch_1/03_candidate_text_v4_reject_handle_on_hinge.png`
  - Door handle/latch too close to hinge side.
- `batch_1/02_candidate_text_v5_reject_unrelated_thermal.png`
- `batch_1/02_candidate_text_v5_reject_unrelated_karma.png`
- `batch_1/02_candidate_text_v5_reject_unrelated_water_cycle.png`
  - Unrelated contaminated outputs from current session.

Experimental local edits, not approved:
- `batch_1/02_candidate_text_v5_reduced_desk_papers_local_edit.png`
- `batch_1/03_candidate_text_v6_reduced_desk_papers_right_handle_local_edit.png`
  - Created as a fallback after generation contamination.
  - Visual QA display failed in this session, so do not promote or upload as accepted without fresh visual inspection.

## Required Locks For New Page 02

Target filename recommendation:
- `batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`

Must preserve:
- Same detective-office layout as page 01.
- Desk position and angle fixed.
- Heavy objects fixed: thick book/notebook stack, file holder, desk lamp, magnifying glass, ink bottle, pen holder, large desk tools, chair, rug, large furniture.
- Door/gap direction consistent with the approved door reference.

Must change:
- The loose thin document stack on the desk is visibly reduced.
- Remaining desk papers are no longer a neat pile: a smaller partial pile plus several loose sheets/cards askew across the desk.
- Some papers visibly cross or slide over the desk edge.
- Floor/rug scatter should look like it came from the reduced desk stack.
- Scatter should fan out from the door/gap direction, supporting later deduction.
- Light objects only move: thin papers, cards, small notes, possibly one feather pen.

Avoid:
- Full neat desk paper stack plus separate added floor papers.
- Moving heavy objects.
- Extra character limbs or odd duplicated props.
- Any unrelated infographic/text contamination.

## Required Locks For New Page 03

Target filename recommendation:
- `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

Must preserve:
- Sherlock Fin sleeping/hat-brim pose from page 03 concept.
- Exactly two arms and two hands.
- Door handle/latch on viewer-right closing edge, hinges on viewer-left.
- No central knob and no handle attached to hinge side.
- Desk and heavy objects fixed as in page 01.

Must change:
- Same paper-stack correction as page 02: desk loose document stack visibly reduced, with papers spread across desk, sliding off desk edge, and continuing onto floor/rug.
- Floor scatter still reads as door-centered/fan-shaped evidence.
- No duplicate feather pen. If a feather pen is on the floor, it should not also remain upright in the pen holder.

Avoid:
- Returning to the page 03 handle-on-hinge problem.
- Full intact desk paper stack.
- Duplicate feather pen.
- Extra hands/arms or distorted sleeping pose.

## Text Requirements

Keep page text exactly as planned in the batch prompt plan unless the user changes it.
Check text panel style against:
- `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## Google Drive Review State

Existing mobile review folder:
- `https://drive.google.com/drive/folders/1SV0e33Q9HTi6nrV9FHzpwd4-WmVQvkwL`

Current uploaded files are now outdated for pages 02 and 03 because they predate the paper-stack QA feedback:
- Page 01: `https://drive.google.com/file/d/1Tl2iLbvg7iFiSs1xftZRibvv3Eapc-KV/view?usp=drivesdk`
- Page 02 old: `https://drive.google.com/file/d/1B6DgLaslXZ9v6XF12BZsq0xKwpvdeaaW/view?usp=drivesdk`
- Page 03 old: `https://drive.google.com/file/d/1UltDaMUpKYRy7OHc5yYPMtgwmkd--xUU/view?usp=drivesdk`

After acceptable new 02/03 candidates are made, upload the new files to the same Drive folder and report the new links. Do not mark final until the user approves.

## QA Checklist Before Showing User

- Page 01 remains the stable before-state anchor.
- Page 02 desk paper pile is visibly reduced, not intact.
- Page 03 desk paper pile is visibly reduced, not intact.
- Papers form a believable path: desk surface -> desk edge -> floor/rug.
- Scatter direction supports door-centered deduction.
- Heavy objects do not move.
- Page 03 door handle is on viewer-right closing edge, not hinge side.
- No duplicate feather pen.
- No extra limbs or distorted character anatomy.
- Text panel exists, style matches references, and text is legible.
- No unrelated generated subject matter appears.

## Recommended Next Step

Start a clean session, read this handoff plus `episode_worklog.md`, then regenerate only pages 02 and 03 using page 01 and the approved door reference as anchors. Upload the accepted new 02/03 candidates to the existing Google Drive folder for mobile review.