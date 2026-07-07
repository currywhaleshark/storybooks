# Batch 3 Prompt Plan - 아루는 안 나올 거야

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. Approved final pages may be used only as continuity locks, not as replacements for official character references.

## Batch 3 Scope

1. `07_candidate_text_v1.png`
2. `08_candidate_text_v1.png`
3. `09_candidate_text_v1.png`

Stop after these three candidates for QA. Do not promote anything to `final` until the user approves the batch.

## Approved Carry-Forward Locks

- Batch 1 final pages promoted:
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/00_표지.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/01_진흙놀이.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/02_씻을_시간.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`
- Batch 2 final pages promoted:
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/04_바뀌는_건_어렵지.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/05_방울이가_먼저_첨벙.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`
- Water tub lock:
  - Use `work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png` as the recurring prop reference.
  - The tub is a low toddler-safe shell basin with warm clear shallow water, a peach-coral scalloped rim, cream/sand shell body, soft bubbles, and no bathroom fixtures.
- Aru continuity lock:
  - Use official Aru references for identity and final page 06 for the approved in-water state.
  - Keep Aru soft cream-yellow with muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf, and no school bag.
  - Avoid saturated orange Aru and blue scarf.
  - Aru must never gain hands, feet, legs, arms, a human torso, separate lower body, or grabbing fingers.
- Emotional lock:
  - Page 07 is joyful water-play absorption.
  - Page 08 mirrors page 03, but in the opposite transition direction: Aru resists leaving water because changing states is hard, not because Aru is naughty.
  - Page 09 is Aru's own realization. Do not make Mari teacher reveal the lesson first.
- No-bag lock: no child wears a school bag in water-play scenes.
- Contamination lock: do not use failed, held, or unnecessary local repair candidates as visual truth.

## Shared Style

- Format: A5 portrait, about `1:1.414`.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Text: generate illustration and exact Korean story text together on the first pass.
- Text panels: clean cream or pale-sand narration area, readable dark brown Korean text, no pseudo-writing.
- No local text overlay unless a separate text repair pass is explicitly needed after QA.

## Page 07 - 첨벙첨벙 신나는 물놀이

### Output

`07_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/05_방울이가_먼저_첨벙.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 07
Primary request: Create page 07 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru, Banguli, and Mari teacher references as character identity truth. Use final pages 05-06 only for continuity of the shell tub, Aru's in-water color/scarf, and warm shallow water-play mood.

Scene/backdrop: warm Coral Town Daycare washing/water-play corner. The approved shell tub is shallow, low, toddler-safe, pastel shell-shaped, filled with warm clear water, soft bubbles, and no bathroom fixtures.

Main action: Aru is now fully absorbed in joyful water play. Aru floats safely in the shallow shell tub, smiling with delighted eyes, bubbles on the head, water droplets bouncing around the round body, and the red-white scarf still visible. Banguli plays nearby, smaller than Aru, happily splashing. Mari teacher watches warmly nearby from a gentle distance, not interrupting.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Aru is cleaner than page 05 but may have tiny fading mud traces washing away. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, or school bag.

Banguli lock: pale sky-blue transparent water droplet with simple happy face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, toy, or animal.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Warm observer posture; no scolding, grabbing, dragging, pulling, or shaming.

Composition/framing: lively medium-wide tub scene with Aru and Banguli as the focus. Keep the text panel clean and readable without covering Aru's face, bubbles, Banguli, or the tub rim.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

아루는
신이 났어요!

첨벙첨벙!
보글보글!

거품을 머리에
얹어 보고,

물방울을
통통 튀기고,

둥근 몸을
둥실둥실.

"물놀이
완전 재밌다!"

Constraints: joyful water play, shallow warm safety, no rough splashing, no deep-water feeling.
Avoid: deep pool, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, Aru hands/feet/legs/body, teacher forcing, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 08 - 안 나올래! 더 할래!

### Output

`08_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/03_안_씻을래.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 08
Primary request: Create page 08 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru, Mari teacher, and Banguli references as character identity truth. Use final page 03 only as mirror-reference for cute transition resistance, and final page 06 for in-water Aru color/scarf and tub continuity.

Scene/backdrop: same warm Coral Town Daycare shallow shell tub washing/water-play corner. The water remains warm, clean, shallow, and safe.

Main action: A little later, Mari teacher gently says it is time to come out. Aru resists leaving the tub. Mirror page 03 emotionally: cute defensive transition resistance, but now the direction is leaving water. Aru presses the round pufferfish body firmly against the inside edge of the shell tub, saying no with a pout, but does not use hands or arms. Small spikes lift slightly, not sharply. Banguli nearby looks surprised but kind.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Aru is wet and mostly clean after water play. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, grabbing fingers, or school bag.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Mari is patient and gentle, not towering, not scolding, not grabbing, not pulling Aru from the tub.

Composition/framing: emotional medium shot focused on Aru inside the tub and Mari nearby. Show the body pressed to the tub rim using Aru's round body only. Keep text panel clear and readable.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

조금 뒤,
마리 선생님이 말했어요.

"아루야,
이제 나올 시간이야."

그러자 아루는—

"싫어!
안 나올래!

더 할래!"

둥근 몸으로
물통에 딱—

"조금만 더
놀 거야!"

Constraints: transition resistance, not bad behavior. Aru refuses with cute self-protection; Mari stays warm and non-forcing.
Avoid: Aru hands/arms/grabbing, teacher pulling, teacher scolding, deep pool, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 09 - 어? 아까는 들어가기 싫었는데

### Output

`09_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 09
Primary request: Create page 09 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru and Banguli references as character identity truth. Use final page 06 only for in-water Aru color/scarf and tub continuity.

Scene/backdrop: close warm realization moment in or beside the approved shallow shell tub. Keep the environment simple and quiet so Aru's face carries the page.

Main action: Aru suddenly pauses and realizes the pattern: earlier entering the water was hard, now leaving is hard. This realization belongs to Aru. Aru's eyes become round and thoughtful, mouth small like `어?`, spikes soften rather than flare. Banguli watches nearby quietly. Mari teacher should be absent or very small/background only; do not visually make Mari explain the lesson.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Aru is wet and mostly clean. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, or school bag.

Banguli lock: pale sky-blue transparent water droplet with simple attentive face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, toy, or animal.

Composition/framing: close-up or medium-close of Aru in the shell tub, with a quiet pause feeling. Use clean negative space for the text panel, with no overlap on Aru's eyes, mouth, spikes, or Banguli.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

그러다
아루는

멈칫—

"어?"

"아까는
씻기 싫다고
했는데……"

"지금은
나오기 싫네?"

아루는 눈을
동그랗게 떴어요.

"내 마음이
바뀌기 어려웠나 봐."

Constraints: Aru owns the insight. The page should feel gentle, thoughtful, and self-aware.
Avoid: Mari explaining the lesson, teacher pointing, Aru hands/feet/legs/body, deep pool, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```
