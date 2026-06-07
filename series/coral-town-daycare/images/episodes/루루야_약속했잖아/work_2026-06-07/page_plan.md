# Page Plan - 루루야, 약속했잖아

## Episode

- Script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아.md`
- TTS script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아_tts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07`
- Final folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final`
- Page format: A5 portrait, about `1:1.414`
- Text workflow: generate illustration and exact Korean story text together on the first pass.

## Locked References

- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`

## Episode-Specific References To Create

- Lulu's favorite picture book: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`
- Messy art-time state: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/messy_art_time_state_ref.png`
- Reference plan: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/reference_asset_plan.md`

## Character Fidelity Locks

- Lulu must be built from the actual `루루.png` reference: coral-pink seahorse child, crown-like spiny head ridge with bead tips, dotted/ridged seahorse texture, long tube snout with round opening, small black eyes, coral-and-shell head ornament, cream sailor top with pink collar/scarf, mauve pleated skirt, translucent pink back fin, curled seahorse tail.
- Do not simplify Lulu into a generic pink fish, mermaid, human child, flat cartoon mascot, or smooth low-detail seahorse. No human legs or feet.
- Sua must be built from the actual `수아.png` reference even when small in the background: purple slender seahorse child, spiny dotted head ridge, long tube snout, small black eyes, blue sailor collar and skirt, curled tail, small fins. Do not turn Sua into a generic purple child or fish.
- Aru must remain a true round orange pufferfish body with small spikes, little fins, pufferfish mouth, and sailor scarf. Never add human hands, human feet, human legs, or a human-like torso.
- Popo must remain the moon jellyfish child from `포포.png`: translucent rounded dome, subtle inner pattern, small sailor collar, soft long tentacles, childlike floating proportion. Do not shrink Popo into a tiny generic jellyfish.
- Jun-i must remain a blue shark child with white belly, dorsal fin, shark tail, small teeth, and sailor outfit. Avoid glove-like human hands or ordinary human legs.
- Banguli is a soft pale sky-blue transparent droplet mascot with a simple face and tiny companion droplets, not a jellyfish, glass bead, crystal, or hard plastic toy.
- Bags are omitted from bodies unless the scene is arrival/departure or the script specifically mentions a bag. For batch 1 indoor classroom scenes, bags should be omitted or placed in storage such as cubbies, hooks, shelves, or beside a chair.

## Batch Split

### Batch 1

- `00_표지.png`: Lulu and Jun-i make a warm promise in the classroom.
- `01_페이지.png`: Lulu chatters through free play; friends play around her.
- `02_페이지.png`: Lulu lends her favorite picture book to Jun-i and asks for a promise.
- `03_페이지.png`: Lulu finds Jun-i forgot the promise; the book lies on the floor.

### Batch 2

- `04_페이지.png`: Lulu calmly tells Jun-i that promises are meant to be kept.
- `05_페이지.png`: Afternoon art play becomes messy and exciting.
- `06_페이지.png`: Lulu quickly promises to clean everything up.

### Batch 3

- `07_페이지.png`: Cleanup time arrives, but Lulu delays.
- `08_페이지.png`: Jun-i gently reminds Lulu of her own promise.
- `09_페이지.png`: Lulu quietly realizes she also made a promise.

### Batch 4

- `10_페이지.png`: Lulu starts cleaning and Jun-i helps.
- `11_페이지.png`: Mari teacher shows the softly glowing heart shell.
- `12_페이지.png`: Lulu thinks before making a new promise.

## Batch 1 QA Notes

- Batch 1 is reference-fidelity sensitive because Lulu is large in all pages and Sua appears as a smaller background friend on page 1.
- Batch 1 v1 candidates are on hold after user QA: bags were worn in non-arrival scenes, page 1 simplified Aru/Popo, and several characters lost the delicate reference style.
- Batch 1 v2/v3 candidates are also on hold after user QA on 2026-06-08: the cast still became too round compared with the references, Aru gained a separate attached body/torso, and Popo was drawn with visible eyes despite no special eye-expression direction.
- Pages 2 and 3 must use the same picture book prop once `lulu_favorite_picture_book_ref.png` is generated.
- For page 1, if the model cannot preserve all friends clearly, prioritize Lulu, Sua, and overall classroom readability over filling the page with many small faces.
- Keep the classroom from the official reference as a soft background only; characters and text must remain readable.
- Avoid unrelated details from prior episodes, extra signs, pseudo-writing, random labels, worn bags in non-arrival scenes, human legs/feet, and harsh conflict expressions.
- Next retry must prioritize reference silhouette over cuteness: keep sharper species-specific structure, do not over-round the characters, keep Aru as one pufferfish body with scarf only, and keep Popo's eyes hidden unless the page explicitly asks for eye expression.

## Later Batch Continuity Notes

- Pages 5 through 9 should share the same messy art-time state once `messy_art_time_state_ref.png` is generated.
- Page 10 should show the same mess being cleaned up, not a new unrelated mess.
