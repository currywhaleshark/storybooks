# Batch 1 Prompt Plan - 수아의 잘 보는 눈 - 2026-06-24

## Scope

- Episode: `수아의 잘 보는 눈 — 다 똑같지 않아서 좋아요`
- Series: `coral-town-daycare`
- Script: `series/coral-town-daycare/sua-different-is-good/script/main.md`
- Page plan: `series/coral-town-daycare/sua-different-is-good/script/pages.json`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work folder: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/batch_1`
- Candidate filenames: `00_candidate_text_v3.png`, `01_candidate_text_v4.png`, `02_candidate_text_v1.png`, `03_candidate_text_v1.png`

## Official References

- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Lulu no-bag: `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
- Special coral hairpin: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/special_coral_hairpin_ref_v1.png`
- Approved Lulu with special hairpin: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Sua no-bag (if needed): `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`

## Shared Hard Locks

- A5 portrait page proportion, about `1:1.414`.
- Generate illustration and exact Korean story text together.
- Use actual official reference image files as visual truth, not prose descriptions alone.
- Keep a clean, readable text area. If exact Korean text cannot be cleanly rendered, leave a clean blank text area rather than inventing wrong text.
- Style: soft toddler picture-book watercolor and colored-pencil texture, warm paper feel, low-saturation pastel palette.
- Avoid neon colors, harsh highlights, plastic 3D toy texture, dense props, scary expressions, pseudo-writing, extra signs, random labels, human legs/feet, and unrelated previous episode details.
- Same-face repetition is forbidden. Characters must have distinct eyes, mouths, postures, and rhythms.
- Preserve the delicate painted reference style for every character. Do not simplify characters into generic round sea-animal children; keep each reference's texture, ridges, fins, tentacles, clothing seams, collars, scarves, and ornaments.

## Sua / Lulu Detail Locks

- Sua is a small purple seahorse child. Preserve the actual `수아.png` design: slender purple seahorse body, dotted/spiny head ridge, long tube snout, small black button eyes, blue sailor collar and skirt, curled tail, small fins, mint bag when specified. Do not turn Sua into a generic purple child, fish, or blob.
- Lulu is a pink seahorse child. Preserve the actual `루루.png` design: coral-pink body, long tube snout, small black button eyes, dotted/ridged skin texture, crown-like spiny head ridge with small bead tips, cream sailor top with pink collar and scarf, mauve pleated skirt, translucent pink back fin, curled tail, yellow bag when specified. Do not simplify her into a generic pink child or round doll.
- Episode special hairpin lock: when this story calls for Lulu's coral ornament, use the new mint/aqua coral hairpin with a cream star-shell and pale-yellow bead nubs from `special_coral_hairpin_ref_v1.png`. It is a special one-day accessory, more noticeable than her ordinary ornament, and must not be recolored pink.
- Cover continuity lock: because the cover shows the lost hairpin in the sand, Lulu must not also be wearing that special hairpin on the cover. Only one special mint/aqua star-shell hairpin may appear, and it must be the loose foreground prop.
- When both appear, their seahorse features must stay distinct: snouts, ridges, curled tails, and fin shapes should remain reference-like even at small scale.
- Hat/clothing preservation lock for page 01 v4: Mongle must keep his yellow beret and sailor collar; Tori must keep his yellow hat/helmet and turtle shell. Bag bans must not remove fixed hats or clothing.

## Mari / Banguli Detail Locks

- Mari teacher: half-up bob, star hairpin, cream blouse, yellow apron, name tag, purple mermaid tail, warm brown eyes. Not a generic mermaid or human teacher.
- Banguli: pale sky-blue transparent droplet shape, small simple face, soft sheen and transparency. No hard plastic look, no shiny highlights. Two or three tiny droplets float nearby.

## Bag Rule for Batch 1

- These first four pages are classroom and playground scenes. Do not put mint bag or yellow bag strictly on character bodies in batch 1 unless the prompt clearly calls for it. If a bag must appear, place it on a hook, cubby, or nearby shelf instead.

## Page 00 - Cover

### Output

`00_candidate_text_v3.png`

### References To Load

- `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/special_coral_hairpin_ref_v1.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_전경과_놀이터.png`

### Exact Page Text

```text
수아의 잘 보는 눈

— 다 똑같지 않아서 좋아요 —
```

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `수아의 잘 보는 눈` in A5 portrait proportion.
Input images: load the official Sua, official Lulu no-bag for identity only, standalone special coral hairpin, Banguli, and playground references as visual truth. Cover continuity lock: Lulu has lost the special hairpin, so the only special mint/aqua star-shell hairpin in the entire cover must be the loose prop in the foreground sand. Lulu must not wear the special hairpin on her head.

Scene: bright and warm playground edge near the daycare. Sua, a small purple seahorse child, is the foreground focus. She lowers her head slightly and looks closely at something tiny in the sand — Lulu's special mint-and-cream coral hairpin with a cream star-shell — with her small eyes sparkling in quiet focus. Preserve official Sua features: slender purple seahorse body, dotted/spiny head ridge, long tube snout, small black button eyes, blue sailor outfit, curled tail, small fins, mint bag and tiny observation tube at her side. Banguli, a pale sky-blue transparent droplet, floats nearby and looks in too, with two or three tiny droplets. In the background, Lulu appears softly as a pink seahorse child; keep her gentle and secondary so she does not compete with Sua. The loose hairpin must match `special_coral_hairpin_ref_v1.png`.

Composition/framing: cover layout with clean title space at the top and subtitle space near the bottom. Sua and the tiny sand detail are the visual center. Perspective is child-height and warm.

Text (verbatim): render exactly:

수아의 잘 보는 눈

— 다 똑같지 않아서 좋아요 —

Constraints: pastel watercolor and colored-pencil picture-book style. No neon colors, harsh highlights, plastic 3D texture, scary features, pseudo-writing, random labels, unrelated episode details, or human legs/feet.
```

## Page 01 - 루루는 반짝반짝

### Output

`01_candidate_text_v4.png`

### References To Load

- `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/준이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/토리_no_bag.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`

### Exact Page Text

```text
루루는 오늘도
반짝반짝.

분홍빛 몸에
산호 장식.

"우와, 루루
공주님 같다!"
"루루 진짜 예쁘다!"

친구들이
모여들었어요.

수아는 멀리서
가만히 봤어요.
```

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `수아의 잘 보는 눈` in A5 portrait proportion.
Input images: loaded approved Lulu-with-special-hairpin reference, official no-bag Sua, no-bag Jun-i, no-bag Mongle with his yellow beret preserved, no-bag Tori with his yellow hat preserved, Banguli, and classroom references are the visual truth. Page 01 continuity lock: this is before Lulu loses the accessory, so the special mint/aqua star-shell hairpin appears only on Lulu's head; do not draw it as a loose object elsewhere.

Scene: free play time in the daycare classroom. Lulu, a bright pink seahorse child wearing the special mint/aqua coral hairpin with a cream star-shell, is smiling warmly among friends. Jun-i, Mongle, and Tori gather around her and say she is pretty and like a princess. Do not include Aru on this retry, because the previous candidate gave Aru a human-like body, hands, and feet. Lulu is not arrogant — she is kind and simply bright. On the other side, Sua watches quietly from a little distance. She lowers her head slightly and looks down at her own purple body with quiet longing, not heavy sadness. Banguli floats beside Sua with two or three tiny droplets.

Composition/framing: medium-wide classroom view with a soft blocked-text area on one side. Place the friend group and Lulu on one side and Sua on the opposite side so the contrast reads clearly but both remain sweet. Keep rounded windows and shell decorations visible as background hints only.

Text (verbatim): render exactly:

루루는 오늘도
반짝반짝.

분홍빛 몸에
산호 장식.

"우와, 루루
공주님 같다!"
"루루 진짜 예쁘다!"

친구들이
모여들었어요.

수아는 멀리서
가만히 봤어요.

Constraints: keep all characters reference-like. Do not include Aru or any pufferfish child on this v4 retry. Keep Lulu and Sua as seahorse children, Jun-i as shark child, Mongle as octopus child with his yellow beret and sailor collar, Tori as turtle child with his yellow hat/helmet and turtle shell, and Banguli as droplet friend. Avoid same-face repetition. Forbid only child-worn backpacks, shoulder bags, cross-body bags, satchels, and bag straps; do not remove fixed hats, shells, collars, or clothing. No neon colors, harsh highlights, human legs/feet, or unrelated previous episode details.
```

## Page 02 - 나도 루루처럼 되면 좋겠다

### Output

`02_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`

### Exact Page Text

```text
수아는
거울 앞에 섰어요.

거울 속에는
가는 보라색 몸,
작은 눈.

"나도 루루처럼
분홍빛이면
좋겠다."

"나도 눈이
크면 좋겠다."

수아는 작게
한숨을 쉬었어요.
```

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `수아의 잘 보는 눈` in A5 portrait proportion.
Input images: load the official Sua, Banguli, and classroom references as visual truth.

Scene: Sua stands in front of the classroom mirror corner. She looks at her reflection — a slender purple seahorse child with a thin body and small eyes. She lets out a small, quiet sigh and thinks she wishes she could be pink like Lulu, and that her eyes were bigger. Her curled tail tightens inward slightly. Banguli watches gently beside her.

Composition/framing: mirror-front medium shot with soft text area on one side. Show both Sua and her reflection clearly. Keep the mirror corner background simple so the emotional focus stays on her quiet expression and self-view.

Text (verbatim): render exactly:

수아는
거울 앞에 섰어요.

거울 속에는
가는 보라색 몸,
작은 눈.

"나도 루루처럼
분홍빛이면
좋겠다."

"나도 눈이
크면 좋겠다."

수아는 작게
한숨을 쉬었어요.

Constraints: preserve Sua's official seahorse shape, snout, ridge, and curled tail. Avoid generic purple-child simplification. Use soft pastel tone. No neon colors, harsh highlights, or unrelated episode details.
```

## Page 03 - "수아도 예뻐"가 안 들려요

### Output

`03_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`

### Exact Page Text

```text
루루가 다가왔어요.

"수아야,
너도 예뻐!"

수아는
고개를 저었어요.

"아니야……"

루루는 진심이었지만,
수아한테는
잘 들리지 않았어요.

"나는 루루처럼
예쁘지 않은걸."
```

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `수아의 잘 보는 눈` in A5 portrait proportion.
Input images: load the official Lulu no-bag, special coral hairpin, Sua, and Banguli references, plus the classroom reference, as visual truth.

Scene: Lulu, still wearing her special mint/aqua coral hairpin with a cream star-shell, comes close to Sua and says sincerely, "You are pretty too!" But Sua shakes her head gently. The comfort does not reach her because the measure is still beauty-in-the-same-way. Keep Lulu kind, not mean. Sua looks quiet and muffled, with her curled tail still tightly curled. Banguli tilts nearby, unsure.

Composition/framing: two-shot or close medium shot between Lulu and Sua, with emotional distance clear but gentle. Soft classroom background. Clean text area on one side.

Text (verbatim): render exactly:

루루가 다가왔어요.

"수아야,
너도 예뻐!"

수아는
고개를 저었어요.

"아니야……"

루루는 진심이었지만,
수아한테는
잘 들리지 않았어요.

"나는 루루처럼
예쁘지 않은걸."

Constraints: preserve both official seahorse faces and reference features. Do not make either character generic or round-child-like. Keep the mood tender, not heavy. No neon colors, harsh highlights, or unrelated episode details.
```













