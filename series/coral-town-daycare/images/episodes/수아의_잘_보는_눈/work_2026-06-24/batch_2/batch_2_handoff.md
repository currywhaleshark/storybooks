# Batch 2 Handoff - 수아의 잘 보는 눈 - 2026-06-25

## Source Paths

- Episode script: `series/coral-town-daycare/sua-different-is-good/script/main.md`
- Current page plan JSON: `series/coral-town-daycare/sua-different-is-good/script/pages.json`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24`
- Batch 1 folder: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/batch_1`
- Batch 2 folder: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/batch_2`

## Batch 1 Gate Status

Final-promoted files: none yet. The `final` folder has not been assembled in this pass.

Current batch-1 candidates:

| Page | File | Status |
| --- | --- | --- |
| 00 cover | `batch_1/00_candidate_text_v3.png` | current cover candidate; final QA/promotion still pending |
| 01 | `batch_1/01_candidate_text_v7.png` | user approved; continue from this version |
| 02 | `batch_1/02_candidate_text_v1.png` | user approved; continue from this version |
| 03 | `batch_1/03_candidate_text_v2.png` | user approved on 2026-06-25 with "음 좋아" |

Held, rejected, or superseded candidates:

- `batch_1/00_candidate_text_v1.png`, `batch_1/00_candidate_text_v2.png`: superseded by cover v3.
- `batch_1/01_candidate_text_v1.png` through `batch_1/01_candidate_text_v3.png`: superseded by later page-01 retries.
- `batch_1/01_candidate_text_v4.png`: held because Mongle's front limbs read as human-like hands, not tentacles.
- `batch_1/01_candidate_text_v5.png`: held because Lulu's small front hands/fins disappeared during the Mongle correction.
- `batch_1/01_candidate_text_v6.png`: held because Mongle again read as attached hands; this led to the page-01 cast strategy change.
- `batch_1/03_candidate_text_v1.png`: held because Lulu and Sua's eyes were too large relative to references, and Lulu's single subtle eyelash needed preservation.
- Rejected or non-approved Lulu wearing-hairpin references: do not use `reference_assets/lulu_wearing_special_coral_hairpin_ref_v1.png` as visual truth unless the user explicitly re-approves it.

## References To Preserve

Approved episode-specific references:

- Special loose hairpin: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/special_coral_hairpin_ref_v1.png`
- Approved Lulu wearing special hairpin: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`

Official character/location references likely needed for batch 2:

- Sua no-bag: `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- Lulu no-bag: `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
- Jun-i no-bag: `series/coral-town-daycare/references/characters/no_bag/준이_no_bag.png`
- Aru no-bag: `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- Mongle no-bag: `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`

## Carried-Forward Locks

- Always inspect or emit the actual reference images before generation. Do not generate from text-only descriptions.
- Keep A5 portrait proportion, soft low-saturation watercolor and colored-pencil toddler picture-book style, warm paper feel.
- Include exact Korean page text during the first generation pass. If the generated text is wrong, keep the candidate separate and run a text-panel correction pass.
- Keep text panels clean and readable; no pseudo-writing, random signs, labels, or extra text.
- No unrelated prior-episode contamination.
- No child-worn bags/straps unless the page explicitly calls for them. In these outdoor pages, prefer no-bag references.
- Sua must keep the official small black button eyes, long tube snout, slender purple seahorse body, dotted/spiny ridge, curled tail, and small fins.
- Lulu must keep the official pink seahorse silhouette and one subtle single eyelash stroke only on Lulu. Do not add eyelashes to Sua. Do not turn either into glossy anime-eyed characters.
- Page 03 eye lock carries forward: avoid large glossy eyes; keep eyes close to official small black button-eye proportions.
- The special hairpin visually remains the approved mint/aqua coral hairpin with cream star-shell and pale-yellow bead nubs. The script text says `분홍 산호 장식`; preserve the exact text, but do not visually recolor the approved prop unless the user asks.
- Continuity for batch 2: page 04 Lulu is still wearing the special hairpin; page 05 it falls and rolls into the sand; page 06 Lulu is missing it while Sua searches; page 07 Sua holds the found hairpin and Lulu has not put it back on yet.
- Mongle caution: when Mongle appears in batch 2, keep him spatially separated from Lulu and avoid paired touching/admiring gestures. His limbs must read as rounded octopus tentacles with suction cups, not hands or fingers.
- Aru caution: if Aru appears, preserve the official pufferfish body. No human hands, feet, shoes, or humanoid body. Keep Aru secondary if the page already has many characters.
- Banguli remains a pale sky-blue transparent droplet with a simple face and two or three small droplets nearby, not a plastic shiny object.

## Batch 2 Scope

Natural next batch range from `main.md`:

- 4페이지 — 마당으로 나가요
- 5페이지 — 앗, 루루의 산호 장식이!
- 6페이지 — 수아가 가만히 들여다봐요
- 7페이지 — 찾았다! 여기 있어!

The current `pages.json` only covers pages 0-3, so the first concrete next action is to extend `pages.json` or use `batch_2_prompt_plan.md` as the batch-local page plan for pages 04-07 before generating page 04.

## First Next Action

Start the next session by reading, in UTF-8:

1. `episode_worklog.md`
2. `batch_2/batch_2_handoff.md`
3. `batch_2/batch_2_prompt_plan.md`
4. `series/coral-town-daycare/sua-different-is-good/script/main.md` around pages 4-7

Then emit/inspect the page-04 references and generate `batch_2/04_candidate_text_v1.png` with the exact page text included.

## Session Update - Page 04 Candidate v1 - 2026-06-25

- Generated and saved `batch_2/04_candidate_text_v1.png`.
- References emitted before generation: playground/yard, no-bag Sua, approved Lulu wearing special hairpin, Banguli, no-bag Jun-i, no-bag Aru, and no-bag Mongle.
- Assistant QA: candidate appears to preserve page 04 continuity. Lulu is still wearing the approved special hairpin; no loose/lost hairpin appears; Sua quietly collects shells with Banguli nearby; no obvious child-worn bags or straps are visible; Mongle stays secondary with octopus tentacles and beret.
- Note: Aru is not visibly included despite being in the optional/secondary reference set. This may be acceptable because page 04 only needs lively friends in the yard, but ask user QA before treating it as accepted.
- Current gate: user QA needed for exact Korean text, Lulu hairpin fidelity, Sua eye/body fidelity, and Aru absence.
- Next action if user approves page 04: generate `batch_2/05_candidate_text_v1.png`, with the loose/falling special hairpin as the single visible prop and Lulu no longer wearing it after the fall.

## Session Update - Page 04 Candidate v3 - 2026-06-25

- Current page 04 candidate is now `batch_2/04_candidate_text_v3.png`.
- Hold `batch_2/04_candidate_text_v1.png`: Lulu clothing color drifted from official reference and Lulu needed her subtle reference eyelash.
- Hold `batch_2/04_candidate_text_v2.png`: Lulu corrections improved, but Jun-i was too small.
- Assistant QA on v3: Lulu's clothing is back to cream/rose-pink, Lulu-only eyelash is present, approved special hairpin remains on Lulu only, Jun-i is larger and reads as a proper playmate, no loose/lost hairpin appears, and the Korean text remains readable.
- Current gate: user QA for `04_candidate_text_v3.png`.
- Next action if user approves page 04: generate `batch_2/05_candidate_text_v1.png`, with the loose/falling special hairpin as the single visible prop and Lulu no longer wearing it after the fall.

## Session Update - Page 05 Candidate v3 - 2026-06-25

- Page 04: `batch_2/04_candidate_text_v3.png` is user approved for continuing.
- Current page 05 candidate is `batch_2/05_candidate_text_v3.png`.
- Hold `batch_2/05_candidate_text_v1.png`: hairpin was too obvious in front of the children, weakening the "could not find it" story logic.
- Hold `batch_2/05_candidate_text_v2.png`: hairpin placement improved, but `톡!` drifted to `록!`.
- Assistant QA on v3: hairpin is only slightly visible in the lower-right coral/tunnel corner, exactly one hairpin appears, Lulu is not wearing it, and text now reads `톡!`.
- Current gate: user QA for `05_candidate_text_v3.png`.
- Next action if user approves page 05: generate `batch_2/06_candidate_text_v1.png`, with Lulu still missing the hairpin and Sua quietly examining the sand gaps without revealing the find too early.
## Session Update - Page 06 Candidate v1 - 2026-06-25

- Page 05: `batch_2/05_candidate_text_v3.png` is user approved for continuing.
- Current page 06 candidate is `batch_2/06_candidate_text_v1.png`.
- References emitted before generation: playground/yard, no-bag Sua, Banguli, Lulu no-bag without special hairpin, optional no-bag Jun-i, and optional no-bag Mongle.
- Assistant QA on v1: Sua is the quiet visual center, lowered close to the sand with small focused eyes and only a subtle sparkle; Banguli looks beside her; Lulu watches from the background without the special hairpin; no found hairpin is revealed early; the Korean text appears exact and readable.
- Current gate: user QA for `06_candidate_text_v1.png`.
- Next action if user approves page 06: generate `batch_2/07_candidate_text_v1.png`, with Sua carefully lifting the found hairpin while Lulu still does not wear it yet.

## Session Update - Page 07 Candidate v2 - 2026-06-25

- Page 06: `batch_2/06_candidate_text_v1.png` is user approved for continuing.
- Current page 07 candidate is `batch_2/07_candidate_text_v2.png`.
- Hold `batch_2/07_candidate_text_v1.png`: illustration was strong, but `루루의 얼굴이 환해졌어요.` rendered like `루루의 얼굴이 화해졌어요.`.
- v2 was made by a local text-panel patch from v1, correcting only the `루루의 얼굴이 / 환해졌어요.` area and preserving the reveal illustration.
- Assistant QA on v2: Sua holds exactly one approved mint/aqua special hairpin; Lulu is not wearing it yet; Banguli and Jun-i react happily; the text panel now reads the intended line correctly.
- Current gate: user QA for `07_candidate_text_v2.png`.
- Next action if user approves page 07: continue to page 08, where Lulu asks how Sua found such a small thing and Sua begins to name her small-eye strength.

## Session Update - Page 07 Candidate v4 - 2026-06-25

- User QA held `batch_2/07_candidate_text_v2.png` because Sua and the coral ornament were too large.
- User also noted Lulu's missing eyelash during the retry discussion, then requested fresh generation rather than local patching: "그냥 생성을 하쇼".
- Current page 07 review candidate is now `batch_2/07_candidate_text_v4.png`, generated fresh and saved without local text or eyelash patching.
- Assistant QA on v4: Sua is less dominant and closer to peer scale; the hairpin is smaller and more hairpin-like; Lulu's head is still bare and has a subtle single eyelash; Banguli and Jun-i react happily; the text appears readable with `루루의 얼굴이 환해졌어요.`.
- Held/superseded: `07_candidate_text_v1.png` text typo, `07_candidate_text_v2.png` oversized Sua/hairpin, and v3 patch/intermediate files after the fresh-generation request.
- Current gate: user QA for `07_candidate_text_v4.png`.
- Next action if user approves page 07: continue to page 08, where Lulu asks how Sua found such a small thing and Sua begins to name her small-eye strength.

## User Approval - Page 07 Candidate v4 - 2026-06-25

- User accepted moving on from `batch_2/07_candidate_text_v4.png` with feedback: "오케이 다음으로".
- Batch 2 can be treated as complete for continuation purposes: page 04 v3, page 05 v3, page 06 v1, and page 07 v4 are approved for moving forward.
- Page 08 work has started in `../batch_3/`.

## Final QA Correction - Page 05 Candidate v4 - 2026-06-26

- Final QA found a story-logic issue in `batch_2/05_candidate_text_v3.png`: the special coral hairpin still read as being inside the lower-right cave/tunnel, while page 06 and page 07 establish the find as coming from a sand gap.
- Created `batch_2/05_candidate_text_v4.png` by editing only the lower-right cave/sand area.
- QA result for v4:
  - The cave/tunnel no longer contains the readable special hairpin.
  - A tiny, mostly buried hint of the mint/aqua coral hairpin remains outside the cave in the nearby sand gap.
  - The clue is subtle enough for the friends to miss, but it now supports the page 06 sand-gap search and page 07 reveal.
  - The Korean story text, page composition, and characters remain visually consistent.
- Current page 05 review/final-QA candidate: `batch_2/05_candidate_text_v4.png`.
- Superseded for final assembly: `batch_2/05_candidate_text_v3.png`.

## 2026-06-26 15:48:14 - Final text corrections
- Page 05 final now uses 05_candidate_text_v5_textfix_generated.png (산호 장식이).
- Page 07 final now uses 07_candidate_text_v5_textfix_generated.png (루루의 산호 장식).
