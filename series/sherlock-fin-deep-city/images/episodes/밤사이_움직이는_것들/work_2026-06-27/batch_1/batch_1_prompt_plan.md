# 밤사이 움직이는 것들 - Batch 1 Prompt Plan

## Batch Scope

- Pages: 00-03
- Output folder: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1`
- Candidate filenames:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`

## Actual References To Emit Before Generation

Use `nodeRepl.emitImage` for the actual PNGs before generation. Do not rely on local path text alone.

- Official office interior: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- Approved door/gap/water-current v2: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- Sherlock Fin character: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Textbox layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

Do not emit the broader Deep City jazz reference for Batch 1 unless needed; it previously encouraged music-like current contamination.

## Shared Visual Rules

- A5 portrait children's picture book page, warm polished illustration.
- Match the official detective office: shell/coral architecture, clue board, shell desk, warm bubble lamps, cozy deep blue-purple walls.
- Sherlock Fin must match the official character sheet: teal hair, detective cap, brown coat, teal mermaid tail, yellow magnifying glass, bright curious child detective expression.
- Use a cream/shell-colored rounded text panel following the textbox reference. Keep text clear and separate from character faces and clues.
- No unrelated previous episode content.
- No scary intruder, no suspicious silhouette, no horror tone.
- If the door/gap appears, use approved v2: a tiny gap at the lower-right closing edge of the shell door, where the door leaf meets the frame/floor area.
- Water current, when visible, must be actual water only: translucent pale blue water ribbons, faint ripples, tiny bubbles. No music notes, no staff lines, no sound-wave graphics, no saxophone shapes, no neon music icons, no decorative audio symbols.
- Pages 01-03 should not over-spoil the final answer. The gap can be subtle or invisible except where the page specifically needs it.

## Page 00 Cover Prompt

Generate an A5 portrait cover page for the children's picture book episode `밤사이 움직이는 것들` from the Sherlock Fin series.

Use the emitted official office image for the room design and the emitted approved door-gap v2 image for the shell door mechanics. Show Sherlock Fin inside the detective office in the morning, holding a yellow magnifying glass, curious and puzzled but not scared. Papers, small cards, and a feather pen are lightly scattered across the office floor and desk area. The shell door is visible on one side; the tiny gap at the lower-right closing edge can be subtly hinted, but do not make it obvious or huge. Warm bubble lamp light, shell desk, clue board, shell bookshelf, cozy deep-sea colors.

Title text must appear clearly near the top with generous margin:

```text
심해탐정 셜록 핀

밤사이 움직이는 것들
```

No other readable text. No music notes, no sound-wave symbols, no jazz icons. No scary intruder. Keep the mystery gentle and cozy.

## Page 01 Prompt

Generate A5 portrait page 01 with the emitted official office and Sherlock Fin references.

Scene: evening in the detective office. Sherlock Fin is tidying the office at the end of the day. Papers are neatly stacked, a feather pen is placed exactly in its holder or on the desk, small cards are neatly squared, and the shell door is being closed with a soft `딸깍` feeling. The office looks clean, calm, and cozy. This page establishes the normal before-state. Door gap should not be visible yet; the shell door appears closed and normal.

Place the cream rounded text panel at lower left, not covering Sherlock Fin's face or the door action. Render the exact Korean text:

```text
하루가 끝나는 저녁이에요.

셜록 핀은 사무소를
깨끗이 정리했어요.

서류는 가지런히,
깃털 펜은 제자리에,
카드는 반듯하게.

그리고 조개 문을
딸깍, 꼭 닫고 집으로 갔어요.

'내일 또 보자, 사무소야!'
```

No music symbols. No water current visible. No scary tone.

## Page 02 Prompt

Generate A5 portrait page 02 with the emitted official office, Sherlock Fin, and approved door-gap v2 references.

Scene: next morning. Sherlock Fin opens the shell door and stops in surprise. The door had been closed, the latch is still intact, but the office is now lightly disordered: papers scattered, feather pen moved, small cards shifted around. Keep the disorder gentle and child-safe, not messy disaster. Sherlock Fin looks surprised and curious, not frightened. The door and latch should be visible and still intact. The tiny lower-right closing-edge gap may be very subtle if visible, but do not make it the main clue yet.

Place the cream rounded text panel at upper right. Render the exact Korean text:

```text
다음 날 아침이에요.

조개 문은 어젯밤처럼
꼭 닫혀 있었어요.

잠금쇠도 그대로였지요.

셜록 핀이 문을 열자······

'어······?'

가지런히 둔 서류가
흩어져 있었어요.

깃털 펜도, 카드도
여기저기 옮겨져 있었어요.

'분명히 정리하고 갔는데?'
```

No music notes, no staff lines, no sound-wave symbols. No intruder, no creepy silhouette, no broken-open door.

## Page 03 Prompt

Generate A5 portrait page 03 with the emitted official office, Sherlock Fin, and approved door-gap v2 references.

Scene: inside the detective office. Sherlock Fin examines the closed shell door, handle, and latch. The door is closed; the handle and latch are intact; there are no forced-open marks. Sherlock Fin tilts their head with a curious detective expression, looking between the door and the lightly scattered papers. The approved v2 gap location may be hinted at the lower-right closing edge, but it must remain tiny and not yet highlighted like a final clue. The mood is calm investigation, not fear.

Place the cream rounded text panel at lower left. Render the exact Korean text:

```text
셜록 핀은 문을 보았어요.

문고리는 그대로,
잠금쇠도 그대로.

억지로 열린 흔적은
없었어요.

'누가 들어왔을까?
아니면,
무엇이 움직였을까?'

셜록 핀은 모자를
살짝 눌러썼어요.

'무서워하지 말고,
차근차근 알아보자!'
```

No music symbols. No water current yet. No intruder. No big crack or hole. Door gap only as a tiny lower-right edge hint if included.

## Batch 1 QA Checklist

- Door/gap follows v2 placement when visible: lower-right closing edge, not center bottom or hinge side.
- No music-note/current contamination anywhere.
- Office identity matches the official office reference.
- Sherlock Fin identity matches the official character reference.
- Text is present, readable, and matches the script without paraphrase.
- Page 01 is clearly tidy before-state.
- Page 02 is clearly next-morning discovery with intact door/latch.
- Page 03 is clearly calm door/latch inspection without fear.

## Batch 1 User QA Corrections - 2026-06-28

- Page 00 cover: title has a stray/incorrect glyph between `사` and `이` in `밤사이`; regenerate with exact title `밤사이 움직이는 것들` and no inserted mark, space, or extra character between `사` and `이`.
- Page 00 cover: Sherlock Fin has three arms; regenerate with exactly two arms and two hands.
- Page 01: candidate is mostly okay, but the door handle became a round knob attached near the middle of the door. Regenerate with the handle/latch attached at the proper side/closing-edge area, not a central round knob.
- Page 02: text is acceptable; issue is visual. Sherlock Fin holding the magnifying glass feels odd here. Regenerate with the magnifying glass not in hand, preferably resting on the desk or absent from the focal action.
- Page 03: Sherlock Fin again has three arms. Regenerate with exactly two arms and two hands.
- Page 03: because the text ends with `셜록 핀은 모자를 살짝 눌러썼어요.`, Sherlock Fin should hold or press the brim of the detective hat with one hand.

### New Batch 1 Locks

- Sherlock Fin anatomy: exactly two arms and two hands, no extra arms, no extra gloves, no duplicated hand silhouettes.
- Page 03 pose: one hand must be on the detective hat brim, gently pressing it down; the other hand should rest naturally or point subtly, but must not create a third arm.
- Door handle/latch: do not invent a central round knob. Keep a side-mounted brass latch/handle consistent with the office door reference.
- Page 02: no magnifying glass in Sherlock Fin's hand.

## Cover Regeneration Notes - 2026-06-28

- Do not use local text overlay for the cover unless the user asks again. User prefers the generated hand-lettered Korean title style.
- `00_candidate_text_v1.png`: rejected/hold for stray glyph between `사` and `이` in `밤사이`, plus extra-arm anatomy issue.
- `00_candidate_text_v2.png`: generated retry; improves `밤사이` and arm count, but `셜록 핀` spacing is too tight.
- `00_candidate_text_v3.png`: current preferred generated cover candidate; keeps flavorful title generation while improving `셜록 핀` spacing and preserving two-arm anatomy.
## Page 01-03 Object Continuity QA - 2026-06-28

- User identified a story-logic continuity issue across pages 01-03: only light objects should move overnight, while heavy objects must stay fixed.
- Baseline before-state: `01_candidate_text_v2.png`.
- Heavy object lock from page 01 to pages 02-03:
  - desk, chair, lamp, file holder, thick book/notebook, magnifying glass, ink bottle, and large desk tools must remain in the same locations and should not imply overnight movement.
- Light object movement lock from page 01 to pages 02-03:
  - loose papers, small cards, and the feather pen are the only objects that move.
  - They must look displaced from their page 01 positions, not duplicated as extra new floor props while originals remain untouched.
  - The pen holder/desk position should show the feather pen no longer neatly in place if the feather pen appears on the floor/rug.
- Page 03 must continue the same post-disturbance arrangement from page 02 while Sherlock Fin inspects the door and presses the detective hat brim.
## Batch 1 Continuity Regeneration Candidates - 2026-06-28

- `01_candidate_text_v2.png`: current page 01 baseline candidate. Door hardware corrected to a side latch/handle. Treat this as the tidy before-state item layout.
- `02_candidate_text_v2.png`: generated continuity retry; saved as history, but text looked slightly unstable on review.
- `02_candidate_text_v3.png`: current page 02 candidate. Sherlock Fin no longer holds the magnifying glass; heavy objects remain on/around the desk; loose papers, cards, and the feather pen are the moved light objects.
- `03_candidate_text_v2.png`: current page 03 candidate. Continues the page 02 disturbed light-object arrangement, removes the hand-held magnifying glass, uses exactly two arms/hands, and adds the hat-brim press pose.
- Current Batch 1 review set: `00_candidate_text_v3.png`, `01_candidate_text_v2.png`, `02_candidate_text_v3.png`, `03_candidate_text_v2.png`.
## Page 01-03 Desk-Locked Rework Plan - 2026-06-28

### User Direction

- Rework pages 01-03 only. Do not touch the cover.
- The desk must stay fixed across pages 01-03.
- Heavy objects do not change position: desk, chair, lamp, file holder, thick book/notebook stack, magnifying glass, ink bottle, pen holder, large desk tools.
- Only light objects move: loose papers, small cards, thin notes, and the feather pen.
- In pages 02-03, light objects should look as if they fell from the desk and spread onto the floor.
- The scattering should support the later deduction scene: use the shell door/lower-right door-gap area as the visual origin, with a gentle fan-shaped spread from the door toward the desk/floor.

### Approach Options

Recommended: regenerate 01-03 as a linked mini-batch using page 01 as a locked tidy anchor. This gives page 02 and page 03 a clear before/after relationship and makes the later "light objects only" deduction easier to see.

Alternative: keep `01_candidate_text_v2.png` and regenerate only 02-03. This is faster, but if the generator cannot preserve the exact desk from page 01, the continuity issue can remain.

Rejected for now: local compositing/text-only patch. The user is asking for object/layout continuity, not only text correction, and the pages need coherent lighting and illustration.

### Shared Hard Locks For 01-03

- Same detective office layout across all three pages.
- The shell desk must keep the same position, angle, size, and silhouette in all three pages.
- The chair behind the desk, bubble lamp, file holder, book/notebook stack, magnifying glass, ink bottle, pen holder, and large desk tools must remain in the same positions from page 01 through page 03.
- Do not add duplicate heavy objects. Do not move heavy objects to the floor.
- Loose papers, small cards, thin notes, and the feather pen are the only moved objects.
- If the feather pen appears on the floor in pages 02-03, its page 01 desk/holder position should look empty or no longer neatly filled. Do not show both an untouched feather pen in the holder and another feather pen on the floor.
- Pages 02 and 03 must share the same post-disturbance arrangement. Page 03 is an inspection moment after the page 02 discovery, not a new mess.
- Light objects should form a subtle fan/trail from the shell door's lower-right closing edge toward the desk and rug, consistent with a weak current entering from the door.
- Keep the door hardware side-mounted; no central round knob.
- No visible water current on pages 01-03 unless it is only a tiny, non-spoiling hint. No music notes, no sound-wave graphics, no jazz icon contamination.
- Sherlock Fin anatomy: exactly two arms and two hands.

### Page 01 Rework Prompt

Generate A5 portrait page 01 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official detective office reference, Sherlock Fin reference, approved door-gap v2 reference, textbox reference, and the current page 01 candidate as continuity guidance.

Scene: evening in Sherlock Fin's detective office. This page is the locked tidy before-state for the next two pages. Sherlock Fin is calmly finishing the office cleanup and closing the shell door. The shell desk is fixed in a clear, repeatable position and angle. On and around the desk, place the heavy objects in stable anchor positions that must be preserved in later pages: chair behind the desk, warm bubble lamp, file holder, thick book/notebook stack, yellow magnifying glass resting on the desk, small ink bottle, pen holder, and large desk tools. Loose papers are neatly stacked, small cards are squared, and the feather pen is neatly in its holder or exact desk position. The shell door appears properly closed; the side-mounted brass latch/handle is at the closing edge, not a central round knob. No water current is visible.

Place a cream rounded text panel at lower left, not covering Sherlock Fin's face, the door action, or the fixed desk anchors. Render the exact Korean text:

```text
하루가 끝나는 저녁이에요.

셜록 핀은 사무소를
깨끗이 정리했어요.

서류는 가지런히,
깃털 펜은 제자리에,
카드는 반듯하게.

그리고 조개 문을
딸깍, 꼭 닫고 집으로 갔어요.

'내일 또 보자, 사무소야!'
```

Avoid: moved heavy furniture, extra heavy objects, duplicate feather pens, water ribbons, music notes, scary tone, extra arms.

### Page 02 Rework Prompt

Generate A5 portrait page 02 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official detective office reference, Sherlock Fin reference, approved door-gap v2 reference, textbox reference, and the newly generated page 01 as the strict spatial anchor.

Scene: next morning discovery. Keep the shell desk, chair, bubble lamp, file holder, thick book/notebook stack, yellow magnifying glass, ink bottle, pen holder, and large desk tools in the same positions, scale, and angle as page 01. The door and latch are intact and still look closed/unchanged before Sherlock Fin opens or enters. Sherlock Fin has just opened the shell door and stops in surprise, curious rather than scared.

Only light objects have moved: loose papers, small cards, thin notes, and the feather pen. Show them as if they slid/fell from the desk and scattered onto the floor/rug. The arrangement should form a gentle fan-shaped trail whose origin is the lower-right closing edge of the shell door, spreading inward toward the desk and across the floor. The desk itself and all heavy objects must look unchanged, making it clear that a weak force moved only light things. If the feather pen is on the floor, the page 01 feather pen position on the desk/holder should look empty or disturbed, not duplicated.

Place a cream rounded text panel at upper right, not covering the door/latch or the fan-shaped scattered trail. Render the exact Korean text:

```text
다음 날 아침이에요.

조개 문은 어젯밤처럼
꼭 닫혀 있었어요.

잠금쇠도 그대로였지요.

셜록 핀이 문을 열자······

'어······?'

가지런히 둔 서류가
흩어져 있었어요.

깃털 펜도, 카드도
여기저기 옮겨져 있었어요.

'분명히 정리하고 갔는데?'
```

Avoid: moved desk, shifted chair, moved lamp, moved book stack, moved magnifying glass, moved ink bottle, duplicate feather pen, random all-over mess, large crack, visible culprit, music notes, water-current reveal, extra arms.

### Page 03 Rework Prompt

Generate A5 portrait page 03 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official detective office reference, Sherlock Fin reference, approved door-gap v2 reference, textbox reference, newly generated page 01, and newly generated page 02 as strict continuity anchors.

Scene: calm investigation inside the same office. The closed shell door, side latch/handle, and lock are visible and intact with no forced-open marks. Sherlock Fin looks between the closed door and the scattered light objects, pressing the brim of the detective hat with one hand. Sherlock Fin has exactly two arms and two hands; the other hand rests naturally or points subtly without creating an extra limb.

Keep all heavy objects fixed exactly as in pages 01-02: shell desk, chair, bubble lamp, file holder, thick book/notebook stack, yellow magnifying glass, ink bottle, pen holder, and large desk tools. Continue the same light-object arrangement from page 02: loose papers, small cards, thin notes, and the feather pen remain scattered on the floor/rug in the same fan-shaped pattern from the lower-right door edge toward the desk. Do not create a new different mess. The visual logic should clearly support the later deduction that the force came from the door and moved only light things.

Place a cream rounded text panel at lower left, not covering Sherlock Fin's hat-brim pose, the intact latch, or the scattered trail. Render the exact Korean text:

```text
셜록 핀은 문을 보았어요.

문고리는 그대로,
잠금쇠도 그대로.

억지로 열린 흔적은
없었어요.

'누가 들어왔을까?
아니면,
무엇이 움직였을까?'

셜록 핀은 모자를
살짝 눌러썼어요.

'무서워하지 말고,
차근차근 알아보자!'
```

Avoid: moved desk, shifted heavy objects, a new different scattered pattern, magnifying glass in Sherlock Fin's hand, central round door knob, visible water current reveal, music notes, scary intruder, extra arms.

### Rework QA Checklist

- Page 01 establishes the tidy before-state with a fixed desk and fixed heavy objects.
- Pages 02-03 preserve the same desk, chair, lamp, file holder, books, magnifying glass, ink bottle, pen holder, and large tools.
- Only loose papers, cards, notes, and the feather pen move.
- Pages 02-03 show moved light objects as falling/sliding from the desk to the floor, not as unrelated new props.
- Pages 02-03 use the door/lower-right gap area as the origin of a fan-shaped scatter pattern.
- Page 03 continues page 02's scattered arrangement while adding the intact-door inspection and hat-brim press.
- Korean text must match the script exactly and remain readable.
## Page 03 Door Handle Correction - 2026-06-28

- User QA: page 03 handle/latch was wrongly attached near the hinge side.
- New door lock for page 03 and later pages:
  - Hinges stay on the viewer-left side of the shell door.
  - Door handle/latch/lock must be on the viewer-right side of the shell door, on the closing edge, opposite the hinges.
  - The handle/latch must not touch the hinges and must not be attached to the hinge side.
  - Do not use a central round knob.
- `03_candidate_text_v4_reject_handle_on_hinge.png`: rejected/hold for handle/latch too close to hinge side.
- `03_candidate_text_v5_desk_lock_door_right_handle.png`: current page 03 review candidate. Handle/latch moved to viewer-right closing edge, heavy desk objects remain fixed, single feather pen remains on floor, and Sherlock Fin presses the hat brim with two-arm anatomy.
## Page 02-03 Paper Stack Reduction Correction - 2026-06-28

- User QA: pages 02-03 still keep the desk paper bundle intact while adding scattered papers only on the floor. This reads as duplicated extra papers, not actual movement.
- New light-paper lock:
  - The neat loose document stack from page 01 must be visibly reduced in pages 02-03.
  - Some of those same thin documents should be partly slid off the desk edge, some should remain askew on the desk, and some should continue onto the floor/rug.
  - Do not preserve a full neat stack of loose papers while also adding many floor papers.
  - It should look like the floor papers came from the desk paper stack.
- Heavy-object clarification:
  - Thick book/notebook stack, file holder, lamp, magnifying glass, ink bottle, pen holder, large desk tools, chair, and desk remain fixed.
  - Thin loose papers, small cards, notes, and the single feather pen are light moving objects.
- Page 02 next filename: `02_candidate_text_v5_reduced_desk_papers_door_fan.png`.
- Page 03 next filename: `03_candidate_text_v6_reduced_desk_papers_right_handle.png`.
## Clean-Session Page 02-03 Paper Stack Regeneration - 2026-06-28

Reason: continue from `handoff_2026-06-28_page02_03_paper_stack.md` after prior generation contamination. Cover and page 01 are excluded. Use `01_candidate_text_v3_desk_lock.png` as the stable tidy before-state anchor.

Target filenames:

- `02_candidate_text_v6_reduced_desk_papers_regen.png`
- `03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

Shared clean-session locks:

- The loose thin document stack visible on page 01 must be visibly reduced on pages 02-03.
- Do not show a full neat desk paper stack plus separate floor papers.
- Some original thin documents remain askew on the desk, some slide or hang over the desk edge, and some continue onto the floor/rug.
- The floor/rug papers must look like they came from the reduced desk stack.
- Keep heavy objects fixed: desk, chair, bubble lamp, file holder, thick book/notebook stack, magnifying glass, ink bottle, pen holder, and large desk tools.
- Only light objects move: thin papers, small cards, notes, and at most one feather pen.
- Scatter direction must support the later deduction: a gentle fan/trail from the door/lower-right closing-edge gap area toward the desk and rug.
- Door/gap rules remain from approved v2: lower-right closing edge; no center-bottom gap, no hinge-side handle.
- No water-current reveal, music notes, staff lines, sound-wave graphics, unrelated infographic/text contamination, scary intruder, duplicated props, or extra limbs.

Page 02 clean-regeneration prompt:

Generate A5 portrait page 02 for the children's picture book episode `밤사이 움직이는 것들`, using the emitted official detective office reference, Sherlock Fin reference, approved door/gap v2 reference, textbox reference, and `01_candidate_text_v3_desk_lock.png` as the strict spatial before-state anchor.

Scene: next morning discovery. Sherlock Fin opens the shell door and stops in surprise, curious rather than frightened. The door and latch are intact. Preserve the page 01 desk position and all heavy objects exactly: shell desk, chair, bubble lamp, file holder, thick book/notebook stack, yellow magnifying glass on the desk, ink bottle, pen holder, and large desk tools.

Correct the paper-stack issue explicitly: the page 01 loose thin document stack on the desk is no longer a full neat pile. It is visibly smaller and broken apart. A partial reduced pile remains on the desk, several sheets/cards are askew across the desktop, several thin papers slide or hang over the desk edge, and the same kind of papers continue onto the floor/rug in a gentle fan-shaped trail from the door/lower-right closing-edge direction toward the desk. The floor papers must read as displaced from the desk stack, not as extra new papers added while the desk stack stayed intact.

Place a cream rounded text panel at upper right. Render the exact Korean text:

```text
다음 날 아침이에요.

조개 문은 어젯밤처럼
꼭 닫혀 있었어요.

잠금쇠도 그대로였지요.

셜록 핀이 문을 열자······

'어······?'

가지런히 둔 서류가
흩어져 있었어요.

깃털 펜도, 카드도
여기저기 옮겨져 있었어요.

'분명히 정리하고 갔는데?'
```

Page 03 clean-regeneration prompt:

Generate A5 portrait page 03 for the children's picture book episode `밤사이 움직이는 것들`, using the emitted official detective office reference, Sherlock Fin reference, approved door/gap v2 reference, textbox reference, `01_candidate_text_v3_desk_lock.png`, and the new page 02 candidate as continuity anchors.

Scene: calm investigation inside the same office. The shell door is closed; hinges are on viewer-left, and the handle/latch/lock are on the viewer-right closing edge, opposite the hinges. There are no forced-open marks. Sherlock Fin presses the detective hat brim with one hand and looks between the intact door and the scattered light objects. Sherlock Fin has exactly two arms and two hands.

Continue the page 02 paper correction: the desk loose document stack remains visibly reduced, not intact. Some thin papers remain askew on the desk, some slide/hang over the desk edge, and the floor/rug papers continue the same door-centered fan/trail. Preserve all heavy objects exactly: desk, chair, lamp, file holder, thick books, magnifying glass, ink bottle, pen holder, and large tools. Do not duplicate the feather pen; if it appears on the floor, it should not also remain upright in the holder.

Place a cream rounded text panel at lower left. Render the exact Korean text:

```text
셜록 핀은 문을 보았어요.

문고리는 그대로,
잠금쇠도 그대로.

억지로 열린 흔적은
없었어요.

'누가 들어왔을까?
아니면,
무엇이 움직였을까?'

셜록 핀은 모자를
살짝 눌러썼어요.

'무서워하지 말고,
차근차근 알아보자!'
```

## Page 02 Gaze Direction Correction - 2026-06-29

- User QA on `02_candidate_text_v6_reduced_desk_papers_regen.png`: Sherlock Fin looks toward empty space rather than actually looking at the messy office.
- Regenerate page 02 only.
- Preserve from v6:
  - fixed desk/heavy-object continuity,
  - reduced loose-paper stack on the desk,
  - thin papers/cards continuing from desk to floor,
  - moved feather pen/card evidence,
  - text panel position and story text as much as possible.
- New page 02 lock:
  - Sherlock Fin's face direction and pupils must turn into the office interior, aimed clearly at the scattered papers/cards and the desk mess.
  - Do not let Sherlock Fin look at the viewer, toward the outside doorway, toward the text panel, or into empty air.
  - Use a slight side/three-quarter head turn, lowered gaze line, or leaning-in discovery pose so the eyeline is unambiguous.
- Next candidate: `02_candidate_text_v7_gaze_into_office.png`.

## Page 02 Gaze Direction Regeneration - 2026-06-29

- User QA on `batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`: Sherlock Fin's face/gaze looked like she was staring into empty space rather than looking into the messy office.
- Regenerated page 02 only.
- Intermediate candidate:
  - `batch_1/02_candidate_text_v7_gaze_into_office.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0180cb1eefecc665016a413974545c8191afe7e8b704577051.png`
  - Dimensions: 1054x1492.
  - SHA256: `F8976CB6C803B66E6F9AB136E0FF94E176A907A9C55C59D98A69FCEA4FB452DC`.
  - Status: hold. Gaze direction improved, but QA found possible duplicate feather-pen reading, with one feather on the floor and another quill-like object near the desk holder.
- Current page 02 candidate:
  - `batch_1/02_candidate_text_v8_gaze_into_office_single_feather.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0f56315c43eb5f16016a413aac7a6c8191bbb224b154c66f70.png`
  - Dimensions: 1054x1492.
  - SHA256: `DA6F2879BB6B0CC2969C02C30BFFBD8C3980BC9D04E91F971BE663E8E2DCE477`.
  - QA: Sherlock Fin's face and pupils now read as looking inward/downward toward the messy floor papers and desk, not into empty air; one feather pen appears displaced on the floor/rug; desk/heavy objects remain fixed; loose papers/cards still read as a trail from the desk.
- Updated current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v8_gaze_into_office_single_feather.png`
  - `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

## Page 02 Mixed Preference Correction - 2026-06-29

- User QA after v7/v8 comparison: desk/table state is better in the second candidate (v8), while Sherlock Fin is better in the first candidate (v7).
- Next candidate should combine:
  - Sherlock Fin from v7: better facial direction, pose, and discovery feeling.
  - Desk/paper state from v8: better desk state, paper trail, and single displaced feather pen logic.
- Avoid local cut-and-paste compositing unless necessary; prefer full-page regeneration so character and room lighting remain natural.
- Next candidate: `02_candidate_text_v9_v7_sherlock_v8_desk.png`.

## Page 02 Door Hinge Visibility Correction - 2026-06-29

- User QA on `02_candidate_text_v9_v7_sherlock_v8_desk.png`: the door angle makes visible hinge barrels/hinge plates physically wrong.
- Regenerate page 02 only; keep full-page generation rather than panel replacement.
- Preserve the v7 Sherlock Fin strengths: face direction, gaze into the messy office, and surprised discovery pose.
- Preserve the v8 desk/table strengths: reduced desk-paper stack, papers/cards continuing from desk to floor, and one displaced feather pen.
- New hard lock: in this open-door view, the shell door's hinge side is hidden behind the door leaf/jamb. Do not show exposed brass hinge barrels, hinge plates, or vertical hinge hardware on the visible face or exposed edge.
- Visible door hardware should be only the latch/handle on the closing edge. No central knob.
- If the hinge side must be implied, hide it in the shadow/overlap between the door and frame so it does not read as visible hardware.
- Next candidate: `02_candidate_text_v10_no_visible_hinge.png`.

## Page 02 No-Visible-Hinge Regeneration - 2026-06-29

- Saved page 02 candidate: `batch_1/02_candidate_text_v10_no_visible_hinge.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0efbb8c848a5eb19016a413f9f096c819195ee65be34070aee.png`
  - Dimensions: 1054x1492.
  - SHA256: `C6C820FAA1C4DB28345527F72120A10802F174F4172199321493564191A7DCD8`.
  - QA: open shell door no longer shows exposed hinge barrels, hinge plates, or vertical brass hinge hardware; the door angle reads more physically natural. Visible hardware is limited to the closing-edge handle/latch area. Sherlock Fin keeps a v7-like surprised inward gaze toward the messy office. Desk/table state remains close to v8 with fixed heavy objects, a reduced/askew paper state, floor cards/papers, and a single displaced feather pen.
- Current page 02 candidate: `batch_1/02_candidate_text_v10_no_visible_hinge.png`.
- Updated current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v10_no_visible_hinge.png`
  - `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`
