# Batch 1 Restart Prompt Plan - 2026-06-11

## Scope

- Episode: `준이의 싫어싫어파도`
- Script: `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Page plan: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/page_plan.md`
- Worklog: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/episode_worklog.md`
- Work folder: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/batch_1`
- Restart scope: cover through page 03.

## Restart Decision

Existing page 01 candidates are held as rejected/process history:

- `01_candidate_text_v1.png`: hold. Jun-i became too round, eyes drifted into large sad eyes, supporting characters drifted.
- `01_candidate_text_v2.png`: hold. Improvement attempt only; do not use as visual reference.
- `01_candidate_text_v3.png`: hold. Best of the first pass, but still not accepted because reference fidelity is not strong enough for a clean restart.

Do not use any prior generated page from this episode as visual truth. Only official reference images and the script/rulebook below should drive the restart.

## Restart Output Names

- Cover: `00_cover_candidate_restart_v1.png`
- Page 01: `01_candidate_text_restart_v1.png`
- Page 02: `02_candidate_text_restart_v1.png`
- Page 03: `03_candidate_text_restart_v1.png`

Generate and QA one page at a time. Do not move to the next page until the current page passes reference fidelity, exact Korean text, story lock, and contamination checks.

## Official References To Use

Core exterior references:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`

Character references:

- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/포포.png`

Reference rule: if a character is visible, attach that character's individual official reference image. Do not rely on prose descriptions or earlier candidates for visible characters.

## Batch 1 Hard Locks

- Format: A5 portrait, about `1:1.414`.
- Text workflow: generate illustration and exact Korean story text together on the first pass.
- If exact Korean text cannot be rendered cleanly, leave a clean blank text area rather than inventing wrong text or pseudo-writing.
- Style: soft Korean toddler picture-book watercolor and colored-pencil texture, warm paper grain, low-saturation pastel palette.
- Background: official Coral Town Daycare exterior/playground. Keep the coral daycare entrance, blue door, playground, and rounded coral tunnel consistent with the official references. Do not replace the setting with a generic fantasy school or dark deep sea.
- Arrival continuity: pages 01-03 are arrival-time exterior scenes, so Jun-i keeps his official blue bag on. Keep the bag visible but do not let it hide his shark body language.
- Emotional tone: big feelings are toddler-safe. No scolding, dragging, shaming, aggressive attack pose, scary shark face, or real dangerous wave.
- Story lock: page 03 must not reveal or imply "밖에 더 있고 싶어." That reason is first spoken by Jun-i on page 05 with Mari teacher's gentle help.

## Reference Fidelity Locks

### Jun-i

Jun-i is the highest-risk character in this restart. Preserve the official `준이.png` design before adding cuteness:

- Keep the projecting shark snout and long side-view shark head shape. Do not compress him into a round whale, plush blob, or generic blue toddler.
- Keep small black oval button eyes. No large sad anime eyes, colored irises, eyelashes, droopy human eyes, or tearful manga eyes.
- Keep the white lower face and white belly boundary, blue shark body, visible gill marks, dorsal fin, side fins, long shark tail, small teeth, sailor shirt, blue shorts, and blue shell-decorated shoulder bag.
- When he pouts, change the mouth/body posture only. Do not redesign the eye shape.
- He may look upset, stubborn, or regretful, but never predatory, toothy, realistic, fierce, or older than a preschooler.

### Mari Teacher

- Match `마리_선생님.png`: half-up dark bob, yellow star hairpin, cream blouse, yellow apron, name tag, purple attendance notebook, purple mermaid tail.
- Daycare teacher, not princess mermaid. Warm, stable, low posture when comforting; no scolding finger.

### Banguli

- Match `방울이.png`: pale sky-blue transparent water droplet, soft rounded outline, simple tiny face, small side bubble/droplet nubs.
- Not a jellyfish, crystal bead, toy, or hard glass object.

### Supporting Friends

- Tori: green turtle child, yellow helmet-like hat, turtle shell, yellow bag during arrival, gentle worried face.
- Mongle: purple octopus child with eight visible tentacle arms, yellow beret, sailor collar, art-child details if visible.
- Lulu: pink seahorse child with long tube snout, dotted/spiny head ridge with bead tips, coral/shell head ornament, textured body, translucent fin, curled tail, sailor outfit, yellow bag during arrival. Do not simplify Lulu into a smooth pink fish or small generic seahorse.
- Aru: round orange pufferfish body with small spikes, fins, pufferfish mouth, sailor scarf, yellow bag during arrival. No human torso, hands, feet, legs, or separate lower body.
- Popo: translucent moon jellyfish dome, subtle inner moon-jelly flower pattern, scalloped dome edge, long soft tentacles, sailor collar, beige bag during arrival. Eyes should be hidden or barely visible unless a tiny mouth/expression is needed.

## Page 00 - Cover

### Output

`00_cover_candidate_restart_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`

### Exact Cover Text

```text
준이의 싫어싫어파도

— 말로 말하면 작아져요 —
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: official daycare exterior/playground reference, official coral tunnel reference, official Jun-i reference, official Mari teacher reference, official Banguli reference.

Scene/backdrop: morning outside Coral Town Daycare. Use the official coral daycare entrance with the blue door, gentle playground, and rounded coral tunnel as visual truth. The background is soft and supportive, not busy.

Subject: Jun-i is the foreground focus. He wears his official blue arrival bag and stands slightly turned away from the entrance, gently pouting because he cannot go in yet. Preserve the official Jun-i silhouette exactly: projecting shark snout, small black oval button eyes, white lower face and belly, blue shark body, gill marks, dorsal fin, side fins, long shark tail, small teeth, sailor shirt, blue shorts, and shell-decorated blue shoulder bag. Do not make him a round whale-like child, a plush blob, or a redesigned shark.

Supporting characters: Mari teacher waits near the doorway with a calm open hand and warm expression. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. Banguli floats near Jun-i as a pale sky-blue transparent droplet with a simple caring face.

Emotion symbol: show the "싫어싫어 파도" as small rounded blue water ribbons, bubbles, and gentle rhythm lines around Jun-i. It is a symbolic feeling wave, not a dangerous ocean wave.

Composition/framing: uncrowded cover. Focus on Jun-i, Mari teacher, and Banguli only. Other children should be omitted or only faint tiny doorway hints. Leave bright clean title space at the top.

Text (verbatim): render exactly:

```text
준이의 싫어싫어파도

— 말로 말하면 작아져요 —
```

Constraints: exact official reference fidelity is more important than extra cuteness. Keep all characters toddler-safe and warm.
Avoid: crowded group cover, over-round Jun-i, changed eye shape, large sad eyes, scary shark expression, aggressive wave, scolding teacher pose, random signs, pseudo-writing, neon colors, plastic 3D texture, watermark.

### QA Before Accepting

- Jun-i still reads as the official shark child, not a rounded whale/plush.
- Jun-i has small black oval button eyes.
- Mari teacher keeps yellow apron, star hairpin, purple tail, and teacher posture.
- Banguli remains a droplet.
- Title text is exact or the title area is cleanly blank for later text repair.

## Page 01 - 아침 문이 열렸어요

### Output

`01_candidate_text_restart_v1.png`

### References To Attach

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

### Exact Page Text

```text
아침이 되었어요.
산호마을 어린이집 문이 열렸어요.
딩동댕동!
그런데 오늘 준이는
조금 삐친 얼굴이었어요.
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: official exterior/playground, official coral tunnel, and individual official references for Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, and Popo.

Scene/backdrop: morning at the Coral Town Daycare entrance. Use the official exterior/playground reference as the setting: coral daycare building with blue door, soft playground, coral slide/water play hints, and the rounded coral tunnel. The scene is bright, safe, and warm.

Main subject: Jun-i is in the foreground, separated slightly from the others, wearing his official blue arrival bag. He is not entering yet. He gently pouts and looks toward the outside playground with regret. Preserve the official shark shape: projecting snout, small black oval button eyes, white lower face/belly boundary, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. Do not make him rounder, softer, younger-looking, or more generic than the official reference.

Other characters: Mari teacher welcomes children at the doorway. Tori, Mongle, Lulu, Aru, and Popo move toward the entrance in a loose diagonal flow. Each visible friend must keep their official species silhouette and arrival bag/hat/details. Lulu must keep her long tube snout, spiny dotted ridge, coral/shell ornament, translucent fin, and curled tail. Popo must keep the moon-jelly dome and soft tentacles with eyes hidden or barely visible. Banguli floats near Jun-i.

Composition/framing: wide establishing view with a slight diagonal flow from playground to doorway. To protect reference fidelity, do not crowd all friends tightly together; give each character enough room for their silhouette to read. Keep Jun-i large enough for the official eye shape, snout, gills, fins, tail, and bag to be visible. Leave a bright clean text area in the upper-left water/sky space.

Text (verbatim): render exactly:

```text
아침이 되었어요.
산호마을 어린이집 문이 열렸어요.
딩동댕동!
그런데 오늘 준이는
조금 삐친 얼굴이었어요.
```

Constraints: official-reference silhouette and facial structure override extra cuteness. Friends may be smaller than Jun-i, but they must not become generic sea creatures.
Avoid: over-round Jun-i, large sad eyes, missing gill marks, missing dorsal fin, missing blue bag, generic pink Lulu, Popo with normal big eyes, Aru with hands/feet, shaming crowd, old generated candidate contamination, pseudo-writing, random signs, watermark.

### QA Before Accepting

- Korean text is exact, readable, and not paraphrased.
- Jun-i has official small black oval eyes, projecting snout, gill marks, fins, long tail, sailor outfit, and blue bag.
- Lulu keeps the seahorse snout/ridge/tail details.
- Popo does not become a generic jellyfish with big eyes.
- Friends are entering gently; Jun-i is separate and pouty, not scary.
- Background matches the official daycare/playground and includes the coral tunnel when visible.

## Page 02 - 아직 안 들어갈래

### Output

`02_candidate_text_restart_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- Optional only if visible at readable size: `토리.png`, `몽글이.png`, `루루.png`, `아루.png`, `포포.png`

### Exact Page Text

```text
"준아, 어서 오렴."
마리 선생님이 말했어요.

하지만 준이는
입을 삐죽 내밀고 말했어요.

"아직 안 들어갈래!"
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: official exterior/playground, official coral tunnel, official Jun-i, official Mari teacher, official Banguli, and only the individual friend references for any friends shown clearly.

Scene/backdrop: medium-distance view at the Coral Town Daycare doorway. The official blue door and exterior/playground are visible, with the outside playground pull clear enough to explain Jun-i's reluctance. Use the rounded coral tunnel naturally if visible.

Main subject: Jun-i stands near the entrance floor, still wearing his official blue bag. His body is slightly turned away from the doorway, with a small tucked-fin or crossed-fin posture that fits a shark body. His snout and small black button eyes angle toward the playground. He looks pouty, stubborn, and regretful, not frightened or angry.

Mari teacher: Mari gestures gently toward the door and waits without scolding. Preserve her official hair, star pin, yellow apron, name tag, purple notebook, and purple mermaid tail. Her posture is patient and low-pressure.

Banguli: Banguli floats near Jun-i, curious and worried, as a soft transparent water droplet.

Composition/framing: side-focused medium shot. Doorway on one side, playground pull on the other. Use fewer supporting friends than page 01 if needed; do not invent or simplify friends without their official reference. Leave a clean text area in the upper-right.

Text (verbatim): render exactly:

```text
"준아, 어서 오렴."
마리 선생님이 말했어요.

하지만 준이는
입을 삐죽 내밀고 말했어요.

"아직 안 들어갈래!"
```

Constraints: Jun-i remains the official blue shark child with small button eyes and full shark silhouette. Mari does not pull, push, scold, or point sharply.
Avoid: changed Jun-i eyes, round whale-like Jun-i, human hands/feet added to sea children, teacher grabbing Jun-i, crowded doorway, random Korean text, pseudo-writing, old generated candidate contamination, watermark.

### QA Before Accepting

- Text is exact and readable.
- Jun-i's official shark silhouette and blue bag are intact.
- Mari teacher is patient, not scolding or pulling.
- The doorway/playground conflict is visually clear.
- No unreferenced background friends are invented.

## Page 03 - 싫어싫어 파도

### Output

`03_candidate_text_restart_v1.png`

### References To Attach

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`

### Exact Page Text

```text
준이는 발을 쿵쿵 굴렀어요.
"싫어! 싫어!
안 들어갈래!"

준이 마음속에는
커다란 싫어싫어 파도가
출렁였어요.
```

### Prompt

Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: official exterior/playground, official coral tunnel, official Jun-i, official Banguli, official Tori, official Mongle, official Lulu.

Scene/backdrop: outside near the daycare entrance and playground path. Use the official exterior/playground reference and keep the setting warm, readable, and safe.

Main subject: Jun-i's big feeling bursts out. He wears his official blue arrival bag. He stomps/taps in a toddler-safe way or taps his shark tail, showing protest without aggression. Preserve the official Jun-i design: projecting snout, small black oval button eyes, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. His mouth may open for "싫어!", but do not enlarge teeth or make him predatory.

Story lock: do not show, write, imply, or speech-bubble the idea "밖에 더 있고 싶어." This page shows only Jun-i's outer protest and the symbolic feeling wave.

Emotion symbol: the "싫어싫어 파도" is a soft symbolic feeling wave around Jun-i: rounded blue water ribbons, bubbles, gentle motion lines, and tiny safe sand/water splashes. It is not a real dangerous wave and should not threaten anyone.

Supporting characters: Banguli bounces in surprise near Jun-i. Tori, Mongle, and Lulu watch from a little distance with concern and surprise, not judgment. Keep them far enough not to crowd or shame Jun-i, but preserve their official silhouettes and details. Lulu must retain her long snout, spiny dotted ridge, head ornament, fin, and curled tail.

Composition/framing: dynamic low toddler-eye view. Jun-i is large enough for the official snout, eye shape, gills, fins, tail, and bag to be clear. Keep clean text space at the top or upper side.

Text (verbatim): render exactly:

```text
준이는 발을 쿵쿵 굴렀어요.
"싫어! 싫어!
안 들어갈래!"

준이 마음속에는
커다란 싫어싫어 파도가
출렁였어요.
```

Constraints: big emotion without fear. Official-reference fidelity over cute simplification. Friends respond with concern, not ridicule.
Avoid: phrase/visual meaning "밖에 더 있고 싶어", dangerous wave, attack pose, scary teeth, large changed eyes, shaming crowd, generic supporting characters, pseudo-writing, random text, old generated candidate contamination, watermark.

### QA Before Accepting

- Text is exact and readable.
- Page does not reveal "밖에 더 있고 싶어."
- Jun-i remains official, childlike, and safe despite the protest.
- Wave reads as symbolic emotion, not disaster.
- Tori, Mongle, and Lulu are concerned observers, not a crowd.

## Batch 1 QA Gate

Before promoting or continuing to batch 2, each accepted candidate must pass:

- Character identity: Jun-i, Mari, Banguli, and any visible friends match their individual official references.
- Text: exact Korean text is present, readable, and not paraphrased. If text fails but art passes, keep the art candidate separate for text repair.
- Continuity: Jun-i wears his blue bag on pages 01-03; cover may also show it.
- Story: page 03 does not reveal the underlying "wanted to stay outside longer" reason; Jun-i first says it on page 05.
- Background: exterior/playground stays consistent with official daycare references and the coral tunnel continuity.
- Contamination: no prior failed episode image, generic character redesign, random signage, or pseudo-writing leaks in.
