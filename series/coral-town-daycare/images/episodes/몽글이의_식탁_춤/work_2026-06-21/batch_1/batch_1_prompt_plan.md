# Batch 1 Prompt Plan - 몽글이의 식탁 춤 - 2026-06-21

## Scope

- Episode: `몽글이의 식탁 춤`
- Script: `series/coral-town-daycare/docs/episodes/몽글이의_식탁_춤.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Page plan: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21/page_plan.md`
- Worklog: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21/episode_worklog.md`
- Work folder: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21/batch_1`
- Batch scope: cover through page 03.

## Output Names

- Cover: `00_cover_candidate_v1.png`
- Page 01: `01_candidate_text_v1.png`
- Page 02: `02_candidate_text_v1.png`
- Page 03: `03_candidate_text_v1.png`

Generate and QA one page at a time. Do not move to the next page until the current page passes reference fidelity, exact Korean text, indoor no-bag lock, and contamination checks.

## Official References To Use

Core background:

- `series/coral-town-daycare/references/배경_식당.png`

Character references:

- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/포포.png`

Reference rule: if a character is visible, attach that character's individual official reference image. Do not rely on prose descriptions or earlier candidates for visible characters.

## Batch 1 Hard Locks

- Format: A5 portrait, about `1:1.414`.
- Text workflow: generate illustration and exact Korean story text together on the first pass.
- If exact Korean text cannot be rendered cleanly, leave a clean blank text area rather than inventing wrong text or pseudo-writing.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Background: official Coral Town Daycare dining room, warm cream lighting, shell table, low chairs, shell plates, soup bowl, water cup, and small side dishes.
- Indoor bag lock: children should not wear bags in the dining-room pages. If bags appear at all, they are stored on hooks, shelves, cubbies, or beside chairs.
- Emotional tone: Mongle is lively, not naughty; friends are surprised or curious, not shaming; Mari teacher is warm and non-scolding.
- Spill prep: page 03 can build a little tension, but the actual spill happens on page 04, not in this batch.
- No old generated episode images as visual references.

## Page 00 - Cover

### Output

`00_cover_candidate_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_식당.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Exact Cover Text

```text
몽글이의 식탁 춤

— 밥 먹을 땐
다리를 가지런히 —
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `몽글이의 식탁 춤` in A5 portrait proportion.
Input images: official dining-room background reference, official Mongle reference, official Banguli reference.

Scene/backdrop: bright and warm Coral Town Daycare dining room. Use the official dining-room reference as visual truth: shell table, low chair, shell plate, soup bowl, water cup, warm cream light, and safe daycare mealtime atmosphere.

Subject: Mongle is the foreground focus. Preserve the official purple octopus child design: round purple head, eight visible octopus legs, yellow beret, sailor collar, and toddler proportions. Mongle sits at the shell table, but his eight legs are joyfully wiggling in different directions: one leg upward, one toward the table, several curling around the chair, and his bottom slightly lifted from the chair. He has a wide excited smile. Do not add human legs or feet.

Supporting character: Banguli floats beside Mongle as a pale sky-blue transparent droplet with a simple curious face and two or three tiny companion droplets.

Composition/framing: uncrowded cover. Mongle and the shell table are centered. Leave bright clean title space at the top and smaller subtitle space near the bottom. Keep tableware neat and readable.

Text (verbatim): render exactly:

```text
몽글이의 식탁 춤

— 밥 먹을 땐
다리를 가지런히 —
```

Constraints: official reference fidelity is more important than extra cuteness. Keep the scene warm and safe. No worn bags. No pseudo-writing.
Avoid: human legs, generic octopus redesign, scary tentacles, chaotic food spill on cover, over-shiny 3D texture, neon colors, random signs, watermark.

### QA Before Accepting

- Mongle has eight visible octopus legs and matches `몽글이.png`.
- Banguli remains a droplet, not a jellyfish or crystal.
- Title/subtitle text is exact, readable, or the title area is cleanly blank for later text repair.
- Dining room matches the official reference enough to read as the series setting.
- No child is wearing a bag indoors.

## Page 01 - 다리가 여덟 개나 신났어요

### Output

`01_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_식당.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/포포.png`

### Exact Page Text

```text
점심 시간이에요.

오늘은 따뜻한 미역국과
동글동글 주먹밥!

몽글이는
다리가 여덟 개나
신났어요.

통통! 통통!

"맛있겠다—!"

다리들이
꼬물꼬물
춤을 췄어요.
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `몽글이의 식탁 춤` in A5 portrait proportion.
Input images: official dining-room reference and individual official references for Mongle, Mari teacher, Banguli, Jun-i, Aru, Lulu, Sua, Tori, and Popo.

Scene/backdrop: lunchtime in the Coral Town Daycare dining room. Use the official dining-room reference: shell table, low child chairs, shell plates, warm cream lighting, soup bowls, water cups, small side dishes, and a clean safe toddler mealtime setting.

Main subject: Mongle enters or reaches the dining table with excited eight-leg motion. Preserve the official purple octopus child exactly: eight visible legs, yellow beret, sailor collar, round purple head, and childlike scale. His legs wiggle with joyful motion, not misbehavior. No human legs or feet.

Other characters: Mari teacher serves or welcomes lunch with a calm teacher posture. Jun-i, Aru, Lulu, Sua, Tori, and Popo are settling near the table, but keep them spaced enough that their official silhouettes read. Banguli floats near Mongle. Since this is a dining-room scene, children do not wear bags; bags are omitted or stored off-body.

Composition/framing: lively wide-to-medium establishing view. Mongle is central and large enough for all eight legs to be clear. Friends and lunch menu support the scene without crowding. Leave a clean text area near the top or one side.

Text (verbatim): render exactly the page text above.

Constraints: official references override prose. Keep each visible character's species structure intact. Warm toddler-safe energy.
Avoid: worn bags, generic sea children, repeated faces, scary tentacles, food spill too early, random text, pseudo-writing, watermark.

### QA Before Accepting

- Korean text is exact and readable.
- Mongle's eight legs are visible and joyful.
- No indoor body-worn bags.
- Mari and supporting friends match official references if visible.
- Background reads as the official dining room.

## Page 02 - 가만히 앉기가 힘들어요

### Output

`02_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_식당.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- Supporting friend refs only if they are clearly visible: `준이.png`, `아루.png`, `수아.png`, `포포.png`

### Exact Page Text

```text
다들 자리에 앉아
냠냠 먹기 시작했어요.

그런데 몽글이는……

가만히 앉아 있기가
힘들었어요.

한 다리는 식탁 위로
슬쩍—

한 다리는 의자를
톡톡톡—

엉덩이가
들썩들썩.

"히히, 신난다!"
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `몽글이의 식탁 춤` in A5 portrait proportion.
Input images: official dining-room reference, official Mongle reference, official Banguli reference, and any official friend references for visible nearby friends.

Scene/backdrop: children are calmly eating lunch at the shell table in the official dining room.

Main subject: Mongle sits on a low chair at the shell table, but staying still is hard. One octopus leg slides gently toward the tabletop, one taps the chair, several wiggle below, and his bottom lifts slightly. He looks delighted, not guilty or naughty. Preserve all eight legs, yellow beret, sailor collar, and purple octopus identity.

Supporting characters: a few nearby friends eat calmly or glance over with mild curiosity. Banguli tilts curiously nearby. Keep supporting friends less crowded than page 01 if necessary. No worn bags.

Composition/framing: medium shot with contrast between calm table rhythm and Mongle's wiggly body. Use the tabletop, low chair, and Mongle's legs as the readable action. Leave clean text space on one side.

Text (verbatim): render exactly the page text above.

Constraints: no scolding tone yet; the page is about overflowing excitement. Keep the food tidy.
Avoid: full spill, angry faces, shaming friends, human legs, worn bags, pseudo-writing, watermark.

### QA Before Accepting

- Text is exact and readable.
- One leg is near/on the table, one taps the chair, and other legs wiggle.
- Mongle still reads as the official octopus child.
- Friends are curious or calm, not judgmental.
- No indoor body-worn bags.

## Page 03 - 주먹밥으로 통통통

### Output

`03_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_식당.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/수아.png`

### Exact Page Text

```text
몽글이는
밥을 먹는 대신—

주먹밥을 통통통
굴리고,

미역국을 휘휘
저었어요.

"이건 공놀이!
이건 빙글빙글!"

국물이 찰랑찰랑.
주먹밥이 데구르르.

친구들이
"어어—" 했어요.
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `몽글이의 식탁 춤` in A5 portrait proportion.
Input images: official dining-room reference and individual official references for Mongle, Mari teacher, Banguli, Aru, and Sua.

Scene/backdrop: at the shell table in the official Coral Town Daycare dining room. The tabletop is becoming a little busy, but not dirty or gross.

Main subject: Mongle plays with food because he is excited: one leg gently rolls a round rice ball, another swirls the seaweed soup, and other legs wiggle in delight. His expression is playful and absorbed. Preserve official Mongle: eight visible octopus legs, yellow beret, sailor collar, round purple head. Do not make him malicious or wild.

Supporting characters: Aru and Sua notice with soft "uh-oh" expressions from nearby. Mari teacher begins to approach gently from the side, not scolding. Banguli floats nearby with a curious/worried tilt. No worn bags.

Composition/framing: medium close-up of Mongle's leg actions, rice ball, and soup bowl. Build a small sense of "this may get messy" without showing the page 04 spill yet. Leave clean text space on one side or above.

Text (verbatim): render exactly the page text above.

Constraints: food-play is cute but clearly not meal-safe; tone stays gentle. Page 04 is the actual spill, so keep page 03 to rolling/stirring/찰랑.
Avoid: scary chaos, gross mess, angry teacher, shaming friends, missing octopus legs, worn bags, pseudo-writing, watermark.

### QA Before Accepting

- Korean text is exact and readable.
- Food action matches: rice ball rolling, soup stirred/찰랑, no full spill yet.
- Mongle keeps eight legs and official identity.
- Mari is approaching gently, not scolding.
- Aru and Sua match references if visible.
- No indoor body-worn bags.

## Batch 1 QA Gate

Before continuing to batch 2, each accepted candidate must pass:

- Character identity: all visible characters match their individual official references.
- Text: exact Korean text is present, readable, and not paraphrased. If text fails but art passes, keep the art candidate separate for text repair.
- Continuity: dining-room setting and tableware stay consistent across all four images.
- Story: page 03 builds food-play tension but does not show the full page 04 spill.
- Rulebook lock: no body-worn bags in the dining-room pages.
- Tone: Mongle is lively, not naughty; friends and Mari stay warm.
- Contamination: no prior failed episode image, generic character redesign, random signage, pseudo-writing, or watermark.
