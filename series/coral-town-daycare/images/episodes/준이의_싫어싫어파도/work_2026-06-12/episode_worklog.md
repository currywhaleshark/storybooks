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
