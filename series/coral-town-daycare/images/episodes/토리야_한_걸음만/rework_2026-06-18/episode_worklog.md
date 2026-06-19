# Episode Worklog - ?좊━?? ??嫄몄쓬留?- Rework 2026-06-18

## Source

- Script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Rulebook: `series/coral-town-daycare/docs/?고샇留덉쓣_?대┛?댁쭛_?대?吏_洹쒖튃??md`
- Design spec: `docs/superpowers/specs/2026-06-18-tori-tunnel-restart-design.md`

## Rework Rule

Existing `final`, `work_2026-06-03`, and `work_2026-06-06` files are process history only. Do not use them as visual truth for generation.

## Current Status

- Status: `final_promoted_2026-06-19`
- Current batch: `final`
- Next action: final folder contains the full new rework set; use only targeted text-panel correction or export/package follow-up if requested.

## Locked Official References

- Tori: `series/coral-town-daycare/references/characters/?좊━.png`
- Mari teacher: `series/coral-town-daycare/references/characters/留덈━_?좎깮??png`
- Banguli: `series/coral-town-daycare/references/characters/諛⑹슱??png`
- Playground: `series/coral-town-daycare/references/諛곌꼍_?꾧꼍怨???댄꽣.png`
- Existing coral tunnel location reference: `series/coral-town-daycare/references/locations/?고샇_?곕꼸_?덊띁?곗뒪.png`
- Coral tunnel scale reference: `series/coral-town-daycare/references/props/?고샇_?곕꼸_?ш린鍮꾧탳_?덊띁?곗뒪_v2.png`

## Tunnel Lock QA

- Required: straight single-axis pass-through tube.
- Required: low toddler crawl-through scale; Tori must lower body/head to pass.
- Required: warm, safe, pastel coral playground prop.
- Forbidden: L shape, corner bend, side branch, second tunnel, same-facing double openings, cave mound, broad interior corridor.

## Candidate Status Log

See dated sections below for tunnel lock and page candidate status.

## Tunnel Lock Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md`
- Next action: generate `coral_tunnel_straight_tube_lock_candidate_v1.png` using the listed reference images.

## Tunnel Lock Reference Board - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/tunnel_lock_reference_board.png`
- Status: `candidate pass`
- Source references:
  - `series/coral-town-daycare/references/locations/?고샇_?곕꼸_?덊띁?곗뒪.png`
  - `series/coral-town-daycare/references/props/?고샇_?곕꼸_?ш린鍮꾧탳_?덊띁?곗뒪_v2.png`
  - `series/coral-town-daycare/references/characters/?좊━.png`
  - `series/coral-town-daycare/references/諛곌꼍_?꾧꼍怨???댄꽣.png`
- QA:
  - Official references are visible on one board: pass
  - Geometry locks are written directly on the board: pass
  - Board is suitable as prompt support for tunnel candidate generation: pass

## Tunnel Lock Candidate Generation Attempt - 2026-06-18

- Status: `resolved`
- The generated preview was found in the user's Downloads folder and copied into the rework folder.

## Tunnel Lock Candidate v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Source from user: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (3).png`
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
- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/batch_1_prompt_plan.md`
- Scope:
  - `00_cover_candidate_2026-06-18_v1.png`
  - `01_candidate_2026-06-18_v1.png`
  - `02_candidate_2026-06-18_v1.png`
  - `03_candidate_2026-06-18_v1.png`
- Required gate: generate only after user confirms this prompt plan.

## Batch 1 Cover Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/00_cover_candidate_2026-06-18_v2.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 2 (1).png`
- Status: `user approved`
- QA:
  - Tori identity and hesitant emotion: pass
  - Banguli identity and reassuring role: pass
  - Approved low side-view tunnel direction: pass
  - Warm Coral Town Daycare style: pass
  - User confirmed cover text is acceptable: pass
- Next action: generate page 1 only.

## Batch 1 Page 1 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/01_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (4).png`
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

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/02_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (5).png`
- Status: `user approved`
- QA:
  - User confirmed the apparent `以?닿?` text concern is acceptable and will handle text QA personally.
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

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/03_candidate_2026-06-18_v1.png`
- Preserved source copy: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_1/03_candidate_2026-06-18_raw.png`
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
- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/batch_2_prompt_plan.md`
- Scope:
  - `04_candidate_2026-06-18_v1.png`
  - `05_candidate_2026-06-18_v1.png`
  - `06_candidate_2026-06-18_v2.png`
- Required gate: generate page 4 first, save it manually, then QA before moving to page 5.

## Batch 2 Page 4 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/04_candidate_2026-06-18_v1.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (11).png`
- Status: `user approved`
- QA:
  - User confirmed the candidate came out well.
  - Character set and story beat are acceptable for continuing: Tori refuses gently, Lulu and Mongle invite kindly, Mari approaches in the background.
  - User clarified Lulu hand/gesture is acceptable.
  - Text remains user-managed and is not blocking.
  - Direct-save/download workflow was used successfully.
- Next action: generate page 5 only.

## Batch 2 Page 5 Generation - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/05_candidate_2026-06-18_v1.png`
- Source from Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (12).png`
- Status: `candidate pass`
- QA:
  - Mari teacher sits at Tori's eye level and validates his fear: pass.
  - Tori's relieved/cautious emotion reads clearly: pass.
  - Banguli appears as a small supportive presence: pass.
  - Tunnel is low and in the background, not a scary cave: pass.
  - Text remains user-managed and is not blocking.
- Next action: generate page 6 only.

## Batch 2 Page 6 Generation v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/06_candidate_2026-06-18_v1_reject_l_tunnel_style_drift.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 2 (3).png`
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

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`
- Source from user Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (13).png`
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
- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/batch_3_prompt_plan.md`
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

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- Source from Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 1 (14).png`
- Status: `candidate pass`
- QA:
  - Tori puts only his head into the tunnel; body and shell remain outside: pass.
  - Mari teacher stays beside the entrance and supports quietly: pass.
  - Banguli waits just inside the entrance as a soft guide: pass.
  - Tunnel shows one visible entrance only, with no L shape or second exit: pass.
  - Text remains user-managed and is not blocking.
- Next action: generate page 8 only.

## Batch 3 Page 8 Generation v1 - 2026-06-18

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-18_v1_reject_oversized_tunnel.png`
- Source from Downloads: `C:/Users/USER/Downloads/?앹꽦???대?吏 2 (4).png`
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
  - Use `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/batch_3_prompt_plan.md`.
  - Attach official Tori, Banguli, tunnel lock, approved page 6 v2, and page 7 candidate references before generating.
  - Keep tunnel scale low and toddler-sized; page 8 v1 is rejected because the tunnel became too large.

## Batch 3 Page 8 Generation v2 - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-18_v2.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edd23-6cc4-7d71-a6dc-5a006fc4606a/ig_0b4767c4bc4fd413016a34859028608191953ea9bc7fae9860.png`
- Status: `superseded`
- Superseded reason: user noted Tori/Banguli character design drifted from the official originals; regenerate with stronger individual character reference lock.
- Reference grounding:
  - Official Tori: `series/coral-town-daycare/references/characters/?좊━.png`
  - Official Banguli: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Tunnel lock: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Style/scale continuity: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_2/06_candidate_2026-06-18_v2.png`
  - Immediate continuity: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio is retained at `1054x1492`: pass.
  - Prompt corrected the v1 failure by locking a shallow outside-the-entrance view, low toddler-sized tunnel scale, one visible exterior opening, and warm interior glow instead of a second exit: pass.
  - Text remains user-managed and is not blocking, consistent with prior accepted pages.
- Next action: user review page 8 v2 visually; if accepted, generate page 9 only.
## Batch 3 Page 8 Generation v3 Character Reference Lock - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-18_v3_character_ref_lock.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edd23-6cc4-7d71-a6dc-5a006fc4606a/ig_0b4767c4bc4fd413016a3491ba71a08191a46005a210fd0b8e.png`
- Status: `superseded`
- Superseded reason: user noted Tori still differed from the original in eye shape, clothing colors, skin texture, and overall design; regenerate with stricter exact Tori locks.
- Reference grounding:
  - Official Tori individual reference, highest priority: `series/coral-town-daycare/references/characters/?좊━.png`
  - Official Banguli individual reference, highest priority: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Character sheet support only: `series/coral-town-daycare/references/?고샇留덉쓣_?대┛?댁쭛_罹먮┃???쒗듃.png`
  - Tunnel lock: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Immediate continuity: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - Prompt explicitly prioritizes individual character PNGs over style continuity: pass.
  - Tori identity was re-locked around green turtle body, yellow hat, visible shell, and sailor-style clothing: pass.
  - Banguli identity was re-locked around pale-blue transparent water-drop shape and simple face: pass.
  - Tunnel remains constrained to one low toddler-sized entrance and warm interior glow: pass.
  - Text remains user-managed and is not blocking, consistent with prior accepted pages.
- Next action: user review page 8 v3 visually; if accepted, generate page 9 only.
## Batch 3 Page 8 Generation v4 Exact Tori Lock - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-18_v4_exact_tori_lock.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edd23-6cc4-7d71-a6dc-5a006fc4606a/ig_0b4767c4bc4fd413016a34b47010cc8191afa45ef6acf4b953.png`
- Status: `candidate pass`
- User correction applied:
  - Preserve Tori's official eye shape rather than large shiny alternate eyes.
  - Preserve Tori's official clothing color family and sailor-style outfit rather than drifting to a new outfit palette.
  - Preserve Tori's official soft matte green watercolor/colored-pencil skin texture rather than glossy, plastic, scaly, or differently colored skin.
  - Keep yellow hat, visible shell, and toddler turtle proportions readable in a close 3/4 front-side view.
- Reference grounding:
  - Official Tori individual reference, highest priority: `series/coral-town-daycare/references/characters/?좊━.png`
  - Official Banguli individual reference, highest priority: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Tunnel lock only for prop scale/shape: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - Prompt did not use v2 or v3 as visual references: pass.
  - Prompt explicitly prioritizes exact Tori eye shape, outfit colors, skin texture, hat, shell, and toddler proportions over scene drama: pass.
  - Tunnel remains constrained to one low toddler-sized entrance and warm interior glow: pass.
  - Text remains user-managed and is not blocking, consistent with prior accepted pages.
- Next action: user review page 8 v4 visually; if accepted, generate page 9 only.
## Batch 3 Page 8 Generation v5 Fresh Reference Lock - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v5_fresh_reference_lock.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edde5-0791-73c1-b62d-9b9f8992b10d/ig_07c7ece23fd5a031016a34b8ec0edc819181fb95a08f827c4f.png`
- Status: `hold / reference-light, do not promote`
- Reason for fresh pass:
  - User flagged that there should be 2026-06-19 rework context and that prior page 8 attempts kept drifting from the references.
  - This pass starts from the correct `rework_2026-06-18` worktree context, not the older `work_2026-06-06` batch folder.
  - Prompt explicitly excludes page 8 v2, v3, and v4 as visual references and restates official Tori/Banguli/tunnel lock as visual truth.
  - Important correction: in this session, the built-in image generation call received local file paths as prompt text only; the official reference PNGs were not actually attached as image inputs. Treat this candidate as prompt-described rather than truly reference-grounded.
- Reference grounding requested in prompt:
  - Official Tori, highest priority: `series/coral-town-daycare/references/characters/?좊━.png`
  - Official Banguli, highest priority: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Tunnel lock for prop scale/shape: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Page 7 continuity only: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Composition is simpler than prior page-8 attempts, with Tori larger for character-detail review: pass.
  - Tunnel remains a low single-entrance toddler crawl-through tube with warm interior glow: candidate pass, user should review scale against the official tunnel lock.
  - Tori and Banguli were re-locked in the prompt text, but the official PNGs were not actually attached as pixel references: fail for non-negotiable reference grounding.
  - Text remains generator-rendered; user has been handling text QA, so visual reference fidelity is the main review criterion.
- Next action: do not use v5 for approval/final. Regenerate page 8 with actual attached image references; if that path is unavailable, pause rather than making another text-only attempt.
## Batch 3 Page 8 Generation v6 Actual Refs With Page 7 Continuity - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v6_actual_refs_page7_continuity.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edde5-0791-73c1-b62d-9b9f8992b10d/ig_07c7ece23fd5a031016a34c2bf4bd88191bdbbe26717bb0f4b.png`
- Status: `hold / superseded`
- Reference grounding:
  - Actual official Tori image emitted into the conversation as image input: `series/coral-town-daycare/references/characters/?좊━.png`
  - Actual official Banguli image emitted into the conversation as image input: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Actual tunnel lock image emitted into the conversation as image input: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Page 7 continuity image also emitted: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
- QA:
  - Actual image references were attached through `nodeRepl.emitImage`: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Page 7 continuity likely contaminated Tori's eye/face shape: fail for exact character lock.
  - Do not promote; use only as process history.
- Next action: retry with official Tori, official Banguli, and tunnel lock only.

## Batch 3 Page 8 Generation v7 Official Refs Only - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v7_official_refs_only.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edde5-0791-73c1-b62d-9b9f8992b10d/ig_07c7ece23fd5a031016a34c48b049881919f2a758ee569227c.png`
- Status: `backup candidate / superseded by v8 tunnel-scale retry`
- Reference grounding:
  - Actual official Tori image emitted into the conversation as image input: `series/coral-town-daycare/references/characters/?좊━.png`
  - Actual official Banguli image emitted into the conversation as image input: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Actual tunnel lock image emitted into the conversation as image input: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Earlier page 7 and page 8 candidates were explicitly excluded as visual references.
- QA:
  - Actual official image references were attached through `nodeRepl.emitImage`: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Tori's profile eye and face moved back toward the official small dark eye and soft character design: pass.
  - Banguli remains close to the official water-drop shape: pass.
  - Tunnel is readable and warm, but user noted it may still feel a little large: hold as backup.
- Next action: make one final targeted tunnel-scale retry, then move on if still imperfect.

## Batch 3 Page 8 Generation v8 Smaller Tunnel Final Retry - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edde5-0791-73c1-b62d-9b9f8992b10d/ig_05276b5ad6e8ae2d016a34c5ea5f548191a693f2655394ce74.png`
- Status: `user approved`
- User correction applied:
  - Keep the recovered v7 character fidelity.
  - Reduce the tunnel entrance and interior volume so the tunnel reads less like a cave and more like a low toddler crawl-through prop.
  - Treat this as the final tunnel-scale retry before moving on unless the user explicitly asks for another pass.
- Reference grounding:
  - v7 was emitted as the edit target after the user noted character recovery.
  - Actual official Tori image was emitted again as highest-priority identity reference: `series/coral-town-daycare/references/characters/?좊━.png`
  - Actual official Banguli image was emitted again as highest-priority identity reference: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Actual tunnel lock image was emitted again as highest-priority tunnel scale/shape reference: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Character identity remains grounded by actual official reference images: pass.
  - Tunnel scale is smaller/lower than v7 and less cave-like: candidate pass, user should make the final visual call.
  - Text remains generator-rendered; user has been handling text QA, so visual reference fidelity and tunnel scale are the main review criteria.
- Next action: user review v8. If accepted, continue page 9; if still slightly imperfect, move on per user direction.
## Batch 3 Page 8 User Approval - 2026-06-19

- Approved file: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png`
- Status: `user approved`
- User note: character reference recovery is acceptable; tunnel scale is acceptable enough to pass.
- Next action: generate page 9 only.
## Batch 3 Page 9 Generation v1 - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/09_candidate_2026-06-19_v1.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019edde5-0791-73c1-b62d-9b9f8992b10d/ig_05276b5ad6e8ae2d016a34c8a1c7f481919679437e0e8d824f.png`
- Status: `user approved`
- Reference grounding:
  - Actual official Tori image emitted into the conversation as highest-priority identity reference: `series/coral-town-daycare/references/characters/?좊━.png`
  - Actual official Banguli image emitted into the conversation as highest-priority identity reference: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Actual tunnel lock image emitted into the conversation as highest-priority tunnel scale/shape reference: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Approved page 8 v8 emitted as immediate continuity reference: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png`
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Tori is moving forward into the tunnel and the shell is entering: pass.
  - Banguli is ahead inside the tunnel as guide: pass.
  - Tunnel remains a single low warm tunnel with no visible second exterior exit: pass.
  - Tori has no school bag during playground tunnel play: pass.
  - Text appears generator-rendered and should receive user text QA before final promotion.
- Next action: user review page 9 v1. If accepted, mark Batch 3 pages 7-9 approved and prepare the next handoff.
## Batch 3 Page 9 User Approval - 2026-06-19

- Approved file: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/09_candidate_2026-06-19_v1.png`
- Status: `user approved`
- User note: page 9 is approved; move to Batch 4 preparation.

## Batch 3 Gate Close - 2026-06-19

- Status: `batch approved for continuing production`
- Approved Batch 3 files:
  - `batch_3/07_candidate_2026-06-18_v1.png`
  - `batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png`
  - `batch_3/09_candidate_2026-06-19_v1.png`
- Held/superseded page 8 files remain process history only and must not be used as visual references:
  - `batch_3/08_candidate_2026-06-18_v2.png`
  - `batch_3/08_candidate_2026-06-18_v3_character_ref_lock.png`
  - `batch_3/08_candidate_2026-06-18_v4_exact_tori_lock.png`
  - `batch_3/08_candidate_2026-06-19_v5_fresh_reference_lock.png`
  - `batch_3/08_candidate_2026-06-19_v6_actual_refs_page7_continuity.png`
  - `batch_3/08_candidate_2026-06-19_v7_official_refs_only.png`
- Carry-forward locks:
  - Use actual image inputs via `nodeRepl.emitImage`; do not rely on local paths in prompt text alone.
  - Official Tori, Banguli, friends, Mari teacher, playground, and tunnel files are the visual truth.
  - Approved pages may support continuity only after user acceptance.
  - Tori has no school bag during playground/tunnel play.
  - Tunnel remains a low straight toddler crawl-through prop unless the page explicitly shows the far exit.

## Batch 4 Prompt Plan Ready - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_4/batch_4_prompt_plan.md`
- Status: `ready`
- Scope:
  - Page 10: Tori comes out the far side, joyful achievement moment.
  - Page 11: friends and Mari teacher celebrate Tori's courage.
  - Page 12: Tori confidently leads the group through the tunnel for the finale.
- Next action: generate page 10 only with actual attached references.

## Batch 4 Page 10 Generation v1 - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_4/10_candidate_2026-06-19_v1.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019ede5b-12f2-7e20-8076-54b574c50559/ig_05c3c66ecf7e0f71016a34d4799d78819195202be85e087b07.png`
- Status: `candidate pass / pending user review`
- Reference grounding:
  - Actual official Tori image emitted into the conversation as highest-priority identity reference: `series/coral-town-daycare/references/characters/?좊━.png`
  - Actual official Banguli image emitted into the conversation as highest-priority identity reference: `series/coral-town-daycare/references/characters/諛⑹슱??png`
  - Actual playground image emitted: `series/coral-town-daycare/references/諛곌꼍_?꾧꼍怨???댄꽣.png`
  - Actual tunnel lock image emitted: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
  - Approved page 9 emitted as immediate continuity support: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_3/09_candidate_2026-06-19_v1.png`
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Tori emerges from the far side with clear joy and achievement: pass.
  - Banguli celebrates beside Tori: pass.
  - Tunnel reads as one exit of the same tunnel, not an L shape or second separate tunnel: candidate pass.
  - Caveat: tunnel opening is still somewhat large; user should make final scale call.
  - Text appears generator-rendered and should receive user text QA before final promotion.
- Next action: user review page 10; if accepted, use as continuity support for final promotion only.

## Batch 4 Page 11 Generation v1 - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_4/11_candidate_2026-06-19_v1.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019ede5b-12f2-7e20-8076-54b574c50559/ig_05c3c66ecf7e0f71016a34d58346808191aaf173c817f39ad8.png`
- Status: `candidate pass / pending user review`
- Reference grounding:
  - Actual official Tori, Mari teacher, Banguli, Juni, Lulu, Aru, and Mongle images emitted as identity references.
  - Actual playground and tunnel lock images emitted.
  - Page 10 candidate emitted as continuity support only.
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Tori remains emotional center and reads shy/proud: pass.
  - Friends celebrate kindly without crowding or grabbing: pass.
  - Mari teacher is warm and at Tori's eye level: pass.
  - Tunnel remains small in the background and does not dominate: pass.
  - Text appears generator-rendered and should receive user text QA before final promotion.
- Next action: user review page 11; if accepted, use as continuity support for final promotion only.

## Batch 4 Page 12 Generation Attempts - 2026-06-19

- Status: `resolved to saved v1 candidate after targeted retries`
- Retry notes:
  - First preview had good finale mood but appeared to omit Popo; not copied into the batch folder.
  - Second preview recovered Popo but appeared to hide or omit Sua; not copied into the batch folder.
  - Third preview was saved because both Sua and Popo are visible enough for review.

## Batch 4 Page 12 Generation v1 - 2026-06-19

- File: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/batch_4/12_candidate_2026-06-19_v1.png`
- Built-in generated source: `C:/Users/USER/.codex/generated_images/019ede5b-12f2-7e20-8076-54b574c50559/ig_05c3c66ecf7e0f71016a34da744df481918538b439d50ea7e7.png`
- Status: `candidate pass with caveats / pending user review`
- Reference grounding:
  - Actual official Tori, Mari teacher, Banguli, Juni, Aru, Lulu, Mongle, Sua, and Popo images emitted as identity references.
  - Actual playground and tunnel lock images emitted.
  - Page 11 candidate emitted as continuity support only.
- QA:
  - File persisted in the batch folder: pass.
  - A5 portrait ratio retained at `1054x1492`: pass.
  - Tori leads at the tunnel with confident forward posture: pass.
  - Banguli stays beside Tori: pass.
  - Popo and Sua are both visible enough for user review: candidate pass.
  - Caveat: a small extra purple seahorse-like duplicate may be present; user should decide whether this needs a targeted retry.
  - Caveat: some friend bag details may have drifted back from the official reference sheets; user should decide whether to retry before final promotion.
  - Tunnel remains one low straight tunnel and does not become an L shape or two-tunnel layout: pass.
  - Text appears generator-rendered and should receive user text QA before final promotion.

## Batch 4 Handoff - 2026-06-19

- Approved final files: none yet; batch 4 is candidate-only pending user review.
- Candidate files for review:
  - `batch_4/10_candidate_2026-06-19_v1.png`
  - `batch_4/11_candidate_2026-06-19_v1.png`
  - `batch_4/12_candidate_2026-06-19_v1.png`
- Rejected/held previews:
  - Unsaved page 12 preview 1: rejected because Popo appeared missing.
  - Unsaved page 12 preview 2: rejected because Sua appeared missing or hidden.
- Required references carried forward:
  - Official character PNGs under `series/coral-town-daycare/references/characters/`
  - Playground reference: `series/coral-town-daycare/references/諛곌꼍_?꾧꼍怨???댄꽣.png`
  - Tunnel lock: `series/coral-town-daycare/images/episodes/?좊━????嫄몄쓬留?rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Carried-forward locks:
  - User text QA is still required before final promotion.
  - Official individual references remain visual truth; candidate pages are continuity support only after user acceptance.
  - Keep Tori without a school bag during tunnel play.
  - Keep the tunnel a single low straight toddler crawl-through prop.
- Next concrete action:
  - User review pages 10-12. If accepted, promote or copy to the series-standard final location. If not, retry only the failing page or run a targeted text-panel correction.
## Batch 4 User Review and Targeted Revisions - 2026-06-19

- User feedback:
  - Page 10 needed a clearer opposite-side composition after page 9. The tunnel should face right, Tori should come out to the right, and the slide should be removed from the background.
  - Page 11 needed Lulu restored to the official Lulu design.
  - Page 12 had duplicate Sua and leftover friend bags.
- Accepted for now:
  - `batch_4/11_candidate_2026-06-19_v2_lulu_fix.png`
  - `batch_4/12_candidate_2026-06-19_v2_last_generated_ok.png`
- New page 10 candidate:
  - `batch_4/10_candidate_2026-06-19_v3_right_exit_no_slide.png`
  - Built-in generated source: `C:/Users/USER/.codex/generated_images/019ede5b-12f2-7e20-8076-54b574c50559/ig_02b38b1ec902f52c016a34ec2ce8788191977c8ae40edd0355.png`
  - Status: `candidate pass / pending user review`
  - Correction applied: right-facing tunnel exit, Tori emerging toward the right, no background slide.
- Carry-forward:
  - User still handles final text QA before promotion.
  - Use page 10 v3, page 11 v2, and page 12 v2 as the active Batch 4 review set unless the user requests another targeted retry.
## Final Promotion - 2026-06-19

- Status: `final promoted`
- User instruction: existing `final` folder files are old-version assets; promote the whole new set based on this worklog.
- Final folder: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final`
- Verification:
  - 13 PNG files present: pass
  - Source-to-final SHA256 hashes match for all promoted files: pass
  - All final files are portrait A5-like ratio: pass
- Promoted files:
  - `batch_1/00_cover_candidate_2026-06-18_v2.png` -> `final/00_표지.png`
  - `batch_1/01_candidate_2026-06-18_v1.png` -> `final/01_페이지.png`
  - `batch_1/02_candidate_2026-06-18_v1.png` -> `final/02_페이지.png`
  - `batch_1/03_candidate_2026-06-18_v1.png` -> `final/03_페이지.png`
  - `batch_2/04_candidate_2026-06-18_v1.png` -> `final/04_페이지.png`
  - `batch_2/05_candidate_2026-06-18_v1.png` -> `final/05_페이지.png`
  - `batch_2/06_candidate_2026-06-18_v2.png` -> `final/06_페이지.png`
  - `batch_3/07_candidate_2026-06-18_v1.png` -> `final/07_페이지.png`
  - `batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png` -> `final/08_페이지.png`
  - `batch_3/09_candidate_2026-06-19_v1.png` -> `final/09_페이지.png`
  - `batch_4/10_candidate_2026-06-19_v3_right_exit_no_slide.png` -> `final/10_페이지.png`
  - `batch_4/11_candidate_2026-06-19_v2_lulu_fix.png` -> `final/11_페이지.png`
  - `batch_4/12_candidate_2026-06-19_v2_last_generated_ok.png` -> `final/12_페이지.png`
- Caveat:
  - Text QA remains user-managed per the earlier batch notes; this promotion follows the user's explicit final-folder replacement instruction.
