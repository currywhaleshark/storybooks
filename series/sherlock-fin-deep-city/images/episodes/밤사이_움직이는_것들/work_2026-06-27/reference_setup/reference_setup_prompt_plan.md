# 밤사이 움직이는 것들 - 문틈 레퍼런스 프롬프트 계획

## 목적

본편 생성 전 조개 문, 헐거운 경첩, 문 아래 아주 작은 틈, 약한 밤 물살, 움직이는 가벼운 물건/그대로인 무거운 물건의 구분을 한 장의 공식 보조 레퍼런스로 고정한다.

## 출력 후보

- 후보 저장 위치: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v1.png`
- 공식 레퍼런스 승격 위치: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`

## 실제 이미지 입력

생성 직전 아래 파일들을 `nodeRepl.emitImage`로 대화 컨텍스트에 방출한다. 프롬프트의 로컬 경로 텍스트만으로 참조하지 않는다.

- 탐정 사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 딥시티 공통: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`

## 고정 규칙

- 기존 탐정 사무소 내부의 따뜻한 물방울 램프, 조개 책장, 추리 칠판, 서류 책상, 네온 심해 사무소 톤을 유지한다.
- 문은 사무소 한쪽의 조개 문이다. 둥근 조개껍데기 판, 부드러운 산호 프레임, 작은 문고리와 잠금쇠가 있다.
- 문고리와 잠금쇠는 멀쩡하다. 억지로 열린 흔적, 부서진 흔적, 큰 구멍은 금지한다.
- 문제는 아래쪽 경첩이 살짝 헐거워진 것뿐이다.
- 문 아래 틈은 아주 작다. 작은 물살과 종이/깃털 펜은 밀 수 있지만, 캐릭터나 생물이 들어올 수 있는 크기가 아니다.
- 밤 물살은 부드럽고 약한 푸른 곡선, 작은 거품, `솔솔`/`사르르` 분위기다. 무섭거나 거센 파도처럼 보이면 안 된다.
- 움직일 수 있는 것: 종이, 작은 카드, 깃털 펜, 얇은 메모지.
- 움직이지 않는 것: 노란 돋보기, 두꺼운 책, 작은 잉크병, 책상.
- 이동 방향은 문 아래 틈에서 책상 쪽이다.

## 생성 프롬프트

```text
Use case: illustration-story
Asset type: official reference design sheet for a children's storybook episode
Primary request: Create a single reusable reference sheet for Sherlock Fin's detective office shell door problem in the episode "밤사이 움직이는 것들".
Input images: Image 1 is the official detective office interior reference and must define the room style, warm lighting, furniture language, and underwater office mood. Image 2 is Sherlock Fin's official character reference for scale and optional small inset only. Image 3 is the Deep City style reference for palette and background language.
Scene/backdrop: A cozy underwater detective office in Deep City, matching the official office reference: warm bubble lamp glow, shell bookshelf, clue board, paper desk, coral/shell decoration, neon deep-sea colors.
Subject: A shell-shaped office door with a tiny new gap at the bottom caused by one slightly loose lower hinge. The door still looks closed; the handle and latch are intact.
Style/medium: bright warm children's picture book illustration, polished reference sheet, same visual language as the official Sherlock Fin series.
Composition/framing: one sheet with clear labeled visual panels but no text labels needed in the image; include: full office corner with the shell door, close-up of the bottom hinge and tiny gap, inset showing soft night current slipping through the tiny gap, comparison of light items that can move versus heavy items that stay put, and a direction cue from door gap toward the desk.
Lighting/mood: cozy, safe, curious, never scary; night-current inset uses deep blue with warm lamp light still visible.
Color palette: deep blue, purple, emerald, pink, warm gold lamp light, cream shell highlights.
Constraints: the gap must be very small; the current must be gentle; the door must not look broken open; no intruder, no creature hiding behind the door, no horror, no flooding, no storm wave. Keep the office consistent with the official office reference. Make the shell door and lower hinge easy to reuse in later page prompts.
Avoid: scary dark room, giant hole, cracked destroyed door, harsh realistic water damage, big wave, violent current, suspicious silhouette, random extra characters, illegible decorative text, changing Sherlock Fin's design if he appears.
```

## QA 기준

- 사무소가 기존 탐정 사무소 레퍼런스와 같은 공간으로 읽히는가?
- 조개 문과 문 아래 틈이 한눈에 보이지만 과장되지 않았는가?
- 문이 닫혀 있고 잠금쇠가 그대로라는 단서가 유지되는가?
- 물살이 약해서 가벼운 물건만 밀 수 있다는 논리가 보이는가?
- 문 아래 틈에서 책상 쪽으로 방향성이 보이는가?
- 무서운 침입자/공포 분위기/침수 사고처럼 보이지 않는가?
