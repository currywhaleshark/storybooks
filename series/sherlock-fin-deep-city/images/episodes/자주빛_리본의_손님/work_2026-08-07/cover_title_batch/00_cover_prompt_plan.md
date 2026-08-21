# 자줏빛 리본의 손님 — 00 표지 후보 계획

## 범위

- 대상: 별도 표지 `00_표지.png`
- 후보 생성 원본: `00_cover_candidate_v1_title_generated_raw_1054x1492.png`
- 후보 검토본: `00_cover_candidate_v1_title_generated.png`
- 상태: `v2 approved — promoted to final/00_표지.png`

## 실제 입력 레퍼런스

1. `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
   - 셜록 핀의 얼굴, 탐정 모자·코트, 청록 머리, 인어 꼬리, 2D 선화 기준.
2. `series/sherlock-fin-deep-city/references/characters/자줏빛_리본의_손님_모리_레퍼런스.png`
   - 모리의 낮아진 포니테일 묶음점, 적갈색 머리, 자줏빛 리본, 남색 조끼, 검은 망토, 회중시계, 보라 꼬리 기준.
3. `series/sherlock-fin-deep-city/references/locations/자줏빛_리본의_손님_미역숲_물길_레퍼런스.png`
   - 에메랄드빛 좁은 수로, 미역 형태, 산호·바위·조개 팔레트 기준.
4. `series/sherlock-fin-deep-city/references/props/자줏빛_리본의_손님_핵심단서_소품_레퍼런스.png`
   - 얇은 금빛 테두리의 자줏빛 리본, 금빛 회중시계, 단순한 소용돌이 카드 기준.
5. `series/sherlock-fin-deep-city/images/episodes/같은_시간에_깜빡이는_가로등/00_표지.png`
   - 세로 표지의 상단 제목 여백과 주인공 중심 가독성만 참고. 해당 에피소드의 가게·가로등·악기·조연은 가져오지 않는다.

## 생성 프롬프트

```text
Use case: illustration-story
Asset type: portrait children's mystery storybook cover illustration
Primary request: Create a polished 2D illustrated cover showing Sherlock Fin and Mori facing each other as friendly young rivals in the emerald kelp-forest waterway from the official references.
Input images:
- Image 1 is the official Sherlock Fin character reference; preserve her face, teal hair, detective cap and coat, gloves, magnifying glass, mermaid tail and fins.
- Image 2 is the official Mori character reference; preserve her face, auburn hair, approved slightly lower high-ponytail tie position, narrow purple ribbon with thin gold edging, navy vest, black cape, gold pocket watch and purple mermaid tail.
- Image 3 is the official kelp-forest waterway reference; preserve its underwater emerald-and-deep-blue palette and narrow physical channel.
- Image 4 is the official prop reference; preserve the exact simple spiral card, purple-and-gold ribbon and pocket-watch design.
- Image 5 is a prior official series cover; use only its clear portrait-cover hierarchy and generous upper title-safe area, not its scene contents or characters.
Scene/backdrop: A calm, mysterious kelp-forest channel with broad smooth painted shapes. Kelp frames both sides and bends gently around a clear central passage. A faint physical current leads deeper into the forest without becoming a magical portal.
Subject: Sherlock Fin floats on the lower-left, turned three-quarters toward Mori with a focused curious expression and magnifying glass lowered near her chest. Mori floats on the lower-right, turned toward Sherlock with a composed, slightly teasing smile; her gold pocket watch and chain are visible. Give both characters equal narrative importance and child-friendly proportions.
Composition/framing: Vertical cover. Reserve the upper 28 percent as a calm, uncluttered deep-blue-to-teal title-safe area with only soft broad water-light shapes. Put the two faces around the middle, clear of the future title. Keep full mermaid tails visible enough to establish anatomy, with no legs or feet. Place one small spiral card between them near the lower center and let a short purple ribbon accent guide the eye, without revealing any Hangul clue cards.
Style/medium: Clean 2D animated children's-book illustration matching the official character sheets: thin clear linework, large expressive eyes, simplified shapes, limited soft shading, painterly but controlled finish. Not 3D.
Lighting/mood: Inviting underwater mystery, elegant friendly rivalry, cool emerald and navy ambience with restrained warm gold accents.
Constraints: Keep character identity faithful. Mori has no hat. Sherlock and Mori are mermaids with continuous tails. Preserve Mori's approved ponytail height. The spiral card is one small clue, not a portal. Leave print-safe margins.
Avoid: legs, feet, shoes, standing poses, hostile weapons, frightening villain expression, magical teleportation vortex, Hangul clue cards, extra characters, shops, bakery, streetlamp, musical instruments, heavy glitter, dense bubbles, tiny gold speckles, noisy pebble texture, fine kelp veins, plastic gloss, clay, toy, Pixar-like 3D volume, photorealism.
```

## 사용자 수정과 타이틀 포함 생성

- 사용자 QA: `셜록핀 표정을 좀 더 진지하게 하고 표지는 문자 넣어줘`.
- 셜록 핀의 웃는 입을 닫고 모리를 차분하게 관찰하는 진지한 탐정 표정으로 수정했다.
- 사용자 확인: `아니 타이틀 포함 생성임`.
- 로컬 조판 계획을 중단하고 이미지 생성 단계에서 정확한 타이틀을 포함하도록 변경했다.
- 1행: `심해탐정 셜록 핀`.
- 2행: `자줏빛 리본의 손님`.
- 제목은 둥글고 따뜻한 한글 그림책 표시체, 크림색 두꺼운 외곽선, 짙은 남색·자주색·청록색 계열로 생성했다.
- 제목 외의 부제·작가명·출판사·로고·영문·가짜 글자는 넣지 않았다.

## 후보 v1 결과

- 초기 생성에서 모리의 회중시계가 손과 허리에 중복되어 허리 쪽 시계만 제거했다.
- 셜록 핀의 표정을 사용자 요청대로 진지하고 집중된 표정으로 수정했다.
- 최신 이미지 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-a3b7a57d-39cc-40de-99f3-e53ef2a024cd.png`.
- 생성 원본이 1054×1492 인쇄 규격으로 저장되어 원본을 그대로 보존하고, 동일 규격의 최적화된 검토 후보를 별도 저장했다.
- 상태: `hold — do not use`. 반복 편집 과정에서 선·바닥·미역의 미세 질감이 누적되었다는 사용자 QA에 따라 최종 후보에서 제외한다.

## 후보 v2 — 수정 없는 단일 생성 계획

- 사용자 QA: `이미지 수정을 거칠때마다 계속 자글거림이 추가되는데 지금까지 내용을 바탕으로 수정없이 다시 생성하자`.
- 이전 v1 생성본과 편집본은 이미지 입력으로 사용하지 않는다.
- 공식 원본 레퍼런스 4장만 실제 입력한다: 셜록 핀 / 모리 / 미역숲 물길 / 핵심 단서 소품.
- 진지한 셜록 표정, 모리의 단일 회중시계, 타이틀 포함, 저질감 화면을 한 번의 신규 생성 프롬프트에 모두 넣는다.
- 생성 결과를 다시 이미지 생성으로 수정하지 않는다. 실패 조건이 있으면 후보 전체를 보류하고 공식 레퍼런스에서 새 후보를 다시 생성한다.
- 목표 파일: `00_cover_candidate_v2_clean_onepass.png`.

```text
Use case: illustration-story
Asset type: finished portrait Korean children's mystery storybook cover, complete in one fresh generation with title included
Primary request: Generate a brand-new clean 2D cover from only the four official reference sheets. Do not imitate or repair any prior generated cover. Show Sherlock Fin and Mori facing each other as composed young rivals in the emerald kelp-forest waterway, with the exact Korean title already included.
Input images:
- Image 1: official Sherlock Fin identity reference. Preserve her teal hair, detective cap and coat, gloves, magnifying glass, continuous teal mermaid tail and fin.
- Image 2: official Mori identity reference. Preserve her auburn hair, approved slightly lower high-ponytail tie position, narrow purple ribbon with thin gold edge, navy vest, black cape and continuous purple mermaid tail.
- Image 3: official kelp-forest waterway reference. Use its emerald/deep-blue palette and narrow physical channel, but simplify surface detail.
- Image 4: official prop reference. Use exactly one gold pocket watch held by Mori, one simple spiral card and one short purple ribbon with thin gold edging.
Scene/backdrop: A calm mysterious underwater kelp channel built from broad, smooth, simple painted shapes. Use a few large kelp fronds on each side, a clean central path, only a handful of large bubbles, and minimal large rocks or coral shapes. No carpet of small pebbles.
Subject: Sherlock Fin floats lower-left, turned three-quarters toward Mori. Her mouth is closed and her eyebrows are gently focused; she looks serious, observant and determined, never angry. Mori floats lower-right with a composed, slightly teasing smile and holds exactly one gold pocket watch in one raised hand. No second watch on her vest or waist.
Composition/framing: Vertical cover. Keep both faces below the title and around the middle of the page. Give both rivals equal visual weight. Keep both mermaid tails readable with no legs or feet. Put one small spiral card and one short purple ribbon near the lower center. Use generous print-safe outer margins.
Text (verbatim), exactly two centered title lines in the upper area:
"심해탐정 셜록 핀"
"자줏빛 리본의 손님"
Typography: large warm rounded Korean children's-book lettering, cream outer stroke, first line deep navy and second line restrained purple/teal. The second line is larger. Mostly flat color with no glitter, speckles or heavy bevel.
Exactness lock: First line is 심-해-탐-정 [space] 셜-록 [space] 핀. Second line is 자-줏-빛 [space] 리-본-의 [space] 손-님. The word must be 자줏빛, never 자주빛. Add no other letters or words.
Style/medium: clean 2D animated children's-book illustration matching the official sheets; thin clear linework, large expressive eyes, limited soft shading, broad controlled color fields, low-frequency painted finish.
Texture restraint: Treat smoothness as a primary requirement. Keep large areas visually quiet. Minimize tiny strokes, scale-by-scale highlights, kelp veins, pebble dots, glitter, grain, stippling, repeated sparkles and dense bubbles. Preserve crisp main silhouettes without filling them with microdetail.
Lighting/mood: elegant friendly rivalry and inviting mystery; cool emerald and navy with only a few restrained gold accents.
Constraints: exactly two characters; exactly one pocket watch; exactly one spiral card; no generated repair artifacts; Mori has no hat; no Hangul clue cards; no extra subtitle, author, publisher, English, logo, page number or watermark.
Avoid: prior generated cover appearance, iterative-edit texture, noisy rendering, tiny gold speckles, dense sea particles, gravel carpet, fine kelp veins, repeated fish-scale highlights, 3D toy, clay, plastic gloss, photorealism, legs, feet, shoes, standing poses, angry Sherlock, frightening Mori, duplicate watch, misspelled Korean, pseudo-text, unrelated shops, streetlamps, instruments or extra characters.
```

## QA

- 셜록 핀과 모리가 공식 시트와 같은 캐릭터로 읽힌다.
- 모리의 포니테일 묶음점이 승인 위치이며 모자를 쓰지 않는다.
- 두 인물 모두 다리·발·신발 없이 연속된 인어 꼬리다.
- 미역숲의 좁은 수로가 공식 레퍼런스와 같은 장소로 읽힌다.
- 리본·회중시계·소용돌이 카드가 공식 소품과 일치한다.
- 상단 제목 영역에 얼굴이나 핵심 단서가 들어오지 않는다.
- 화면 전체의 점묘·잔기포·잔자갈·반복 반짝이가 억제되어 있다.
- 관련 없는 에피소드의 가게·가로등·악기·조연·글자가 없다.
- 제목이 `심해탐정 셜록 핀 / 자줏빛 리본의 손님`으로 정확하고 다른 글자가 없다.

## 후보 v2 결과

- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-2f7f98fd-221e-4ca5-b766-f0f60086e7ad.png`.
- 작업 원본: `00_cover_candidate_v2_clean_onepass_raw.png`.
- 검토 후보: `00_cover_candidate_v2_clean_onepass.png`.
- 생성 방식: 이전 표지 후보를 입력하지 않은 신규 단일 생성. 공식 셜록 핀·모리·미역숲·핵심 소품 레퍼런스 4장만 사용했다.
- 캐릭터 QA: 셜록 핀은 입을 닫은 진지한 탐정 표정, 모리는 여유로운 미소이며 두 인물 모두 다리·발 없이 인어 꼬리를 유지한다.
- 소품 QA: 모리가 든 회중시계 1개, 아래 소용돌이 카드 1개, 자줏빛 리본 장식 1개만 있다.
- 타이틀 QA: `심해탐정 셜록 핀 / 자줏빛 리본의 손님`이 두 줄로 정확하며 다른 글자가 없다.
- 저질감 QA: 미역과 바닥을 큰 색면 위주로 단순화했고, 잔자갈·비늘 반복 하이라이트·금빛 점·기포 수를 v1보다 줄였다.
- 규격 QA: 생성 원본 1024×1536을 보존하고, 재단 없이 1054×1492 검토 후보로 보정했다.
- 사용자 승인: `좋았어`.
- 최종 파일: `final/00_표지.png`.
- 후보·최종본 SHA-256: `9D22DC8560E6FA7506008CED5EF27B2B5B5DF231E39F3C6A47F2C7A59BFEDF83`, 해시 일치.
