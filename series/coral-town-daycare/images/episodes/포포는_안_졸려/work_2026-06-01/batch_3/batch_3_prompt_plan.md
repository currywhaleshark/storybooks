# Batch 3 Prompt Plan - Popo Naptime Story

## Scope

Generate candidate pages 8-12 only. Do not overwrite or regenerate approved final pages 0-7.

Candidate filenames:

- `08_candidate_text_v1.png`
- `09_candidate_text_v1.png`
- `10_candidate_text_v1.png`
- `11_candidate_text_v1.png`
- `12_candidate_text_v1.png`

Stop for QA/user review before promoting anything into `final/`.

## Shared Format And Style

- Portrait storybook page matching existing finals, approximately 3:4 vertical.
- Warm watercolor and colored-pencil texture, soft paper grain, low-saturation pastel colors.
- Generate the Korean story text directly inside the image.
- Use the existing episode text panel style when helpful: cream rounded rectangular panel with small coral/shell decorations, readable black Korean text, no text over faces or main action.
- Avoid pseudo-writing, extra signs, speech bubbles, random labels, neon highlights, glossy 3D, scary darkness, and unrelated prior-episode details.

## Official Visual References

Use these actual files as visual truth:

- `series/coral-town-daycare/references/characters/포포.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/수아.png`
- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
- `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`

Continuity pages inspected:

- `final/04_페이지.png`: approved nap-room bed map and page text panel style.
- `final/05_페이지.png`: playground/exterior, Aru scarf visible.
- `final/06_페이지.png`: sleepy Popo, playground height contrast.
- `final/07_페이지.png`: Popo low and disappointed below friends; use as direct emotional lead-in for page 8.

## Carry-Forward Locks

- Popo's translucent jellyfish bell itself is Popo's face. Do not draw a separate head, face, body, cheeks, human limbs, or hair under the bell.
- Popo has a pale sky-blue translucent scalloped bell, white moon-jellyfish flower pattern inside the bell, small mouth on the bell, soft thin tentacles, and small sailor collar.
- Popo should not have drawn eyes unless the user explicitly asks for eyes. Express Popo's emotion only through the mouth, bell shape/tilt/droop/lift, and tentacle movement.
- Do not add Popo's bag in pages 8-11. Page 12 may omit the bag to preserve the current episode continuity unless the scene clearly needs it.
- Banguli is one separate tiny pale-blue water droplet mascot. Do not duplicate Banguli.
- Mari teacher is a warm mermaid teacher with brown half-up bob hair, star hairpin, cream blouse, yellow apron/name tag, purple mermaid tail. She should look like a daycare teacher, not a princess.
- Aru is a round orange pufferfish with side fins only. No human hands, fingers, arms, or gloves. In playground pages, Aru's red-and-white sailor scarf should be visible.
- Lulu and Sua must remain seahorses with long tube snouts and curled tails.
- Friends should react warmly, not competitively or mockingly.
- Keep Popo tired and learning, not shamed.

## Page 8 - Mari Notices Popo

Output: `08_candidate_text_v1.png`

References:

- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Continuity: `final/07_페이지.png`

Exact story text:

```text
마리 선생님이
포포를 보았어요.

선생님은 무릎을 굽혀
포포랑 눈을 맞췄어요.

"포포야,
많이 졸리구나."

포포는 작게
끄덕였어요.

"낮잠 시간에
푹 쉬지 못했지?"

포포의 갓이
더 처졌어요.

"……응."
```

Prompt:

```text
Use case: illustration-story
Asset type: Korean children's storybook page, portrait 3:4.
Primary request: Generate page 8 of the Popo naptime story with Korean story text rendered directly in the image.
Input images: official Popo reference; official Banguli reference; official Mari teacher reference; official playground/exterior reference; approved final page 7 for emotional and layout continuity.
Scene/backdrop: bright Coral Town daycare playground/exterior, matching the approved page 7 coral building, slide, sandy path, pastel underwater sunlight, and soft watercolor texture.
Subject: Mari teacher gently notices tired Popo and lowers herself to Popo's eye level.
Composition/framing: close medium shot. Keep the cream rounded Korean text panel on the left side, similar to pages 5-7. On the right, Mari bends or lowers herself warmly toward low-floating Popo so their eye level meets. Banguli floats beside Popo with a worried face. Background friends are soft and secondary.
Style/medium: warm Korean picture-book watercolor and colored pencil, soft paper grain, low-saturation pastel.
Lighting/mood: gentle afternoon playground light, reassuring, warm, safe.
Text (verbatim): "마리 선생님이
포포를 보았어요.

선생님은 무릎을 굽혀
포포랑 눈을 맞췄어요.

\"포포야,
많이 졸리구나.\"

포포는 작게
끄덕였어요.

\"낮잠 시간에
푹 쉬지 못했지?\"

포포의 갓이
더 처졌어요.

\"……응.\""
Constraints: Popo's bell itself is the face; no separate head, body, cheeks, human limbs, hair, or bag. Popo is pale sky-blue translucent with scalloped bell, white moon-jellyfish flower inside the bell, small sad mouth on the bell, no drawn eyes, drooping thin tentacles, small sailor collar. Express Popo's emotion only with the mouth, bell droop, bell tilt, and tentacle posture. Mari has half-up brown bob hair, star hairpin, cream blouse, yellow apron with name tag, purple mermaid tail; she is kind and not scolding. Banguli appears exactly once as a tiny pale-blue droplet mascot with two or three tiny droplets. Friends in background are soft and not teasing.
Avoid: visible eyes on Popo, scolding gestures, finger pointing, speech bubbles, random labels, pseudo-writing, duplicate Banguli, Popo bag, Popo as a simple droplet, human arms/legs on sea-creature children, glossy 3D, neon highlights.
```

## Page 9 - Naps Gather Strength

Output: `09_candidate_text_v1.png`

References:

- Popo, Banguli, Mari teacher.
- Playground/exterior or simplified activity-area backdrop, keeping page 8 emotional continuity.

Exact story text:

```text
마리 선생님이
두 손을 동그랗게 모았어요.

"포포야,
낮잠은 말이야—

오후에 신나게 놀
힘을 모으는 시간이란다."

"푹 자고 나면
힘이 가득 모여서

높이높이
떠오를 수 있어."

포포의 입이
동그래졌어요.

"아……
그래서 친구들이
쌩쌩했구나!"
```

Prompt:

```text
Generate page 9 as a close medium storybook page. Mari teacher is the visual center, warmly cupping both round hands to show "strength gathering" like a small glowing but non-sparkly warm circle of gathered energy. Popo listens with a drooped but attentive jellyfish bell, then has a small round "아..." mouth of realization. Banguli nods beside Popo with two or three tiny droplets moving up and down. Use the same watercolor style and left or upper cream text panel. Keep the tone gentle and explanatory, like sharing a secret, never scolding.
Render the exact Korean story text above directly in the image.
Apply all shared Popo, Mari, Banguli, text, and avoid locks. Popo must have no visible/drawn eyes; use only the mouth, bell, and tentacles for expression.
```

## Page 10 - Popo Rests Softly

Output: `10_candidate_text_v1.png`

References:

- Popo, Banguli, Mari teacher.
- `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
- Approved final pages 1-4 for nap-room continuity.

Exact story text:

```text
마리 선생님이
폭신한 쿠션을
가져왔어요.

"지금 조금 쉬어도
괜찮아.

다음에 또 놀자."

포포는 이번엔
살래살래 하지 않았어요.

처진 갓을
쿠션에 살며시—

방울이도
옆에 딱 붙어
쌔근쌔근.

"포포야,
잘 자."
```

Prompt:

```text
Generate page 10 in the warm nap room. Popo rests willingly on a soft cushion, no bag, no resistance. Mari teacher watches gently nearby. Banguli sleeps beside Popo as one small pale-blue droplet with two or three tiny sleep bubbles/droplets. The light is warm and calm, not dark. Keep the established nap-room shell beds/cushions and cozy curtains. Use a cream Korean text panel in a quiet blank area.
Render the exact Korean story text above directly in the image.
Apply all shared Popo, Mari, Banguli, nap-room, text, and avoid locks. Popo must have no visible/drawn eyes; use only the mouth, bell, and tentacles for expression.
```

## Page 11 - Next Day Popo Settles First

Output: `11_candidate_text_v1.png`

References:

- Popo, Banguli, Mari teacher, all friends.
- `series/coral-town-daycare/references/배경_낮잠방_자는친구들_레퍼런스_v2.png`
- `series/coral-town-daycare/references/배경_낮잠방_포포침대빈_레퍼런스_v2.png`
- Approved final pages 1-4 for bed map.

Exact story text:

```text
다음 날
낮잠 시간이 왔어요.

이번에는
포포가 제일 먼저
쿠션 속으로 쏙.

둥실 떠오르지 않고
폭신하게
자리를 잡았어요.

방울이가 윙크했어요.

'오늘은 같이 자자—'

포포가 끄덕끄덕.

"응!
힘을 모을 거야."
```

Prompt:

```text
Generate page 11 as next-day nap time. Preserve the established nap-room bed map: Popo chooses the aqua/teal cushion/bed first and settles calmly, no bag, not floating away. Mari smiles proudly. Banguli winks once beside Popo. Other friends are entering or settling into their beds softly. The mood is growth and self-chosen rest. Use the same warm nap-room watercolor style and readable cream text panel.
Render the exact Korean story text above directly in the image.
Apply all shared character, nap-room bed-map, text, and avoid locks. Popo must have no visible/drawn eyes; use only the mouth, bell, and tentacles for expression.
```

## Page 12 - Popo Floats Highest

Output: `12_candidate_text_v1.png`

References:

- Popo, Banguli, Mari teacher, all friends.
- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Approved final pages 5-7 for playground and height-game continuity.

Exact story text:

```text
낮잠을 푹 자고 난
오후—

다시 둥실둥실
떠오르기 놀이!

딩— 딩— 둥실!

포포가
위로, 위로,
가장 높이—

둥실!

"우와— 포포 최고!"

친구들이
올려다보며 웃었어요.

푹 쉬었더니
힘이 가득!

산호마을 어린이집은
오늘도 맑음.

포포의 낮잠도,
포포의 오후도
반짝반짝 맑음.
```

Prompt:

```text
Generate page 12 as the bright ending. In the playground/exterior, Popo floats highest at the upper center, fully energized with a round lifted bell, white moon-jellyfish flower pattern, small happy mouth, thin tentacles spread gently, and no separate body/head. Banguli floats near Popo, exactly one droplet mascot. Friends and Mari look up warmly from below, cheering and smiling, not competing. Aru's red-and-white sailor scarf is visible and Aru has side fins only. Use a bright but soft finish, with no glittery 3D or neon. Use a readable cream Korean text panel with enough space for the longer ending text.
Render the exact Korean story text above directly in the image.
Apply all shared character, playground, text, and avoid locks. Popo must have no visible/drawn eyes; use only the mouth, bell, and tentacles for expression.
```
