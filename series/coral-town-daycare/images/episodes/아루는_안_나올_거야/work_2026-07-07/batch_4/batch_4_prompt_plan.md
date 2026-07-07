# Batch 4 Prompt Plan - 아루는 안 나올 거야

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. Approved final pages may be used only as continuity locks, not as replacements for official character references.

## Batch 4 Scope

1. `10_candidate_text_v1.png`
2. `11_candidate_text_v1.png`
3. `12_candidate_text_v1.png`

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
- Batch 3 final pages promoted:
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/07_첨벙첨벙_신나는_물놀이.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/08_안_나올래_더_할래.png`
  - `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/09_어_아까는_들어가기_싫었는데.png`
- Water tub lock:
  - Use `work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png` as the recurring prop reference for pages 10-11.
  - The tub is a low toddler-safe shell basin with warm clear shallow water, a peach-coral scalloped rim, cream/sand shell body, soft bubbles, and no bathroom fixtures.
- Aru continuity lock:
  - Use official Aru references for identity and final pages 06-09 for the approved in-water state.
  - Keep Aru soft cream-yellow with muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf, and no school bag.
  - Avoid saturated orange Aru and blue scarf.
  - Aru must never gain hands, feet, legs, arms, a human torso, separate lower body, or grabbing fingers.
- Emotional lock:
  - Page 10 confirms Aru's page 09 insight. Mari reflects warmly; Mari does not reveal the lesson first, lecture, point, or explain with a diagram.
  - Page 11 is Aru's first self-led transition. Aru agrees to five splashes and comes out by choice. Mari may hold a towel but must not grab, pull, drag, or lift Aru.
  - Page 12 closes with warmth and confidence: changing is hard, but trying can lead somewhere good.
- No-bag lock: no child wears a school bag in water-play or closing scenes.
- Contamination lock: do not use failed, held, or superseded candidates as visual truth.

## Shared Style

- Format: A5 portrait, about `1:1.414`.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Text: generate illustration and exact Korean story text together on the first pass.
- Text panels: clean cream or pale-sand narration area, readable dark brown Korean text, no pseudo-writing.
- No local text overlay unless a separate text repair pass is explicitly needed after QA.

## Page 10 - 바뀌는 게 어려웠구나

### Output

`10_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/09_어_아까는_들어가기_싫었는데.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 10
Primary request: Create page 10 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru, Mari teacher, and Banguli references as character identity truth. Use final page 09 only as continuity for Aru's own realization and final page 06 for the approved in-water color/scarf and shell-tub continuity.

Scene/backdrop: same warm Coral Town Daycare shallow shell tub washing/water-play corner. The water remains warm, clean, shallow, and safe.

Main action: After Aru's own realization from page 09, Mari teacher smiles warmly and gently confirms what Aru already noticed. Aru relaxes and nods in the shell tub. Banguli watches nearby with a soft supportive face. The emotional focus is calm recognition, not a lesson lecture.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Aru is wet, clean, and relaxed. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, grabbing fingers, or school bag.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Mari is low, warm, and reflective. No pointing, scolding, grabbing, dragging, pulling, or shaming. Do not make Mari the original explainer; she only confirms Aru's own insight.

Banguli lock: pale sky-blue transparent water droplet with simple supportive face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, toy, or animal.

Composition/framing: gentle medium shot, with Aru in the shell tub and Mari nearby at a calm low angle. Keep the text panel clean and readable without covering Aru's face, Mari's expression, Banguli, or the tub rim.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

마리 선생님이
방긋 웃었어요.

"맞아.
바뀌는 게
어려웠구나."

"진흙도 좋고,
물도 좋았지?"

아루는
끄덕였어요.

"응.
둘 다 좋았어.

멈추는 게
어려웠어."

Constraints: confirmation after Aru's realization, warm non-scolding tone, shallow water safety.
Avoid: Mari explaining first, teacher pointing, diagrams, lesson board, Aru hands/feet/legs/body, deep pool, sink, bathtub, bathroom fixtures, orange Aru, blue scarf, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 11 - 조금만 더, 그리고 나오기

### Output

`11_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/work_2026-07-07/reference_assets/shallow_shell_water_tub_ref.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/06_어_따뜻하고_좋네.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/09_어_아까는_들어가기_싫었는데.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 11
Primary request: Create page 11 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded shallow shell water tub reference as prop/setting truth. Use official Aru, Mari teacher, and Banguli references as character identity truth. Use final pages 06 and 09 only for approved in-water Aru color/scarf, shell tub continuity, and Aru's newly calmer self-awareness.

Scene/backdrop: same warm Coral Town Daycare shallow shell tub washing/water-play corner. A soft towel is ready nearby.

Main action: Aru makes a small promise: five more splashes, then coming out. Show the moment as self-led and playful. Aru is at the edge of the shallow shell tub after splashing, choosing to come out. Mari teacher gently holds or opens a warm towel nearby, waiting. Banguli floats nearby supportively. The action must show Aru's choice, not adult force.

Aru lock: soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. Aru is wet, clean, and brave. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, grabbing fingers, or school bag. If Aru comes out, use the round pufferfish body lifting/rolling from the tub by self-choice, not humanoid climbing.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Mari is patient and prepared with a towel. No grabbing, pulling, dragging, lifting, or forcing.

Banguli lock: pale sky-blue transparent water droplet with simple happy/supportive face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, toy, or animal.

Composition/framing: medium-wide scene showing the shell tub, Aru's self-led exit, Mari's towel, and small playful splash marks. Five splashes may be suggested with five small water arcs/bubbles, but do not turn the page into a counting diagram. Keep text panel clean and readable.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

"그럼,
다섯 번만 더 첨벙—

그리고
나오기로 약속!"

하나, 둘, 셋,
넷, 다섯!

첨벙—!

"이제……
나갈래."

아루는 스스로
물통에서 나왔어요.

마리 선생님이
포근한 수건을
펼쳤어요.

Constraints: Aru chooses the transition, toddler-safe shallow water, towel warmth, no adult force.
Avoid: Mari pulling Aru out, grabbing, lifting, dragging, teacher scolding, Aru hands/feet/legs/body, deep pool, sink, bathtub, bathroom fixtures, cold water, orange Aru, blue scarf, bags, random text, pseudo-writing, watermark, plastic 3D texture.
```

## Page 12 - 바뀌는 건 어렵지만, 해보면 괜찮아

### Output

`12_candidate_text_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/마리_선생님_no_bag.png`
- `series/coral-town-daycare/references/characters/no_bag/방울이_no_bag.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/01_진흙놀이.png`
- `series/coral-town-daycare/images/episodes/아루는_안_나올_거야/final/09_어_아까는_들어가기_싫었는데.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 12 ending page
Primary request: Create page 12 of `아루는 안 나올 거야` in A5 portrait proportion.
Input images: Use the loaded exterior/playground and coral tunnel references as setting truth. Use official no-bag and original character references as identity truth for Aru, Mari teacher, and Banguli only. Use final pages 01 and 09 only for story continuity: this ending resolves mud play and water play with Aru's calm insight.

Scene/backdrop: bright warm Coral Town Daycare yard or entrance-side play area after water play. The setting should feel clean, sunny, safe, and familiar, with soft coral decorations and the round coral tunnel if visible. No water tub is required on this page unless it is very small in the background.

Main action: Dry, clean Aru smiles with Banguli and Mari teacher in a warm closing scene. Aru feels proud and calm after trying the transition. The page should feel like a soft final page, not a poster or classroom lesson.

Aru lock: dry and clean soft cream-yellow pufferfish body, muted tan-olive top shading, darker brown top spots, warm beige fins, red-white sailor scarf. No saturated orange. No blue scarf. No hands, feet, legs, arms, human torso, separate lower body, grabbing fingers, towel costume, or school bag.

Mari lock: preserve half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple mermaid tail. Mari is warm and present as a caregiver, not lecturing.

No-extra-character lock: Show only Aru, Banguli, and Mari teacher. Do not add friends, background children, pink octopus characters, mermaid children, or unnamed mascots. Fill any empty areas with ordinary coral scenery, stones, bubbles, shells, or playground architecture.

Coral tunnel scale lock: the coral tunnel is a small daycare crawl-through playground toy, not a building, gate, monument, cave, or architectural entrance. Its opening should be around Aru's body height, and at most Mari teacher's knee-to-waist height. It must read as something children crawl through, not a giant background structure.

Banguli lock: pale sky-blue transparent water droplet with simple happy face and tiny companion droplets. Banguli is not a jellyfish, bead, crystal, toy, or animal.

Composition/framing: warm closing scene with Aru clearly visible as the emotional center. Keep the text panel clean and readable, preferably over a calm cream/sand or pale background area. Avoid any lineup or crowd. Keep any coral tunnel in the mid/background small enough to be a child play object.

Style/medium: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette, rounded forms.

Text (verbatim): render exactly:

아루는
조금 웃었어요.

"다음에도
처음은 어려울 수 있고,

나중엔
그만두기 어려울 수도 있지."

마리 선생님이
끄덕였어요.

"그래도 아루는
해낼 수 있어.
천천히 해도 괜찮아."

산호마을 어린이집은
오늘도 맑음.

아루의 마음도
반짝반짝 맑음.

Constraints: warm ending, clean dry Aru, Banguli and Mari only, small crawl-through coral tunnel if visible, no bags, no random signage.
Avoid: giant coral tunnel, building-scale tunnel, architectural arch, pink octopus character, mermaid child, unnamed children, extra friends, extra mascots, lecture poster, chart, teacher pointing, graduation/performance stage, crowded copied faces, school bags, Aru hands/feet/legs/body, orange Aru, blue scarf, generic animal redesigns, random text, pseudo-writing, watermark, plastic 3D texture.
```
