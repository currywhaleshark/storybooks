# 자줏빛 리본의 손님 — 내지 3페이지 장면 01 글 페이지 계획

## 범위

- 내지 3페이지: 장면 01 글 전용 오른쪽 페이지
- 선택 후보: `03_scene01_text_candidate_v3_katuri.png`
- 맞은편 승인 그림: `02_scene01_illustration_candidate_v2_legless_crowd.png`
- 상태: `v3 approved — promoted to final/03_페이지.png`

## 입력과 역할

- `references/layouts/텍스트박스_레이아웃_레퍼런스.png`: 조개빛 크림 패널, 넓은 여백, 또렷한 계층만 참고한다.
- 승인된 내지 2페이지 그림: 산호 골목의 분홍·복숭아·청보라 팔레트와 수중 조명만 참고한다.
- 대본 `자줏빛_리본의_손님_수정본(1).md`의 01 `Text:` 블록: 한 글자도 바꾸지 않는 본문 원본.

## 제작 방식

1. 이미지 생성기로 글자 없는 A5 세로 장식 배경만 만든다.
2. 1054×1492로 맞춘 뒤 한글 지원 글꼴로 본문을 로컬 조판한다.
3. 원문과 조판 결과를 기계적으로 비교하고 시각 검수한다.

이 에피소드는 그림과 글을 별도 페이지로 나누기로 사용자가 승인했으므로, 생성기 임의 한글이 아니라 정확한 별도 조판을 사용한다.

## 장식 배경 프롬프트

```text
Use case: illustration-story
Asset type: A5 portrait right-hand text-only page paired with a Coral Alley illustration

Create a calm underwater children's storybook text-page background with one very large blank warm shell-cream writing field occupying about 82% of the canvas. Use a thin soft coral-pink and muted teal double border, rounded corners, and only a few simple edge decorations: one small coral sprig at the upper-right, one small shell at the lower-right, and three tiny picture-symbol plaques along the bottom edge showing a shell snack, an open book, and a loaf of bread. Keep the entire central writing field perfectly blank and pale.

Composition:
A5 portrait. This is the right-hand page, so reserve an extra-wide quiet inner gutter along the left edge. Keep all decoration outside the main text field and away from the left gutter. Use broad smooth color planes and generous negative space.

Style:
Clean 2D hand-painted children's picture-book design matching the approved Coral Alley palette, with dark-brown detail lines only on the tiny symbols, limited soft shading, and a warm cream paper feel.

Text:
No text anywhere. No letters, numbers, punctuation, labels, watermark, pseudo-writing, or decorative script.

Avoid:
Characters, fish, footprints, ladders, dense bubbles, tiny gold dots, stippling, pebble carpets, all-over grain, glossy 3D objects, plastic render, elaborate frames, busy corners, dark central areas, or anything that reduces reading contrast.
```

## 정확한 본문

```text
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
```

## 조판 규칙

- 왼쪽 책등 안전 여백은 바깥쪽보다 넓게 둔다.
- 제목이나 페이지 안의 추가 문구를 만들지 않는다.
- 본문은 어두운 남색 또는 짙은 갈색의 큰 글씨로 조판한다.
- 대본의 줄 순서·문장부호·따옴표·쉼표를 그대로 유지한다.
- 문단 사이 여백은 줄 간격보다 약간 넓게 두고, 페이지 한가운데에 안정적으로 배치한다.
- 배경 장식은 글보다 먼저 보이지 않게 대비와 면적을 낮춘다.

## QA

- 대본 원문과 한 글자도 다르지 않다.
- 모든 글자가 선명하며 잘림·겹침·접힘선 침범이 없다.
- 맞은편 2페이지와 팔레트가 이어지지만 글이 가장 먼저 읽힌다.
- 글자 영역에 자글자글한 무늬·기포·점묘가 없다.
- 잘못 생성된 글자나 장식 문자가 없다.

## 생성 결과

### 장식 배경 v1

- 파일: `03_scene01_text_background_v1.png`
- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-de6e4c5d-87e3-44d3-a52b-a3ed80625263.png`
- 방식: built-in 이미지 생성, `illustration-story`.
- 결과: 넓은 무늬 없는 크림색 본문 영역, 산호색·청록색 이중 테두리, 오른쪽 위 산호와 오른쪽 아래 조개, 아래쪽 `조개 간식 / 책 / 빵` 그림 기호만 사용함.
- 텍스트 QA: 생성 배경에 글자·숫자·가짜 문자가 없음.

### 글 조판 후보 v1

- 파일: `03_scene01_text_candidate_v1.png`
- 상태: `superseded by v2 — retained as history`
- 원문 QA: 대본에서 직접 추출한 7문단 12줄이며 UTF-8 본문 SHA-256 `C250C100F5B360E2CA07C58B449F97A9C842AD1055D886A110B0984C5A2D12C3`.
- 보류 이유: Noto Sans KR 가변 글꼴의 기본 굵기 100이 화면에서는 깨끗하지만 인쇄 시 획이 지나치게 가늘 수 있음.
- 파일 QA: 1054×1492 PNG, 997,261 bytes, SHA-256 `431C4C75471077892CC7AFA814F78176C7DBD3F8DEA0D3CAE1CE016214B6CC4B`.

### 글 조판 후보 v2 — 중간 굵기

- 파일: `03_scene01_text_candidate_v2_medium_weight.png`
- 상태: `superseded by v3 — retained as history`
- 변경: 글꼴·크기·줄바꿈·위치·색을 유지하고 가변 글꼴 굵기만 100에서 450으로 올려 인쇄 가독성을 보강함.
- 원문 QA: 대본에서 직접 추출한 7문단 12줄이며 문장·줄 순서·문장부호·따옴표·쉼표가 정확함. UTF-8 본문 SHA-256 `C250C100F5B360E2CA07C58B449F97A9C842AD1055D886A110B0984C5A2D12C3`.
- 레이아웃 QA: 왼쪽 책등 여백, 오른쪽 바깥 여백, 위아래 장식 안전 여백을 침범하지 않음. 마지막 본문 기준선은 y=1216이며 아래 그림 기호와 분리됨.
- 스타일 QA: 기본 본문은 짙은 남색, 혼란 문단은 차분한 산호색, 손님 대사는 청록색으로 제한해 맞은편 삽화의 팔레트만 이어감.
- 시각 피로 QA: 본문 바탕에 점묘·기포·잔자갈·미세 무늬가 없고 장식이 가장자리에만 있음.
- 파일 QA: 1054×1492 PNG, 991,715 bytes, SHA-256 `1DC7A09B3DCB91C6A1586A70CCEF189796A972F63974485D8149B77B9CEF5568`.

### 글 조판 후보 v3 — 안동엄마까투리체

- 사용자 QA: `안동엄마까투리체 가능? 깔려있을텐데` / `그걸로 해보자`
- 파일: `03_scene01_text_candidate_v3_katuri.png`
- 사용 글꼴: `C:/Windows/Fonts/Katuri.ttf`, 안동엄마까투리체 48px.
- 상태: `approved — promoted to final/03_페이지.png`
- 변경: 배경·글자 크기·줄바꿈·좌표·문단 간격·색 강조는 그대로 두고 글꼴만 Noto Sans KR에서 안동엄마까투리체로 교체함.
- 원문 QA: 대본에서 직접 추출한 7문단 12줄. UTF-8 본문 SHA-256 `C250C100F5B360E2CA07C58B449F97A9C842AD1055D886A110B0984C5A2D12C3`로 이전 후보와 동일함.
- 레이아웃 QA: 가장 긴 줄과 마지막 문단이 모두 인쇄 안전 영역 안에 있으며 마지막 본문 기준선은 y=1216으로 아래 기호와 분리됨.
- 가독성 QA: 둥글고 굵은 획이 작은 화면과 인쇄에서 분명하며, 어린이 그림책 분위기가 강화됨.
- 파일 QA: 1054×1492 PNG, 1,020,833 bytes, SHA-256 `64E824582FF4009F6BDC31FC2F41C0D8527F2061AB49427126F011A2F1EE865A`.

### v3 사용자 승인 및 최종 승격

- 사용자 확인: `좋아 이걸로 하자`
- 최종 파일: `series/sherlock-fin-deep-city/images/episodes/자주빛_리본의_손님/final/03_페이지.png`
- 후보·최종본 SHA-256: `64E824582FF4009F6BDC31FC2F41C0D8527F2061AB49427126F011A2F1EE865A`, 해시 일치.
- 에피소드 글 페이지 공통 서체: `C:/Windows/Fonts/Katuri.ttf` 안동엄마까투리체.
