# Episode Worklog - Sherlock Umbrella Story

## Purpose

Continue the episode across sessions without carrying generated images in chat history. Record file paths, candidate status, QA notes, rejected files, and next steps only.

## Source Script

- Drive source: `https://drive.google.com/file/d/1nN_YVrxfe_i2mHHDSlpg9_RK6WuGbeL9/view?usp=drivesdk`
- Local script copy: `광장에_떨어진_알록달록한_것.drive.md`
- Series: `series/sherlock-fin-deep-city`
- Episode title: `광장에 떨어진 알록달록한 것`
- Theme: `알아낸 것과 아직 모르는 것을 또렷이 나누기`
- Core message: `모든 걸 다 몰라도 괜찮고, 모르는 것은 앞으로 알아가면 된다`

## Official References

Use actual image files as visual truth. Do not infer character, location, text-panel, or prop appearance from prose alone when a reference exists.

- Rulebook: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_이미지_생성_디자인_규칙서.md`
- Character references:
  - `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - `series/sherlock-fin-deep-city/references/characters/펄리.png`
  - `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/모모.png`
- Background/style references:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_인물_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Prop reference to create first:
  - `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`

## Output Plan

- Work folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31`
- Final folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/final`
- Final naming:
  - `00_표지.png`
  - `01_페이지.png` through `11_페이지.png`

## Page Plan

| File | Page | Scene | Main refs |
| --- | --- | --- | --- |
| `00_표지.png` | 표지 | Sherlock Fin and friends surround a half-open colorful umbrella in Jazz Plaza | all characters, Deep City, umbrella prop |
| `01_페이지.png` | 1 | Morning Jazz Plaza, object only barely visible | Deep City, umbrella prop |
| `02_페이지.png` | 2 | Friends view the half-open umbrella from a distance | friends, Deep City, umbrella prop |
| `03_페이지.png` | 3 | Friends guess big jellyfish/table coral/sea lily with imagination bubbles | friends, Deep City, umbrella prop |
| `04_페이지.png` | 4 | Sherlock Fin arrives and starts observation | Sherlock Fin, friends, Deep City, umbrella prop |
| `05_페이지.png` | 5 | Handle clue close-up | Sherlock Fin, umbrella prop |
| `06_페이지.png` | 6 | Umbrella rib movement, folded/open action | Sherlock Fin, friends, umbrella prop |
| `07_페이지.png` | 7 | Looking upward from under opened umbrella | Sherlock Fin, friends, umbrella prop |
| `08_페이지.png` | 8 | Two-column clue board: known vs unknown | Sherlock Fin, friends, text layout |
| `09_페이지.png` | 9 | Friends look upward in water; nothing falls | Sherlock Fin, friends, Deep City |
| `10_페이지.png` | 10 | Sherlock Fin says not knowing is okay | Sherlock Fin, friends |
| `11_페이지.png` | 11 | Umbrella becomes a cozy plaza shelter | all characters, Deep City, umbrella prop |

## Production Batches

- Prop setup: create and QA `알록달록한_우산_레퍼런스.png` first.
- Batch 1: cover + pages 1-3.
- Batch 2: pages 4-7.
- Batch 3: pages 8-11 and final QA.

Keep each generation batch small. Before every page generation, inspect or pass the actual reference images for visible characters, background, layout, and umbrella prop.

## Current Status

- Script fetched from Google Drive and saved locally.
- Official series rulebook and character/background/layout references found.
- Episode work/final folders created.
- Dedicated colorful umbrella prop reference generated and saved:
  - `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`
- Prop QA:
  - Pass as official recurring prop reference.
  - Main half-open view shows red, yellow, blue, and green segmented canopy.
  - Includes thin metal ribs, central shaft, curved hook handle, folded view, top view, and handle/rib close-up.
  - Reads as an ordinary human-world umbrella, not a jellyfish, mushroom, tent, flower, or sea creature.
- Batch 1 candidates generated and saved:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1/00_candidate_text_v1.png`
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1/01_candidate_text_v1.png`
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1/02_candidate_text_v1.png`
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1/03_candidate_text_v1.png`

## Batch 1 QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `00_candidate_text_v1.png` | Pass with caution | Strong cover composition; Sherlock Fin, friends, Deep City plaza, and umbrella are clear. Title appears readable. Background includes extra jazz signage, so regenerate if strict no-English-background-text is required. |
| `01_candidate_text_v1.png` | Fail - regenerate | User QA: Sherlock Fin should not appear yet on page 1. Momo back view looks odd. Also part of the batch shows subtle art-style drift. |
| `02_candidate_text_v1.png` | Pass | User QA: page 2 is OK. Friends view the umbrella at a safe distance; Sherlock Fin is absent as required. Text matches page 2 script. |
| `03_candidate_text_v1.png` | Fail - regenerate | User QA: PopPop's sunglasses disappeared. Keep the guess scene, but lock PopPop sunglasses and reduce style drift. |

## Batch 1 Style Drift Notes

- Likely cause: prompts emphasized a polished Deep City/jazz-plaza look and broad "premium picture book" rendering, which pushed the generator toward a glossier, sign-heavy, more detailed digital-painting finish than the official character/design sheets.
- Character-reference locks were not strict enough on page-specific absences and accessories: page 1 allowed the generator to introduce Sherlock Fin early, and page 3 omitted PopPop's sunglasses.
- Regeneration prompt locks:
  - Keep the official character-sheet proportions and accessory details.
  - Use simpler rounded shapes, cleaner linework, softer watercolor texture, less glossy neon detail.
  - Avoid extra signage and pseudo-writing.
  - Page 1: no Sherlock Fin anywhere; Momo only if his body reads clearly and naturally from behind.
  - Page 3: PopPop must wear black sunglasses and teal headphones.

## Batch 1 Regeneration QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `01_candidate_text_v2.png` | Review | Sherlock Fin removed. Momo back view is clearer and less distorted than v1. Background is less sign-heavy. Text remains readable. |
| `03_candidate_text_v2.png` | Review | PopPop sunglasses restored while retaining teal headphones. Imagination bubbles and umbrella continuity remain correct. Background is less sign-heavy than v1. |

Current Batch 1 review set:

- `00_candidate_text_v1.png`
- `01_candidate_text_v2.png`
- `02_candidate_text_v1.png`
- `03_candidate_text_v2.png`

## Batch 1 Approval

- User approved Batch 1 after reviewing the corrected page 1 and page 3.
- Approved files promoted to `final`:
  - `work_2026-05-31/batch_1/00_candidate_text_v1.png` -> `final/00_표지.png`
  - `work_2026-05-31/batch_1/01_candidate_text_v2.png` -> `final/01_페이지.png`
  - `work_2026-05-31/batch_1/02_candidate_text_v1.png` -> `final/02_페이지.png`
  - `work_2026-05-31/batch_1/03_candidate_text_v2.png` -> `final/03_페이지.png`

## Official Batch 2 Preparation

- Official next-batch folder prepared:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_2_official`
- Prompt plan:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_2_official/batch_2_prompt_plan.md`
- Official Batch 2 scope: pages 4-7 only.
- Generation gate:
  - Generate pages 4-7 only.
  - QA pages 4-7 and wait for review before starting pages 8-11.
- Continuity locks:
  - Page 4 is Sherlock Fin's first body-page appearance.
  - Sherlock Fin must follow the official character sheet: teal hair, brown detective hat and coat, teal mermaid tail, black gloves, yellow magnifying glass.
  - PopPop keeps black sunglasses and teal headphones.
  - Momo's shape must remain rounded/readable and not distorted.
  - Keep the softer Batch 1 v2 direction: simple rounded forms, clean soft linework, gentle watercolor texture, less glossy neon density, no readable English signage or pseudo-writing.
  - Do not imply rain or draw falling raindrops yet.
- Existing `work_2026-05-31/batch_2` images remain ungated drafts from the earlier mistaken run and are not approved production outputs.

## Next Step

- Wait for user visual approval on Batch 1 before copying candidates to `final`.
- If approved, promote:
  - `00_candidate_text_v1.png` -> `final/00_표지.png`
  - `01_candidate_text_v1.png` -> `final/01_페이지.png`
  - `02_candidate_text_v1.png` -> `final/02_페이지.png`
  - `03_candidate_text_v1.png` -> `final/03_페이지.png`
- Then generate Batch 2 pages 4-7: Sherlock Fin arrival, handle clue, rib movement, and under-umbrella view.

## Batch 2 QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `04_candidate_text_v1.png` | Pass | Sherlock Fin arrival, hat, magnifying glass, friends, and umbrella are clear. Korean text matches page 4 script. |
| `05_candidate_text_v1.png` | Pass with text caution | Strong handle clue close-up; magnifying glass enlarges the blue hook handle. Text content matches the script, but the ellipsis uses dot glyphs rather than the exact script marks. |
| `06_candidate_text_v1.png` | Pass with text caution | Good folding/opening action and friend reactions. Text content matches, but the `스르륵—` dash and quote glyphs are not exact. |
| `07_candidate_text_v1.png` | Pass with text caution | Strong under-umbrella view with canopy acting as roof. Text content matches, but ellipsis/quote glyphs are not exact. |

## Updated Next Step

- Keep Batch 1 and Batch 2 as visual candidates.
- Generate Batch 3 pages 8-11.
- Before final promotion, decide whether to accept generator-rendered text as-is or run a deterministic text-panel cleanup pass on pages with text cautions.

## Earlier Ungated Batch 3 QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `08_candidate_text_v1.png` | Hold | Board structure and text were good, but the known-facts board included rain/drop-like marks, which risks revealing the unknown too early. Do not promote. |
| `08_candidate_text_v2.png` | Pass with text caution | Improved board: no rain/droplet answer; left side shows handle, fold/open, and roof-like protection; right side stays a question mark. Text content matches, punctuation glyphs are not exact. |
| `09_candidate_text_v1.png` | Pass with text caution | Clear upward-looking scene; nothing falls from above; Sherlock Fin honestly admits he does not know. Text content matches, punctuation glyphs are not exact. |
| `10_candidate_text_v1.png` | Pass with text caution | Warm reassurance scene; friends smile and umbrella remains visible. Text content matches, punctuation glyphs are not exact. |
| `11_candidate_text_v1.png` | Pass | Strong cozy ending with all characters under the umbrella shelter. Text is readable and matches the ending content. |

## Current Candidate Set

- Final-approved cover/pages 1-7:
  - `final/00_표지.png`
  - `final/01_페이지.png` through `final/07_페이지.png`
- Current official Batch 3 review set:
  - `work_2026-05-31/batch_3_official/08_candidate_text_v1.png`
  - `work_2026-05-31/batch_3_official/09_candidate_text_v1.png`
  - `work_2026-05-31/batch_3_official/10_candidate_text_v1.png`
  - `work_2026-05-31/batch_3_official/11_candidate_text_v1.png`

## Workflow Correction

- Intended workflow: create one batch session, generate only that batch, QA and record it, then stop for user review or a fresh next-batch session.
- Current run deviated from that flow: Batch 2 and Batch 3 were generated immediately after Batch 1, before a separate user approval/new-session handoff.
- Treat Batch 2 and Batch 3 as ungated draft candidates only. They may be useful for visual direction, but they are not approved production outputs.
- Resume the official flow from the Batch 1 review gate.

## Final Promotion Gate

- Do not copy to `final` yet.
- First review gate: Batch 1 only. Page 3 must use a corrected `03_candidate_text_v3.png` before Batch 1 can be treated as complete.
- After corrected Batch 1 approval, start a separate next-batch pass for pages 4-7. Existing Batch 2 images can be referenced only as drafts, not as approved outputs.
- After Batch 2 approval, start a separate next-batch pass for pages 8-11. Existing Batch 3 images can be referenced only as drafts, not as approved outputs.
- If exact text is required, run a deterministic text-panel cleanup pass on the accepted visual candidates before final promotion.

## 2026-05-31 Page 3 Story-World Correction

- User caught an important story-world issue before official Batch 2: page 3's original guesses (`큰 버섯`, `텐트`, `활짝 핀 꽃`) are not natural for an underwater Deep City setting.
- Corrected page 3 guesses:
  - Momo: `큰 해파리`
  - PopPop: `테이블산호`
  - Pearly: `바다나리`
- Updated local script copy:
  - `광장에_떨어진_알록달록한_것.drive.md`
- Updated Batch 1 prompt plan:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_1/batch_1_prompt_plan.md`
- Existing page 3 candidates/final are now superseded for story-content reasons:
  - `work_2026-05-31/batch_1/03_candidate_text_v1.png`
  - `work_2026-05-31/batch_1/03_candidate_text_v2.png`
  - `final/03_페이지.png`
- Required next action before official Batch 2:
  - Review corrected page 3 candidate `work_2026-05-31/batch_1/03_candidate_text_v3.png`.
  - If approved, promote the corrected page to `final/03_페이지.png`.
  - Keep Batch 2 gated until this corrected page replaces the superseded final page.

## 2026-05-31 Corrected Page 3 Regeneration

| Candidate | Status | QA notes |
| --- | --- | --- |
| `03_candidate_raw_v3.png` | Raw visual source | Corrected underwater imagination bubbles generated: sea lily, table coral, and jellyfish. PopPop keeps black sunglasses and teal headphones. Real umbrella remains centered and unchanged. Generator-rendered text had spacing issues, so do not promote raw. |
| `03_candidate_text_v3.png` | Candidate pass, needs user approval | Deterministic text panel applied over the raw visual source with corrected page text. Visual content matches the story-world correction: no mushroom, tent, or land flower guesses. No Sherlock Fin appears. Ready for user review before replacing `final/03_페이지.png`. |

Current corrected Batch 1 review set:

- `00_candidate_text_v1.png`
- `01_candidate_text_v2.png`
- `02_candidate_text_v1.png`
- `03_candidate_text_v3.png`

## 2026-05-31 Page 3 Final Override

- User preferred the original generator-rendered `03_candidate_raw_v3.png` because its color and font treatment fit the book better, and the minor text spacing issue was acceptable.
- Promoted:
  - `work_2026-05-31/batch_1/03_candidate_raw_v3.png` -> `final/03_페이지.png`
- Batch 2 gate is now open.

## 2026-05-31 Official Batch 2 Continuation

- User clarified that the generator-rendered `돋보기` text on page 4 is acceptable. Restored `04_candidate_text_v1.png` to the original generated page and kept `04_candidate_raw_v1.png` as the same preserved source.
- User requested page 6 and 7 action corrections:
  - Page 6: Sherlock Fin should put away the magnifying glass and use her hands to fold/test the umbrella.
  - Page 7: Sherlock Fin should put away the magnifying glass and hold the opened umbrella.

| Candidate | Status | QA notes |
| --- | --- | --- |
| `04_candidate_text_v1.png` | Candidate pass, user text tolerance confirmed | Sherlock Fin first body-page appearance with friends and umbrella. User said the `돋보기` rendering is not an issue. |
| `05_candidate_text_v1.png` | Candidate pass | Handle clue close-up reads clearly; Sherlock Fin examines the blue curved hook handle. Text is generator-rendered and acceptable under current tolerance unless later exact text cleanup is requested. |
| `06_candidate_text_v1.png` | Superseded | Good folding clue, but Sherlock Fin still used/held a magnifying glass rather than physically handling the umbrella as requested. |
| `06_candidate_text_v2.png` | Superseded | Sherlock Fin has no magnifying glass and physically holds/pushes the umbrella, but the action can read like taking the umbrella apart. |
| `06_candidate_text_v3.png` | Superseded | Sherlock Fin has no magnifying glass and gently operates the intact umbrella, but the umbrella became too small and slightly crooked. |
| `06_candidate_text_v4.png` | Candidate pass | Umbrella is large, centered, upright, and intact. Sherlock Fin holds the shaft/handle and slides the mechanism; action reads as normal folding/opening rather than dismantling. |
| `07_candidate_text_v1.png` | Superseded | Strong under-umbrella view, but did not fully satisfy the requested hands-on holding direction. |
| `07_candidate_text_v2.png` | Candidate pass | Sherlock Fin holds the opened umbrella upright over the group. No magnifying glass in hand; canopy/ribs read as roof. No rain implied. |

Current official Batch 2 review set:

- `04_candidate_text_v1.png`
- `05_candidate_text_v1.png`
- `06_candidate_text_v4.png`
- `07_candidate_text_v2.png`

## 2026-05-31 Official Batch 2 Approval

- User approved Batch 2 after reviewing the corrected page 6.
- Approved files promoted to `final`:
  - `work_2026-05-31/batch_2_official/04_candidate_text_v1.png` -> `final/04_페이지.png`
  - `work_2026-05-31/batch_2_official/05_candidate_text_v1.png` -> `final/05_페이지.png`
  - `work_2026-05-31/batch_2_official/06_candidate_text_v4.png` -> `final/06_페이지.png`
  - `work_2026-05-31/batch_2_official/07_candidate_text_v2.png` -> `final/07_페이지.png`
- Final folder now contains approved cover and pages 1-7.
- Next official batch: pages 8-11.

## 2026-05-31 Official Batch 3 Preparation

- Official next-batch folder prepared:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_3_official`
- Prompt plan:
  - `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_3_official/batch_3_prompt_plan.md`
- Official Batch 3 scope: pages 8-11 only.
- Critical logic lock:
  - Do not reveal rain as the answer.
  - Page 8 board must show only known functions on the left and a question mark on the right.
  - No rain, falling droplets, clouds, storm, or weather-answer icons anywhere in pages 8-11.
- Existing `work_2026-05-31/batch_3` images remain ungated drafts from the earlier mistaken run and are not approved production outputs.

## 2026-05-31 Official Batch 3 QA

| Candidate | Status | QA notes |
| --- | --- | --- |
| `08_candidate_text_v1.png` | Candidate pass | Deduction board logic is correct: left side shows known functions, right side stays a question mark. No rain/drop answer appears. Text is generator-rendered and slightly paraphrased, consistent with current tolerance. |
| `09_candidate_text_v1.png` | Candidate pass | Characters look upward into blue water and star-sand; nothing falls from above. No rain/weather answer. Honest uncertainty beat reads clearly. |
| `10_candidate_text_v1.png` | Superseded | Warm reassurance scene works, but the umbrella became too small and visually secondary. |
| `10_candidate_text_v2.png` | Candidate pass | Umbrella is large, upright, and visually prominent while Sherlock Fin reassures the friends. Warm emotional beat remains clear. Text is generator-rendered and slightly paraphrased. |
| `11_candidate_text_v1.png` | Candidate pass | Cozy final shelter scene with all core characters under the upright umbrella. Warm ending reads well; no rain/weather answer is shown. |

Current official Batch 3 review set:

- `08_candidate_text_v1.png`
- `09_candidate_text_v1.png`
- `10_candidate_text_v2.png`
- `11_candidate_text_v1.png`

Next step:

- Wait for user visual approval on Batch 3 before promoting pages 8-11 to `final`.

## 2026-05-31 Official Batch 3 Approval

- User approved Batch 3 after reviewing corrected page 10.
- Approved files promoted to `final`:
  - `work_2026-05-31/batch_3_official/08_candidate_text_v1.png` -> `final/08_페이지.png`
  - `work_2026-05-31/batch_3_official/09_candidate_text_v1.png` -> `final/09_페이지.png`
  - `work_2026-05-31/batch_3_official/10_candidate_text_v2.png` -> `final/10_페이지.png`
  - `work_2026-05-31/batch_3_official/11_candidate_text_v1.png` -> `final/11_페이지.png`
- Final folder now contains the complete approved episode set:
  - `00_표지.png`
  - `01_페이지.png` through `11_페이지.png`
- Final count verified: 12 PNG files.
- Episode image production is complete unless later text cleanup/export packaging is requested.
