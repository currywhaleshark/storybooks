# 자줏빛 리본의 손님 — 내지 10페이지 장면 05 그림 계획

## 범위

- 내지 10페이지: 장면 05 그림 전용 왼쪽 페이지.
- 검토 후보: `10_scene05_illustration_candidate_v1.png`.
- 상태: `v1 hold — Pearly arm anatomy correction required; v2 planned`.
- 맞은편 11페이지는 장면 05 원문을 안동엄마까투리체로 별도 조판한다.
- 그림 속 문자는 카드에 필요한 자모 `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`만 허용한다.

## 원본 장면 잠금

- 마지막 간판 뒤에서 숨겨진 단서를 발견하는 순간이다.
- 셜록 핀이 간판을 살짝 들추고 뒤쪽의 카드 보관 공간을 살핀다.
- 별도의 소용돌이 무늬 카드 한 장이 있다.
- 자모 카드들은 바닥에 무작위로 흩어진 것이 아니라 세 개의 작은 테두리 안에 나뉘어 정돈되어 있다.
- 첫 묶음은 `ㅁ ㅣ`, 두 번째 묶음은 `ㅇ ㅕ ㄱ`, 세 번째 묶음은 `ㅅ ㅜ ㅍ`이다.
- 펄리는 아래 조개를 지지면에 둔 채 카드를 조심스럽게 모은다.

## 실제 입력 레퍼런스

1. `references/characters/셜록핀.png`
2. `references/characters/펄리.png`
3. `references/locations/자줏빛_리본의_손님_산호골목_세가게_레퍼런스.png`
4. `references/props/자줏빛_리본의_손님_핵심단서_소품_레퍼런스.png`

- 이전에 생성한 본편 페이지나 보류 후보는 입력하지 않는다.
- 공식 레퍼런스 네 장에서 새로 한 번에 생성해 반복 편집에 따른 질감 누적을 피한다.

## 구도

- 세로 그림책 면, 발견 순간을 강조한 중간 거리 구도.
- 배경은 공식 순환 상태의 오른쪽 보라색 조개 도서관이며, 위에는 잘못 걸린 빵 그림 간판이 보인다.
- 셜록 핀은 간판 옆으로 헤엄쳐 올라가 한 손으로 나무 간판을 살짝 앞으로 들어 숨은 공간을 보여준다.
- 카드들은 간판 바로 뒤쪽의 넓고 안정된 조개 모양 선반 또는 얕은 받침에 정돈되어 있다.
- 소용돌이 카드 한 장은 세 자모 묶음과 떨어져 별도로 놓는다.
- 자모 카드 세 묶음은 정면에 가깝게 보여 글자와 순서가 명확히 읽혀야 한다.
- 펄리는 카드 선반의 낮고 넓은 받침 위에 아래 조개 전체를 놓고, 손 하나로 카드 한 장을 조심스럽게 모으는 동작을 한다.
- 카드와 인물의 손이 겹쳐 글자를 가리지 않는다.

## 카드 정확성

- 왼쪽 청록 테두리 안: 아이보리 카드 2장, 왼쪽부터 `ㅁ`, `ㅣ`.
- 가운데 금빛 테두리 안: 아이보리 카드 3장, 왼쪽부터 `ㅇ`, `ㅕ`, `ㄱ`.
- 오른쪽 보라 테두리 안: 아이보리 카드 3장, 왼쪽부터 `ㅅ`, `ㅜ`, `ㅍ`.
- 각 카드는 정확히 한 글자만 담고, 글자는 짙은 남색의 단정한 굵은 형태다.
- `미`, `역`, `숲`, `미역숲` 완성 카드와 다른 한글·영문·숫자를 넣지 않는다.
- 소용돌이 카드는 공식 시트의 짙은 보라색 바탕, 얇은 금빛 테두리, 중앙 금빛 소용돌이 1개를 유지한다.

## 캐릭터·장소 연속성

- 셜록 핀: 청록색 머리, 갈색 탐정 모자와 코트, 검은 장갑, 청록색 인어 꼬리. 다리·발·신발 금지.
- 펄리: 분홍 위 조개 1개와 받침에 닿는 얕은 아래 조개 1개, 크림색 얼굴, 검은 나비넥타이. 아래 조개 밑·뒤의 별도 몸통·배·꼬리·다리·발·신발 금지.
- 조개 도서관: 파랑·보라 외벽, 조개형 출입구, 책장과 책이 보이는 내부, 위에는 빵 그림 간판.
- 분홍 빵집이나 금빛 간식 가게를 중심 장소로 바꾸지 않는다.

## 저질감 잠금

- 넓고 매끈한 색면, 선명하고 단정한 외곽선, 제한된 부드러운 명암을 사용한다.
- 잔자갈·점묘·반복 반짝이·조밀한 기포·과도한 산호 돌기·종이 노이즈·거친 카드 질감을 최소화한다.
- 카드 글자와 인물 얼굴은 깨끗한 단색 면으로 유지한다.
- 3D 토이 광택, 사진 질감, 과도한 비늘 하이라이트를 금지한다.

## 생성 프롬프트

```text
Use case: illustration-story
Asset type: vertical full-page children's storybook illustration, illustration-only page
Input images: Image 1 official Sherlock Fin identity reference; Image 2 official Pearly identity reference; Image 3 official Coral Alley three-shop and switched-sign reference; Image 4 official clue-prop and exact Korean jamo card reference.

Create a brand-new scene from the four official references only. Do not use any previous generated story page. Show the discovery behind the LAST sign in the switched-sign sequence: the rightmost blue-purple shell library in Coral Alley, with the wrong wooden BREAD pictogram sign hanging above it. Sherlock Fin floats beside the high sign and gently lifts the wooden signboard slightly forward with one black-gloved hand, revealing a wide stable shell-shaped shelf or shallow compartment immediately behind it.

On that hidden shelf are exactly four organized clue areas. First, one separate dark-purple card with a thin gold border and one centered gold spiral, matching Image 4. Next are exactly three small bordered trays, never a random scatter. The left teal-bordered tray contains exactly two ivory cards, left-to-right: `ㅁ` then `ㅣ`. The middle gold-bordered tray contains exactly three ivory cards, left-to-right: `ㅇ` then `ㅕ` then `ㄱ`. The right purple-bordered tray contains exactly three ivory cards, left-to-right: `ㅅ` then `ㅜ` then `ㅍ`. Each small card has exactly one bold dark-navy Korean jamo, copied faithfully from Image 4. No missing, duplicated, substituted, rotated, merged, or extra characters. Do not show assembled syllable cards `미`, `역`, `숲`, or the word `미역숲`.

Pearly rests with the entire official shallow lower shell on the broad shelf/support beside the cards, with a soft contact shadow, and carefully reaches toward one card without covering any letter. Match the official upper shell, cream face, black bow tie, and small gold magnifying glass. No separate lower body, torso beneath the shell, belly, tail, legs, feet, shoes, or pedestal.

Match Sherlock Fin's official teal hair, brown deerstalker hat and coat, black gloves, serious curious expression, and one continuous teal mermaid tail. No legs, feet, or shoes. Use exactly these two characters.

Keep the cards large, front-facing, evenly spaced, and readable as the main clue. Keep the library facade, books, and a few large coral shapes simple and secondary. Established polished 2D children's-book style, clean rounded linework, broad smooth color areas, gentle limited shading, friendly underwater light. Strongly suppress visual noise: almost no tiny pebbles, stippling, repeated sparkles, dense bubbles, coral specks, paper grain, fabric grain, or repeated scale highlights.

No title, caption, body text, sign words, speech bubbles, numbers, English, watermark, border, extra characters, ribbon, pocket watch, ladder, footprints, notebook, or unrelated episode props. The only visible writing anywhere is exactly the eight required jamo characters on the eight small clue cards.
```

## QA

- 셜록 핀과 펄리만 등장한다.
- 오른쪽 보라색 조개 도서관과 잘못 걸린 빵 그림 간판이 보인다.
- 소용돌이 카드가 정확히 1장이고 자모 묶음과 분리되어 있다.
- 세 테두리에 `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`이 정확한 순서로 보인다.
- 카드가 무작위로 흩어지지 않고 손·조개·간판에 가려지지 않는다.
- 셜록 핀에게 다리·발·신발이 없고 꼬리가 자연스럽다.
- 펄리의 아래 조개 전체가 받침에 닿고 별도 하반신처럼 보이는 형태가 없다.
- 리본·회중시계·사다리·발자국·다른 에피소드 소품이 없다.
- 카드 외의 글자·말풍선·가짜 문자가 없다.
- 미세 질감과 반복 반짝이가 억제되어 눈이 편안하다.

## 후보 v1 결과

- 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-1dc25b6b-cd8c-4cde-9c89-73e9c081d26a.png`.
- 작업 원본: `10_scene05_illustration_candidate_v1_raw.png`.
- 검토 후보: `10_scene05_illustration_candidate_v1.png`.
- 생성 방식: 이전 생성 페이지를 입력하지 않고 공식 셜록 핀·펄리·산호 골목·핵심 단서 소품 레퍼런스 4장만 사용한 신규 단일 생성.
- 장소 QA: 오른쪽 보라색 조개 도서관과 잘못 걸린 빵 그림 간판이 보이고, 셜록 핀이 간판을 살짝 들어 올림.
- 소품 QA: 소용돌이 카드 1장이 세 자모 묶음과 분리되어 있음.
- 자모 QA: 청록 테두리 `ㅁ ㅣ`, 금빛 테두리 `ㅇ ㅕ ㄱ`, 보라 테두리 `ㅅ ㅜ ㅍ`이 정확한 순서와 개수로 선명하게 보임. 완성 음절·추가 글자 없음.
- 정돈 QA: 세 묶음이 각각 작은 테두리 안에 가지런히 놓이고 무작위로 흩어지거나 인물 손에 가려지지 않음.
- 신체 QA: 셜록 핀은 연속된 인어 꼬리이며 다리·발·신발 없음. 펄리는 아래 조개 전체가 넓은 받침에 닿고 별도 하반신·꼬리·다리·발 없음.
- 오염 QA: 리본·회중시계·사다리·발자국·다른 에피소드 소품·말풍선·카드 외 글자 없음.
- 저질감 QA: 카드·인물·큰 조개 구조는 매끈한 색면 중심이며 잔자갈·점묘·반복 반짝이·과도한 기포가 억제됨.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,461,747 bytes, SHA-256 `C3E2DC6E78A255C781E41FEBE4BEC1137F31746BBFE00FCE486242271DF4300C`.
- 사용자 QA: `펄리 팔이 뭔가 가늘어져서 원래의 통통한 아기팔로`.
- v1 판정: 뻗은 팔이 공식 시트보다 길고 가늘어 `hold — do not use`.
- v2 방식: v1을 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v2 펄리 팔 잠금: 두 팔 모두 공식 시트처럼 짧고 통통한 아기팔, 둥근 팔뚝, 작은 손. 긴 팔·가는 팔·뾰족한 팔꿈치·성인형 손목 금지.
- v2 동작 잠금: 펄리를 카드 가까이에 배치해 팔을 길게 뻗지 않아도 되며, 한 손은 조개 가장자리 가까이에서 짧게 카드를 향하고 다른 손은 작은 돋보기를 몸 가까이에 든다.
- v2 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-2708d9c6-8ac7-4ec1-9344-fd10fc262789.png`.
- v2 작업 원본: `10_scene05_illustration_candidate_v2_chubby_arms_raw.png`.
- v2 검토 후보: `10_scene05_illustration_candidate_v2_chubby_arms.png`.
- 팔 QA: 두 팔 모두 공식 시트에 가까운 짧고 통통한 아기팔, 둥근 팔뚝, 작은 손으로 교정됨. 긴 팔·가는 팔·뾰족한 팔꿈치·성인형 손목 없음.
- 동작 QA: 펄리가 카드 가까이에 있어 뻗은 팔의 길이가 짧고, 다른 손의 돋보기도 얼굴 가까이에 유지됨.
- 자모 QA: `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`의 순서·개수·테두리 색이 유지되고 추가 글자 없음.
- 장소·소품 QA: 보라색 조개 도서관, 빵 그림 간판, 소용돌이 카드 1장 유지.
- 신체 QA: 펄리 아래 조개 전체가 받침에 닿고 별도 하반신·꼬리·다리·발 없음. 셜록 핀은 연속된 인어 꼬리 유지.
- 저질감 QA: 큰 색면 중심이며 자글자글한 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,536,131 bytes, SHA-256 `D17FD4BBAE8EC1AF3CFFBC751A246CE079EC3251A1EB66B23FD95B2575C21BBC`.
- 사용자 추가 QA: `이번엔 너무 통통하네 / 간판을 들춰보니 그 아래에 있는 느낌으로 나타내면 좋겠음 / 지금 위치라면 사실 첫 페이지부터 보이고있어야하니까`.
- v2 판정: 팔이 공식 시트보다 과도하게 통통하고, 카드가 평소에도 보이는 열린 선반에 놓여 사건 도입부터 노출되었어야 하는 구조라 `hold — do not use`.
- v3 펄리 팔 잠금: v1의 가는 팔과 v2의 과장된 팔 사이. 공식 시트처럼 짧고 부드럽게 둥글며 약간 통통하되, 손목까지 풍선처럼 굵지 않고 작은 손으로 자연스럽게 좁아진다.
- v3 은닉 구조 잠금: 간판은 평소 벽의 얕은 오목칸을 완전히 덮는 뚜껑 역할을 한다. 셜록 핀이 간판의 아래쪽을 앞으로·위로 들춘 순간에만 간판 바로 뒤이자 아래의 어두운 숨김칸과 카드들이 드러난다.
- v3 가시성 잠금: 카드와 테두리는 간판이 정상 위치일 때 외부에서 전혀 보이지 않는다. 건물의 열린 진열 선반·창문·평상시 노출 선반 위에 놓지 않는다.
- v3 생성 방식: v1·v2를 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v3 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-23c514b7-9ea0-4947-9f3d-afdcee322363.png`.
- v3 작업 원본: `10_scene05_illustration_candidate_v3_hidden_compartment_raw.png`.
- v3 검토 후보: `10_scene05_illustration_candidate_v3_hidden_compartment.png`.
- 은닉 구조 QA: 빵 간판이 위쪽 두 고리에 걸린 뚜껑처럼 앞으로 들려 있고, 같은 면적의 어두운 오목칸과 카드가 바로 뒤·아래에서만 드러남. 간판을 내리면 카드 전체가 가려지는 구조.
- 가시성 QA: 카드는 열린 진열 선반·창문·평상시 노출면에 놓이지 않으며, 이번 발견 전부터 보였을 법한 배치가 아님.
- 펄리 팔 QA: v1보다 둥글고 v2보다 슬림한 짧은 아기팔과 작은 손으로 조정됨. 과도하게 가늘거나 풍선처럼 굵지 않음.
- 자모 QA: `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`의 순서·개수·테두리 색이 정확하고 추가 글자 없음.
- 신체·소품 QA: 펄리 아래 조개가 오목칸의 넓은 아랫턱에 접지하고 별도 하반신·꼬리·다리·발 없음. 셜록 핀은 인어 꼬리. 소용돌이 카드 1장.
- 저질감 QA: 큰 조개 외벽과 어두운 숨김칸의 넓은 색면 중심이며 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,384,925 bytes, SHA-256 `7210B881C80EF5033D0ABEC4A09749134857DA45BEBA8D61D3D3960255225B3D`.
- 사용자 추가 QA: `간판이 건물 아래로 내려와버렸네 / 원래 건물 간판위치는 건물 위쪽이잖아`.
- v3 판정: 숨김 구조는 읽히지만 간판과 오목칸이 출입구 높이까지 내려와 공식 산호 골목의 지붕선 위 간판 위치와 불일치하므로 `hold — do not use`.
- v4 높이 잠금: 카메라를 조금 넓혀 보라색 조개 도서관의 출입구·책장·상부 지붕선을 함께 보여주고, 빵 간판은 공식 레퍼런스처럼 건물 꼭대기 지붕선 위의 높은 금빛 막대에 달린다.
- v4 은닉 잠금: 카드 오목칸도 간판 바로 뒤의 높은 지붕선 위치에 붙어 있으며, 간판이 내려가면 오목칸 전체를 완전히 덮는다. 건물 중앙 창구·출입구·낮은 선반으로 이동하지 않는다.
- v4 동작 잠금: 셜록 핀이 높은 곳에서 간판 아래 모서리를 위로 들추고, 펄리는 그 바로 뒤의 넓은 지붕선 받침에 아래 조개를 놓는다.
- v4 생성 방식: v1·v2·v3를 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v4 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-cdd25dd0-0d88-48b7-8bae-8933131f71a6.png`.
- v4 작업 원본: `10_scene05_illustration_candidate_v4_high_sign_hidden_compartment_raw.png`.
- v4 검토 후보: `10_scene05_illustration_candidate_v4_high_sign_hidden_compartment.png`.
- 높이 QA: 도서관 출입구와 책장이 화면 아래 절반에 보이고, 빵 간판과 숨김칸은 공식 레퍼런스처럼 건물 꼭대기 지붕선 위에 명확히 위치함.
- 은닉 QA: 높은 간판이 위쪽 두 고리에 매달린 채 들려 있고, 같은 폭의 어두운 오목칸이 바로 뒤에 드러남. 간판을 내리면 카드·테두리·펄리가 놓인 받침 영역이 가려지는 구조.
- 자모 QA: `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`의 순서·개수·테두리 색 정확, 추가 글자·완성 음절 없음.
- 펄리 QA: 팔은 짧고 완만하게 둥근 중간 굵기이며, 아래 조개 전체가 높은 오목칸의 안정된 받침에 접지. 별도 하반신·꼬리·다리·발 없음.
- 셜록 핀 QA: 높은 간판 옆에서 한 손으로 아래 모서리를 들고 다른 손에 돋보기를 듦. 연속된 인어 꼬리, 다리·발·신발 없음.
- 저질감 QA: 넓은 조개 외벽과 수면 색면 중심이며 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,404,869 bytes, SHA-256 `4186F687C26BCDE99161D404EE6B013D60C55A7732C4C4D0BEA53716D9B5040D`.
- 사용자 추가 QA: `아 좋은데 펄리 조개껍질이 어긋났다`.
- v4 판정: 간판 높이와 숨김 구조는 통과했으나 펄리의 위 조개와 아래 조개 중심축·힌지축이 어긋나 몸이 옆으로 밀려 보이므로 `hold — do not use`.
- v5 조개 정렬 잠금: 펄리는 정면에 가까운 자세. 위 조개의 꼭대기 중심, 얼굴 중심, 나비넥타이 매듭, 아래 조개의 중앙 골이 하나의 수직선에 놓인다.
- v5 힌지 잠금: 위 조개의 아래 양끝과 아래 조개의 뒤쪽 양끝이 좌우 대칭으로 같은 힌지축에 맞물린다. 위 조개가 왼쪽·오른쪽으로 밀리거나 회전하지 않는다.
- v5 실루엣 잠금: 아래 조개 전체가 받침에 수평으로 닿고, 위·아래 조개가 같은 원근과 크기 비율을 공유한다. 중복 조개·세 번째 조개·분리된 조각 금지.
- v5 보존 잠금: v4의 건물 꼭대기 간판 위치, 간판 뒤 숨김칸, 도서관 출입구와 책장, 정확한 자모 묶음, 중간 굵기 아기팔을 유지한다.
- v5 생성 방식: v1~v4를 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v5 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-1844902c-2190-4d40-9564-0fee538b61b0.png`.
- v5 작업 원본: `10_scene05_illustration_candidate_v5_pearly_shell_aligned_raw.png`.
- v5 검토 후보: `10_scene05_illustration_candidate_v5_pearly_shell_aligned.png`.
- 조개 중심축 QA: 위 조개 꼭대기, 얼굴, 나비넥타이, 아래 조개 중앙이 하나의 수직선에 정렬됨.
- 힌지 QA: 위·아래 조개의 좌우 끝이 같은 높이에서 대칭으로 맞물리고, 위 조개가 좌우로 밀리거나 회전하지 않음.
- 실루엣 QA: 아래 조개 전체가 높은 받침에 수평으로 닿으며 중복 조개·세 번째 조개·분리 조각·별도 하반신 없음.
- 보존 QA: 도서관 전경, 건물 꼭대기 높은 빵 간판, 간판 뒤 숨김칸, 소용돌이 카드, `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`, 셜록 핀과 중간 굵기 펄리 팔 유지.
- 저질감 QA: 큰 색면 중심이며 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,487,432 bytes, SHA-256 `99412410580E49EEF68AE2AA38207ADCED404AF62DB3F1603CAA95C6912AE24C`.
- 상태: `candidate v5 generated — user review pending`. 승인 전 `final/10_페이지.png`로 승격하지 않는다.
- 사용자 추가 QA: `정면은 좀 이상하지않겠냐 / 같이 카드를 보고있어야지`.
- v5 판정: 펄리의 조개 정렬은 통과했으나 정면을 바라보는 자세 때문에 셜록 핀과 함께 단서를 살피는 발견 장면의 시선 흐름이 끊기므로 `hold — do not use`.
- v6 공동 시선 잠금: 셜록 핀과 펄리 모두 독자·카메라를 보지 않고, 눈·고개·돋보기 방향이 소용돌이 카드와 세 자모 묶음으로 모인다.
- v6 펄리 자세 잠금: 펄리는 카드 옆에서 왼쪽 아래를 보는 자연스러운 3/4 자세. 위 조개와 아래 조개는 하나의 단단히 맞물린 조개쌍처럼 같은 각도·원근·소실 방향으로 함께 회전한다.
- v6 조개 정렬 잠금: 3/4 원근에서도 위 조개 중심·얼굴·나비넥타이·아래 조개 중심이 동일한 기울어진 로컬 축에 놓이고, 양쪽 힌지가 맞물린다. 옆밀림·비틀림·중복 조개·세 번째 조개 금지.
- v6 동작 잠금: 펄리의 짧고 적당히 통통한 아기팔 하나는 카드 가까이에, 다른 손의 작은 금빛 돋보기는 카드 쪽을 향한다. 셜록 핀의 고개와 돋보기도 같은 카드 묶음을 향한다.
- v6 보존 잠금: 건물 꼭대기의 높은 빵 간판과 간판 뒤 숨김칸, 아래 절반의 도서관 출입구·책장, 소용돌이 카드 1장, `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`, 저자극 저질감 색면을 유지한다.
- v6 생성 방식: v1~v5를 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v6 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-01df6f0c-b4b6-4bc9-ad4d-6ace762c8745.png`.
- v6 내부 QA 판정: 펄리 조개 정렬과 자모는 양호하나 두 인물의 시선이 카드보다 서로에게 걸리고, 셜록 핀이 간판을 실제로 들어 올리지 못해 `hold — do not use`.
- v7 공통 응시점 잠금: 세 자모 트레이의 중앙을 명확한 공통 응시점으로 설정한다. 두 인물의 동공·코끝·고개·돋보기 렌즈축을 모두 이 지점으로 향하게 한다.
- v7 동작 잠금: 셜록 핀의 한 손은 간판 아랫모서리를 잡아 확실히 위로 젖히고, 다른 손의 돋보기는 아래 카드에 기울인다. 펄리는 카드 바로 옆에서 몸 전체를 카드 쪽으로 돌리고 눈을 아래로 내린다.
- v7 생성 방식: v1~v6을 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v7 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-04495883-2b7a-490f-bcc4-52ecc7a07120.png`.
- v7 작업 원본: `10_scene05_illustration_candidate_v7_shared_card_gaze_raw.png`.
- v7 검토 후보: `10_scene05_illustration_candidate_v7_shared_card_gaze.png`.
- 공동 시선 QA: 펄리의 동공·고개·작은 금빛 돋보기는 오른쪽 아래 자모 카드로, 셜록 핀의 동공·고개·돋보기는 왼쪽 아래 같은 카드 묶음으로 향함. 두 인물 모두 독자 정면을 응시하지 않음.
- 간판 동작 QA: 셜록 핀이 높은 빵 간판의 아랫모서리를 잡아 위·바깥쪽으로 젖히고, 바로 뒤의 어두운 숨김칸과 카드 받침이 드러남.
- 펄리 구조 QA: 위·아래 조개 중심이 같은 축에 맞물리고 아래 조개 전체가 받침에 접지. 중복 조개·세 번째 조개·별도 하반신·다리·발 없음.
- 자모 QA: 소용돌이 카드 1장과 `ㅁ ㅣ / ㅇ ㅕ ㄱ / ㅅ ㅜ ㅍ`의 순서·개수·테두리 색이 정확하고 추가 글자 없음.
- 장소 QA: 도서관 출입구·책장이 아래 절반에 보이고, 빵 간판과 숨김칸은 건물 꼭대기 지붕선 위에 유지됨.
- 저질감 QA: 큰 색면 중심이며 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,433,304 bytes, SHA-256 `414E743DE9ED17D23E570B1CA98D3B4B759A2175612FC8E4DDA7CF047D06A226`.
- 상태: `candidate v7 generated — user review pending`. 승인 전 `final/10_페이지.png`로 승격하지 않는다.
- 사용자 추가 QA: `이번에는 카드가 붙어버렸다야`.
- v7 판정: 공동 시선과 간판 동작은 통과했으나 각 자모 묶음이 한 장의 긴 가로판처럼 합쳐져 공식 소품 레퍼런스의 낱장 카드 구조와 불일치하므로 `hold — do not use`.
- v8 낱장 카드 잠금: 자모는 총 8장의 독립된 세로형 카드다. 청록 `ㅁ`, 청록 `ㅣ`; 금색 `ㅇ`, 금색 `ㅕ`, 금색 `ㄱ`; 보라 `ㅅ`, 보라 `ㅜ`, 보라 `ㅍ`.
- v8 분리 가시성 잠금: 각 카드마다 네 모서리·개별 색 테두리·얇은 그림자·카드 사이 배경색 틈이 모두 보여야 한다. 두 글자 이상을 한 장에 인쇄하거나 긴 가로판·연결판·공용 테두리로 합치지 않는다.
- v8 묶음 구조 잠금: 2장·3장·3장은 서로 가까이 놓여 세 묶음으로 읽히되, 묶음 사이 간격은 카드 사이 간격보다 넓다. 별도의 큰 트레이가 있더라도 8장 각각의 완전한 윤곽을 가리지 않는다.
- v8 보존 잠금: v7의 두 인물이 같은 카드를 보는 시선, 높은 간판을 젖힌 동작, 간판 뒤 숨김칸, 펄리 조개 정렬, 소용돌이 카드 1장, 도서관 전경, 낮은 미세 질감을 유지한다.
- v8 생성 방식: v1~v7을 입력하거나 편집하지 않고 공식 레퍼런스 4장만 사용한 신규 단일 생성.
- v8 생성 원본: `C:/Users/yurib/.codex/generated_images/019fdc33-d58d-79f2-a486-33638838b7db/exec-44e28802-7ac7-4155-9e8a-ad4aa5062725.png`.
- v8 작업 원본: `10_scene05_illustration_candidate_v8_discrete_cards_raw.png`.
- v8 검토 후보: `10_scene05_illustration_candidate_v8_discrete_cards.png`.
- 낱장 구조 QA: 총 8장의 세로형 자모 카드가 각자 완전한 네 모서리·독립 색 테두리·그림자·사이 틈을 가지며 서로 닿거나 연결되지 않음.
- 자모 QA: 청록 `ㅁ`, `ㅣ`; 금색 `ㅇ`, `ㅕ`, `ㄱ`; 보라 `ㅅ`, `ㅜ`, `ㅍ`이 각각 한 글자씩 정확히 배치됨. 추가 글자·완성 음절 없음.
- 묶음 QA: 2장 / 3장 / 3장으로 읽히고, 묶음 사이 간격이 낱장 사이보다 넓음. 소용돌이 카드 1장 별도 유지.
- 공동 시선 QA: 펄리의 고개와 작은 돋보기, 셜록 핀의 동공·고개·돋보기가 카드 쪽으로 내려가며 독자 정면 응시를 피함.
- 구조 QA: 높은 간판이 위로 젖혀져 숨김칸이 드러나고, 펄리 위·아래 조개 중심축이 맞물리며 아래 조개가 받침에 접지함.
- 저질감 QA: 큰 색면 중심이며 점묘·잔기포·반복 반짝이를 억제함.
- 규격 QA: 생성 원본 1024×1536 보존, 검토 후보 1054×1492 PNG.
- 파일 QA: 후보 2,513,472 bytes, SHA-256 `A89D3995D56D9A85B7A0A95B9F181B7C5242F410881C15132499671169C06099`.
- 상태: `candidate v8 generated — user review pending`. 승인 전 `final/10_페이지.png`로 승격하지 않는다.
- 사용자 승인: `좋아 다음`.
- 최종 파일: `final/10_페이지.png`.
- 후보·최종본 SHA-256: `A89D3995D56D9A85B7A0A95B9F181B7C5242F410881C15132499671169C06099`, 해시 일치.
- 상태: `approved — promoted to final/10_페이지.png`.
