# 밤사이 움직이는 것들 - 레퍼런스 준비 계획

## 목적

이번 에피소드는 대부분 탐정 사무소 내부에서 진행된다. 기존 사무소 내부 레퍼런스를 사용하되, 반복 등장하는 조개 문과 문 아래 틈, 밤 물살, 가벼운 물건 이동 방향이 페이지마다 흔들리지 않도록 본편 생성 전 고정 조건을 정리한다.

## 사용할 공식 레퍼런스

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 딥시티 공통: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- 탐정 사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- 텍스트박스: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## 고정해야 할 반복 요소

- 탐정 사무소는 따뜻한 물방울 램프, 추리 칠판, 조개 책장, 서류가 놓인 책상, 작은 카드, 얇은 메모지, 깃털 펜, 조개 문이 있는 아늑한 공간이다.
- 조개 문은 사무소 한쪽에 반복 등장한다. 문고리와 잠금쇠는 멀쩡하지만, 아래쪽 경첩이 헐거워져 문 아래에 아주 작은 틈이 생긴다.
- 문틈은 처음부터 너무 크게 보이면 안 된다. 표지와 02-03에서는 암시 수준, 06에서는 돋보기 확대를 통해 명확히 보인다.
- 밤 물살은 공포스럽지 않은 부드러운 푸른 물결과 작은 거품이다. 의성어 분위기는 `솔솔-`, `사르르-`이다.
- 움직이는 물건은 종이, 작은 카드, 깃털 펜, 얇은 메모지다.
- 움직이지 않는 물건은 노란 돋보기, 두꺼운 책, 작은 잉크병, 책상이다.
- 이동 방향은 문 아래 틈에서 책상 쪽이다. 페이지 05와 07의 추리 카드에서 같은 방향성이 유지되어야 한다.

## 선제작 레퍼런스 권장 여부

전용 레퍼런스 없이도 본편 생성은 가능하지만, 사용자 판단에 따라 문/문틈 흔들림 위험이 크므로 먼저 생성했다. 다음 요소는 `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`를 기준으로 고정한다.

- 페이지마다 조개 문 위치와 모양이 크게 달라지는 경우
- 문틈이 너무 크거나 위험한 고장처럼 보이는 경우
- 밤 물살이 무섭거나 폭풍처럼 보이는 경우
- 움직인 물건과 그대로인 물건의 구분이 반복해서 흐려지는 경우

## 전용 레퍼런스 생성 프롬프트 메모

생성한다면 한 장의 장소/소품 통합 디자인 시트로 만든다.

- 제목: `밤사이 움직이는 것들 - 탐정 사무소 문틈 레퍼런스`
- 구성: 사무소 내부 전체, 조개 문 클로즈업, 문 아래 작은 틈 확대, 헐거운 경첩, 밤 물살이 부드럽게 들어오는 인서트, 움직이는 가벼운 물건/그대로인 무거운 물건 비교
- 톤: 밝고 따뜻한 아동용 그림책, 무섭지 않은 심해 사무소, 깊은 파랑/보라에 따뜻한 골드 램프빛
- 금지: 공포 분위기, 크게 부서진 문, 거센 파도, 침수, 위험한 밤 장면, 누군가 숨어 있는 듯한 연출

## 현재 결정

- 이번 준비 단계에서 문틈/밤 물살 레퍼런스 v1을 생성했다.
- 생성 방식은 로컬 경로 텍스트만 쓰는 방식이 아니라, 공식 사무소 내부/셜록 핀/딥시티 레퍼런스를 `nodeRepl.emitImage`로 실제 방출한 뒤 이미지 생성했다.
- 후보: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v1.png`
- 공식 참조 복사본: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- 다음 본편 생성에서는 이 문틈 레퍼런스 파일도 실제 이미지 입력으로 방출한다.

## Node-Emitted Reference Result - 2026-06-27

- Decision update: the door/gap reference was needed because the shell door and tiny gap may drift across pages.
- Generation method: official office interior, Sherlock Fin, and Deep City reference PNGs were emitted into conversation context with `nodeRepl.emitImage` before image generation. Local path text alone was not used as the visual reference.
- Candidate: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v1.png`
- Official reference copy: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- Downstream rule: before any page generation involving the door, gap, hinge, night current, or moved office papers, emit this new reference with `nodeRepl.emitImage`.

## Reference QA Update - 문틈/밤 물살 v2 승인 - 2026-06-27

- User identified v1 failure: the current read like music entering the room, not water current.
- User marked the physically correct gap location on the office door: lower-right closing edge of the shell door, not the center bottom and not the hinge side.
- Regenerated v2 after node-emitting only:
  - official detective office interior reference
  - user annotated correction image with the red circle marking the correct gap location
- Deliberately did not emit the Deep City/jazz reference for v2 to avoid music-note contamination.
- Saved v2 candidate: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v2.png`
- Replaced official reference copy with v2: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- v2 dimensions: 1536x1024.
- v2 SHA256: `12C71646516BA6BB88554D35A93C1D34EB1D619E2E99FD738C9061118F23C669`
- v1 status: rejected/hold for music contamination and wrong gap placement. Keep only as history.
- v2 status: user approved for moving to the next step.
- New global lock: show actual water current only as translucent blue water ribbons, ripples, and small bubbles. No music notes, staff lines, sound-wave graphics, saxophone shapes, neon music icons, or decorative audio symbols.
- New door lock: the gap belongs at the lower-right closing edge of the door leaf where it meets the frame/floor area.
