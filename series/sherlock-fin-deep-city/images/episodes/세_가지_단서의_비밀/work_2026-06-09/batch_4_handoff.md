# 세 가지 단서의 비밀 - Batch 4 마무리 핸드오프

## 현재 상태

- 작업 위치: `series/sherlock-fin-deep-city/images/episodes/세_가지_단서의_비밀/work_2026-06-09`
- 대본: `series/sherlock-fin-deep-city/docs/episodes/세_가지_단서의_비밀.md`
- 페이지 계획: `page_plan.md`
- 워크로그: `episode_worklog.md`
- Batch 4 프롬프트 계획: `batch_4_prompt_plan.md`
- 본편 구성: 00 표지 + 01-12 본문, 총 13장.
- 현 대본 기준 Batch 4가 마지막 배치다.
- 2026-06-11 사용자 요청으로 `final` 폴더에 전체 13장을 승격했다.

## Batch 4 모바일 확인 후보

- 새 꽃게 친구 레퍼런스:
  - `reference_setup/candidates/꽃게친구들_reference_candidate_v1.png`
  - 크랩슨과 분리되는 작은 일반 꽃게 친구들이다.
  - 신사 모자, 검은 정장, 보라색 보타이는 크랩슨에게만 허용한다.
- 11 페이지 후보:
  - `batch_4_a5/11_page_candidate_a5_v2_crab_friends_ref.png`
  - 크랩슨이 별진주를 펄리에게 돌려주는 순간.
  - 새 꽃게 친구 레퍼런스를 반영해 배경 꽃게들이 크랩슨 복제처럼 보이는 문제를 수정했다.
- 12 페이지 후보:
  - `batch_4_a5/12_page_candidate_a5_v2_crab_friends_ref.png`
  - 첫 사건 성공 마무리.
  - 별진주는 펄리 조개 안에 들어가 있고, 세 단서 아이콘이 뒤쪽에 보인다.
  - 새 꽃게 친구 레퍼런스를 반영해 크랩슨과 일반 꽃게 친구들이 분리되었다.

## 대체/미채택 기록

- `batch_4_a5/11_page_candidate_a5_v1.png`
  - 대체됨. 뒤쪽 꽃게 친구들이 모두 크랩슨처럼 신사 모자/정장 차림으로 나와 실패.
- `batch_4_a5/12_page_candidate_a5_v1.png`
  - 대체됨. 아래쪽 꽃게 친구들이 크랩슨 복제처럼 보이는 문제가 있다.
- `batch_4_a5/11_page_candidate_a5_v3_crab_friends_textfix.png`
- `batch_4_a5/12_page_candidate_a5_v3_crab_friends_textfix.png`
  - 미채택 기록. 사용자가 생성 원본 텍스트가 문제없다고 확인했으므로 모바일 확인 후보로 쓰지 않는다.

## Google Drive 모바일 확인

- Google Doc:
  - `https://docs.google.com/document/d/1R3P9GpyOnrb0XboTanYr87BnviubJGnoVmUyE_f7p78/edit?usp=drivesdk`
- 포함 이미지:
  - 꽃게 친구들 레퍼런스 v1
  - 11 페이지 v2
  - 12 페이지 v2
- 별도 텍스트 보정판은 문서에 넣지 않았다.

## carried-forward 잠금

- 크랩슨은 한 명만 등장해야 한다.
- 일반 꽃게 친구들은 `꽃게친구들_reference_candidate_v1.png`처럼 작은 일반 꽃게여야 한다.
- 꽃게 친구들은 악역이 아니라, 파티 장식으로 착각한 뒤 미안해하는 밝고 안전한 친구들이다.
- 별진주는 분홍색 둥근 별 모양 진주다.
- 11페이지에서는 별진주를 펄리에게 돌려주는 순간이 핵심이다.
- 12페이지에서는 별진주가 펄리의 조개 가방 안에 안전하게 들어가 있어야 한다.
- 셜록 핀은 하나의 연속된 인어 하반신과 꼬리만 보여야 한다.
- 최종 승격 전에는 00-12 전체 페이지의 비율, 텍스트, 캐릭터 정체성, 오염 여부를 다시 확인한다.

## 다음 액션

1. 필요하면 05, 09, 11, 12의 `1024x1536` 비율 후보를 정확한 A5 비율로 리마스터한다.
2. 필요하면 Google Drive에 final 13장 확인 문서를 별도로 만든다.
3. 배포/커밋 전에는 `final` 폴더 13장과 워크로그 변경분을 함께 확인한다.
