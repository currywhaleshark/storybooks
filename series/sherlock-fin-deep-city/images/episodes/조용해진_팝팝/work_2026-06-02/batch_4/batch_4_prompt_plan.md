# 배치 4 프롬프트 계획

## 범위

- 에피소드: `조용해진 팝팝`
- 페이지: `11`, `12`, `13`
- 후보 저장 위치: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/work_2026-06-02/batch_4`
- 최종 승인 후 복사 위치: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/final`

## 공통 시각 규칙

- 모든 페이지는 세로 A5 비율.
- 3세 대상 밝고 따뜻한 유아 그림책 일러스트.
- 장소는 미역숲 쉼터. `초롱불을_어디에_두고_왔을까_미역숲쉼터_레퍼런스.png`의 부드러운 미역, 별모래, 차분한 푸른/보라빛, 낮고 작은 둥근 돌 좌석을 기준으로 한다.
- 배치4는 그리움이 사라지는 장면이 아니라, 친구들이 함께 있어 주며 따뜻하게 안아주는 결말 장면이다.
- 04~10에서 확정된 연속성 유지: 바위는 낮고 납작한 둥근 타원형 회색 돌 좌석, 따뜻한 금빛 상단, 거친 돌 옆면, 주변 작은 자갈로 고정한다.
- 팝팝은 작은 낮은 바위 위 또는 바로 붙은 자리에서 유지한다. 바위 아래로 멀리 내려오면 연속성 실패.
- 헤드폰은 계속 바위 앞 오른쪽 별모래 위에 벗어둔 상태. 12에서도 헤드폰 없이 친구들과 직접 흥얼거리는 것이 핵심이다.
- 팝팝은 공식 레퍼런스의 둥근 노란 복어, 검은 선글라스, 단순 오션 틸 캡모자를 유지한다.
- 팝팝 캡모자는 장식 없는 단순 야구 캡이다. 별, 조개, 꽃, 금장, 배지, 검은 밴드, 정복/선장/경찰/군모 느낌 금지.
- 팝팝은 공식 레퍼런스처럼 작은 둥근 옆지느러미만 허용한다. 사람 손/팔/손가락/가리키는 제스처 금지.
- 셜록 핀은 돋보기를 꺼내지 않는다. 추리 승리 포즈, 손가락질, 다그침 금지.
- 펄리, 모모, 크랩슨은 공식 참조를 사용한다. 새 캐릭터처럼 재해석하지 않는다.
- 본문 텍스트는 크림색 텍스트 패널 또는 깨끗한 여백에 정확한 한국어로 읽기 쉽게 넣는다. 생성기 텍스트가 흔들리면 원본 후보를 보존하고 `_text_v1` 같은 별도 텍스트 보정본을 만든다.
- 이전 에피소드의 실패 이미지나 후보 이미지는 참조하지 않는다.
- 사용자 승인 전에는 `final` 폴더로 승격하지 않는다.

## 공식 참조

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 팝팝: `series/sherlock-fin-deep-city/references/characters/팝팝.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 모모: `series/sherlock-fin-deep-city/references/characters/모모.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 반짝이: `series/sherlock-fin-deep-city/references/characters/조용해진_팝팝_반짝이_레퍼런스.png`
- 미역숲 쉼터: `series/sherlock-fin-deep-city/references/locations/초롱불을_어디에_두고_왔을까_미역숲쉼터_레퍼런스.png`
- 텍스트박스: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## 페이지별 계획

### 11

- 후보 파일: `11_candidate_v1.png`
- 참조: 셜록 핀, 팝팝, 펄리, 모모, 크랩슨, 미역숲 쉼터, 텍스트박스
- 장면: 펄리, 모모, 크랩슨이 하나둘 미역 숲으로 와서 둥근 바위 주위에 함께 앉는다. 05의 비어 있던 자리가 친구들로 따뜻하게 채워지는 대비. 모두 조용히 팝팝 곁에 있다.
- 잠금: 친구들이 팝팝을 둘러싸되 다그치거나 울지 말라고 하지 않는다. 팝팝은 작은 낮은 바위 근처 위치 유지. 헤드폰은 바위 앞 오른쪽 별모래 위. 큰 무대 바위 금지.
- 텍스트 위치: 오른쪽 위.
- 정확한 텍스트:

```text
그때, 펄리가 왔어요.
모모도 왔어요.
크랩슨도 왔어요.

친구들이 하나둘
둥근 바위 주위에
함께 앉았어요.

비어 있던 자리가
친구들로 채워졌어요.

아무도 팝팝에게
울지 말라고 하지 않았어요.

그냥, 함께 있어 주었어요.
```

프롬프트:

```text
Create page 11 for the Korean children's picture book episode "조용해진 팝팝".

FORMAT: portrait A5 page, vertical children's book page, full-page illustration with print-safe margins.

Use the official Sherlock Fin, Popop, Pearly, Momo, Crabson, kelp forest clearing, and text box references. Scene: Pearly, Momo, and Crabson quietly arrive one by one in the kelp forest clearing and sit around the same small low round-oval stone seat. The previously empty space is now warmly filled by friends. Nobody tells Popop not to cry; everyone simply stays nearby.

Continuity lock: Popop remains on or directly beside the same small low stone seat. The stone is not a large platform. Removed teal headphones sit on the star-sand immediately in front-right of the stone, not on the stone. Sherlock Fin has no magnifying glass in hand. Popop has only small rounded fish fins, no human hands or arms.

Popop lock: round yellow pufferfish, black sunglasses, official plain ocean-teal baseball cap, no cap decoration, no star, no shell, no flower, no gold badge, no black band, no uniform/captain hat feeling.

Composition: vertical A5 slightly top-down warm wide shot of the small stone, Popop, Sherlock Fin, Pearly, Momo, and Crabson gathered gently around it. Gold warmth begins to spread through the blue-purple kelp forest. Leave text area at upper right with a cream readable panel. Add the exact Korean text:
"그때, 펄리가 왔어요.
모모도 왔어요.
크랩슨도 왔어요.

친구들이 하나둘
둥근 바위 주위에
함께 앉았어요.

비어 있던 자리가
친구들로 채워졌어요.

아무도 팝팝에게
울지 말라고 하지 않았어요.

그냥, 함께 있어 주었어요."

Avoid large platform rock, Popop far on the sand, headphones on the rock, decorated cap, human hands on Popop, magnifying glass, pointing, scolding, scary mood, unreadable text.
```

### 12

- 후보 파일: `12_candidate_v1.png`
- 참조: 셜록 핀, 팝팝, 펄리, 모모, 크랩슨, 미역숲 쉼터, 텍스트박스
- 장면: 팝팝이 작게 흥얼거리기 시작하고 친구들이 함께 흥얼거린다. 헤드폰은 여전히 벗어둔 채. 이번엔 헤드폰 없이, 혼자가 아니라 다 같이 부른다. 부드러운 음표가 떠오르고 팝팝 표정이 풀린다.
- 잠금: 헤드폰을 다시 쓰지 않는다. 팝팝에게 사람 손 금지. 친구들이 과하게 춤추지 않고 조용히 같이 흥얼거리는 따뜻한 장면.
- 텍스트 위치: 아래쪽.
- 정확한 텍스트:

```text
팝팝이 작게 흥얼거렸어요.

흠…… 흐음……

반짝이랑
부르던 노래였어요.

그러자 친구들이
함께 흥얼거렸어요.

흠…… 흐음……

이번에는 헤드폰 없이,
혼자가 아니라
다 같이 불렀어요.

팝팝이 말했어요.
‘반짝이 보고 싶어.’

셜록 핀이 말했어요.
’보고 싶어해도 괜찮아.

보고 싶다는 건,
그만큼 좋아했다는 거니까.’
```

프롬프트:

```text
Create page 12 for the Korean children's picture book episode "조용해진 팝팝".

FORMAT: portrait A5 page, vertical children's book page, full-page illustration with print-safe margins.

Use the official Sherlock Fin, Popop, Pearly, Momo, Crabson, kelp forest clearing, and text box references. Scene: Popop begins to hum softly, and the friends hum along. Popop's teal headphones remain removed on the star-sand; this time Popop sings without headphones, not alone but together with friends. Soft gentle music notes float above them. Popop's expression begins to relax.

Continuity lock: small low round-oval stone seat remains small, not a platform. Popop stays on or directly beside the small stone seat. Removed teal headphones sit on the star-sand immediately in front-right of the stone. No character wears the removed headphones. Sherlock Fin has no magnifying glass in hand.

Popop lock: round yellow pufferfish, black sunglasses, official plain ocean-teal baseball cap, no cap decoration, no human hands or arms, only small rounded fish fins.

Composition: vertical A5 warm medium shot of Popop and friends humming together around the small stone in the kelp forest. Gentle gold light spreads through the blue-purple scene. Leave text area at the bottom with a cream readable panel. Add the exact Korean text:
"팝팝이 작게 흥얼거렸어요.

흠…… 흐음……

반짝이랑
부르던 노래였어요.

그러자 친구들이
함께 흥얼거렸어요.

흠…… 흐음……

이번에는 헤드폰 없이,
혼자가 아니라
다 같이 불렀어요.

팝팝이 말했어요.
‘반짝이 보고 싶어.’

셜록 핀이 말했어요.
’보고 싶어해도 괜찮아.

보고 싶다는 건,
그만큼 좋아했다는 거니까.’"

Avoid Popop wearing headphones, large platform rock, dramatic dancing, decorated cap, human hands on Popop, magnifying glass, pointing, scary mood, unreadable text.
```

### 13

- 후보 파일: `13_candidate_v1.png`
- 참조: 셜록 핀, 팝팝, 펄리, 모모, 크랩슨, 반짝이, 미역숲 쉼터, 텍스트박스
- 장면: 미역 숲 위로 작은 푸른빛 점 하나가 반짝 지나간다. 반짝이가 보낸 빛 편지일 수도, 별모래일 수도 있다. 팝팝이 그 빛을 올려다보며 살며시 웃고, 친구들도 함께 바라본다.
- 잠금: 반짝이는 직접 크게 등장시키지 않고 작은 푸른빛 한 점 또는 아주 작은 발광 오스트라코드 실루엣 정도로 상징한다. 그리움은 지워진 게 아니라 따뜻하게 안긴 결말. 팝팝은 헤드폰을 쓰지 않아도 된다. 헤드폰은 바위 앞 오른쪽 별모래 위에 유지 가능.
- 텍스트 위치: 아래쪽 가운데.
- 정확한 텍스트:

```text
그때, 미역 숲 위로
작은 푸른빛 하나가
반짝— 지나갔어요.

반짝이가 보낸
빛 편지였을까요?

아니면 그냥
별모래였을까요?

팝팝이 그 빛을 올려다보며
살며시 웃었어요.

잘 보고,
잘 듣고,
때로는 그냥 곁에 있어 주면

친구의 마음도
함께 안아줄 수 있어요.

꼬마 탐정단,
오늘도…… 함께예요.
```

프롬프트:

```text
Create page 13 for the Korean children's picture book episode "조용해진 팝팝".

FORMAT: portrait A5 page, vertical children's book page, full-page illustration with print-safe margins.

Use the official Sherlock Fin, Popop, Pearly, Momo, Crabson, Bangjagi, kelp forest clearing, and text box references. Scene: Above the kelp forest, one small blue glowing light passes by with a gentle sparkle. It could be a light letter from Bangjagi, or it could simply be star-sand. Popop looks up at the light and smiles softly for the first time. The friends look up together. The ending is warm: the longing is not erased, but held together.

Bangjagi lock: do not show a large new character. Show only one tiny soft blue bioluminescent dot, or at most a very tiny translucent glowing ostracod-like silhouette high above the group.

Continuity lock: small low round-oval stone seat remains small, not a platform. Popop stays near the small stone with friends nearby. Removed teal headphones may remain on the star-sand front-right of the stone. Sherlock Fin has no magnifying glass in hand. Popop has only small rounded fish fins, no human hands or arms.

Popop lock: round yellow pufferfish, black sunglasses, official plain ocean-teal baseball cap, no cap decoration, no star, no shell, no flower, no gold badge, no black band, no uniform/captain hat feeling.

Composition: vertical A5 closing wide shot of the kelp forest, the small gathered friends, and the tiny blue light passing above. Blue bioluminescence, warm gold star-sand, gentle pink highlights. Leave text area at lower center with a cream readable panel. Add the exact Korean text:
"그때, 미역 숲 위로
작은 푸른빛 하나가
반짝— 지나갔어요.

반짝이가 보낸
빛 편지였을까요?

아니면 그냥
별모래였을까요?

팝팝이 그 빛을 올려다보며
살며시 웃었어요.

잘 보고,
잘 듣고,
때로는 그냥 곁에 있어 주면

친구의 마음도
함께 안아줄 수 있어요.

꼬마 탐정단,
오늘도…… 함께예요."

Avoid large Bangjagi character, anglerfish lantern, old Chorongi reference, large platform rock, decorated cap, human hands on Popop, magnifying glass, scary mood, unreadable text.
```
