# Batch 3 Prompt Plan - 토리야, 한 걸음만 - Rework 2026-06-18

## Batch Scope

- Output folder: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3`
- Pages:
  - `07_candidate_2026-06-18_v1.png`
  - `08_candidate_2026-06-18_v2.png`
  - `09_candidate_2026-06-18_v1.png`
- Workflow:
  - Generate one page at a time.
  - The built-in image preview may not create an accessible file under `C:/Users/USER/.codex/generated_images`.
  - After each generation, manually download or directly save the displayed image, then copy it into this folder with the stable candidate filename above.

## Approved Continuity Context

- Approved Batch 2 candidates:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/04_candidate_2026-06-18_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/05_candidate_2026-06-18_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`
- Use these for current-episode style, text layout, character scale, and tunnel continuity only.
- Official character, playground, and tunnel reference images remain the visual truth.
- Rejected 6-page candidate `06_candidate_2026-06-18_v1_reject_l_tunnel_style_drift.png` is a negative reference only.

## Shared Visual Rules

- Format: A5 portrait, about `1:1.414`.
- Style: match approved Batch 2 pages 4-6: low-saturation pastel watercolor, warm Coral Town Daycare mood, soft safe toddler picture-book lighting.
- Text workflow: include the exact Korean story text in the first generation pass, with readable spacing and a clean side or upper text area.
- Do not use earlier `final`, `work_2026-06-03`, or `work_2026-06-06` episode images as visual truth.
- No unrelated character substitutions, no rabbit/dolphin/clownfish replacements for the official cast.
- No bags during playground play or tunnel exploration.
- No human legs, adult feet, cropped human body parts, pseudo text, decorative fake Korean, misspelled proper names, or paraphrased story text.

## Shared Tunnel Locks

- Required tunnel reference: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Approved page-6 tunnel layout reference: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`
- The tunnel must remain a single straight, low toddler crawl-through tube.
- Prioritize side-view/crawling-view scale: Tori must lower his head/body to enter.
- Do not display both exterior openings in the same page unless a later page explicitly needs it and the user approves.
- Treat script mentions of the opposite side or light as warm interior glow, not as a visible second exit arch.
- Forbidden: L shape, corner bend, side branch, second tunnel, same-facing double openings, cave mound, oversized corridor, dark scary cave.

## Page 07 - 머리만 살짝, 들여다볼까

### Candidate

- Save as: `07_candidate_2026-06-18_v1.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Style/continuity: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`

### Exact Page Text

```text
토리는 터널 앞으로
천천히 갔어요.

그리고 머리만
살짝—

안을 들여다봤어요.

마리 선생님이
조용히 말했어요.

"천천히 봐도 돼."

토리는 가만히
안을 보았어요.
```

### Prompt

Attach the official references listed above. Create an A5 portrait Korean children's picture-book page in the same soft pastel watercolor style as the approved Batch 2 pages. In the Coral Town Daycare playground, Tori slowly approaches the low straight coral tunnel and puts only his head slightly into the single visible round entrance to look inside. Tori's shell and body remain outside the entrance; only his face/head is just inside. His eyes are round with both nervousness and curiosity. Mari teacher sits or kneels beside the entrance, calmly watching and reassuring him, not pushing or touching him. Banguli waits inside the tunnel near the entrance, softly glowing as a small pale-blue bubble friend. The inside of the tunnel is dim but warm and safe, with a gentle warm glow deeper inside and tiny shell details on the wall. Show only one visible tunnel entrance; do not show the far exit arch. Leave a clean readable text area and render the exact Korean page text verbatim.

### QA Focus

- Tori's head only is inside; body and shell stay outside.
- Mari supports quietly; no pressure, pulling, or blocking.
- Banguli is inside as a soft guide.
- Exactly one tunnel entrance is visible; no L shape or second exit.

## Page 08 - 어? 무섭지 않네!

### Candidate

- Rejected: `08_candidate_2026-06-18_v1_reject_oversized_tunnel.png`
- Save next candidate as: `08_candidate_2026-06-18_v2.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Style/continuity: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`

### Exact Page Text

```text
그런데……

터널 안은
어둡지 않았어요.

반대편 구멍으로
따뜻한 빛이
들어왔어요.

벽에는 작은 조개가
반짝 반짝.

"어?
무섭지 않네!"

"오히려……
예쁘다!"
```

### Prompt

Attach the official references listed above. Create an A5 portrait Korean children's picture-book page in the same approved Batch 2 and page-7 pastel watercolor style. Show Tori discovering that the inside of the low straight coral tunnel is not scary. Use an outside-the-entrance view or shallow entrance view, not a large interior cave view. Tori is still mostly outside the tunnel, with only his head and front upper body near or just inside the single visible entrance. His shell remains partly outside and the low entrance should be only a little taller than Tori's crouched head and shell; he must clearly need to crouch to look in. Tori's eyes soften from worry into surprise and relief, and his mouth is slightly open as if saying "oh." Inside the same straight tube, small shells on the wall glow softly and tiny bubbles catch the warm light. Banguli floats just inside the tunnel near Tori, smiling brightly and welcoming him. The warm light from the opposite side should appear only as a soft golden glow deeper inside the tunnel, not as a visible exterior exit arch or a second round opening. The tunnel must stay low, cozy, and toddler-sized like page 6 v2 and page 7, not enlarged into a cave corridor. Leave a clean readable text area and render the exact Korean page text verbatim.

### QA Focus

- Tori's expression changes from worry to relief and discovery.
- Interior is warm and pretty, with small shells and gentle light.
- Banguli welcomes Tori from inside.
- Do not show a second exterior exit arch, L shape, broad corridor, or scary cave.
- Reject if the tunnel entrance is taller than Mari, reads as building-sized, or lets Tori stand/crawl fully inside without crouching.

## Page 09 - 한 걸음, 또 한 걸음

### Candidate

- Save as: `09_candidate_2026-06-18_v1.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Style/continuity: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`

### Exact Page Text

```text
토리는 입을
꼭 다물었어요.

그리고
한 걸음—

또 한 걸음—

등껍질이
쏙 들어갔어요.

방울이가 앞에서
길을 알려 줬어요.

'이쪽이야,
조금만 더!'

토리는 천천히
나아갔어요.
```

### Prompt

Attach the official references listed above. Create an A5 portrait Korean children's picture-book page in the same approved Batch 2 pastel watercolor style. Tori finally begins to enter the low straight coral tunnel. Show him moving forward slowly, one step and then another, with his round shell slipping into the single visible entrance. Tori's mouth is gently closed in concentration; he still looks cautious but determined. Banguli floats ahead inside the same tunnel, guiding him with a friendly "this way" feeling and two or three tiny bubbles. The tunnel interior has warm soft light and small shell details, safe and cozy, not scary. Use a side-view or slightly rear-side view that shows movement into the tube and the scale: Tori must crouch or lower his head to fit. Show only the entrance behind/around him and warm interior glow ahead; do not show a separate exterior far exit arch. Leave a clean readable text area and render the exact Korean page text verbatim.

### QA Focus

- Tori is now entering, but slowly and cautiously.
- His shell is going into the tunnel; this is the first real forward movement.
- Banguli leads from inside, ahead of Tori.
- Tunnel stays one low straight tube; no second visible exit, L shape, cave corridor, or oversized scale.
