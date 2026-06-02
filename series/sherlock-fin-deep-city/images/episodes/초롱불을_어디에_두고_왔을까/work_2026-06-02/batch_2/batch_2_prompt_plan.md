# Batch 2 Prompt Plan - 초롱불을 어디에 두고 왔을까

## Scope

- Episode: `초롱불을 어디에 두고 왔을까`
- Batch: pages 4-7 only
- Work folder: `series/sherlock-fin-deep-city/images/episodes/초롱불을_어디에_두고_왔을까/work_2026-06-02/batch_2`
- Candidate filenames:
  - `04_candidate_text_v1.png`
  - `05_candidate_text_v1.png`
  - `06_candidate_text_v1.png`
  - `07_candidate_text_v1.png`

## Official References

Use the actual image files as visual truth. Do not generate from prose alone.

- Characters:
  - `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_초롱이_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_가게주인_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_해마친구_레퍼런스.png`
- Props:
  - `series/sherlock-fin-deep-city/references/props/초롱불을_어디에_두고_왔을까_불씨구슬_레퍼런스.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/locations/초롱불을_어디에_두고_왔을까_미역숲쉼터_레퍼런스.png`

## Shared Visual Rules

- A5 portrait page proportion, about `1:1.414`, for all interior page candidates.
- Include the approved Korean page text directly in the image from the first generation pass.
- Use one clean cream or shell-light text panel with rounded corners, thin border, and generous margins, following the text layout reference.
- Keep the Sherlock Fin series style: bright warm underwater Deep City, coral buildings, shell doors, bubble streetlamps, gentle neon, warm window lights, no horror.
- Evening darkness must feel cozy and safe, not scary.
- Chorong must follow the approved reference: round dark-blue baby anglerfish body, big eyes, teal/gold fins, head lantern shape. Tiny cute teeth are allowed only if harmless; do not enlarge the mouth or make teeth sharp.
- Chorong's lantern state must be exact:
  - Page 04 present: dark/empty lantern.
  - Page 05 present and recall bubble: dark/empty lantern.
  - Page 06 present and recall bubble: dark/empty lantern.
  - Page 07 present: dark/empty lantern; recall bubble: Chorong's head lantern is also dark/empty while Chorong cleans the removed flame bead. The warm light comes from the bead only.
- Do not reveal the solution before page 07. Pages 04-06 must not show the flame bead outside Chorong's lantern.
- Recall bubbles must be clear but secondary; do not let them become separate comic panels with extra text.
- Sherlock Fin must follow the official sheet: teal hair, brown detective hat and coat, teal mermaid tail, black gloves, yellow magnifying glass or small notebook as the scene requires.
- PopPop must keep the official look: round yellow pufferfish, black sunglasses, teal headphones.
- Shopkeeper must stay cute and friendly, not insect-like or unpleasant.
- Seahorse friend must read kind and helpful, not guilty, sneaky, or scary.
- Avoid extra signage, pseudo-writing, invented labels, speech bubbles outside the approved text, watermarks, unrelated prior-episode details, and over-glossy neon drift.

## Page Prompt Records

### 04 Page 4

- Candidate: `04_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, detective office interior, Deep City route mood, layout.
- Scene prompt: Sherlock Fin's detective office. Sherlock Fin and Chorong look down together at a small notebook. In the notebook, a simple child-readable route map connects seaweed rest area, shell snack shop, jazz plaza, and detective office. Sherlock Fin points with a pen at the detective office side, the most recent place, and draws reverse arrows from office back toward plaza, shop, and seaweed rest area. Chorong watches with curious hopeful eyes. Chorong's head lantern is dark and empty. Overhead slightly downward view focused on the notebook and the two friends. Text panel at the top.
- Continuity locks: route direction must communicate reverse thinking; do not show the flame bead. The map can use icons rather than readable labels to avoid pseudo-writing.
- Text:

```text
셜록 핀이 말했어요.

'처음부터 찾지 말고,
거꾸로 가 보자.

지금 막 어디에서 왔어?'

'광장이요!'

'그럼 광장부터.
거기서 한 걸음씩
뒤로 거슬러 가 보는 거야.'
```

### 05 Page 5

- Candidate: `05_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, PopPop, Deep City/Jazz Plaza, layout.
- Scene prompt: Jazz Plaza in cozy early evening. Bubble streetlamps are on, warm coral windows glow, no scary darkness. Sherlock Fin and Chorong meet PopPop. PopPop lowers the teal headphones slightly and remembers Chorong with a thoughtful expression. Above PopPop, a soft recall bubble shows Chorong passing through the plaza already dark; the recall Chorong's head lantern is clearly off and empty. Present Chorong's lantern is also dark. Medium shot of the three friends in the plaza. Text panel in lower left.
- Continuity locks: PopPop has black sunglasses and teal headphones. The recall bubble must show dark Chorong, not glowing Chorong. Do not show the flame bead.
- Text:

```text
먼저 광장으로 갔어요.

팝팝에게 물었어요.

'초롱이가 광장을 지날 때
초롱불이 환했어?'

팝팝이 고개를 저었어요.

'아니, 그때도 어두웠어.
그래서 내가 물어봤는걸.
왜 초롱이 어둡지? 하고.'

'음, 광장에 올 때
이미 꺼져 있었구나.
더 거슬러 가 보자!'
```

### 06 Page 6

- Candidate: `06_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, shopkeeper, Deep City/shell snack shop mood, layout.
- Scene prompt: In front of a shell snack shop in cozy evening. The shop glows with warm lights. Sherlock Fin and Chorong ask the small friendly pom-pom shopkeeper. Above the shopkeeper, a soft recall bubble shows Chorong arriving at the shop already dark, with the shopkeeper brightening the shop lights to help. Both present Chorong and recall Chorong have dark empty head lanterns. Medium shot at the shop front. Text panel in upper right.
- Continuity locks: shopkeeper must stay cute and warm. The shop lights are brightened in the recall bubble, but Chorong's lantern remains off. Do not show the flame bead.
- Text:

```text
이번에는 조개 간식 가게로 갔어요.

가게 주인에게 물었어요.

'초롱이가 왔을 때
초롱불이 환했나요?'

가게 주인이 말했어요.

'아니요, 그때도 어두웠어요.
그래서 제가 가게 불을
더 밝혀줬는걸요.'

'가게에 올 때도
이미 꺼져 있었구나.
더, 더 거슬러 가 보자!'
```

### 07 Page 7

- Candidate: `07_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, seahorse friend, seaweed rest area, flame bead, layout.
- Scene prompt: Cozy seaweed rest area with soft waving kelp and a small central rock. On the central rock, the warm yellow-gold flame bead is clearly visible and sparkling. Sherlock Fin and Chorong meet the small friendly seahorse friend. The seahorse looks kind and helpful. Above the seahorse, a soft recall bubble shows Chorong at the rock cleaning the removed glowing flame bead; recall Chorong's head lantern is dark/empty. Present Chorong's head lantern is still dark/empty, but Chorong's expression begins to brighten as everyone notices the bead. Medium shot with all eyes leading to the bead on the rock. Text panel in upper left.
- Continuity locks: this is the first batch 2 page where the flame bead may appear. The bead must match the prop reference: small warm yellow-gold bead, not a pearl, gem, or open flame. The central rock must match the seaweed rest area reference.
- Text:

```text
마지막으로 미역 숲 쉼터로 갔어요.

해마 친구가 말했어요.

'아까 초롱이가 여기서
반짝이는 구슬을 닦고 있었어!

내가 부르니까
좋아서 폴짝 일어나던데?'

그때, 바위 위를 보았어요.

반짝, 반짝.

'아! 불씨 구슬이다!'
```

## QA Checklist

- [x] Text is included in each image and remains readable.
- [x] Page 04 clearly shows reverse route thinking without revealing the answer.
- [x] Page 05 recall bubble shows Chorong already dark in Jazz Plaza.
- [x] Page 06 recall bubble shows Chorong already dark at the shop while shop lights are brightened.
- [x] Page 07 shows the central rock, the flame bead, and recall Chorong cleaning the removed glowing bead while Chorong's head lantern stays dark/empty.
- [x] Chorong follows the official reference and the lantern state is correct on every page.
- [x] Sherlock Fin follows the official reference on every page.
- [x] PopPop, shopkeeper, and seahorse match their official references.
- [x] Evening mood stays cozy and safe, not scary.
- [ ] No unrelated prior-episode content, random signage, pseudo-writing, watermark, or glossy style drift.

## Batch 2 QA Notes

| Candidate | Status | QA notes |
| --- | --- | --- |
| `04_candidate_text_v1.png` | Candidate pass | Reverse-route notebook is clear, arrows move backward from office/plaza toward shop/rest area, and no flame bead is revealed. Text is readable with minor generator-normalized line breaks. |
| `05_candidate_text_v1.png` | Candidate pass with caution | PopPop identity is strong, recall bubble shows dark Chorong, and present Chorong is dark. Background includes readable English Jazz signage; acceptable only if the Batch 1 signage tolerance carries forward. Text is readable but slightly shortened/normalized. |
| `06_candidate_text_v1.png` | Candidate pass with text caution | Shopkeeper identity and warm shop lights are strong. Recall bubble shows dark Chorong while the shopkeeper brightens the shop lights. Text is readable but notably shortened/normalized against the exact script. |
| `07_candidate_text_v1.png` | Superseded after user revision | Central rock, flame bead, seahorse, and dark present Chorong were clear, but the recall bubble incorrectly lit Chorong's head lantern. Text was readable but shortened/normalized against the exact script. |

## Batch 2 Gate

- Generate only pages 04-07.
- Save candidates in this folder only.
- Do not promote to `final` until QA notes are recorded and the user approves the batch.
- Do not start pages 08-11 until Batch 2 has QA notes and user approval.

## 2026-06-02 User Revision Notes

Batch 2 is not ready for set approval yet. Keep pages 04 and 06 as active candidates unless the user requests further changes. Pages 05 and 07 need revised candidates.

| Candidate | Updated status | Required fix |
| --- | --- | --- |
| `05_candidate_text_v1.png` | Hold - retry required | PopPop has generated human-like hands/gesture appendages. Corrected page must keep PopPop as a round yellow pufferfish with black sunglasses and teal headphones, but with no arms, no hands, no fingers, and no pointing/raised-hand gesture. Show reaction through body tilt, mouth shape, sunglasses/headphones, and posture only. |
| `07_candidate_text_v1.png` | Hold - retry required | The recall bubble currently makes Chorong's head lantern glow. Correct logic: Chorong has taken the flame bead out to wipe it, so recall Chorong's head lantern must be dark/empty. The warm light in the recall bubble must come only from the flame bead being cleaned. Present Chorong's lantern also remains dark/empty. |

### Revision Candidate Targets

- Create `05_candidate_text_v2.png` from page 05 with PopPop's hands removed or regenerated away.
- Create `07_candidate_text_v2.png` from page 07 with both present and recall Chorong lanterns dark/empty; only the removed flame bead glows.
- Do not promote `05_candidate_text_v1.png` or `07_candidate_text_v1.png` to final.
- Do not start pages 08-11 until revised page 05 and page 07 candidates are QA'd and user approved.

## 2026-06-02 Revision Candidate QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `05_candidate_text_v2.png` | Candidate pass | PopPop no longer has human-like hands, fingers, pointing, or raised-hand appendages. PopPop remains a round yellow pufferfish with black sunglasses, teal headphones, and side fins only. Present and recall Chorong lanterns remain dark/empty. Text remains readable. |
| `07_candidate_text_v2.png` | Candidate pass | Recall Chorong's head lantern is now dark/empty while Chorong cleans the removed flame bead. The warm light in the recall bubble comes from the bead, not the head lantern. Present Chorong's head lantern remains dark/empty. Central rock, visible bead, seahorse, and text remain clear. |

Current Batch 2 approval set:

- `04_candidate_text_v1.png`
- `05_candidate_text_v2.png`
- `06_candidate_text_v1.png`
- `07_candidate_text_v2.png`

## 2026-06-02 Batch 2 Approval

User approved Batch 2 after revision QA. Approved candidates were promoted to final:

- `04_candidate_text_v1.png` -> `final/04_페이지.png`
- `05_candidate_text_v2.png` -> `final/05_페이지.png`
- `06_candidate_text_v1.png` -> `final/06_페이지.png`
- `07_candidate_text_v2.png` -> `final/07_페이지.png`

Rejected/held candidates:

- `05_candidate_text_v1.png`: superseded because PopPop had generated human-like hands.
- `07_candidate_text_v1.png`: superseded because recall Chorong's head lantern was lit when it should be dark/empty.

Next gate: do not start or promote pages 08-11 until the next batch plan is created with the carried-forward locks from this approval.
