# 자줏빛 리본의 손님 — 내지 4페이지 장면 02 그림 계획

## 범위

- 내지 4페이지: 장면 02 그림 전용 왼쪽 페이지
- 후보 파일: `04_scene02_illustration_candidate_v1.png`
- 상태: `v2 approved — promoted to final/04_페이지.png`
- 맞은편 예정 페이지: 내지 5페이지 장면 02 글 전용 면

## 장면

산호 골목에서 크랩슨과 빵집 주인이 셜록 핀과 펄리에게 도움을 청한다. 크랩슨은 큰 집게로 위쪽의 뒤바뀐 세 간판을 가리키고, 빵집 주인은 앞치마를 만지작거리며 곤란해한다. 셜록 핀은 진지하고 다정하게 이야기를 듣고, 펄리는 세 간판을 번갈아 살핀다.

## 실제 입력

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 빵집 주인: `series/sherlock-fin-deep-city/references/characters/같은_시간에_깜빡이는_가로등_빵집_주인_레퍼런스.png`
- 산호 골목 세 가게: `series/sherlock-fin-deep-city/references/locations/자줏빛_리본의_손님_산호골목_세가게_레퍼런스.png`
- 승인된 장면 01 그림: `series/sherlock-fin-deep-city/images/episodes/자주빛_리본의_손님/final/02_페이지.png` — 사전 스타일 확인용, 생성 입력 최대 5장 제한으로 직접 첨부하지 않음.

승인된 장면 01 그림은 통합된 2D 선화·눈·색면·배경 질감의 연속성만 참고한다. 인물 배치와 군중을 복사하지 않는다.

## 프롬프트

```text
Use case: illustration-story
Asset type: interior page 4, full-page illustration-only left page of a printed children's picture-book spread

Input images:
- Image 1: official Sherlock Fin identity reference; strict truth for teal mermaid child, brown detective cap and coat, gold shell ornaments, black gloves, magnifying glass, teal tail and mint tail fins.
- Image 2: official Pearly identity reference; strict truth for small pink clam child, open scallop shell body, cream face, black bow tie, tiny gold magnifying glass.
- Image 3: official Crabson identity reference; strict truth for red gentleman crab, natural crab legs and claws, black top hat, black pinstripe suit, purple bow tie. Do not include his saxophone in this scene.
- Image 4: official bakery owner identity reference; strict truth for round pink sponge body, large white chef hat, cream apron, floury hands, small official feet.
- Image 5: official Coral Alley reference; strict truth for the three shops, their colors and order, and the shifted signs.

Scene:
Morning in Coral Alley. A warm, concerned conversation in front of the three shops. Crabson and the bakery owner ask Sherlock Fin and Pearly for help. Crabson raises one large claw and clearly points toward the three wrong signs overhead. The bakery owner gently fidgets with the edge of the cream apron, eyebrows worried and posture slightly hunched. Sherlock Fin floats facing them, magnifying glass lowered, listening seriously and kindly. Pearly floats beside Sherlock and looks from one wrong sign to the next with alert curiosity.

Background continuity:
Show enough of all three storefronts across the upper background to keep the incident readable: left pink bakery, center peach-gold shell snack shop, right blue-purple library. The shifted picture signs remain exactly shell snack over the bakery, open book over the snack shop, bread over the library. The buildings and signs are secondary to the four-character conversation but still legible.

Composition:
A5 portrait full-bleed illustration, medium group shot. Put Crabson and the bakery owner on the left half facing Sherlock Fin and Pearly on the center-right. Keep the four faces, Crabson's pointing claw, the bakery owner's hands, and all three signs away from the inner right-edge gutter by at least 10%. Use a clear eye path from Crabson's claw to the signs and back to Sherlock's attentive face. No text panel and no crowd.

Character mechanics hard lock:
Sherlock Fin is a mermaid child and must have one continuous teal fish tail with tail fins, never legs, feet, shoes, trousers, or a walking stance. Sherlock floats above the sand. Pearly is a small open clam and floats without human legs. Crabson has only anatomically natural crab legs and claws; no human arms or legs. The bakery owner is not a fish and retains the official small feet.

Art style hard lock:
Clean 2D hand-painted children's storybook art matching the approved page 2. Use crisp dark-brown character outlines, large anime-style eyes with simple highlights, stable official proportions, broad painted color areas, and limited soft cel-like shading. Expressions and gestures must be easy for a child to read. No 3D toy or plastic volume.

Visual-fatigue lock:
Use broad smooth color planes. Suppress tiny gold dots, stippling, dense bubbles, pebble carpets, micro-scratches, repeated surface specks, and all-over grain. Keep faces, hands/claws, and signs crisp without blur.

Text:
No text anywhere. No title, letters, numbers, speech balloons, punctuation, question marks, labels, watermark, or decorative writing. Only the three approved picture-symbol signs may appear.

Avoid:
Extra characters, generic crowd, saxophone, detective office, text panel, ladders, platforms, footprints, broken signs, scary anger, crying, weapons, human legs on fish, human limbs on Pearly, missing crab legs, extra claws, 3D toy render, clay, Pixar-like style, plastic gloss, photorealism, dense microtexture, or unrelated prior-episode props.
```

## QA

- 네 공식 인물의 색·의상·소품·신체 구조가 시트와 일치한다.
- 셜록 핀과 펄리에게 다리·발·신발이 없고 물속에 떠 있다.
- 크랩슨은 자연스러운 게 다리와 집게만 있으며 색소폰이 없다.
- 빵집 주인의 공식 작은 발·요리사 모자·앞치마가 유지된다.
- 크랩슨이 간판을 가리키고 빵집 주인이 앞치마를 만지작거리며, 셜록은 듣고 펄리는 간판을 살핀다.
- 세 가게와 `조개 간식 / 책 / 빵` 간판 순서가 정확하다.
- 오른쪽 책등 안전 여백에 핵심 얼굴·손·집게·간판이 없다.
- 글자·말풍선·물음표·발자국·사다리·추가 군중이 없다.
- 2D 그림체와 낮은 미세 질감 기준이 승인된 2페이지와 이어진다.

## v1 결과

- 후보 파일: `04_scene02_illustration_candidate_v1.png`
- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-0c05900a-e8bf-4b08-a51c-5078e4a7317b.png`
- 원본 보존 파일: `04_scene02_illustration_candidate_v1_raw_1024x1536.png`
- 상태: `superseded by v2 — retained as history`
- 실제 입력: 셜록 핀 / 펄리 / 크랩슨 / 빵집 주인 공식 캐릭터 시트와 공식 산호 골목 세 가게 시트, 총 5장. 승인된 2페이지는 입력 한도 때문에 직접 첨부하지 않고 사전 확인한 스타일 잠금만 적용함.
- 장면 QA: 크랩슨이 위쪽 간판을 집게로 가리키고, 빵집 주인은 걱정스러운 얼굴로 앞치마를 만지작거림. 셜록 핀은 돋보기를 낮추고 진지하게 듣고, 펄리는 곁에서 놀란 표정으로 상황을 살핌.
- 신체 구조 QA: 셜록 핀은 하나로 이어진 청록색 인어 꼬리와 지느러미만 있고 다리·발·신발이 없음. 펄리는 조개 몸으로 떠 있음. 크랩슨은 자연스러운 게 다리와 집게, 빵집 주인은 공식 작은 발을 유지함.
- 정체 QA: 셜록의 탐정 모자·갈색 코트·청록색 머리, 펄리의 분홍 조개·검은 나비넥타이, 크랩슨의 검은 실크해트·정장·보라 나비넥타이, 빵집 주인의 흰 요리사 모자·크림 앞치마가 공식 시트와 연결됨.
- 장소 QA: 왼쪽 분홍 빵집 / 가운데 복숭아·금빛 간식 가게 / 오른쪽 파랑·보라 도서관과 `조개 간식 / 책 / 빵` 간판 순서가 정확함.
- 오염 QA: 군중·색소폰·사다리·발판·발자국·글자·말풍선·물음표·다른 에피소드 소품 없음.
- 시각 피로 QA: 인물과 간판은 선명하고 넓은 모래 여백을 사용함. 모래 점과 건물 표면무늬는 승인된 2페이지와 비슷한 중간 수준이며 조밀한 기포·반짝이 필드는 없음.
- 규격 보정: 생성 원본 1024×1536을 `_raw`로 보존하고, 재단 없는 LANCZOS 비율 보정으로 기존 내지 규격 1054×1492 후보를 제작함.
- 원본 파일 QA: 1024×1536 PNG, 2,975,383 bytes, SHA-256 `BC91C130A3FBC6F290A6651F9EA8AA03F7FAC26E310A48FEE05767C204E361EE`.
- 후보 파일 QA: 1054×1492 PNG, 2,703,757 bytes, SHA-256 `24E120E530E9028A24D3EE326ABA177FC6C1FFE32DDBD1E5AE4911656390DF29`.

## v2 수정 계획 — 펄리 바닥 접지

- 사용자 QA: `펄리를 바닥에 내려놔줘 / 조개가 떠있는건 이상하잖아`
- 편집 대상: `04_scene02_illustration_candidate_v1.png`
- 목표 파일: `04_scene02_illustration_candidate_v2_pearly_grounded.png`
- 편집 분류: `precise-object-edit`

### 변경 범위

- 오른쪽의 펄리만 수직으로 아래로 내려 아래 조개껍데기의 가장 낮은 면이 모래 바닥에 닿게 한다.
- 펄리 바로 아래에 작고 부드러운 타원형 접지 그림자를 붙인다.
- 펄리의 크기·얼굴·표정·분홍 조개 형태·검은 나비넥타이·금빛 돋보기·방향은 바꾸지 않는다.

### 절대 보존

- 셜록 핀·크랩슨·빵집 주인의 위치·크기·표정·자세·신체 구조를 바꾸지 않는다.
- 세 건물·세 간판·모래·산호·카메라·A5 세로 구도·색·빛·2D 그림체를 바꾸지 않는다.
- 새 인물·소품·글자·말풍선·물음표·발자국을 추가하지 않는다.

### 펄리 공통 연속성 잠금

- 펄리가 멈춰 대화하거나 관찰하는 장면에서는 아래 조개껍데기가 바닥·책상·받침 같은 지지면에 닿아 있어야 한다.
- 대본이 명시적으로 헤엄치거나 이동 중이라고 할 때만 물속에 떠 있는 자세를 허용한다.
- 펄리에게 다리·발·신발을 붙이지 않는다.

## v2 결과

- 파일: `04_scene02_illustration_candidate_v2_pearly_grounded.png`
- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-fe6377f8-25dd-4be5-8374-07e9e292c214.png`
- 원본 보존 파일: `04_scene02_illustration_candidate_v2_pearly_grounded_raw_1024x1536.png`
- 상태: `approved — promoted to final/04_페이지.png`
- 펄리 접지 QA: 펄리의 아래 조개껍데기가 모래 바닥에 직접 닿고 바로 아래에 작고 부드러운 접지 그림자가 있음. 공중에 뜬 간격이 없음.
- 펄리 정체 QA: 분홍 조개 형태·크림색 얼굴·검은 나비넥타이·금빛 돋보기·표정·방향이 유지되고 다리·발·신발·새 지느러미가 없음.
- 보존 QA: 셜록 핀·크랩슨·빵집 주인의 정체와 동작, 세 가게, `조개 간식 / 책 / 빵` 간판 순서, 수중 조명과 2D 스타일이 유지됨.
- 금지 요소 QA: 새 인물·소품·글자·말풍선·물음표·발자국·사다리·발판 없음.
- 규격 QA: 생성 원본 1024×1536을 `_raw`로 보존하고, 재단 없이 LANCZOS 보정한 1054×1492 후보를 제작함.
- 후보 파일 QA: 1054×1492 PNG, 2,583,379 bytes, SHA-256 `8667DBB3A8AAAAF5D841F05F6A0FDDD1923DC22F0BA8F27BE5E7FAE07658DEFF`.
- 원본 SHA-256: `282FA9F56D156D6D94CC196AC8BB9DD8F6D3A969D3A156E26BF7702EFD4AF23A`.

### v2 사용자 승인 및 최종 승격

- 사용자 확인: `좋아`
- 최종 파일: `series/sherlock-fin-deep-city/images/episodes/자주빛_리본의_손님/final/04_페이지.png`
- 후보·최종본 SHA-256: `8667DBB3A8AAAAF5D841F05F6A0FDDD1923DC22F0BA8F27BE5E7FAE07658DEFF`, 해시 일치.
- 이후 연속성: 정지 장면의 펄리는 아래 조개껍데기를 지지면에 놓는다.
