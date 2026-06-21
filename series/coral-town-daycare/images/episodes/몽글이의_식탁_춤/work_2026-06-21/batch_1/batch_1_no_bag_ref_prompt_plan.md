# Batch 1 No-Bag Reference Rework Prompt Plan - 2026-06-21

## Scope

- Keep approved cover: `00_cover_candidate_v1.png`.
- Regenerate page 01, page 02, and page 03 only.
- New candidate names:
  - `01_candidate_text_v5_nobagref_v1.png`
  - `02_candidate_text_v3_nobagref_v1.png`
  - `03_candidate_text_v3_nobagref_v1.png`

## Reference Policy

- Use official no-bag indoor character reference sheets from `series/coral-town-daycare/references/characters/no_bag/`.
- Do not use strong repeated negative bag-removal prompts as the main method. Use the no-bag references positively.
- Text QA is deferred to the user. Do not add local text panels or opaque text overlays.

## Shared Locks

- A5 portrait page, Korean toddler picture-book watercolor and colored-pencil style.
- Official dining room reference: `series/coral-town-daycare/references/배경_식당.png`.
- Same table continuity across pages 01-03:
  - central round/shell toddler table
  - same 3/4 front camera angle
  - same table direction and chair positions
  - same shell plates, soup bowls, water cups, small side dishes
- Character locks:
  - Mongle: purple octopus child, yellow beret, sailor collar, eight visible tentacles.
  - Aru: one round orange/beige pufferfish body, side fins only, no arms, no hands, no legs, no snowman stacking.
  - Lulu: coral-red seahorse, long tube snout, high crest, green coral hair ornament, curled tail, cream sailor top and pink skirt.
  - Sua: purple seahorse, long tube snout, high crest, dotted texture, curled tail, blue sailor outfit.
  - Popo: translucent moon jellyfish, essentially no eye marks; use tiny mouth/internal markings for expression.
- No body-worn bags at the dining table.

## Page 01 Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 01

Primary request: Regenerate page 01 of `몽글이의 식탁 춤` using the no-bag indoor character reference sheets as visual truth. Focus on character reference fidelity and stable table continuity.

Input images: dining-room background reference; no-bag indoor character reference sheets for Mongle, Mari teacher, Banguli, Jun-i, Aru, Lulu, Sua, Tori, and Popo.

Scene/layout: lunchtime at Coral Town Daycare. One central round/shell toddler table in a consistent 3/4 front view. Use this as the table layout anchor for pages 02 and 03. Shell plates, seaweed soup bowls, water cups, and small side dishes are neatly arranged.

Main action: Mongle enters or reaches the dining table, excited that lunch has begun. His eight octopus tentacles wiggle joyfully while he stays cute and safe.

Supporting characters: friends gather around the same table. Preserve silhouettes even if simplified. Aru is a single round pufferfish with fins only. Lulu and Sua are clearly seahorses with long tube snouts and curled tails. Popo is eyeless translucent jellyfish. No worn bags.

Text: include the original page 01 Korean story text in the image, integrated into open cream space or clean margin. Do not add an opaque panel.

Avoid: snowman Aru, Aru hands/arms/legs, generic fish Lulu/Sua, missing seahorse snouts or curled tails, Popo black eyes, worn bags, changed table layout, text overlay panel, watermark.

## Page 02 Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 02

Primary request: Regenerate page 02 using the same no-bag references and the same table setup as page 01.

Input images: dining-room background reference; no-bag indoor character reference sheets for Mongle, Banguli, Aru, Lulu, and any visible nearby friends.

Scene/layout: same central round/shell toddler table, same 3/4 front camera, same chair positions and tableware arrangement as page 01. Children are now seated and eating.

Main action: Mongle sits on a low chair. One octopus tentacle gently rises toward the tabletop, one taps the chair, and the other tentacles wiggle below because he is excited. Keep eight tentacles, yellow beret, sailor collar, and official body.

Supporting characters: nearby friends eat calmly or glance over. Aru, if visible, remains one round pufferfish with fins only and no hands. Lulu, if visible, remains coral-red seahorse with snout, crest, ornament, curled tail, top, and skirt. No worn bags.

Text: include the original page 02 Korean story text in the image. Do not add a separate text panel.

Avoid: table drift from page 01, Aru hands/arms, snowman Aru, generic Lulu, missing Lulu snout/crest/tail, full spill, angry faces, worn bags, watermark.

## Page 03 Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 03

Primary request: Regenerate page 03 using the same no-bag references and the same table setup as pages 01-02.

Input images: dining-room background reference; no-bag indoor character reference sheets for Mongle, Mari teacher, Banguli, Aru, and Sua.

Scene/layout: same central round/shell toddler table, same 3/4 front camera, same table direction and tableware. This is a closer action moment but still the same dining setup.

Main action: Mongle playfully rolls a round rice ball with one tentacle and gently stirs seaweed soup with another; other tentacles wiggle. Keep the moment cute, not chaotic. No full spill yet.

Supporting characters: Aru and Sua notice with soft concern. Aru is one round pufferfish with fins only, no hands. Sua is purple seahorse with long snout, high crest, curled tail, blue sailor outfit. Mari approaches gently. No worn bags.

Text: include the original page 03 Korean story text in the image. Do not add a separate text panel.

Avoid: table drift, Aru hands/arms, snowman Aru, generic Sua, missing Sua snout/crest/tail, full spill, angry teacher, shaming friends, worn bags, watermark.

## Stop Notes Before Next Attempt - 2026-06-22

- Stop this generation thread here; page 03 began drifting from the storybook context.
- Fix for next page 01: Mongle should not already be on/over the table. He should be entering, beside the table, or at his chair while excited.
- Fix for next page 02: Mari teacher should not be seated/eating with the children. She should be absent from the seats, supervising, serving, or off-frame.
- Continuity fix for later dining-room pages: because all friends are seated in page 01, keep friends naturally seated in later pages even if the page-specific prompt only names a subset for reference QA.
