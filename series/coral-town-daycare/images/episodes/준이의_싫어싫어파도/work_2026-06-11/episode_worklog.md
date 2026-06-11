# Episode Worklog - 준이의 싫어싫어파도

## Source

- Full prompt/script: `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11`
- Final folder: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/final`

## Reference Audit

- Official references to use:
  - `series/coral-town-daycare/references/배경_전경과_놀이터.png`
  - `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
  - `series/coral-town-daycare/references/배경_교실.png`
  - `series/coral-town-daycare/references/characters/마리_선생님.png`
  - `series/coral-town-daycare/references/characters/준이.png`
  - `series/coral-town-daycare/references/characters/방울이.png`
  - `series/coral-town-daycare/references/characters/토리.png`
  - `series/coral-town-daycare/references/characters/몽글이.png`
  - `series/coral-town-daycare/references/characters/루루.png`
  - `series/coral-town-daycare/references/characters/아루.png`
  - `series/coral-town-daycare/references/characters/포포.png`
  - `series/coral-town-daycare/references/characters/수아.png`
- Episode-specific references:
  - `reference_assets/shell_hourglass_ref.png`
  - `reference_assets/reference_asset_plan.md`

## User QA Locks

- Rewrite the old prompt document into the new Sanho Village Daycare design format.
- Page 03 must not reveal "밖에 더 있고 싶어" yet. Jun-i should only protest that he does not want to go in.
- Page 05 is where Mari teacher helps Jun-i find the words for his underlying feeling; Jun-i himself first says "밖에... 더 있고 싶어."
- Page 06 follows because Jun-i has said what he wants; Mari teacher can then offer the shell-hourglass timed alternative.
- Pages 01-08 are all arrival-time exterior/entrance continuity, so Jun-i keeps his blue bag on.
- Page 09 is inside after arrival; bags are stored and not worn.
- The shell hourglass needs its own reference because it drifted in earlier attempts.

## Batch Status

- Script converted to new-format prompt document:
  - `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- Shell hourglass reference generated and accepted for continuity use:
  - `work_2026-06-11/reference_assets/shell_hourglass_ref.png`
- Page plan prepared:
  - `work_2026-06-11/page_plan.md`
- Batch 1 prepared:
  - `work_2026-06-11/batch_1/batch_1_prompt_plan.md`
- Batch 1 scope:
  - `00_표지.png` through `03_페이지.png`
- Cover prompt added:
  - Cover focuses on Jun-i, Mari teacher, and Banguli rather than the full cast, because page 01 attempts showed that crowded scenes are currently weakening reference fidelity.
- Batch 1 page 01 generated:
  - `work_2026-06-11/batch_1/01_candidate_text_v1.png`
- Page 01 QA note:
  - Candidate is suitable for mobile review. Exact Korean text appears correct, Jun-i reads as pouty rather than scary, and the blue arrival bag is present. Small caution: Mari teacher's tiny name tag may not read perfectly at mobile size, so user visual QA should check whether that matters.
- Google Drive mobile review doc:
  - `https://docs.google.com/document/d/1jqoTmAZaAr65DKcAunsMTJ_TL_wWVxQPkeNgUupnT-I/edit?usp=drivesdk`
- User mobile QA update:
  - `01_candidate_text_v1.png` is on hold / rejected for reference fidelity.
  - Jun-i became too round, and his eyes changed away from the official small black button-eye look.
  - Supporting characters drifted; Lulu's official details were especially reduced.
  - Next attempt must preserve exact official silhouettes and details over added cuteness.
- Page 01 regeneration:
  - `work_2026-06-11/batch_1/01_candidate_text_v2.png`
  - `work_2026-06-11/batch_1/01_candidate_text_v3.png`
- Page 01 v2/v3 QA note:
  - v2 improves Jun-i's button eyes and Lulu detail, but Jun-i remains slightly too round.
  - v3 is the best current candidate for mobile review. Jun-i reads closer to the official side-view shark silhouette, keeps small button eyes, and Lulu keeps more visible snout/ridge/tail detail.
  - Google Drive mobile review doc now includes v1 and v3 for comparison.

## Batch 1 Restart - 2026-06-11

- User requested batch 1 re-prep because the prior session ignored too many official references.
- Existing page 01 candidates are now process history only:
  - `work_2026-06-11/batch_1/01_candidate_text_v1.png`: hold/reject. Jun-i too round, eyes changed, supporting character fidelity weak.
  - `work_2026-06-11/batch_1/01_candidate_text_v2.png`: hold/reject. Improvement attempt only.
  - `work_2026-06-11/batch_1/01_candidate_text_v3.png`: hold. Best first-pass comparison image but not accepted as restart visual truth.
- Rewritten restart plan:
  - `work_2026-06-11/batch_1/batch_1_prompt_plan.md`
- Restart output targets:
  - `00_cover_candidate_restart_v1.png`
  - `01_candidate_text_restart_v1.png`
  - `02_candidate_text_restart_v1.png`
  - `03_candidate_text_restart_v1.png`
- Restart locks promoted to hard requirements:
  - Generate and QA one page at a time.
  - Do not use prior generated candidates as visual references.
  - Attach every visible character's individual official reference image.
  - Jun-i must preserve the official projecting shark snout, small black oval button eyes, white belly/lower face, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
  - Lulu must preserve the official long tube snout, spiny dotted head ridge, coral/shell ornament, translucent fin, curled tail, and sailor outfit when visible.
  - Page 03 must not reveal or imply "밖에 더 있고 싶어."

## Batch 1 Cover Restart Candidates

- Generated:
  - `work_2026-06-11/batch_1/00_cover_candidate_restart_v1.png`
  - `work_2026-06-11/batch_1/00_cover_candidate_restart_v2.png`
  - `work_2026-06-11/batch_1/00_cover_candidate_restart_v3.png`
- Cover v1 QA:
  - Hold/reject for restart standards.
  - Title text is mostly readable, but Jun-i is still too compressed and round compared with the official shark reference.
  - Jun-i's eye gained a slightly stylized sad/eyelash feeling, which conflicts with the small black oval button-eye lock.
- Cover v2 QA:
  - Current best cover candidate for user review.
  - Korean title/subtitle are readable and appear correct.
  - Jun-i keeps the blue arrival bag, white lower face/belly, gill marks, dorsal fin, side fin, long tail, and small black oval eye more clearly than v1.
  - Mari teacher keeps the yellow apron, star hairpin, purple notebook, and purple mermaid tail; Banguli remains a droplet.
  - Background follows the official daycare exterior/playground with blue door and coral tunnel.
  - Remaining caution: Jun-i is still a little rounder than the official character sheet, so user visual approval is needed before promoting to final.
- Cover v3 QA:
  - Current best cover candidate after user noted v2 still looked rounder than the official Jun-i reference.
  - Korean title/subtitle remain readable and appear correct.
  - Jun-i's snout, head length, dorsal fin, tail, gill marks, white lower face/belly, blue arrival bag, and small black oval eye are closer to the official sheet than v2.
  - Mari teacher and Banguli remain on-reference enough for cover review.
  - Remaining caution: Jun-i is still slightly softened for picture-book style, but v3 is less compressed and less whale-like than v2.
- User decision:
  - Cover is good enough to move on with `00_cover_candidate_restart_v3.png` as the current cover candidate.

## Script Revision - Page 05/06 Emotional Logic

- User requested page 05 revision:
  - Jun-i should still only be able to say "그냥 싫어" at first.
  - Mari teacher should not simply read/announce "밖에서 더 놀고 싶었구나" for him.
  - Mari teacher should gently help pull out the words inside Jun-i's heart.
  - Jun-i should be the one who first says the desire: "밖에... 더 있고 싶어."
  - Because Jun-i has said what he wants, page 06 can naturally move to Mari teacher offering a timed alternative with the shell hourglass.
- Updated:
  - `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
  - `work_2026-06-11/page_plan.md`
  - `work_2026-06-11/batch_1/batch_1_prompt_plan.md` page 03 story lock language
- New page 05 title:
  - `밖에 더 있고 싶어`
- New page 05 exact text starts with Jun-i saying:
  - `"나... 그냥 싫어."`
- New page 05 exact text ends with Jun-i saying:
  - `"밖에... 더 있고 싶어."`
- New page 06 logic:
  - Mari teacher says, "말해 줘서 고마워," then proposes waiting outside until the shell hourglass finishes.

## Next Step

- Continue to `01_candidate_text_restart_v1.png` and QA one page at a time for Jun-i identity, bag continuity, readable exact text, non-scary emotion, official-reference fidelity, updated page 05/06 emotional logic, and no old-version contamination.

## Batch 1 Page 01 Restart Candidate

- Generated:
  - `work_2026-06-11/batch_1/01_candidate_text_restart_v1.png`
- Page 01 restart v1 QA:
  - Korean story text is readable and appears exact:
    - `아침이 되었어요.`
    - `산호마을 어린이집 문이 열렸어요.`
    - `딩동댕동!`
    - `그런데 오늘 준이는`
    - `조금 삐친 얼굴이었어요.`
  - Scene matches the daycare exterior/playground with entrance, slide, coral tunnel, and warm morning atmosphere.
  - Friends are entering gently; Jun-i is separated in the foreground with blue arrival bag and pouty body language.
  - Lulu keeps visible seahorse snout/ridge/tail; Popo remains a moon jelly with eyes hidden/barely visible; Aru remains pufferfish-like without human limbs.
  - Remaining caution: Jun-i is still slightly softened/rounder than the official reference, but keeps the shark snout, white lower face/belly, gill marks, dorsal fin, side fin, long tail, sailor outfit, and bag. Treat as current review candidate unless user requests a stricter redraw.

## Next Step

- Continue to `02_candidate_text_restart_v1.png`.

## Batch 1 Page 02 Restart Candidates

- Generated:
  - `work_2026-06-11/batch_1/02_candidate_text_restart_v1.png`
  - `work_2026-06-11/batch_1/02_candidate_text_restart_v2.png`
- Page 02 restart v1 QA:
  - Text is readable and story content is correct.
  - Mari teacher's posture is warm and non-scolding; Banguli remains droplet-like.
  - Hold as backup only because Jun-i's body/head reads too round and plush-like for a central restart page.
- Page 02 restart v2 QA:
  - Current best page 02 candidate.
  - Text is readable and appears correct, though generated quote marks are curly rather than plain script quotes.
  - Doorway/playground conflict is visually clear.
  - Mari teacher keeps yellow apron, star hairpin, purple notebook, and purple tail; her hand is open and patient.
  - Banguli remains a soft droplet.
  - Jun-i is closer to official side-view silhouette than v1: clearer snout, white lower face/belly, gill marks, dorsal fin, side fin, long tail, sailor outfit, and blue bag.
  - Remaining caution: Jun-i is still slightly picture-book-rounded and the eye carries a tiny pout line, but it no longer reads as strongly whale-like as v1.

## Next Step

- Continue to `03_candidate_text_restart_v1.png`.

## Batch 1 Page 03 Restart Candidates

- Generated:
  - `work_2026-06-11/batch_1/03_candidate_text_restart_v1.png`
  - `work_2026-06-11/batch_1/03_candidate_text_restart_v2.png`
- Page 03 restart v1 QA:
  - Hold/reject for text and expression.
  - First line rendered as `굴렸어요` instead of script-correct `굴렀어요`.
  - Jun-i's open mouth/teeth read a little too sharp for the toddler-safe protest tone.
- Page 03 restart v2 QA:
  - Current best page 03 candidate.
  - Text is readable and appears exact:
    - `준이는 발을 쿵쿵 굴렀어요.`
    - `"싫어! 싫어!`
    - `안 들어갈래!"`
    - `준이 마음속에는`
    - `커다란 싫어싫어 파도가`
    - `출렁였어요.`
  - Does not reveal or imply `밖에 더 있고 싶어`.
  - Symbolic wave reads as a visible emotion wave, not a dangerous real wave.
  - Friends are concerned observers, not a shaming crowd.
  - Lulu keeps her snout/ridge/tail; Tori keeps shell/hat; Mongle keeps octopus silhouette; Banguli remains a droplet.
  - Remaining caution: Jun-i's mouth still shows small official shark teeth, but the expression is less predatory than v1 and stays within childlike protest.

## Batch 1 Restart Current Review Set

- Cover: `00_cover_candidate_restart_v3.png`
- Page 01: `01_candidate_text_restart_v1.png`
- Page 02: `02_candidate_text_restart_v2.png`
- Page 03: `03_candidate_text_restart_v2.png`
