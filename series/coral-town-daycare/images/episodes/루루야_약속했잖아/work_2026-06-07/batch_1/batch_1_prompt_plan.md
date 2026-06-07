# Batch 1 Prompt Plan - 2026-06-07

## Scope

- Episode: `루루야, 약속했잖아`
- Script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아.md`
- TTS script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아_tts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Page plan: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/page_plan.md`
- Worklog: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/episode_worklog.md`
- Work folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/batch_1`
- Candidate filenames: `00_candidate_text_v1.png`, `01_candidate_text_v1.png`, `02_candidate_text_v1.png`, `03_candidate_text_v1.png`
- Regeneration filenames after user QA: `00_candidate_text_v2.png`, `01_candidate_text_v2.png`, `02_candidate_text_v2.png`, `03_candidate_text_v2.png`

## Official References

- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Lulu's favorite picture book: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

## Shared Hard Locks

- A5 portrait page proportion, about `1:1.414`.
- Generate illustration and exact Korean story text together.
- Use actual official reference image files as visual truth, not prose descriptions alone.
- Keep a clean, readable text area. If exact Korean text cannot be cleanly rendered, leave a clean blank text area rather than inventing wrong text.
- Style: soft toddler picture-book watercolor and colored-pencil texture, warm paper feel, low-saturation pastel palette.
- Avoid neon colors, harsh highlights, plastic 3D toy texture, dense props, scary expressions, pseudo-writing, extra signs, random labels, human legs/feet, and unrelated previous episode details.
- Same-face repetition is forbidden. Characters must have distinct eyes, mouths, postures, and rhythms.
- Preserve the delicate painted reference style for every character. Do not simplify characters into generic round sea-animal children; keep each reference's texture, ridges, fins, tentacles, clothing seams, collars, scarves, and ornaments.
- Bags are not worn in batch 1. These are indoor classroom play/promise scenes, not arrival or departure. Omit bags from the bodies. If a bag must appear, place it in a classroom cubby, on a wall hook, or near a shelf as background storage.
- Batch 1 v2 success is primarily visual: character reference fidelity, no worn bags, Aru/Popo body correctness, and Lulu/Sua fine detail. Text may be accepted if readable and close, but a visually wrong character is a failure.
- Batch 1 v2/v3 user QA on 2026-06-08: still not acceptable. Overall characters became too round compared with the references, Aru gained a separate attached body/torso, and Popo had visible eyes without a special direction. Do not continue from v2/v3 as approved candidates.

## Lulu / Sua Detail Locks

- Lulu is not just a pink seahorse silhouette. Preserve the actual `루루.png` design: coral-pink body, long tube snout with round opening, small black eyes, dotted/ridged skin texture, crown-like spiny head ridge with small bead tips, green coral and shell head ornament, cream sailor top with pink collar and scarf, mauve pleated skirt, translucent pink back fin, curled tail. Do not put her yellow bag on her body in batch 1.
- Lulu should keep her chatty gesture when appropriate: small hand/fin near her mouth, lively open mouth, bright expression. For page 3, keep the same detailed body while changing emotion to a cute pout and slightly moist eyes.
- Sua appears in page 1 as a background friend. Even if small, she must remain the purple seahorse from `수아.png`: slender purple seahorse body, dotted/spiny head ridge, long tube snout, blue sailor outfit, curled tail. Do not put her mint bag on her body in batch 1. Do not simplify her into a generic purple child, fish, or blob.

## Aru / Popo Detail Locks

- Aru must match `아루.png`: a round orange pufferfish child with a true single pufferfish body, small spikes, small fins, pufferfish mouth, and sailor scarf wrapped around the pufferfish body. Never add human hands, human feet, human legs, a separate belly/torso, or a human-like lower body. Do not turn Aru into a child body with a fish head.
- Popo must match `포포.png`: pale sky-blue moon jellyfish child with a round translucent dome, subtle moon-jelly pattern inside the bell, small sailor collar, soft long tentacles, and a childlike floating proportion. Unless the page explicitly calls for eye expression, Popo's eyes should be hidden or barely visible; express emotion with the mouth, dome tilt, and tentacle movement. Do not shrink Popo into a tiny generic jellyfish or draw ordinary visible eyes.

## Picture Book Prop Lock

- Pages 2 and 3 must use the same favorite picture book from `lulu_favorite_picture_book_ref.png` once generated.
- The book is a small toddler board book with rounded corners, pastel seafoam/aqua cover, pink coral border, warm yellow shell emblem, cream page edges, and a tiny pink ribbon or shell tab.
- Do not turn the book into a notebook, tablet, signboard, school worksheet, random book with pseudo-writing, or a second story title.

## Page 00 - Cover

### Output

`00_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

### Exact Page Text

```text
루루야, 약속했잖아

— 지킨 약속은 반짝반짝 —
```

### Prompt

Create the cover page for the Korean toddler picture book `루루야, 약속했잖아` in the Coral Town Daycare series. Use the official reference images as visual truth.

Scene: a bright, warm daycare classroom. Lulu and Jun-i are centered, facing each other and making a pinky-promise gesture. The promise moment should feel warm, joyful, and safe.

Lulu: use the exact Lulu reference. She is a coral-pink seahorse child with a detailed spiny head ridge, bead-like ridge tips, dotted/ridged skin texture, long tube snout, small black eyes, coral-and-shell head ornament, cream sailor top with pink collar/scarf, mauve pleated skirt, translucent pink back fin, and curled tail. She smiles brightly with one small hand/fin near her mouth and the other reaching for the promise gesture. Do not simplify her. Do not put her yellow bag on her body in this classroom cover; if visible at all, it belongs on a classroom hook or cubby.

Jun-i: use the exact Jun-i reference. He is a blue shark child with white belly, shark snout, dorsal fin, tail, small teeth, and sailor outfit. He smiles courageously and gently reaches his small fin/hand toward Lulu for the promise. Do not put his blue bag on his body in this classroom cover; if visible at all, it belongs on a classroom hook or cubby.

Banguli: use the exact Banguli reference. A soft pale sky-blue transparent droplet floats beside them, nodding happily, with two or three tiny droplets.

Background: keep the official classroom reference soft and simple: rounded windows, shell-shaped shelves, picture books, toy shelf. Do not let background details compete with the characters.

Composition: A5 portrait. Leave clean title space at the top and subtitle space near the bottom. Main focus is Lulu and Jun-i facing each other. Render the exact Korean text if possible:

```text
루루야, 약속했잖아

— 지킨 약속은 반짝반짝 —
```

If exact Korean text cannot be cleanly rendered, leave blank title/subtitle areas rather than inventing wrong text.

## Page 01 - 재잘재잘 루루

### Output

`01_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`

### Exact Page Text

```text
루루는 말이 많아요.

"이거 하자!"
"저거도 하자!"
"이따 또 놀자!"

재잘재잘.
조잘조잘.

루루는 오늘도
신이 났어요.
```

### Prompt

Create page 1 of the Korean toddler picture book `루루야, 약속했잖아`. Use the official reference images as visual truth.

Scene: morning free-play time in the Coral Town Daycare classroom. Lulu moves busily and cheerfully between friends, chatting and inviting them to play. The emotional tone is bright, talkative, and lively.

Lulu: preserve the exact Lulu reference details. She is a coral-pink seahorse child with spiny dotted head ridge, long tube snout, coral head ornament, sailor outfit, translucent back fin, and curled tail. She is the focus, moving through the room with one small hand/fin near her mouth, mouth open as if chattering, small fins fluttering. Do not reduce her to a generic smooth pink seahorse. Do not put her yellow bag on her body.

Friends around her:
- Aru is the orange round pufferfish child from the official reference: true pufferfish body, small spikes, little fins, pufferfish mouth, and sailor scarf. No human hands, feet, legs, or humanoid torso.
- Mongle is the purple octopus child with yellow beret and sailor collar from the official reference.
- Sua is the purple seahorse child from the official reference. Even if small, keep her spiny dotted head ridge, long snout, blue sailor outfit, and curled tail. Do not put her mint bag on her body. Do not make her a generic purple child or fish.
- Tori is the green turtle child with yellow hat from the official reference.
- Popo is the pale sky-blue moon jellyfish child from the official reference: translucent dome, subtle moon-jelly pattern, small sailor collar, soft long tentacles, floating childlike proportion. Do not shrink Popo into a small generic jellyfish and do not overemphasize eyes.

Banguli floats after Lulu, soft pale sky-blue and transparent, with two or three tiny droplets.

Background: use the official classroom reference softly: rounded windows, shell decorations, toy shelves, low tables. Keep it readable and not cluttered.

Composition: A5 portrait, lively wide-medium classroom view. Show Lulu's path between friends. Each friend should have a different posture; no copied faces. Leave a clean text area at the top or one side. Render the exact Korean text if possible:

```text
루루는 말이 많아요.

"이거 하자!"
"저거도 하자!"
"이따 또 놀자!"

재잘재잘.
조잘조잘.

루루는 오늘도
신이 났어요.
```

If exact Korean text cannot be cleanly rendered, leave a clean blank text area.

## Page 02 - 준이야, 이따 꼭 돌려줘

### Output

`02_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`

### Exact Page Text

```text
루루는 아끼는
그림책을
준이에게 빌려줬어요.

"준이야,
이따 꼭 돌려줘.

약속이야!"

"응! 약속!"

준이가 새끼 손가락을
걸었어요.
```

### Prompt

Create page 2 of the Korean toddler picture book `루루야, 약속했잖아`. Use the official reference images as visual truth.

Scene: Lulu lends her favorite picture book to Jun-i and asks him to promise he will return it. The moment is gentle, trusting, and clear.

Lulu: preserve the exact Lulu reference details: coral-pink seahorse child, spiny dotted head ridge with bead tips, long tube snout, small black eyes, coral-and-shell head ornament, sailor outfit, translucent back fin, curled tail. She looks kind but definite, one hand/fin near her mouth as she speaks, the other offering the book or making the promise gesture. Do not put her yellow bag on her body in this classroom scene.

Jun-i: preserve the exact blue shark child reference with white belly, shark fins, tail, small teeth, and sailor outfit. He receives the book and answers cheerfully, making a promise gesture. Do not put his blue bag on his body in this classroom scene.

Book: use the exact favorite picture book prop reference if available. The favorite picture book is the visual center between Lulu and Jun-i: small rounded board book, pastel seafoam/aqua cover, pink coral border, warm yellow shell emblem, cream page edges, and a tiny pink ribbon or shell tab. It should not be a notebook, sign, tablet, worksheet, or book with invented writing.

Banguli floats nearby, nodding like a witness to the promise, soft transparent sky-blue droplet, with two or three tiny droplets.

Composition: A5 portrait, close medium shot of the two friends, book centered between them, one clean text area on the side. Classroom background is soft and simple. Render the exact Korean text if possible:

```text
루루는 아끼는
그림책을
준이에게 빌려줬어요.

"준이야,
이따 꼭 돌려줘.

약속이야!"

"응! 약속!"

준이가 새끼 손가락을
걸었어요.
```

If exact Korean text cannot be cleanly rendered, leave a clean blank text area.

## Page 03 - 어? 아직 안 돌려줬네

### Output

`03_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

### Exact Page Text

```text
조금 뒤,
루루는 그림책을
보고 싶었어요.

그런데 준이는
블록 놀이에
푹 빠져 있었어요.

그림책은
바닥에 그냥—

루루는 입을
삐죽 내밀었어요.

"약속했잖아……"
```

### Prompt

Create page 3 of the Korean toddler picture book `루루야, 약속했잖아`. Use the official reference images as visual truth.

Scene: a little time has passed. Lulu wants to read her picture book, but Jun-i has forgotten the promise and is absorbed in block play. The borrowed picture book lies on one side of the classroom floor. Lulu feels disappointed, but the scene must stay gentle and not heavy.

Lulu: preserve the exact Lulu reference details even in an emotional close-medium shot. Coral-pink seahorse child, spiny dotted head ridge with bead tips, long tube snout, coral head ornament, sailor outfit, translucent back fin, curled tail. Her mouth is a small pout, eyes slightly moist, and her curled tail turns inward more than usual. Do not put her yellow bag on her body. Do not simplify or smooth away her head ridge, dots, outfit, fin, or tail.

Jun-i: blue shark child from the official reference, in the background or mid-background, happily focused on block play. Keep him friendly and unaware, not mean. Preserve shark body, white belly, fins, tail, small teeth, and sailor outfit. Do not put his blue bag on his body.

Book: use the same favorite picture book prop reference from page 2 if available. The small rounded board book lies on the floor between or near them, clearly visible and safe, not damaged or dirty. Its pastel seafoam/aqua cover, pink coral border, yellow shell emblem, cream page edges, and tiny pink ribbon/shell tab should make it recognizable as the same cherished book.

Banguli floats beside Lulu with a puzzled tilted expression, soft pale sky-blue transparent droplet, with two or three tiny droplets.

Composition: A5 portrait, Lulu in front with her cute disappointed pout clearly visible; Jun-i farther back playing with blocks. Show the distance contrast between them. Keep classroom background soft. Leave a clean text area. Render the exact Korean text if possible:

```text
조금 뒤,
루루는 그림책을
보고 싶었어요.

그런데 준이는
블록 놀이에
푹 빠져 있었어요.

그림책은
바닥에 그냥—

루루는 입을
삐죽 내밀었어요.

"약속했잖아……"
```

If exact Korean text cannot be cleanly rendered, leave a clean blank text area.

## Batch 1 QA Checklist

- No character wears a bag in batch 1. Bags are omitted or stored in the classroom background only.
- Lulu matches `루루.png`: head ridge, bead tips, dots/ridges, snout, coral ornament, outfit, translucent fin, curled tail, not simplified.
- Sua, if visible on page 1, matches `수아.png`: purple seahorse, blue sailor outfit, curled tail, detailed head ridge and snout, not generic.
- Aru, if visible on page 1, matches `아루.png`: true pufferfish body and sailor scarf, no human hands/feet/torso.
- Popo, if visible on page 1, matches `포포.png`: moon jellyfish dome, subtle pattern, sailor collar, soft tentacles, not a tiny generic jellyfish.
- Jun-i matches `준이.png`: blue shark body, white belly, fins, small teeth, sailor outfit, no humanized hands/feet.
- Banguli matches `방울이.png`: soft droplet, transparent pastel, simple face, tiny droplets.
- Korean text is exact, readable, and not paraphrased; otherwise the text area is blank for later text pass.
- The same picture book design appears on pages 2 and 3.
- A5 portrait proportion is preserved.
- No unrelated previous episode details, extra signs, pseudo-writing, or harsh conflict mood.
