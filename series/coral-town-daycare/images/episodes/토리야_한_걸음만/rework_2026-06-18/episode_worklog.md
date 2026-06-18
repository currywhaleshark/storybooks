# Episode Worklog - 토리야, 한 걸음만 - Rework 2026-06-18

## Source

- Script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Design spec: `docs/superpowers/specs/2026-06-18-tori-tunnel-restart-design.md`

## Rework Rule

Existing `final`, `work_2026-06-03`, and `work_2026-06-06` files are process history only. Do not use them as visual truth for generation.

## Current Status

- Status: `paused_handoff`
- Current batch: `batch_3`
- Next action: resume tomorrow in a fresh session from page 8 v2 using `batch_3/batch_3_prompt_plan.md`; do not continue image generation in the current contaminated session.

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

See dated sections below for tunnel lock and page candidate status.

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

## Batch 1 Page 2 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/02_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (5).png`
- Status: `user approved`
- QA:
  - User confirmed the apparent `준이가` text concern is acceptable and will handle text QA personally.
  - Coral tunnel: pass, low horizontal tunnel form is retained.
  - Character set: pass, official friend set is closer than the rejected page-1 retry.
  - Tori hesitation: pass, Tori stands apart with hands gathered.
- Next action: persist page 3 candidate if a downloadable/generated source file is available.

## Batch 1 Page 3 Generation Attempt - 2026-06-18

- Status: `hold`
- A page 3 candidate was generated in chat and visually reviewed as usable for Tori's worry page, but the built-in image result did not appear in Downloads or `C:/Users/USER/.codex/generated_images`.
- Because the user left before manually downloading the displayed preview, no page 3 source image file was available to copy into the project.
- Next action: download or regenerate page 3 in a session where the output file can be persisted, then save as `batch_1/03_candidate_2026-06-18_v1.png`.

## Batch 1 Page 3 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/03_candidate_2026-06-18_v1.png`
- Preserved source copy: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/03_candidate_2026-06-18_raw.png`
- Status: `user approved`
- QA:
  - User confirmed page 3 is good enough to continue.
  - User confirmed text is not blocking.
  - Use this only as approved current-episode continuity context; official references remain visual truth.
- Next action: prepare Batch 2 for pages 4-6.

## Direct Save Workflow Note - 2026-06-18

- The built-in image generation preview may display in the chat without creating an accessible local file under `C:/Users/USER/.codex/generated_images`.
- Until this is resolved upstream, use manual direct-save/download from the displayed preview, then copy the saved file into the active batch folder with the stable candidate filename.

## Batch 2 Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/batch_2_prompt_plan.md`
- Scope:
  - `04_candidate_2026-06-18_v1.png`
  - `05_candidate_2026-06-18_v1.png`
  - `06_candidate_2026-06-18_v2.png`
- Required gate: generate page 4 first, save it manually, then QA before moving to page 5.

## Batch 2 Page 4 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/04_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (11).png`
- Status: `user approved`
- QA:
  - User confirmed the candidate came out well.
  - Character set and story beat are acceptable for continuing: Tori refuses gently, Lulu and Mongle invite kindly, Mari approaches in the background.
  - User clarified Lulu hand/gesture is acceptable.
  - Text remains user-managed and is not blocking.
  - Direct-save/download workflow was used successfully.
- Next action: generate page 5 only.

## Batch 2 Page 5 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/05_candidate_2026-06-18_v1.png`
- Source from Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (12).png`
- Status: `candidate pass`
- QA:
  - Mari teacher sits at Tori's eye level and validates his fear: pass.
  - Tori's relieved/cautious emotion reads clearly: pass.
  - Banguli appears as a small supportive presence: pass.
  - Tunnel is low and in the background, not a scary cave: pass.
  - Text remains user-managed and is not blocking.
- Next action: generate page 6 only.

## Batch 2 Page 6 Generation v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v1_reject_l_tunnel_style_drift.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 2 (3).png`
- Status: `rejected`
- Rejection reasons:
  - Art style drifted away from the current approved Batch 1-2 style.
  - The prompt phrase about Banguli peeking from the opposite side caused the model to show both tunnel openings in one page.
  - The tunnel reads as bent/L-shaped or as a two-opening display instead of a clean single side-view tube.
- Corrective lock for v2:
  - Do not show a visible far exit hole.
  - Show only one visible round entrance and a mostly closed side wall of one straight horizontal tube.
  - Banguli should peek from beside or just above the far side/top edge of the tunnel after passing through, not from an exit arch.
- Next action: regenerate page 6 as `06_candidate_2026-06-18_v2.png`.

## Batch 2 Page 6 Generation v2 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`
- Source from user Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (13).png`
- Status: `candidate pass`
- QA:
  - Art style returns to the approved Batch 2 watercolor direction: pass.
  - Tunnel shows one visible entrance and a single straight side-view tube: pass.
  - Banguli peeks from the side/top of the tunnel, not from a second exit arch: pass.
  - Tori remains outside and takes only a small step toward the entrance: pass.
  - Mari stays supportive and does not block the action: pass.
  - Text remains user-managed and is not blocking.
- Next action: review Batch 2 pages 4-6 together, then prepare Batch 3 if accepted.

## Batch 3 Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/batch_3_prompt_plan.md`
- Scope:
  - `07_candidate_2026-06-18_v1.png`
  - `08_candidate_2026-06-18_v1.png`
  - `09_candidate_2026-06-18_v1.png`
- Continuity locks:
  - Use approved page 6 v2 as the tunnel-composition reference.
  - Do not show both exterior tunnel openings in one image.
  - Treat opposite-side light as soft interior glow unless the user explicitly asks for a visible exit.
- Required gate: generate page 7 first, save it manually, then QA before moving to page 8.

## Batch 3 Page 7 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- Source from Downloads: `C:/Users/USER/Downloads/생성된 이미지 1 (14).png`
- Status: `candidate pass`
- QA:
  - Tori puts only his head into the tunnel; body and shell remain outside: pass.
  - Mari teacher stays beside the entrance and supports quietly: pass.
  - Banguli waits just inside the entrance as a soft guide: pass.
  - Tunnel shows one visible entrance only, with no L shape or second exit: pass.
  - Text remains user-managed and is not blocking.
- Next action: generate page 8 only.

## Batch 3 Page 8 Generation v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/08_candidate_2026-06-18_v1_reject_oversized_tunnel.png`
- Source from Downloads: `C:/Users/USER/Downloads/생성된 이미지 2 (4).png`
- Status: `rejected`
- Rejection reasons:
  - Tunnel interior mood was good, but the tunnel scale became about twice too large.
  - The image read as Tori being inside a large cave-like tube instead of peeking into a low toddler crawl-through tunnel.
  - Page 8 should preserve the page 6 v2/page 7 tunnel scale: Tori should still be mostly outside and should need to crouch.
- Corrective lock for v2:
  - Use an outside-the-entrance or shallow entrance view, not a grand interior arch.
  - Keep the entrance only slightly taller than Tori's crouched head and shell.
  - Treat opposite-side light as warm glow deeper in the tube, not as a second exterior exit.
- Next action: regenerate page 8 as `08_candidate_2026-06-18_v2.png`.

## Session Stop Handoff - 2026-06-18

- Reason: user identified session contamination after page 8 v2 regeneration was started.
- Status: stop all further image generation in this session.
- Do not use any unsaved preview or newly generated image after this point unless the user explicitly re-approves it tomorrow.
- Resume point:
  - Start from page 8 v2 in a fresh session.
  - Use `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/batch_3_prompt_plan.md`.
  - Attach official Tori, Banguli, tunnel lock, approved page 6 v2, and page 7 candidate references before generating.
  - Keep tunnel scale low and toddler-sized; page 8 v1 is rejected because the tunnel became too large.
