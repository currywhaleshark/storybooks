# 세 가지 단서의 비밀 - Batch 3 Prompt Plan

## Batch Scope

- 범위: 08-10페이지.
- 작업 폴더: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09`
- 후보 저장 폴더: `batch_3_a5/`
- 후보 파일명:
  - `08_page_candidate_a5_v1.png`
  - `09_page_candidate_a5_v1.png`
  - `10_page_candidate_a5_v1.png`
- 출력 규격: A5 세로비율, 기존 승인 후보와 같은 약 `1054x1492` 계열의 세로 페이지.
- 텍스트: 페이지 안에 정확한 한국어 본문을 포함한다. 생성 텍스트가 틀리면 시각 후보와 텍스트 보정 후보를 분리한다.

## Shared Visual Rules

- 3세 대상 유아 그림책 일러스트. 밝고 따뜻한 네온 해저도시 딥시티.
- 공식 캐릭터 시트를 실제 시각 기준으로 사용한다. 대본 설명만으로 외형을 추론하지 않는다.
- 셜록 핀: 청록색 머리의 어린 인어 탐정, 갈색 탐정 코트와 탐정 모자, 노란 돋보기, 검은 장갑.
- 펄리: 분홍색 조개껍데기 안의 작은 조개 친구, 큰 눈, 작은 볼, 검은 나비넥타이, 작은 돋보기 액세서리. 펄리의 조개껍데기 방향과 얼굴 방향은 서로 모순되면 안 된다.
- 크랩슨: 빨간 꽃게, 검은 신사 모자, 검은 정장, 보라색 나비넥타이, 큰 집게발. 10페이지에서 처음 만나는 친구이므로 놀람과 해명 표정이 필요하다.
- 텍스트 패널은 `텍스트박스_레이아웃_레퍼런스.png`처럼 큰 크림색 패널, 둥근 모서리, 분홍 점선 테두리, 조개/불가사리 장식으로 구성한다.
- 본편 배경에는 읽을 수 있는 불필요한 글자, 라벨, 표지판 문구를 넣지 않는다.
- 단서 카드나 칠판 안에는 긴 문장을 쓰지 않는다. 아이콘과 아주 짧은 표시 중심으로 읽히게 한다.
- 별진주는 `펄리_별진주_reference_candidate_v1.png` 기준: 분홍색 둥근 별 모양 진주, 부드러운 광택, 은은한 중심 빛. 돋보기/모노클, 일반 미러볼, 조개 장식, 하트 보석으로 바뀌면 실패다.
- 분홍 별진주 가루는 한 갈래 흔적/한 톨 원칙을 유지한다. 여러 줄, 굵은 띠, 길 안내선, 리본, 화살표처럼 보이면 실패다.
- 꽃게 친구들과 크랩슨은 악역처럼 보이면 안 된다. 착하지만 파티 장식으로 착각한 친구들이다.
- 기존 실패 후보의 잘못된 바닥, 여러 줄 분홍 가루, 과한 목적지 노출, 위협적인 꽃게 분위기가 들어오지 않게 한다.

## Reference Images

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 탐정사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- 재즈광장: `series/sherlock-fin-deep-city/references/locations/재즈광장_레퍼런스.png`
- 텍스트박스 레이아웃: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- 게 발자국: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/게발자국_reference_candidate_v1.png`
- 펄리 별진주: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/reference_setup/candidates/펄리_별진주_reference_candidate_v1.png`
- Batch 2 현재 연결 후보:
  - `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/batch_2_a5/05_page_candidate_a5_v6_pearly_back_clean_upper_paths.png`
  - `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/batch_2_a5/06_page_candidate_a5_v1.png`
  - `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09/batch_2_a5/07_page_candidate_a5_v1.png`

## 08 Page Prompt

### Scene Lock

- 추리 칠판 장면. 배경은 탐정사무소 내부 또는 탐정사무소 안의 단서 칠판.
- 칠판에는 세 가지 단서 카드가 붙어 있다.
  - 카드 1: 해마 우체부의 증언과 꽃게 친구들뿐이었다는 느낌. 해마/우체통/꽃게 실루엣 아이콘 중심.
  - 카드 2: 작은 타원/슬릿형 게 발자국, 아주 절제된 한 갈래 분홍 별진주 가루, 재즈광장 길목의 한 톨.
  - 카드 3: 재즈 음악 아이콘과 딱딱 집게발 소리, 여러 꽃게가 한곳에 모인 느낌.
- 셜록 핀이 세 카드를 선으로 잇는다. 연결선은 추리 흐름을 보여주되 화살표/길 안내선처럼 과하게 보이면 안 된다.
- 펄리는 눈을 동그랗게 뜨고 깨닫는 표정.
- 08페이지는 06의 소리만으로 결론을 내는 장면이 아니다. 07의 한 톨 단서까지 포함해 결론을 닫는다.
- 칠판이나 카드 안에 실제로 긴 글자를 많이 넣지 않는다. 본문은 아래 텍스트 패널에만 정확히 넣는다.
- 텍스트 여백은 아래쪽.

### Text

"셜록 핀은 단서를
하나로 모았어요.

그때 골목을 지난 건
꽃게 친구들뿐.

별진주 가루는
꽃게 발자국을 따라갔고,
재즈광장 길목에도
한 톨이 남아 있었어요.

딱딱 집게발 소리는
재즈광장에 모여 있어요.

셜록 핀이 말했어요.

'잘 생각해 보자.

별진주를 가진 꽃게가
재즈광장 길로 갔어.

그리고 꽃게 친구들은
재즈광장에 모여 있어.

그러니까 별진주는
재즈광장에 있어!'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 08
Primary request: Create page 08 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: inside Sherlock Fin's cozy deep-sea detective office, focused on a clue board wall with warm shell lamps, coral decorations, detective desk details, and no extra readable labels.
Subject: Sherlock Fin stands by the clue board and connects three clue cards with a neat line. Pearly watches with wide surprised eyes as she understands the reasoning.
Clue board: show three icon-based cards only. Card 1 shows a seahorse mail carrier witness plus harmless crab friends. Card 2 shows small crab footprints, one subtle pink pearl-powder trail, and one tiny pink speck at the jazz-plaza path corner. Card 3 shows jazz music icons and gentle clacking crab-claw sound icons gathered toward one place.
Style/medium: polished warm children's picture book illustration, consistent with approved A5 pages 05-07.
Composition/framing: A5 portrait, front-facing clue board scene. Keep a large cream text panel with pink dotted border along the lower area; do not cover Sherlock Fin's connecting gesture or the three cards.
Lighting/mood: warm detective thinking moment, satisfying but gentle, safe for a toddler.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: preserve Sherlock Fin and Pearly from official character sheets; cards must be icon-led, not text-heavy; the conclusion must visually combine all three clues, including the single speck from page 07; no long card labels; no readable background signs.
Avoid: solving from sound alone, missing the one-speck clue, villain mood, police/crime-board mood, scary red string, dense tiny writing, extra story text, random English/Korean labels.

## 09 Page Prompt

### Scene Lock

- 딥시티 재즈광장으로 향하는 이동 장면.
- 셜록 핀과 펄리가 네온 불빛과 음악 소리가 커지는 재즈광장 쪽으로 간다.
- 셜록 핀은 확신 있게 앞을 가리킨다. 펄리는 긴장하면서도 기대하는 표정.
- 사용자 QA 반영: 셜록 핀의 하반신은 하나의 연속된 인어 몸통과 꼬리만 보여야 한다. 역동 포즈 때문에 두 번째 하반신, 보조 꼬리, 분리된 꼬리지느러미, 복제된 몸통처럼 읽히면 실패다.
- 멀리 물방울 조명, 산호 무대의 빛, 골드 조명이 보인다.
- 음악 소리와 집게발 박수 리듬이 커지는 방향감은 허용한다.
- 09페이지는 이동 장면이다. 별진주 발견 장면이 아니므로, 분홍 별진주를 중앙에 크게 보여주면 실패다.
- 재즈광장 분위기는 가까워져도 되지만, 10페이지의 중앙 파티/별진주 미러볼 발견을 미리 크게 보여주지 않는다.
- 실제 재즈광장 레퍼런스의 네온 블루/골드 조명, 물방울 조명, 산호 무대 분위기를 참고한다.
- 텍스트 여백은 왼쪽 아래.

### Text

"셜록 핀과 펄리는
재즈광장으로 갔어요.

가까이 갈수록
소리가 커졌어요.

둠칫둠칫!
딱딱딱!

물방울 조명이 반짝이고,
산호 무대가 빛났어요.

'저기야!'

셜록 핀이
재즈광장을 가리켰어요."

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 09
Primary request: Create page 09 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: Deep City path leading toward the jazz plaza, with neon blue and gold light growing brighter ahead, bubble lamps, coral buildings, shell-shaped stage glow in the distance, and drifting music-note bubbles.
Subject: Sherlock Fin swims/walks forward confidently and points toward the jazz plaza. Pearly follows beside her, nervous but hopeful and excited.
Style/medium: polished warm children's picture book illustration, consistent with approved A5 pages 05-07 and the jazz plaza reference.
Composition/framing: A5 portrait dynamic wide shot following the direction of sound. Put the jazz plaza glow in the distance, not as the full central reveal. Keep a large cream text panel with pink dotted border at lower left.
Lighting/mood: energetic, bright, expectant, not scary. The sound feels closer and warmer.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: this is a travel/movement page, not the discovery page; do not reveal the star pearl as a large central object; preserve Sherlock Fin and Pearly identities; use jazz plaza lighting and stage mood only as destination signals.
Anatomy lock: Sherlock Fin must have exactly one continuous mermaid lower body and one tail fin, clearly connected to her torso. No second lower body, no duplicate tail, no detached fin, no extra tail silhouette behind her.
Avoid: central pink star pearl, crab party fully revealed, Crabs/Crabson dominating the scene, final discovery composition, readable signs, arrows, extra story text, duplicate mermaid tail, second lower body, detached tail fin.

## 10 Page Prompt

### Scene Lock

- 재즈광장 중앙. 여러 꽃게 친구들이 파티 준비를 하고 있다.
- 가운데에는 펄리의 분홍색 별진주가 네온 조명을 받아 미러볼처럼 반짝인다.
- 별진주는 분홍색 둥근 별 모양 진주여야 한다. 일반 둥근 미러볼, 하트 보석, 조개 램프, 큰 괴물 장치로 변하면 실패다.
- 크랩슨은 `크랩슨.png` 기준: 빨간 꽃게, 검은 신사 모자, 검은 정장, 보라색 나비넥타이, 큰 집게발.
- 크랩슨은 집게발을 들고 리듬을 맞추다가 펄리와 셜록 핀을 보고 깜짝 놀란다.
- 크랩슨은 이번 페이지에서 처음 소개된다. 이전부터 친한 표정이나 이미 해결된 분위기보다, "어? 이게 네 별진주였어?"라는 첫 만남의 놀람과 해명 표정이 필요하다.
- 꽃게 친구들은 파티 준비 중인 착한 친구들이다. 범죄자/악당/도망치는 느낌 금지.
- 별진주는 파티 조명처럼 보이되, "훔친 물건" 분위기가 아니라 "장식인 줄 착각했다"는 밝은 오해 분위기여야 한다.
- 텍스트 여백은 오른쪽 위.

### Text

"재즈광장 한가운데에서
무언가 반짝였어요.

분홍빛으로
반짝반짝!

펄리가 외쳤어요.

'내 별진주다!'

검은 신사 모자를 쓴
빨간 꽃게 친구가
깜짝 놀랐어요.

'어?
이게 네 별진주였어?

나는 크랩슨이야.
우리는 파티 장식인 줄 알았어!'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 10
Primary request: Create page 10 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: center of the Deep City jazz plaza, neon blue and gold lights, shell-shaped stage, bubble lamps, coral decorations, warm party setup.
Subject: In the middle, Pearly's pink rounded star-shaped pearl shines under jazz-plaza lights like a small party light. Friendly crab friends are preparing decorations around it. Crabson, the red gentleman crab in black top hat and bow tie, lifts his claws in rhythm but looks surprised when he sees Pearly and Sherlock Fin arrive.
Style/medium: polished warm children's picture book illustration, consistent with approved A5 pages and the jazz plaza reference.
Composition/framing: A5 portrait wide reveal of the plaza center. The star pearl is clearly visible near the center but child-sized and recognizable as Pearly's pearl, not an oversized machine. Keep a large cream text panel with pink dotted border at upper right.
Lighting/mood: bright, funny, harmless misunderstanding; party preparation, not accusation.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: preserve Crabson from the official character sheet; preserve the pink rounded star pearl from the pearl reference; Crabson and crab friends are friendly and surprised, not guilty or fleeing; first-meeting feeling; no theft/crime mood.
Avoid: villain expressions, chase scene, dark interrogation, huge monster-like mirrorball, generic disco ball, heart-shaped jewel, pearl confused with Pearly's monocle, extra readable signs, extra story text.

## QA Checklist

- 캐릭터 정체성: 셜록 핀/펄리/크랩슨이 공식 레퍼런스와 일치한다.
- 텍스트: 페이지별 한국어 본문이 정확하고 읽을 수 있다.
- 08: 세 단서 카드가 모두 보이고, 07의 한 톨 단서까지 포함해 결론을 낸다. 소리만으로 답을 닫지 않는다.
- 08: 카드/칠판 내부는 아이콘 중심이며 긴 문장이나 읽기 어려운 글자가 많지 않다.
- 09: 재즈광장으로 향하는 이동 장면이다. 별진주 발견이나 크랩슨 소개가 미리 크게 나오지 않는다.
- 09: 음악과 집게발 소리가 커지는 방향감이 있고, 셜록 핀은 확신 있게 앞을 가리킨다.
- 10: 별진주는 분홍색 둥근 별 모양 진주로 보이며, 일반 미러볼이나 다른 보석으로 변하지 않는다.
- 10: 크랩슨은 공식 시트의 빨간 꽃게/검은 신사 모자/보라 보타이를 유지하고, 첫 만남의 깜짝 놀람과 해명 분위기가 보인다.
- 10: 꽃게 친구들은 악역이 아니라 파티 장식으로 착각한 밝은 친구들처럼 보인다.
- 오염 방지: 이전 실패 후보의 과한 분홍 길 안내선, 목적지 과다 노출, 범죄/추궁 분위기가 들어오지 않는다.
