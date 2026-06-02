# 새 세션 핸드오프: 조용해진 팝팝

## 현재 상태

- 사용자가 제공한 Drive 대본을 저장함: `series/sherlock-fin-deep-city/docs/episodes/조용해진_팝팝.md`
- 이름 충돌 때문에 신규 친구를 `초롱초롱`에서 `반짝이`로 변경함.
- 반짝이 설정: 바다반딧불이류 발광 오스트라코드 모티브, 작고 둥근 투명 몸, 부드러운 푸른 생물발광.
- 재즈광장 전용 공식 레퍼런스를 새로 고정함.
- 영어 간판 기준 변경: 짧은 영어/알파벳 네온 간판은 허용. 긴 문장과 본문처럼 보이는 과한 텍스트만 피함.

## 공식 참조

- 반짝이: `series/sherlock-fin-deep-city/references/characters/조용해진_팝팝_반짝이_레퍼런스.png`
- 재즈광장: `series/sherlock-fin-deep-city/references/locations/재즈광장_레퍼런스.png`
- 미역숲 쉼터: `series/sherlock-fin-deep-city/references/locations/초롱불을_어디에_두고_왔을까_미역숲쉼터_레퍼런스.png`
- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 팝팝: `series/sherlock-fin-deep-city/references/characters/팝팝.png`
- 펄리: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- 모모: `series/sherlock-fin-deep-city/references/characters/모모.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- 텍스트박스: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## 작업 문서

- 작업로그: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/work_2026-06-02/episode_worklog.md`
- 반짝이 계획: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/work_2026-06-02/reference_setup/reference_setup_prompt_plan.md`
- 재즈광장 계획: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/work_2026-06-02/location_setup/jazz_plaza_reference_prompt_plan.md`
- 배치1 계획: `series/sherlock-fin-deep-city/images/episodes/조용해진_팝팝/work_2026-06-02/batch_1/batch_1_prompt_plan.md`

## 다음 작업

1. `storybook-episode-production` 및 `imagegen` 스킬을 사용한다.
2. 배치1 계획 파일을 읽는다.
3. 실제 참조 이미지들을 `view_image`로 확인한다.
4. `00_cover_candidate_v1.png`, `01_candidate_v1.png`, `02_candidate_v1.png`, `03_candidate_v1.png`를 생성한다.
5. 각 후보를 작업로그에 기록하고, 텍스트 정확도/캐릭터 일치/장소 일관성 QA를 한다.
6. 사용자 승인 전에는 `final` 폴더로 승격하지 않는다.

## 주의

- 본편 이미지에는 대본의 정확한 한국어 텍스트가 들어가야 한다.
- 00 표지의 반짝이는 푸른빛 점으로 암시한다.
- 01은 밝은 평소 팝팝, 02는 조용해진 대비, 03은 펄리의 걱정과 셜록 핀의 관찰 시작이 핵심이다.
- 이전 `초롱이` 초롱아귀 레퍼런스를 반짝이 시각 참조로 쓰지 않는다.
