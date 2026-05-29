# HANDOFF - Sanho Waiting Story Batch 1

작성일: 2026-05-29

## Current Branch

`codex/booklet-printing`

Start the next session with:

```powershell
git status --short --branch
```

Do not revert user or prior-session changes.

## Main Worklog

Read this first:

`docs/episode_worklog_2026-05-28_sanho_waiting.md`

Script:

`C:/Users/USER/Downloads/sanho_waiting_story_prompts.md`

Series rulebook:

`series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`

## Episode

Title:

`산호마을 어린이집의 기다림 이야기`

Theme:

`기다리는 마음도 자라요`

Core message:

`기다리는 마음도 반짝반짝 빛나는 마음이야`

Work folder:

`series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/work_2026-05-28/batch_1`

Final folder:

`series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/final`

## Official References

Use actual image files as visual truth. Do not rely on prose alone.

Characters:

- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`

Backgrounds:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/배경_식당.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/references/배경_낮잠방.png`

Prop:

- `series/coral-town-daycare/references/props/산호_미끄럼틀_레퍼런스.png`

Coral slide locked features:

- orange-pink coral frame
- blue chute descending on left/front side
- green-blue stairs on right
- yellow handrail
- no landing mat
- sandy playground floor with shell stepping stones
- waiting spot separated from chute/landing path

## Batch 1 Candidate Status

Current best candidates:

- `00_candidate_text_v2.png` - cover, user approved
- `01_candidate_text_v2.png` - page 1 candidate, needs final text proof/user visual approval
- `02_candidate_text_v5.png` - page 2 improved safety candidate, needs final text proof/user visual approval
- `03_candidate_text_v8.png` - page 3 best current candidate, needs user visual approval

Important rejected/hold candidates:

- Do not use `02_candidate_text_v2.png` or `03_candidate_text_v2.png`; failed safety/prompt-following QA.
- `02_candidate_text_v4.png` introduced unwanted extra sign/text.
- `03_candidate_text_v7.png` improved slide consistency but did not show the actual sliding moment strongly enough.

## Page 3 Latest Direction

User corrected page 3 design:

- Page 3 should be a two-panel page.
- Top panel: 준이 calms himself and counts `한 번, 두 번, 세 번` beside the safe stair/waiting area.
- Bottom panel: 준이 joyfully rides the coral slide with `슝—`.
- This fixes the mismatch between the counting scene and the script line `준이가 미끄럼틀을 탔어요.`

Generated current best:

`series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/work_2026-05-28/batch_1/03_candidate_text_v8.png`

QA:

- A5-ish, `1054x1492`
- text appears once in a single left panel
- top panel shows counting
- bottom panel shows sliding
- no bags or art tools
- coral slide is consistent across panels
- 포포 is closer to reference with eyes hidden under bell

## Character Locks From User

아루:

- baby pufferfish body only
- scarf/bag only
- no human arms, legs, hands, sleeves, shoes, or full body clothing

포포:

- unless explicitly requested otherwise, eyes should be hidden like the official moon jellyfish reference
- express mostly with small mouth
- must not become 방울이/droplet-like

Outdoor pages 2-3:

- no bags/backpacks/shoulder straps
- no art tools
- no child waiting in chute, exit, or landing path
- landing zone should be visibly empty
- no landing mat

## Prompt Plan Updated

Updated file:

`series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/work_2026-05-28/batch_1/batch_1_prompt_plan.md`

The `03 Page Prompt` now includes:

- two stacked panels
- single story text panel
- coral slide prop reference
- 포포 hidden-eye rule
- no bags/art tools for outdoor play

## Next Step

Do not start Batch 2 yet unless user confirms Batch 1 is accepted.

Recommended next session flow:

1. Open `03_candidate_text_v8.png` for user visual approval.
2. Open/check `00_candidate_text_v2.png`, `01_candidate_text_v2.png`, and `02_candidate_text_v5.png`.
3. If user approves Batch 1 candidates, copy approved files into `final` using:
   - `00_표지.png`
   - `01_페이지.png`
   - `02_페이지.png`
   - `03_페이지.png`
4. Only then move to Batch 2 pages 4-7.

## Generation Rule

Keep generation batches small: 3-4 images max per session. Do not load all generated images into chat history. Record only file paths and QA judgment in the worklog.
