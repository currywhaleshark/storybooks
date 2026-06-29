# 밤사이 움직이는 것들 - Batch 2 Prompt Plan

## Batch Scope

- Pages: 04-06
- Output folder: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_2`
- Candidate filenames:
  - `04_candidate_text_v1.png`
  - `05_candidate_text_v1.png`
  - `06_candidate_text_v1.png`

## Actual References To Emit Before Generation

Use `nodeRepl.emitImage` for actual PNGs before generation. Do not rely on local path text alone.

- Official office interior: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- Approved door/gap/water-current v2: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- Sherlock Fin character: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Textbox layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Current page 02 disturbance anchor: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`
- Current page 03 inspection anchor: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

Do not emit the broader Deep City jazz reference for Batch 2. It previously encouraged music-note contamination.

## Shared Visual Rules

- A5 portrait children's picture book page, warm polished Korean illustration.
- Match the official detective office: shell/coral architecture, shell desk, clue board, shell door, bubble lamps, cozy deep blue-purple walls.
- Sherlock Fin must match the official character sheet: teal hair, detective cap, brown coat, teal mermaid tail, curious child detective expression.
- Use a cream/shell-colored rounded text panel following the textbox reference.
- Continue the current post-disturbance state from pages 02-03: the desk loose-paper pile is reduced, some light papers/cards are on the desk, some hang/slide over the desk edge, and some continue on the rug/floor.
- Heavy objects remain fixed unless Sherlock is actively touching them for investigation: shell desk, chair, bubble lamp, file holder, thick book/notebook stack, yellow magnifying glass, ink bottle, pen holder, and large desk tools.
- The story logic must stay visible: light objects moved; heavy objects did not move overnight.
- Sherlock Fin anatomy: exactly two arms and two hands.
- No scary intruder, no culprit silhouette, no horror tone.
- No unrelated previous episode content or infographic contamination.
- No music notes, staff lines, sound-wave graphics, saxophone shapes, neon music icons, or decorative audio symbols.
- Water current appears only on page 06 and only as translucent pale-blue water ribbons, faint ripples, and small bubbles.

## Page 04 Prompt

Generate A5 portrait page 04 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official office, Sherlock Fin, textbox, and current page 02/03 anchors. Scene: inside the detective office after the discovery. Sherlock Fin calmly observes which objects moved. The composition should clearly compare light moved objects versus heavy unchanged objects.

Visual evidence: circle or gently highlight the light moved objects: thin papers, small cards, a feather pen, and thin notes scattered from the desk toward the rug/floor. Mark or visually tag the heavy unchanged objects as stable: yellow magnifying glass, thick book/notebook stack, small ink bottle, and shell desk. If small labels appear, the only readable label should be `그대로`; do not add extra explanatory text outside the story panel. The yellow magnifying glass should preferably remain on the desk as an unchanged heavy object, not in Sherlock Fin's hand, to avoid confusing the clue. Sherlock Fin may hold or point at the feather pen/small card while thinking.

Keep the post-disturbance paper logic from pages 02-03: reduced desk pile, askew papers on desk, papers hanging over the desk edge, and papers/cards continuing onto the rug. No water current visible yet.

Place the cream rounded text panel at upper right, not covering Sherlock Fin's face or the evidence comparison. Render exact Korean text:

```text
먼저 잘 보자.

무엇이 움직였을까?

움직인 건······
종이, 카드,
깃털 펜, 얇은 메모지.

모두 가벼운 것들이에요.

무거운 돋보기랑
두꺼운 책,
작은 잉크병은
그대로 있었어요.

'무거운 건 그대로야.
가벼운 것만 움직였어.

그럼 힘이
아주 약했겠구나.

첫 번째 단서!'
```

Avoid: moved heavy objects, magnifying glass in Sherlock Fin's hand if it makes the clue unclear, duplicate feather pens, water current reveal, music symbols, extra arms, unreadable or paraphrased Korean text.

## Page 05 Prompt

Generate A5 portrait page 05 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official office, Sherlock Fin, textbox, approved door/gap reference, and current page 02/03 anchors. Scene: Sherlock Fin studies the direction of the moved light objects. The scattered papers, feather pen, small cards, and notes should all lean or point in one clear direction: from the shell door/lower-right door-edge area toward the desk and rug.

Visual evidence: draw one or more soft, child-friendly directional arrows over the floor/rug and desk-edge trail, showing movement from the door side toward the desk. The arrows are deduction graphics, not actual water. Do not show visible water current yet. Sherlock Fin looks toward the door, following the arrow back to its starting point. The office remains calm and cozy.

Continue the reduced paper-stack logic from pages 02-03. Heavy objects stay fixed. The scattered light objects must not look random; they should form one readable directional pattern.

Place the cream rounded text panel along the bottom, with enough margin and not covering the door origin or the arrow path. Render exact Korean text:

```text
이번에도 잘 보자.

물건들이 어느 쪽으로
움직였을까?

종이도,
깃털 펜도,
작은 카드도
모두 같은 방향으로
쏠려 있었어요.

문 쪽에서
책상 쪽으로.

'아무렇게나 어질러진 게 아니야.

한 방향에서 오는 힘이야.

그 힘이 시작된 쪽은······
저기, 문이구나!

두 번째 단서!'
```

Avoid: random all-over mess, arrows going opposite directions, visible water current reveal, moved heavy objects, music symbols, scary intruder, extra arms, unreadable or paraphrased Korean text.

## Page 06 Prompt

Generate A5 portrait page 06 for the children's picture book episode `밤사이 움직이는 것들`.

Use the emitted official office, approved door/gap/water-current v2 reference, Sherlock Fin character, and textbox reference. Scene: close near the shell door. Sherlock Fin examines the bottom of the closed shell door with focused curiosity. The hinges are slightly loose, and a tiny gap is visible at the lower-right closing edge where the door leaf meets the frame/floor area. The gap must be tiny, not a big crack or open doorway.

Visual evidence: include a magnifying-glass inset or close-up bubble showing the small lower-right door gap and loose hinge detail. Sherlock Fin gently places one hand near the gap and feels a tiny current. Show the first clear water-current reveal: translucent pale-blue water ribbons, faint ripples, and small bubbles entering softly through the tiny gap. The water must be gentle and safe, not a flood or wave.

Door lock: handle/latch remains on the viewer-right closing edge, hinges on viewer-left. No central knob, no handle on hinge side. No music-note contamination.

Place the cream rounded text panel at upper left, not covering the door gap, Sherlock Fin's hand, or the magnifying inset. Render exact Korean text:

```text
셜록 핀은 문으로 갔어요.

문 아래를 자세히 보니······

어라?

경첩이 헐거워져서,
문을 닫아도
작은 틈이 생겨 있었어요.

틈에 손을 대보니,

솔솔—

작은 물살이
들어오고 있었어요.

'문 아래에서
힘이 들어오고 있어.

세 번째 단서!'
```

Avoid: large hole, broken-open door, scary tone, strong wave/flood, music notes, staff lines, sound-wave graphics, saxophone shapes, extra limbs, wrong handle side, unreadable or paraphrased Korean text.

## Batch 2 QA Checklist

- Page 04 clearly separates moved light objects from unchanged heavy objects.
- Page 04 does not visually imply that heavy objects moved overnight.
- Page 05 shows one consistent direction: door side toward desk/rug.
- Page 05 uses arrows as deduction graphics, not visible water current.
- Page 06 shows the approved tiny lower-right door gap and loose hinge logic.
- Page 06 water current is gentle blue water/ripples/bubbles only, with no music symbols.
- Door hardware remains physically plausible.
- Sherlock Fin has exactly two arms and two hands.
- Text panels are present, readable, and match the script as closely as generator text allows.

## Page 06 Anatomy QA Correction - 2026-06-28

- User QA: `06_candidate_text_v1_hold_text.png` text is acceptable, but Sherlock Fin has three visible hands/arms: one holding the magnifying glass, one touching the door gap/floor, and one extra hand resting near the knee.
- Root cause: the page 06 prompt allowed a crouching/leaning pose while assigning one hand to the gap and the other to the magnifying glass, leaving room for the model to invent a support/knee hand.
- Correction lock for page 06 and later regenerations:
  - Exactly two visible arms total.
  - Exactly two visible hands total.
  - One hand holds the yellow magnifying glass.
  - One hand gently touches the tiny lower-right door gap / floor-current area.
  - No hand on knee, no hand on lap, no extra support hand on floor, no third glove silhouette.
- Rejected/hold: `06_candidate_text_v1_hold_text.png` for extra hand/anatomy.
- Current corrected candidate: `06_candidate_text_v2_two_hands.png`.
