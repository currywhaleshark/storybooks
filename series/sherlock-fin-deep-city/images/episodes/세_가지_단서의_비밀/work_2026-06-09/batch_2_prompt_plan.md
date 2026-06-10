# 세 가지 단서의 비밀 - Batch 2 Prompt Plan

## Batch Scope

- 범위: 04-07페이지.
- 작업 폴더: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09`
- 후보 저장 폴더: `batch_2_a5/`
- 후보 파일명:
  - `04_page_candidate_a5_v1.png`
  - `05_page_candidate_a5_v1.png`
  - `06_page_candidate_a5_v1.png`
  - `07_page_candidate_a5_v1.png`
- 출력 규격: A5 세로비율, 기존 승인본과 같은 약 `1054x1492` 계열의 세로 페이지.
- 텍스트: 페이지 안에 정확한 한국어 본문을 포함한다. 생성 텍스트가 틀리면 시각 후보와 텍스트 보정 후보를 분리한다.

## Shared Visual Rules

- 3세 대상 유아 그림책 일러스트. 밝고 따뜻한 네온 해저도시 딥시티.
- 공식 캐릭터 시트를 시각 기준으로 사용한다. 대본 설명만으로 외형을 추론하지 않는다.
- 셜록 핀: 청록색 머리의 어린 인어 탐정, 갈색 탐정 코트와 탐정 모자, 노란 돋보기, 검은 장갑.
- 펄리: 분홍색 조개껍데기 안의 작은 조개 친구, 큰 눈, 작은 볼, 검은 나비넥타이, 작은 돋보기 액세서리.
- 텍스트 패널은 `텍스트박스_레이아웃_레퍼런스.png`처럼 큰 크림색 패널, 둥근 모서리, 분홍 점선 테두리, 조개/불가사리 장식으로 구성한다.
- 본편 배경에는 읽을 수 있는 불필요한 글자, 라벨, 표지판 문구를 넣지 않는다.
- 산호 골목은 따뜻한 분홍/주황 산호와 모래바닥, 버블 가로등, 우체통이 있는 생활 골목이다.
- 물살 세갈래길은 자연 모래바닥이다. 포장바닥, 타일, 돌길, 광장형 플랫폼, 계단, 인공 바닥 패턴 금지.
- 세갈래길에서는 실제 재즈광장/조개시장/미역숲 구역을 직접 보여주지 않는다. 길목의 아이콘, 색감, 방향감만 허용한다.
- 재즈광장 방향은 목적지 자체가 아니라 음악 아이콘과 따뜻한 빛으로만 암시한다.
- 별진주 가루는 분홍빛 작은 점/반짝이. 액체, 페인트, 리본, 화살표, 굵은 띠처럼 보이면 안 된다.
- 03 승인본의 원칙을 따른다: 게 발자국은 여러 줄 가능, 분홍 별진주 가루는 하나의 별진주에서 떨어진 한 갈래 점선 흔적만 허용.

## Reference Images

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 텍스트박스 레이아웃: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- 03 승인본: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/batch_1_a5/03_page_candidate_a5_v5_single_powder_trail.png`
- 산호 골목: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/산호골목_reference_candidate_v2.png`
- 게 발자국: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/게발자국_reference_candidate_v1.png`
- 물살 세갈래길: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/물살세갈래길_reference_candidate_v4.png`
- 펄리 별진주: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/펄리_별진주_reference_candidate_v1.png`
- 해마 우체부: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/해마우체부_reference_candidate_v2.png`

## 04 Page Prompt

### Scene Lock

- 산호 골목 우체통 앞.
- 해마 우체부는 `해마우체부_reference_candidate_v2.png` 기준: 작은 주황색 해마, 청록색 우체부 모자, 편지 가방과 편지 꾸러미, 차분하고 믿음직한 성인 동네 우체부 느낌.
- 회상 말풍선에는 꽃게 친구들이 한꺼번에 몰려가지 않고 한 마리, 또 한 마리, 조금 있다 또 한 마리씩 띄엄띄엄 지나간다.
- 꽃게 친구들은 악역처럼 보이면 안 된다.
- 다른 헤엄치는 친구는 보이지 않는다.
- 배경 우체통/편지 소품에 읽을 수 있는 우편 라벨 문구 금지.
- 텍스트 여백은 왼쪽 아래 중심.

### Text

"하지만 발자국만 보고는
알 수 없어요.

딥시티에는
헤엄쳐 지나가는 친구도
많으니까요.

셜록 핀이 말했어요.

'이번에는 잘 들어 보자.
누가 이 골목을 지나갔는지
물어보는 거야.'

해마 우체부가 말했어요.

'그때 지나간 건
꽃게 친구들뿐이었어.

한 마리, 또 한 마리,
조금 있다 또 한 마리.

모두 딱딱딱
집게발 소리를 냈지.

다른 친구는
지나가지 않았단다.'

'좋아.
첫 번째 단서야!'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 04
Primary request: Create page 04 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: warm coral alley in Deep City, sandy floor, bubble lamps, coral mailbox, cozy pink-orange coral buildings, no readable background labels.
Subject: Sherlock Fin and Pearly ask a calm seahorse mail carrier in front of the mailbox. Above the mail carrier, show a soft memory bubble with friendly crab friends passing one by one with spacing between them, not as a crowd.
Style/medium: polished warm children's picture book illustration, same look as the approved A5 page 03.
Composition/framing: A5 portrait page, medium shot. Keep a large cream text panel with pink dotted border at lower left; illustration remains visible around and behind it.
Lighting/mood: bright, curious, friendly witness scene; no villain mood.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: preserve Sherlock Fin and Pearly from their character sheets; preserve seahorse mail carrier v2; no other swimming friends; crab friends must look harmless; no readable mail labels, signs, or extra text.
Avoid: baby-faced seahorse, police/military uniform, crowd of crabs, threatening crabs, random English/Korean signs, extra story text.

## 05 Page Prompt

### Scene Lock

- 산호 골목 모래길 끝에서 물살 세갈래길로 이어지는 장면.
- 셜록 핀과 펄리가 옆걸음 발자국과 분홍 별진주 가루를 따라간다.
- 게 발자국은 작은 타원/슬릿형 콕콕 자국이 여러 줄이어도 된다.
- 별진주 가루는 하나의 별진주에서 떨어진 한 갈래 점선 흔적만 허용한다. 여러 평행 분홍 가루 줄 금지.
- 사용자 QA 반영: 05페이지는 텍스트가 아니라 시각 단서가 문제다. 별진주 가루가 과하게 보이면 실패, 발자국이 한 줄뿐이면 실패.
- 게 발자국은 여러 마리 꽃게가 지나간 사건 구조에 맞게 여러 줄/여러 방향의 작은 게 발자국 흔적으로 보여야 한다.
- 별진주 가루는 03 승인본보다도 더 절제해, 길 안내선처럼 보이지 않는 드문드문한 작은 분홍 반짝 점 한 갈래만 남긴다.
- 추가 사용자 QA 반영: 셜록 핀과 펄리는 카메라를 보지 말고 물살 세갈래길을 바라보는 구도여야 한다. 얼굴이 안 보여도 괜찮으므로 뒷모습이나 측후면 구도가 가능하다.
- 추가 사용자 QA 반영: 위쪽 세 갈래 길에는 발자국이 없어야 한다. 발자국과 별진주 가루는 물살 앞/전경까지만 보이고, 물살을 지나 갈라진 세 길 위에는 깨끗한 모래만 보여야 한다.
- 추가 사용자 QA 반영: 펄리는 얼굴과 조개껍데기 입구가 같은 방향을 봐야 한다. 조개껍데기 입구가 카메라를 향하고 얼굴만 뒤를 보면 실패다. 펄리가 세갈래길을 보려면 조개껍데기 입구도 세갈래길 쪽을 향해야 한다.
- 발자국과 분홍 가루가 물살에 씻겨 함께 흐릿해진다.
- 세 길 끝의 실제 장소를 직접 보여주지 않는다.
- 텍스트 여백은 오른쪽 위 중심.

### Text

"셜록 핀과 펄리는
발자국을 따라갔어요.

옆으로, 옆으로,
발자국이 이어졌어요.

분홍빛 가루도
조금씩 반짝였지요.

'꽃게 친구들 중 누군가가
별진주를 주워 간 게 맞아.

두 번째 단서야!'

그런데 길 끝에
물살 세갈래길이 나왔어요.

재즈광장 길,
조개시장 길,
미역숲 길.

세 갈래로 나뉘었지요.

그곳은 물살이 빨라
작은 흔적이
금방 사라지는 길목이었어요.

발자국도,
분홍빛 가루도
물살에 씻겨
흐릿해졌어요.

펄리가 물었어요.

'이제 어느 길로 가야 하죠?'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 05
Primary request: Create page 05 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: natural sandy end of the coral alley opening into the three-way current path. Three sandy paths split ahead; only icons/color cues suggest jazz plaza, shell market, and seaweed forest.
Subject: Sherlock Fin and Pearly follow sideways crab footprints and a single pink dotted pearl-powder trail until both fade in the fast underwater current.
Style/medium: polished warm children's picture book illustration, consistent with approved page 03 and the three-way current reference v4.
Composition/framing: A5 portrait, wide medium shot from the sandy trail into the fork. Keep a large cream text panel with pink dotted border at upper right.
Lighting/mood: investigative but gentle; the clue disappearing should feel puzzling, not scary.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: natural sand floor only; crab footprints are small oval/slit impressions; pink powder is one loose dotted sparkling trail, not multiple trails; footprints and powder become blurry together in the water current; actual destination locations are not visible.
Avoid: paved floor, tile, stone path, platform, stairs, arrows, thick pink stripe, multiple parallel pink trails, visible jazz plaza/market/forest scenes, readable sign text.

## 06 Page Prompt

### Scene Lock

- 물살 세갈래길에서 셜록 핀이 손을 들어 조용히 하자는 표시를 한다.
- 펄리는 귀를 기울인다.
- 멀리 재즈광장 쪽에서 음악 소리와 여러 집게발 소리가 물방울 소리 글자로 흘러온다.
- 소리는 답을 직접 확정하지 않고, 어디를 다시 봐야 할지 알려주는 단서다.
- 재즈광장 실제 장소를 보여주지 말고 방향감과 따뜻한 빛/음악 아이콘만 사용한다.
- 산호 골목은 뒤쪽 진입부로만 작게 보이고 선택지처럼 강조하지 않는다.
- 흔적은 이미 흐릿해진 상태. 발자국/가루가 선명하게 계속 이어지면 안 된다.
- 텍스트 여백은 아래쪽 중심.

### Text

"물살 세갈래길은
세 방향으로 나뉘었어요.

꽃게 친구들은
어디로 갔을까요?

따로따로 흩어졌을까요?

셜록 핀이 손을 들었어요.

'눈으로 보는 단서가 지워졌다면,
이번에는 귀로 찾아보자.'

둘은 조용히
귀를 기울였어요.

둠칫둠칫!
딱딱딱! 딱딱딱!

멀리서 재즈 음악과
여러 집게발 소리가
한곳에 모여 들렸어요.

'세 번째 단서야!

꽃게 친구들은
흩어진 게 아니야.
재즈광장에 모여 있어.

그렇다면······
별진주를 가진 꽃게도
거기 있을지 몰라!'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 06
Primary request: Create page 06 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: natural sandy three-way current path, with three path mouths indicated by subtle icons and color glows only. Jazz-plaza direction has warm golden light and small music-note icons, but the plaza itself is not visible.
Subject: Sherlock Fin raises one gloved hand in a quiet-listening gesture. Pearly leans in and listens. From the jazz-plaza direction, bubble-like sound lettering and icons drift toward them: "둠칫둠칫!" and "딱딱딱! 딱딱딱!".
Style/medium: polished warm children's picture book illustration, consistent with approved page 03 and the three-way current reference v4.
Composition/framing: A5 portrait, show the fork and sound direction. Keep a large cream text panel with pink dotted border along the lower area, leaving characters and sound trail visible.
Lighting/mood: quiet discovery, listening carefully; gentle suspense.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: current has already blurred the visual traces; do not continue a clear footprint or powder trail; actual destination places not visible; coral alley only small in the rear entry; sound is a clue, not a final proof.
Avoid: visible jazz plaza stage, visible shell market or seaweed forest, clear ongoing footprints, clear ongoing pink powder trail, arrows, readable signs, extra explanatory text.

## 07 Page Prompt

### Scene Lock

- 물살 세갈래길의 재즈광장 길목.
- 셜록 핀이 돋보기로 산호 모서리 틈을 다시 본다.
- 물살 중심부가 아니라 물살이 닿지 않는 산호 모서리 틈이어야 한다.
- 분홍 별진주 가루는 한 톨이어야 한다. 여러 가루 점, 여러 줄, 흩뿌려진 반짝이 금지.
- 돋보기 인서트 안에서 한 톨이 명확히 보이되, 과한 보석이나 큰 별진주처럼 보이면 안 된다.
- 06페이지 소리 단서가 "다시 어디를 봐야 할지" 이끈 뒤, 다시 본 단서가 결론을 닫는 장면이다.
- 텍스트 여백은 오른쪽 위 중심.

### Text

"셜록 핀은 재즈광장 길목을
다시 유심히 보았어요.

'그 길로 갔다면,
흔적이 남았을지도 몰라.'

물살이 닿지 않는
산호 모서리,

바로 거기에······

반짝.

분홍 별진주 가루
한 톨이 남아 있었어요!

'찾았다!
별진주는 재즈광장 길로 갔어.

물살에 다 씻긴 줄 알았는데,
끝까지 잘 보니
한 톨이 남아 있었구나.'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 07
Primary request: Create page 07 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: jazz-plaza path mouth within the natural sandy three-way current area. Show a coral corner niche protected from the swirling current; do not show the jazz plaza itself.
Subject: Sherlock Fin bends close with the yellow magnifying glass, studying the protected coral corner. Pearly watches with bright eyes. In the coral crevice is exactly one tiny pink pearl-powder speck. Include one magnifying inset that clearly enlarges that single speck only.
Style/medium: polished warm children's picture book illustration, consistent with approved page 03 and the three-way current reference v4.
Composition/framing: A5 portrait, visual focus on the coral corner and magnifying glass. Keep a large cream text panel with pink dotted border at upper right without covering the key clue.
Lighting/mood: satisfying discovery, precise observation, warm and safe.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: exactly one pink powder speck; the speck is small but readable; no extra pink dots around it; not a jewel, not a whole star pearl; current swirls nearby but does not touch the protected crevice; actual jazz plaza not visible.
Avoid: multiple pink specks, glitter spray, pink trail, big pearl, star-shaped object, arrows, readable signs, destination scenes, extra story text.

## QA Checklist

- 캐릭터 정체성: 셜록 핀/펄리/해마 우체부가 레퍼런스와 일치한다.
- 텍스트: 페이지별 한국어 본문이 정확하고 읽을 수 있다.
- 04: 꽃게 회상은 한꺼번에 몰려가지 않고 띄엄띄엄 지나간다. 다른 헤엄치는 친구가 없다.
- 05: 게 발자국은 실제 게 발자국형 작은 콕콕 자국이고, 분홍 가루는 한 갈래 점선이다. 물살에서 함께 흐릿해진다.
- 06: 소리는 재즈광장 방향을 암시하지만 답을 확정하지 않는다. 실제 재즈광장 장면은 보이지 않는다.
- 07: 분홍 별진주 가루는 정확히 한 톨이다. 돋보기 인서트에도 한 톨만 보인다.
- 세갈래길: 자연 모래바닥이며 포장/타일/돌길/플랫폼이 없다.
- 오염 방지: 이전 실패 후보의 잘못된 바닥, 여러 줄 분홍 가루, 과한 목적지 노출이 들어오지 않는다.
