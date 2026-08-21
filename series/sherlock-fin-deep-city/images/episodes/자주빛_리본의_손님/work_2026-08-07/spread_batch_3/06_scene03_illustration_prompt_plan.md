# 자줏빛 리본의 손님 — 내지 6페이지 장면 03 그림 계획

## 범위

- 내지 6페이지: 장면 03 그림 전용 왼쪽 페이지.
- 목표 후보: `06_scene03_illustration_candidate_v1.png`.
- 맞은편 예정 글 페이지: 내지 7페이지 장면 03 본문.
- 상태: `v2 approved — promoted to final/06_페이지.png`.

## 기준 장면

- 세 가게가 한눈에 보이는 산호 골목.
- 셜록 핀이 세 간판을 차례로 가리키며 규칙을 발견한다.
- 펄리는 작은 수첩에 원래 가게와 현재 간판을 그림 기호로 정리한다.
- 공식 장소 시트의 세 아이콘 원형 화살표 도식을 간단하고 크게 보여준다.
- 새 그림·글 분리 구성에 따라 본문 텍스트 여백과 본문 문장은 넣지 않는다.

## 실제 입력 레퍼런스

1. `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
   - 셜록 핀의 얼굴, 모자·코트·장갑·돋보기, 청록 인어 꼬리, 2D 선화 기준.
2. `series/sherlock-fin-deep-city/references/characters/펄리.png`
   - 분홍 조개 몸, 크림 얼굴, 검은 나비넥타이, 금빛 돋보기, 아래 조개껍데기 접지 기준.
3. `series/sherlock-fin-deep-city/references/locations/자줏빛_리본의_손님_산호골목_세가게_레퍼런스.png`
   - 세 가게 좌우 순서, 순환된 간판 상태, 그림 기호, 원형 화살표 도식 기준.

## 연속성 잠금

- 세 가게 순서: 왼쪽 분홍 빵집 / 가운데 금빛 조개 간식 가게 / 오른쪽 보라 도서관.
- 현재 잘못 걸린 간판: 왼쪽 빵집=`조개 간식`, 가운데 간식 가게=`책`, 오른쪽 도서관=`빵`.
- 셜록 핀은 다리·발·신발 없이 연속된 인어 꼬리다.
- 펄리는 정지해 기록하는 장면이므로 아래 조개껍데기를 모래 바닥에 놓는다. 다리·발·신발은 없다.
- 등장인물은 셜록 핀과 펄리만 사용한다. 크랩슨·빵집 주인·군중은 넣지 않는다.
- 수첩에는 세 간판 그림 기호만 넣고 한글·영문·숫자·가짜 글자는 넣지 않는다.

## 생성 프롬프트

```text
Use case: illustration-story
Asset type: portrait left-page illustration for a children's mystery storybook, no story text
Primary request: Create a brand-new clean 2D illustration of Sherlock Fin discovering the one-step circular sign-swapping rule in Coral Alley while Pearly records the picture clues in a small notebook. Generate once from only the three official reference sheets; do not use or imitate prior generated page images.
Input images:
- Image 1: official Sherlock Fin character reference. Preserve her face, teal hair, detective cap and coat, gloves, magnifying glass and continuous teal mermaid tail.
- Image 2: official Pearly character reference. Preserve the pink clam shell body, cream face, black bow tie and tiny gold magnifying glass. In this stationary scene, the lower shell rests directly on the sand with a subtle contact shadow.
- Image 3: official three-shop Coral Alley reference. Preserve the exact left-to-right building order, the shifted sign state, the three pictogram designs and the small circular-arrow diagram's direction.
Scene/backdrop: Bright morning underwater Coral Alley. Across the upper half, show exactly three complete shop fronts in one readable view: left pink bakery, middle warm-gold shell-snack shop, right purple shell library.
Sign accuracy: The signs are already shifted and must be exactly: left bakery sign = shell-snack pictogram; middle snack-shop sign = open-book pictogram; right library sign = bread-loaf pictogram. No words on signs.
Subject/action: Sherlock Fin is in the lower-left/center foreground, floating naturally with her continuous mermaid tail and pointing upward from one sign to the next with a focused discovery expression. Her magnifying glass remains visible in her other hand. Pearly is lower-right, resting on the sand, looking between the signs and an open small notebook. The notebook contains only three clear simple pictograms corresponding to shell snack, open book and bread loaf, with no writing.
Inference diagram: Include one clean, simple, cream-backed circular three-icon arrow diagram near the middle without covering faces or signs. Follow the direction and icon arrangement shown in Image 3. It must communicate that bread moved from the bakery to the library, the book moved from the library to the snack shop, and the shell-snack sign moved from the snack shop to the bakery. Use only the three official pictograms and three broad arrows; no text or numbers.
Composition/framing: Portrait page, wide-enough environmental view. Buildings fill the upper half; characters and notebook fill the lower third. Keep all faces, pointing hand, signs, notebook and diagram away from the left book gutter and outer trim.
Style/medium: clean 2D animated children's-book illustration matching the official sheets; thin clear linework, large expressive eyes, simplified forms, limited soft shading and broad smooth color fields.
Texture restraint: Keep the sand, buildings and water visually calm. Minimize tiny pebbles, grain, stippling, repeated bubbles, gold speckles, scale-by-scale highlights and micro-coral. Use a few large decorative shapes only. Keep the three signs and diagram crisp.
Lighting/mood: clear morning discovery, friendly and intelligent, coral pinks, warm cream, teal and deep underwater blue.
Constraints: exactly two characters; exactly three shops; exactly three shifted signs; exactly one notebook; exactly one circular diagram; no body-text panel, caption, title, speech bubble, Hangul, English, numbers, watermark or pseudo-text.
Avoid: wrong sign order, extra shop, extra sign, duplicate icons, circular diagram pointing the wrong way, floating Pearly, legs, feet, shoes, standing fish, ladder, footprints, Mori, Crabson, bakery owner, crowds, saxophone, purple ribbon, spiral card, 3D toy, clay, plastic gloss, Pixar-like rendering, dense glitter, noisy gravel texture, unrelated episode props.
```

## QA

- 세 가게와 간판의 좌우 관계가 공식 순환 상태와 정확히 일치한다.
- 원형 도식의 세 아이콘과 화살표 방향이 공식 장소 시트와 일치한다.
- 셜록 핀의 가리키기와 펄리의 수첩 기록이 한눈에 읽힌다.
- 펄리의 아래 조개껍데기가 모래에 닿고 두 캐릭터에게 다리·발·신발이 없다.
- 글자·말풍선·제목·본문 패널·가짜 글자가 없다.
- 배경의 잔자갈·점묘·기포·금빛 점·반복 하이라이트가 절제되어 있다.

## 후보 v1 결과

- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-5cccb38a-af36-4cdb-a0db-3e1a38162a2f.png`.
- 작업 원본: `06_scene03_illustration_candidate_v1_raw.png`.
- 검토 후보: `06_scene03_illustration_candidate_v1.png`.
- 생성 방식: 이전 생성 페이지를 입력하지 않고 공식 셜록 핀·펄리·산호 골목 레퍼런스 3장만 사용한 신규 단일 생성.
- 장소 QA: 정확히 세 가게이며 왼쪽 빵집=`조개 간식`, 가운데 간식 가게=`책`, 오른쪽 도서관=`빵`으로 순환 상태가 정확하다.
- 도식 QA: 조개 간식→책→빵→조개 간식 순서의 세 아이콘 원형 화살표가 표시되고 글자는 없다.
- 행동 QA: 셜록 핀은 간판을 가리키고 다른 손에 돋보기를 들며, 펄리는 세 그림 기호가 있는 수첩을 기록한다.
- 신체 QA: 셜록 핀은 연속된 인어 꼬리이며, 펄리는 아래 조개껍데기가 모래에 닿고 접지 그림자가 있다. 다리·발·신발이 없다.
- 저질감 QA: 모래와 건물은 큰 색면 위주이며 잔자갈·기포·점묘·반복 반짝이가 절제되어 있다.
- 규격 QA: 생성 원본 1024×1536 보존, 재단 없이 1054×1492 검토 후보로 보정.
- 파일 QA: 원본 2,911,662 bytes, SHA-256 `D25F075CA99FD2C3AA140F4E940EE2EE30DD0A8F7321D323AAC5739570402C0D`; 후보 2,703,416 bytes, SHA-256 `FF84899157987B438F5CD92F167A71D7E536991DC28805242B337B891DA53279`.
- 사용자 QA: `펄리한테 이상한 하반신같은게 생겨났군`.
- 상태: `hold — do not use`. 수첩과 아래 조개껍데기 사이 형태가 몸통·하반신처럼 읽혀 최종 후보에서 제외한다.

## 후보 v2 — 펄리 조개 구조 잠금 재생성

- v1이나 다른 생성 페이지를 이미지 입력으로 사용하지 않는다.
- 공식 셜록 핀·펄리·산호 골목 시트 3장만 다시 입력해 신규 단일 생성한다.
- 펄리의 아래 구조는 공식 시트처럼 하나의 얕고 둥근 분홍 조개 받침뿐이며 모래에 완전히 닿는다.
- 펄리의 크림색 얼굴은 위·아래 조개 사이에 놓이고, 아래 조개 밑이나 뒤로 몸통·배·꼬리·다리·발 모양이 이어지지 않는다.
- 수첩은 펄리 몸 앞을 가리지 않고 모래 위에 완전히 분리해 놓아 조개 실루엣을 명확히 보인다.
- 목표 후보: `06_scene03_illustration_candidate_v2_pearly_shell_locked.png`.

```text
Use case: illustration-story
Asset type: portrait left-page illustration for a children's mystery storybook, no story text
Primary request: Generate a brand-new clean 2D illustration of Sherlock Fin discovering the circular sign-swapping rule while Pearly records the clue. Use only the three official reference sheets and do not use any prior generated page as an input.
Input images:
- Image 1: official Sherlock Fin identity and anatomy reference.
- Image 2: official Pearly identity and strict clam-body anatomy reference.
- Image 3: official three-shop Coral Alley layout, shifted signs and circular-arrow diagram reference.
Scene/backdrop: Bright morning Coral Alley with exactly three full shop fronts across the upper half: left pink bakery, middle warm-gold shell-snack shop, right purple library.
Sign accuracy: left bakery sign = shell-snack pictogram; middle snack-shop sign = open-book pictogram; right library sign = bread-loaf pictogram. No words.
Sherlock: lower-left/center, natural continuous teal mermaid tail with no legs or feet, pointing to the signs with one gloved hand and holding her magnifying glass in the other, focused discovery expression.
Pearly anatomy lock: lower-right, identical to Image 2. Pearly is a clam character made of one pink upper shell and one single shallow rounded pink lower shell. The lower shell is a simple bowl-shaped base resting directly and fully on the sand with one soft contact shadow. Only Pearly's round cream face and tiny arms appear between the two shell halves. There is absolutely no torso, abdomen, pelvis, tail, fish body, lower body, legs, feet, shoes, pedestal, cushion or fleshy extension below, behind or attached under the lower shell. Show the complete outer silhouette of the lower shell unobstructed.
Notebook separation: Put one small open notebook flat on the sand to Pearly's left with a visible gap between the notebook and Pearly's shell. Pearly does not sit on, wear, merge with or hold the notebook against her body. The notebook shows only three simple pictograms: shell snack, open book and bread loaf; no writing.
Inference diagram: one cream-backed circular three-icon arrow diagram near the middle, based on Image 3. It shows shell snack → open book → bread loaf → shell snack with three broad arrows and no text.
Composition: portrait page; three shops in upper half; Sherlock and Pearly in lower third. Keep signs, diagram, pointing hand, faces, the separated notebook and Pearly's complete shell silhouette clear and print-safe.
Style: clean 2D animated children's-book illustration matching the official sheets; thin clear linework, large expressive eyes, simplified forms, limited soft shading and broad smooth color fields.
Texture restraint: calm smooth sand, buildings and water. Minimize tiny pebbles, grain, stippling, repeated bubbles, gold speckles, micro-coral and scale-by-scale highlights.
Constraints: exactly two characters; exactly three shops; exactly three shifted signs; exactly one separate notebook; exactly one circular diagram; Pearly has exactly one upper and one lower shell; no text, title, caption, speech bubble, watermark or pseudo-text.
Avoid: Pearly lower body, torso below shell, belly, tail, fish body, legs, feet, shoes, shell pedestal, shell cushion, notebook fused to Pearly, notebook hiding lower shell, floating Pearly, wrong signs, extra shop, extra character, Mori, Crabson, bakery owner, crowds, footprints, ladder, saxophone, purple ribbon, spiral card, 3D toy, clay, plastic gloss, noisy gravel, dense glitter.
```

## 후보 v2 결과

- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-78b78499-11b6-4fb7-8c84-89beb2aa97ce.png`.
- 작업 원본: `06_scene03_illustration_candidate_v2_pearly_shell_locked_raw.png`.
- 검토 후보: `06_scene03_illustration_candidate_v2_pearly_shell_locked.png`.
- 생성 방식: v1을 입력하지 않고 공식 셜록 핀·펄리·산호 골목 레퍼런스 3장만 사용한 신규 단일 생성.
- 펄리 QA: 위 조개 1개와 모래에 닿는 얕은 아래 조개 1개로만 구성되며, 아래 조개 전체 실루엣과 접지 그림자가 보인다. 몸통·배·꼬리·다리·발·받침 형태가 없다.
- 수첩 QA: 펄리와 간격을 두고 모래 위에 별도로 놓여 있으며 조개 몸과 합쳐지거나 아래 조개를 가리지 않는다.
- 보존 QA: 세 가게 순서, `조개 간식 / 책 / 빵` 간판, 세 아이콘 원형 도식, 셜록의 가리키기와 돋보기가 유지된다.
- 저질감 QA: 모래와 물의 큰 색면이 유지되고 잔자갈·점묘·반복 기포·금빛 점이 절제되어 있다.
- 규격 QA: 생성 원본 1024×1536 보존, 재단 없이 1054×1492 검토 후보로 보정.
- 파일 QA: 원본 2,995,517 bytes, SHA-256 `A10650062106042504616577E7E3A8336DAB62D0383AE3923F0DD4BC8526ED04`; 후보 2,742,956 bytes, SHA-256 `609B5CC62206D8485715FD943025648E4BC41EE1C44B2C5572EBE4BB449D95FD`.
- 사용자 승인: `오케이`.
- 최종 파일: `final/06_페이지.png`.
- 후보·최종본 SHA-256: `609B5CC62206D8485715FD943025648E4BC41EE1C44B2C5572EBE4BB449D95FD`, 해시 일치.

