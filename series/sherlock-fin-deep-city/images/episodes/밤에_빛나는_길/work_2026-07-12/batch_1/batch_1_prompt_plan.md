# 밤에 빛나는 길 - Batch 1 Prompt Plan

## Status

- Scope: cover `00` and story pages `01`-`03` only.
- Reference gate: complete. Grandfather v5 and the golden-trail effect are user-approved official references.
- Candidate folder: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/work_2026-07-12/batch_1/`
- User QA: **BATCH 1 APPROVED AND PROMOTED**. Cover `00` v3, page `01` v4, page `02` v1, and page `03` v1 are final. Page `01` v3 remains rejected for missing torso and arms.
- Final outputs: `final/00_표지.png` through `final/03_페이지.png`; all are `1054 x 1492`.
- Built-in image generation mode, one call per page.

## Official References

- Sherlock Fin: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Pearly: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- User-approved long-legged spider-crab grandfather v5: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Deep City: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Golden plankton trail and green moss flakes: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Text-panel layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Detective-office interior: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`

## Shared Locks

- **Format lock: A5 portrait, 148:210 ratio; production target `1054 x 1492`. Never landscape.**
- Built-in output may arrive at a nearby portrait ratio. Preserve it as `_raw.png`, then normalize to `1054 x 1492` without stretching; keep all text, faces, and clues inside a generous central safe area.
- Warm softly painted children's picture-book illustration matching the official Sherlock Fin sheets. No photorealism or glossy 3D toy rendering.
- Night scenes are cozy rather than dark: deep navy/violet, warm windows, bubble lamps, pink/teal coral, and soft golden glow.
- The golden path hugs the alley floor and remains granular: many tiny warm-gold plankton lights around much smaller soft green moss flakes. No solid yellow road, ribbon, liquid, footprints, laser, or floating beam.
- In wide views, green flakes are much smaller than the macro reference and never look like large seaweed tiles.
- Cream or shell-light rounded text panels with a thin understated border and generous padding. Keep panel styling consistent across `01`-`03`.
- Render only the exact Korean text specified for each page. Preserve punctuation, quotation marks, spacing, and line breaks. No paraphrase, pseudo-writing, decorative letters, random signs, or watermark.
- Do not let panels cover faces, the golden path, Pearly's shell, Sherlock's magnifier, or the memory bubbles.
- Sherlock and Pearly must match their official individual sheets exactly. Do not infer their appearance from prose.
- Grandfather v5 is attached on cover `00` only to lock the long-leg silhouette. Do not reveal his shell, face, scarf, glasses, cane, moss, or identity before page `08`.
- No unrelated character, prop, clue, footprint, necklace, star marker, or content from prior episodes.

## Page 01-02 Alley Continuity Anchor

Use the same recognizable bend and landmarks on both pages:

- One smooth S-curving cobalt cobblestone alley.
- A pink fan-coral building/arch on the left side of the bend.
- A teal shell-door home with one round amber window on the right side.
- Two bubble-globe lamps placed at the bend.
- A small pale shell-shaped paving inlay near the middle foreground.
- Page `01`: these landmarks appear through Pearly's window at night with the gold trail.
- Page `02`: the same landmarks are seen outside in bright aqua morning with no present-day trail.

## 00 - Cover

- Raw candidate: `00_candidate_text_v1_raw.png`
- Normalized candidate: `00_candidate_text_v1.png`
- References: Sherlock Fin, Pearly, grandfather v5 for silhouette only, Deep City, golden-trail effect, text layout.
- Focus: the winding gold plankton path is the visual lead and mystery hook. Sherlock and Pearly study it without revealing the answer.
- Composition: A5 portrait. Large S-shaped path begins near the lower foreground, curves through the middle, and disappears toward the upper distance. Sherlock and Pearly stand in the lower-middle side zones looking down. Tiny unidentified long-legged silhouette at the far upper end. Large clear title area at the top without covering the silhouette or trail.
- Reveal lock: the distant figure must be a tiny dark long-legged silhouette only. No readable shell, face, glasses, scarf, cane, moss, or elderly features.
- Exact title:

```text
심해탐정 셜록 핀

밤에 빛나는 길
```

### Prompt

```text
Use case: illustration-story
Asset type: A5 portrait children's picture-book cover with exact Korean title
Primary request: Create the cover for the Sherlock Fin episode "밤에 빛나는 길" in a strict A5 portrait 148:210 composition. The main mystery image is one beautiful winding golden plankton trail lying low on a cozy nighttime Deep City coral alley.
Input images: Image 1 is the official Sherlock Fin character sheet and visual truth for Sherlock. Image 2 is the official Pearly sheet and visual truth for Pearly. Image 3 is the user-approved grandfather v5 sheet, used ONLY to derive a tiny distant long-legged silhouette without revealing identity. Image 4 is the official Deep City sheet for city architecture, palette, lighting, and picture-book finish. Image 5 is the official golden-trail effect sheet for the granular gold plankton path and small green moss flakes. Image 6 is the official text layout reference for title-panel spacing.
Scene/backdrop: Warm safe nighttime Deep City coral alley, deep navy and violet, pink and teal coral buildings, shell doors, warm amber windows, bubble-globe lamps, tiny bubbles and star-sand sparkles. Never frightening or empty-dark.
Subject/composition: A strong vertical A5 composition. One S-shaped granular golden path begins large in the lower foreground, curves through the center, and leads to the far upper distance. Sherlock Fin and Pearly stand at the lower-middle sides, accurately matching their official sheets, looking down with wonder. At the far end show only a very small dark long-legged silhouette. Reserve a clean cream shell-light rounded title area at the top with safe margins.
Text (verbatim, exactly these two blocks and no other writing):
"심해탐정 셜록 핀

밤에 빛나는 길"
Typography: large, clean, highly legible Korean picture-book title; preserve the exact spacing and spelling. The episode title is the largest line.
Constraints: A5 portrait, never landscape. Keep all content inside a central safe area for later 1054x1492 normalization. Golden trail stays on the ground and is made of many tiny gold specks, not a solid road. Green flakes are subtle and much smaller than the macro reference. Do not reveal the grandfather's shell, face, glasses, scarf, cane, moss, or identity. No extra text, signs, watermark, unrelated characters, prior-episode clues, footprints, necklace, or star marker.
```

- Candidate 1 raw: `00_candidate_text_v1_raw.png` — `1054 x 1492`.
- Local QA: PASS. Exact title, A5 portrait composition, Sherlock/Pearly identity, floor-hugging gold trail, and tiny unrevealed long-legged silhouette are present. Hold for user QA; do not promote to `final`.
- Candidate 1 normalized edit base: `00_candidate_text_v1.png` — SHA-256 `7504D6BBC8C1695B8E0A963D10F51A825D6F908377D1FE4340EAE2AA76F4CF0A`; **HOLD / revise Pearly only** because a second inner scalloped shell layer reads as an unnecessary hat.

## 01 - First Discovery

- Raw candidate: `01_candidate_text_v1_raw.png`
- Normalized candidate: `01_candidate_text_v1.png`
- References: Pearly, Deep City, golden-trail effect, text layout.
- Focus: Pearly discovers the path from her warm home at bedtime.
- Composition: A5 portrait, view from inside Pearly's cozy shell-themed room. Pearly in lower-right foreground, back/3-4 view but with enough face to read surprise, looking through a round window. The S-bend and continuity landmarks appear outside. Large cream text panel at lower left, approximately 38-42% of usable page area.
- Current-time lock: trail clearly present outside at night. No Sherlock and no grandfather silhouette.
- Exact text:

```text
딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요.
```

### Prompt

```text
Use case: illustration-story
Asset type: A5 portrait text-in-image children's picture-book page
Primary request: Create page 01 of "밤에 빛나는 길". From inside Pearly's warm shell-themed home at bedtime, Pearly suddenly notices a winding golden path outside the round window.
Input images: Image 1 is Pearly's official sheet and visual truth for her pink scallop shell, baby face, black bow tie, pearl blush, and small magnifier. Image 2 is the official Deep City sheet for coral architecture, palette, and lighting. Image 3 is the official golden-trail effect sheet for the ground-hugging granular gold path and tiny green flakes. Image 4 is the official text-panel layout reference.
Scene/backdrop: Cozy warm interior in shell cream and muted pink, looking outward through one round window into a safe deep navy/violet Deep City night. Outside use the locked S-curving cobalt alley: pink fan-coral building/arch on the left, teal shell-door home with one round amber window on the right, two bubble-globe lamps at the bend, and a small pale shell paving inlay in the foreground.
Subject/composition: Strict A5 portrait. Pearly occupies the lower-right foreground in a back/3-4 view, still showing her surprised wide-eyed face as she looks outside. The glowing trail curves visibly through the window. Place one large cream shell-light rounded text panel at the lower left with thin border and generous padding, about 38-42% of usable area. Keep the window view, Pearly's face, and the trail unobstructed.
Text (verbatim; render every line exactly and no other text):
"딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요."
Typography: large, clean, dark navy Korean children's-book type, even line spacing, exact punctuation and curly quotation marks.
Constraints: A5 portrait, never landscape. Keep text/faces/clue in the central safe area for later 1054x1492 normalization. Pearly must match the official sheet. Trail stays on the alley floor and remains granular. Green pieces remain tiny. No Sherlock, grandfather, silhouette, extra character, extra text, random sign, watermark, prior-episode prop, or scary darkness.
```

- Candidate 1 raw: `01_candidate_text_v1_raw.png` — `1055 x 1491`.
- Local QA: PASS WITH NORMALIZATION. Exact Korean text, Pearly identity, warm interior, window viewpoint, and night trail pass. Normalize by one pixel in each dimension to `1054 x 1492` without clipping or visible distortion; preserve raw.
- Candidate 1 normalized edit base: `01_candidate_text_v1.png` — `1054 x 1492`, SHA-256 `E07EA617A61BB85CC8AF9BA07212346BD37D64E03A2E232F3291335A0C4DE3B0`; **HOLD / revise Pearly shell only** because the upper and lower valves are yawed about 90 degrees relative to one another. The natural open angle may remain, but both valves must share one hinge axis and direction.

## 02 - Gone by Morning

- Raw candidate: `02_candidate_text_v1_raw.png`
- Normalized candidate: `02_candidate_text_v1.png`
- References: Pearly, Deep City, golden-trail effect for memory bubble only, text layout.
- Focus: the same alley is ordinary and empty in the morning; only a small memory bubble shows the prior-night trail.
- Composition: A5 portrait. Outside medium shot. Pearly lower-left, puzzled and pointing gently at the empty shell paving. Same S-bend landmarks as page `01`. Small memory bubble near upper left or above Pearly; large cream text panel upper-right, approximately 42-46% of usable page.
- Present-time lock: absolutely no gold plankton lights or green moss pieces anywhere in the present-day alley. Gold trail appears only inside the memory bubble.
- Exact text:

```text
다음 날 아침,
펄리는 골목으로 나가 보았어요.

그런데······

빛나는 길이
감쪽같이 사라졌어요!

“분명히 어젯밤에
여기 있었는데?”

그리고 그날 밤,
빛나는 길은
또 나타났어요.

밤마다, 밤마다요.
```

### Prompt

```text
Use case: illustration-story
Asset type: A5 portrait text-in-image children's picture-book page
Primary request: Create page 02 of "밤에 빛나는 길". In bright safe morning, Pearly stands outside in the exact same alley bend from page 01, but the golden path has completely vanished. A small memory bubble alone shows last night's glowing path.
Input images: Image 1 is Pearly's official sheet and visual truth for identity. Image 2 is the official Deep City sheet for the coral city style and bright aqua daytime treatment. Image 3 is the official golden-trail effect sheet, used ONLY inside the memory bubble. Image 4 is the official text-panel layout reference.
Scene/backdrop: Bright aqua morning version of the locked S-curving cobalt alley: pink fan-coral building/arch on the left, teal shell-door home with one round amber window on the right, two bubble-globe lamps at the bend, and the small pale shell paving inlay in the middle foreground. Same geometry and landmark placement as page 01.
Subject/composition: Strict A5 portrait outside medium shot. Pearly occupies the lower-left, puzzled, gently pointing toward the empty shell paving where the path had been. Add one small soft-edged memory bubble above/near Pearly showing the same bend at night with the granular golden path. Put one large cream shell-light rounded text panel in the upper-right with thin border and generous padding, about 42-46% of usable area. Keep Pearly, the empty ground, and memory bubble unobstructed.
Text (verbatim; render every line exactly and no other text):
"다음 날 아침,
펄리는 골목으로 나가 보았어요.

그런데······

빛나는 길이
감쪽같이 사라졌어요!

“분명히 어젯밤에
여기 있었는데?”

그리고 그날 밤,
빛나는 길은
또 나타났어요.

밤마다, 밤마다요."
Typography: large, clean, dark navy Korean children's-book type, even line spacing, exact punctuation, six middle dots in `······`, and curly quotation marks.
Constraints: A5 portrait, never landscape. Keep content in central safe area for 1054x1492 normalization. Present-time morning alley contains ZERO gold lights and ZERO green moss flakes. The glowing trail may appear only inside the memory bubble. Pearly matches the official sheet. No Sherlock, grandfather, silhouette, extra character, extra writing, watermark, prior-episode clue, or nighttime darkness outside the memory bubble.
```

- Candidate 1 raw: `02_candidate_text_v1_raw.png` — `1054 x 1492`.
- Local QA: PASS. Exact Korean text, morning alley without a present-time trail, memory bubble containing the trail, and Pearly identity pass. Hold for user QA; do not promote to `final`.
- Selected normalized candidate: `02_candidate_text_v1.png` — byte-identical copy, SHA-256 `513458E251A2680FA19FC9E551155AD005BEAB7225E434CDCA48456A93694E11`.
- User QA: **APPROVED**. No regeneration.

## 03 - The Request

- Raw candidate: `03_candidate_text_v1_raw.png`
- Normalized candidate: `03_candidate_text_v1.png`
- References: Sherlock Fin, Pearly, detective-office interior, golden-trail effect for memory bubble only, text layout.
- Focus: Pearly explains the recurring mystery; Sherlock listens and agrees to investigate.
- Composition: A5 portrait office medium shot. Sherlock and Pearly occupy the right/upper illustration zone. Pearly speaks with a small memory bubble showing the gold path. Sherlock listens and lightly presses the brim of the official hat. Large cream text panel lower-left/left half, approximately 44-48% of usable page.
- Sherlock lock: official teal hair, brown deerstalker, brown detective coat, black gloves, teal mermaid tail, yellow magnifier, official gold/teal hat ornament. Add one tiny pale-gold luminous shell pin beside the existing hat ornament without replacing or reshaping it.
- No grandfather silhouette or body part.
- Exact text:

```text
펄리는 셜록 핀에게 갔어요.

“밤마다 골목에
빛나는 길이 생겨요.

그런데 아침이면
사라져 버려요.

누가 만드는 걸까요?”

셜록 핀이 모자를
살짝 눌러썼어요.

“빛나는 길이라······
정말 신기한걸!

좋아, 같이 알아보자!”
```

### Prompt

```text
Use case: illustration-story
Asset type: A5 portrait text-in-image children's picture-book page
Primary request: Create page 03 of "밤에 빛나는 길" inside Sherlock Fin's official detective office. Pearly explains the recurring nighttime golden path while Sherlock listens kindly and agrees to investigate.
Input images: Image 1 is Sherlock Fin's official sheet and visual truth for her exact character identity, clothes, tail, hat, gloves, magnifier, and ornament. Image 2 is Pearly's official sheet and visual truth for her exact identity. Image 3 is the official detective-office interior sheet and visual truth for the shell desk, round city window, clue board, warm bubble lamps, chair, files, coral decor, and palette. Image 4 is the official golden-trail effect sheet, used ONLY inside Pearly's memory bubble. Image 5 is the official text-panel layout reference.
Scene/backdrop: Cozy detective office with the official shell desk, round city window, clue board, warm golden bubble lamps, blue shell chair, files and coral decor. Any papers or board marks remain tiny abstract shapes without readable pseudo-writing.
Subject/composition: Strict A5 portrait office medium shot. Place Sherlock and Pearly in the right/upper illustration zone. Pearly gestures while explaining, with a small soft-edged memory bubble above her showing a winding granular gold path on a night alley floor. Sherlock listens seriously but warmly and lightly presses the brim of the official hat with one gloved hand; the yellow magnifier remains visible. Add one tiny pale-gold luminous shell pin beside, not instead of, the existing official gold/teal hat ornament. Place one large cream shell-light rounded text panel on the lower-left/left half with thin border and generous padding, about 44-48% of usable page.
Text (verbatim; render every line exactly and no other text):
"펄리는 셜록 핀에게 갔어요.

“밤마다 골목에
빛나는 길이 생겨요.

그런데 아침이면
사라져 버려요.

누가 만드는 걸까요?”

셜록 핀이 모자를
살짝 눌러썼어요.

“빛나는 길이라······
정말 신기한걸!

좋아, 같이 알아보자!”"
Typography: large, clean, dark navy Korean children's-book type, even line spacing, exact punctuation, six middle dots in `······`, and curly quotation marks.
Constraints: A5 portrait, never landscape. Keep content in central safe area for 1054x1492 normalization. Sherlock and Pearly match their official individual sheets. Do not replace the hat ornament. No grandfather, crab silhouette, extra character, extra text, readable board writing, watermark, prior-episode prop, or unrelated clue.
```

- Candidate 1 raw: `03_candidate_text_v1_raw.png` — `1054 x 1492`.
- Illustration QA: PASS. Sherlock/Pearly identity, detective-office continuity, memory bubble, composition, and safe layout pass.
- Text QA: **USER-CONFIRMED PASS**. The first sentence has read `펄리는 셜록 핀에게 갔어요.` correctly since Candidate 1; the earlier internal reading of `셜록` as `설록` was mistaken. Candidate 1 is selected.
- Selected normalized candidate: `03_candidate_text_v1.png` — byte-identical copy, SHA-256 `E08FA2368C12F6BCB95E64193FC61287AFE7B35CC65B3D4B78FA01C23AC4BD4E`.
- User QA: **APPROVED**. No regeneration.
- Unnecessary repair candidate: `03_candidate_text_v2_text_repair_raw.png` — **HOLD / do not use**.
- No repair prompt remains active. The v2 attempt is retained only as a rejected work artifact; Candidate 1 is the visual and text source of truth.
- `03_candidate_text_v3_single_glyph_repair_raw.png` — **CANCELED / never generated**. No glyph change, panel rewrite, or text reflow will be performed.

## User QA Revision Pass - Pages 00 and 01

### Locked Pearly Details

- Pearly's gold eye piece is her planned official **monocle**. Keep the monocle lens, gold rim, and chain in both revisions; it is not a hat or an error.
- Keep Pearly's cream head, face, black bow tie, pink shell palette, scale, pose, and expression unless a tiny adjustment is unavoidable for correct shell attachment.
- The official Pearly sheet is the character-geometry source of truth. Ignore all labels and layout text on the sheet.
- Do not alter any story text, title text, Sherlock, lighting, background, trail, silhouette, text panel, crop, or composition outside the smallest failing Pearly unit.

### 00 Revision Prompt

- Edit target: `00_candidate_text_v1.png`
- Official identity reference: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Raw candidate output: `00_candidate_text_v2_pearly_hat_removed_raw.png`
- Normalized candidate output: `00_candidate_text_v2_pearly_hat_removed.png`

```text
Use case: precise-object-edit
Asset type: A5 portrait Korean children's storybook cover revision
Primary request: Edit ONLY Pearly in the lower-right of Image 1. Remove the separate smaller inner scalloped pink shell layer that reads as a bonnet or hat directly around/on Pearly's head. Pearly wears no hat. Leave one clean official rear upper clam-shell valve behind her bare cream head and the matching lower shell bowl, following Pearly's official geometry in Image 2.
Input images: Image 1 is the edit target and absolute source of truth for the cover composition, title, Sherlock, trail, background, lighting, and silhouette. Image 2 is the official Pearly identity and shell-geometry reference only; ignore its labels, diagrams, and white sheet background.
Subject lock: Keep Pearly's gold monocle beside her eye, gold monocle chain, black bow tie, face, expression, pose, scale, lower shell, and main rear upper shell. The monocle is intentional and must NOT be removed or changed.
Text (verbatim; preserve existing pixels and do not redraw):
"심해탐정 셜록 핀

밤에 빛나는 길"
Constraints: Change only the extra hat-like inner shell layer on Pearly. Preserve the existing 1054x1492 portrait crop; title panel and exact Korean glyphs; Sherlock Fin; magnifiers; gold plankton trail and green flakes; Deep City buildings, lamps, bubbles, coral, and lighting; and the tiny distant long-legged silhouette exactly. No new clothes, hat, bonnet, text, character, prop, watermark, or unrelated redraw.
```

- Generated raw: `00_candidate_text_v2_pearly_hat_removed_raw.png` — `1054 x 1492`.
- Selected revision candidate: `00_candidate_text_v2_pearly_hat_removed.png` — byte-identical copy, SHA-256 `C353A53B6FFD4AD4774665ACB755C17E0DF341BA93ADA4B530B1A8079640EA06`.
- Local QA: **PASS / awaiting user**. The separate hat-like inner scalloped layer is gone; Pearly retains one clean rear upper valve, lower shell, gold monocle and chain, black bow tie, face, and pose. Exact cover title, Sherlock, trail, silhouette, and composition remain correct.
- User QA override: **FAIL / do not use**. Pearly's head silhouette became flattened. Do not use this v2 image as a regeneration reference.

### 01 Revision Prompt

- Edit target: `01_candidate_text_v1.png`
- Official identity reference: `series/sherlock-fin-deep-city/references/characters/펄리.png`
- Raw candidate output: `01_candidate_text_v2_shell_axis_fixed_raw.png`
- Normalized candidate output: `01_candidate_text_v2_shell_axis_fixed.png`

```text
Use case: precise-object-edit
Asset type: A5 portrait Korean children's storybook page revision
Primary request: Edit ONLY Pearly's pink clam shell in the lower-right of Image 1. Correct the 90-degree yaw/twist mismatch between the upper and lower shell valves. Keep the natural open angle, but reconstruct them as two matching halves of one clam: one shared rear hinge, the same left-right/fore-aft direction, matching scalloped outline and radial ribs converging toward that hinge. Follow the coherent side/3-4 shell geometry in Image 2.
Input images: Image 1 is the edit target and absolute source of truth for Pearly's pose, the room, round window, night alley, gold trail, text panel, lighting, palette, crop, and composition. Image 2 is the official Pearly identity and shell-geometry reference only; ignore its labels, diagrams, and white sheet background.
Subject lock: Keep Pearly's cream head, facial features, expression, black bow tie, gold monocle lens, gold rim, and monocle chain. The monocle is an intentional official prop and must remain. Keep the upper valve visibly open behind Pearly; correct its shared axis and hinge rather than flattening or closing the shell.
Text (verbatim; preserve existing pixels, line breaks, punctuation, and do not redraw):
"딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요."
Constraints: Change only Pearly's shell geometry. Preserve the existing text panel pixel-for-pixel and all exact Korean text; Pearly's body, face, monocle and chain, bow tie, pose, and scale; the 1054x1492 portrait crop; room, window, buildings, lamps, gold trail, green flakes, furniture, colors, and lighting. No hat, bonnet, extra shell layer, new text, pseudo-writing, extra character, watermark, or unrelated redraw.
```

- Generated raw: `01_candidate_text_v2_shell_axis_fixed_raw.png` — `1054 x 1492`.
- Selected revision candidate: `01_candidate_text_v2_shell_axis_fixed.png` — byte-identical copy, SHA-256 `62AC8674BC707D94C084E1C05FCA745AF3CF6DB49520B6A1E4C52B0412ECEEB9`.
- Local QA: **PASS / awaiting user**. Upper and lower valves share one rear hinge and matching radial axis while keeping the natural open angle. Pearly's official monocle, chain, bow tie, face, pose, exact text, room, window, and trail remain correct.
- User QA override: **FAIL / do not use**. Pearly's head silhouette became flattened. Do not use this v2 image as a regeneration reference.

## Full Regeneration Pass v3 - Pages 00 and 01

### Regeneration Source Policy

- Regenerate each entire page as a new `illustration-story` asset. This is not an edit or inpainting pass.
- Use only original official references: Sherlock, Pearly, Deep City, the approved golden trail, grandfather v5 for the tiny cover silhouette, and the official text-layout sheet where the five-image input limit permits.
- Do not attach or imitate page `00`/`01` v1 or v2 candidates. They are process history only.
- Highest-priority Pearly lock: a fully rounded pearl/egg-shaped baby head with a high smooth dome, full forehead, round cheeks, and no flattened top, back, or side. The shell never substitutes for or cuts into the head silhouette.
- Pearly is never a floating head. Her small cream torso, two anatomically connected short arms, and two separate hands must be visible above the lower shell rim, matching the official sheet.
- Pearly wears no hat or bonnet. Keep exactly one official upper shell valve behind the head, one matching lower bowl, black bow tie, and the planned gold monocle with chain.
- Both shell valves share one rear hinge and the same directional axis. The upper valve may rotate open around that hinge but may not be yawed/twisted 90 degrees relative to the lower valve.

### 00 Full-Regeneration Prompt

- Official references: `characters/셜록핀.png`, `characters/펄리.png`, `심해탐정_셜록핀_딥시티_레퍼런스.png`, `props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`, `characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`.
- Raw output: `00_candidate_text_v3_full_regen_round_head_raw.png`
- Normalized output: `00_candidate_text_v3_full_regen_round_head.png`

```text
Use case: illustration-story
Asset type: new A5 portrait cover for a Korean picture-book episode; generate from scratch rather than editing any prior page
Input images: Image 1 is the official Sherlock Fin identity sheet. Image 2 is the official Pearly identity and shell-geometry sheet. Image 3 is the official Deep City environment/style reference. Image 4 is the approved golden-plankton trail and green-moss-flake reference. Image 5 is the approved elderly long-legged spider-crab grandfather reference, used only to derive a tiny anonymous distant silhouette. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: cozy midnight Deep City coral alley with indigo and violet buildings, warm windows, bubble lamps, soft bubbles, and an S-curving ground-level trail made of many tiny gold plankton lights with small green moss flakes.
Subject: Sherlock Fin and Pearly stand beside the trail and study it with magnifiers. Sherlock matches Image 1. Pearly matches Image 2 with a FULLY ROUND pearl/egg-shaped baby head: high smooth dome, full forehead, round cheeks, no flat top, no flat rear, no compressed skull. Her cream head must remain clearly separate from the shell. Keep her official gold monocle and chain and black bow tie. She wears no hat or bonnet. Use exactly one upper pink clam valve behind her head and one aligned lower valve, sharing one hinge and axis.
Composition/framing: A5 portrait `148:210`. Large cream ornamental title panel in the upper 36-40%. The bright S-path begins in the lower foreground and leads into the distance. Sherlock appears lower-left and Pearly lower-right, both below the title. At the far end of the path, show only a very small unreadable long-legged silhouette; do not reveal the grandfather's face, shell, glasses, scarf, cane, or moss.
Style/medium: polished warm 3-year-old children's picture-book illustration; rounded readable forms; cozy neon-jazz underwater fantasy; crisp Korean typography.
Text (verbatim; render exactly and no other text):
"심해탐정 셜록 핀

밤에 빛나는 길"
Constraints: Keep Pearly's head tall, domed, round, and baby-like; never flatten or crop the head. No extra inner scalloped shell around the head, no shell hat, no bonnet. Preserve the official monocle, chain, bow tie, shell palette, and coherent hinge anatomy. Golden trail stays on the ground and remains granular. Green pieces remain small. No extra character, readable sign, prior-episode clue, extra text, pseudo-writing, watermark, footprints, necklace, or star marker. Never landscape.
```

- Generated raw: `00_candidate_text_v3_full_regen_round_head_raw.png` — `1054 x 1492`.
- Selected regeneration candidate: `00_candidate_text_v3_full_regen_round_head.png` — byte-identical copy, SHA-256 `BFA97BA68E97FCA22D7D4033DA6E0F17A54D253691684414B67DD2FDB0F46330`.
- Local QA: **PASS / awaiting user**. Pearly's head has a high smooth dome, full forehead and rear curve, and round cheeks; no flattened edge or hat-like inner shell. Official monocle, chain, bow tie, coherent shell, exact title, Sherlock, granular trail, and tiny unrevealed silhouette pass.

### 01 Full-Regeneration Prompt

- Official references: `characters/펄리.png`, `심해탐정_셜록핀_딥시티_레퍼런스.png`, `props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`, `layouts/텍스트박스_레이아웃_레퍼런스.png`.
- Raw output: `01_candidate_text_v3_full_regen_round_head_shell_axis_raw.png`
- Normalized output: `01_candidate_text_v3_full_regen_round_head_shell_axis.png`

```text
Use case: illustration-story
Asset type: new A5 portrait Korean picture-book story page; generate from scratch rather than editing any prior page
Input images: Image 1 is the official Pearly identity and shell-geometry sheet. Image 2 is the official Deep City environment/style reference. Image 3 is the approved golden-plankton trail and green-moss-flake reference. Image 4 is the official text-panel layout reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: nighttime inside Pearly's cozy shell-themed bedroom. Warm peach light indoors. A large round window looks out onto an indigo Deep City alley with pink fan-coral building left, teal shell-door house right, two bubble lamps, and a granular S-curving gold trail on the paving.
Subject: Pearly is awake in the lower-right foreground and looks left/up through the window with a surprised curious expression. Match Image 1 exactly. Her cream baby head must be fully rounded and three-dimensional in side/3-4 view: high smooth dome, full forehead and back of skull, round cheek, no flat top, no flat rear, no compressed profile. Keep the official gold monocle lens, rim, and chain beside her eye and the black bow tie. She wears no hat or bonnet. Use one matching upper shell valve behind her head and one lower shell bowl. Both valves share the same rear hinge, the same fore-aft direction, matching scallops, and radial ribs converging to that hinge. The upper valve is naturally open but not yawed/twisted sideways relative to the lower valve.
Composition/framing: A5 portrait `148:210`. View from inside the room toward the round window. Pearly occupies the lower-right 32-36% without touching the page edge with her head. A large cream scalloped text panel occupies the lower-left 38-42%, with generous padding. The window and trail remain clearly visible above.
Style/medium: polished warm 3-year-old children's picture-book illustration; rounded readable anatomy; cozy neon-jazz underwater fantasy; crisp Korean typography.
Text (verbatim; render every character, line break, space, punctuation mark, and quote exactly; no other text):
"딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요."
Constraints: Highest priority is Pearly's intact round head silhouette and official identity. No flattened head, compressed forehead, cropped cranium, extra inner shell, shell hat, or bonnet. Retain the monocle and chain. Shell valves must form one coherent hinged clam. Trail stays on the alley floor and remains granular; green flakes stay small. No Sherlock, grandfather, silhouette, extra character, random sign, extra text, pseudo-writing, watermark, prior-episode prop, or scary darkness. Never landscape.
```

- Generated raw: `01_candidate_text_v3_full_regen_round_head_shell_axis_raw.png` — `1054 x 1492`.
- Rejected candidate: `01_candidate_text_v3_full_regen_round_head_shell_axis.png` — SHA-256 `A0529C24EA19ADE8742123C0AC77B4A9C0729C23973AC3B1A9092C135D80F42C`.
- User QA: **FAIL / do not use**. Pearly's rounded head, shell axis, monocle, and text improved, but her torso and both arms disappeared, leaving a floating-head read. Do not use v3 as a visual input.

## Page 01 Full Regeneration Pass v4 - Two Arms Lock

- Official references only: `characters/펄리.png`, `심해탐정_셜록핀_딥시티_레퍼런스.png`, `props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`, `layouts/텍스트박스_레이아웃_레퍼런스.png`.
- Raw output: `01_candidate_text_v4_full_regen_round_head_two_arms_shell_axis_raw.png`
- Normalized output: `01_candidate_text_v4_full_regen_round_head_two_arms_shell_axis.png`
- Do not attach or imitate page `01` v1, v2, or v3.

```text
Use case: illustration-story
Asset type: new A5 portrait Korean picture-book story page; generate from scratch from official references only
Input images: Image 1 is the official Pearly identity, complete-body, arm, hand, monocle, and shell-geometry sheet. Image 2 is the official Deep City environment/style reference. Image 3 is the approved golden-plankton trail and green-moss-flake reference. Image 4 is the official text-panel layout reference. Ignore all labels, diagrams, sheet backgrounds, and reference-image text.
Scene/backdrop: nighttime inside Pearly's cozy shell-themed bedroom. Warm peach light indoors. A large round window looks out onto an indigo Deep City alley with a pink fan-coral building left, teal shell-door house right, bubble lamps, and a granular S-curving gold trail on the paving.
Subject: Show Pearly as a COMPLETE small character seated in her open clam, never as a floating head. Match Image 1. Her cream baby head is fully round and three-dimensional in side/3-4 view: high smooth dome, full forehead and back of skull, round cheek, no flat edge. Beneath the head, show a small cream upper torso. Show TWO complete short arms connected naturally at the shoulders and TWO distinct little hands above the lower shell rim, one hand visible on each side of her torso. Both forearms and hands must be readable and separate from the bow tie, shell rim, and monocle chain. Let both hands rest gently on the lower shell rim while she looks left/up through the window. Keep the black bow tie centered on her torso. Keep the official gold monocle lens, rim, and chain beside her eye.
Shell anatomy: Pearly wears no hat or bonnet. Use exactly one upper valve behind her and one lower shell bowl. Both valves share one rear hinge, the same fore-aft direction, matching scallops, and radial ribs converging to that hinge. The upper valve is naturally open, not twisted 90 degrees relative to the lower valve.
Composition/framing: A5 portrait `148:210`. View from inside toward the round window. Pearly occupies the lower-right 32-36%, with her full head, torso, both arms, both hands, bow tie, monocle, and shell clearly inside the safe area. A large cream scalloped text panel occupies the lower-left 38-42% with generous padding. Window and trail remain clear above.
Style/medium: polished warm 3-year-old children's picture-book illustration; rounded readable anatomy; cozy neon-jazz underwater fantasy; crisp Korean typography.
Text (verbatim; render every character, line break, space, punctuation mark, and quote exactly; no other text):
"딥시티에
포근한 밤이 왔어요.

펄리가 잠자리에 들려는데,

창밖이
반짝반짝 빛났어요.

“어? 저게 뭐지?”

골목에
금빛으로 빛나는 길이
구불구불 나 있었어요."
Constraints: Highest priority is complete Pearly anatomy: round head plus visible torso plus exactly two connected arms and exactly two hands. No missing arms, hidden hands, detached hands, floating head, flattened head, compressed skull, extra limb, extra inner shell, shell hat, or bonnet. Retain the monocle and chain. Keep a coherent hinged clam. Trail remains ground-hugging and granular; green flakes stay small. No Sherlock, grandfather, silhouette, extra character, random sign, extra text, pseudo-writing, watermark, prior-episode prop, or scary darkness. Never landscape.
```

- Generated raw: `01_candidate_text_v4_full_regen_round_head_two_arms_shell_axis_raw.png` — `1054 x 1492`.
- Selected regeneration candidate: `01_candidate_text_v4_full_regen_round_head_two_arms_shell_axis.png` — byte-identical copy, SHA-256 `30F045CCCAAA6A57B4D056E55F9EE30C0AB265C79695E23879ADBC4D709F58D4`.
- Local QA: **PASS / awaiting user**. Pearly has a high round head, visible small torso, exactly two shoulder-connected arms and two distinct hands resting above the lower shell rim. Official monocle/chain, centered bow tie, coherent shared shell hinge/axis, exact Korean text, text panel, room, window, and granular trail pass.

## QA Gate

- [x] All four images are portrait and normalized to `1054 x 1492` without stretching or clipping required content.
- [x] Cover title is exact and grandfather identity remains unrevealed.
- [x] Page `01` and `02` alley landmarks match; night/day contrast is clear.
- [x] Page `02` present-time alley has no current gold trail or green flakes.
- [x] Page `03` matches the official office and both character sheets.
- [x] Every Korean character, space, punctuation mark, quote, and line break matches this plan. Page `03` Candidate 1 was additionally confirmed by the user.
- [x] Text panels are consistent, readable, and do not cover required story elements.
- [x] No prior-episode contamination, legible pseudo-writing, extra text, or watermark.
- [x] Page `00` v2 removed the extra hat-like shell layer, but **USER FAIL** because Pearly's head became flat.
- [x] Page `01` v2 corrected the shell hinge/axis, but **USER FAIL** because Pearly's head became flat.
- [x] Pages `02` and `03` are user approved and locked against regeneration.
- [x] Page `00` v3 full regeneration has a high, fully rounded Pearly head, no hat-like extra shell, and the official monocle; awaiting user approval.
- [x] Page `01` v3 restored the round head and shell axis, but **USER FAIL** because the torso and both arms disappeared.
- [x] Page `01` v4 has a round head, visible torso, exactly two connected arms and two hands, coherent shell hinge/axis, and the official monocle.
- [x] User approval for cover `00` v3 and page `01` v4; both promoted to final.
