# Batch 3 Prompt Plan - 초롱불을 어디에 두고 왔을까

## Scope

- Episode: `초롱불을 어디에 두고 왔을까`
- Batch: pages 8-11 only, plus final episode QA after user approval
- Work folder: `series/sherlock-fin-deep-city/images/episodes/초롱불을_어디에_두고_왔을까/work_2026-06-02/batch_3`
- Candidate filenames:
  - `08_candidate_text_v1.png`
  - `09_candidate_text_v1.png`
  - `10_candidate_text_v1.png`
  - `11_candidate_text_v1.png`

## Current Final Folder Gate

Before generation, verify `final` contains only the approved pages:

- `00_표지.png`
- `01_페이지.png`
- `02_페이지.png`
- `03_페이지.png`
- `04_페이지.png`
- `05_페이지.png`
- `06_페이지.png`
- `07_페이지.png`

Do not promote pages 08-11 until candidates have QA notes and user approval.

## Official References

Use the actual image files as visual truth. Do not generate from prose alone.

- Characters:
  - `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_초롱이_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_해마친구_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_가게주인_레퍼런스.png`
- Props:
  - `series/sherlock-fin-deep-city/references/props/초롱불을_어디에_두고_왔을까_불씨구슬_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/props/초롱불을_어디에_두고_왔을까_손수건주머니_레퍼런스.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/locations/초롱불을_어디에_두고_왔을까_미역숲쉼터_레퍼런스.png`

## Shared Visual Rules

- A5 portrait page proportion, about `1:1.414`, for all interior page candidates.
- Include the approved Korean page text directly in the image from the first generation pass.
- Use one clean cream or shell-light text panel with rounded corners, thin border, and generous margins, following the text layout reference.
- Keep the Sherlock Fin series style: bright warm underwater Deep City, coral buildings, shell doors, bubble streetlamps, gentle neon, warm window lights, no horror.
- Evening darkness must feel cozy and safe, not scary.
- Chorong must follow the approved reference: round dark-blue baby anglerfish body, big eyes, teal/gold fins, head lantern shape. Tiny cute teeth are allowed only if harmless; do not enlarge the mouth or make teeth sharp.
- Flame bead must stay a small warm yellow-gold glowing bead, not a pearl, gem, jewel, open flame, or loose fire.
- Seahorse friend must read kind and helpful, not guilty, sneaky, or scary.
- PopPop must remain a round yellow pufferfish with black sunglasses, teal headphones, and side fins only. No hands, arms, fingers, pointing, or raised-hand gestures.
- Shopkeeper must stay cute, warm, and friendly, not insect-like or unpleasant.
- Do not carry reference-sheet construction arrows from the handkerchief pouch sheet into story pages.
- Avoid extra signage, pseudo-writing, invented labels, speech bubbles outside the approved text, watermarks, unrelated prior-episode details, and over-glossy neon drift.

## Lantern State Locks

- Page 08: Notebook/map shows dark at plaza and shop, bright at seaweed rest area. Present Chorong can still be dark/empty while the explanation is happening unless the bead has already been picked up in the composition; the safest read is dark/empty present Chorong beside the map.
- Page 09: Chorong places the flame bead into the head lantern. The bead glows as it enters; the lantern becomes bright only after the bead is inside.
- Page 10: Chorong's lantern is bright. The small handkerchief pouch is tied beside the lantern and must not replace the lantern.
- Page 11: Chorong's lantern is bright and warmly lights the path home.

## Page Prompt Records

### 08 Page 8

- Candidate: `08_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, seaweed rest area, flame bead, layout.
- Scene prompt: Cozy seaweed rest area. Sherlock Fin opens a small notebook map and shows it to Chorong. The notebook clearly shows reverse arrows: detective office <- jazz plaza marked dark <- shell snack shop marked dark <- seaweed rest area marked bright with a tiny flame bead icon. Only the seaweed rest area point has warm golden brightness. Chorong and Sherlock Fin look at the notebook together with understanding expressions. Present Chorong's head lantern is dark/empty to preserve the explanation moment. The central rock and warm flame bead can be visible nearby as the continuity anchor, but the notebook is the main focus. Text panel at the bottom.
- Continuity locks: reverse-thinking visual must be unmistakable. Use icons and arrows instead of readable map labels when possible. Do not add random pseudo-writing.
- Text:

```text
거꾸로 따라가 보니 알 수 있었어요.

광장에서는 어두웠어요.
가게에서도 어두웠어요.
미역 숲 쉼터에서는 환했어요!

'아, 그런 이유가 있었구나!

여기가 마지막으로
초롱이 환했던 곳이야.

구슬을 여기 두고 온 거였어!'
```

### 09 Page 9

- Candidate: `09_candidate_text_v1.png`
- Required references: Chorong, seahorse friend, seaweed rest area, flame bead, layout.
- Scene prompt: Cozy seaweed rest area close-up. Chorong gently holds the warm yellow-gold flame bead and places it into the small head lantern. Show the exact moment the bead enters the lantern and the lantern lights up warmly. The light spreads across the seaweed, the central rock, and the friends' faces. The seahorse friend stands nearby with a kind, slightly apologetic expression. Chorong is smiling brightly and relieved. Text panel in upper right.
- Continuity locks: bead must be visibly entering the lantern. The glow comes from the bead and then the lantern, not from random sparks. Seahorse is apologetic and kind, not guilty or sneaky.
- Text:

```text
초롱이가 구슬을 살며시
초롱 안에 넣었어요.

반짝—

초롱불이 환하게 켜졌어요!

해마 친구가 말했어요.

'구슬이 예뻐서,
잘 보이게 바위 가운데로
옮겨뒀어. 알려줄 걸 그랬다.'

'아니야, 잘 지켜줘서 고마워!'
```

### 10 Page 10

- Candidate: `10_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, seahorse friend, seaweed rest area, handkerchief pouch, flame bead, layout.
- Scene prompt: Cozy seaweed rest area. Chorong has made a tiny cream handkerchief pouch with a teal tie and shell button and ties it beside the head lantern. The head lantern is bright with the flame bead inside. Sherlock Fin watches proudly and gently. The seahorse friend smiles warmly beside them. Medium shot of the three friends gathered together in warm lantern light. Text panel in lower left.
- Continuity locks: pouch must be small and attached beside the lantern, not covering the lantern. Do not include arrows, construction notes, labels, or diagrams from the pouch reference sheet.
- Text:

```text
초롱이는 작은 주머니를 만들었어요.

'다음에 구슬을 닦을 때는
여기에 쏙 넣어둘래.

그러면 두고 오지 않을 거야!'

셜록 핀이 고개를 끄덕였어요.

'좋은 생각이야, 초롱이!'
```

### 11 Page 11

- Candidate: `11_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, PopPop, seahorse friend, shopkeeper, Deep City, layout.
- Scene prompt: Warm final evening scene in Deep City. Chorong's bright head lantern lights the coral alley as Sherlock Fin, PopPop, the seahorse friend, and the shell snack shopkeeper walk home together. The path glows with warm yellow lantern light, star-sand, bubble streetlamps, and warm coral window lights. Everyone looks peaceful and happy. Wide closing shot from a slight distance with a cozy safe evening mood. Text panel centered at the bottom.
- Continuity locks: PopPop must have no hands or arms. Shopkeeper is cute and friendly. Chorong's lantern stays bright and becomes the warm guide light for the group. No unrelated prior-episode characters.
- Text:

```text
어두워진 저녁,
초롱이의 불빛이
길을 환하게 밝혔어요.

잃어버린 것을 찾을 때는
마지막에 있던 곳부터
거꾸로 생각해 보면 돼요.

'여기엔 없었어.
그럼 그 전에는?'

한 걸음씩 거슬러 가면
찾을 수 있어요.

꼬마 탐정단,
오늘도 성공!
```

## QA Checklist

- [x] Text is included in each image and remains readable.
- [x] Page 08 clearly explains reverse tracking with dark-dark-bright state progression.
- [x] Page 09 shows the bead entering Chorong's lantern and the lantern lighting only after that.
- [x] Page 10 shows the handkerchief pouch around Chorong's neck/chest without reference-sheet arrows or labels.
- [x] Page 11 closes warmly with the approved character group, bright Chorong lantern, and neck/chest pouch continuity.
- [x] Chorong follows the official reference and the lantern state is correct on every page.
- [x] Sherlock Fin follows the official reference on pages 08, 10, and 11.
- [x] Seahorse friend remains kind and child-safe on pages 09-11.
- [x] PopPop has no hands, arms, fingers, or human-like gesture appendages on page 11.
- [x] Shopkeeper remains cute and friendly on page 11.
- [x] Evening mood stays cozy and safe, not scary.
- [ ] No unrelated prior-episode content, random signage, pseudo-writing, watermark, or glossy style drift.

## Batch 3 Candidate QA

Current approval set:

- `08_candidate_text_v1.png`
- `09_candidate_text_v1.png`
- `10_candidate_text_v4.png`
- `11_candidate_text_v3.png`

| Candidate | Status | QA notes |
| --- | --- | --- |
| `08_candidate_text_v1.png` | Candidate pass | A5 ratio is correct. Reverse route notebook is clear, with dark states for plaza/shop and a bright seaweed-rest-area endpoint. Chorong's present lantern stays dark for the explanation moment. |
| `09_candidate_text_v1.png` | Candidate pass | A5 ratio is correct. Flame bead is visibly being placed into Chorong's lantern and the lantern lights warmly. Seahorse reads kind and apologetic. |
| `10_candidate_text_v1.png` | Superseded | Pouch placement and duplicate bead logic needed revision. |
| `10_candidate_text_v2.png` | Superseded | Loose bead was removed, but pouch sat awkwardly on Chorong's head. |
| `10_candidate_text_v3.png` | Superseded | Same head-pouch issue remained. |
| `10_candidate_text_v4.png` | Candidate pass | A5 ratio is correct. Pouch now hangs naturally around Chorong's neck/chest, not on the head or lantern. No loose flame bead outside the lantern. |
| `11_candidate_text_v1.png` | Superseded | Wrong canvas ratio: `862x1825`, about `2.117`, too tall for A5. |
| `11_candidate_text_v2.png` | Superseded | Ratio fixed, but pouch still sat awkwardly near Chorong's head. |
| `11_candidate_text_v3.png` | Candidate pass | A5 ratio is correct. Pouch continuity now reads as a neck/chest pouch. PopPop has no hands or arms, and the final group mood is warm and safe. |

## Batch 3 Gate

- Generate only pages 08-11.
- Save candidates in this folder only.
- Do not promote to `final` until QA notes are recorded and the user approves the batch.
- After approval, promote to `final/08_페이지.png` through `final/11_페이지.png`.
- After promotion, perform final episode QA across `00_표지.png` through `11_페이지.png`.

## 2026-06-02 Approval

User approved the full Batch 3 set. Promoted:

- `08_candidate_text_v1.png` -> `final/08_페이지.png`
- `09_candidate_text_v1.png` -> `final/09_페이지.png`
- `10_candidate_text_v4.png` -> `final/10_페이지.png`
- `11_candidate_text_v3.png` -> `final/11_페이지.png`

Final folder verification confirmed 12 files from `00_표지.png` through `11_페이지.png`, all at A5 portrait ratio approximately `1.413`-`1.416`.
