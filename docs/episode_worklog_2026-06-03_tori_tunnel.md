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
