# Batch 1 Prompt Plan - 기다림 이야기

## Scope

- Episode: 산호마을 어린이집의 기다림 이야기
- Batch: cover + pages 1-3
- Candidate filenames:
  - `00_candidate_v1.png`
  - `01_candidate_v1.png`
  - `02_candidate_v1.png`
  - `03_candidate_v1.png`
- Work folder:
  - `series/coral-town-daycare/images/episodes/산호마을_어린이집의_기다림_이야기/work_2026-05-28/batch_1`

## Official References

Use official references as visual truth. Do not borrow details from prior generated episode images.

- Characters:
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
- Background:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`

## Shared Visual Rules

Soft warm Korean picture-book illustration for 3-year-old children. Gentle paper texture, pastel mid-saturation colors, rounded childlike proportions, safe daycare atmosphere, coral-town ocean motif. Backgrounds should stay simple and secondary to characters. Preserve each character's official body shape, color, outfit, accessories, and sea-creature motif. Avoid shiny plastic 3D toy texture, intense glow effects, dark deep-sea backgrounds, scary expressions, repeated identical front-facing poses, and overfilled compositions. Leave clean blank space for later Korean story text.

## 2026-05-28 Correction

For this series, generate the illustration and page text together in the image unless the user explicitly asks for illustration-only drafts. Page text must be rendered inside the image in a soft Korean picture-book text area.

Page format:

- Use A5 portrait proportion for all new pages: approximately 1:1.414 width-to-height.
- Prompt wording: "A5 portrait page proportion, about 1:1.414, not square and not extra-tall poster."
- Keep a print-safe margin around all text and important faces.
- The approved cover candidate `00_candidate_text_v2.png` may remain as-is even though it is slightly taller than A5.

Character locks for retries:

- 아루: round baby pufferfish body only, orange-yellow pufferfish body, tiny fins and tiny spikes, sailor scarf and yellow bag. No human arms, no human legs, no shoes, no hands.
- 포포: moon jellyfish child, pale sky-blue translucent rounded bell, soft tentacles under the bell, sailor collar and beige bag. Eyes are hidden or barely visible; express mostly with a small mouth. No droplet body, no hard glass look.
- 방울이: tiny water droplet mascot, separate from 포포. Simple pale sky-blue droplet with a tiny face and two or three small droplets nearby.

Safety and scene locks for slide pages:

- Children must never wait in the slide chute, at the slide exit, or in the landing path.
- Waiting children stand in a safe line beside the ladder/stairs or at a marked waiting spot away from the slide path.
- Only the sliding child is on the slide surface; others are clearly off to the side or on the stairs platform.
- For pages 2-3, it is outdoor free-play time: no backpacks, no school bags, and 몽글이 does not hold brush/crayon unless the script explicitly asks for art tools.

## 00 Cover Prompt

Use case: illustration-story
Asset type: picture-book cover candidate
Primary request: Create the cover illustration for "산호마을 어린이집의 기다림 이야기".
Input images: Official character references for 준이, 아루, 루루, 몽글이, 방울이; official background reference `배경_전경과_놀이터.png`.
Scene/backdrop: A bright, gentle outdoor playground in front of Coral Town Daycare, with the coral-roof daycare building softly visible in the background.
Subject: 준이, 아루, 루루, and 몽글이 gathered naturally near the playground, with 방울이 subtly floating between them like a tiny supportive mascot.
Style/medium: warm children's picture-book illustration, soft watercolor and colored pencil feel, gentle paper texture.
Composition/framing: centered cover composition, slightly wide view, children arranged in a loose friendly arc rather than a straight line. Leave clean open space at the top for the book title and a small open area near the bottom for subtitle text.
Lighting/mood: soft morning light, warm, calm, expectant, friendly.
Text: no rendered text in this candidate; reserve blank areas only.
Constraints: Keep character identities faithful to official references. Use different poses and expressions for each child. 방울이 should be small, simple, pale sky-blue translucent, and not over-detailed.
Avoid: no prior episode contamination, no scary faces, no aggressive conflict, no deep ocean darkness, no shiny 3D toy look, no overpacked background, no illegible or invented text.

## 01 Page Prompt

Use case: illustration-story
Asset type: picture-book interior page candidate
Primary request: Morning arrival at Coral Town Daycare.
Input images: Official references for 마리_선생님, 준이, 아루, 루루, 몽글이, 수아, 토리, 포포, 방울이; official background reference `배경_전경과_놀이터.png`.
Scene/backdrop: The entrance and playground of Coral Town Daycare on a bright morning.
Subject: 마리 선생님 welcomes the children near the entrance. 준이 walks in with his bag, 아루 wiggles forward eagerly, 루루 quietly waves, 몽글이 carries art supplies, while 수아, 토리, and 포포 move gently toward their places. 방울이 peeks subtly near the entrance.
Style/medium: warm children's picture-book illustration, soft pastel paper texture.
Composition/framing: wide establishing view with the daycare building and entrance visible. Natural staggered arrival positions, not a lineup. Leave clean blank space at the top or upper-left for later story text.
Lighting/mood: fresh morning, peaceful, curious, lightly excited.
Text: no rendered text in this candidate; reserve blank area only.
Constraints: Preserve all official character designs, outfits, bags, hats, and sea-creature motifs. Keep the scene calm and readable despite many characters.
Avoid: no crowded wall of characters, no identical smiles or poses, no invented signage text, no prior episode details.

## 02 Page Prompt

Use case: illustration-story
Asset type: picture-book interior page candidate
Primary request: 준이 waits for the coral slide and feels impatient but safe.
Input images: Official references for 준이, 포포, 몽글이, 방울이; official background reference `배경_전경과_놀이터.png`.
Scene/backdrop: The Coral Town Daycare playground, focused on the coral slide.
Subject: 포포 is gently sliding first, 몽글이 waits next, and 준이 waits behind them. 준이 is a small blue shark child with his official bag and features, softly stomping the sand and wiggling with impatience, but not looking scary. 방울이 watches from near the coral slide with a tiny supportive expression.
Style/medium: warm children's picture-book illustration, soft watercolor and pencil texture.
Composition/framing: side view or three-quarter side view showing the waiting order clearly: 포포 on/near the slide, 몽글이 next, 준이 behind. Leave blank space on the upper-right for text.
Lighting/mood: playground energy with a gentle emotional focus on waiting.
Text: no rendered text in this candidate; reserve blank area only.
Constraints: Show 준이's impatient body language through tiny feet, tail, and eyebrows, while keeping the tone kind and non-threatening. Keep slide and background simple.
Avoid: no angry yelling, no unsafe slide use, no exaggerated motion blur, no over-detailed background, no invented text.

## 03 Page Prompt

Use case: illustration-story
Asset type: picture-book interior page candidate
Primary request: 준이 calms himself by counting turns before using the coral slide.
Input images: Official references for 준이, 포포, 몽글이, 방울이; official background reference `배경_전경과_놀이터.png`.
Scene/backdrop: Near the bottom or steps of the coral slide in the playground.
Subject: It is almost 준이's turn. 준이 stands calmly near the slide steps, holding up small fingers or quietly counting "one, two, three" with a softened expression. 포포 has finished sliding in the background and 몽글이 is moving away after their turn. 방울이 glows very subtly near a coral decoration, smiling supportively.
Style/medium: warm children's picture-book illustration, soft pastel, paper texture.
Composition/framing: medium shot or gentle close medium shot focused on 준이's calmer face and counting gesture, with enough background context to show the slide and the previous children. Leave blank space on the upper-left for text.
Lighting/mood: warm, patient, quietly proud.
Text: no rendered text in this candidate; reserve blank area only.
Constraints: 준이 should still look like the official blue shark child, not a generic shark. 방울이 remains small and simple, with only a soft glow, not a dramatic light effect.
Avoid: no big typography inside the image, no neon glow, no crowded cast, no repeated pose from page 2, no prior episode contamination.

## QA Criteria For Batch 1

- Character identity matches official individual references.
- Background matches the official daycare exterior/playground reference.
- Page proportions match A5 portrait for new retries and interiors.
- Text-safe blank space is visible and not blocked by faces or key props.
- Cover and pages 1-3 have varied compositions.
- 방울이 appears subtly and does not become a complex main character.
- No generated image from another episode is used as a visual reference.
