# Reference Setup Prompt Plan - 밤에 빛나는 길

## Scope

- Episode: `밤에 빛나는 길`
- Batch: `reference setup only`
- Work folder: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/work_2026-07-12/reference_setup`
- Final episode folder: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final`
- Do not generate final story pages in this batch.
- Create only the two missing recurring visual references required by the page plan.

## Existing Official References To Use As Visual Truth

- `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
  - Role: series crab-character rendering language and child-safe simplification only.
  - Do not copy Crabson's red body, top hat, tuxedo, saxophone, compact legs, or identity.
- `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`
  - Role: overall series character proportions, rounded forms, large readable eyes, finish, and emotional tone.
- `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - Role: Deep City palette, soft picture-book finish, neon-jazz underwater mood, and coral-alley lighting.

## Shared Reference Rules

- Use case: `illustration-story`.
- Bright, warm children's picture-book/animation illustration matching the official Sherlock Fin references.
- Deep City is cozy, safe, and magical: deep blue and violet with emerald, pink, and warm gold accents.
- Rounded, friendly shapes; clear large eyes; soft painterly finish; no photorealism or glossy 3D toy rendering.
- Reference-sheet composition must be clean and reusable for later page generation.
- No story-page text, labels, letters, pseudo-writing, random signage, arrows, or watermarks.
- Do not import characters, props, or plot details from unrelated prior episodes.

## 1. Long-Legged Spider-Crab Grandfather Character Sheet

- Candidate output: `reference_setup/긴다리거미게_할아버지_reference_candidate_v1.png`
- Official target: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Input images:
  - Image 1: `크랩슨.png` — style reference only, not identity.
  - Image 2: `심해탐정_셜록핀_인물_레퍼런스.png` — overall character-sheet language.
  - Image 3: `심해탐정_셜록핀_딥시티_레퍼런스.png` — palette and finish.

### Locked Features

- New identity: an elderly long-legged spider crab, not Crabson and not a lobster.
- Warm stone-brown to muted umber rounded triangular carapace; friendly and dignified, never realistic or creepy.
- A soft patch of old-rock-like green moss grows on the upper/back carapace.
- Very long, thin, gently jointed legs are the defining silhouette.
- Show four principal legs clearly; overlap or simplify the remaining legs behind the body so the anatomy stays stable.
- Two small friendly front claws, much smaller than Crabson's claws.
- Round glasses, a small child-safe walking cane held naturally by one front claw, and a cozy muted plaid scarf.
- No top hat, tuxedo, saxophone, red body, sharp spikes, exposed mouthparts, huge claws, weapon-like cane, or threatening pose.
- Expressions: gentle smile, warm “허허” laugh, surprised delight, calm thoughtful look.
- Include a clear back/3-4 rear view showing the moss placement for pages `08`-`10`.

### Prompt

```text
Use case: illustration-story
Asset type: official reusable character design sheet for the Sherlock Fin children's picture-book series
Primary request: Create the official reference sheet for the new long-legged spider-crab grandfather from the episode "밤에 빛나는 길".
Input images: Image 1 is the official Crabson sheet for the series' child-safe crab rendering language only; do not copy Crabson's identity. Image 2 is the official Sherlock Fin ensemble sheet for proportions, rounded shapes, large readable eyes, and finish. Image 3 is the official Deep City sheet for palette and soft neon-jazz underwater mood.
Subject: A large, dignified, very gentle elderly long-legged spider crab. He has a warm stone-brown to muted umber rounded triangular carapace, a soft patch of old-rock-like green moss growing across the upper and rear shell, round glasses, a small safe walking cane, and a cozy muted plaid scarf. His defining silhouette is extremely long, thin, gently jointed legs. Keep four principal legs clearly readable and overlap or simplify the remaining legs behind the body. Give him two small friendly front claws, much smaller than Crabson's.
Composition/framing: Clean text-free character sheet on a light neutral softly underwater background. Show full-body front, 3/4, side, and rear/3-4 rear views with the exact same design and proportions. Add small expression portraits for gentle smile, warm laughing eyes, surprised delight, and calm thoughtfulness. Add small detail vignettes for moss placement, plaid scarf, round glasses, cane, and the stable leg-joint silhouette.
Style/medium: Match the official Sherlock Fin children's picture-book/animation illustration, softly painterly, rounded, clean, warm, safe, cute, emotionally readable, not photorealistic and not glossy 3D.
Color palette: warm stone brown and muted umber shell, soft moss green, cream and muted teal-gold plaid accents, deep-city blue/violet only as light decorative accents.
Constraints: This is a new identity. Preserve one consistent carapace shape, moss placement, glasses, scarf, cane, claw size, and long-leg proportions across every view. Make the rear view usable as visual truth for story pages 08 through 10.
Avoid: Crabson's red body, tall hat, tuxedo, saxophone, compact crab legs, or large claws; no lobster shape; no extra arms, tentacles, missing legs, tangled anatomy, sharp spikes, exposed mouthparts, monster realism, fear, text, labels, letters, arrows, signage, or watermark.
```

### QA

- [x] Reads immediately as a kind grandfather and as a distinct new character.
- [x] Long-legged spider-crab silhouette is stable across all views.
- [x] Four principal long legs are clearly readable; lighter secondary legs stay overlapped and do not become a tangled mass.
- [x] Rear view clearly locks the moss location.
- [x] Round glasses, cane, and plaid scarf are consistent.
- [x] No Crabson identity contamination or unrelated episode details.
- [x] No text, pseudo-writing, labels, arrows, or watermark.

## 2. Golden Plankton Trail and Green Moss Flakes Effect Sheet

- Candidate output: `reference_setup/금빛플랑크톤길_이끼가루_reference_candidate_v1.png`
- Official target: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Input images:
  - Image 1: `심해탐정_셜록핀_딥시티_레퍼런스.png` — palette, coral alley, lighting, and finish.

### Locked Features

- The trail hugs the alley floor; it is not a floating ribbon, beam, liquid stream, painted stripe, or solid road.
- The trail is formed by many tiny warm-gold glowing plankton specks gathered into a gentle winding curve.
- Plankton are a luminous swarm, not individual mascot characters; no faces, or only imperceptible simple dot eyes in rare close detail.
- Soft green moss flakes are clearly distinct among the gold lights, especially in macro views; they are small rounded leafy fragments, not dust-only pixels.
- The causal sequence must read visually: green moss flakes fall, gold plankton gather around them, the cluster glows brighter, and a connected path remains behind.
- Gold glow supplies warmth but does not wash out the green flakes or turn the night scene white.

### Prompt

```text
Use case: illustration-story
Asset type: official reusable visual-effect and story-clue reference sheet for the Sherlock Fin children's picture-book series
Primary request: Create the official visual reference for the winding golden plankton trail and soft green moss flakes from the episode "밤에 빛나는 길".
Input images: Image 1 is the official Deep City sheet and is visual truth for the coral-alley palette, underwater neon-jazz atmosphere, warm window lights, bubble lamps, and soft picture-book finish.
Scene/backdrop: A cozy nighttime Deep City coral alley in deep navy and violet with warm windows and gentle bubble lamps. Keep the setting sparse enough that the recurring effect is unmistakable.
Subject: A low ground-hugging winding trail made from many tiny warm-gold bioluminescent plankton specks. Small soft green moss flakes are scattered within the gold clusters and remain clearly visible. The plankton act as a luminous swarm, not separate mascot characters.
Composition/framing: A clean text-free four-part visual reference sheet: one wide alley view showing the full winding floor trail; one medium close view showing gold plankton gathering around green moss flakes; one macro clue view where the green fragments are child-readable among the gold lights; and one simple left-to-right process vignette showing green moss flakes falling, gold plankton clustering around them, and the cluster brightening into a connected trail. Use visual spacing only, with no arrows or labels.
Style/medium: Match the official Sherlock Fin warm children's picture-book illustration, softly painterly, magical, clear, cozy, safe, not photorealistic and not glossy 3D.
Color palette: deep navy, violet, emerald and coral accents, warm window yellow, luminous soft gold, distinct moss green.
Constraints: Keep the light on or immediately above the alley floor. The trail must remain visibly granular and organic, formed from many gold specks around green flakes. Preserve clear green-vs-gold contrast in every close view. No characters, legs, crabs, or story-page text.
Avoid: floating ribbon, laser beam, liquid river, solid yellow road, painted stripe, star-shaped confetti, fire, smoke, glowing footprints, separate trails from multiple characters, faces on every plankton, unreadable green dust, harsh darkness, horror, text, labels, letters, arrows, signage, or watermark.
```

### QA

- [x] Wide view reads as one winding path on the alley floor.
- [x] Trail remains granular and clearly formed by many gold plankton lights.
- [x] Green moss flakes are visibly distinct and child-readable in the close and macro views.
- [x] Process sequence makes the cause understandable without text or arrows.
- [x] No character, body-part, unrelated prop, or prior-episode contamination.
- [x] No text, pseudo-writing, labels, arrows, or watermark.

## Completed Outputs

- Selected: `긴다리거미게_할아버지_reference_candidate_v1.png`
- Promoted: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Selected: `금빛플랑크톤길_이끼가루_reference_candidate_v1.png`
- Promoted: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`

## QA Notes

- Grandfather v1: PASS. Distinct from Crabson; friendly elder identity, long-leg silhouette, rear moss placement, glasses, scarf, and cane are all reusable.
- Golden trail v1: PASS WITH LOCK. Use the full-size green pieces as a macro reference. Scale them down in wide pages while preserving visible green-vs-gold contrast; they must not look like large floor tiles.
- Both official outputs are exact byte copies of their selected candidate files.

## Revision 1 - Grandfather Eye Language

- User direction: the grandfather should not have uniformly large, round, sparkling baby-like eyes. A gentle squint better communicates his age and “허허” personality.
- Edit target: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Candidate output: `reference_setup/긴다리거미게_할아버지_reference_candidate_v2_squint.png`
- Intent: `precise-object-edit`; change only the eyes and the minimum surrounding facial expression needed for natural squints.

### Revision Locks

- Preserve the exact sheet layout, canvas ratio, view order, body silhouettes, shell shape and texture, moss placement, leg count and joints, claws, scarf, glasses, cane, palette, background, detail objects, and painterly finish from v1.
- Full-body front, 3/4, and side views: gentle narrow crescent squints behind the glasses, with little or no visible iris. The character should look alert, kind, and unhurried, never sleepy or lifeless.
- Gentle-smile and thoughtful portraits: the same soft crescent squint; use white eyebrows and the small mouth to distinguish mood.
- “허허” laugh portrait: fully closed upward-curving smiling eyes.
- Surprised-delight portrait only: eyes open modestly behind the glasses, smaller and less round/sparkling than v1; this is the model for page `09`.
- Do not change the rear view or non-face detail panels.
- No giant glossy pupils, baby-anime sparkle eyes, droopy sad eyes, exhausted eyes, new wrinkles, beard, moustache, text, labels, or unrelated additions.

### Revision Prompt

```text
Use case: precise-object-edit
Asset type: revised official character reference sheet for the Sherlock Fin children's picture-book series
Primary request: Edit only the eye language of the long-legged spider-crab grandfather in Image 1 so he reads as a warm, dignified elderly character rather than a baby-like character.
Input images: Image 1 is the edit target and visual truth for every non-eye feature and for the complete sheet layout.
Change: In every full-body front, 3/4, and side view, replace the large round sparkling eyes with gentle narrow crescent-shaped squinting eyes behind the same round glasses. Keep him alert, kind, warm, and unhurried—not sleepy. In the expression portraits, use soft crescent squints for the gentle smile and thoughtful look, fully closed upward-curving smiling eyes for the warm “허허” laugh, and modestly opened eyes only for surprised delight. The surprise eyes must remain smaller, calmer, and less glossy or round than the original v1 eyes. Let the existing white eyebrows and small mouth carry the emotion.
Constraints: Preserve exactly the canvas ratio, panel layout, view order, character identity, triangular stone-brown carapace, shell texture, moss shape and placement, long thin leg anatomy, small claws, plaid scarf, round glasses frames, cane, colors, lighting, background decoration, detail panels, and soft painterly finish. Change only the eyes and the minimum eyelid/eyebrow interaction needed to make the squints natural. Leave the rear view and non-face detail panels unchanged.
Avoid: giant glossy pupils, baby-anime sparkle eyes, uniformly wide-open eyes, droopy sad eyes, exhausted or sleeping expression, new wrinkles, beard, moustache, altered glasses, altered body or props, missing or extra limbs, text, labels, letters, arrows, watermark, or unrelated episode content.
```

### Revision QA

- [x] Default views immediately read as a gentle older grandfather.
- [x] Squints remain lively and warm, not sleepy, sad, or lifeless.
- [x] Only the surprised portrait opens the eyes, and those eyes are modest rather than baby-like.
- [x] Round glasses remain unchanged and do not obscure the intended eye shapes.
- [x] Every body, prop, layout, color, texture, and detail-panel invariant from v1 remains stable.
- [x] No text or unrelated visual contamination.

### Revision Result

- Selected: `긴다리거미게_할아버지_reference_candidate_v2_squint.png`
- SHA-256: `5D691548CBD147BD4B2D50D36099C682D77BA346E824F8EB9975E9A59DC48256`
- Size: `1448 x 1086 PNG`
- Promoted to active official path: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Superseded but preserved: `긴다리거미게_할아버지_reference_candidate_v1.png` (`HOLD / do not use`).

## Revision 2 - Mouth-Corner Grandfather Smile Lines

- User direction: retain the approved squint-eye personality but add a clearer age cue around the mouth so the character reads more immediately as a grandfather.
- Edit target: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png` (active squint-eye v2).
- Candidate output: `reference_setup/긴다리거미게_할아버지_reference_candidate_v3_squint_smile_lines.png`
- Intent: `precise-object-edit`; add only subtle mouth-corner age/smile lines and the minimum adjacent shading needed to integrate them.

### Revision 2 Locks

- Preserve the exact approved v2 squint-eye language: warm crescent squints in default views, fully closed laughing eyes, and modestly opened eyes only in the surprise portrait.
- Add one or two short, thin, softly curved smile/age creases immediately beside each visible mouth corner. On side and 3/4 views, follow the face perspective and show only the naturally visible creases.
- Smile and “허허” laugh portraits may show two slightly clearer creases per side. Calm and thoughtful expressions use one faint crease per side. The surprised portrait keeps very light short creases so the age cue remains without looking like a smile.
- Creases use a soft medium-brown line close to the existing face outline color, never black, harsh, or etched.
- Keep the face smooth and child-friendly everywhere else. Do not add eye wrinkles, forehead wrinkles, deep nasolabial folds, drooping cheeks, jowls, facial hair, liver spots, or realistic aged skin texture.
- Preserve exactly the v2 sheet layout, canvas ratio, body, shell texture, moss, legs, claws, scarf, glasses, cane, palette, background, detail panels, and painterly finish.

### Revision 2 Prompt

```text
Use case: precise-object-edit
Asset type: revised official character reference sheet for the Sherlock Fin children's picture-book series
Primary request: Edit only the mouth-corner age cues of the long-legged spider-crab grandfather in Image 1, keeping the approved squint-eye v2 character intact. Add subtle child-friendly smile wrinkles so he reads more immediately as a warm grandfather.
Input images: Image 1 is the active squint-eye v2 edit target and visual truth for the complete layout, identity, eyes, body, props, palette, textures, and finish.
Change: Add one or two short, thin, softly curved smile/age creases immediately beside each visible mouth corner in every face view. Follow each view's perspective. Make the creases slightly clearer in the gentle smile and warm “허허” laugh portraits, faint in calm and thoughtful expressions, and very light beside the surprised O-shaped mouth so the age cue remains without turning it into a smile. Use a soft medium-brown line matching the existing facial outline, not black. Keep the face warm, lively, and child-friendly.
Constraints: Preserve exactly the approved v2 crescent squints, closed laughing eyes, modest surprise eyes, white eyebrows, mouth shapes, round glasses, canvas ratio, sheet layout, view order, triangular stone-brown carapace, shell texture, moss shape and placement, long thin leg anatomy, small claws, plaid scarf, cane, colors, lighting, background decoration, detail panels, and soft painterly finish. Change only the small mouth-corner creases and the minimum blending needed around them.
Avoid: eye wrinkles, forehead wrinkles, deep human nasolabial folds, sagging cheeks, jowls, frown lines, tired or sad expression, beard, moustache, realistic aged skin texture, altered eyes or glasses, altered body or props, missing or extra limbs, text, labels, arrows, watermark, or unrelated episode content.
```

### Revision 2 QA

- [ ] Character reads more immediately as a grandfather than v2. — USER QA FAIL: no meaningful visible difference.
- [ ] Mouth-corner creases are visible but soft, short, and child-friendly. — USER QA FAIL: creases disappear at normal viewing size.
- [x] Creases respond naturally to smile, laugh, surprise, and thoughtful expressions.
- [x] Approved v2 squint-eye language remains unchanged.
- [x] No deep folds, sagging, sadness, facial hair, or realistic aged-skin effect.
- [x] Every non-mouth invariant from v2 remains stable.
- [x] No text or unrelated visual contamination.

### Revision 2 Result

- Rejected: `긴다리거미게_할아버지_reference_candidate_v3_squint_smile_lines.png` (`FAIL / do not use`).
- SHA-256: `CA5086E2E86342C772AEF6382CDCF20B29CC66A5F72E3A5C402DC513AF573A6D`
- Size: `1448 x 1086 PNG`
- Temporarily promoted before user review, but rejected after user visual comparison; must be replaced by a clearly different v4.
- Superseded but preserved: `긴다리거미게_할아버지_reference_candidate_v2_squint.png` (`HOLD / edit base`).

## Revision 3 - Clearly Visible Mouth Wrinkles

- User verdict on v3: “똑같은 것 같다.” The wrinkle edit was too subtle to function as a design change.
- Clean edit target: `reference_setup/긴다리거미게_할아버지_reference_candidate_v2_squint.png` — the user-approved squint-eye version, not rejected v3.
- Candidate output: `reference_setup/긴다리거미게_할아버지_reference_candidate_v4_squint_clear_mouth_wrinkles.png`
- Intent: `precise-object-edit`; make the mouth wrinkles unmistakable at normal reference-sheet viewing size while preserving the v2 character.

### Revision 3 Locks

- Preserve the approved v2 eye language and every non-mouth feature exactly.
- In each front-facing face, draw two distinct medium-length curved dark-warm-brown wrinkle strokes immediately outside each mouth corner. The upper stroke follows the smile arc outward; the lower stroke sits slightly below and sweeps gently down/out. Add one short lower auxiliary crease where space allows.
- Keep the strokes visibly separated from each other and from the mouth so they do not merge into one thicker smile.
- Main wrinkle strokes should be approximately one-half of the mouth's width and carry nearly the same visual weight as the white eyebrow outline, though still thinner and softer than the mouth outline.
- The wrinkles must remain clearly visible when the entire 1448 x 1086 sheet is displayed at about 25% size or as a conversation preview.
- Smile and “허허” portraits use the clearest wrinkles. Calm and thoughtful portraits retain the same two-line identity at slightly reduced contrast. The surprised portrait uses two shorter but still visible side creases around the O-shaped mouth.
- On 3/4 and side views, transform the same design with perspective and show only naturally visible lines.
- Do not add wrinkles anywhere else. No eye crow's feet, forehead lines, deep nose-to-mouth folds, sagging cheeks, sadness, beard, or moustache.

### Revision 3 Prompt

```text
Use case: precise-object-edit
Asset type: revised official character reference sheet for the Sherlock Fin children's picture-book series
Primary request: Starting from Image 1, make an OBVIOUS, clearly visible mouth-wrinkle redesign for the long-legged spider-crab grandfather. The previous attempt was rejected because it looked identical at normal viewing size. Keep the approved squint-eye v2 character, but add unmistakable warm grandfather smile wrinkles around every visible mouth.
Input images: Image 1 is the user-approved squint-eye v2 edit target and visual truth for all eyes, identity, layout, body, props, textures, colors, and finish. Do not use or imitate the rejected subtle v3.
Change: For each front-facing face, add TWO DISTINCT medium-length curved warm dark-brown wrinkle strokes immediately outside EACH mouth corner. The upper stroke follows the smile arc outward; the lower stroke sits separately beneath it and curves gently down and outward. Where space allows, add one additional short lower auxiliary crease. Keep clear spacing between the mouth and each stroke and between the strokes themselves. Each main wrinkle should be about half the width of the mouth and strong enough to remain clearly visible when the full sheet is shown at 25% size. Use a line weight almost as visible as the white eyebrow outline, but slightly thinner and softer than the mouth outline. In 3/4 and side views, preserve the same wrinkle identity in correct perspective. Smile and “허허” portraits have the strongest clear wrinkles; calm/thoughtful faces keep two visible lines per side; the surprised O-mouth portrait has two shorter but still obvious age creases.
Constraints: Preserve exactly the v2 crescent squints, closed laughing eyes, modest surprise eyes, white eyebrows, mouth shapes, round glasses, canvas ratio, sheet layout, view order, triangular stone-brown carapace, shell texture, moss shape and placement, long thin leg anatomy, small claws, plaid scarf, cane, colors, lighting, background decoration, detail panels, and soft painterly finish. Change only the clearly visible mouth-corner wrinkles and minimal blending around them.
Avoid: barely visible micro-lines, a result that looks the same as v2, merged lines that become an oversized mouth, black harsh ink, eye crow's feet, forehead wrinkles, deep human nasolabial folds, sagging cheeks, jowls, frown lines, tired or sad expression, beard, moustache, realistic aged skin texture, altered eyes or glasses, altered body or props, missing or extra limbs, text, labels, arrows, watermark, or unrelated episode content.
```

### Revision 3 QA

- [x] Difference from v2 is obvious at conversation-preview size.
- [x] Two separated mouth-corner wrinkle strokes are visible on each applicable side.
- [x] Wrinkles read as warm age cues, not an enlarged mouth, sadness, or realistic skin folds.
- [x] Approved v2 squints and all non-mouth invariants remain stable.
- [x] No text or unrelated contamination.

### Revision 3 Result

- Candidate: `긴다리거미게_할아버지_reference_candidate_v4_squint_clear_mouth_wrinkles.png`
- Status: `USER QA FAIL / do not use`; visible marks are outer-mouth smile wrinkles, not nasolabial folds.
- SHA-256: `05905844C44F29E1CB1E5F0164BCDF899AF361B42E9FE20D5E82CBE644914499`
- Size: `1448 x 1086 PNG`
- Active official reference: restored to `긴다리거미게_할아버지_reference_candidate_v2_squint.png` content until v4 is explicitly approved.
- Rejected v3 remains preserved as `FAIL / do not use` and is not the active official image.

## Revision 4 - Explicit Elderly Male Face With Nasolabial Folds

- User correction: the needed feature is `팔자주름`—true nasolabial folds—not smile lines placed outside the mouth. The prompt must explicitly demand an old man's face.
- Clean edit target: `reference_setup/긴다리거미게_할아버지_reference_candidate_v2_squint.png`.
- Candidate output: `reference_setup/긴다리거미게_할아버지_reference_candidate_v5_squint_elderly_nasolabial_folds.png`
- Intent: `precise-object-edit`; preserve the approved v2 design while changing the lower face into an unmistakably elderly male grandfather face.

### Revision 4 Locks

- State the age category directly: elderly male, old man, grandfather, approximately 70s–80s in stylized character terms; absolutely not a baby, child, or ageless cute mascot face.
- Keep the approved warm crescent squints, white bushy eyebrows, round glasses, and gentle expression.
- Use the existing small central nose as the anatomical anchor. On each side, add one continuous, clearly visible nasolabial fold.
- Each fold starts beside the lower side of the nose, directly under the inner lower rim of the glasses; curves downward and outward through the cheek; and ends immediately beside the corresponding mouth corner.
- The paired lines frame the lower central face like soft parentheses or a stylized Korean `팔자` shape. They are not short dashes outside the mouth.
- Add slight soft elderly cheek heaviness inside/outside the folds so the lower face reads older, but keep it warm and child-safe rather than realistic or frail.
- Folds remain present across front, 3/4, side, calm, laughing, surprised, and thoughtful face views, transformed correctly with perspective and expression.
- Preserve the exact v2 eyes, glasses, mouth expressions, shell, moss, body, legs, claws, scarf, cane, palette, layout, detail panels, and painterly finish.

### Revision 4 Prompt

```text
Use case: precise-object-edit
Asset type: revised official character reference sheet for the Sherlock Fin children's picture-book series
Primary request: Transform only the lower facial age cues of the character in Image 1 so his face reads UNMISTAKABLY as an ELDERLY MALE OLD MAN and GRANDFATHER, approximately 70s–80s in a warm stylized children's-book way. He must not look like a baby-faced cute mascot with added decorative lines. Add true, clearly placed NASOLABIAL FOLDS (smile folds / Korean 팔자주름), not short wrinkles outside the mouth.
Input images: Image 1 is the user-approved squint-eye v2 edit target and visual truth for all eyes, identity, layout, body, props, textures, colors, and finish. Do not use or imitate rejected v3 or v4.
Change: Keep the existing small central nose. On EACH side of the nose, draw ONE CONTINUOUS, clearly visible curved nasolabial fold. Each fold must START directly beside the lower side of the nose underneath the inner lower rim of the round glasses, curve downward and outward through the cheek, and END immediately beside the matching mouth corner. The left and right folds should frame the lower central face like a pair of soft parentheses or a clear stylized 팔자 shape. Add mild soft elderly cheek heaviness along these folds so the lower face reads as an old man's face. These are long nose-to-mouth folds, NOT short smile dashes placed outside the mouth. Make them visible when the full sheet is shown at conversation-preview size. Preserve the folds in front, 3/4, side, gentle, laughing, surprised, and thoughtful views with correct perspective and expression.
Style: warm, kind, dignified elderly grandfather in a children's picture-book illustration. Clearly old, but healthy, safe, gentle, and cheerful—not frail, frightening, sad, or photorealistic.
Constraints: Preserve exactly the v2 warm crescent squints, closed laughing eyes, modest surprise eyes, white bushy eyebrows, round glasses, existing nose, mouth shapes, canvas ratio, sheet layout, view order, triangular stone-brown carapace, shell texture, moss shape and placement, long thin leg anatomy, small claws, plaid scarf, cane, colors, lighting, background decoration, detail panels, and soft painterly finish. Change only the paired nose-to-mouth nasolabial folds and the minimum lower-cheek shaping needed for a clear elderly male face.
Avoid: baby face, child face, ageless mascot face, short isolated lines outside the mouth, crow's feet as a substitute, forehead wrinkles as a substitute, moustache, beard, toothless caricature, extreme sagging jowls, sickly or exhausted expression, frightening realism, altered eyes or glasses, altered body or props, missing or extra limbs, text, labels, arrows, watermark, or unrelated episode content.
```

### Revision 4 QA

- [x] Face reads unmistakably as an elderly male grandfather at preview size.
- [x] One continuous fold per side starts beside the nose and ends at the mouth corner.
- [x] Folds are true paired nasolabial/팔자 folds, not outer-mouth smile dashes.
- [x] Slight cheek heaviness supports age without frailty or disturbing realism.
- [x] Approved v2 squints and every non-lower-face invariant remain stable.
- [x] No text or unrelated contamination.

### Revision 4 Result

- Candidate: `긴다리거미게_할아버지_reference_candidate_v5_squint_elderly_nasolabial_folds.png`
- Status: `USER APPROVED / active official reference`
- SHA-256: `5FC6E1CD49CD034662031DAC58B660DA97E4622789608D1FA9A84583B31FA274`
- Size: `1448 x 1086 PNG`
- Promoted to active official reference: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`.
- Candidate and official copy share SHA-256 `5FC6E1CD49CD034662031DAC58B660DA97E4622789608D1FA9A84583B31FA274`.
- Rejected v3 and v4 remain preserved as `FAIL / do not use` history.

## Next Gate

Reference gate complete. The golden-trail reference and grandfather v5 are both accepted official references. Proceed to Batch 1 pages `00`-`03`; stop for user page QA before Batch 2.
