# 자줏빛 리본의 손님 — Spread Batch 1 Prompt Plan

## 범위

- 내지 2페이지: 장면 01 그림 전용 왼쪽 페이지
- 기준 후보 파일: `02_scene01_illustration_candidate_v1.png`
- 수정 후보 예정 파일: `02_scene01_illustration_candidate_v2_legless_crowd.png`
- 상태: `candidate v2 generated — user review pending`
- 사용자 승인 게이트: 이 한 장으로 새 그림체를 먼저 확정한 뒤 나머지 그림·글 페이지를 진행한다.

## 실제 입력

- 장소 구조·간판: `series/sherlock-fin-deep-city/references/locations/자줏빛_리본의_손님_산호골목_세가게_레퍼런스.png`
- 빵집 주인 정체: `series/sherlock-fin-deep-city/references/characters/같은_시간에_깜빡이는_가로등_빵집_주인_레퍼런스.png`
- 기존 장면 통합 스타일: `series/sherlock-fin-deep-city/images/episodes/같은_시간에_깜빡이는_가로등/10_페이지.png`

기존 10페이지는 인물의 2D 윤곽선·눈·비율·제한된 명암만 참고한다. 빵집 내부, 셜록 핀, 팝팝, 모모, 크랩슨, 펄리, 오븐, 가로등 단면도와 본문 패널은 가져오지 않는다.

## 프롬프트

```text
Use case: illustration-story
Asset type: interior page 2, full-page illustration-only left page of a printed children's picture-book spread

Input images:
- Image 1: official Coral Alley reference; strict visual truth for the three buildings, their left-to-right order, colors, storefront purposes, and all three picture signs.
- Image 2: official bakery owner sheet; strict identity truth for body shape, face, eye style, sponge texture, large white chef hat, cream apron, hands, and proportions.
- Image 3: existing Sherlock Fin series story page; style reference only for integrated 2D character linework, anime-style eyes, proportions, limited soft shading, and warm hand-painted finish. Do not copy its location, characters, text, props, or story content.

Scene:
Morning in Coral Alley. Exactly three shops in fixed order: left pink bakery, center peach-and-gold shell snack shop, right blue-purple library. Show the approved shifted signs: shell-snack sign over the bakery, book sign over the snack shop, bread sign over the library. Every sign hangs high from two tidy rings. The official bakery owner stands near the bakery, looking up in puzzled surprise. Add only three small generic sea residents moving between the wrong shops in gentle confusion. They are background supporting figures, not new mascots.

Composition:
A5 portrait full-bleed illustration with no text panel. The three storefronts and all three wrong signs must remain readable. Use layered depth suited to a portrait page: buildings across the upper and middle area, bakery owner in the lower-left foreground, three small residents distributed sparsely through the middle ground. This is a left-hand page: keep essential faces and signs away from the inner right-edge gutter by at least 10%; no critical detail on the rightmost edge.

Character art-style hard lock:
Match the existing Sherlock Fin series as 2D hand-painted children's storybook art. Use clean visible dark-brown linework around every character, large anime-style eyes with simple graphic highlights, clear brows and mouths, stable official proportions, and limited soft cel-like painterly shading. The bakery owner must match Image 2 exactly: round soft pink sea-sponge body, large white chef hat, small cream apron, simple oval brown-black eyes, chubby mitten-like hands, subtle flour on hands, no nose redesign.

Generic residents:
Draw them in the same clean 2D outlined series style, with simplified shapes, flatter painted color areas, restrained detail, and smaller visual scale. No glossy spherical toy bodies, no new franchise-mascot designs, no hyper-rendered pores, and no unique accessories that steal focus.

Background style:
Preserve Image 1's building silhouettes and palette, but simplify surface microtexture. Use broad smooth color planes, restrained coral details, a small number of large readable sand stones, very few bubbles, and soft warm water lighting.

Text:
No text anywhere. No title, labels, speech balloons, question marks, letters, numbers, English signs, watermark, or decorative writing. Only the three picture-symbol signs are visible.

Visual-fatigue lock:
Suppress tiny gold dots, stippling, dense bubbles, pebble carpets, repeated micro-highlights, fine scratches, and all-over grain. Keep signs, faces, and shop silhouettes crisp. Do not blur.

Avoid:
3D toy render, clay render, Pixar-like mascot style, plastic gloss, realistic subsurface scattering, thick volumetric shading, weak/no character outlines, tiny dot eyes, official baker identity drift, a fourth shop, normal sign arrangement, swapped building positions, dense crowd, ladders, platforms, footprints, broken signs, scary mood, text, unrelated episode content, or any visual element from the rejected prior 01 draft.
```

## QA

- 빵집 주인이 공식 시트의 눈·윤곽선·모자·앞치마·해면 질감과 일치한다.
- 단역이 3D 토이 마스코트가 아니라 같은 2D 선화 스타일로 보인다.
- 왼쪽 분홍 빵집 / 가운데 간식 가게 / 오른쪽 도서관 구조가 유지된다.
- 간판은 왼쪽부터 조개 간식 / 책 / 빵으로 정확하다.
- 글자·말풍선·물음표가 없다.
- 책등 쪽 오른쪽 10%에 핵심 얼굴·간판이 없다.
- 자글자글한 미세 질감은 억제되고 핵심 형태는 선명하다.

## v1 결과

- 파일: `02_scene01_illustration_candidate_v1.png`
- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-caa4d64a-5a7f-4294-9c18-b2c7773e4cfa.png`
- 상태: `superseded by v2 — retained as history`
- 캐릭터 스타일: 빵집 주인과 세 단역 모두 짙은 2D 윤곽선, 큰 애니메이션풍 눈, 제한된 부드러운 명암을 사용해 이전 실패본의 3D 토이 느낌이 크게 줄어듦.
- 장소·사건: 세 건물 순서와 `조개 간식 / 책 / 빵` 간판 순서가 정확함.
- 텍스트: 글자·말풍선·물음표 없음.
- 시각 피로: 이전 실패본보다 차분하지만 모래 점과 건물 표면무늬가 중간 정도 남아 있어 사용자 확인 필요.
- 파일 QA: 1054×1492 PNG, 2,833,602 bytes, SHA-256 `9E31A2F22BA6A4181F74E57A44B33DB019D939B8D0E2867D5FB32EB303B84A31`.

## v2 수정 계획 — 물고기 해부 구조와 골목 군중

- 사용자 QA: `스타일은 괜찮은데 시리즈 공통 물고기한테 다리를 달지는 않고있거든 / 발자국 관련 추리들이 있으니까 / 그리고 좀 더 조연들이 많이 웅성웅성하는 느낌이면 좋겠다`
- 편집 대상: `02_scene01_illustration_candidate_v1.png`
- 목표 파일: `02_scene01_illustration_candidate_v2_legless_crowd.png`
- 편집 분류: `precise-object-edit`

### 변경 범위

- 다리가 붙은 파란 물고기를 다리·발·신발 없이 꼬리지느러미와 옆지느러미로 떠 있는 물고기로 바꾼다.
- 거북 조연은 사람처럼 선 두 다리를 제거하고 자연스러운 네 지느러미로 헤엄치게 한다.
- 해마처럼 본래 다리가 없는 조연은 형태를 유지한다.
- 골목 주민을 총 8~10마리로 늘리고, 세 개의 작은 무리로 나누어 서로 속삭이거나 간판을 번갈아 보며 지느러미로 가리키는 가벼운 혼란을 만든다.
- 새 조연은 작고 단순한 2D 선화로 처리하며 빵집 주인과 간판보다 시각적 비중을 낮춘다.

### 절대 보존

- 빵집 주인은 물고기가 아니므로 공식 레퍼런스의 작은 발을 그대로 둔다.
- 빵집 주인의 얼굴·모자·앞치마·표정·위치, 세 가게의 구조·색·순서, `조개 간식 / 책 / 빵` 간판 순서, 카메라와 A5 세로 구도는 바꾸지 않는다.
- 글자·말풍선·물음표·발자국·사다리·발판을 추가하지 않는다.
- 2D 그림체와 낮은 고주파 질감 기준을 유지한다.

### 해부 구조 하드 락

- 모든 일반 물고기는 몸통, 꼬리지느러미, 옆지느러미만 사용한다.
- 물고기에게 다리·발·신발·바지 모양의 사람형 하체·걷는 자세·바닥에 선 자세를 금지한다.
- 물고기와 거북 조연은 바닥에서 약간 떠서 서로 다른 높이에 배치한다.
- 발자국 단서의 세계관 논리를 위해 이후 모든 본편 그림 프롬프트에도 같은 규칙을 반복한다.

## v2 결과

- 파일: `02_scene01_illustration_candidate_v2_legless_crowd.png`
- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-f0e700b1-2e1e-46eb-a1ba-6d9d9f919c57.png`
- 상태: `candidate pass — user review pending`
- 해부 구조 QA: 일반 물고기 9마리는 모두 꼬리지느러미와 옆지느러미로 떠 있고 다리·발·신발·걷는 자세가 없음. 거북 1마리는 네 지느러미로 헤엄치며, 해마 1마리는 기존의 다리 없는 형태를 유지함.
- 군중 QA: 총 11마리 조연이 세 개의 느슨한 대화 무리로 나뉘어 서로 마주 보고 입을 벌리거나 지느러미로 반응해 웅성거림이 강화됨. 핵심 간판과 빵집 주인을 가리지 않음.
- 보존 QA: 빵집 주인의 공식 작은 발·모자·앞치마·표정과 왼쪽 아래 위치가 유지됨. 세 가게와 `조개 간식 / 책 / 빵` 간판 순서가 정확함.
- 텍스트 QA: 글자·말풍선·물음표·발자국·사다리·발판 없음.
- 스타일 QA: 기존 승인 방향의 2D 짙은 윤곽선·큰 눈·부드러운 제한 명암을 유지하고 3D 토이·플라스틱 광택이 없음.
- 파일 QA: 1054×1492 PNG, 2,751,058 bytes, SHA-256 `6F78475F8830AC24BCD854EE38FA219C0C48C0B8C8F94723EA485DF0DDD76FA1`.
