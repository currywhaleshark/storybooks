# 자줏빛 리본의 손님 — Batch 1 Prompt Plan

## 배치 범위

- 페이지: 01~04
- 후보 폴더: `series/sherlock-fin-deep-city/images/episodes/자주빛_리본의_손님/work_2026-08-07/batch_1`
- 후보 파일: `01_candidate_text_v1.png`, `02_candidate_text_v1.png`, `03_candidate_text_v1.png`, `04_candidate_text_v1.png`
- 상태: `superseded / do not use — page format changed to illustration-text spreads and art style needs correction`

> 2026-08-07 사용자 QA에 따라 이 계획의 텍스트 포함 단일 페이지 방식은 중단한다. 생성된 01 초안은 `01_candidate_text_v1_hold_style_mismatch.png`로 보관하며 재사용하지 않는다. 새 배치는 `print_spread_plan.md`의 32페이지 내지 구조와 아트스타일 잠금을 기준으로 다시 작성한다.

## 공통 공식 입력

- 산호 골목 세 가게: `series/sherlock-fin-deep-city/references/locations/자줏빛_리본의_손님_산호골목_세가게_레퍼런스.png`
- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 빵집 주인: `series/sherlock-fin-deep-city/references/characters/같은_시간에_깜빡이는_가로등_빵집_주인_레퍼런스.png`
- 핵심 단서 소품: `series/sherlock-fin-deep-city/references/props/자줏빛_리본의_손님_핵심단서_소품_레퍼런스.png`
- 텍스트 패널: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## 공통 시각 잠금

- A5 비율 세로형 그림책 페이지. 기존 최종본 규격 1054×1492에 가까운 비율을 유지한다.
- 따뜻하고 정돈된 아동용 수중 그림책 삽화. 공식 레퍼런스의 실제 형태·색·비율을 따른다.
- 산호 골목은 왼쪽 분홍 빵집 / 가운데 복숭아·금빛 조개 간식 가게 / 오른쪽 파랑·보라 도서관 순서로 고정한다.
- 배치 1 전체에서 뒤바뀐 상태를 유지한다: 빵집=조개 간식 간판 / 간식 가게=책 간판 / 도서관=빵 간판.
- 모든 간판은 높은 곳에 두 고리로 달려 있고, 사다리·발판·발자국은 없다.
- 본문은 크림색 또는 조개빛 둥근 설명 패널에 정확히 렌더링한다. 인물 얼굴·손·간판·핵심 단서를 가리지 않는다.
- 본문 외 읽을 수 있는 글자, 영문 간판, 숫자, 워터마크를 넣지 않는다.
- 셜록 핀·펄리·크랩슨은 정확한 팔다리 수와 공식 소품을 유지한다. 크랩슨은 02페이지에서 색소폰을 들지 않는다.
- 장면은 유쾌한 소동과 차분한 관찰이며 공포·악당 실루엣·위협 자세를 금지한다.
- 고주파 질감 억제: 작은 금빛 점·점묘·잔기포·잔자갈·미세 잎맥·반복 하이라이트를 절제하고, 넓고 매끈한 색면과 분명한 시선 중심을 우선한다. 핵심 단서와 인물 표정은 선명하게 유지하며 흐림으로 해결하지 않는다.
- 이전 실패 이미지나 다른 에피소드 소품을 참조하지 않는다.

## 01페이지

실제 입력:

- 산호 골목 세 가게
- 빵집 주인
- 텍스트 패널

프롬프트:

```text
Use case: illustration-story
Asset type: A5 portrait children's storybook page 01 with exact Korean text

Use the official Coral Alley, bakery owner, and text-panel references as visual truth.

Morning wide establishing view of Coral Alley. Preserve exactly three shops in fixed order: left pink bakery, center peach-and-gold shell snack shop, right blue-purple library. Show the approved shifted sign state clearly: shell-snack sign above the bakery, book sign above the snack shop, bread sign above the library. Each sign hangs high from two tidy rings. The pink round bakery owner looks puzzled and looks up toward the wrong sign. Add a small number of friendly generic sea customers peeking between shops and gently wandering in confusion; keep the crowd sparse and readable.

Composition: portrait page with the three shop fronts and all three wrong signs readable in the upper two-thirds. Reserve the lower-left area for one large cream rounded text panel. Keep the panel away from the signs and faces.

Render this Korean story text exactly, with the same line order and no paraphrase or extra text:

딥시티에 아침이 왔어요.

그런데 산호 골목이
온통 뒤죽박죽이었어요!

빵집 앞에는
조개 간식 간판이,

간식 가게 앞에는
책 간판이,

도서관 앞에는
빵 간판이 걸려 있었어요.

“어? 빵집이 어디지?”

손님들이 이리저리
헤맸어요.

Visual-fatigue lock: large clean shapes, smooth broad color planes, restrained highlights, few bubbles and pebbles, no tiny sparkle field, no dense coral microtexture. Do not blur.

Avoid: normal sign arrangement, a fourth shop, swapped building positions, broken signs, ladders, footprints, dense crowd, scary expressions, English signs, extra readable text, unrelated episode props.
```

## 02페이지

실제 입력:

- 산호 골목 세 가게
- 셜록 핀
- 펄리
- 크랩슨
- 빵집 주인
- 텍스트 패널

프롬프트:

```text
Use case: illustration-story
Asset type: A5 portrait children's storybook page 02 with exact Korean text

Use all emitted official references as visual truth. Keep the same Coral Alley and the same shifted signs from page 01 visible behind the conversation.

Medium group shot in Coral Alley. Crabson urgently points with one claw toward the three wrong signs but carries no saxophone. The pink round bakery owner fidgets with the cream apron and looks worried. Sherlock Fin listens seriously, wearing the brown detective coat and hat, teal tail and hair, with exactly two arms and two hands. Pearly looks back and forth between the three signs. The mood is concerned but safe and friendly.

Composition: group and wrong signs in the lower-left and center; one large cream rounded text panel at upper right, not covering faces, Crabson's pointing claw, or the sign evidence.

Render this Korean story text exactly, with the same line order and punctuation and no extra text:

크랩슨이 달려왔어요.

“셜록 핀, 큰일이야!

밤사이에 누가
간판을 전부 바꿔 놨어.”

빵집 주인도 말했어요.

“손님들이 자꾸
다른 가게로 들어가요.”

셜록 핀이 물었어요.

“다친 친구는 없나요?
간판은 부서지지 않았고요?”

“다행히 모두 괜찮아.”

셜록 핀이 모자를
살짝 눌러썼어요.

“그럼 왜 이런 일이 일어났는지
잘 살펴보자.”

Visual-fatigue lock: prioritize faces, gesture, and wrong signs; simplify background coral, bubbles, sand texture, and glints; no all-over dots or micro-sparkles; crisp, not blurred.

Avoid: saxophone, extra claws or arms, wrong character colors, normal signs, broken shops, frightening culprit, crowd clutter, English, extra text, unrelated props.
```

## 03페이지

실제 입력:

- 산호 골목 세 가게
- 셜록 핀
- 펄리
- 텍스트 패널

프롬프트:

```text
Use case: illustration-story
Asset type: A5 portrait children's storybook page 03 with exact Korean text

Use the official Coral Alley, Sherlock Fin, Pearly, and text-panel references as visual truth. Preserve the fixed three buildings and same shifted sign state from pages 01-02.

Wide investigative view. Sherlock Fin points in sequence at the three high signs with one hand while keeping exactly two arms and two hands. Pearly records the original shop and current sign in a small notebook. Add one simple clean circular-arrow deduction overlay near the shop signs: bread sign moved to library, book sign moved to snack shop, shell-snack sign moved to bakery. Use only the approved three sign pictures and three broad arrows; do not add words, letters, numbers, or extra diagram symbols.

Composition: the three shops and circular sign movement occupy the upper half; Sherlock Fin and Pearly stand at one side without covering the storefronts. Place a wide cream rounded text panel along the bottom, preserving sign visibility.

Render this Korean story text exactly, with the same line order and punctuation and no extra text:

셜록 핀은 세 간판을
차례로 살펴보았어요.

“아무렇게나 섞인 게 아니야.”

빵 간판은 도서관으로,
책 간판은 간식 가게로,
간식 간판은 빵집으로.

“모두 바로 옆 가게로
한 칸씩 옮겨졌어.

누군가 규칙을 정해
계획한 일이야.

첫 번째 단서!”

Visual-fatigue lock: diagram is simple and bold, background detail restrained, broad color areas, few bubbles, no tiny arrows, no dense sparkles or repeated microtexture. Keep key sign pictures and expressions crisp.

Avoid: wrong arrow direction, random swapping, fourth sign, text inside the diagram, extra limbs, Sherlock holding a ribbon or cards too early, busy infographic clutter, English, extra story text.
```

## 04페이지

실제 입력:

- 산호 골목 세 가게
- 셜록 핀
- 펄리
- 핵심 단서 소품
- 텍스트 패널

프롬프트:

```text
Use case: illustration-story
Asset type: A5 portrait children's storybook page 04 with exact Korean text

Use the official Coral Alley, Sherlock Fin, Pearly, clue-prop, and text-panel references as visual truth.

Clue investigation beneath one high hanging shop sign. Show the sign attached by two neatly tied rings. The fine sand below is smooth and completely free of ladder marks, platform marks, or footprints. On one ring, show the exact official muted-purple ribbon fragment with thin gold edging, tied in a small neat knot. Its loose end is cut perfectly straight, not torn or frayed. Sherlock Fin examines the straight ribbon end and knot with the official yellow magnifying glass. Pearly looks upward at the very high sign. Sherlock Fin has exactly two arms and two hands.

Composition: use a clear vertical relationship: high sign at upper left, clean sand below, Sherlock and Pearly at lower left/center, and one readable close-up inset of the gold-edged ribbon knot and straight-cut end. Place one large cream rounded text panel at upper right without covering the ring, ribbon, magnifying glass, or characters' faces.

Render this Korean story text exactly, with the same line order and punctuation and no extra text:

이번에는 간판 아래를
살펴보았어요.

간판은 아주 높은데,
모래에는 사다리 자국이
하나도 없었어요.

양쪽 고리는
가지런히 묶여 있었지요.

그리고 한쪽에는
자줏빛 리본 조각이
곱게 매여 있었어요.

셜록 핀이 리본 끝을 보았어요.

“찢겨 걸린 게 아니야.
반듯하게 자른 뒤
일부러 묶어 놓았어.

높이 헤엄쳐 올라가
두 손을 자유롭게 쓴 친구야.

두 번째 단서!”

Visual-fatigue lock: smooth sand with only a few large quiet tonal shapes, simplified coral and bubbles, broad clean color planes, restrained highlights, no tiny sparkles, no pebble carpet, no fine grain. Keep ribbon edge, knot, rings, and magnifier sharp; do not blur.

Avoid: ladder, platform, footprints, torn or frayed ribbon, thick gold border, wrong ribbon color, bow larger than the clue, extra ribbon pieces, missing ring, extra arms, scary culprit, text on the sign, English, unrelated props.
```

## 배치 QA

- 01~04에서 세 가게 위치와 뒤바뀐 간판 상태가 동일하다.
- 01은 세 가게와 세 간판이 모두 한눈에 보인다.
- 02는 크랩슨에게 색소폰이 없고 네 인물의 표정·동작이 대본과 맞는다.
- 03은 간판 이동 방향이 `빵→도서관 / 책→간식 가게 / 간식→빵집`으로 정확하다.
- 04는 사다리·발판·발자국이 없고 자줏빛 리본 끝이 반듯하며 얇은 금빛 테두리가 있다.
- 모든 본문이 기준 대본과 글자·문장부호·줄 순서까지 일치한다.
- 모든 페이지에서 공식 캐릭터 정체, 두 팔·두 손, 아동 안전, 텍스트 패널 가림 없음, 다른 에피소드 오염 없음이 통과한다.
- 모든 페이지에서 `고주파 질감 억제 / 핵심 단서 선명 / 배경 미세 요소 절제`를 확인한다.
