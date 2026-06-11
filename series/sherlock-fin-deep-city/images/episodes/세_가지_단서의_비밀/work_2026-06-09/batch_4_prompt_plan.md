# 세 가지 단서의 비밀 - Batch 4 프롬프트 계획

## 범위

- Batch 4는 11-12페이지다.
- 현재 대본 기준 마지막 배치다. 전체 구성은 00 표지 + 01-12 본문, 총 13장이다.
- 본편 규격은 A5 세로비율이다.
- 아직 `final` 폴더로 승격하지 않는다. 이 배치는 모바일 확인용 후보 생성 단계다.

## 사용 레퍼런스

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 재즈광장: `series/sherlock-fin-deep-city/references/locations/재즈광장_레퍼런스.png`
- 텍스트박스 레이아웃: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- 펄리 별진주: `reference_setup/candidates/펄리_별진주_reference_candidate_v1.png`
- 꽃게 친구들: `reference_setup/candidates/꽃게친구들_reference_candidate_v1.png`
- Batch 3 연결 후보:
  - `batch_3_a5/09_page_candidate_a5_v5_single_tail_crabsen_group.png`
  - `batch_3_a5/10_page_candidate_a5_v1.png`

## 공통 잠금

- 꽃게 친구들과 크랩슨은 악역처럼 보이면 안 된다. 착각을 사과하는 밝고 안전한 친구들이다.
- 별진주는 분홍색 둥근 별 모양 진주다. 일반 진주, 하트 보석, 미러볼, 조개 램프가 되면 실패다.
- 11페이지에서는 별진주를 펄리에게 돌려주는 순간이 핵심이다.
- 12페이지에서는 별진주가 펄리의 조개 가방 안에 안전하게 들어가 있어야 한다.
- 셜록 핀은 공식 레퍼런스의 탐정 모자, 갈색 코트, 노란 돋보기, 하나의 연속된 인어 꼬리를 유지한다.
- 펄리는 공식 레퍼런스의 분홍 조개껍질, 큰 눈, 검은 나비넥타이, 작은 돋보기를 유지한다.
- 크랩슨은 공식 레퍼런스의 빨간 꽃게, 검은 신사 모자, 검은 정장, 보라색 보타이, 큰 집게발을 유지한다.
- 꽃게 친구들은 새 `꽃게친구들_reference_candidate_v1.png` 기준으로, 작은 일반 꽃게 친구들이어야 한다. 신사 모자, 검은 정장, 보라색 보타이는 크랩슨에게만 허용한다.
- 본편 배경에는 읽을 수 있는 불필요한 글자, 라벨, 표지판 문구를 넣지 않는다.
- 텍스트는 크림색 패널 + 분홍 점선/조개 장식 계열로 읽기 쉽게 넣는다.
- 사용자 확인: 생성 원본 텍스트가 문제없으므로 별도 텍스트 보정판은 모바일 확인 후보에서 제외한다.

## 11 Page Prompt

### Scene Lock

- 재즈광장 중앙 또는 무대 앞.
- 크랩슨이 두 집게발로 별진주를 조심스럽게 들어 펄리에게 돌려준다.
- 꽃게 친구들은 뒤쪽에서 미안한 표정으로 고개를 숙이거나 조심스럽게 손짓한다.
- 펄리는 안심한 얼굴로 별진주를 받거나 꼭 안는다.
- 셜록 핀은 옆에서 다정하게 웃으며 상황을 부드럽게 정리한다.
- 구도는 돌려주는 순간을 따뜻하게 담은 중간샷.
- 텍스트 여백은 왼쪽 아래.

### Text

"크랩슨은 별진주를
조심조심 돌려주었어요.

'미안해, 펄리.
네 소중한 물건인 줄
몰랐어.'

꽃게 친구들도 말했어요.

'먼저 주인을
찾아봤어야 했는데······
미안해!'

펄리는 별진주를
꼭 안았어요.

'찾아서 다행이에요.'

셜록 핀이 말했어요.

'반짝이는 물건을 주우면
먼저 주인을 찾아주자.

누군가에게는
아주 소중한 보물일 수 있어.'"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 11
Primary request: Create page 11 of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: Deep City jazz plaza, warm neon blue and gold lights, shell-shaped stage glow, bubble lamps, coral decorations, friendly party atmosphere.
Subject: Crabson carefully returns Pearly's pink rounded star-shaped pearl to Pearly with both claws. Pearly looks relieved and hugs the star pearl. Sherlock Fin smiles kindly beside them. Several friendly crab friends in the background bow or look apologetic.
Style/medium: polished warm Korean children's picture book illustration, consistent with the approved Sherlock Fin series references and previous A5 pages.
Composition/framing: A5 portrait medium shot focused on the handoff moment. Keep a large cream text panel with pink dotted border at lower left. Preserve enough open space so the text is readable.
Lighting/mood: warm apology, relief, kindness, harmless misunderstanding resolved.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: preserve Crabson from the official character sheet; preserve Pearly's star pearl from the pearl reference; show apology without villain/crime mood; the pearl must be returned to Pearly, not displayed as a party light.
Avoid: interrogation, chase, angry accusation, dark shadows, villain faces, oversized mirrorball pearl, generic round pearl, heart jewel, extra readable signs, extra story text.

## 12 Page Prompt

### Scene Lock

- 재즈광장 마무리 전경.
- 펄리, 셜록 핀, 크랩슨, 꽃게 친구들이 함께 웃는다.
- 별진주는 다시 펄리의 조개 가방 안에 안전하게 들어가 있다.
- 크랩슨은 펄리에게 새 친구가 되자는 듯 집게발을 내민다.
- 펄리는 미소 지으며 인사한다.
- 셜록 핀은 독자를 향해 노란 돋보기를 반짝 들어 보인다.
- 뒤쪽에는 세 가지 단서 카드가 물방울처럼 떠 있다. 카드들은 아이콘 중심으로, 긴 글자는 넣지 않는다.
- 구도는 첫 사건을 마무리하는 따뜻한 전경.
- 텍스트 여백은 아래쪽 가운데.

### Text

"펄리는 셜록 핀을 보았어요.

'고마워요, 셜록 핀!'

크랩슨도 웃었어요.

'우리도 이제 친구야!'

셜록 핀이
돋보기를 반짝 들었어요.

'오늘 우리는
잘 보고,
잘 듣고,
잘 생각해서
별진주의 길을 찾았어.

그게 바로
탐정이 하는 일이야!'

꼬마 탐정단,
첫 사건 성공!"

### Generation Prompt

Use case: illustration-story
Asset type: A5 portrait Korean children's storybook page 12
Primary request: Create page 12, the final page of the Sherlock Fin deep-sea detective story, using the inspected reference images as visual truth.
Scene/backdrop: Deep City jazz plaza after the misunderstanding is resolved, warm neon blue and gold light, shell stage, bubble lamps, coral buildings, friendly plaza glow.
Subject: Pearly, Sherlock Fin, Crabson, and several friendly crab friends smile together. Pearly's pink rounded star pearl is safely back inside Pearly's open shell bag. Crabson offers a friendly claw greeting to Pearly. Sherlock Fin faces the reader and raises her yellow magnifying glass with a confident warm smile. Behind them, three small clue cards float like bubbles: looking clue, listening clue, thinking clue, icon-based only.
Style/medium: polished warm Korean children's picture book illustration, consistent with Sherlock Fin character sheets and jazz plaza reference.
Composition/framing: A5 portrait warm closing wide shot. Keep a large cream text panel with pink dotted border at bottom center. Characters should not crowd or cover the panel.
Lighting/mood: celebratory but gentle, first case solved, new friends, safe and warm.
Text (verbatim): include the exact Korean text from the Text section.
Constraints: the star pearl must be inside Pearly's shell bag, not floating in the plaza; clue cards must be icon-based and not contain long pseudo-writing; Crabson and crab friends are friendly; Sherlock Fin has exactly one continuous mermaid lower body and one tail fin.
Avoid: large central pearl reveal, unresolved apology, villain mood, readable signs, extra story text, too many floating labels, duplicate mermaid tail, detached tail fin, panel overlap.

## QA Checklist

- 11: 크랩슨이 별진주를 펄리에게 돌려주는 순간이 명확하다.
- 11: 꽃게 친구들의 사과는 따뜻하고 안전하며 악역처럼 보이지 않는다.
- 11: 별진주는 분홍색 둥근 별 모양 진주로 유지된다.
- 12: 별진주는 펄리 조개 가방 안에 안전하게 들어가 있다.
- 12: 셜록 핀이 돋보기를 들고 파일럿 메시지를 정리하는 느낌이 난다.
- 12: 세 가지 단서 카드는 아이콘 중심이고 긴 배경 글자가 없다.
- 12: 첫 사건 성공과 새 친구 분위기가 보인다.
- 텍스트: 페이지별 한국어 본문이 정확하고 읽을 수 있다.
- 캐릭터 정체성: 셜록 핀, 펄리, 크랩슨이 공식 레퍼런스와 일치한다.
- 오염 방지: 범죄/추궁/도망 분위기, 목적지 과다 노출, 과한 라벨 문자가 들어오지 않는다.
