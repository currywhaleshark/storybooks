# Episode Worklog - 밤에 빛나는 길

## Intake

- Episode: `밤에 빛나는 길`
- Series: `심해탐정 셜록 핀`
- Work date: `2026-07-12`
- Supplied script: `C:\Users\yurib\.codex\codex-remote-attachments\019f54d3-16c8-7753-a697-ab7ec667c864\44F81AFC-C407-4078-9B66-37EF102B139B\1-밤에_빛나는_길_수정본.md`
- Supplied script SHA-256: `39C530F1018D7234B947077BB4B48C0100BF9AEACC268BC712CD8EC6EA83349F`
- Imported script: `series/sherlock-fin-deep-city/docs/episodes/밤에_빛나는_길.md`
- Episode work root: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/work_2026-07-12`
- Final target: `series/sherlock-fin-deep-city/images/episodes/밤에_빛나는_길/final`
- Planned pages: `12` (`00_표지.png`, `01_페이지.png` through `11_페이지.png`)

## Official Rules

- `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_이미지_생성_디자인_규칙서.md`
- `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_사건생성_규칙서.md`
- `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## Approved Existing References

### Characters

- `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- `series/sherlock-fin-deep-city/references/characters/펄리.png`
- `series/sherlock-fin-deep-city/references/characters/팝팝.png`
- `series/sherlock-fin-deep-city/references/characters/모모.png`
- `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
- `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`

### Backgrounds and Layout

- `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

## Coverage Audit

- PASS: Sherlock Fin, Pearly, Pop Pop, Momo, and Crabson have official character sheets.
- PASS: Deep City coral alley visual language is covered by the official Deep City sheet.
- PASS: Detective office and text-panel conventions have official references.
- PASS: official grandfather reference is user-approved v5 with squint eyes, unmistakable elderly male face, and paired nose-to-mouth nasolabial folds.
- PASS: locked official visual reference for the recurring golden plankton trail and readable green moss flakes.
- NOT REQUIRED NOW: a new location sheet. The script uses the established generic coral alley; create an episode-specific alley sheet only if continuity drifts during story-page generation.

## Batch Status

### Reference Setup

- Status: `reference gate complete; Batch 1 planning in progress`
- Prompt plan: `reference_setup/reference_setup_prompt_plan.md`
- Superseded candidate 1: `reference_setup/긴다리거미게_할아버지_reference_candidate_v1.png`
  - Status: `HOLD / do not use`; large round sparkling eyes read too young.
  - SHA-256: `D7CD718986461B1BD229638B06C4BC648D07AE8718B1B3B2F02EDF0D4A18A802`
  - Size: `1448 x 1086 PNG`
- Superseded grandfather candidate: `reference_setup/긴다리거미게_할아버지_reference_candidate_v2_squint.png`
  - Status: `HOLD / historical edit base`; approved squint direction but incomplete elderly lower face.
  - SHA-256: `5D691548CBD147BD4B2D50D36099C682D77BA346E824F8EB9975E9A59DC48256`
  - Size: `1448 x 1086 PNG`
- Rejected grandfather candidate: `reference_setup/긴다리거미게_할아버지_reference_candidate_v3_squint_smile_lines.png`
  - Status: `FAIL / do not use`; user reports it looks the same as v2 because the wrinkles disappear at normal viewing size.
  - SHA-256: `CA5086E2E86342C772AEF6382CDCF20B29CC66A5F72E3A5C402DC513AF573A6D`
  - Size: `1448 x 1086 PNG`
- Current grandfather candidate: `reference_setup/긴다리거미게_할아버지_reference_candidate_v4_squint_clear_mouth_wrinkles.png`
  - Status: `FAIL / do not use`; wrinkles are visible but are the wrong type and location—outer mouth smile lines rather than nasolabial folds.
  - SHA-256: `05905844C44F29E1CB1E5F0164BCDF899AF361B42E9FE20D5E82CBE644914499`
  - Size: `1448 x 1086 PNG`
- Selected grandfather candidate: `reference_setup/긴다리거미게_할아버지_reference_candidate_v5_squint_elderly_nasolabial_folds.png`
  - Status: `USER APPROVED / active official reference`
  - SHA-256: `5FC6E1CD49CD034662031DAC58B660DA97E4622789608D1FA9A84583B31FA274`
  - Size: `1448 x 1086 PNG`
- Selected candidate 2: `reference_setup/금빛플랑크톤길_이끼가루_reference_candidate_v1.png`
  - SHA-256: `58EDFF42A4451276F4412E462C47CB277382C9248D02031965E6D0563816659A`
  - Size: `1448 x 1086 PNG`
- Official output 1: `series/sherlock-fin-deep-city/references/characters/밤에_빛나는_길_긴다리거미게_할아버지_레퍼런스.png`
- Official output 2: `series/sherlock-fin-deep-city/references/props/밤에_빛나는_길_금빛플랑크톤길_이끼가루_레퍼런스.png`
- Integrity: the active grandfather official copy matches selected v5 SHA-256 `5FC6E1CD49CD034662031DAC58B660DA97E4622789608D1FA9A84583B31FA274`; the official golden-trail copy matches its selected v1.
- Gate: `COMPLETE`; user approved v5 and asked to continue production.

### Story Pages

- Batch 1 (`00`-`03`): `COMPLETE / USER APPROVED / 00-03 FINAL`
  - Prompt plan: `batch_1/batch_1_prompt_plan.md`
  - Format: A5 portrait `148:210`; production target `1054 x 1492`.
  - Candidate lineage: preserve all built-in originals with `_raw.png`; revise only the smallest user-identified page unit.
  - `00_candidate_text_v1.png`: HOLD / edit base; remove the extra inner scalloped shell layer that reads as a hat, but retain Pearly's official monocle and chain.
  - `00_candidate_text_v2_pearly_hat_removed.png`: **USER FAIL / do not use**; Pearly's head became flattened. `1054 x 1492`; SHA-256 `C353A53B6FFD4AD4774665ACB755C17E0DF341BA93ADA4B530B1A8079640EA06`.
  - `00_candidate_text_v3_full_regen_round_head.png`: **USER APPROVED / FINAL**; official-reference-only full regeneration; `1054 x 1492`; SHA-256 `BFA97BA68E97FCA22D7D4033DA6E0F17A54D253691684414B67DD2FDB0F46330`.
  - Final: `final/00_표지.png`; candidate-to-final SHA-256 equality verified.
  - `01_candidate_text_v1.png`: HOLD / edit base; correct the 90-degree upper/lower shell yaw mismatch while retaining the natural open angle, official monocle, chain, and exact text.
  - `01_candidate_text_v2_shell_axis_fixed.png`: **USER FAIL / do not use**; Pearly's head became flattened. `1054 x 1492`; SHA-256 `62AC8674BC707D94C084E1C05FCA745AF3CF6DB49520B6A1E4C52B0412ECEEB9`.
  - `01_candidate_text_v3_full_regen_round_head_shell_axis.png`: **USER FAIL / do not use**; Pearly's torso and both arms disappeared, leaving only the head above the shell. `1054 x 1492`; SHA-256 `A0529C24EA19ADE8742123C0AC77B4A9C0729C23973AC3B1A9092C135D80F42C`.
  - `01_candidate_text_v4_full_regen_round_head_two_arms_shell_axis.png`: **USER APPROVED / FINAL**; visible torso, exactly two connected arms and two hands, round head, monocle, coherent shell, and exact text; `1054 x 1492`; SHA-256 `30F045CCCAAA6A57B4D056E55F9EE30C0AB265C79695E23879ADBC4D709F58D4`.
  - Final: `final/01_페이지.png`; candidate-to-final SHA-256 equality verified.
  - `02_candidate_text_v1.png`: **USER APPROVED / locked**; `1054 x 1492`; SHA-256 `513458E251A2680FA19FC9E551155AD005BEAB7225E434CDCA48456A93694E11`.
  - Final: `final/02_페이지.png`; candidate-to-final SHA-256 equality verified.
  - `03_candidate_text_v1_raw.png`: illustration PASS and user-confirmed text PASS; the original has read `셜록` correctly from the start. Selected.
  - `03_candidate_text_v1.png`: **USER APPROVED / locked**; `1054 x 1492`; SHA-256 `E08FA2368C12F6BCB95E64193FC61287AFE7B35CC65B3D4B78FA01C23AC4BD4E`.
  - Final: `final/03_페이지.png`; candidate-to-final SHA-256 equality verified.
  - `03_candidate_text_v2_text_repair_raw.png`: unnecessary repair generated after an internal glyph misread; HOLD / do not use.
  - `03_candidate_text_v3_single_glyph_repair_raw.png`: canceled; never generated.
- Batch 2 (`04`-`07`): `COMPLETE / USER APPROVED / 04-07 FINAL`
  - Prompt plan: `batch_2/batch_2_prompt_plan.md`
  - Format: A5 portrait `148:210`; production target `1054 x 1492`.
  - Candidate targets: `04_candidate_text_v1.png` through `07_candidate_text_v1.png`; preserve built-in originals with `_raw.png`.
  - `04_candidate_text_v1.png`: **USER APPROVED / FINAL**; `1054 x 1492`; SHA-256 `C77846E8DD401585AAF75AB5CD5486A7FEB592E2CDDD7BFF461277B41EBEAB75`; final `final/04_페이지.png` verified equal.
  - `05_candidate_text_v1.png`: **USER APPROVED / FINAL**; `1054 x 1492`; SHA-256 `5BB242D6A62A07418C80B089F4E5CBE3222BCDCF1A5B1FAC9B2022ED6925E9DD`; final `final/05_페이지.png` verified equal.
  - `06_candidate_text_v1.png`: **USER APPROVED / FINAL**; `1054 x 1492`; SHA-256 `C524C9707B930E6EEE059ED0382C6A2F967C5779B8EF4679E554DF0F2FE521CE`; final `final/06_페이지.png` verified equal.
  - `07_candidate_text_v1.png`: **USER APPROVED / FINAL**; `1054 x 1492`; SHA-256 `28C9FA4A66C787A60E470308CF21A39142111F09C36F43EC1A2892C87A8C8B78`; final `final/07_페이지.png` verified equal.
- Batch 3 (`08`-`11`): `waiting for user reference approval and deduction/reveal continuity`

## Episode Locks

- The golden trail stays low on the alley floor and follows a smooth winding route.
- It is made from many tiny warm-gold plankton lights, not a painted solid stripe, liquid, stars, or floating ribbon.
- In close views, soft green moss flakes must be visibly distinct among the gold lights.
- The grandfather alone drops the moss flakes; friends do not create separate glowing trails.
- Before page `08`, the grandfather must not be clearly revealed; the cover shows only a tiny distant long-legged silhouette.
- The grandfather has very long thin legs, a gentle rounded carapace with soft green moss, round glasses, a small cane, and a plaid scarf.
- The grandfather's default eye shape is a soft narrow crescent squint behind the round glasses, giving him an elderly, warm, unhurried presence rather than a baby-like large sparkling gaze.
- His warm “허허” laugh uses fully closed smiling eyes. Only the page `09` surprise beat may open his eyes slightly, and even there the irises remain modest and less round/sparkling than v1.
- White eyebrows and a small mouth carry most of his readable emotion; do not enlarge the eyes to communicate expression.
- The face must read unmistakably as an elderly male grandfather, not a baby-faced cute character with decorative smile marks.
- Add one continuous nasolabial fold on each side: each line begins beside the small nose directly under the inner lower edge of the glasses, then curves down and outward across the cheek to finish beside the corresponding mouth corner. Together the pair forms clear bracket-like/팔자-shaped folds around the lower central face.
- Nasolabial folds remain visible at thumbnail scale and in every applicable face view. Add only mild softened lower-cheek volume to support the old-man read; no isolated outer-mouth smile dashes, beard, moustache, extreme jowls, or disturbing realism.
- Keep four principal legs clearly readable; overlap/simplify remaining legs behind the body to reduce anatomy drift.
- Distinguish the grandfather from Crabson: no red body, no top hat, no tuxedo, no saxophone.
- Night scenes remain cozy and child-safe, with warm windows, bubble lamps, and golden light preventing a dark or frightening mood.
- All page text must be rendered verbatim from the imported script and checked against it after generation.
- Pearly's gold eye piece is the planned official monocle. Always retain its lens, rim, and chain; never interpret it as an unwanted hat or accessory error.
- Pearly's upper and lower shell valves may open around their hinge, but must never be yawed/twisted into different directions. They share one hinge axis and matching radial geometry.
- Pearly's baby head must remain a tall, fully rounded pearl/egg shape with a high smooth dome, full forehead and back of skull, and round cheeks. Never flatten, compress, crop, or replace the head silhouette with shell geometry.
- Pearly must never render as a floating head. Preserve her small torso, two shoulder-connected short arms, and two distinct hands above the lower shell rim.

## QA Log

- `2026-07-12`: script intake complete; 12-page structure confirmed.
- `2026-07-12`: existing reference audit complete; two missing visual references identified.
- `2026-07-12`: no prior work or same-title episode folder found; clean new-episode setup.
- `2026-07-12`: unrelated dirty worktree changes under `두_갈래_발자국` noted and left untouched.
- `2026-07-12`: grandfather candidate v1 generated and visually inspected. PASS: clear new identity, kind elder expression, stable triangular brown carapace, rear moss placement, round glasses, plaid scarf, cane, long legs, and no Crabson contamination. The two lighter inner legs in the front views function as overlapped secondary legs and preserve four dominant readable supports.
- `2026-07-12`: golden-trail candidate v1 generated and visually inspected. PASS WITH LOCK: winding granular gold trail stays on the floor; green moss pieces remain clearly distinct; bottom sequence communicates fall -> gather -> glow without text or arrows. In wide story pages, scale the green pieces down from the macro reference so they read as flakes rather than large seaweed tiles; retain the larger readable fragments only inside page `06` magnification and page `10` mechanism close-up.
- `2026-07-12`: both selected candidates copied non-destructively to official references folders; PNG dimensions and candidate-to-official SHA-256 equality verified.
- `2026-07-12`: user QA promoted to an explicit lock: v1's large round sparkling eyes read too baby-like for a grandfather. Revise only the eye language to default crescent squints, closed laughing eyes, and modestly opened surprise eyes while preserving all other design features.
- `2026-07-12`: grandfather candidate v2 squint generated with the built-in image editor and visually inspected. PASS: default full-body views use lively warm crescent squints; gentle, laughing, and thoughtful portraits remain distinct through brows and mouth; only the surprise portrait opens its eyes modestly. Shell, moss, glasses, scarf, cane, long-leg anatomy, palette, sheet layout, and detail panels remain stable with no unrelated contamination.
- `2026-07-12`: v1 retained as `HOLD / do not use`. Selected v2 copied to the active official grandfather reference; candidate-to-official dimensions (`1448 x 1086`) and SHA-256 equality verified.
- `2026-07-12`: user requested one more age cue: subtle mouth-corner wrinkles. Promote as a minimal face-only revision while preserving the approved squint-eye language and every body, prop, palette, and layout invariant.
- `2026-07-12`: grandfather candidate v3 generated with the built-in image editor and visually inspected. PASS: short soft mouth-corner creases add a clearer grandfather cue without deep folds, sagging, sadness, or realistic aged skin. Creases are stronger in smile/laugh portraits and lighter in surprise/thoughtful views. Approved squints, white eyebrows, shell, moss, glasses, scarf, cane, legs, palette, sheet layout, and detail panels remain stable with no unrelated contamination.
- `2026-07-12`: v2 retained as `HOLD / edit base`. Selected v3 copied to the active official reference; candidate-to-official dimensions (`1448 x 1086`) and SHA-256 equality verified.
- `2026-07-12`: user visual QA overrides local v3 QA: FAIL. The v3 mouth lines are too faint and short to distinguish from v2 at normal viewing size. Mark v3 `do not use`; return to the user-approved v2 squint image as the clean edit target.
- `2026-07-12`: v4 lock: two clearly separated medium-length curved mouth-corner wrinkles per visible side plus one short lower auxiliary crease; visible at thumbnail scale and still warm, never sad or realistically aged.
- `2026-07-12`: grandfather candidate v4 generated from preserved v2, not rejected v3. LOCAL QA PASS: the difference is obvious at conversation-preview size; multiple separated curved mouth wrinkles are visible in full-body and portrait views; squints, glasses, eyebrows, mouth expressions, shell, moss, scarf, cane, legs, palette, layout, and detail panels remain stable. No sadness, deep folds, facial hair, text, or contamination.
- `2026-07-12`: rejected v3 removed from the active official path. Official grandfather reference restored to v2 while v4 waits for explicit user visual approval; no unapproved candidate was promoted.
- `2026-07-12`: user rejects v4 conceptually: visible lines are still the wrong wrinkle type. Required feature is a true paired nasolabial fold running from beside the nose to the mouth corners, with the prompt explicitly stating an elderly male/old-man/grandfather face.
- `2026-07-12`: mark v4 `FAIL / do not use`; return again to the clean user-approved v2 squint base for v5. Do not use v3 or v4 as image inputs.
- `2026-07-12`: grandfather candidate v5 generated from v2 with the prompt explicitly defining an elderly male old-man/grandfather face. LOCAL QA PASS: a continuous fold on each side begins beside the nose under the glasses, curves through the cheek, and ends at the mouth corner; the paired folds remain visible in full-body and portrait views and are not isolated outer-mouth dashes. Mild lower-cheek heaviness strengthens the old-man read without frailty. Squints, glasses, eyebrows, shell, moss, scarf, cane, legs, palette, layout, and detail panels remain stable with no text or contamination.
- `2026-07-12`: v5 retained as a separate candidate; active official grandfather path remains byte-identical to v2 until explicit user visual approval.
- `2026-07-12`: user approved v5 (“오 이제 됐다”) and instructed registration plus continued production. V5 copied to the active official grandfather reference; candidate-to-official dimensions (`1448 x 1086`) and SHA-256 equality verified. Reference gate complete.
- `2026-07-12`: user corrected the page `03` internal QA reading: there was no typo in the original. Candidate 1 has rendered `셜록` correctly from the start and is restored as the selected page. The unnecessary v2 edit is `HOLD / do not use`; v3 single-glyph repair was canceled and never generated.
- `2026-07-12`: Batch 1 selected candidates `00`-`03` saved at `1054 x 1492`. Pages `00`, `02`, and `03` are byte-identical copies of their raw generations. Page `01` was normalized mechanically by cropping the outermost right column and duplicating the bottom edge row; no content was stretched and the raw file remains preserved.
- `2026-07-12`: Batch 1 local QA complete. Exact Korean script text, title, character identity, `01`/`02` alley continuity, night/day contrast, page `02` present-time trail absence, page `03` office scene, safe layout, and contamination checks pass. Files remain outside `final/` pending user page approval.
- `2026-07-12`: user QA approves pages `02` and `03`. Page `00` requires removal of an unnecessary hat-like extra shell layer on Pearly; page `01` requires correction of the upper/lower shell's 90-degree direction mismatch. User clarifies that the gold object beside Pearly's eye is her planned monocle, so its lens and chain are explicit keep-locks.
- `2026-07-12`: approved pages `02` and `03` copied to `final/02_페이지.png` and `final/03_페이지.png`; both candidate-to-final SHA-256 values match.
- `2026-07-12`: generated page `00` v2 from the normalized v1 cover plus the official Pearly sheet. LOCAL QA PASS: removed the extra inner scalloped hat-like shell layer while retaining one rear upper valve, lower shell, monocle, chain, bow tie, face, pose, exact title, Sherlock, trail, and silhouette.
- `2026-07-12`: generated page `01` v2 from the normalized v1 page plus the official Pearly sheet. LOCAL QA PASS: both shell valves now share one rear hinge and radial axis without losing the natural open angle; monocle, chain, bow tie, face, pose, exact Korean text, room, window, and trail remain correct.
- `2026-07-12`: user QA overrides both v2 local judgments: Pearly's head became visibly flat in both pages. Mark both v2 candidates `FAIL / do not use`. Full regeneration is required for pages `00` and `01`; do not use any v1/v2 page candidate as a visual input.
- `2026-07-12`: v3 regeneration lock: use original official references only; prioritize Pearly's high, fully rounded pearl/egg-shaped head, full forehead and rear skull, round cheeks, official monocle and chain, no hat-like extra shell, and coherent shared shell hinge/axis.
- `2026-07-12`: cover `00` v3 generated from official references only. LOCAL QA PASS: Pearly's high rounded head, monocle, no hat-like extra shell, exact title, Sherlock, trail, and silhouette pass; waiting for user QA.
- `2026-07-12`: page `01` v3 generated from official references only, then USER FAIL: Pearly's head and shell improved but her torso and both arms disappeared. Mark v3 `do not use`; do not use it as a v4 input.
- `2026-07-12`: page `01` v4 lock: full regeneration from official references only; show a visible small torso plus exactly two shoulder-connected arms and two separate hands resting above the lower shell rim, while preserving the round head, monocle, coherent shell axis, and exact text.
- `2026-07-12`: page `01` v4 generated from official references only. LOCAL QA PASS: visible torso, two shoulder-connected arms, two distinct hands above the shell rim, high rounded head, official monocle/chain, centered bow tie, coherent shell hinge/axis, exact Korean text, room, window, and trail all pass.
- `2026-07-13`: user approved cover `00` v3 and page `01` v4 (“좋아 다음 준비하자”). Both copied to `final/00_표지.png` and `final/01_페이지.png`; candidate-to-final SHA-256 equality and `1054 x 1492` dimensions verified. Batch 1 is complete with final pages `00`-`03`.
- `2026-07-13`: Batch 2 prompt plan created for pages `04`-`07`. Locks: position/time/material/deduction clue order, no grandfather reveal, exact script text, official Sherlock/Pearly identity, Pearly round-head/two-arm/monocle/shell anatomy, floor-hugging granular trail, and approved page `01`/`02` alley continuity where applicable.
- `2026-07-13`: Batch 2 pages `04`-`07` generated one page per built-in call from listed official/approved references. All raw outputs were already `1054 x 1492`; byte-identical review candidates saved alongside them.
- `2026-07-13`: Batch 2 local QA complete. PASS: exact Korean text on all four pages; official character identity and complete Pearly anatomy; page `04` floor position/direction clue; page `05` separate night/morning timing bubbles with empty morning; page `06` faceless gold plankton versus distinct green moss; page `07` exactly three clue visuals and no grandfather/silhouette; no contamination or watermark.
- `2026-07-13`: user approved Batch 2 (“좋아 여기까지 정하고”). Pages `04`-`07` copied to stable final filenames; candidate-to-final SHA-256 equality and `1054 x 1492` dimensions verified. Final folder now contains approved pages `00`-`07`.

## Next Step

Checkpoint complete through page `07`. Preserve final pages `00`-`07`. Batch 3 (`08`-`11`) remains ungenerated and will begin only when the user resumes production.
