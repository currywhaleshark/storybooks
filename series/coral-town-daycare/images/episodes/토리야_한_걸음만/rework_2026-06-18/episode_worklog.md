# Episode Worklog - 토리야, 한 걸음만 - Rework 2026-06-18

## Source

- Script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Design spec: `docs/superpowers/specs/2026-06-18-tori-tunnel-restart-design.md`

## Rework Rule

Existing `final`, `work_2026-06-03`, and `work_2026-06-06` files are process history only. Do not use them as visual truth for generation.

## Current Status

- Status: `setup`
- Current batch: `tunnel_lock`
- Next action: create and QA a straight single-axis toddler crawl-through coral tunnel lock before generating any page.

## Locked Official References

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Existing coral tunnel location reference: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Coral tunnel scale reference: `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`

## Tunnel Lock QA

- Required: straight single-axis pass-through tube.
- Required: low toddler crawl-through scale; Tori must lower body/head to pass.
- Required: warm, safe, pastel coral playground prop.
- Forbidden: L shape, corner bend, side branch, second tunnel, same-facing double openings, cave mound, broad interior corridor.

## Candidate Status Log

No candidates generated yet.

## Tunnel Lock Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md`
- Next action: generate `coral_tunnel_straight_tube_lock_candidate_v1.png` using the listed reference images.

## Tunnel Lock Reference Board - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_reference_board.png`
- Status: `candidate pass`
- Source references:
  - `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- QA:
  - Official references are visible on one board: pass
  - Geometry locks are written directly on the board: pass
  - Board is suitable as prompt support for tunnel candidate generation: pass

## Tunnel Lock Candidate Generation Attempt - 2026-06-18

- Status: `resolved`
- The generated preview was found in the user's Downloads folder and copied into the rework folder.

## Tunnel Lock Candidate v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Source from user: `C:/Users/USER/Downloads/생성된 이미지 1 (3).png`
- Status: `candidate pass`
- QA:
  - Straight single-axis tube: pass
  - Same-facing double opening: pass
  - L shape / corner / branch: pass
  - Toddler scale with Tori: pass
  - Warm safe style: pass
  - Tori identity for scale marker: pass
- Caveat:
  - The top main view has a large dark near opening. For story pages, prioritize the lower side-view and crawling-view scale so the tunnel stays low and toddler-sized, not cave-like.
- Next action: ask user to approve this tunnel lock before Batch 1 page generation.

## Batch 1 Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/batch_1_prompt_plan.md`
- Scope:
  - `00_cover_candidate_2026-06-18_v1.png`
  - `01_candidate_2026-06-18_v1.png`
  - `02_candidate_2026-06-18_v1.png`
  - `03_candidate_2026-06-18_v1.png`
- Required gate: generate only after user confirms this prompt plan.

## Batch 1 Cover Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/00_cover_candidate_2026-06-18_v2.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 2 (1).png`
- Status: `user approved`
- QA:
  - Tori identity and hesitant emotion: pass
  - Banguli identity and reassuring role: pass
  - Approved low side-view tunnel direction: pass
  - Warm Coral Town Daycare style: pass
  - User confirmed cover text is acceptable: pass
- Next action: generate page 1 only.

## Batch 1 Page 1 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/01_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (4).png`
- Status: `user approved`
- QA:
  - Page text: pass, user confirmed it is not misspelled.
  - Coral tunnel: pass, readable as the new tunnel prop for this page.
  - Tori emotion and position: pass, Tori is hesitant and slightly apart.
  - Story setting: pass, daycare playground is visible.
  - Continuity caveat: classmates and Mari teacher are acceptable for this page, but next pages must lock official character references more strongly to avoid unrelated rabbit/dolphin/clownfish substitutions.
- Rejected/superseded:
  - The second page-1 generation was rejected by the user because non-Tori characters changed into unrelated rabbit/dolphin/clownfish designs.
- Next action: commit approved page 1, then generate page 2 with stricter official-character constraints.
