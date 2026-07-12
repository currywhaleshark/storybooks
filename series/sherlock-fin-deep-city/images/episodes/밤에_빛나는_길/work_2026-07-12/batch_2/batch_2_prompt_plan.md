# 밤에 빛나는 길 - Batch 2 Prompt Plan

## Status

- Scope: story pages `04`-`07` only.
- Batch 1 gate: complete; user-approved final pages `00`-`03` are registered.
- Candidate folder: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/work_2026-07-12/batch_2/`
- Generation, local QA, and user QA complete. Pages `04`-`07` are promoted to stable final filenames.
- Built-in image generation mode, one call per page.

## Official and Approved References

- Sherlock Fin: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Deep City: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Golden trail and moss flakes: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Text layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Approved night-alley continuity: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/01_페이지.png`
- Approved morning-alley continuity: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final/02_페이지.png`

## Shared Batch Locks

- Format: A5 portrait `148:210`; production target `1054 x 1492`; never landscape.
- Use original official sheets for character identity. Approved pages `01` and `02` may be used only for the established alley landmarks and night/morning memory continuity.
- Do not attach or imitate rejected Batch 1 candidates.
- Cozy night palette: deep navy/violet water, warm windows, bubble lamps, coral, and soft gold glow; never frightening darkness.
- The trail stays on the alley floor, follows bends, and consists of tiny gold plankton lights around small distinct green moss flakes. It never floats as a ribbon in midwater.
- No grandfather, long-legged silhouette, crab body, cane, scarf, glasses, or mossy carapace appears anywhere in pages `04`-`07`. The deduction must precede the reveal on page `08`.
- Sherlock matches the official sheet: teal hair, brown deerstalker with official ornament, brown detective coat, teal tail, black gloves, and yellow-gold magnifier. No substitute hat ornament or unrelated tool.
- Pearly matches the official sheet and approved anatomy: high fully rounded cream head, full forehead/rear skull, visible small torso, exactly two shoulder-connected short arms and two hands whenever her upper body is visible, centered black bow tie, planned gold monocle and chain, exactly one upper shell valve and one lower bowl sharing one hinge axis. No flattened head, floating head, missing arms, hat, bonnet, extra inner shell, or twisted valves.
- Text is rendered directly in a large cream shell-light rounded panel with generous padding. Every Korean character, space, line break, punctuation mark, quote, and middle dot must match the script verbatim.
- No prior-episode object, extra character, readable sign, pseudo-writing, watermark, or unrelated clue.

## 04 - First Clue: Position and Direction

- Raw candidate: `04_candidate_text_v1_raw.png`
- Normalized candidate: `04_candidate_text_v1.png`
- References: Sherlock official, Pearly official, golden-trail official, text-layout official, approved page `01` alley continuity.
- Scene lock: slightly elevated nighttime wide view. The ground-hugging trail visibly bends around the same pink-left/teal-right coral alley established on page `01`. Sherlock points along the trail's direction without touching it. Pearly watches beside him. No subject is visible at the end of the trail.
- Layout: illustration occupies left/lower and central route; tall cream text panel occupies upper/right approximately 46-50% of the page while preserving the path's bends.

### Page 04 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the approved golden-plankton trail and moss-flake reference. Image 4 is the official text-panel layout reference. Image 5 is the user-approved page 01, used only for the same night-alley landmarks and color continuity. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy midnight Deep City coral alley in a slightly elevated wide view. Repeat the recognizable S-bend, pink fan-coral building on the left, teal shell-door house on the right, pale shell paving, warm windows, and bubble lamps from Image 5. A granular gold plankton trail with small green moss flakes stays LOW ON THE PAVING and bends around the corner.
Subject: Sherlock Fin and Pearly stand safely beside the trail. Sherlock matches Image 1 and points one gloved hand along the route without touching the lights. Pearly matches Image 2 with round head, visible torso, two connected arms/hands, bow tie, monocle/chain, and coherent two-valve clam. Both study the trail; no one stands on it.
Composition/framing: A5 portrait 148:210. Show the full bent route clearly from above-left toward the distance. Keep characters in the left/lower illustration zone. Place a tall cream shell-light rounded text panel in the upper/right 46-50% with generous padding and readable line spacing.
Style/medium: polished warm 3-year-old picture-book illustration; cozy neon-jazz underwater mystery; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"그날 밤,
셜록 핀과 펄리는
골목으로 나갔어요.

정말이었어요!

금빛 길이
은은하게 빛나고 있었어요.

셜록 핀이 말했어요.

“먼저 잘 보자.

빛이 물속에 떠 있지 않아.
골목 바닥을 따라
굽이굽이 이어지고 있어.

누군가 이 길을 따라
움직인 자취야.

첫 번째 단서!”"
Constraints: Trail is granular and ground-hugging, never a floating ribbon. Sherlock points along it without touching. Preserve official character identity and Pearly's full anatomy. Absolutely no grandfather, crab silhouette, cane, scarf, glasses, extra character, extra text, readable sign, watermark, unrelated prop, or prior-episode clue. Never landscape.
```

## 05 - Second Clue: Time

- Raw candidate: `05_candidate_text_v1_raw.png`
- Normalized candidate: `05_candidate_text_v1.png`
- References: Sherlock official, Pearly official, text-layout official, approved page `01` night alley, approved page `02` morning alley.
- Scene lock: current setting is night. Sherlock asks Pearly about timing. Two separate memory bubbles above/right show (1) the approved late-night glowing trail and (2) the approved bright morning alley with no present trail. Do not blend the bubbles.
- Layout: tall cream text panel on left approximately 46-50%; Sherlock/Pearly medium shot lower-right; two memory bubbles upper-right.

### Page 05 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the official text-panel layout reference. Image 4 is the user-approved page 01 night-alley continuity reference. Image 5 is the user-approved page 02 morning-alley continuity reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: current scene is a cozy Deep City alley at night. Sherlock and Pearly converse beside the low gold trail. Above them are TWO clearly separate rounded memory bubbles: the first shows the late-night alley with the glowing trail from Image 4; the second shows the bright morning version from Image 5 with NO trail and NO green flakes.
Subject: Sherlock matches Image 1, listening and nodding. Pearly matches Image 2 and answers him, with high round head, visible torso, two connected arms and two hands, black bow tie, official gold monocle/chain, and coherent hinged shell. Their expressions are calm, thoughtful, and child-friendly.
Composition/framing: A5 portrait 148:210. Tall cream shell-light text panel on the left 46-50%. Character conversation occupies lower-right. The two memory bubbles sit upper-right and remain easy to compare without covering faces.
Style/medium: polished warm 3-year-old picture-book illustration; cozy neon-jazz underwater mystery; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"이번에는 잘 들어 보자.

“펄리, 빛은 언제 나타났어?”

펄리가 대답했어요.

“밤늦은 시간에요.
늘 비슷한 때였어요.

그리고 아침이면
사라져 있었어요.”

셜록 핀이 고개를 끄덕였어요.

“밤마다 비슷한 시간에
되풀이되는 일이구나.

그리고 이 빛은
오래 남아 있지 않아.

두 번째 단서!”"
Constraints: Current scene remains night. Night and morning memory bubbles are separate and unmistakable; morning bubble has zero gold trail and zero moss flakes. Preserve official characters and complete Pearly anatomy. No grandfather, silhouette, crab, extra character, extra text, readable sign, watermark, or unrelated clue. Never landscape.
```

## 06 - Third Clue: Plankton and Moss

- Raw candidate: `06_candidate_text_v1_raw.png`
- Normalized candidate: `06_candidate_text_v1.png`
- References: Sherlock official, Pearly official, golden-trail official, text-layout official, Deep City official.
- Scene lock: extreme clue close-up dominated by Sherlock's yellow magnifier. Inside the lens, many individual gold plankton specks gather around distinct small soft green moss fragments. Plankton are a faceless swarm, not mascot characters. Pearly observes from the side with complete readable anatomy.
- Layout: large cream panel across upper 42-46%; magnifier macro fills lower center; Sherlock and Pearly frame it without covering the evidence.

### Page 06 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book clue close-up
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the approved golden-plankton trail and green-moss-flake macro reference. Image 4 is the official text-panel layout reference. Image 5 is the official Deep City environment/style reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy night alley floor seen very close. Sherlock's yellow-gold magnifier dominates the lower-center. Through its lens, show dozens of tiny gold plankton lights clustering around several distinct soft green moss fragments. The child can clearly distinguish gold plankton from green moss. Outside the lens, the same evidence continues at normal scale on the paving.
Subject: Sherlock matches Image 1 and holds the magnifier safely without covering the evidence. Pearly matches Image 2 beside him with round head, visible torso, two connected arms/hands, bow tie, gold monocle/chain, and coherent shell, watching with curious wide eyes.
Composition/framing: A5 portrait 148:210. Cream shell-light text panel spans the upper 42-46% with generous padding. Magnifier macro is the lower visual lead; Sherlock and Pearly frame it at the lower sides.
Style/medium: polished warm 3-year-old picture-book illustration; educational clue close-up within cozy neon-jazz fantasy; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"이번에는
아주 가까이서 보았어요.

셜록 핀이 돋보기를 들고
빛나는 길을 들여다보았어요.

“어라!”

길이 빛나는 게 아니었어요.

작은 야광 플랑크톤들이
모여 반짝이고 있었지요.

그 사이에는
초록 이끼 가루도
조금씩 섞여 있었어요.

“플랑크톤들이
이끼 가루 주변에 모였어.

세 번째 단서!”"
Constraints: Gold plankton remain a faceless granular swarm; no eyes or mascot bodies. Green moss fragments are small but clearly distinguishable, not giant tiles and not invisible dust. Magnifier does not hide the clue. Preserve official characters and complete Pearly anatomy. No grandfather, silhouette, crab, extra character, extra text, pseudo-writing, watermark, or unrelated clue. Never landscape.
```

## 07 - Deduction Before Reveal

- Raw candidate: `07_candidate_text_v1_raw.png`
- Normalized candidate: `07_candidate_text_v1.png`
- References: Sherlock official, Pearly official, Deep City official, golden-trail official, text-layout official.
- Scene lock: Sherlock combines three visual clues before the reveal. Three clear thought-bubble cells show (1) floor-hugging bent trail, (2) night trail versus empty morning, and (3) gold plankton around green moss flakes. No grandfather or silhouette anywhere.
- Layout: Sherlock/Pearly medium shot lower-left; clue bubbles upper/left or center; tall cream text panel right approximately 48-52%.

### Page 07 Prompt

```text
Use case: illustration-story
Asset type: new A5 portrait Korean children's picture-book deduction page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity/anatomy sheet. Image 3 is the official Deep City environment/style reference. Image 4 is the approved golden-plankton trail and moss-flake reference. Image 5 is the official text-panel layout reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy nighttime Deep City alley. Sherlock explains while Pearly listens brightly. Above/behind Sherlock are THREE distinct connected thought-bubble cells with visual clues only: Cell 1, a ground-hugging trail bending along alley paving; Cell 2, a simple split night-with-trail versus morning-without-trail comparison; Cell 3, gold plankton specks clustered around small green moss flakes. Do not show the cause or any character inside the clues.
Subject: Sherlock matches Image 1 and gathers the three clues with a thoughtful pointing/counting gesture. Pearly matches Image 2 with high round head, visible torso, two connected arms and hands, bow tie, official monocle/chain, coherent shell, and sparkling understanding expression.
Composition/framing: A5 portrait 148:210. Sherlock and Pearly occupy lower-left/center. Three clue bubbles remain readable above them. Tall cream shell-light text panel occupies the right 48-52% with generous padding.
Style/medium: polished warm 3-year-old picture-book illustration; cozy neon-jazz underwater deduction scene; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"셜록 핀은 단서를
하나로 모았어요.

빛은 골목길을 따라 이어졌어요.
밤마다 비슷한 시간에 나타났어요.
플랑크톤 사이에는
초록 이끼 가루가 있었어요.

“아, 그런 이유가 있었구나!

밤마다 이 길을 지나며
이끼 가루를 떨어뜨리는
친구가 있어.

플랑크톤들은
그 가루를 좋아해서
뒤를 따라 빛나는 거야.

빛의 길이 이어지는 곳에
그 친구가 있을 거야!”"
Constraints: Absolutely no grandfather, long-legged silhouette, crab body, cane, scarf, glasses, or mossy carapace. Deduction occurs before reveal. Thought bubbles contain only the three clue visuals and no text. Preserve official characters and complete Pearly anatomy. No extra character, extra text, readable sign, watermark, or prior-episode clue. Never landscape.
```

## Generation Results

- `04_candidate_text_v1_raw.png` / `04_candidate_text_v1.png` — `1054 x 1492`, SHA-256 `C77846E8DD401585AAF75AB5CD5486A7FEB592E2CDDD7BFF461277B41EBEAB75`. LOCAL QA PASS: exact text; elevated bent route; ground-hugging trail; Sherlock points without touching; complete Pearly anatomy; no reveal.
- `05_candidate_text_v1_raw.png` / `05_candidate_text_v1.png` — `1054 x 1492`, SHA-256 `5BB242D6A62A07418C80B089F4E5CBE3222BCDCF1A5B1FAC9B2022ED6925E9DD`. LOCAL QA PASS: exact text; current night scene; two separate night/morning memory bubbles; morning has no trail; official characters pass.
- `06_candidate_text_v1_raw.png` / `06_candidate_text_v1.png` — `1054 x 1492`, SHA-256 `C524C9707B930E6EEE059ED0382C6A2F967C5779B8EF4679E554DF0F2FE521CE`. LOCAL QA PASS: exact text; magnifier-led clue macro; faceless gold specks and distinct green fragments; complete characters; no reveal.
- `07_candidate_text_v1_raw.png` / `07_candidate_text_v1.png` — `1054 x 1492`, SHA-256 `28C9FA4A66C787A60E470308CF21A39142111F09C36F43EC1A2892C87A8C8B78`. LOCAL QA PASS: exact text; exactly three clue cells; official characters; no grandfather or silhouette.

## QA Gate

- [x] All four pages are A5 portrait and normalized to `1054 x 1492` without stretching or clipping required content.
- [x] Every page contains exact script text with correct Korean glyphs, spaces, punctuation, quotes, and line breaks.
- [x] Sherlock and Pearly match official sheets; Pearly retains round head, visible torso, two arms/hands, monocle, and coherent shell.
- [x] Page `04` trail stays on the floor and follows the established alley bend.
- [x] Page `05` has two separate night/morning bubbles; morning contains no trail.
- [x] Page `06` clearly distinguishes faceless gold plankton from green moss fragments.
- [x] Page `07` combines exactly three clue visuals without revealing the grandfather or any silhouette.
- [x] No prior-episode contamination, extra character, extra text, readable sign, pseudo-writing, or watermark.
- [x] User approval for pages `04`-`07`; promoted to `final/04_페이지.png` through `final/07_페이지.png`.
