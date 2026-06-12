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
