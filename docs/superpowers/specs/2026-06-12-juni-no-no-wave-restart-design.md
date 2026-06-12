# 준이의 싫어싫어파도 재시작 설계

Date: 2026-06-12

## Goal

`준이의 싫어싫어파도` 에피소드를 어제 후보 이미지의 시각 오염 없이 다시 시작한다. 새 작업은 공식 캐릭터, 배경, 소품 레퍼런스 PNG를 visual truth로 사용하고, 이전 후보 이미지는 과정 기록으로만 남긴다.

## Approved Scope

- 재시작 방식: A안, 완전 새 배치 시작
- 새 작업 폴더: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12`
- 첫 배치 범위: 표지, 1페이지, 2페이지, 3페이지
- 기존 `work_2026-06-11` 페이지 후보: `superseded` 또는 process history로만 취급
- 유지할 에피소드 전용 레퍼런스: `work_2026-06-11/reference_assets/shell_hourglass_ref.png`

## Reference Policy

생성 또는 수정 전에는 페이지별 실제 파일 경로 체크리스트를 만든다. 체크리스트에 없는 캐릭터나 소품은 생성 프롬프트에 등장시키지 않는다.

필수 공식 레퍼런스:

- 규칙서: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- 대본/프롬프트 문서: `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- 배경: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- 산호 터널: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- 준이: `series/coral-town-daycare/references/characters/준이.png`
- 마리 선생님: `series/coral-town-daycare/references/characters/마리_선생님.png`
- 방울이: `series/coral-town-daycare/references/characters/방울이.png`
- 토리: `series/coral-town-daycare/references/characters/토리.png`
- 몽글이: `series/coral-town-daycare/references/characters/몽글이.png`
- 루루: `series/coral-town-daycare/references/characters/루루.png`
- 아루: `series/coral-town-daycare/references/characters/아루.png`
- 포포: `series/coral-town-daycare/references/characters/포포.png`
- 수아: `series/coral-town-daycare/references/characters/수아.png`
- 조개 모래시계: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

금지:

- `work_2026-06-11/batch_1/*.png` 후보를 visual truth로 사용
- 어제 후보의 준이 얼굴, 눈, 몸 비율, 배경 색감, 친구 단순화 방식을 새 프롬프트에 반영
- 레퍼런스 파일 없이 텍스트 설명만으로 visible character 생성

## Page Workflow

1. `work_2026-06-12`에 새 `episode_worklog.md`, `page_plan.md`, `batch_1/batch_1_prompt_plan.md`를 만든다.
2. `work_2026-06-11` 후보의 상태를 새 worklog에 `superseded`로 명시한다.
3. 표지부터 3페이지까지 한 장씩 생성한다.
4. 각 페이지 생성 전 `References To Attach` 목록을 확인한다.
5. 각 페이지 생성 후 QA를 통과해야 다음 페이지로 넘어간다.
6. 후보가 통과하면 `candidate pass`로 기록한다. 사용자가 승인하기 전에는 `final`에 승격하지 않는다.

## QA Gates

### Character Identity

준이가 최우선 위험 요소다. 각 후보는 아래 기준을 먼저 통과해야 한다.

- 공식 `준이.png`처럼 긴 상어 주둥이를 유지한다.
- 작은 검은 단추눈을 유지한다.
- 둥근 고래, 파란 plush blob, 큰 슬픈 애니메이션 눈으로 변하지 않는다.
- 흰 배, 흰 아래 얼굴, 아가미, 등지느러미, 옆지느러미, 긴 꼬리, 세일러복, 파란 등원 가방을 유지한다.
- 감정 장면에서도 무섭거나 공격적인 상어로 보이지 않는다.

다른 캐릭터도 공식 종과 고정 디테일을 유지해야 한다. 특히 루루의 긴 주둥이/머리 능선/말린 꼬리, 아루의 사람 손발 금지, 포포의 보름달해파리 구조와 눈 숨김을 확인한다.

### Story Logic

- 3페이지에서는 `밖에 더 있고 싶어`를 말하거나 암시하지 않는다.
- 5페이지에서 준이가 처음 직접 `밖에... 더 있고 싶어.`라고 말한다.
- 6페이지의 조개 모래시계 제안은 준이가 마음을 말한 뒤에만 자연스럽게 이어진다.
- 1-8페이지는 등원 시간 외부 연속 장면이므로 준이는 파란 가방을 계속 멘다.
- 9페이지 실내 장면에서는 가방을 몸에 메지 않는다.

### Text

- 첫 생성부터 정확한 한국어 본문 텍스트를 포함한다.
- 텍스트가 틀렸지만 그림이 좋으면 그림 후보를 따로 보존하고, 텍스트 패널 수정 대상으로 기록한다.
- 틀린 텍스트가 있는 후보를 `final`로 승격하지 않는다.

### Contamination

- 어제 후보와 비슷한 둥근 준이 얼굴, 눈매 변경, 친구 단순화가 보이면 실패 처리한다.
- 의미 없는 글자, 추가 간판, pseudo-writing, random signage가 있으면 실패 또는 텍스트 수정 대상으로 둔다.
- 배경은 공식 어린이집 입구/놀이터와 산호 터널 계열을 유지한다.

## Output Rules

- 새 후보는 `work_2026-06-12/batch_1` 아래에 저장한다.
- 첫 배치 후보 이름은 `00_cover_candidate_2026-06-12_v1.png`, `01_candidate_2026-06-12_v1.png`처럼 날짜와 버전을 포함한다.
- 사용자가 승인한 파일만 이후 `final` 승격 대상으로 삼는다.
- 작업 중간마다 worklog에 상태, QA 결과, 다음 행동을 기록한다.

## First Action

새 배치 첫 장은 표지부터 시작한다. 표지가 다시 준이 레퍼런스를 놓치면 표지에서 즉시 멈추고 준이 중심 프롬프트를 더 좁힌다. 표지가 통과하면 1페이지로 넘어간다.
