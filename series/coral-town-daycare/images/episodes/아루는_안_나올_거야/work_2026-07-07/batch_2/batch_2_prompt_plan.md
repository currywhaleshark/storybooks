# Batch 2 Prompt Plan - 아루는 안 나올 거야

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. User-approved Batch 1 finals may be used only as continuity locks, not as replacements for official character references.

## Batch 2 Scope

1. `04_candidate_text_v1.png`
2. `05_candidate_text_v1.png`
3. `06_candidate_text_v1.png`

Stop after these three candidates for QA. Do not promote anything to `final` until the user approves the batch.

## Approved Carry-Forward Locks

- Batch 1 final pages promoted:
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/00_표지.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/01_진흙놀이.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/02_씻을_시간.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`
- Aru color lock: use page 03/final Aru as the approved in-episode color reference, backed by official Aru sheets.
  - Soft cream-yellow body.
  - Muted tan-olive top shading.
  - Darker brown top spots.
  - Warm beige fins.
  - Red-white sailor scarf.
  - Avoid saturated orange Aru and blue scarf.
- No-bag lock: no child wears a school bag in yard, washing, or water-play scenes.
- Tone lock: Aru's resistance is transition difficulty, not bad behavior. Mari validates and waits; she never scolds, grabs, drags, or forces.
- Page 01 duplicate lock: do not duplicate characters in a single scene. If Mongle or Tori appear, use one instance only and only when the page calls for them.
- Water tub lock: use the approved shallow shell water tub reference for pages 05-06. It is a low toddler-safe shell basin with warm water, soft bubbles, and no bathroom fixtures.

## Shared Style

- Format: A5 portrait, about `1:1.414`.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Text: generate illustration and exact Korean story text together on the first pass.
- Text panels: clean cream or pale-sand narration area, readable dark brown Korean text, no pseudo-writing.
- No local text overlay unless a separate text repair pass is explicitly needed after QA.
- Contamination: do not use prior failed or held candidates as visual truth.

## Page 04 - 바뀌는 건 어렵지

### Output

`04_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 04
Primary request: Create page 04 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded official exterior/playground as setting truth. Use official Aru, Mari teacher, and Banguli references as character identity truth. Use the approved final page 03 only as continuity reference for Aru's color, mud marks, lowered transition-resistance emotion, and red-white scarf.

Scene/backdrop: warm Coral Town Daycare yard mud-play area, calmer after Aru's refusal. Soft sand-colored ground, gentle pastel mud, small play props only if unobtrusive, daycare exterior in the background.

Main action: Mari teacher lowers herself beside Aru and gently names the difficulty. She is calm and close, sitting or kneeling low, not towering. Aru stays round and still, listening. Aru's small spikes soften and lower a little; the face is quiet and guarded but less tense than page 03. Banguli floats nearby and nods gently with two or three tiny droplets.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, small spikes, pufferfish mouth, red-white sailor scarf, pastel mud marks. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, or school bag.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Warm low-pressure posture. No scolding finger, grabbing, dragging, pulling, or shaming.

Composition/framing: close or medium-close emotional two-shot of Mari beside Aru. Keep the text panel on one side with generous margins and no overlap on faces, spikes, or Banguli.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

마리 선생님이
아루 옆에 앉았어요.

"재밌게 놀다가
멈추는 거,

어려웠구나."

아루는
가만히 있었어요.

"마지막 통통 한 번,
그리고 첨벙해 볼까?"

아루의 가시가
조금 내려갔어요.

Constraints: transition validation, not discipline. Emotional safety is the priority.
Avoid: orange Aru, blue scarf, Aru hands/feet/legs/body, teacher forcing, teacher scolding, extra friends, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 05 - 방울이가 먼저 첨벙

### Output

`05_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 05
Primary request: Create page 05 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru, Mari teacher, and Banguli references as character identity truth. Use final page 03 only for Aru color/scarf continuity.

Scene/backdrop: warm Coral Town Daycare washing/water-play corner near the yard. The approved shell tub is shallow, low, toddler-safe, pastel shell-shaped, filled with warm water, soft bubbles, and no bathroom fixtures.

Main action: Mari has prepared warm water. Banguli is first inside the shallow shell tub, joyfully splashing as if inviting Aru. Aru is outside the tub, still muddy, hesitant and curious, looking at the water with a small uncertain mouth. Mari may be nearby in a gentle supporting role, but she does not pressure Aru.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf, pastel mud marks. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, or school bag.

Banguli lock: pale sky-blue transparent water droplet with simple happy face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, or toy.

Composition/framing: medium shot showing Banguli inside the shell tub and Aru just outside, hesitating. Keep the text panel on one side or top with generous margins.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

마리 선생님이
따뜻한 물을
받아 줬어요.

보글보글
거품이
몽글몽글.

방울이가 먼저
첨벙—!

'아루야,
들어와! 괜찮아!'

아루는
물을 봤어요.

"들어가도……
괜찮을까?"

Constraints: Banguli demonstrates safety and fun; Aru is hesitant, not frightened. The water is warm, shallow, and safe.
Avoid: deep pool, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, Aru hands/feet/legs/body, teacher forcing, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 06 - 어? 따뜻하고 좋네!

### Output

`06_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 06
Primary request: Create page 06 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru and Banguli references as character identity truth. Use final page 03 only for Aru color/scarf continuity.

Scene/backdrop: close warm water-play/washing moment in the approved shallow shell tub. Keep the shell tub low and safe with warm water, soft bubbles, and no bathroom fixtures.

Main action: Aru carefully enters the warm water and discovers it feels pleasant. Aru's round body floats gently in the shallow water; mud begins to wash away in soft swirls; bubbles gather around the body. Small spikes relax and lie softly. Aru's expression changes from cautious to surprised delight. Banguli shines happily nearby with tiny companion droplets.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Keep a little mud washing off, but do not make Aru saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, or school bag.

Composition/framing: medium-close view of Aru partially in the shell tub, warm water and bubbles clearly visible. Banguli nearby, smaller than Aru. Keep the text panel clean and readable without covering Aru's face, spikes, or Banguli.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

아루는 살짝
몸을 담갔어요.

"어?"

"따뜻하고……
좋네!"

진흙이
스르르 씻겨 가고,

거품이
보글보글.

작은 가시가
부드럽게 누웠어요.

Constraints: this is the first positive shift into water. Aru should look safe, surprised, and comforted.
Avoid: deep water, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, Aru hands/feet/legs/body, scary bubbles, extra characters unless needed, random text, pseudo-writing, watermark, plastic 3D texture.
```
