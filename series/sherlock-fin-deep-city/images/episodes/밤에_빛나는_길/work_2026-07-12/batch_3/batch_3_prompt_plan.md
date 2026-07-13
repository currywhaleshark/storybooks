# 밤에 빛나는 길 - Batch 3 Prompt Plan

## Status

- Scope: story pages `08`-`11` only.
- Batch 2 gate: complete; user-approved final pages `00`-`07` are registered.
- Candidate folder: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/work_2026-07-12/batch_3/`
- Generation mode: built-in image generation, one call per page.
- Generation and local QA: complete; selected candidates are ready for user review.
- Promotion gate: candidates stay outside `final/` until user approval.

## Official and Approved References

- Sherlock Fin: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Grandfather: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Pop Pop: `series/sherlock-fin-deep-city/references/characters/팝팝.png`
- Momo: `series/sherlock-fin-deep-city/references/characters/모모.png`
- Crabson: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- Deep City: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Golden trail and moss flakes: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Text layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Official integrated recurring-character reference: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`
- Approved deduction continuity: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/07_페이지.png`
- Approved clue-macro continuity: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/06_페이지.png`

## Executed Reference Sets

The built-in generator accepts at most five image paths per call. No page was generated from prose-only identity or environment descriptions.

- Page `08`: Sherlock official, Pearly official, grandfather official, effect official, approved page `07` for the same alley/palette/panel language.
- Page `09`: approved page `07` as the exact A5 canvas/style base, Sherlock official, Pearly official, grandfather official, effect official.
- Page `10`: Sherlock official, Pearly official, grandfather official, effect official, approved page `06` for the established macro/panel language.
- Page `11`: approved page `07` as the exact A5 canvas/style base, official integrated recurring-character reference, grandfather official, effect official. Targeted edits also attached Momo's individual official sheet when repairing the missing cameo.

## Shared Batch Locks

- Format: A5 portrait `148:210`; production target `1054 x 1492`; never landscape.
- Use only official character/effect/environment/layout sheets plus the explicitly approved final pages listed above. Do not attach rejected or held candidates.
- Cozy night palette: deep navy/violet water, warm windows, bubble lamps, coral, and soft gold glow; never frightening darkness.
- The trail is one continuous, winding, floor-hugging route of many tiny warm-gold plankton lights gathered around small distinct green moss flakes. It is not paint, liquid, stars, or a floating ribbon.
- Only the grandfather drops moss flakes and causes the trail. Sherlock, Pearly, Pop Pop, Momo, and Crabson never create their own trails.
- Grandfather identity lock: gentle triangular brown carapace, soft green moss on the upper/rear shell, round gold glasses, plaid teal-and-tan scarf, small brown cane, very long thin jointed legs, four principal legs readable with secondary legs overlapped behind.
- Grandfather age/face lock: unmistakably elderly male; white eyebrows; paired continuous nose-to-mouth nasolabial folds visible at normal size; mild lower-cheek fullness; no beard, moustache, baby face, giant sparkling eyes, red crab body, top hat, tuxedo, or saxophone.
- Grandfather expression lock: pages `08`, `10`, and `11` use warm crescent squints or fully closed laughing eyes. Only page `09` may open the eyes slightly in modest joyful surprise; keep the irises small and the paired folds visible around the O-shaped mouth.
- Sherlock matches the official sheet: teal hair, brown deerstalker with official ornament, brown detective coat, teal tail, black gloves, and yellow-gold magnifier.
- Pearly matches the official sheet and approved episode anatomy: high fully rounded cream head, full forehead/rear skull, visible small torso and exactly two shoulder-connected arms/hands when front-facing, centered black bow tie, official gold monocle and chain, exactly one upper valve and one lower bowl sharing one hinge axis. No flattened/floating head, missing arms, bonnet, extra inner shell, or twisted valves.
- Text is rendered directly in a large cream shell-light rounded panel with generous padding. Every Korean character, space, line break, punctuation mark, and quote must match the imported script verbatim.
- No unrelated character/object, readable sign, pseudo-writing, watermark, prior-episode clue, horror, photorealism, or extra text.

## 08 - First Clear Reveal

- Raw candidate: `08_candidate_text_v1_raw.png`
- Review candidate: `08_candidate_text_v1.png`
- References: Sherlock, Pearly, grandfather, golden trail, Deep City, text layout, approved page `07` for immediate palette/style continuity only.
- Scene lock: over-the-shoulder discovery view. Sherlock and Pearly are seen from behind in the near right foreground. The newly forming gold trail leads toward the grandfather's first clear rear view in the middle distance. Small green flakes fall from his rear moss and gold plankton gather around them. Do not show his face.
- Layout: tall cream panel at left around 46-49%; deep alley view on right.

### Page 08 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the user-approved official grandfather identity and rear-view sheet. Image 4 is the approved golden-plankton trail and moss-flake reference. Image 5 is the official Deep City environment/style reference. Image 6 is the official text-panel layout reference. Image 7 is the user-approved page 07, used only for immediate palette, finish, and night-alley continuity. Ignore all reference labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy nighttime Deep City coral alley with warm windows and bubble lamps. A single granular gold-plankton trail stays low on the paving and winds into the middle distance.
Subject: from behind Sherlock Fin and Pearly, discover the long-legged spider-crab grandfather for the first time. Grandfather is clearly visible only from the rear, slowly walking away with triangular brown carapace, rear green moss, plaid scarf, cane, and four dominant long thin legs. Small green moss flakes drift down from his rear carapace; tiny faceless gold plankton gather and brighten around the falling flakes. Sherlock and Pearly never create light.
Composition/framing: A5 portrait 148:210. Tall cream rounded shell-light text panel on the left 46-49% with generous padding. Over-shoulder figures occupy near lower-right; the trail creates depth toward the grandfather in upper-right/middle distance. Keep the cause visually readable and the grandfather's face completely hidden.
Style/medium: polished warm 3-year-old picture-book illustration; cozy neon-jazz underwater mystery; match the approved page 07 finish; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"셜록 핀과 펄리는
빛의 길을 따라갔어요.

반짝반짝,
굽이굽이.

그때 저 앞에
커다란 뒷모습이 보였어요.

아주 긴 다리로
천천히 걷는
게 할아버지였어요.

등딱지에서는
초록 이끼 가루가 살랑살랑.

그 주위로
금빛 플랑크톤들이
모여들고 있었어요.

“찾았다!”"
Constraints: first clear REAR reveal only; no face or front view. Keep four principal legs readable and secondary legs overlapped. Moss flakes are small soft fragments, not giant tiles. Trail is granular and floor-hugging. Preserve official Sherlock/Pearly rear silhouettes and coherent Pearly shell. No extra character, extra text, readable sign, watermark, unrelated prop, red crab, top hat, tuxedo, saxophone, or prior-episode clue. Never landscape.
```

## 09 - He Looks Back

- Raw candidate: `09_candidate_text_v1_raw.png`
- Review candidate: `09_candidate_text_v1.png`
- References: Sherlock, Pearly, grandfather, golden trail, Deep City, text layout.
- Scene lock: the grandfather turns three-quarters toward Sherlock and Pearly and sees the long trail behind him. This is his only modest open-eye surprise page. Surprise is warm and delighted, not alarmed.
- Layout: tall cream panel on left around 47-50%; three-quarter grandfather and readable trail on right.

### Page 09 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the user-approved official grandfather identity/expression sheet. Image 4 is the approved golden-plankton trail and moss-flake reference. Image 5 is the official Deep City environment/style reference. Image 6 is the official text-panel layout reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy nighttime coral alley. One long granular gold-plankton trail winds on the paving behind the grandfather, with small green moss flakes among the lights.
Subject: Sherlock and Pearly greet the grandfather from the lower-right side. The grandfather turns three-quarters back toward them while also noticing the glowing trail behind him. Match his official triangular brown mossy carapace, round gold glasses, plaid scarf, cane, long thin legs, white eyebrows, and paired nasolabial folds. This is the only page where his eyes open slightly: modest small irises and joyful surprise, O-shaped mouth, never baby-like or frightened.
Composition/framing: A5 portrait 148:210. Tall cream rounded shell-light text panel on the left 47-50%. Grandfather dominates right-center in a readable three-quarter full-body pose; Sherlock and Pearly are smaller greeting figures; show the winding trail clearly behind him without putting anyone on it.
Style/medium: polished warm 3-year-old picture-book illustration; cozy neon-jazz underwater discovery; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"“안녕하세요!”

셜록 핀과 펄리가
다가가 인사했어요.

할아버지가 천천히
뒤를 돌아보았어요.

그리고 깜짝 놀랐어요.

자기 뒤로
금빛 길이 구불구불
반짝이고 있었거든요.

“허허, 이런!

내가 지나온 길이
이렇게 빛나고 있었구나!

나는 통 몰랐지 뭐냐.”"
Constraints: modest joyful surprise only; not panic. Keep paired nose-to-mouth folds visible around the O-shaped mouth. Keep four principal long legs readable, cane and scarf stable. Exactly one floor trail, caused only by grandfather. Preserve official Sherlock and complete Pearly anatomy. No extra character, extra text, readable sign, watermark, baby face, giant sparkling eyes, red body, top hat, tuxedo, saxophone, or unrelated clue. Never landscape.
```

## 10 - Cause Explained

- Raw candidate: `10_candidate_text_v1_raw.png`
- Review candidate: `10_candidate_text_v1.png`
- References: Sherlock, Pearly, grandfather, golden trail, text layout, Deep City, approved page `06` for clue-macro continuity only.
- Scene lock: close view must show the process in one readable direction: moss on grandfather's shell -> a few falling green flakes -> gold plankton gathering around the flakes -> warm glow. Sherlock's magnifier indicates but does not block the sequence.
- Layout: illustration left/lower; tall cream panel right around 47-50%.

### Page 10 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book mechanism close-up
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the user-approved official grandfather identity sheet. Image 4 is the approved golden-plankton trail and moss-flake mechanism reference. Image 5 is the official text-panel layout reference. Image 6 is the official Deep City environment/style reference. Image 7 is the user-approved page 06, used only for the established clue-macro visual language. Ignore all reference labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: warm close view beside the grandfather in the cozy night alley. Visually explain one clear process: soft green moss on the upper/rear shell, several small green flakes falling, dozens of tiny faceless gold plankton gathering around those flakes, and the cluster brightening into gold.
Subject: grandfather smiles warmly with crescent squint eyes, white eyebrows, round glasses, plaid scarf, cane, and clear paired nose-to-mouth nasolabial folds. Sherlock matches the official sheet and indicates the process with his yellow magnifier without covering it. Pearly watches with a high round head, visible torso, exactly two connected arms/hands, bow tie, monocle/chain, and coherent shell.
Composition/framing: A5 portrait 148:210. Mechanism close-up occupies left/lower center in a clear diagonal sequence. Sherlock and Pearly frame the evidence without blocking it. Tall cream rounded shell-light text panel on the right 47-50% with generous padding.
Style/medium: polished warm 3-year-old picture-book illustration; educational but magical neon-jazz underwater close-up; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"셜록 핀이 말했어요.

“할아버지가 걸을 때마다
등의 이끼에서
작은 가루가 떨어져요.

빛 친구들은
그 이끼 가루를 좋아해요.

그래서 가루 주변에 모여
금빛으로 반짝인 거예요.”

할아버지가
허허 웃었어요.

“내 뒤를 따라온 건
다정한 빛 친구들이었구나.

허허, 딥시티의 밤이
더 아름다워졌네!”"
Constraints: cause sequence must be readable and unobstructed. Gold plankton are a faceless granular swarm. Green flakes are small, distinct, and come only from grandfather's moss. Keep grandfather's squints and paired folds visible. Preserve official Sherlock and complete Pearly anatomy. No extra character, extra trail, extra text, pseudo-writing, watermark, unrelated object, or prior-episode clue. Never landscape.
```

## 11 - Shared Night Walk

- Raw candidate: `11_candidate_text_v1_raw.png`
- Review candidate: `11_candidate_text_v1.png`
- References: Sherlock, Pearly, grandfather, Pop Pop, Momo, Crabson, golden trail, Deep City, text layout.
- Scene lock: main trio is foreground and emotionally dominant. Pop Pop, Momo, and Crabson are small secondary cameos. Only one gold trail exists behind the grandfather's route.
- Layout: warm wide closing illustration across upper 45-48%; broad cream text panel centered across lower 52-55%.

### Page 11 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book closing page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the user-approved official grandfather identity sheet. Image 4 is the official Pop Pop identity sheet. Image 5 is the official Momo identity sheet. Image 6 is the official Crabson identity sheet. Image 7 is the approved golden-plankton trail and moss-flake reference. Image 8 is the official Deep City environment/style reference. Image 9 is the official text-panel layout reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy celebratory nighttime Deep City coral alley with warm windows, bubble lamps, soft navy/violet water, and a single winding floor trail of tiny gold plankton lights around small green flakes.
Subject: the grandfather leads a slow friendly walk with Sherlock Fin and Pearly beside him as the dominant foreground trio. Grandfather matches the official sheet, with crescent squints, paired nose-to-mouth folds, long thin legs, mossy brown shell, plaid scarf, glasses, and cane. Pop Pop, Momo, and Crabson follow farther behind as small cheerful cameos matching their official sheets. Only the grandfather drops moss and creates the single gold trail behind his route; none of the friends has a separate trail.
Composition/framing: A5 portrait 148:210. Warm wide closing illustration across the upper 45-48%, with the main trio largest and centered; three cameos smaller and clearly secondary. A broad cream rounded shell-light text panel is centered across the lower 52-55%, with generous padding and readable line spacing. Do not crowd the illustration or cover faces.
Style/medium: polished warm 3-year-old picture-book illustration; affectionate neon-jazz underwater finale; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"“허허, 그럼
같이 걸어 보겠나?”

할아버지의 밤 산책에
친구들이 함께했어요.

느릿느릿,
반짝반짝.

할아버지와 친구들이
천천히 걸어가는 뒤로
금빛 길이 길게 이어졌어요.

이상해 보이는 일에도
아름다운 이유가
숨어 있을 수 있어요.

잘 보고,
잘 듣고,
잘 생각하면
그 이유를 찾을 수 있지요.

그리고 우리는
자기도 모르는 사이
누군가의 길을 환하게
만들기도 해요.

꼬마 탐정단,
오늘도 성공!"
Constraints: exactly six named characters and no extras. Main trio foreground; Pop Pop, Momo, and Crabson small cameos. Exactly one floor-hugging trail behind the grandfather; no separate glow under any friend. Preserve all official identities, grandfather age locks, and complete Pearly anatomy. No extra text, readable sign, pseudo-writing, watermark, unrelated prop, horror, photorealism, or prior-episode clue. Never landscape.
```

## Generation Results

- Page `08`
  - `08_candidate_text_v1.png`: **FAIL / do not use**. User correctly identified that the trail continued ahead of the walking grandfather, contradicting the cause direction.
  - `08_candidate_text_v2_trail_behind_only.png`: **SUPERSEDED**. Corrected the direction so lights and moss exist only behind him.
  - Selected `08_candidate_text_v3_trail_behind_small_flakes.png`: **USER APPROVED / FINAL**. Rear-only reveal; zero trail ahead; one trail behind; wide-scene moss reduced to small flakes; exact text; `1054 x 1492`; SHA-256 `B9CB7436B92DE2C1EBC6F1827D10DD49DFA482D162EB8A8AF5A67EA84928DA61`; final `final/08_페이지.png` verified equal.
- Page `09`
  - `09_candidate_text_v1.png`: **SUPERSEDED / do not use**. Illustration and text passed, but the raw canvas was extra-tall (`887 x 1774`).
  - `09_candidate_text_v2_a5.png`: **SUPERSEDED**. Full A5 regeneration passed scene/text but retained oversized green trail pieces.
  - `09_candidate_text_v3_a5_small_flakes.png`: **SUPERSEDED**. Flake scale corrected; Pearly's second arm/hand was not explicit enough.
  - `09_candidate_text_v4_two_hands.png`: **SUPERSEDED / do not use**. Anatomy and text passed, but user QA found the trail rising behind the turned grandfather and Sherlock/Pearly reading as if greeting each other.
  - `09_candidate_text_v5_trail_downward_eyelines.png`: **SUPERSEDED**. Corrected the trail to run downward below the grandfather and redirected both friends toward him, but the green moss pieces became oversized.
  - Selected `09_candidate_text_v6_trail_downward_look_grandfather.png`: **USER APPROVED / FINAL**. The grandfather has turned back and looks down; one gold trail begins below him and continues toward the bottom edge with no trail above; Sherlock and Pearly both face and look up toward him instead of at each other; moss restored to small flakes; exact text and approved anatomy retained; `1054 x 1492`; SHA-256 `A319C7DB660B039477E71EA3A35A6750B7CC0F2CCC74AACD4C6685D92C69523F`; final `final/09_페이지.png` verified equal.
- Page `10`
  - `10_candidate_text_v1.png`: **FAIL / do not use**. Mechanism and exact text passed, but the green pieces read as large square seaweed tiles.
  - Selected `10_candidate_text_v2_small_moss_flakes.png`: **USER APPROVED / FINAL**. Clear fall -> gather -> glow sequence with small green flakes, grandfather squints/folds, complete Sherlock/Pearly, and exact text. Raw `1055 x 1491` was mechanically normalized by cropping the outermost right column and duplicating the bottom edge row, without stretching; selected `1054 x 1492`; SHA-256 `756592BA5C83CF0B1E6397353D919ACAE4A177C96F5AA3E64BC3107FA92CD5A5`; final `final/10_페이지.png` verified equal.
- Page `11`
  - `11_candidate_text_v1.png`: **FAIL / do not use**. Extra-tall canvas and weak travel-direction staging.
  - `11_candidate_text_v2_a5_missing_momo.png`: **FAIL / do not use**. A5 and exact text passed, but Momo was absent.
  - `11_candidate_text_v3_momo_added.png`: **SUPERSEDED**. All six characters present; wide-scene moss was too large.
  - `11_candidate_text_v4_momo_small_flakes.png`: **SUPERSEDED**. Flake scale corrected; the group still read as posing rather than walking.
  - `11_candidate_text_v5_walking_boot_leg.png`: **FAIL / do not use**. Walking action passed, but one raised grandfather limb became a thick boot-like human leg.
  - Selected `11_candidate_text_v6_walking_crab_leg.png`: **USER APPROVED / FINAL**. Exactly six official characters, readable shared-walk action, grandfather's raised limb restored to thin jointed crab anatomy, one trail behind him only, small flakes, exact two-column text; `1054 x 1492`; SHA-256 `DD59CFC2FB1BB9CB376458F9A06D700E428A569451A7AE063A08164C32FFFDED`; final `final/11_페이지.png` verified equal.

## QA Gate

- [x] All four selected pages are A5 portrait `1054 x 1492` without stretching or clipping required content.
- [x] Every selected page contains exact script text with correct Korean glyphs, spaces, punctuation, and quotes.
- [x] All named characters match official sheets; Pearly retains episode anatomy locks.
- [x] Grandfather matches the approved v5 sheet, including the relevant eye expression and visible paired nasolabial folds.
- [x] Page `08` is rear-only first reveal, has zero light ahead, and visibly shows moss -> plankton gathering behind him.
- [x] Page `09` alone uses modest open-eye surprise; after he turns back, the single trail runs downward below him and both friends look toward him.
- [x] Page `10` clearly explains moss falling -> plankton gathering -> gold glow.
- [x] Page `11` contains exactly six named characters, shows a shared walk, keeps cameos secondary, and has only one trail caused by grandfather.
- [x] No contamination, extra character, extra text, readable sign, pseudo-writing, or watermark.
- [x] User approved pages `08`, `10`, and `11`; each was promoted to its stable final filename with matching SHA-256.
- [x] User approved revised page `09`; it was promoted to `final/09_페이지.png` with matching dimensions and SHA-256.
