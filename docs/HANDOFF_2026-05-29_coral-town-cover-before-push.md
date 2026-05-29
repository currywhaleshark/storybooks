# HANDOFF - 산호마을 표지 제작 후 푸시

작성일: 2026-05-29

## 현재 상태

- 브랜치: `codex/booklet-printing`
- 원격: `origin https://github.com/currywhaleshark/storybooks.git`
- 상태 확인 시점: 원격보다 `ahead 2`
- 현재 워킹트리에는 이 핸드오프 파일 외에도 사용자가 정리한 것으로 보이는 변경이 있다. 다음 세션 시작 시 반드시 `git status --short`로 다시 확인하고, 사용자 변경을 임의로 되돌리지 말 것.
- 최근 커밋:
  - `5cfd974 Merge branch 'codex/booklet-printing' of https://github.com/currywhaleshark/storybooks into codex/booklet-printing`
  - `097c77a Add Sanho waiting batch one assets`
  - `0c8a85e Add print layout run instructions`

주의:

- 아직 푸시하지 말 것. 사용자가 "표지 뽑고 푸시"를 요청했다.
- 표지 생성 후 표지 파일까지 포함해 추가 커밋을 만들고, 그 다음 `origin/codex/booklet-printing`으로 푸시한다.

## 에피소드

시리즈:

`series/coral-town-daycare`

대본:

`series/coral-town-daycare/docs/episodes/아루와_수아의_반짝_마음조개.md`

이미지 폴더:

`series/coral-town-daycare/images/episodes/아루와_수아의_반짝_마음조개_new_2026-05-27`

현재 본문 페이지:

- `01_페이지.png` ~ `12_페이지.png`
- 최근 수정된 페이지: `05`, `07`, `09`, `10`, `11`, `12`
- 사용자 확인: 수정본 통과

참고 후보 폴더:

`series/coral-town-daycare/images/episodes/아루와_수아의_반짝_마음조개_new_2026-05-27/rework_candidates`

사용자가 급한대로 파일 정리했다고 했으므로, 표지 작업 전 `git status --short`와 대상 폴더를 다시 확인할 것. 현재 확인된 추가 변경 후보는 `docs/episode_worklog_2026-05-28_sanho_waiting.md` 및 `series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/work_2026-05-28/batch_1/03_candidate_text_v7*.png` 계열이다.

## 표지 산출물 목표

새 표지 파일을 아래 경로에 저장:

`series/coral-town-daycare/images/episodes/아루와_수아의_반짝_마음조개_new_2026-05-27/00_표지.png`

기존 파일이 이미 있으면 덮어쓰기 전에 반드시 확인하거나 후보 파일로 저장:

`00_표지_candidate_20260529.png`

## 공식 레퍼런스

반드시 실제 이미지 파일을 reference로 사용한다.

- 아루: `series/coral-town-daycare/references/characters/아루.png`
- 수아: `series/coral-town-daycare/references/characters/수아.png`
- 마리 선생님: `series/coral-town-daycare/references/characters/마리_선생님.png`
- 몽글이: `series/coral-town-daycare/references/characters/몽글이.png`
- 놀이터/전경: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- 규칙서: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`

## 표지 핵심 방향

제목:

`아루와 수아의 반짝 마음조개`

표지 장면:

- 산호마을 어린이집 놀이터/조개 놀이 공간.
- 아루와 수아가 중심.
- 아루와 수아 사이 또는 앞쪽에 주황 마음조개와 보라 마음조개가 은은하게 빛남.
- 분위기는 갈등보다 "서로의 마음을 기다리고 존중하는 따뜻한 결말" 쪽.
- 마리 선생님은 작게 배경에서 다정하게 지켜보거나, 표지가 복잡해지면 생략 가능.
- 몽글이는 필요하면 작은 보조 인물로만 사용하고, 중심은 아루와 수아.

아루 불변 조건:

- 3세 가시복/복어 아이.
- 둥글고 통통한 주황빛 복어 몸.
- 작은 가시와 작은 납작한 지느러미.
- 흰색/코랄 세일러 스카프.
- 노란 조개 가방.
- 사람 팔, 손, 소매, 셔츠, 세일러복, 몸통 옷 금지.
- 아루에게 허용되는 착장은 스카프와 노란 조개 가방뿐.

수아 불변 조건:

- 보라빛 해마 아이.
- 파란 세일러복, 민트색 가방.
- 말린 꼬리, 작은 지느러미.
- 조용하지만 표지에서는 편안하고 안심한 표정.

피해야 할 것:

- 아루의 의상/가방 누락.
- 아루에게 사람 팔/손/옷 붙이기.
- 수아 중복 등장.
- 텍스트 오탈자 또는 깨진 한글.
- 너무 반짝이는 조개, 네온톤, 복잡한 소품.

## 권장 프롬프트 골격

```text
Use case: illustration-story
Asset type: Korean preschool picture book cover, landscape 5:4
Primary request: Create the cover for "아루와 수아의 반짝 마음조개" using the official Coral Town Daycare references. Do not use failed previous page candidates as references.

Scene: warm Coral Town Daycare underwater playground, gentle shell play area, soft coral daycare building in background.

Subjects: Aru and Sua are centered. Aru, a round orange pufferfish child, and Sua, a purple seahorse child, look at two small heart shells between them: one warm orange shell for Aru's heart and one soft purple shell for Sua's heart. The shells glow only softly. The feeling is warm, respectful, and calm, about "my heart and my friend's heart are both precious."

ABSOLUTE ARU RULE: Aru is only a round orange pufferfish child with small spikes, small flat fish side fins, tiny tail fin, face, white-and-coral sailor scarf, and yellow shell shoulder bag. No shirt, no sleeves, no sailor outfit, no body clothing, no human arms, no hands. Only scarf and yellow shell bag are allowed and both must be visible.

Sua rule: Sua is one purple seahorse child with blue sailor outfit and mint bag, curled tail, gentle relieved expression.

Text verbatim, large clear Korean cover title:
아루와 수아의 반짝 마음조개

Style: soft Korean preschool picture book, watercolor and colored pencil, warm paper grain, low-saturation pastel, rounded gentle forms.

Composition: cover title at top with clean readable space; Aru and Sua centered below; heart shells visible; not cluttered.

Avoid: missing Aru scarf, missing Aru yellow bag, human arms or hands on Aru, clothing on Aru except scarf and bag, duplicate Sua, garbled Korean, excessive glitter, watermark.
```

## 작업 순서

1. `storybook-episode-production` 및 `imagegen` 스킬 기준을 따른다.
2. 공식 레퍼런스 이미지를 열어 확인한다.
3. 표지 후보를 생성한다.
4. 후보를 프로젝트 폴더에 저장한다.
5. QA:
   - 제목이 정확한가?
   - 아루 스카프와 노란 가방이 보이는가?
   - 아루에게 사람 팔/손/몸통 옷이 붙지 않았는가?
   - 수아가 한 명만 나오는가?
   - 수아 의상/가방이 공식 레퍼런스와 맞는가?
   - 표지 구도가 너무 복잡하지 않은가?
6. 통과 후보를 `00_표지.png`로 저장한다.
7. `git status --short` 확인.
8. 표지 파일과 이 핸드오프 파일을 커밋한다.
9. 사용자에게 `origin https://github.com/currywhaleshark/storybooks.git`로 푸시해도 되는지 명시 승인을 받은 뒤 `git push`한다.

## 남은 일

- 표지 생성.
- 표지 QA.
- 표지 커밋.
- 푸시.
