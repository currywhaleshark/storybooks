# Episode Worklog - 준이의 싫어싫어파도 - 2026-06-12 Restart

## Source

- Script: `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Restart design: `docs/superpowers/specs/2026-06-12-juni-no-no-wave-restart-design.md`
- Implementation plan: `docs/superpowers/plans/2026-06-12-juni-no-no-wave-restart.md`
- Work root: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12`
- Final folder: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/final`

## Restart Decision

- Approved approach: A, complete new batch start.
- `work_2026-06-11/batch_1/*.png` candidates are `superseded` process history only.
- Do not use any 2026-06-11 page candidate as visual truth.
- Keep only the independent shell hourglass prop reference:
  - `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

## Superseded 2026-06-11 Candidates

- `00_cover_candidate_restart_v3.png`: superseded; not visual truth.
- `01_candidate_text_restart_v1.png`: superseded; not visual truth.
- `02_candidate_text_restart_v2.png`: superseded; not visual truth.
- `03_candidate_text_restart_v2.png`: superseded; not visual truth.

## Hard QA Locks

- Jun-i must match `references/characters/준이.png`: projecting shark snout, small black oval button eyes, white lower face and belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
- Pages 01-08 are arrival-time exterior continuity, so Jun-i keeps the blue bag on.
- Page 03 must not reveal or imply `밖에 더 있고 싶어`.
- Generate and QA one page at a time.
- A page candidate with wrong or garbled required text cannot be final promoted.
- If the generation workflow cannot use loaded image references as visual grounding, stop instead of generating from prose only.

## Batch 1 Status

- Scope: cover through page 03.
- Current page: cover.
- Next action: verify references, then generate cover candidate v1 using official references only.

## Batch 1 Cover - 2026-06-12

- Generated: `batch_1/00_cover_candidate_2026-06-12_v1.png`
- Status: `fail`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli loaded before generation.
- QA:
  - Background follows official daycare exterior and includes playground/tunnel cues.
  - Mari teacher keeps yellow apron, star hairpin, purple notebook, and purple mermaid tail.
  - Banguli remains a droplet.
  - Fail: Jun-i's eye changed into a droopy expressive eye with eyebrow-like styling instead of the official small black oval button eye.
  - Fail: cover title was split into oversized separate title blocks instead of the exact title line `준이의 싫어싫어파도`.
- Next action: regenerate cover only as v2 with stricter Jun-i eye and title locks. Do not continue to page 01 yet.

## Batch 1 Cover v2 - 2026-06-12

- Generated: `batch_1/00_cover_candidate_2026-06-12_v2.png`
- Status: `reject`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli loaded before generation.
- QA:
  - Improved: title reads as one clean title line, and Jun-i's eye is closer to the official small black oval button eye.
  - Fail: art style drifted too far from the Sanho Village Daycare watercolor/colored-pencil paper texture and became smoother, cleaner, and more 3D/plastic-like.
  - User feedback: v1 is preferable for overall art style; v2 should not guide the next attempt.
- Next action: regenerate cover v3 by restoring the official watercolor/colored-pencil paper texture and v1-like warmth, while fixing v1's Jun-i eye and title issues. Do not use v1 or v2 as character visual truth; official references remain the visual truth.

## Batch 1 Cover v3 - 2026-06-12

- Generated: `batch_1/00_cover_candidate_2026-06-12_v3.png`
- Status: `candidate pass` for illustration, `hold` for text repair before final promotion
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli loaded before generation.
- QA:
  - Pass: watercolor/colored-pencil paper texture and warm Sanho Village Daycare style returned; v2's smooth 3D/plastic drift is gone.
  - Pass: Jun-i keeps a clear side-view shark silhouette, small black oval button eye, projecting snout, white lower face/belly, gill marks, dorsal fin, long tail, sailor outfit, and blue arrival bag.
  - Pass: Mari teacher keeps yellow apron, star hairpin, purple notebook, and purple mermaid tail.
  - Pass: Banguli remains a droplet.
  - Hold: title appears as `준이의 싫어 싫어파도` with an unwanted space; required title is `준이의 싫어싫어파도`.
- Next action: continue to page 01 because the cover illustration passes character/style QA. Keep cover v3 separate for later text repair; do not promote to `final`.

## Batch 1 Page 01 - 2026-06-12

- Generated: `batch_1/01_candidate_2026-06-12_v1.png`
- Status: `candidate pass`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, and Popo loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `아침이 되었어요.`
    - `산호마을 어린이집 문이 열렸어요.`
    - `딩동댕동!`
    - `그런데 오늘 준이는`
    - `조금 삐친 얼굴이었어요.`
  - Pass: watercolor/colored-pencil paper texture follows the v1/v3 Sanho Village Daycare direction; no v2 smooth 3D/plastic drift.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass: Mari teacher keeps yellow apron, star hairpin, purple notebook, and purple mermaid tail.
  - Pass: Banguli remains a transparent droplet.
  - Pass: Tori, Mongle, Lulu, Popo, and Aru are readable as their official species silhouettes with arrival bags/details; Aru does not gain human hands or feet.
  - Pass: scene logic shows friends entering while Jun-i stays separate and pouty outside.
- Next action: continue to page 02 with the same watercolor/colored-pencil style lock and no v2-style smoothing.

## Batch 1 Page 02 - 2026-06-12

- Generated: `batch_1/02_candidate_2026-06-12_v1.png`
- Status: `candidate pass`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, and Banguli loaded before generation.
- QA:
  - Pass: Korean page text is readable and matches the required story content:
    - `"준아, 어서 오렴."`
    - `마리 선생님이 말했어요.`
    - `하지만 준이는`
    - `입을 쭉 내밀고 말했어요.`
    - `"아직 안 들어갈래!"`
  - Pass: watercolor/colored-pencil paper texture stays aligned with page 01 and cover v3; no rejected v2 smooth 3D/plastic drift.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass: Mari teacher keeps yellow apron, star hairpin, purple attendance notebook, purple mermaid tail, and a patient open-hand posture.
  - Pass: Banguli remains a transparent droplet and reads as concerned/curious.
  - Pass: doorway/playground conflict is clear, with no unreferenced supporting friends invented.
- Next action: continue to page 03 with the same style lock. Keep page 03 story lock: do not reveal or imply `밖에 더 놀고 싶어`.

## Batch 1 Page 03 - 2026-06-12

- Generated: `batch_1/03_candidate_2026-06-12_v1.png`
- Status: `candidate pass`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Banguli, Tori, Mongle, and Lulu loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `준이는 발을 쿵쿵 굴렀어요.`
    - `"싫어! 싫어!`
    - `안 들어갈래!"`
    - `준이 마음속에는`
    - `커다란 싫어싫어 파도가`
    - `출렁거렸어요.`
  - Pass: page does not write, show, or imply `밖에 더 놀고 싶어`; it only shows Jun-i's outward protest and symbolic emotion wave.
  - Pass: watercolor/colored-pencil paper texture remains aligned with pages 01-02 and cover v3; no rejected v2 smooth 3D/plastic drift.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass: Jun-i's open mouth reads as toddler protest, not scary or predatory.
  - Pass: Banguli remains a transparent droplet and reacts with surprise.
  - Pass: Tori, Mongle, and Lulu are set back as concerned observers, not a shaming crowd, and their species silhouettes/details remain readable.
  - Pass: the `싫어싫어 파도` reads as a soft symbolic feeling wave, not a dangerous real wave.
- Next action: write batch 1 handoff. Do not promote any candidate to `final` until user approval; cover v3 still needs title text repair before final promotion.

## Batch 2 Prep - 2026-06-12

- Prepared: `HANDOFF_batch_2_prep.md`
- Prepared: `batch_2/batch_2_prompt_plan.md`
- Scope: pages 04-06.
- Reference verification: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, and shell hourglass paths were checked and exist.
- Style lock: continue page 01-03 / cover v3 watercolor and colored-pencil paper texture; do not use cover v2's smooth 3D/plastic style.
- Story locks:
  - Page 04: Mari waits, validates, and does not scold or pull.
  - Page 05: `밖에 더 있고 싶어` is first clearly revealed, and Jun-i directly says `"밖에... 더 있고 싶어."`
  - Page 06: shell hourglass appears as a small time-bound alternative after Jun-i says what he wants.
- Next action: if user approves continuing, load page 04 references with `view_image` and generate only page 04.

## Batch 2 Page 04 - 2026-06-12

- Generated: `batch_2/04_candidate_2026-06-12_v1.png`
- Status: `hold - rework required for supporting-character reference fidelity`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, and Lulu loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `마리 선생님은`
    - `준이 옆에 조용히 앉았어요.`
    - `"준아, 많이 속상했구나."`
    - `선생님은 혼내지 않았어요.`
    - `그냥 다정하게 기다렸어요.`
  - Pass: watercolor/colored-pencil paper texture stays aligned with the accepted batch 1 direction; no rejected v2 smooth 3D/plastic drift.
  - Pass: Mari teacher is lowered beside Jun-i and waits warmly without scolding, grabbing, pulling, pushing, or sharp pointing.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass with note: Jun-i has a small pout/frown crease, but the eye itself remains the required small black oval button eye.
  - Pass: Banguli remains a transparent droplet and reads as worried/gentle.
  - Fail: the back-row friends drift too far from the official references. Tori is simplified, Mongle reads as a generic purple sea animal instead of the official octopus child with yellow beret, sailor collar, and visible tentacles, and Lulu loses the official seahorse structure such as long snout, head ridge, fin, and curled tail.
  - User QA: page 04 needs rework specifically for the background friends. Do not promote v1 to `final`.
  - Pass: no scary emotion wave appears; the scene reads as calming down after page 03.
- Next action: prepare/regenerate `batch_2/04_candidate_2026-06-12_v2.png` before final promotion. Keep the main page 04 text, Mari-Jun-i waiting emotion, Jun-i bag, and watercolor style, but rebuild or omit background friends unless Tori, Mongle, Lulu, and Banguli match their official reference PNGs.

## Batch 2 Page 04 Retry - 2026-06-12

- Generated: `batch_2/04_candidate_2026-06-12_v2.png`
- Status: `candidate pass`
- Reference grounding: official exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, and Lulu were loaded before generation.
- QA:
  - Pass: requested supporting-character rework improved. Tori reads as the official green turtle child with yellow hat, visible shell, sailor clothes, and yellow bag.
  - Pass: Mongle reads as the official purple octopus child with yellow beret, sailor collar, yellow bag, and multiple visible tentacles.
  - Pass: Lulu reads as the official pink seahorse child with long snout, head ridge/spiky silhouette, small fin, curled tail, sailor outfit, and yellow bag.
  - Pass: Banguli remains a translucent blue droplet with worried face.
  - Pass: Mari and Jun-i keep the intended waiting/validation posture; Jun-i keeps his blue arrival bag and official shark details.
  - Pass: Korean story text is readable and accepted by user review; earlier dot/separator concern was an overcall caused by paper texture/antialiasing.
- Generated text-edit attempts: `batch_2/04_candidate_2026-06-12_v3.png`
  - Status: `candidate pass`
  - Note: v3 kept the improved friends and readable generated text. User review clarified that the suspected dot/separator was not an actual text error.
- Created local text repair: `batch_2/04_candidate_2026-06-12_v4_textfix.png`
  - Status: `superseded optional textfix`
  - Note: v4_textfix was created from an over-conservative text concern and should not replace the natural generated candidate unless the user later wants a cleaner text-panel style.
- User clarification: suspected dot in `준이` did not actually appear as a text error. Continue to batch 3.
- Next action: proceed to batch 3 pages 07-09. Use page 04 retry v2/v3 only as review context; official references remain visual truth.

## Batch 2 Page 05 - 2026-06-12

- Generated: `batch_2/05_candidate_2026-06-12_v1.png`
- Status: `candidate pass`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, and Tori loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `준이는 작은 목소리로 말했어요.`
    - `"나... 그냥 싫어."`
    - `마리 선생님은`
    - `준이 눈길을 따라 보았어요.`
    - `"준이 마음속 말이`
    - `혹시 이 말일까?`
    - `'밖에 더 있고 싶어.'"`
    - `준이는 아주 작게 말했어요.`
    - `"밖에... 더 있고 싶어."`
  - Pass: `밖에 더 있고 싶어` is first clearly revealed on this page.
  - Pass: Jun-i directly says the final line `"밖에... 더 있고 싶어."`; it is not replaced by a thought bubble.
  - Pass: watercolor/colored-pencil paper texture remains aligned with pages 01-04; no rejected v2 smooth 3D/plastic drift.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass: Mari teacher keeps yellow apron, star hairpin, purple attendance notebook, and purple mermaid tail.
  - Pass with note: Mari gestures gently toward the playground direction, but the pose reads as helping Jun-i find words rather than scolding or forcing an answer.
  - Pass: Banguli remains a transparent droplet; Tori stays behind them with concern rather than pressure.
- Next action: continue to page 06. Keep the shell hourglass first appearance locked to page 06 and use the official prop reference.

## Batch 2 Page 06 - 2026-06-12

- Generated: `batch_2/06_candidate_2026-06-12_v1.png`
- Status: `candidate pass`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, and shell hourglass loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `마리 선생님이`
    - `조개 모래시계를 꺼냈어요.`
    - `"말해 줘서 고마워.`
    - `그럼 모래가 다 내려갈 때까지만`
    - `밖에 조금 더 있다가`
    - `들어가 볼까?"`
    - `준이는 가만히 모래시계를 보았어요.`
  - Pass: watercolor/colored-pencil paper texture remains aligned with pages 01-05; no rejected v2 smooth 3D/plastic drift.
  - Pass: the shell hourglass appears for the first time on this page and follows `shell_hourglass_ref.png`: scallop shell top and bottom, transparent rounded glass, warm sand grains, and center falling sand.
  - Pass: no jewels, magic glow, numbers, clock face, metal frame, wings, or handles were added.
  - Pass: Jun-i keeps the official shark identity: projecting snout, small black oval button eye, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Pass: Mari teacher keeps yellow apron, star hairpin, purple attendance notebook, and purple mermaid tail.
  - Pass: Mari's posture reads as offering a small time-bound option rather than bargaining, scolding, or forcing Jun-i inside.
  - Pass: Banguli remains a transparent droplet and looks curious/calm.
- Next action: stop batch 2 here and write a handoff before any next batch. Do not promote candidates to `final` without explicit user approval.

## Batch 2 Summary - 2026-06-12

- Scope completed: pages 04-06.
- Generated candidates:
  - `batch_2/04_candidate_2026-06-12_v1.png` - `hold - rework required for supporting-character reference fidelity`
  - `batch_2/04_candidate_2026-06-12_v2.png` - `candidate pass`
  - `batch_2/04_candidate_2026-06-12_v3.png` - `candidate pass`
  - `batch_2/04_candidate_2026-06-12_v4_textfix.png` - `superseded optional textfix`
  - `batch_2/05_candidate_2026-06-12_v1.png` - `candidate pass`
  - `batch_2/06_candidate_2026-06-12_v1.png` - `candidate pass`
- Final promotion: none. No files were copied to `final`.
- Carry forward:
  - Page 04 background-friend rework is accepted enough to continue; do not let the old v1 background-friend drift guide later pages.
  - Keep Jun-i's blue arrival bag through pages 07-08.
  - Use `batch_2/06_candidate_2026-06-12_v1.png` only as continuity discussion/candidate context, not as official prop truth; official shell hourglass truth remains `work_2026-06-11/reference_assets/shell_hourglass_ref.png`.
  - Continue watercolor/colored-pencil paper texture; avoid cover v2 smooth 3D/plastic drift.
  - Page 07 should show the `싫어싫어 파도` getting smaller while Jun-i waits outside with the same shell hourglass logic.
- Next action: prepare and generate batch 3 pages 07-09.

## Batch 3 Page 09 - 2026-06-12

- Generated: `batch_3/09_candidate_2026-06-12_v1.png`
- Status: `fail - regenerate`
- Reference grounding: official classroom, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua were loaded before generation.
- QA:
  - Pass: overall classroom warmth and watercolor/colored-pencil texture followed the accepted Sanho Village Daycare direction.
  - Fail: Korean text misspelled `앉았어요` as `앉었어요`.
  - Fail: some indoor friend details drifted toward worn bags/straps and off-reference body shapes.
- Next action: regenerate a simpler page 09 with fewer visible friends, no Aru/Popo/Sua, and a hard no-bags-worn-indoors lock.

## Batch 3 Page 09 Retry - 2026-06-12

- Generated: `batch_3/09_candidate_2026-06-12_v2.png`
- Status: `superseded - omitted Sua and Popo`
- Reference grounding: official classroom, Jun-i, Mari teacher, Banguli, Tori, Mongle, and Lulu were loaded before generation. Aru, Popo, and Sua were intentionally omitted in this retry to protect reference fidelity and reduce crowding.
- QA:
  - Pass: Korean page text is exact and readable:
    - `어린이집 안으로 들어온 준이는`
    - `친구들과 함께 앉았어요.`
    - `이제 준이는 알았어요.`
    - `싫은 마음은 말해도 돼요.`
    - `쿵쿵하기보다`
    - `말로 말하면 돼요.`
  - Pass: Jun-i keeps the official shark identity, small black oval button eye, white lower face/belly, gill marks, side fins, sailor shirt, and blue shorts.
  - Pass: Jun-i is not wearing his blue arrival bag indoors; the blue bag is stored in the classroom cubby area.
  - Pass: Mari teacher keeps her yellow apron, star hairpin, attendance notebook, and purple mermaid tail, and reads as warmly supportive.
  - Pass: Banguli, Tori, Mongle, and Lulu form a calm supportive group and do not wear bags indoors.
  - Pass: classroom setting is readable with rounded windows, cubbies, coral details, and warm underwater light.
  - User QA: v2 omitted Sua and Popo, so it should not be the preferred page 09 candidate.
- Next action: retry with Sua and Popo as required visible classmates.

## Batch 3 Page 09 Sua/Popo Retry - 2026-06-12

- Generated: `batch_3/09_candidate_2026-06-12_v3.png`
- Status: `hold - indoor bag/strap drift`
- Reference grounding: official classroom, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Popo, and Sua were loaded before generation.
- QA:
  - Pass: Sua and Popo are restored as visible classmates.
  - Pass: Korean page text is exact and readable.
  - Hold: a bag/strap-like detail appears on Popo and some classmates, conflicting with the page 09 indoor no-bags lock.
- Next action: retry once more with the same Sua/Popo inclusion lock and stricter no-bags-on-children lock.

## Batch 3 Page 09 Sua/Popo No-Bag Retry - 2026-06-12

- Generated: `batch_3/09_candidate_2026-06-12_v4.png`
- Status: `candidate pass`
- Reference grounding: official classroom, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Popo, and Sua were loaded before generation.
- QA:
  - Pass: Korean page text is exact and readable:
    - `어린이집 안으로 들어온 준이는`
    - `친구들과 함께 앉았어요.`
    - `이제 준이는 알았어요.`
    - `싫은 마음은 말해도 돼요.`
    - `쿵쿵하기보다`
    - `말로 말하면 돼요.`
  - Pass: Sua is visible as a purple seahorse child with long snout, ridged head, small fin, curled tail, and blue sailor outfit.
  - Pass: Popo is visible as a translucent moon jellyfish child with internal flower-like pattern and trailing tentacles.
  - Pass: Jun-i is calm, speaks with a raised hand, and is not wearing his blue arrival bag.
  - Pass: bags are stored on hooks/cubbies in the classroom, not worn by children.
  - Pass: Mari teacher reads as warm and supportive; Banguli, Tori, Mongle, Lulu, Sua, and Popo are supportive classmates.
- Next action: hold `v4` as the preferred page 09 candidate for user review. Do not promote to `final` without approval.

## Batch 4 Prep - 2026-06-13

- Prepared: `batch_4/batch_4_prompt_plan.md`
- Scope: page 10.
- Reference verification: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua paths were checked/loaded before generation attempts.
- Story locks:
  - Page 10 is dismissal time outside the daycare.
  - Jun-i and friends may wear official bags again.
  - Jun-i should feel emotionally settled, bright, and confident.
  - Ending text must be exact:
    - `하원 시간이 되었어요.`
    - `준이는 활짝 웃으며 말했어요.`
    - `"내일도 올래!"`
    - `산호마을 어린이집은`
    - `오늘도 맑음.`
    - `준이 마음도`
    - `조금씩 맑음.`

## Batch 4 Page 10 Built-in Generation Attempts - 2026-06-13

- Intended output: `batch_4/10_candidate_2026-06-13_v1.png`
- Status: `blocked - built-in image generator ignored prompt`
- Reference grounding: official exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua were loaded before attempts.
- QA:
  - Fail: first built-in `image_gen` output was an unrelated English `VITAMINS AND THEIR BENEFITS` infographic.
  - Fail: second built-in `image_gen` output was an unrelated English `TYPES OF POLLUTION` infographic.
  - Fail: third built-in `image_gen` output was an unrelated English `TYPES OF ROCKS` infographic.
  - No page 10 candidates were copied into `batch_4` because all outputs were unrelated to the episode.
- Next action: do not keep retrying the same built-in path until the generator state is healthy. Use a fresh generation route/session or user-approved CLI fallback if needed.

## Batch 4 Page 10 Fresh Session Retry - 2026-06-13

- Generated: `batch_4/10_candidate_2026-06-13_v1.png`
- Source generated image preserved at: `C:\Users\yurib\.codex\generated_images\019ebc75-1c90-74a3-88aa-9e04ee5e7828\ig_0d10b51dffc569a8016a2c272ceab8819180ba43d9ad66213f.png`
- Status: `hold - review/regenerate likely`
- Reference grounding: official exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua were loaded before generation.
- QA:
  - Pass: output is a proper Korean toddler picture-book page, not an unrelated infographic.
  - Pass: Korean ending text is exact and readable:
    - `하원 시간이 되었어요.`
    - `준이는 활짝 웃으며 말했어요.`
    - `"내일도 올래!"`
    - `산호마을 어린이집은`
    - `오늘도 맑음.`
    - `준이 마음도`
    - `조금씩 맑음.`
  - Pass: daycare exterior, blue door, coral playground details, warm underwater light, and closing-page mood are strong.
  - Pass: Jun-i is the clear focus, smiling/waving, wearing the official-style blue dismissal bag, and reads emotionally settled.
  - Pass: Mari teacher is near the doorway, warm, waving, and not controlling Jun-i.
  - Hold: a non-reference dog-like character appears in the foreground, replacing or distracting from official friend coverage.
  - Hold: Banguli is not clearly visible as the official blue droplet friend.
  - Hold: Popo is missing or unclear, and several background friends drift from exact official shapes.
- Next action: keep v1 as a useful visual/text candidate, but regenerate page 10 if official-friend fidelity is required. Next prompt should explicitly forbid any pet/dog/new character and either reduce the friend group or make Banguli/Popo placement unambiguous.

## Batch 4 Page 10 Focused Friend Retry - 2026-06-13

- Generated: `batch_4/10_candidate_2026-06-13_v2.png`
- Source generated image preserved at: `C:\Users\yurib\.codex\generated_images\019ebc75-1c90-74a3-88aa-9e04ee5e7828\ig_0d10b51dffc569a8016a2c28a4723c8191962d91cbbb4630e9.png`
- Status: `candidate pass - preferred over v1`
- Reference grounding: official exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo, and Sua were loaded before generation. The prompt reduced the visible friend group to protect official-friend fidelity.
- QA:
  - Pass: output is a proper Korean toddler picture-book page and no unrelated infographic content appears.
  - Pass: Korean ending text is exact and readable:
    - `하원 시간이 되었어요.`
    - `준이는 활짝 웃으며 말했어요.`
    - `"내일도 올래!"`
    - `산호마을 어린이집은`
    - `오늘도 맑음.`
    - `준이 마음도`
    - `조금씩 맑음.`
  - Pass: daycare exterior, blue door, coral playground, and warm closing mood match the series direction.
  - Pass: Jun-i is the clear emotional focus, smiling/waving, wearing the official-style blue dismissal bag, and reads calm/resolved.
  - Pass: Mari teacher is near the doorway, waving warmly, with star hairpin, yellow apron, purple notebook, and purple mermaid tail.
  - Pass: Banguli is clearly visible as the official light-blue droplet friend.
  - Pass: Popo is clearly visible as a moon jellyfish child with translucent bell, internal flower-like pattern, sailor collar, tentacles, and shell bag; no big human eyes.
  - Pass: no dog/pet/new character appears in this retry.
  - Note: friend group is intentionally simplified compared with the full class roster; this is preferable to v1's off-reference extra character.
- Next action: hold v2 as the preferred page 10 candidate for user review. Do not promote to `final` without approval.

## Friend Door Continuity Revisions - 2026-06-15

- Source plan: `work_2026-06-14_revisions/friend_door_continuity_prompt_plan.md`
- Scope: pages 03, 04, 05, 06, and 07.
- User QA lock applied:
  - Friends must not reappear outside around Jun-i after entering daycare on earlier pages.
  - Visible classmates on these pages are placed inside the open daycare doorway or just behind the interior threshold.
  - Jun-i, Mari teacher, and Banguli remain outside near the entrance/playground.
- Generated revision candidates:
  - `work_2026-06-14_revisions/03_candidate_2026-06-14_v2_door_friends.png`
  - `work_2026-06-14_revisions/04_candidate_2026-06-14_v5_door_friends.png`
  - `work_2026-06-14_revisions/05_candidate_2026-06-14_v2_door_friend.png`
  - `work_2026-06-14_revisions/06_candidate_2026-06-15_v4_door_official_friends_lulu_refined.png`
  - `work_2026-06-14_revisions/07_candidate_2026-06-14_v3_door_friends.png`
- Review copies added:
  - `review_final_candidates_2026-06-14/03_페이지_후보_v2_문안친구.png`
  - `review_final_candidates_2026-06-14/04_페이지_후보_v5_문안친구.png`
  - `review_final_candidates_2026-06-14/05_페이지_후보_v2_문안친구.png`
  - `review_final_candidates_2026-06-14/06_페이지_후보_v4_문안친구_루루수정.png`
  - `review_final_candidates_2026-06-14/07_페이지_후보_v3_문안친구.png`
- QA status: `user approved` for the requested door-continuity fix after mobile review. Page 06 was additionally revised so the door is open and official classmates watch from inside. Korean text, main character placement, and shell hourglass remain usable by visual inspection.
- Next action: use the five approved revised candidates for final packaging after the remaining cover/title decision is resolved.

## Final Approval And Packaging - 2026-06-15

- User confirmed the cover title spacing is acceptable and the whole episode is OK.
- Promoted approved review candidates to `final/`:
  - `final/00_표지.png`
  - `final/01_페이지.png`
  - `final/02_페이지.png`
  - `final/03_페이지.png`
  - `final/04_페이지.png`
  - `final/05_페이지.png`
  - `final/06_페이지.png`
  - `final/07_페이지.png`
  - `final/08_페이지.png`
  - `final/09_페이지.png`
  - `final/10_페이지.png`
- Packaged final approved pages:
  - `준이의_싫어싫어파도_최종승인본_페이지순_2026-06-15.zip`
- Final status: `user approved` and `final promoted` for cover plus 10 story pages.

## Page 06 Door Continuity Patch - 2026-06-15

- User requested page 06 match the open-door continuity: the daycare door should be open and friends should be watching from inside.
- First v2 attempt was rejected by user because the doorway characters were not official classmates.
- Regenerated v3 with official Tori, Mongle, and Lulu in the doorway, then refined Lulu's silhouette and details in v4:
  - `work_2026-06-14_revisions/06_candidate_2026-06-15_v4_door_official_friends_lulu_refined.png`
  - `review_final_candidates_2026-06-14/06_페이지_후보_v4_문안친구_루루수정.png`
  - `final/06_페이지.png`
- Existing `review_final_candidates_2026-06-14/06_페이지_후보_v1.png` remains as comparison history, v2 remains rejected history, and v3 remains official-friends correction history.
- Final zip refreshed with the revised page 06.
