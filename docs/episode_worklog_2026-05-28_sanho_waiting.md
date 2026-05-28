# Episode Worklog - Sanho Waiting Story

## Purpose

Keep the episode context light enough to continue across sessions without carrying generated images in chat history.

## Source Script

- Script: `C:/Users/yurib/Downloads/sanho_waiting_story_prompts.md`
- Series: `series/coral-town-daycare`
- Episode title: `산호마을 어린이집의 기다림 이야기`
- Subtitle/theme: `기다리는 마음도 자라요`
- Core message: `기다리는 마음도 반짝반짝 빛나는 마음이야`

## Official References

Use these as visual truth. Do not infer character appearance from prose if an image reference exists.

- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Character references:
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
- Background references:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/배경_식당.png`
  - `series/coral-town-daycare/references/배경_교실.png`
  - `series/coral-town-daycare/references/배경_낮잠방.png`
- Integrated character sheet is secondary only:
  - `series/coral-town-daycare/references/산호마을_어린이집_캐릭터_시트.png`

## Output Plan

- Work folder: `series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기_work_2026-05-28`
- Final folder, once approved: `series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기`
- Candidate naming: `00_candidate_v1.png`, `01_candidate_v1.png`, etc.
- Final naming for print tool: `00_표지.png`, `01_페이지.png` through `12_페이지.png`

## Page Plan

| File | Page | Scene | Main refs |
| --- | --- | --- | --- |
| `00_표지.png` | 표지 | Daycare playground cover with Jun, Aru, Lulu, Mongle, Banguli | main four, Banguli, exterior/playground |
| `01_페이지.png` | 1 | Morning arrival at Coral Town Daycare | Mari, Jun, Aru, Lulu, Mongle, Sua, Tori, Popo, Banguli, exterior |
| `02_페이지.png` | 2 | Jun waits for the coral slide | Jun, Popo, Mongle, Banguli, playground |
| `03_페이지.png` | 3 | Jun counts turns and waits calmly | Jun, Popo, Mongle, Banguli, playground |
| `04_페이지.png` | 4 | Aru smells snack and wants to eat first | Aru, Mari, Banguli, dining room |
| `05_페이지.png` | 5 | Snack is better when eaten together | Aru, friends, Mari, Banguli, dining room |
| `06_페이지.png` | 6 | Lulu waits to show teacher her drawing | Lulu, Sua, Mari, Banguli, classroom |
| `07_페이지.png` | 7 | Teacher thanks Lulu for waiting | Lulu, Mari, Sua, Banguli, classroom |
| `08_페이지.png` | 8 | Mongle waits for the drawing to dry | Mongle, Mari, Banguli, art classroom |
| `09_페이지.png` | 9 | Dried drawing shines softly | Mongle, Mari, Banguli, art classroom |
| `10_페이지.png` | 10 | Friends gather and share waiting stories | Mari, Jun, Aru, Lulu, Mongle, Sua, Tori, Popo, Banguli, classroom |
| `11_페이지.png` | 11 | Mari shows the glowing heart-shell | Mari, main four, Banguli, classroom |
| `12_페이지.png` | 12 | Sunset dismissal and warm goodbye | Mari, all children, Banguli, exterior |

## Production Batches

- Batch 1: reference QA, output folder setup, cover + pages 1-3.
- Batch 2: pages 4-7.
- Batch 3: pages 8-12.
- Batch 4: final QA, text panel pass if needed, final folder assembly.

Keep each batch small. Avoid loading all generated images back into the chat. Inspect only the current page candidates or pages that need QA.

## QA Rules

- Character identity must match individual character references first.
- Backgrounds must match official space references and stay light/simple.
- Do not use failed prior episode outputs as visual references unless explicitly approved.
- Banguli should appear subtly across the episode, with expression changes matching the script.
- Keep clean whitespace for storybook text.
- Avoid repeated front-facing full-body compositions.
- Do not overwrite an approved final page unless the replacement is clearly better for the requested issue.

## Current Status

- Script inspected.
- Official character and background reference files found.
- No page images generated for this episode yet.

## Next Session Prompt

```text
C:/Users/yurib/Documents/New project/storybooks 에서 이어서 작업해줘.
먼저 docs/episode_worklog_2026-05-28_sanho_waiting.md 를 읽고,
C:/Users/yurib/Downloads/sanho_waiting_story_prompts.md 대본과
series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md 를 기준으로
산호마을 어린이집의 기다림 이야기 작업을 이어가면 돼.

공식 캐릭터 레퍼런스는 series/coral-town-daycare/references/characters/*.png 이고,
배경 레퍼런스는 series/coral-town-daycare/references/배경_*.png 이야.
이미지 생성은 한 세션에 3-4장 단위로 끊고, 생성 이미지를 대화에 계속 누적하지 말고 파일 경로와 판정만 worklog에 남겨줘.
다음 작업은 Batch 1: 출력 폴더 준비, 표지 + 1-3페이지 생성 계획/프롬프트 확정부터 시작.
```
