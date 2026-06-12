# Batch 1 Prompt Plan - 준이의 싫어싫어파도 - 2026-06-12 Restart

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. If the image generation workflow cannot use the loaded image references as visual grounding, stop and report the limitation instead of generating from prose only.

## Shared Locks

- Format: A5 portrait, about `1:1.414`.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Text: generate illustration and exact Korean story text together on the first pass.
- Contamination: do not use 2026-06-11 page candidates as visual truth.
- Jun-i: preserve official long shark snout, small black oval button eyes, white lower face and belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue shell-decorated arrival bag.
- Safety: no scolding, dragging, shaming, aggressive attack pose, scary shark face, or real dangerous wave.

## Page 00 - Cover

### Output

`00_cover_candidate_2026-06-12_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: the loaded official daycare exterior/playground reference and coral tunnel reference are the setting truth; the loaded official Jun-i, Mari teacher, and Banguli references are character identity truth.

Scene/backdrop: morning outside Coral Town Daycare. Use the official coral daycare entrance with blue door, gentle playground, and rounded coral tunnel as visual truth. The background is soft and supportive, not busy.

Subject: Jun-i is the foreground focus. He wears his official blue arrival bag and stands slightly turned away from the entrance, gently pouting because he cannot go in yet. Preserve the official Jun-i silhouette exactly: projecting shark snout, small black oval button eyes, white lower face and belly, blue shark body, gill marks, dorsal fin, side fins, long shark tail, small teeth, sailor shirt, blue shorts, and shell-decorated blue shoulder bag. Do not make him a round whale-like child, plush blob, generic blue toddler, or redesigned shark.

Supporting characters: Mari teacher waits near the doorway with a calm open hand and warm expression. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. Banguli floats near Jun-i as a pale sky-blue transparent droplet with a simple caring face.

Emotion symbol: show the `싫어싫어 파도` as small rounded blue water ribbons, bubbles, and gentle rhythm lines around Jun-i. It is a symbolic feeling wave, not a dangerous ocean wave.

Composition/framing: uncrowded cover. Focus on Jun-i, Mari teacher, and Banguli only. Other children should be omitted or only faint tiny doorway hints. Leave bright clean title space at the top.

Text (verbatim): render exactly:

준이의 싫어싫어파도

— 말로 말하면 작아져요 —

Constraints: exact official reference fidelity is more important than extra cuteness. Keep all characters toddler-safe and warm.
Avoid: crowded group cover, over-round Jun-i, changed eye shape, large sad eyes, scary shark expression, aggressive wave, scolding teacher pose, random signs, pseudo-writing, neon colors, plastic 3D texture, watermark.
```

## Page 01 - 아침 문이 열렸어요

### Output

`01_candidate_2026-06-12_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/포포.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are the setting truth; loaded official Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, and Popo are character identity truth.

Scene/backdrop: morning at the Coral Town Daycare entrance. Use the official exterior/playground reference: coral daycare building with blue door, soft playground, coral slide/water play hints, and rounded coral tunnel. Bright, safe, warm morning.

Main subject: Jun-i is in the foreground, separated slightly from the others, wearing his official blue arrival bag. He is not entering yet. He gently pouts and looks toward the outside playground with regret. Preserve the official shark shape: projecting snout, small black oval button eyes, white lower face/belly boundary, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. Do not make him rounder, softer, younger-looking, or more generic than the official reference.

Other characters: Mari teacher welcomes children at the doorway. Tori, Mongle, Lulu, Aru, and Popo move toward the entrance in a loose diagonal flow. Each visible friend must keep their official species silhouette and arrival bag/hat/details. Lulu must keep her long tube snout, spiny dotted ridge, coral/shell ornament, translucent fin, and curled tail. Popo must keep the moon-jelly dome and soft tentacles with eyes hidden or barely visible. Aru must remain a pufferfish body with no human hands, feet, legs, or separate lower body. Banguli floats near Jun-i.

Composition/framing: wide establishing view with slight diagonal flow from playground to doorway. Do not crowd all friends tightly together; give each character enough room for silhouette to read. Keep Jun-i large enough for official eye shape, snout, gills, fins, tail, and bag to be visible. Leave a bright clean text area in the upper-left water/sky space.

Text (verbatim): render exactly:

아침이 되었어요.
산호마을 어린이집 문이 열렸어요.
딩동댕동!
그런데 오늘 준이는
조금 삐친 얼굴이었어요.

Constraints: official-reference silhouette and facial structure override extra cuteness. Friends may be smaller than Jun-i, but they must not become generic sea creatures.
Avoid: over-round Jun-i, large sad eyes, missing gill marks, missing dorsal fin, missing blue bag, generic pink Lulu, Popo with normal big eyes, Aru with hands/feet, shaming crowd, old generated candidate contamination, pseudo-writing, random signs, watermark.
```

## Page 02 - 아직 안 들어갈래

### Output

`02_candidate_2026-06-12_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are setting truth; loaded official Jun-i, Mari teacher, Banguli, and any visible friend references are character identity truth.

Scene/backdrop: medium-distance view at the Coral Town Daycare doorway. The official blue door and exterior/playground are visible, with the outside playground pull clear enough to explain Jun-i's reluctance. Use the rounded coral tunnel naturally if visible.

Main subject: Jun-i stands near the entrance floor, still wearing his official blue bag. His body is slightly turned away from the doorway, with a small tucked-fin or crossed-fin posture that fits a shark body. His snout and small black button eyes angle toward the playground. He looks pouty, stubborn, and regretful, not frightened or angry.

Mari teacher: Mari gestures gently toward the door and waits without scolding. Preserve her official hair, star pin, yellow apron, name tag, purple notebook, and purple mermaid tail. Her posture is patient and low-pressure.

Banguli: Banguli floats near Jun-i, curious and worried, as a soft transparent water droplet.

Composition/framing: side-focused medium shot. Doorway on one side, playground pull on the other. Use fewer supporting friends than page 01 if needed; do not invent or simplify friends without their official reference. Leave a clean text area in the upper-right.

Text (verbatim): render exactly:

"준아, 어서 오렴."
마리 선생님이 말했어요.

하지만 준이는
입을 삐죽 내밀고 말했어요.

"아직 안 들어갈래!"

Constraints: Jun-i remains the official blue shark child with small button eyes and full shark silhouette. Mari does not pull, push, scold, or point sharply.
Avoid: changed Jun-i eyes, round whale-like Jun-i, human hands/feet added to sea children, teacher grabbing Jun-i, crowded doorway, random Korean text, pseudo-writing, old generated candidate contamination, watermark.
```

## Page 03 - 싫어싫어 파도

### Output

`03_candidate_2026-06-12_v1.png`

### References To Load

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`

### Prompt

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are setting truth; loaded official Jun-i, Banguli, Tori, Mongle, and Lulu references are character identity truth.

Scene/backdrop: outside near the daycare entrance and playground path. Use the official exterior/playground reference and keep the setting warm, readable, and safe.

Main subject: Jun-i's big feeling bursts out. He wears his official blue arrival bag. He stomps/taps in a toddler-safe way or taps his shark tail, showing protest without aggression. Preserve the official Jun-i design: projecting snout, small black oval button eyes, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. His mouth may open for `싫어!`, but do not enlarge teeth or make him predatory.

Story lock: do not show, write, imply, or speech-bubble the idea `밖에 더 있고 싶어`. This page shows only Jun-i's outer protest and the symbolic feeling wave.

Emotion symbol: the `싫어싫어 파도` is a soft symbolic feeling wave around Jun-i: rounded blue water ribbons, bubbles, gentle motion lines, and tiny safe sand/water splashes. It is not a real dangerous wave and should not threaten anyone.

Supporting characters: Banguli bounces in surprise near Jun-i. Tori, Mongle, and Lulu watch from a little distance with concern and surprise, not judgment. Keep them far enough not to crowd or shame Jun-i, but preserve their official silhouettes and details. Lulu must retain her long snout, spiny dotted ridge, head ornament, fin, and curled tail.

Composition/framing: dynamic low toddler-eye view. Jun-i is large enough for official snout, eye shape, gills, fins, tail, and bag to be clear. Keep clean text space at the top or upper side.

Text (verbatim): render exactly:

준이는 발을 쿵쿵 굴렀어요.
"싫어! 싫어!
안 들어갈래!"

준이 마음속에는
커다란 싫어싫어 파도가
출렁였어요.

Constraints: big emotion without fear. Official-reference fidelity over cute simplification. Friends respond with concern, not ridicule.
Avoid: phrase/visual meaning `밖에 더 있고 싶어`, dangerous wave, attack pose, scary teeth, large changed eyes, shaming crowd, generic supporting characters, pseudo-writing, random text, old generated candidate contamination, watermark.
```
