# Batch 1 Prompt Plan - 아루는 안 나올 거야

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. If the image generation workflow cannot use loaded image references as visual grounding, stop and report the limitation instead of generating from prose only.

## Reference Setup Status

The required reference exists and was accepted by the user on 2026-07-07:

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`

Carry-forward lock: use it as a shallow toddler-safe shell water tub with warm water. Do not let page generations reinterpret it as a deep pool, metal bathtub, sink, or bathroom fixture.

Batch 1 can start from the cover in a fresh image-generation context.

## Shared Locks

- Format: A5 portrait, about `1:1.414`.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Text: generate illustration and exact Korean story text together on the first pass.
- No local text overlay unless a separate text repair pass is explicitly needed after QA.
- Contamination: do not use prior generated images from other episodes as visual truth.
- No body-worn school bags for this episode.
- Aru: preserve official round orange pufferfish body, small spikes, small fins, pufferfish mouth, and sailor scarf. No hands, feet, legs, arms, separate human torso, or separate lower body.
- Mari: warm, patient, low-pressure daycare teacher; no scolding finger, grabbing, dragging, forcing, or princess-mermaid styling.
- Banguli: pale sky-blue transparent water droplet with simple face and tiny companion droplets.
- Safety: mud is cute and pastel, not gross; water is shallow, warm, clean, and safe.

## Generation Order

1. `00_cover_candidate_v1.png`
2. `01_candidate_text_v1.png`
3. `02_candidate_text_v1.png`
4. `03_candidate_text_v1.png`

Stop after these four candidates for QA. Do not promote anything to `final` until the user approves the batch.

## Page 00 - Cover

### Output

`00_cover_candidate_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `아루는 안 나올 거야` in A5 portrait proportion.
Input images: the loaded shallow shell water tub reference is the setting/prop truth; loaded Aru and Banguli references are character identity truth. Use the no-bag references positively for this no-bag water-play episode.

Scene/backdrop: warm Coral Town Daycare water-play/washing corner. Use the shallow shell water tub reference clearly: low, rounded, safe, warm water, soft bubbles, pastel shell shape. Not a deep pool, sink, bathtub, or bathroom.

Main subject: Aru is the foreground focus inside the shell water tub. Preserve Aru exactly as a round orange pufferfish child with small spikes, small fins, pufferfish mouth, and sailor scarf. Aru has bubbles on the head and is happily splashing, smiling with cute stubborn joy as if saying "안 나올래!" Small spikes are relaxed and the body looks comfortable. No hands, feet, legs, arms, human torso, or separate lower body.

Supporting subject: Banguli splashes nearby as a pale sky-blue transparent droplet with a simple happy face and two or three tiny companion droplets.

Composition/framing: uncluttered cover. Focus on Aru and Banguli only. Leave bright clean title space at the top and smaller subtitle space at the bottom. Keep the text away from Aru's face, spikes, and Banguli.

Text (verbatim): render exactly:

아루는 안 나올 거야

— 바뀌는 건 어렵지만,
해보면 괜찮아 —

Constraints: official-reference fidelity is more important than extra cuteness. Make Aru joyful and stubborn, not angry or scary.
Avoid: Aru with hands/feet/legs/body, scary pufferfish, deep water, bathroom fixtures, random signs, pseudo-writing, extra text, old episode imagery, watermark, plastic 3D texture.
```

## Page 01 - 진흙놀이가 제일 좋아

### Output

`01_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/토리_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are setting truth; loaded Aru, Mongle, Tori, and Banguli references are character identity truth. Use no-bag references positively; this is a mud-play scene with no school bags worn.

Scene/backdrop: bright afternoon in the Coral Town Daycare yard, mud/sand play corner. Use the official exterior/playground reference as visual truth, with soft sand-colored ground, small pastel mud puddles, tiny shovel and bucket, and gentle coral decorations. Include the coral tunnel only if it fits naturally and does not distract.

Main subject: Aru is happily absorbed in mud play, center of the page. Preserve Aru as the official round orange pufferfish child with small spikes, small fins, pufferfish mouth, and sailor scarf. Aru rolls the round body through soft pastel mud; mud marks are cute and light on the round body and between small spikes. Aru's spikes are relaxed, expression joyful and completely focused. No hands, feet, legs, arms, or separate body parts.

Supporting characters: Mongle and Tori play nearby with mud/sand in a gentle supporting role. Preserve Mongle's purple octopus shape with yellow beret and visible tentacles; preserve Tori's green turtle body, shell, and yellow hat. Banguli floats nearby as a small transparent droplet.

Composition/framing: lively medium-distance view, Aru large enough for pufferfish anatomy to be clear. Leave clean text space at the top or one side.

Text (verbatim): render exactly:

아루는 진흙놀이가
제일 좋아요.

통통!
조물조물!

둥근 몸에도
진흙이 묻고,

작은 가시에도
진흙이 묻었어요.

"히히,
정말 재밌어!"

Constraints: mud is warm pastel and safe, not gross or dark. Character reference fidelity over extra cuteness.
Avoid: bags, Aru hands/feet/legs/body, dirty scary mud, generic sea creatures, crowded background, pseudo-writing, extra text, watermark.
```

## Page 02 - 이제 씻자

### Output

`02_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/토리_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: loaded official exterior/playground is setting truth; loaded Aru, Mari teacher, Banguli, and visible friends are character identity truth. Use no-bag references positively.

Scene/backdrop: the mud-play time is ending in the warm daycare yard. The mud/sand play area is still visible but calmer than page 01.

Main subject: Aru suddenly freezes after hearing that it is time to wash. Preserve the official round orange pufferfish body with small spikes, small fins, pufferfish mouth, and sailor scarf. Aru still has cute pastel mud marks. Aru's expression shifts from joy to a small stunned "어? 벌써?" face. No hands, feet, legs, arms, or human body.

Mari teacher: Mari teacher approaches gently and says it is washing time. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, and purple mermaid tail. Her posture is warm and low-pressure, not pointing sharply or scolding.

Supporting action: a few friends begin moving toward the washing area in the background. Use fewer friends if necessary to keep reference fidelity. Banguli watches near Aru.

Composition/framing: medium shot showing Mari's gentle invitation and Aru's freeze. Leave a clean text area on one side.

Text (verbatim): render exactly:

"아루야,
이제 씻을 시간이야."

마리 선생님이
다정하게 말했어요.

친구들이 하나둘
씻으러 갔어요.

그런데 아루는—

멈칫.

"어?
벌써?"

Constraints: this is the first transition shock, not anger yet. Mari does not force.
Avoid: Aru hands/feet/legs/body, teacher grabbing, bags, shaming friends, random text, pseudo-writing, watermark.
```

## Page 03 - 싫어! 안 씻을래!

### Output

`03_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: loaded official exterior/playground is setting truth; loaded Aru, Mari teacher, and Banguli references are character identity truth. Use no-bag references positively.

Scene/backdrop: daycare yard mud-play area, softly simplified so the emotion is clear.

Main subject: Aru's transition resistance appears. Preserve Aru as the official round orange pufferfish child with small spikes, small fins, pufferfish mouth, and sailor scarf. Aru turns the round body away defensively, small spikes slightly lifted, mouth pressed or pouting. The expression says "싫어! 안 씻을래!" but is cute, vulnerable, and self-protective, not scary or aggressive. Pastel mud marks remain visible. No hands, feet, legs, arms, human torso, or separate lower body.

Mari teacher: Mari waits calmly nearby, watching with patient warmth. She does not pull, push, point sharply, scold, or shame Aru.

Banguli: Banguli floats nearby with a gentle curious tilt, as a small transparent droplet with tiny companion droplets.

Composition/framing: close or medium-close view of Aru's turned body and small raised spikes, with Mari in a calm secondary position. This page should later mirror page 08's "안 나올래" posture. Leave clean text space on one side.

Text (verbatim): render exactly:

"싫어!
안 씻을래!"

아루는 몸을
홱 돌렸어요.

작은 가시가
살짝 곤두섰어요.

진흙이
좋아서가 아니라—

지금 멈추는 게
싫었어요.

"조금만 더
놀 거야!"

Constraints: transition resistance, not bad behavior. Keep the scene emotionally safe.
Avoid: scary pufferfish, sharp teeth, attack pose, Aru hands/feet/legs/body, teacher forcing, bags, old episode contamination, random text, watermark.
```
