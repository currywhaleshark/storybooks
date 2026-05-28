# HANDOFF - codex/booklet-printing

작성일: 2026-05-28

## 브랜치

`codex/booklet-printing`

## 이번 묶음 범위

- 인쇄 레이아웃 도구 수정
- 산호마을 어린이집 새 에피소드 산출물 추가 및 캐릭터 레퍼런스 갱신
- 스토리북 에피소드 제작 스킬 번들 업데이트
- 다른 세션에서 생성된 셜록핀 에피소드 페이지 1장 포함

## 주요 변경 사항

### 1. 인쇄 레이아웃 도구

대상 파일:

- `tools/print_layout/pdf_layout.py`
- `tools/print_layout/tests/test_pdf_layout.py`
- `tools/print-layout/server.js`
- `tools/print-layout/public/app.js`
- `tools/print-layout/public/index.html`
- `tools/print-layout/public/styles.css`
- `tools/print-layout/README.md`
- `docs/superpowers/plans/2026-05-26-booklet-printing.md`
- `docs/superpowers/specs/2026-05-26-booklet-printing-design.md`

요약:

- 책자 인쇄용 `booklet` 출력 경로가 추가되었다.
- 웹 UI와 서버에서 책자 PDF 생성을 다룰 수 있게 수정되었다.
- 관련 계획/디자인 문서가 함께 추가되었다.

### 2. 산호마을 어린이집 에피소드

출력 폴더:

`C:/Users/USER/Documents/Projects/산호마을어린이집/series/coral-town-daycare/images/episodes/아루와_수아의_반짝_마음조개_new_2026-05-27`

포함 파일:

- `01_페이지.png` ~ `12_페이지.png`

메모:

- 사용자의 피드백을 반영해 `05`, `07`, `09`, `10`, `11`, `12` 페이지의 아루 추가 손/지느러미 문제를 교정한 최신본으로 교체했다.
- 문제 페이지는 아루 실루엣 안정성을 우선해 가방을 제거한 버전이 포함되어 있다.

### 3. 산호마을 어린이집 캐릭터 레퍼런스

대상 폴더:

`C:/Users/USER/Documents/Projects/산호마을어린이집/series/coral-town-daycare/references`

메모:

- 통합 캐릭터 시트 원본이 갱신되었다.
- 백업 및 후보 시트 파일이 함께 추가되었다.

### 4. 기타 포함 변경

- `storybook-episode-production-skill.zip` 갱신
- `series/sherlock-fin-deep-city/images/episodes/색소폰에서_들리는_작은_소리/12_페이지.png` 추가

## 확인 경로

집에서 바로 확인할 때 우선 보면 되는 위치:

- 산호마을 새 에피소드: `series/coral-town-daycare/images/episodes/아루와_수아의_반짝_마음조개_new_2026-05-27`
- 인쇄 도구 문서: `tools/print-layout/README.md`

## 검증 메모

- 인쇄 레이아웃 테스트는 어제 중간에 실행이 끊겨 이번 커밋 직전에는 다시 완료하지 못했다.
- 산호마을 에피소드 이미지는 생성 결과를 교체해 반영했지만, 최종 시각 QA는 사용자가 직접 한 번 더 확인하는 것이 좋다.
