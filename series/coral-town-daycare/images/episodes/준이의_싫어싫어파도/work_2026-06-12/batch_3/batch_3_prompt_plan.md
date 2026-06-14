# Batch 3 Prompt Plan - 준이의 싫어싫어파도 - 2026-06-12

Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. Official reference PNGs are the visual truth. Generated candidates can inform story continuity only; do not use rejected or superseded page images as character truth.

Scope: pages 07-09. Generate and QA one page at a time. Do not promote anything to `final` in this batch.

## Shared Batch 3 Locks

- Continue the accepted Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, and gentle toddler picture-book emotion.
- Avoid the rejected smooth 3D/plastic look.
- Do not use old 2026-06-11 page candidates as visual truth.
- Pages 07-08 are still arrival-time exterior continuity, so Jun-i keeps his official blue arrival bag.
- Page 09 is inside the classroom, so Jun-i and friends must not wear their bags; bags can be stored on hooks, shelves, cubbies, or beside chairs.
- Page 06 candidate can inform story continuity only. The official shell hourglass truth remains `work_2026-06-11/reference_assets/shell_hourglass_ref.png`.
- Page 04 v1 background-friend drift must not guide later friends. Use individual official character PNGs.

## Page 07 - 파도가 작아졌어요

Output: `batch_3/07_candidate_2026-06-12_v1.png`

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
Asset type: Korean toddler picture-book page 07
Primary request: Create page 07 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: official exterior/playground and coral tunnel are setting truth; official Jun-i, Mari teacher, Banguli, and shell hourglass are character/prop truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, layered coral details, gentle toddler picture-book emotion. Avoid smooth 3D, plastic toy texture, glossy CG, or over-clean rendering.

Scene/backdrop: outside between the Coral Town Daycare entrance and playground. This is a quiet waiting moment after Mari offered the shell hourglass. The daycare blue door and a soft hint of the coral tunnel/playground may appear, but the page should feel calmer and more spacious than the earlier conflict pages.

Main subject: Jun-i waits outside beside the small shell hourglass. He still wears his official blue arrival bag. His posture is quieter and less tense, looking at the playground, small bubbles, or the hourglass while calming down. Preserve official Jun-i exactly: projecting shark snout, tiny black oval button eye, no eyebrow, no eyelid line, white lower face/belly boundary, three gill marks, dorsal fin, side fins, long shark tail, sailor shirt, blue shorts, and blue shell-decorated shoulder bag.

Supporting subjects: Mari teacher waits nearby with a warm patient expression, not controlling Jun-i. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. Banguli floats near Jun-i with a calmer worried-to-relieved expression. Far inside the doorway, friends may be tiny silhouettes waving gently, but only if they do not distract or drift off-reference.

Emotion wave lock: show the `싫어싫어 파도` much smaller than page 03: a few soft rounded blue ripples or small bubble arcs near Jun-i, not a dangerous real wave.

Prop lock: shell hourglass must match `shell_hourglass_ref.png`: small shell top and bottom, transparent rounded glass body, warm sand-colored grains, thin stream of sand falling in the center. Do not add jewels, metal frame, clock numbers, wings, handles, or magic glow.

Composition/framing: calm medium-wide shot with generous upper text space. Use a stable quiet composition; Jun-i and the hourglass should be easy to read.

Text (verbatim): render exactly with these line breaks:
모래가 사르르 내려갔어요.
준이는 바깥을 바라보며
조금 기다렸어요.

싫어싫어 파도도
조금씩 작아졌어요.
출렁... 출렁...

Constraints: Mari must not scold, pull, push, or hurry. Jun-i's blue bag remains visible. The hourglass must be small and consistent. The wave is symbolic and gentle.
Avoid: scary wave, forcing Jun-i inside, missing hourglass, jeweled/magical hourglass, changed Jun-i eye shape, missing bag, random Korean text, pseudo-writing, smooth 3D/plastic texture, watermark.
```

QA:

- Text exact and readable.
- Jun-i keeps official shark identity and blue bag.
- Shell hourglass matches the reference.
- The wave is clearly smaller and symbolic.
- Mari waits rather than forcing.

## Page 08 - 이제 들어갈래

Output: `batch_3/08_candidate_2026-06-12_v1.png`

References to load:

- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

Prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 08
Primary request: Create page 08 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: official exterior/playground and coral tunnel are setting truth; official Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, and shell hourglass are character/prop truth.

Style/medium: match the Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, gentle toddler picture-book mood.

Scene/backdrop: at the Coral Town Daycare blue doorway, showing both outside and a warm glimpse inside. The shell hourglass is nearby with the sand finished. This is the transition from waiting outside to choosing to enter.

Main subject: Jun-i chooses to go in by himself. He still wears his official blue arrival bag and takes a small step toward the doorway. His expression is shy, calmer, and a little proud. Preserve his official shark shape: projecting snout, tiny black oval button eye, no eyebrow, no eyelid line, white lower face/belly, three gill marks, dorsal fin, side fins, long tail, sailor shirt, blue shorts, and blue shell-decorated bag.

Mari teacher smiles warmly and lets Jun-i decide; she does not push, pull, or block him. Preserve official Mari details: half-up bob, star hairpin, yellow apron with name tag, cream blouse, purple attendance notebook, and purple mermaid tail.

Supporting characters: Tori, Mongle, and Lulu may appear inside the doorway, welcoming gently from a distance. They must match their official references: Tori green turtle with yellow hat and shell; Mongle purple octopus with yellow beret, sailor collar, and visible tentacles; Lulu pink seahorse with long snout, ridge, fin, curled tail, sailor outfit, and yellow bag. Banguli floats near Jun-i with a relieved expression.

Prop lock: shell hourglass matches `shell_hourglass_ref.png`, with shell top/bottom and sand fully settled. It should be visible but not oversized.

Composition/framing: doorway transition composition, with outside foreground and inside background both visible. Leave clean text space in the upper-left or upper-right.

Text (verbatim): render exactly with these line breaks:
모래가 다 내려가자
마리 선생님이 물었어요.

"이제 어떻게 할까?"

준이는 조용히 말했어요.
"이제... 들어갈래."

Constraints: Jun-i moves by choice. Mari must not drag or push. Friends welcome but do not crowd. Keep Jun-i's bag visible.
Avoid: teacher forcing, crowd pressure, missing hourglass, changed Jun-i eye shape, off-reference friends, random Korean text, pseudo-writing, smooth 3D/plastic texture, watermark.
```

QA:

- Text exact and readable.
- Jun-i chooses to enter by himself.
- Mari does not push or pull.
- Shell hourglass is consistent with page 06-07.
- Doorway transition is clear.

## Page 09 - 말로 말하면 돼요

Output: `batch_3/09_candidate_2026-06-12_v1.png`

User QA carry-forward:

- `09_candidate_2026-06-12_v2.png` omitted Sua and Popo. For the next retry, Sua and Popo are required visible classmates, not optional background extras. If crowding becomes a problem, omit Aru first and keep Tori/Mongle/Lulu smaller, but do not remove Sua or Popo.

References to load:

- `series/coral-town-daycare/references/배경_교실.png`
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
Asset type: Korean toddler picture-book page 09
Primary request: Create page 09 of `준이의 싫어싫어파도` in A5 portrait proportion. Use only the official loaded reference images as visual truth.
Input images: official classroom is setting truth; official Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua are character truth.

Style/medium: match the official Sanho Village Daycare watercolor and colored-pencil paper texture: warm paper grain, soft hand-drawn edges, low-saturation pastel palette, gentle toddler picture-book warmth. Avoid smooth 3D, plastic toy texture, glossy CG, or over-clean rendering.

Scene/backdrop: inside the official classroom. Children sit together in a soft circle or small activity group. The mood is settled and safe after Jun-i entered. Use coral classroom furniture, shells, rounded windows, cubbies/hooks, and warm underwater light. Keep the classroom readable but not too busy.

Main subject: Jun-i is calmer and brighter, sitting with friends or raising a small hand to speak. He is not wearing his blue bag indoors. Preserve official Jun-i shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor shirt, and blue shorts. His blue bag may be stored on a hook, cubby, shelf, or beside a chair.

Mari teacher watches nearby with a warm supportive smile. Preserve official Mari details: half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, purple mermaid tail.

Friends: Tori, Mongle, Lulu, Aru, Popo, Sua, and Banguli may appear as a gentle classroom group. Use individual official references as visual truth. Aru must remain a round orange pufferfish child with small spikes/fins and no human body or legs. Popo must remain a moon jellyfish child with translucent bell, subtle internal pattern, sailor collar, and soft tentacles; do not give Popo prominent eyes unless very subtle. Sua must remain a purple seahorse child with long snout, ridge, curled tail, and blue sailor outfit. No children wear arrival bags indoors.

Composition/framing: calm classroom group scene, slightly overhead or mid-wide, with a clean text area on one side of the classroom wall or floor. Keep all visible characters small but on-model; reduce the number of visible friends rather than drifting off-reference.

Text (verbatim): render exactly with these line breaks:
어린이집 안으로 들어온 준이는
친구들과 함께 앉았어요.

이제 준이는 알았어요.
싫은 마음은 말해도 돼요.
쿵쿵하기보다
말로 말하면 돼요.

Constraints: no bags worn indoors. Jun-i is emotionally recovered but not overexcited. Friends are supportive, not laughing at him. Use official character species and details.
Avoid: bags on children indoors, Aru with human legs/body, Popo with big human eyes, off-reference friends, random Korean text, pseudo-writing, smooth 3D/plastic texture, watermark.
```

QA:

- Text exact and readable.
- Classroom matches official reference.
- No child wears a bag indoors.
- Jun-i looks calm/recovered and official.
- Group friends remain on-model enough for review.
