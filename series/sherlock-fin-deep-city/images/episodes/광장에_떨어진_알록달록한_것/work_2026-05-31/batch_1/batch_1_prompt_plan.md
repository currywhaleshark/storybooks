# Batch 1 Prompt Plan - 광장에 떨어진 알록달록한 것

## Scope

- Episode: 광장에 떨어진 알록달록한 것
- Batch: umbrella prop reference + cover + pages 1-3
- Work folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1`
- Final folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/final`
- Candidate filenames:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`

## Official References

Use the actual image files as visual truth.

- Characters:
  - `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - `series/sherlock-fin-deep-city/references/characters/펄리.png`
  - `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/모모.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Prop:
  - `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`

## Shared Visual Rules

- A5 portrait page proportion, about `1:1.414`, for all interior pages and cover candidates unless the user asks otherwise.
- Include the approved Korean page text directly in the image from the first page-generation pass.
- Use one clean cream or shell-light text panel with rounded corners, thin border, and generous margins.
- Keep the Sherlock Fin series style: bright warm underwater Deep City, jazz plaza, coral buildings, shell doors, bubble streetlamps, gentle neon, no horror, no dark scary deep-sea mood.
- Character identity must follow the official individual references, not prose alone.
- The umbrella must follow the new prop reference once created: ordinary human-world umbrella, red/yellow/blue/green segmented canopy, thin metal ribs, curved handle, half-open or open as the page requires.
- Do not use failed prior generated episode candidates as visual references.
- Avoid extra signs, random labels, invented letters, speech bubbles outside the approved script, watermarks, or unrelated prior-episode details.

## Prop Reference Prompt

Use case: illustration-story
Asset type: official recurring prop reference sheet
Primary request: Create the official reference image for the colorful umbrella from the episode "광장에 떨어진 알록달록한 것".
Scene/backdrop: simple light neutral background, no full story scene.
Subject: One ordinary human-world umbrella, shown in a clear reference-sheet style. The umbrella has a round canopy divided into bold red, yellow, blue, and green wedge-shaped panels, thin silver-gray metal ribs, a central shaft, and a curved hook handle. Show one main half-open view, one small fully-open top/side view, one small folded silhouette, and a small close-up of the curved handle and ribs.
Style/medium: bright children's picture-book illustration matching the Sherlock Fin series; soft polished watercolor and animation-book finish.
Composition/framing: clean reference sheet, the main half-open umbrella large in the center, smaller views arranged around it with generous spacing.
Lighting/mood: curious, friendly, not mysterious or scary.
Text: no text, no labels, no letters.
Constraints: Make it recognizable as a normal umbrella from the human world, not a jellyfish, mushroom, parasol-only decoration, tent, flower, sea creature, or magical artifact. Keep the colors vivid enough to contrast with Deep City blue backgrounds. Keep the silhouette simple enough to repeat across story pages.
Avoid: no characters, no raindrops, no storm, no sky, no beach, no logo, no writing, no watermark, no photorealism, no 3D plastic toy look.

## Batch 1 Page Generation Notes

Umbrella prop reference created and accepted for page-generation use:

- `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`
- Locked features: red/yellow/blue/green segmented canopy, thin metal ribs, central shaft, blue curved hook handle, ordinary human-world umbrella silhouette, usable half-open/open/folded variants.

For every page prompt, attach or inspect the actual official character references, Deep City reference, layout reference, and umbrella prop reference first.

## Page Prompt Records

### 00 Cover

- Candidate: `00_candidate_text_v1.png`
- Scene prompt: Sherlock Fin and friends gather around the half-open red/yellow/blue/green umbrella in Deep City Jazz Plaza. Keep the umbrella central and ordinary, not magical or creature-like. Use cover-title layout with the title text and series name.
- Required title text:

```text
심해탐정 셜록 핀
광장에 떨어진 알록달록한 것
```

### 01 Page 1

- Candidate: `01_candidate_text_v1.png`
- Scene prompt: Bright morning in Deep City Jazz Plaza. Friends walk into the plaza while a small unknown colorful object rests in the center at a distance. Keep the object mysterious but readable as the episode umbrella for continuity.
- Required story text:

```text
딥시티에
반짝반짝 아침이 왔어요.

친구들이 하나둘
재즈 광장으로 나왔어요.

그런데……
광장 한가운데에
무언가 놓여 있었어요.
```

### 02 Page 2

- Candidate: `02_candidate_text_v1.png`
- Scene prompt: Pearly, PopPop, Momo, and Crabson view the half-open umbrella from a safe distance. Do not include Sherlock Fin. Show the thin ribs, colorful fabric, shaft, and blue hook handle clearly.
- Required story text:

```text
알록달록.
크고 둥근 물건이었어요.

가는 살이 쭉쭉 뻗어 있고,
색색의 천이 펼쳐져 있었어요.

‘우와, 이게 뭐지?’

친구들은 한 번도
본 적이 없었어요.
```

### 03 Page 3

- Candidate: `03_candidate_text_v1.png`
- Scene prompt: Pearly, PopPop, Momo, and Crabson guess what the object might be. Keep the real umbrella centered and unchanged. Put the big jellyfish, table coral, and sea lily only inside soft imagination bubbles. Do not include Sherlock Fin.
- Required story text:

```text
모모가 말했어요.
‘큰 해파리야!’

팝팝이 말했어요.
‘아니야, 테이블산호야!’

펄리가 말했어요.
‘바다나리 같은데?’

모두 다르게 보았어요.

‘정말 뭘까?’
```

## Batch 1 QA Notes

- `00_candidate_text_v1.png`: pass with caution. Strong cover and readable title, but background contains extra jazz signage.
- `01_candidate_text_v1.png`: fail. User QA: Sherlock Fin appears too early; page 1 should not include Sherlock Fin. Momo's back view looks odd.
- `02_candidate_text_v1.png`: pass. User QA: page 2 is OK.
- `03_candidate_text_v1.png`: fail. User QA: PopPop's sunglasses disappeared.

## Regeneration Locks

- Reduce art-style drift: closer to official character sheets, simpler rounded shapes, clean linework, soft watercolor/picture-book finish, less glossy neon density.
- Avoid extra signage, random labels, and pseudo-writing in the background.
- Page 1 v2:
  - No Sherlock Fin anywhere.
  - Friends may be small and distant, but Momo's silhouette must be clear and natural.
  - Morning plaza and far umbrella remain the focus.
- Page 3 v2:
  - PopPop must wear black sunglasses and teal headphones.
  - Keep big jellyfish/table coral/sea lily only inside imagination bubbles.
  - Do not change the real umbrella into those guessed objects.

## 2026-05-31 Page 3 Underwater-Context Correction

- User correction before official Batch 2: the original mushroom/tent/flower guesses do not fit the underwater story world.
- Replace page 3 guesses everywhere with:
  - Momo: `큰 해파리`
  - PopPop: `테이블산호`
  - Pearly: `바다나리`
- Existing `03_candidate_text_v1.png` and `03_candidate_text_v2.png` are superseded for story-content reasons even if their character/accessory QA passed.
- Next valid page 3 candidate should be generated as `03_candidate_text_v3.png` using the corrected guesses and the existing PopPop sunglasses/headphones lock.
