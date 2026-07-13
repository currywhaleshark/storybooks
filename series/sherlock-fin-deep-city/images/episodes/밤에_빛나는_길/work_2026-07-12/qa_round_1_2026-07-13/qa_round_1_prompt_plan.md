# QA Round 1 Prompt Plan - Moss Scale and Page 06 Magnifier

## Status

- User QA scope: cover `00`, pages `01`, `04`, and `06`.
- Original approved finals remained intact during revision; user-approved QA candidates are now promoted to the stable final filenames.
- User QA: **APPROVED AND FINAL PROMOTED** (“아주 좋아 / 마무리”).
- User lock: outside the page `06` magnified cutout, green moss powder must be sparse, tiny, and only barely perceptible. It must never read as a row of tiles, leaves, stepping stones, or large chunks.
- Page `06` lock: replace the oversized physical magnifier with a normal small handheld magnifier plus a separate modest circular cutaway enlargement. Only the cutaway may show child-readable enlarged moss fragments.
- Preserve every page's exact Korean text, approved character identity/anatomy, text-panel geometry, alley continuity, gold trail, and A5 portrait composition unless the page-specific prompt explicitly changes the magnifier staging.
- Built-in image editor; one page per call; final replacement occurred only after renewed user approval.

## Page 00 - Cover

### Reference Checklist

- Edit target: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/00_표지.png`
- Sherlock: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Distant grandfather identity/silhouette: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Trail/moss material: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Deep City environment and title-panel continuity are already present in the approved edit target.

### Prompt

```text
Use case: precise-object-edit
Asset type: A5 portrait Korean picture-book cover revision
Input images: Image 1 is the approved cover and the edit target. Image 2 is the official Sherlock identity sheet. Image 3 is the official Pearly identity/anatomy sheet. Image 4 is the approved elderly spider-crab grandfather sheet, used only to lock the tiny distant silhouette. Image 5 is the official gold-plankton trail and moss material reference; its close-up fragments are macro information, not the correct wide-scene scale.
Primary request: Edit only the oversized green moss pieces along the gold trail in Image 1. Replace every large square, leaf-like, tile-like, or stepping-stone green piece with very sparse, soft, pinhead-sized green moss flecks. At cover-wide scale the green flecks should be barely perceptible and discovered only on close inspection. No green fleck may be larger than the nearby small gold plankton dots. The trail must read overwhelmingly as gold light, not as a green dotted route.
Composition/framing: preserve Image 1 pixel-for-pixel in intent: same A5 portrait crop, title panel, exact title placement, alley, gold S-curve, Sherlock lower-left, Pearly lower-right, and tiny anonymous long-legged silhouette in the distance.
Text (verbatim; preserve exactly and add no other text):
"심해탐정 셜록 핀

밤에 빛나는 길"
Constraints: change only moss scale and density. Keep all gold plankton lights, brightness, trail route, buildings, lamps, bubbles, colors, characters, poses, faces, clothing, magnifiers, Pearly's round head/two arms/two hands/monocle/coherent shell, and distant silhouette unchanged. Do not reveal the grandfather. No extra character, sign, pseudo-writing, watermark, footprints, or new prop. Never landscape.
```

### Outputs

- Raw: `00_candidate_qa_v1_micro_moss_raw.png`
- Review candidate: `00_candidate_qa_v1_micro_moss.png`

## Page 01 - First Night Discovery

### Reference Checklist

- Edit target: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/01_페이지.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Deep City: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Trail/moss material: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Text panel: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

### Prompt

```text
Use case: precise-object-edit
Asset type: A5 portrait Korean picture-book page revision
Input images: Image 1 is the approved page 01 and the edit target. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the official Deep City environment/style sheet. Image 4 is the official gold-plankton trail and moss material reference; its close-up fragments are macro information only. Image 5 is the official text-panel layout reference.
Primary request: Edit only the oversized green moss pieces in the distant gold trail visible through the round window. Replace every large square, leaf-like, tile-like, or stepping-stone green piece with sparse pinhead-sized soft green flecks mixed among the gold lights. From the room-wide view they should be almost invisible—just a faint occasional green hint, never a readable chain of green shapes.
Composition/framing: preserve the exact approved room, round window, alley landmarks, warm/cool lighting, Pearly pose and scale, shell furniture, gold trail route, cream text panel, typography, and A5 crop.
Text (verbatim; preserve every glyph, line break, space, punctuation mark, and quote; add no other text):
"딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요."
Constraints: change only moss scale and density. Keep Pearly's high round head, visible torso, exactly two connected arms and two hands, black bow tie, gold monocle and chain, and coherent hinged two-valve shell unchanged. Keep the text completely intact. No Sherlock, grandfather, silhouette, extra character, random sign, pseudo-writing, watermark, or new object. Never landscape.
```

### Outputs

- Raw: `01_candidate_qa_v1_micro_moss_raw.png`
- Review candidate: `01_candidate_qa_v1_micro_moss.png`

## Page 04 - First Clue

### Reference Checklist

- Edit target: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/04_페이지.png`
- Sherlock: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Trail/moss material: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Deep City: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Text-panel continuity is already locked by the approved edit target.

### Prompt

```text
Use case: precise-object-edit
Asset type: A5 portrait Korean picture-book page revision
Input images: Image 1 is the approved page 04 and the edit target. Image 2 is the official Sherlock identity sheet. Image 3 is the official Pearly identity/anatomy sheet. Image 4 is the official gold-plankton trail and moss material reference; its close-up fragments are macro information only. Image 5 is the official Deep City environment/style sheet.
Primary request: Edit only the oversized green moss pieces distributed along the ground-hugging gold trail. Replace all large square, leaf-like, tile-like, or stepping-stone shapes with very sparse, soft, pinhead-sized green flecks mixed among the tiny gold plankton lights. In this elevated wide shot the moss should be barely perceptible and must not form its own route; the visible clue on this page is the gold trail's floor position and direction.
Composition/framing: preserve the exact approved elevated alley composition, S-bend, landmarks, gold trail route, Sherlock/Pearly placement and gestures, right-side cream text panel, typography, and A5 crop.
Text (verbatim; preserve every glyph, line break, space, punctuation mark, and quote; add no other text):
"그날 밤,
셜록 핀과 펄리는
골목으로 나갔어요.

정말이었어요!

금빛 길이
은은하게 빛나고 있었어요.

셜록 핀이 말했어요.

“먼저 잘 보자.

빛이 물속에 떠 있지 않아.
골목 바닥을 따라
굽이굽이 이어지고 있어.

누군가 이 길을 따라
움직인 자취야.

첫 번째 단서!”"
Constraints: change only moss scale and density. Keep gold lights and trail direction unchanged. Preserve Sherlock and Pearly identities, complete Pearly anatomy, text, buildings, lamps, and safe spacing. No grandfather, silhouette, cane, scarf, glasses, extra character, extra text, sign, pseudo-writing, watermark, or unrelated clue. Never landscape.
```

### Outputs

- Raw: `04_candidate_qa_v1_micro_moss_raw.png`
- Review candidate: `04_candidate_qa_v1_micro_moss.png`

## Page 06 - Small Magnifier and Cutaway Macro

### Reference Checklist

- Edit target: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/06_페이지.png`
- Sherlock: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Trail/moss macro material: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Text panel: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Alley/style continuity is already present in the approved edit target.

### Prompt

```text
Use case: precise-object-edit with a diagrammatic cutaway inset
Asset type: A5 portrait Korean picture-book clue page revision
Input images: Image 1 is the approved page 06 and the edit target. Image 2 is the official Sherlock identity sheet. Image 3 is the official Pearly identity/anatomy sheet. Image 4 is the official gold-plankton and green-moss macro material reference. Image 5 is the official text-panel layout reference.
Primary request: Replace the giant lower-center handheld magnifier with two clearly different elements. First, Sherlock holds one normal small yellow-gold magnifying glass in his gloved hand, with a lens about 10-12% of page width, aimed safely at one spot on the glowing trail. Second, add one separate circular cutaway enlargement with no handle, about 21-24% of page width, framed by a thin cream-and-gold rim and linked to that observed spot by one fine pointer line. The cutaway is an explanatory zoom window, not a second physical magnifier and not a giant lens lying on the floor.
Evidence scale: outside the cutaway, the normal-scale trail contains many tiny gold plankton lights and only very sparse, almost invisible pinhead green moss flecks. Remove every large green clump from the open paving. Inside the cutaway only, enlarge the evidence so a child can distinguish dozens of tiny faceless gold plankton specks gathering around three to five small soft green moss fragments. The enlarged fragments may be readable inside the cutaway but must stay contained there.
Composition/framing: preserve the approved upper cream text panel and exact text. Keep Sherlock lower-left and Pearly lower-right framing the evidence. Place the modest cutaway between them or slightly above the lower trail without covering either character, the text panel, or the small physical magnifier. Maintain cozy night alley and A5 portrait crop.
Text (verbatim; preserve every glyph, line break, space, punctuation mark, and quote; add no other text):
"이번에는
아주 가까이서 보았어요.

셜록 핀이 돋보기를 들고
빛나는 길을 들여다보았어요.

“어라!”

길이 빛나는 게 아니었어요.

작은 야광 플랑크톤들이
모여 반짝이고 있었지요.

그 사이에는
초록 이끼 가루도
조금씩 섞여 있었어요.

“플랑크톤들이
이끼 가루 주변에 모였어.

세 번째 단서!”"
Constraints: exactly one small physical magnifier and exactly one handleless cutaway inset. No oversized floor lens, no second handle, no duplicated magnifier, no arrows with text, and no large moss outside the cutaway. Preserve Sherlock identity and safe grip. Preserve Pearly's round head, visible torso, two connected arms/hands, bow tie, monocle/chain, and coherent shell. Gold plankton have no faces or mascot bodies. No grandfather, crab, extra character, extra text, pseudo-writing, watermark, or unrelated clue. Never landscape.
```

### Outputs

- Raw: `06_candidate_qa_v1_small_magnifier_cutaway_raw.png`
- Review candidate: `06_candidate_qa_v1_small_magnifier_cutaway.png`

## Generation Results

- Cover `00`: selected `00_candidate_qa_v1_micro_moss.png` — **USER APPROVED / FINAL**. Large green tiles are gone; the S-curve reads as gold plankton light with no separate green route. Exact title, Sherlock, Pearly, alley, magnifiers, and tiny unrevealed silhouette pass. `1054 x 1492`; SHA-256 `8DED3E1B977FE96024A0A9F34F92F834888EDBB58656461C9AA06E24A154D07D`; final `final/00_표지.png` verified equal.
- Page `01`: selected `01_candidate_qa_v1_micro_moss.png` — **USER APPROVED / FINAL**. Window trail reads as gold light with no tile-sized moss; exact text, room, window, alley landmarks, and complete Pearly anatomy pass. `1054 x 1492`; SHA-256 `DF98BE27C99CE0F9A2918227BEABA3FCE27B78854FEFC9F68002016C2214EFD8`; final `final/01_페이지.png` verified equal.
- Page `04`: selected `04_candidate_qa_v1_micro_moss.png` — **USER APPROVED / FINAL**. Large green stepping-stone shapes are removed, leaving the gold floor route and direction as the clear first clue. Exact text, Sherlock gesture, Pearly, alley, and panel pass. `1054 x 1492`; SHA-256 `A3EAFB9F898C56283AC7AAC1A15D0B29B51386F27E6319887E7D9952E1B82654`; final `final/04_페이지.png` verified equal.
- Page `06`: selected `06_candidate_qa_v1_small_magnifier_cutaway.png` — **USER APPROVED / FINAL**. Sherlock now holds one normal small magnifier; one separate handleless circular cutaway is connected to the observed spot. Only the cutaway contains enlarged readable moss fragments; normal paving retains only tiny sparse hints among the gold plankton. Exact text, Sherlock, Pearly, panel, and evidence logic pass. `1054 x 1492`; SHA-256 `5B67309BCD2E411C0DFBE45495805A2FC01D0DB4297A67E54CBC13C3E5893BD9`; final `final/06_페이지.png` verified equal.
- All four `_raw.png` files are preserved as byte-identical built-in outputs. Each selected candidate is byte-identical to its promoted final.

## QA Gate

- [x] All four candidates are A5 portrait `1054 x 1492`; no normalization or stretching was required.
- [x] Exact Korean text is preserved on all four pages.
- [x] Pages `00`, `01`, and `04` show only barely perceptible micro-moss hints; no tile/leaf/stepping-stone chain remains.
- [x] Page `06` has one normal small physical magnifier and one modest handleless cutaway inset.
- [x] Page `06` shows enlarged readable moss only inside the cutaway; normal-scale paving has no large moss.
- [x] Character identities and fragile Pearly anatomy/accessory locks pass.
- [x] No contamination, extra character, pseudo-writing, or watermark.
- [x] User approval received; all four selected candidates promoted to their stable final filenames with matching dimensions and SHA-256.
