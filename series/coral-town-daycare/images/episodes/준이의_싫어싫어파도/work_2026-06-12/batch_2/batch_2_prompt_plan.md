# Batch 2 Prompt Plan - 준이의 싫어싫어파도 - 2026-06-12

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. If the image generation workflow cannot use the loaded image references as visual grounding, stop and report the limitation instead of generating from prose only.

Do not generate page 05 until page 04 has QA notes. Do not generate page 06 until page 05 has QA notes. Do not promote anything to `final` in this batch.

## Shared Batch 2 Style Lock

Use the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, and gentle toddler picture-book emotion. Continue the accepted page 01-03 direction. Avoid the rejected cover v2 look: no smooth 3D, no plastic toy texture, no glossy CG finish, no over-clean rendering.

Official reference fidelity is more important than extra cuteness.

## Page 04 - 선생님은 기다렸어요

Output: `batch_2/04_candidate_2026-06-12_v1.png`

References to load:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`

Prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 04
Primary request: Create page 04 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: loaded official exterior/playground and coral tunnel are the setting truth; loaded official Jun-i, Mari teacher, Banguli, Tori, Mongle, and Lulu are character identity truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, gentle toddler picture-book mood. Avoid smooth 3D, plastic toy texture, glossy CG, or the rejected cover v2 style.

Scene/backdrop: quiet morning outside the Coral Town Daycare entrance. Use the official coral daycare exterior with the blue door and a gentle hint of the playground/coral tunnel. The mood is quieter than page 03: the big wave has settled into a calm pause.

Main subjects: Mari teacher and Jun-i. Mari has moved close and lowered herself beside Jun-i at child eye level. She waits warmly without scolding. Preserve her official half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail.

Jun-i still wears his official blue arrival bag. He is still a little pouty, but his body begins to listen. Preserve the official shark shape exactly: projecting shark snout, tiny black oval button eye with small highlight, no eyebrow, no eyelid line, white lower face/belly boundary, three gill marks, dorsal fin, side fins, long shark tail, sailor shirt, blue shorts, and blue shell-decorated shoulder bag.

Supporting characters: Banguli floats nearby with a gentle worried face. Tori, Mongle, and Lulu may appear small in the background at a respectful distance, quietly watching without crowding or judging.

Composition/framing: close medium shot, child-eye-level. Mari and Jun-i share the emotional center. Leave a clean bright text area in the upper-left.

Text (verbatim): render exactly with these line breaks:
마리 선생님은
준이 옆에 조용히 앉았어요.

"준아, 많이 속상했구나."
선생님은 혼내지 않았어요.
그냥 다정하게 기다렸어요.

Constraints: Mari must not grab, pull, push, point sharply, or scold. Jun-i's blue bag and official shark details must remain visible. Friends must not become a pressure crowd.
Avoid: teacher scolding, teacher dragging Jun-i, sharp pointing, generic shark child, changed eye shape, missing gills, missing bag, big dangerous wave, random text, pseudo-writing, old 2026-06-11 candidate contamination, smooth 3D, plastic toy texture, watermark.
```

QA:

- Text exact and readable.
- Mari waits without scolding or touching Jun-i forcefully.
- Jun-i keeps official snout, small black button eye, gills, fins, tail, sailor outfit, and blue bag.
- Scene reads as calming down after page 03.

## Page 05 - 밖에 더 있고 싶어

Output: `batch_2/05_candidate_2026-06-12_v1.png`

References to load:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`

Prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 05
Primary request: Create page 05 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: loaded official exterior/playground and coral tunnel are the setting truth; loaded official Jun-i, Mari teacher, Banguli, and Tori are character identity truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, gentle toddler picture-book emotion. Avoid smooth 3D, plastic toy texture, glossy CG, or the rejected cover v2 style.

Scene/backdrop: outside the daycare entrance, with the playground softly visible in the direction Jun-i has been looking. Keep the background calm and not too busy.

Main subjects: Jun-i and Mari teacher in an emotional close-up or close medium shot. Jun-i is a little tearful or small in posture, still wearing his official blue arrival bag. He says only what he can at first. Preserve his official shark shape: projecting snout, tiny black oval button eye, no eyebrow, no eyelid line, white lower face/belly, three gill marks, dorsal fin, side fins, long tail, sailor shirt, blue shorts, and blue shell-decorated bag.

Mari teacher sits or leans near Jun-i and follows his gaze toward the playground. She does not decide his feeling for him. She gently offers a possible phrase with a warm, tentative expression. Preserve her official half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail.

Story lock: this is the first clear reveal of `밖에 더 있고 싶어`. Mari may gently offer the phrase as a possibility, but Jun-i must directly say the final line himself. Do not reveal it as a thought bubble only. Do not make Mari force the answer.

Supporting characters: Banguli floats quietly near Jun-i. Tori may watch from a little distance with concern and relief, not pressure.

Composition/framing: emotional close-up with generous upper text space. The playground direction should be visible enough to explain the feeling, but it should not overpower Jun-i and Mari.

Text (verbatim): render exactly with these line breaks:
준이는 작은 목소리로 말했어요.
"나... 그냥 싫어."

마리 선생님은
준이 눈길을 따라 보았어요.

"준이 마음속 말이
혹시 이 말일까?
'밖에 더 있고 싶어.'"

준이는 아주 작게 말했어요.
"밖에... 더 있고 싶어."

Constraints: Jun-i's final spoken line must be present. Mari's posture is tentative and helping, not correcting. Keep the moment quiet and emotionally safe.
Avoid: Mari saying the final line as the answer alone, thought bubble replacing Jun-i's spoken line, scolding, dragging, crowd pressure, changed Jun-i eye shape, missing blue bag, random Korean text, pseudo-writing, old 2026-06-11 candidate contamination, smooth 3D, plastic toy texture, watermark.
```

QA:

- Text exact and readable.
- `밖에 더 있고 싶어` appears here, not as a hidden or substitute earlier reveal.
- Jun-i directly says `"밖에... 더 있고 싶어."`
- Mari helps find words without imposing or scolding.

## Page 06 - 조개 모래시계

Output: `batch_2/06_candidate_2026-06-12_v1.png`

References to load:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

Prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 06
Primary request: Create page 06 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: loaded official exterior/playground and coral tunnel are the setting truth; loaded official Jun-i, Mari teacher, Banguli, and shell hourglass are character/prop identity truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, gentle toddler picture-book emotion. Avoid smooth 3D, plastic toy texture, glossy CG, or the rejected cover v2 style.

Scene/backdrop: outside near the Coral Town Daycare entrance. Mari and Jun-i are low to the ground in a calm, stable moment after Jun-i has named his feeling.

Main subjects: Mari teacher shows the shell hourglass to Jun-i. Preserve Mari's official half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. Her gesture offers a choice and a small waiting plan, not a command.

Jun-i still wears his official blue arrival bag and looks at the shell hourglass with curiosity and a calmer expression. Preserve his official shark shape: projecting snout, tiny black oval button eye, no eyebrow, no eyelid line, white lower face/belly, three gill marks, dorsal fin, side fins, long tail, sailor shirt, blue shorts, and blue shell-decorated bag.

Prop lock: the shell hourglass must match the loaded `shell_hourglass_ref.png`: small shell top and bottom, transparent rounded glass body, warm sand-colored grains, a thin stream of sand falling in the center. Do not add jewels, metal frame, numbers, clock face, magic glow, wings, handles, or a new color scheme.

Supporting character: Banguli floats beside them and looks curiously at the hourglass.

Composition/framing: stable close medium shot, slightly overhead or child-eye-level. The hourglass is clearly visible but not huge. Leave clean text space in the upper-right or upper-left.

Text (verbatim): render exactly with these line breaks:
마리 선생님이
조개 모래시계를 꺼냈어요.

"말해 줘서 고마워.
그럼 모래가 다 내려갈 때까지만
밖에 조금 더 있다가
들어가 볼까?"

준이는 가만히 모래시계를 보았어요.

Constraints: this is a gentle time-bound alternative after Jun-i uses words. Keep Mari patient, Jun-i calmer, and the prop consistent for pages 07-08.
Avoid: bargaining tone, scolding, forcing Jun-i inside, oversized magical artifact, jeweled hourglass, metal frame, clock numbers, changed Jun-i eye shape, missing blue bag, pseudo-writing, random text, old 2026-06-11 page candidate contamination, smooth 3D, plastic toy texture, watermark.
```

QA:

- Text exact and readable.
- Shell hourglass matches the reference and is usable for pages 07-08 continuity.
- Mari offers a choice rather than forcing.
- Jun-i remains official and still wears the blue bag.
