# Batch 4 Prompt Plan - 준이의 싫어싫어파도 - 2026-06-13

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. Generated candidates can inform story continuity only; do not use rejected or superseded page images as character truth.

Scope: page 10. Generate and QA one page at a time. Do not promote anything to `final` in this batch.

## Shared Batch 4 Locks

- Continue the accepted Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, and gentle toddler picture-book emotion.
- Avoid the rejected smooth 3D/plastic look.
- Do not use old 2026-06-11 page candidates as visual truth.
- Page 10 is dismissal time outside the daycare, so Jun-i and friends may wear their official arrival/dismissal bags again.
- Page 09 v4 is accepted review context for emotional continuity only. Official reference PNGs remain the character truth.
- The ending should feel warm and resolved, not like a new conflict or a crowded action scene.

## Page 10 - 준이 마음도 맑음

Output: `batch_4/10_candidate_2026-06-13_v1.png`

References to load:

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
- `series/coral-town-daycare/references/characters/수아.png`

Prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 10
Primary request: Create page 10 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: official exterior/playground and coral tunnel are setting truth; official Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua are character truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, gentle toddler picture-book emotion. Avoid smooth 3D, plastic toy texture, glossy CG, or over-clean rendering.

Scene/backdrop: dismissal time outside Coral Town Daycare. Use the official exterior/playground reference with the daycare entrance, warm coral details, blue door, and a natural hint of the coral tunnel/playground. The light is soft late-afternoon peach-gold underwater glow, not harsh sunset drama.

Main subject: Jun-i is bright and calm at the end of the day, smiling and waving goodbye. He may wear his official blue shell-decorated dismissal bag again. Preserve official Jun-i exactly: projecting shark snout, small black oval button eye, no eyebrow, no eyelid line, white lower face/belly boundary, three gill marks, dorsal fin, side fins, long shark tail, sailor shirt, blue shorts, and blue bag. He should look confident and emotionally settled, not wild or overexcited.

Mari teacher: near the doorway, warmly waving goodbye. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. She should look proud and gentle, not tearful or dramatic.

Friends: Tori, Mongle, Lulu, Aru, Popo, Sua, and Banguli may appear as a cheerful but not crowded dismissal group. Use individual official references as visual truth. Since this is dismissal time, friends may wear their official bags again. Aru must remain a round orange pufferfish child with small spikes/fins and no human body or legs. Popo must remain a moon jellyfish child with translucent bell, subtle internal pattern, sailor collar, and soft tentacles; do not give Popo prominent human eyes. Sua must remain a purple seahorse child with long snout, ridge, curled tail, and blue sailor outfit. Reduce or partially background some friends rather than drifting off-reference.

Composition/framing: warm wide closing page outside the daycare. Jun-i should be the clear emotional focus in the lower/middle area, waving toward Mari teacher or toward the viewer. Friends and Banguli support the ending without crowding Jun-i. Leave clean upper text space in the sky/water-light area.

Text (verbatim): render exactly with these line breaks:
하원 시간이 되었어요.
준이는 활짝 웃으며 말했어요.

"내일도 올래!"

산호마을 어린이집은
오늘도 맑음.
준이 마음도
조금씩 맑음.

Constraints: page 10 is outside dismissal, so bags are allowed again. The mood is resolved, warm, and safe. Jun-i's official shark silhouette and small black oval eye must stay intact. Mari must be supportive, not pulling or pushing. Friends should be on-model enough for review.
Avoid: indoor classroom setting, missing Jun-i bag if a dismissal bag is shown on friends, scary wave, new conflict, off-reference friends, Aru with human legs/body, Popo with big human eyes, random Korean text, pseudo-writing, misspelled Korean, smooth 3D/plastic texture, watermark.
```

QA:

- Text exact and readable.
- Exterior/daycare matches official reference and feels like dismissal time.
- Jun-i is calm, happy, official, and may wear his blue bag again.
- Mari waves warmly and does not control Jun-i.
- Friends remain on-model enough for review; bags are acceptable because this is dismissal.
- No page 09 indoor no-bag rule is accidentally carried into page 10.
