# Episode worklog - 토리야, 한 걸음만

## Source

- Drive source: https://drive.google.com/file/d/1bQmCApoPYbDmHod0wD00f35Jf2KFaNGK/view?usp=drivesdk
- Local script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Series rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`

## Reference setup

- Created official coral tunnel reference:
  - `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Updated official playground/front reference so the coral tunnel is now part of the recurring playground:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Created a larger-tunnel V2 playground reference for mobile review and possible official selection:
  - `series/coral-town-daycare/references/배경_전경과_놀이터_v2_coral_tunnel_large.png`
- Created V3 with the tunnel pulled forward from the sand-play boundary and extra lower foreground space:
  - `series/coral-town-daycare/references/배경_전경과_놀이터_v3_coral_tunnel_foreground.png`
- Created V4 with the tunnel turned sideways so it reads as a left-to-right playground passage, with less emphasis on the detailed interior:
  - `series/coral-town-daycare/references/배경_전경과_놀이터_v4_coral_tunnel_sideways.png`
- User approved V4 as the playground reference. Copied V4 over the official recurring playground file:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Preserved previous playground reference:
  - `series/coral-town-daycare/references/배경_전경과_놀이터_backup_before_coral_tunnel_2026-06-03.png`
- Mobile review deck:
  - https://docs.google.com/presentation/d/1yKEF-tZIr5nY_6PCu7_bCc1hFePJtHD5PUzyJzeCWi8

## Locked visual notes

- The coral tunnel is a rounded toddler-safe playground tunnel, not a scary cave.
- It uses pastel pink-coral puffy coral forms, thick rounded rims, and visible open ends.
- The inside can be slightly dim, but it must stay warm and safe with soft light from the opposite opening.
- Small shell and sea-glass decorations may appear on the inner wall.
- Future playground scenes should include the coral tunnel as a normal recurring playground fixture after this episode.

## Episode scope

- Title: `토리야, 한 걸음만`
- Structure: cover plus pages 1-12.
- Core story: Tori is nervous about the new coral tunnel, receives patient support, tries one small step, and later leads the tunnel play.

## Next step

- Batch 1 has been prepared and readiness-checked, but not generated yet.
- Page plan:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/page_plan.md`
- Batch 1 prompt plan:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/batch_1_prompt_plan.md`
- Batch 1 scope:
  - `00_표지`, `01_페이지`, `02_페이지`, `03_페이지`
- Use character refs from `series/coral-town-daycare/references/characters/`.
- Use the updated playground reference and the coral tunnel reference for all playground/tunnel pages.

## Batch 1 readiness check - 2026-06-03

- Required character references verified present:
  - `토리.png`, `방울이.png`, `마리_선생님.png`, `준이.png`, `아루.png`, `루루.png`, `몽글이.png`, `수아.png`, `포포.png`
- Required background/location references verified present:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Work folder exists:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1`
- Final folder exists and is still empty:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final`
- Batch 1 candidate output names locked:
  - `00_cover_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`
- Generation status:
  - Ready to generate Batch 1 with exact Korean text in-image on the first pass.
  - After generation, QA text exactness first, then character identity, tunnel safety/readability, A5 portrait ratio, and contamination.

## Batch 1 generation - 2026-06-03

- Generated and saved first-pass candidates:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/00_cover_candidate_text_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - Visual QA: Tori/Banguli/tunnel composition usable.
    - Text QA: fail/repair needed. Title/subtitle lettering is not reliably exact.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/01_candidate_text_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - Visual QA: playground introduction, group placement, Tori cautious approach usable.
    - Text QA: needs close visual review before approval.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/02_candidate_text_v1.png`
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - Visual QA: friends' tunnel play and Tori watching from a distance usable.
    - Text QA: fail/repair needed. At least `슝—` appears unreliable, and full text must be corrected or regenerated.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/03_candidate_text_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - Visual QA: Tori worry close/medium shot and safe tunnel mood usable.
    - Text QA: needs close visual review before approval.
- Batch 1 status:
  - First-pass visual candidates complete.
  - Do not promote to final yet.
  - Next recommended step: repair text on the best visual candidates with deterministic text panels, or regenerate only failed text pages if generator-rendered text is required.

## User QA notes - Batch 1

- Cover:
  - `00_cover_candidate_text_v1.png` accepted visually by user.
- Pages 1-3:
  - Outdoor play scenes should not show children wearing bags. Remove bags from Tori and friends during playground play pages.
  - The tunnel grows too large from page 2 to page 3. Keep the tunnel about the same relative size as page 1.
  - Regenerate pages 1-3 with a consistent toddler playground tunnel scale: visible and story-important, but not oversized or cave-like.

## Batch 1 revision after user QA - 2026-06-03

- Cover:
  - Keep `00_cover_candidate_text_v1.png` as the accepted visual candidate.
- Page 1:
  - Generated `01_candidate_text_v2.png` with no bags, but the tunnel became too large.
  - Edited the original page 1 candidate to preserve its better tunnel scale and remove children's bags.
  - Current preferred candidate: `01_candidate_text_v3.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - Visual QA: no child bags, tunnel scale closest to the user-approved page 1 size.
- Page 2:
  - Generated `02_candidate_text_v2.png`; bags improved, but tunnel still too large.
  - Generated `02_candidate_text_v3.png` with stronger scale lock.
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - Visual QA: no bags and smaller than v2; still needs user review for whether tunnel scale now matches page 1 closely enough.
- Page 3:
  - Generated `03_candidate_text_v2.png`; Tori bag removed, but tunnel still oversized.
  - Generated `03_candidate_text_v3.png` with physical tunnel held in mid-ground/background and worry shown through Tori/thought clouds.
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - Visual QA: no bag and improved scale; still needs user review for whether tunnel is sufficiently close to page 1 size.
- Current batch 1 review set:
  - `00_cover_candidate_text_v1.png`
  - `01_candidate_text_v3.png`
  - `02_candidate_text_v3.png`
  - `03_candidate_text_v3.png`

## Batch 1 restart attempt - aborted QA - 2026-06-03

- User identified the restart outputs as not accurately reference-driven:
  - Except for Mari teacher, the child characters appear generated mostly from text prompts rather than faithfully reflecting the official character reference images.
- Treat the newly generated restart attempt as rejected / do not use for final.
- Required process change before continuing:
  - Do not generate crowded multi-character pages from prose plus many reference names.
  - Use fewer characters per generation pass where possible, or prepare page-specific visual reference boards with the exact official character references enlarged and separated.
  - For page 1, if all friends must appear, composition should reduce them to clear, reference-faithful small groups rather than asking the generator to invent all children at once.
  - Keep the user's hard locks: outside playtime means no bags; Lulu and Sua must not mix; Aru must have no hands/arms/legs/feet and must keep scarf; tunnel size stays just large enough that Tori has to lower his body/head to pass.

## Reference-board workflow test - Batch 1 - 2026-06-03

- Created page-specific official reference boards under:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/ref_boards/`
- Boards created:
  - `00_cover_ref_board.png`
  - `01_page_ref_board.png`
  - `02_page_ref_board.png`
  - `03_page_ref_board.png`
- Board procedure:
  - Put only official reference images on the board.
  - Add page-specific labels and hard locks directly inside the board.
  - Explicitly state that reference bags are to be removed only because this is outside playtime.
  - Use the board as the visual source of truth immediately before generation.
- Generated reference-board candidates:
  - `00_cover_candidate_refboard_v1.png`
    - Visual QA: strongest result of this test. Tori and Banguli read close to official references, Tori has no bag, tunnel is small enough for the story scale, and blank title area is usable.
    - Text QA: illustration-only / blank title area. Needs deterministic title/subtitle panel later.
  - `01_candidate_refboard_v1.png`
    - Visual QA: major improvement over prose-only attempt. Tori, Mari, Jun, Aru, Lulu, Mongle, Sua, and Popo are more reference-faithful; child bags are mostly removed; Aru has no limbs and keeps scarf; Lulu/Sua separation is readable.
    - Remaining issue: page feels posed/inspection-like rather than an active discovery scene; Sua's blue outfit detail is weak; tunnel still reads a little large.
    - Text QA: illustration-only / blank panel. Needs deterministic story text later.
  - `02_candidate_refboard_v1.png`
    - Visual QA: major improvement over prose-only attempt. Tori has no bag, Aru remains a limbless pufferfish with scarf, Lulu stays pink, Mongle stays octopus, tunnel scale is much improved.
    - Remaining issue: Jun's movement pose is awkward/crawling-like; could use a simpler standing/entering pose if regenerated.
    - Text QA: illustration-only / blank panel. Needs deterministic story text later.
  - `03_candidate_refboard_v1.png`
    - Visual QA: Tori identity and no-bag rule improved, but tunnel became too large.
    - Status: reject/hold; superseded by v2.
  - `03_candidate_refboard_v2.png`
    - Visual QA: strongest page 3 candidate. Tori is reference-faithful, no bag, tunnel is reduced to toddler playground scale, blank text panel is usable.
    - Text QA: illustration-only / blank panel. Needs deterministic story text later.
- Procedure verdict:
  - Page-specific reference boards are materially better than text prompts plus separate references.
  - The workflow should become an official skill step, but with two extra constraints:
    - First pass should prioritize visual fidelity and leave blank text panels; add story text deterministically later.
    - Multi-character scenes need simplified actions and smaller groups; otherwise they become posed or motion gets awkward.

## Hold / next-day handoff - 2026-06-03

- User decided to pause Batch 1 restart for today.
- Important interpretation:
  - Do not treat the reference-board procedure itself as proven defective.
  - Today's outputs may have been affected by temporary image model quality degradation / instability.
  - The reference-board workflow showed enough improvement to keep as a candidate procedure, but final judgment should wait for a fresh generation pass.
- Current status:
  - Do not promote any `*_refboard_*` candidate to final yet.
  - Keep them as diagnostic candidates for comparing against the next session's model behavior.
  - Best diagnostic candidates from today's run:
    - `00_cover_candidate_refboard_v1.png`
    - `02_candidate_refboard_v1.png`
    - `03_candidate_refboard_v2.png`
  - Page 1 remains the most fragile because it contains many characters.
- Recommended next session:
  - Re-open this worklog and `batch_1_prompt_plan.md`.
  - Reuse the official reference boards in `batch_1/ref_boards/`.
  - Start with one low-complexity page such as page 3 or cover to check whether image model reference fidelity has recovered.
  - If quality is better, continue with smaller grouped generations for pages 1-2.
  - Keep all hard locks: outside playtime means no bags; Lulu and Sua must not mix; Aru must have no hands/arms/legs/feet and must keep scarf; tunnel size stays just large enough that Tori has to lower his body/head to pass.

## Batch 1 fresh reference-board pass - 2026-06-04

- Restarted Batch 1 from the next-day handoff using the page-specific reference boards.
- Generation mode:
  - illustration-only candidates with clean blank text panels/spaces.
  - exact Korean story text still needs a deterministic text pass after user visual approval.
- Fresh candidate set:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/00_cover_candidate_refboard_fresh_v1.png`
    - QA: candidate pass for mobile review. Tori/Banguli/tunnel relationship is clear, no bag on Tori, blank title/subtitle panels available. Tunnel is prominent but still warm and toddler-safe.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/01_candidate_refboard_fresh_v1.png`
    - QA: candidate pass for mobile review. Character reference fidelity is improved over the aborted prose-only pass. No child bags visible, Aru remains limbless with scarf, Lulu/Sua separation is readable, and the group scene is less inspection-like than the prior refboard candidate.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/02_candidate_refboard_fresh_v1.png`
    - QA: candidate pass for mobile review. Jun's pose is simpler and less awkward than the prior diagnostic candidate. Tori watches from the side with no bag; Aru/Lulu/Mongle identities are readable. Tunnel is slightly large but remains soft and non-scary.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/03_candidate_refboard_fresh_v1.png`
    - QA: candidate pass / review carefully. Tori identity, no-bag rule, and blank text panel pass. One worry-thought cloud is darker than ideal, so user should decide whether to keep, lighten in edit, or regenerate page 3.
- Mobile review upload:
  - Google Slides: https://docs.google.com/presentation/d/14TQ2mpYPU8-58h0k1N-M5MjHtRjNLKDBc4-JApFrag8/edit?usp=drivesdk
- Current status:
  - Do not promote to final yet.
  - Await user visual approval or targeted regeneration requests.
  - If approved, next step is deterministic Korean text-panel pass for cover and pages 1-3, then final promotion.

## Batch 1 text-in-image pass - 2026-06-04

- User feedback on `*_refboard_fresh_v1`:
  - Character fidelity is better than the prior day but still weak.
  - Page 1 Mari teacher is not accurate enough.
  - Page 1 Sua outfit is distorted.
  - Tunnel scale is too large overall.
  - Required tunnel scale: just large enough that Tori must bend/lower the body to pass.
- Generated text-in-image candidates:
  - `00_cover_candidate_text_fresh_v1.png`
  - `01_candidate_text_fresh_v1.png`
  - `02_candidate_text_fresh_v1.png`
  - `03_candidate_text_fresh_v1.png`
- QA on v1 text candidates:
  - Text rendering is stronger than earlier text attempts.
  - Tunnel scale still reads too large, especially pages 2-3.
  - Do not use v1 as the primary review set unless comparing text quality.
- Generated stricter small-tunnel v2 candidates:
  - `00_cover_candidate_text_fresh_v2.png`
    - QA: primary text review candidate. Korean text readable. Tunnel is smaller than v1 and shows Tori standing taller than the opening, but still visually prominent.
  - `01_candidate_text_fresh_v2.png`
    - QA: primary text review candidate. Korean text readable. Mari teacher is improved; Sua keeps lavender/blue direction better than v1. Tunnel is lower and smaller than v1, though still has strong page presence.
  - `02_candidate_text_fresh_v2.png`
    - QA: primary text review candidate. Korean text readable. Tunnel scale is best aligned with the user's bend/lower-body requirement; Jun's pose supports the low-opening scale.
  - `03_candidate_text_fresh_v2.png`
    - QA: primary text review candidate with caveat. Korean text readable and tunnel is smaller than v1. One thought cloud remains darker than ideal; consider lightening or regenerating if user rejects the mood.
- Current recommended review set:
  - `00_cover_candidate_text_fresh_v2.png`
  - `01_candidate_text_fresh_v2.png`
  - `02_candidate_text_fresh_v2.png`
  - `03_candidate_text_fresh_v2.png`
- Google Drive upload status:
  - Created empty review deck: https://docs.google.com/presentation/d/1p05mqwc5Q4u7YmX7ZrYU4WSrc96OOUdjRni-fmEXqbE/edit?usp=drivesdk
  - After explicit user approval, inserted all four v2 text candidates into the deck and removed the default blank title slide.
  - Verified the deck contains only four review slides.
- Current status:
  - Do not promote to final yet.
  - Await mobile visual review decision.

## Coral tunnel prop scale lock - 2026-06-04

- User observed the coral tunnel size and shape keep changing between pages.
- Diagnosis:
  - The existing playground reference only contains the tunnel as a single background element.
  - Page prompts were asking the image model to reinterpret tunnel size and shape per scene.
  - For this episode, the tunnel must be treated as a recurring prop with a concrete reference sheet, especially for scale.
- Generated prop reference sheet candidates:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/prop_refs/coral_tunnel_scale_reference_sheet_v1.png`
    - QA: useful layout, but still reads too much like a coral cave/mound and the entrance is slightly high for the required Tori bend.
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/prop_refs/coral_tunnel_scale_reference_sheet_v2.png`
    - QA: preferred prop lock candidate. Lower, flatter toddler crawl-tube silhouette; Tori must bend at the waist to enter; Mari teacher is clearly too tall; small child scale is readable.
- Promoted reference copy for future sessions:
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v1.png`
- User feedback on promoted v1:
  - It still reads as a closed coral cave, not a pass-through tunnel.
  - The crawling Tori is much smaller than the standing Tori, which breaks the scale comparison.
- Generated corrected pass-through candidate:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/prop_refs/coral_tunnel_scale_reference_sheet_v3.png`
    - QA: preferred over v1/v2. Both ends are visibly open; front and 3/4 views read as a pass-through tunnel rather than a cave. Bending Tori is closer to the same scale as standing Tori, though the coral body remains visually thick.
- Updated promoted reference copy for future sessions:
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
- Carried-forward tunnel lock:
  - Use `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png` as the visual source of truth for every future page containing the coral tunnel.
  - Prompt lock: the tunnel is a pass-through low toddler crawl-through half-cylinder tube with both ends open, not a cave, not a closed den, not a giant arch, not a building-like mound.
  - Scale lock: tunnel top is around Tori's lower chest / upper belly height when Tori stands beside it; Tori must bend at the waist and lower the shell/head to pass.
  - Same-character scale lock: if Tori appears standing and bending/crawling in the same reference or story page, both poses must keep the same head, shell, hat, and body size; only the pose changes.
  - Teacher lock: Mari teacher is far too tall to enter.
  - Avoid generating Batch 1 pages again from the old playground tunnel alone; attach this prop reference sheet together with character references.

## Handoff before commit/push - 2026-06-04

- User had to move and requested logging, commit, and push.
- Current newest prop reference:
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
  - Use this instead of the earlier cave-like tunnel references.
- First cover regeneration attempt with the new tunnel reference:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/00_cover_candidate_text_prop_tunnel_v1_reject.png`
  - Status: reject / diagnostic only.
  - Problems:
    - Cover was not generated in the required A5 portrait format.
    - Tunnel reads as a pass-through tunnel better than before, but it is slightly too small for the cover composition.
    - Tori still needs to remain clearly larger than the tunnel opening, but the tunnel itself can be a little larger and more readable than this rejected cover attempt.
- Next concrete action:
  - Regenerate cover first, not the full batch.
  - Required canvas/composition: A5 portrait cover, not landscape.
  - Required tunnel lock: both ends open / pass-through, not a cave; slightly larger than `00_cover_candidate_text_prop_tunnel_v1_reject.png`, but still low enough that Tori must bend at the waist to pass.
  - Required Tori lock: no outside-play bag; green turtle child with yellow hat and shell.
  - Required text: include exact Korean cover text only after the A5 portrait composition and tunnel scale are correct, or generate with text if text fidelity is stable.

## Cover text-in-image retry with prop reference - 2026-06-04

- User requested one more cover generation with text included, 반드시 레퍼런스 이미지 참조.
- References inspected immediately before generation:
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
- Generated and saved:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/00_cover_candidate_text_prop_tunnel_v2_hold.png`
- QA:
  - A5 portrait composition: pass.
  - Korean cover text: mostly readable; title is close to exact, subtitle is readable.
  - Reference use: playground mood, Tori/Banguli, and pass-through tunnel are visibly reference-driven.
  - Hold / do not promote yet:
    - Tori still appears to retain a strap/backpack-like detail despite the no-bag lock.
    - Tunnel remains somewhat large/high relative to the strict lower-chest / upper-belly scale lock.
- Next recommended action:
  - If regenerating again, use an even simpler cover composition with Tori drawn from the front/side without any back-visible area, so the model cannot preserve a bag/strap silhouette from the character sheet.
  - Keep text-in-image if user prioritizes quick mobile review; otherwise generate illustration-only after the no-bag and tunnel scale pass, then add deterministic text.

## Batch 1 body text-in-image attempt with prop reference - 2026-06-04

- User approved the cover direction as good-looking and requested trying the body pages too.
- References inspected / used in context before generation:
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/수아.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
- Note:
  - The older `batch_1/ref_boards/` image files are no longer present after repository sync, so generation used the official source references directly rather than the missing board composites.
- Generated and saved:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/02_candidate_text_prop_tunnel_v1_hold.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-03/batch_1/03_candidate_text_prop_tunnel_v1_hold.png`
- QA:
  - Page 2 hold:
    - Tori no-bag direction improved.
    - Friend action and pass-through tunnel are readable.
    - Text is not exact; `슝—` appears unreliable.
    - Tunnel still reads larger than the strict prop scale lock.
  - Page 3 hold:
    - Tori worry mood and text block are readable.
    - Text is not exact enough for final.
    - Tunnel still reads larger than the strict prop scale lock.
- Page 1:
  - Three text-in-image generation attempts failed with image generation server errors, including simplified prompts.
  - Do not infer a visual QA judgment for page 1 from this failure; retry later with a shorter prompt or a freshly rebuilt page-specific reference board.
- Current recommendation:
  - Treat pages 2-3 as mobile-review / direction candidates only.
  - For final-quality body pages, rebuild page-specific ref boards including the new tunnel prop reference, then regenerate in smaller units.
  - If exact Korean text remains unstable, use approved illustration candidates plus deterministic text panel placement.

## Batch 1 restart - 2026-06-06

- Restarting after the 2026-06-04 hold because the user wants to test whether today's image model quality has recovered.
- New work folder:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_1`
- Prompt plan:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_1/batch_1_restart_prompt_plan.md`
- First action:
  - Regenerate cover only as a model-quality check before continuing pages 1-3.
- Hard locks carried forward:
  - Use `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png` as the tunnel scale source of truth.
  - Tunnel is a low pass-through toddler crawl-through tube with both ends open, not a cave or giant arch.
  - Tori has no bag or strap in outdoor-play cover/pages.
  - Banguli remains a soft pale sky-blue water droplet mascot.
  - If text is unstable, preserve clean blank text areas and add deterministic Korean text later.

## Batch 1 generation - 2026-06-06

- User accepted the cover direction and asked to continue the rest of Batch 1.
- Current review candidates saved in:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_1`
- Candidate set:
  - `00_cover_candidate_20260606_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - User note: looks good; do not keep reworking cover text.
    - QA: title/subtitle are readable enough for review; Tori/Banguli mood works. Tunnel remains larger than the strict prop scale, but user accepted the cover direction.
  - `00_cover_candidate_20260606_v2_illustration_only.png`
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - Status: diagnostic/hold only because user preferred v1 and asked not to continue cover work.
  - `01_candidate_20260606_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: review candidate. Text is readable and close to exact; Mari teacher, Tori, Jun, Aru, Lulu, Mongle, Sua, and Popo are visually readable. No obvious child bags. Aru remains limbless with scarf; Lulu/Sua separation is readable. Tunnel is still a little large but warm and non-scary.
  - `02_candidate_20260606_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: strong review candidate. Text is readable and close to exact. Tori's cautious distance, Jun entering, Aru bouncing, Lulu laughing, and Mongle exiting are readable. No obvious child bags. Tunnel reads as a play tunnel, though still slightly larger than the strict prop scale.
  - `03_candidate_20260606_v1.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: review candidate with caveat. Tori's worried expression and Korean text are strong. Thought-cloud worries are gentle. Physical tunnel is larger than the strict prop scale and should be reviewed against the user's tolerance for "emotionally large" page 3 staging.
- Current recommendation:
  - Present Batch 1 candidate set for user review:
    - `00_cover_candidate_20260606_v1.png`
    - `01_candidate_20260606_v1.png`
    - `02_candidate_20260606_v1.png`
    - `03_candidate_20260606_v1.png`
  - Do not promote to final until user approval.
  - If regenerating, page 3 is the most likely target because of tunnel scale; pages 1-2 are usable review candidates.

## User QA notes - Batch 1 - 2026-06-07

- Cover:
  - Keep `00_cover_candidate_20260606_v1.png` direction; no further cover text work requested.
- Page 1:
  - `01_candidate_20260606_v1.png` is rejected/hold for tunnel structure.
  - Problem: tunnel changed from a straight tube into an L-shaped / cornered structure.
  - Required: tunnel must be a straight, single-axis, left-to-right pass-through tube. No L shape, no corner bend, no side branch, no second perpendicular opening.
  - Popo note: unless specifically requested, Popo should not have visible eyes emphasized. Popo emotion should be mostly mouth/body silhouette; do not draw clear black eyes.
- Page 2:
  - `02_candidate_20260606_v1.png` is rejected/hold for tunnel structure.
  - Problem: tunnel changed from straight tube into an L-shaped / cornered structure.
  - Required: same straight, single-axis, left-to-right pass-through tube lock.
- Page 3:
  - `03_candidate_20260606_v1.png` has the correct issue diagnosis: tunnel scale is the problem.
  - Required: regenerate page 3 with the same emotional setup and text quality, but reduce tunnel to the prop reference scale.
- Next action:
  - Regenerate pages 1, 2, and 3 only.
  - Use strong tunnel structure lock: straight horizontal low toddler crawl-through tube, both ends visible or implied along one axis, no L-turn, no corner, no perpendicular second opening, no cave mound.
  - Use Popo eye lock on page 1: no visible black eyes unless the page specifically calls for it.

## Batch 1 revision generation - 2026-06-07

- Regenerated pages 1-3 in the existing work folder:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_1`
- New candidate set:
  - `01_candidate_20260607_v2.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: tunnel is now straight / single-axis rather than L-shaped. Text remains readable and close to exact. Character grouping remains readable.
    - Caveat: Popo no longer has strong black open eyes, but a closed-eye expression is still visible. If the user's Popo rule means no eye marks at all, regenerate page 1 again with Popo turned away or partially behind another child.
  - `02_candidate_20260607_v2.png`
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - QA: tunnel is now straight / single-axis rather than L-shaped. Text is readable and close to exact. Tori's cautious distance and friends' movement read clearly.
  - `03_candidate_20260607_v2.png`
    - Size: `1055 x 1491`, A5 portrait ratio pass.
    - QA: tunnel scale is much improved versus `03_candidate_20260606_v1.png`; actual tunnel is low and toddler-sized while the worry-cloud handles the emotionally large/dark idea. Text is readable and close to exact.
- Current recommended Batch 1 review set:
  - `00_cover_candidate_20260606_v1.png`
  - `01_candidate_20260607_v2.png`
  - `02_candidate_20260607_v2.png`
  - `03_candidate_20260607_v2.png`
- Status:
  - Do not promote to final until user approval.

## User QA notes - Batch 1 revision - 2026-06-07

- Page 1:
  - `01_candidate_20260607_v2.png` is acceptable for now.
- Page 2:
  - `02_candidate_20260607_v2.png` still needs regeneration.
  - Problem: tunnel entrance and exit face the same direction.
  - Required: straight tube remains, but the two openings must be opposite ends of one tube and face opposite directions. Do not draw two front-facing arches on the same side.
- Page 3:
  - `03_candidate_20260607_v2.png` still needs regeneration.
  - Problem: tunnel became too small.
  - Required: increase tunnel size to a middle scale between `03_candidate_20260606_v1.png` and `03_candidate_20260607_v2.png`; still low enough that Tori must bend, but visible enough to feel story-important.

## Batch 1 second revision generation - 2026-06-07

- Regenerated pages 2 and 3 after user QA.
- New candidates:
  - `02_candidate_20260607_v3.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: improves the prior issue where entrance and exit faced the same direction. The tunnel now reads more like one straight tube with opposite ends, though it should still be user-reviewed for geometry tolerance.
    - Text remains readable and close to exact.
  - `03_candidate_20260607_v3.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: tunnel is larger than `03_candidate_20260607_v2.png` and smaller than the too-large `03_candidate_20260606_v1.png`; this is the intended middle scale. Text and Tori worry mood remain strong.
- Current recommended Batch 1 review set:
  - `00_cover_candidate_20260606_v1.png`
  - `01_candidate_20260607_v2.png`
  - `02_candidate_20260607_v3.png`
  - `03_candidate_20260607_v3.png`
- Status:
  - Do not promote to final until user approval.

## User QA notes - Batch 1 second revision - 2026-06-07

- Page 2:
  - `02_candidate_20260607_v3.png` still needs regeneration.
  - Problem: entrance and exit keep appearing at the same time, causing geometry confusion.
  - Required: the exit does not need to be visible. For page 2, show only the near entrance or mostly one visible opening of a straight tube, with the far exit hidden by the tube body, angle, characters, or coral decoration.
- Page 3:
  - `03_candidate_20260607_v3.png` is still too small.
  - Required: make the tunnel about the same visual scale as the accepted cover `00_cover_candidate_20260606_v1.png`; larger and story-important, but still a safe playground tunnel rather than a scary cave.
- Next action:
  - Regenerate pages 2 and 3 only.
  - Page 2 lock: one visible entrance is enough; hide or occlude the far exit.
  - Page 3 lock: cover-like tunnel scale.

## Batch 1 third revision generation - 2026-06-07

- Regenerated pages 2 and 3 after user QA.
- New candidates:
  - `02_candidate_20260607_v4.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: far exit is not visible, so the entrance/exit simultaneous-visibility issue is resolved. One visible entrance is shown; tunnel body continues behind coral decoration/characters. Text remains readable and close to exact.
  - `03_candidate_20260607_v4.png`
    - Size: `1054 x 1492`, A5 portrait ratio pass.
    - QA: tunnel is now cover-like in visual scale and story presence. Tori worry mood and readable text are preserved. Caveat: the imagined dark tunnel in the thought cloud is visually strong; treat it as Tori's worry image, not the real tunnel.
- Current recommended Batch 1 review set:
  - `00_cover_candidate_20260606_v1.png`
  - `01_candidate_20260607_v2.png`
  - `02_candidate_20260607_v4.png`
  - `03_candidate_20260607_v4.png`
- Status:
  - Do not promote to final until user approval.

## Batch 1 approval and Batch 2 handoff prep - 2026-06-07

- User said the latest Batch 1 set is done.
- Promoted approved Batch 1 candidates to final:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/00_표지.png`
    - Source: `work_2026-06-06/batch_1/00_cover_candidate_20260606_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/01_페이지.png`
    - Source: `work_2026-06-06/batch_1/01_candidate_20260607_v2.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/02_페이지.png`
    - Source: `work_2026-06-06/batch_1/02_candidate_20260607_v4.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/03_페이지.png`
    - Source: `work_2026-06-06/batch_1/03_candidate_20260607_v4.png`
- Created Batch 2 work folder and prompt plan:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/batch_2_prompt_plan.md`
- Created next-thread handoff:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/HANDOFF_next_thread_batch_2.md`
- Batch 2 scope:
  - `04_페이지.png`: Lulu and Mongle invite Tori; Tori says no; friends wait.
  - `05_페이지.png`: Mari teacher validates Tori's fear.
  - `06_페이지.png`: Banguli shows the tunnel is safe; Tori takes a tiny step.
- Batch 2 must preserve Batch 1 lessons:
  - For tunnel geometry, one visible entrance is enough when the far exit is not needed.
  - Avoid same-facing double openings and L-shaped tunnel structures.
  - Keep tunnel warm and story-important, not tiny.
  - Outdoor play means no child bags.
  - Popo eyes should not be emphasized unless explicitly requested.

## Batch 2 generation - 2026-06-07

- Started Batch 2 in:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2`
- Generated page 4:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/04_candidate_20260607_v1.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: review candidate. Korean story text appears exact and readable. Tori, Lulu, Mongle, and Mari teacher are visually readable; no child bags are visible; Tori is cautious and respected. The tunnel uses one visible entrance with the far end hidden, avoiding the Batch 1 same-facing/double-opening issue.
  - Caveat: tunnel has a clear right-side presence, so user should confirm whether the page still satisfies "visible but not dominant."
- Generated page 5:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/05_candidate_20260607_v1.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: review candidate. Korean story text appears exact and readable. Mari teacher keeps the yellow apron, star hairpin, purple mermaid tail, and notebook; Tori has no child bag and looks relieved; Banguli reads as a soft water droplet. The tunnel stays in the soft background with one clear entrance and no L-shape or confusing double opening.
  - Caveat: Mari remains visually much larger than Tori, but the pose reads lowered, calm, and validating rather than scolding or pressuring.
- Generated page 6:
  - Raw visual candidate: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/06_candidate_20260607_v1.png`
  - Text-fixed alternate candidate: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/06_candidate_20260607_v1_textfix_v2.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: visual review candidate. Tori has no child bag and takes a tiny step; Mari teacher stays calm and encouraging; Banguli reads as a soft water droplet and peeks out safely. The tunnel is not L-shaped and reads as a single straight playground tube with a near entrance plus an opposite/side exit for Banguli.
  - Text QA: raw generated version was initially suspected for quote-mark drift, so a deterministic text panel repair was created as an alternate. User later confirmed page 6 text has no problem and requested the first version, so `06_candidate_20260607_v1.png` is the current review file.
  - Caveat: because page 6 shows both openings, user should review whether the side/rear Banguli exit clearly reads as the opposite end of one straight tube. The deterministic text uses a clean system Korean font rather than the generator's handwritten text style.
  - Reject/diagnostic only: `06_candidate_20260607_v1_textfix_reject.png` used a variable font that rendered Korean poorly; do not use.
- Mobile review upload:
  - Created local review PPTX: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_2/토리야_한_걸음만_batch_2_mobile_review_20260607.pptx`
  - Imported to Google Drive as native Google Slides:
    - https://docs.google.com/presentation/d/1P4Sf_jnLaK8rH_-1naqDbtEAqj14fr0hF4LI3sgmklc/edit?usp=drivesdk
  - Connector readback verified title, native Slides MIME type, and 3 slides.
  - Thumbnail verification returned all three slides as portrait thumbnails (`1600 x 2264`).
- Mobile review update after user QA:
  - User said page 6 text had no problem and requested the first version.
  - Updated Google Slides slide 3 from `06_candidate_20260607_v1_textfix_v2.png` to `06_candidate_20260607_v1.png`.
  - Connector readback verified the target deck and slide `p3`; fresh thumbnail was downloaded and visually checked as the original page 6 candidate.

## Batch 3 handoff prep - 2026-06-07

- User requested next-thread handoff prep for Batch 3.
- Created Batch 3 work folder and prompt plan:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3/batch_3_prompt_plan.md`
- Created next-thread handoff:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/HANDOFF_next_thread_batch_3.md`
- Batch 3 scope:
  - `07_페이지.png`: Tori reaches the entrance and only peeks the head inside.
  - `08_페이지.png`: Tori discovers the tunnel interior is warm, pretty, and not scary.
  - `09_페이지.png`: Tori takes one step, then another, entering with Banguli guiding ahead.
- Handoff caveat:
  - Batch 2 has review candidates and an updated mobile review deck, but pages 4-6 have not been copied to final yet in this workspace.
  - Next thread should confirm Batch 2 approval first. If accepted, copy `04_candidate_20260607_v1.png`, `05_candidate_20260607_v1.png`, and `06_candidate_20260607_v1.png` to final before generating Batch 3.
- Batch 3 must preserve:
  - one straight toddler crawl-through tunnel, no L shape or confusing double openings;
  - no child bags/straps on Tori;
  - page 7 head-only peek pose;
  - page 8 warm/safe tunnel discovery mood;
  - page 9 forward movement without showing the final exit success yet.

## Batch 2 approval and final promotion - 2026-06-07

- User approved Batch 2 and requested starting Batch 3.
- Promoted approved Batch 2 candidates to final:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/04_페이지.png`
    - Source: `work_2026-06-06/batch_2/04_candidate_20260607_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/05_페이지.png`
    - Source: `work_2026-06-06/batch_2/05_candidate_20260607_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/06_페이지.png`
    - Source: `work_2026-06-06/batch_2/06_candidate_20260607_v1.png`

## Batch 3 generation - 2026-06-07

- Started Batch 3 in:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3`
- References inspected immediately before generation:
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/final/06_페이지.png`
- Generated page 7:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3/07_candidate_20260607_v1.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: review candidate. Tori's shell/body remain outside the near entrance while the head/neck peek inside. No child bag or strap is visible. Mari teacher stays low and calm; Banguli remains a soft water droplet inside the tunnel. Korean story text is readable and appears exact.
- Generated page 8:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3/08_candidate_20260607_v1.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: review candidate. Tunnel interior is warm, pretty, and safe with light from the opposite opening and shell details. Tori reads relieved rather than scared. Banguli remains a soft water droplet. Korean story text is readable and appears exact, with generator-style ellipsis punctuation.
- Generated page 9:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3/09_candidate_20260607_v1.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: review candidate. Tori is moving forward inside the tunnel with the shell entering and Banguli guiding ahead. This does not show the completed exit/success moment. No child bag or strap is visible. Korean story text is readable and appears exact.
- Current recommended Batch 3 review set:
  - `07_candidate_20260607_v1.png`
  - `08_candidate_20260607_v1.png`
  - `09_candidate_20260607_v1.png`
- Mobile review upload:
  - Created Google Slides deck directly after local PPTX import returned Drive `400 Bad Request`.
  - Google Slides: https://docs.google.com/presentation/d/1-xuP5WseuLPw1T8VgftRjoZos-4T5kQcWDkhggjXxic/edit?usp=drivesdk
  - Connector readback verified title, native Slides MIME type, and 3 slides.
  - Thumbnail verification returned all three slides as rendered landscape thumbnails (`1600 x 900`) with the portrait page images centered at full slide height.
- Status:
  - Do not promote Batch 3 to final and do not generate Batch 4 until user review/approval.

## User QA notes - Batch 3 - 2026-06-07

- Page 7:
  - `07_candidate_20260607_v1.png` needs regeneration.
  - Problem: Tori's body appears to pass through / penetrate the tunnel instead of staying outside while only the head peeks in.
  - Required: body, shell, legs, and feet must remain outside the entrance; only head/neck may enter slightly.
- Pages 8-9:
  - `08_candidate_20260607_v1.png` and `09_candidate_20260607_v1.png` need regeneration.
  - Problem: the tunnel interior is too wide and reads like a large tunnel/cavern.
  - Required: make the tunnel a low toddler crawl-through tube, narrow and child-scale, just big enough for Tori to crawl through safely.

## Batch 3 revision generation - 2026-06-07

- Regenerated page 7:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/work_2026-06-06/batch_3/07_candidate_20260607_v2.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: improved candidate. Tori's shell/body now read as outside the near entrance while the head/neck peek in. No child bag or strap is visible. Korean text remains readable.
- Regenerated page 8:
  - First narrower pass: `08_candidate_20260607_v2.png`
  - Stronger narrow-tube pass: `08_candidate_20260607_v3.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: `v3` is the preferred revision. The composition uses a near-entrance view and reads more like a small toddler crawl-through tube rather than a broad interior corridor. Korean text remains readable.
- Regenerated page 9:
  - First narrower pass: `09_candidate_20260607_v2.png`
  - Stronger narrow-tube pass: `09_candidate_20260607_v3.png`
  - Size: `1054 x 1492`, A5 portrait ratio pass.
  - QA: `v3` is the preferred revision. Tori is partly entering a low tube with the shell close to the tunnel scale, and the page does not show the exit/success moment. Korean text remains readable.
- Updated the existing Batch 3 Google Slides mobile review deck with the revised recommended set:
  - `07_candidate_20260607_v2.png`
  - `08_candidate_20260607_v3.png`
  - `09_candidate_20260607_v3.png`
- Mobile review deck:
  - https://docs.google.com/presentation/d/1-xuP5WseuLPw1T8VgftRjoZos-4T5kQcWDkhggjXxic/edit?usp=drivesdk
  - Connector readback verified the target deck and existing image object IDs.
  - Fresh thumbnail verification returned all three revised slides as rendered thumbnails (`1600 x 900`).
- Current recommended Batch 3 review set:
  - `07_candidate_20260607_v2.png`
  - `08_candidate_20260607_v3.png`
  - `09_candidate_20260607_v3.png`
- Status:
  - Await user review. Do not promote Batch 3 to final and do not generate Batch 4 until approval.
