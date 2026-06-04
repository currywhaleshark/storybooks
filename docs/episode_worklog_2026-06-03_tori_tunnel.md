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
