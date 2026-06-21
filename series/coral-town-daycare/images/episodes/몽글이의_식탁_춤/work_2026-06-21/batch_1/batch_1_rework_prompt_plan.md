# Batch 1 Rework Prompt Plan - User QA 2026-06-21

## Scope

- Keep approved cover: `00_cover_candidate_v1.png`.
- Regenerate page 01, page 02, and page 03 only.
- New candidate names:
  - `01_candidate_text_v3_reflock.png`
  - `02_candidate_text_v2_reflock.png`
  - `03_candidate_text_v2_reflock.png`

## User QA To Fix

- Do not add local text panels or post-generation text overlays. The user will QA text.
- Page 01: Aru became snowman-like instead of one round pufferfish body. Sua and Lulu drifted from their references.
- Page 02: table placement changed from page 01. Aru gained hands. Lulu details drifted from reference.
- Page 03: Aru gained hands. Sua details drifted from reference.

## Rework Locks

- Visual fidelity outranks text repair in this pass.
- Keep generated story text in the image, but do not add a separate opaque text box or panel over the art.
- Same dining table continuity across pages 01-03:
  - Use one central round/shell toddler table in the foreground/midground.
  - Keep a consistent 3/4 front camera angle.
  - Keep the same table direction, chair/stool positions, shell plates, soup bowls, cups, and small side dishes.
  - Do not rotate the table or replace it with a different dining setup between pages.
- Indoor no-bag lock remains active: no character wears a bag at the dining table.
- Character reference locks:
  - Aru: one round beige pufferfish body, black spots on top, tiny spikes/bumps, side fins only, duck-like small mouth. No separate torso, no snowman stacking, no arms, no hands, no legs.
  - Sua: purple seahorse child, long tube snout, high ridged crest, dotted texture, small arms only if needed, curled seahorse tail, blue sailor outfit. No generic fish face, no missing snout, no bag.
  - Lulu: coral-red seahorse child, long tube snout, high ridged crest, green coral hair ornament, curled seahorse tail, cream sailor top and pink skirt. No generic fish face, no missing crest, no bag.
  - Mongle: purple octopus child with eight visible tentacles, yellow beret, sailor collar, round head.

## Page 01 Rework Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 01

Primary request: Regenerate page 01 of `몽글이의 식탁 춤` as an A5 portrait page, correcting character-reference fidelity and keeping the dining table setup stable for pages 01-03.

Official visual truth: dining room reference, Mongle reference, Mari teacher reference, Banguli reference, Jun-i reference, Aru reference, Lulu reference, Sua reference, Tori reference, Popo reference.

Scene and layout: lunchtime at Coral Town Daycare. Use one central round/shell toddler table, seen from the same 3/4 front camera angle that will be reused for pages 02 and 03. Keep the table direction fixed, with shell plates, soup bowls, water cups, small side dishes, and pastel stools consistently arranged.

Main subject: Mongle is central and excited, with eight visible octopus tentacles wiggling joyfully. Preserve the official purple round head, yellow beret, sailor collar, and toddler octopus body.

Supporting characters: show friends around the same table, but simplify crowding if needed to preserve silhouettes. Aru must be one round beige pufferfish body with side fins only, no arms or hands. Sua must remain a purple seahorse with long tube snout, high ridged crest, dotted texture, curled tail, and blue sailor outfit. Lulu must remain a coral-red seahorse with long tube snout, high ridged crest, green coral ornament, curled tail, cream sailor top, and pink skirt. No worn bags.

Text: include the original page 01 Korean story text in the image. Keep text integrated in open cream page space or a clean margin. Do not add an opaque panel over characters or cover the illustration.

Avoid: local text overlay look, large panel box, snowman-shaped Aru, Aru hands, Aru arms, human limbs on sea creatures, generic fish redesigns, missing seahorse snouts, missing curled tails, worn bags, different table layout, watermark.

## Page 02 Rework Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 02

Primary request: Regenerate page 02 with the same dining table setup as page 01 and stronger Aru/Lulu reference fidelity.

Official visual truth: dining room reference, Mongle reference, Banguli reference, and visible friend references including Aru and Lulu.

Scene and layout: same central round/shell toddler table, same 3/4 front camera angle, same stool/tableware arrangement as page 01. Children are now seated and eating. Do not rotate or redesign the table.

Main subject: Mongle sits on the low chair at the same table. One octopus leg gently reaches toward the tabletop, one taps the chair, and other tentacles wiggle below. Keep eight visible tentacles, yellow beret, sailor collar, and purple octopus identity.

Supporting characters: nearby friends eat calmly or glance over. Aru, if visible, is a single round beige pufferfish with side fins only and no hands. Lulu, if visible, is the coral-red seahorse with long tube snout, ridged crest, green coral ornament, curled tail, cream sailor top, and pink skirt. No worn bags.

Text: include the original page 02 Korean story text in the image. No separate text-panel repair, no opaque overlay covering art.

Avoid: Aru hands, Aru arms, snowman-body Aru, generic fish Lulu, missing Lulu snout/crest/tail, table layout drift from page 01, full spill, angry faces, worn bags, watermark.

## Page 03 Rework Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 03

Primary request: Regenerate page 03 with the same dining table setup as pages 01-02 and stronger Aru/Sua reference fidelity.

Official visual truth: dining room reference, Mongle reference, Mari teacher reference, Banguli reference, Aru reference, and Sua reference.

Scene and layout: same central round/shell toddler table and same 3/4 front camera angle as pages 01-02. Keep the same table direction, stools, bowls, shell plates, cups, and side dishes. Page 03 is a closer action moment but must still read as the same table.

Main subject: Mongle plays excitedly with food: one tentacle rolls a round rice ball, another gently stirs seaweed soup, other tentacles wiggle. Keep all eight tentacles and official Mongle identity. No full spill yet.

Supporting characters: Aru and Sua notice with soft concern. Aru is a round beige pufferfish body with side fins only, no arms or hands. Sua is a purple seahorse with long tube snout, high ridged crest, dotted texture, curled tail, blue sailor outfit, and no bag. Mari approaches gently from the side.

Text: include the original page 03 Korean story text in the image. No separate panel overlay or local text repair.

Avoid: Aru hands, Aru arms, snowman-body Aru, generic fish Sua, missing Sua long snout/crest/curled tail, table layout drift, full spill, angry teacher, shaming friends, worn bags, watermark.

## Rework Generation Results - 2026-06-21

- `01_candidate_text_v3_reflock.png`: generated; hold. Aru/Sua/Lulu improved, but several children still wore reference-derived bags in the dining-room scene.
- `01_candidate_text_v4_reflock_nobag.png`: current page 01 review candidate. No visible worn bags; Aru remains a round pufferfish body without hands; Sua/Lulu retain seahorse silhouettes.
- `02_candidate_text_v2_reflock.png`: current page 02 review candidate. Table setup simplified and stable; Aru has no hands; Lulu is closer to official seahorse reference.
- `03_candidate_text_v2_reflock.png`: current page 03 review candidate. Same central table direction; Aru has no hands; Sua is closer to official seahorse reference.
- Text QA intentionally deferred to user. No local text panel overlays were added.
