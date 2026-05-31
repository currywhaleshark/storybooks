# Batch 2 Prompt Plan - 광장에 떨어진 알록달록한 것

## Scope

- Episode: 광장에 떨어진 알록달록한 것
- Batch: pages 4-7
- Work folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_2`
- Candidate filenames:
  - `04_candidate_text_v1.png`
  - `05_candidate_text_v1.png`
  - `06_candidate_text_v1.png`
  - `07_candidate_text_v1.png`

## Official References

- Sherlock Fin: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Friends:
  - `series/sherlock-fin-deep-city/references/characters/펄리.png`
  - `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/모모.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Prop: `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`

## Shared Locks

- A5 portrait page proportion.
- Render the exact Korean story text in a cream rounded text panel with a thin warm dashed border.
- Sherlock Fin must match the official reference: teal-haired young mermaid detective, brown detective hat and coat, yellow magnifying glass, teal tail.
- The umbrella must stay an ordinary red/yellow/blue/green human-world umbrella with thin metal ribs and blue curved hook handle.
- Keep the plaza bright, warm, and non-scary.
- Avoid random signage, watermark, decorative pseudo-writing, and unrelated prior-episode details.

## Page Prompt Records

### 04 Page 4

- Scene prompt: Sherlock Fin arrives in the plaza and stands beside the umbrella. He adjusts his detective hat and pulls out his magnifying glass while the friends gather around him. Side-view medium shot, umbrella clear at center, text panel lower-right.
- Required story text:

```text
그때 셜록 핀이 왔어요.

‘다 같이 짐작만 하지 말고,
하나씩 잘 살펴보자!’

셜록 핀이 돋보기를 꺼냈어요.

‘먼저 잘 보는 거야.’
```

### 05 Page 5

- Scene prompt: Close-up clue shot of the umbrella's curved handle. Sherlock Fin examines the handle through his yellow magnifying glass and gently holds it. The magnifying glass enlarges the blue hook handle and metal shaft. Text panel upper area.
- Required story text:

```text
먼저 여기를 봐.

한쪽 끝에
구부러진 손잡이가 있어요.

셜록 핀이 살짝 잡아 보았어요.

’딱 잡기 좋은 모양이야.

이건······
손에 들고 다니는 물건이구나!’

첫 번째 단서를 찾았어요.
```

### 06 Page 6

- Scene prompt: Sherlock Fin gently pushes the umbrella ribs so the fabric folds and opens again. Show the motion clearly with a folded ghosted position and opened position in one scene. Friends watch with delighted surprise. Text panel lower-left.
- Required story text:

```text
이번에는 살을 살짝 밀어 보았어요.

스르륵—

천이 접혔다가
다시 펴졌어요!

‘오오!’

’접었다 폈다 할 수 있구나.

안 쓸 때는
작게 접어두는 물건이야!’

두 번째 단서를 찾았어요.
```

### 07 Page 7

- Scene prompt: Special under-umbrella view. Sherlock Fin and friends stand under the fully opened umbrella and look upward. The colorful canopy fills the top of the page like a roof, with ribs visible overhead. Their faces show discovery and delight. Text panel lower area.
- Required story text:

```text
이번에는 활짝 펴고
그 아래로 들어가 보았어요.

위를 올려다보니······

둥근 천이
지붕처럼 위를 막아주었어요!

’아! 위를 막아주는 물건이야.

위에서 무언가 내려오는 걸
막아주는 거구나!’

세 번째 단서를 찾았어요.
```

## Batch 2 QA Notes

- `04_candidate_text_v1.png`: pass. Sherlock Fin first arrival, umbrella, friends, and text are aligned with the script.
- `05_candidate_text_v1.png`: pass with text caution. Handle clue and magnifying glass are strong; ellipsis glyphs are not exact.
- `06_candidate_text_v1.png`: pass with text caution. Folding/opening action is clear; dash and quote glyphs are not exact.
- `07_candidate_text_v1.png`: pass with text caution. Special under-umbrella view works; ellipsis and quote glyphs are not exact.

For final production, either accept these as storybook candidates or perform a deterministic text-panel cleanup pass for exact punctuation.
