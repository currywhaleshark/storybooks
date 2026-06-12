# Juni No-No Wave Restart Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restart `준이의 싫어싫어파도` batch 1 in a clean `work_2026-06-12` folder, using official reference PNGs as visual truth and treating 2026-06-11 page candidates as superseded process history only.

**Architecture:** Create a fresh episode work scaffold with explicit reference checklists, page prompts, and QA gates before generating any image. Generate cover through page 03 one page at a time; before every image generation, load the actual visible reference image files into the conversation with `view_image`, label their roles in the prompt, then QA the output before continuing. If the generation workflow cannot use the loaded reference images as visual grounding, stop and report the limitation instead of producing a text-only-reference page.

**Tech Stack:** Local Markdown worklogs and prompt plans, Codex `view_image`, built-in `image_gen`, PowerShell filesystem checks, Git.

---

## File Structure

- `docs/superpowers/specs/2026-06-12-juni-no-no-wave-restart-design.md`: approved restart design, already written.
- `docs/superpowers/plans/2026-06-12-juni-no-no-wave-restart.md`: this implementation plan.
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`: new authoritative worklog for today, including superseded 2026-06-11 candidates and per-page QA.
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/page_plan.md`: page-by-page scene, text, visible characters, and concrete reference file checklist for cover through page 10.
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/batch_1_prompt_plan.md`: executable prompt plan for cover through page 03.
- `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/*.png`: generated candidates for cover through page 03, saved only after QA.

### Task 1: Create Clean Work Scaffold

**Files:**
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/page_plan.md`
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/batch_1_prompt_plan.md`

- [ ] **Step 1: Create the work folders**

Run:

```powershell
New-Item -ItemType Directory -Force -Path 'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1'
```

Expected: the `work_2026-06-12` and `batch_1` folders exist.

- [ ] **Step 2: Write the new worklog**

Create `episode_worklog.md` with this structure:

```markdown
# Episode Worklog - 준이의 싫어싫어파도 - 2026-06-12 Restart

## Source

- Script: `series/coral-town-daycare/docs/episodes/준이의_싫어싫어파도.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Restart design: `docs/superpowers/specs/2026-06-12-juni-no-no-wave-restart-design.md`
- Work root: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12`
- Final folder: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/final`

## Restart Decision

- Approved approach: A, complete new batch start.
- `work_2026-06-11/batch_1/*.png` candidates are `superseded` process history only.
- Do not use any 2026-06-11 page candidate as visual truth.
- Keep only the independent shell hourglass prop reference:
  - `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

## Superseded 2026-06-11 Candidates

- `00_cover_candidate_restart_v3.png`: superseded; not visual truth.
- `01_candidate_text_restart_v1.png`: superseded; not visual truth.
- `02_candidate_text_restart_v2.png`: superseded; not visual truth.
- `03_candidate_text_restart_v2.png`: superseded; not visual truth.

## Hard QA Locks

- Jun-i must match `references/characters/준이.png`: projecting shark snout, small black oval button eyes, white lower face and belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, and blue arrival bag.
- Pages 01-08 are arrival-time exterior continuity, so Jun-i keeps the blue bag on.
- Page 03 must not reveal or imply `밖에 더 있고 싶어`.
- Generate and QA one page at a time.
- A page candidate with wrong or garbled required text cannot be final promoted.

## Batch 1 Status

- Scope: cover through page 03.
- Current page: cover.
- Next action: create `page_plan.md` and `batch_1/batch_1_prompt_plan.md`, then generate cover candidate v1 using official references only.
```

- [ ] **Step 3: Write the page plan**

Create `page_plan.md` with page rows for cover through page 10. For batch 1, include these concrete reference lists:

```markdown
# Page Plan - 준이의 싫어싫어파도 - 2026-06-12 Restart

## Locked Reference Files

- Exterior/playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Coral tunnel: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Shell hourglass: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png`

## Batch 1

### 00 Cover

- Output: `work_2026-06-12/batch_1/00_cover_candidate_2026-06-12_v1.png`
- Visible characters: Jun-i, Mari teacher, Banguli
- References to load: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli
- Required text:

```text
준이의 싫어싫어파도

— 말로 말하면 작아져요 —
```

### 01 Page

- Output: `work_2026-06-12/batch_1/01_candidate_2026-06-12_v1.png`
- Visible characters: Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo
- References to load: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, Popo
- Required text:

```text
아침이 되었어요.
산호마을 어린이집 문이 열렸어요.
딩동댕동!
그런데 오늘 준이는
조금 삐친 얼굴이었어요.
```

### 02 Page

- Output: `work_2026-06-12/batch_1/02_candidate_2026-06-12_v1.png`
- Visible characters: Jun-i, Mari teacher, Banguli; background friends only if their references are loaded
- References to load: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, plus any visible friend references
- Required text:

```text
"준아, 어서 오렴."
마리 선생님이 말했어요.

하지만 준이는
입을 삐죽 내밀고 말했어요.

"아직 안 들어갈래!"
```

### 03 Page

- Output: `work_2026-06-12/batch_1/03_candidate_2026-06-12_v1.png`
- Visible characters: Jun-i, Banguli, Tori, Mongle, Lulu
- References to load: exterior/playground, coral tunnel, Jun-i, Banguli, Tori, Mongle, Lulu
- Required text:

```text
준이는 발을 쿵쿵 굴렀어요.
"싫어! 싫어!
안 들어갈래!"

준이 마음속에는
커다란 싫어싫어 파도가
출렁였어요.
```
```

- [ ] **Step 4: Write the batch 1 prompt plan**

Create `batch_1_prompt_plan.md` with the prompts from Tasks 2-5 below. Include a visible note at the top:

```markdown
Reference rule: before each `image_gen` call, load every listed local reference file with `view_image`. If the image generation workflow cannot use the loaded image references as visual grounding, stop and report the limitation instead of generating from prose only.
```

- [ ] **Step 5: Verify reference paths**

Run:

```powershell
$paths = @(
  'series/coral-town-daycare/references/배경_전경과_놀이터.png',
  'series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png',
  'series/coral-town-daycare/references/characters/준이.png',
  'series/coral-town-daycare/references/characters/마리_선생님.png',
  'series/coral-town-daycare/references/characters/방울이.png',
  'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-11/reference_assets/shell_hourglass_ref.png'
)
$paths | ForEach-Object { if (-not (Test-Path -LiteralPath $_)) { throw "Missing reference: $_" } }
```

Expected: no output and no exception.

### Task 2: Generate Cover Candidate

**Files:**
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/00_cover_candidate_2026-06-12_v1.png`
- Modify: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`

- [ ] **Step 1: Load reference images**

Use `view_image` on:

- `C:\Users\USER\Documents\Projects\산호마을어린이집\series\coral-town-daycare\references\배경_전경과_놀이터.png`
- `C:\Users\USER\Documents\Projects\산호마을어린이집\series\coral-town-daycare\references\locations\산호_터널_레퍼런스.png`
- `C:\Users\USER\Documents\Projects\산호마을어린이집\series\coral-town-daycare\references\characters\준이.png`
- `C:\Users\USER\Documents\Projects\산호마을어린이집\series\coral-town-daycare\references\characters\마리_선생님.png`
- `C:\Users\USER\Documents\Projects\산호마을어린이집\series\coral-town-daycare\references\characters\방울이.png`

Expected: all five images are visible in conversation context before the generation call.

- [ ] **Step 2: Generate cover**

Call `image_gen` once with this prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book cover
Primary request: Create the cover for `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: the loaded official daycare exterior/playground reference and coral tunnel reference are the setting truth; the loaded official Jun-i, Mari teacher, and Banguli references are character identity truth.

Scene/backdrop: morning outside Coral Town Daycare. Use the official coral daycare entrance with blue door, gentle playground, and rounded coral tunnel as visual truth. The background is soft and supportive, not busy.

Subject: Jun-i is the foreground focus. He wears his official blue arrival bag and stands slightly turned away from the entrance, gently pouting because he cannot go in yet. Preserve the official Jun-i silhouette exactly: projecting shark snout, small black oval button eyes, white lower face and belly, blue shark body, gill marks, dorsal fin, side fins, long shark tail, small teeth, sailor shirt, blue shorts, and shell-decorated blue shoulder bag. Do not make him a round whale-like child, plush blob, generic blue toddler, or redesigned shark.

Supporting characters: Mari teacher waits near the doorway with a calm open hand and warm expression. Preserve her half-up bob, star hairpin, yellow apron, name tag, cream blouse, purple attendance notebook, and purple mermaid tail. Banguli floats near Jun-i as a pale sky-blue transparent droplet with a simple caring face.

Emotion symbol: show the `싫어싫어 파도` as small rounded blue water ribbons, bubbles, and gentle rhythm lines around Jun-i. It is a symbolic feeling wave, not a dangerous ocean wave.

Composition/framing: uncrowded cover. Focus on Jun-i, Mari teacher, and Banguli only. Other children should be omitted or only faint tiny doorway hints. Leave bright clean title space at the top.

Text (verbatim): render exactly:

준이의 싫어싫어파도

— 말로 말하면 작아져요 —

Constraints: exact official reference fidelity is more important than extra cuteness. Keep all characters toddler-safe and warm.
Avoid: crowded group cover, over-round Jun-i, changed eye shape, large sad eyes, scary shark expression, aggressive wave, scolding teacher pose, random signs, pseudo-writing, neon colors, plastic 3D texture, watermark.
```

Expected: one generated cover image.

- [ ] **Step 3: Save the generated image into the batch folder**

Copy the selected generated image reported by the tool to:

```text
series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/00_cover_candidate_2026-06-12_v1.png
```

Expected: the workspace file exists and the original generated image is not overwritten.

- [ ] **Step 4: QA the cover**

Use `view_image` on the saved candidate and check:

- Jun-i is not whale-like or plush-round.
- Jun-i keeps small black oval button eyes.
- Jun-i keeps snout, gills, fins, tail, sailor outfit, and blue bag.
- Mari teacher keeps yellow apron, star pin, purple tail, and teacher posture.
- Banguli remains a droplet.
- Title is exact or the title area is clean enough for a text-panel repair.

Expected: if all pass, mark `candidate pass`; if any identity lock fails, mark `fail` and do not continue to page 01.

- [ ] **Step 5: Update worklog**

Append the QA result:

```markdown
## Batch 1 Cover - 2026-06-12

- Generated: `batch_1/00_cover_candidate_2026-06-12_v1.png`
- Status: `candidate pass` or `fail`
- Reference grounding: exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli loaded before generation.
- QA: Jun-i identity, Mari identity, Banguli identity, text, background, contamination.
- Next action: continue to page 01 only if the cover passes Jun-i identity.
```

### Task 3: Generate Page 01 Candidate

**Files:**
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/01_candidate_2026-06-12_v1.png`
- Modify: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`

- [ ] **Step 1: Load reference images**

Use `view_image` on exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, and Popo.

Expected: all visible characters have actual official reference images loaded before generation.

- [ ] **Step 2: Generate page 01**

Call `image_gen` with this prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 01
Primary request: Create page 01 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are the setting truth; loaded official Jun-i, Mari teacher, Banguli, Tori, Mongle, Lulu, Aru, and Popo are character identity truth.

Scene/backdrop: morning at the Coral Town Daycare entrance. Use the official exterior/playground reference: coral daycare building with blue door, soft playground, coral slide/water play hints, and rounded coral tunnel. Bright, safe, warm morning.

Main subject: Jun-i is in the foreground, separated slightly from the others, wearing his official blue arrival bag. He is not entering yet. He gently pouts and looks toward the outside playground with regret. Preserve the official shark shape: projecting snout, small black oval button eyes, white lower face/belly boundary, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. Do not make him rounder, softer, younger-looking, or more generic than the official reference.

Other characters: Mari teacher welcomes children at the doorway. Tori, Mongle, Lulu, Aru, and Popo move toward the entrance in a loose diagonal flow. Each visible friend must keep their official species silhouette and arrival bag/hat/details. Lulu must keep her long tube snout, spiny dotted ridge, coral/shell ornament, translucent fin, and curled tail. Popo must keep the moon-jelly dome and soft tentacles with eyes hidden or barely visible. Aru must remain a pufferfish body with no human hands, feet, legs, or separate lower body. Banguli floats near Jun-i.

Composition/framing: wide establishing view with slight diagonal flow from playground to doorway. Do not crowd all friends tightly together; give each character enough room for silhouette to read. Keep Jun-i large enough for official eye shape, snout, gills, fins, tail, and bag to be visible. Leave a bright clean text area in the upper-left water/sky space.

Text (verbatim): render exactly:

아침이 되었어요.
산호마을 어린이집 문이 열렸어요.
딩동댕동!
그런데 오늘 준이는
조금 삐친 얼굴이었어요.

Constraints: official-reference silhouette and facial structure override extra cuteness. Friends may be smaller than Jun-i, but they must not become generic sea creatures.
Avoid: over-round Jun-i, large sad eyes, missing gill marks, missing dorsal fin, missing blue bag, generic pink Lulu, Popo with normal big eyes, Aru with hands/feet, shaming crowd, old generated candidate contamination, pseudo-writing, random signs, watermark.
```

- [ ] **Step 3: Save and QA**

Save to `batch_1/01_candidate_2026-06-12_v1.png`, then inspect with `view_image`.

Expected QA pass:

- Korean text is exact and readable.
- Jun-i has official button eyes, projecting snout, gill marks, fins, long tail, sailor outfit, and blue bag.
- Lulu, Popo, and Aru keep fragile official details.
- Friends enter gently; Jun-i is separate and pouty, not scary.

- [ ] **Step 4: Update worklog**

Append page 01 status with `candidate pass`, `hold`, or `fail`. Do not continue to page 02 if Jun-i identity fails.

### Task 4: Generate Page 02 Candidate

**Files:**
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/02_candidate_2026-06-12_v1.png`
- Modify: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`

- [ ] **Step 1: Load reference images**

Use `view_image` on exterior/playground, coral tunnel, Jun-i, Mari teacher, Banguli, and any clearly visible friend references.

Expected: no visible named character lacks an official loaded reference.

- [ ] **Step 2: Generate page 02**

Call `image_gen` with this prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 02
Primary request: Create page 02 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are setting truth; loaded official Jun-i, Mari teacher, Banguli, and any visible friend references are character identity truth.

Scene/backdrop: medium-distance view at the Coral Town Daycare doorway. The official blue door and exterior/playground are visible, with the outside playground pull clear enough to explain Jun-i's reluctance. Use the rounded coral tunnel naturally if visible.

Main subject: Jun-i stands near the entrance floor, still wearing his official blue bag. His body is slightly turned away from the doorway, with a small tucked-fin or crossed-fin posture that fits a shark body. His snout and small black button eyes angle toward the playground. He looks pouty, stubborn, and regretful, not frightened or angry.

Mari teacher: Mari gestures gently toward the door and waits without scolding. Preserve her official hair, star pin, yellow apron, name tag, purple notebook, and purple mermaid tail. Her posture is patient and low-pressure.

Banguli: Banguli floats near Jun-i, curious and worried, as a soft transparent water droplet.

Composition/framing: side-focused medium shot. Doorway on one side, playground pull on the other. Use fewer supporting friends than page 01 if needed; do not invent or simplify friends without their official reference. Leave a clean text area in the upper-right.

Text (verbatim): render exactly:

"준아, 어서 오렴."
마리 선생님이 말했어요.

하지만 준이는
입을 삐죽 내밀고 말했어요.

"아직 안 들어갈래!"

Constraints: Jun-i remains the official blue shark child with small button eyes and full shark silhouette. Mari does not pull, push, scold, or point sharply.
Avoid: changed Jun-i eyes, round whale-like Jun-i, human hands/feet added to sea children, teacher grabbing Jun-i, crowded doorway, random Korean text, pseudo-writing, old generated candidate contamination, watermark.
```

- [ ] **Step 3: Save and QA**

Save to `batch_1/02_candidate_2026-06-12_v1.png`, then inspect with `view_image`.

Expected QA pass:

- Text is exact and readable.
- Doorway/playground conflict is visually clear.
- Jun-i's official shark silhouette and blue bag are intact.
- Mari teacher is patient, not scolding or pulling.
- No unreferenced background friends are invented.

- [ ] **Step 4: Update worklog**

Append page 02 status. Do not continue to page 03 if Jun-i identity or story clarity fails.

### Task 5: Generate Page 03 Candidate

**Files:**
- Create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/03_candidate_2026-06-12_v1.png`
- Modify: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`

- [ ] **Step 1: Load reference images**

Use `view_image` on exterior/playground, coral tunnel, Jun-i, Banguli, Tori, Mongle, and Lulu.

Expected: all visible named characters have actual official references loaded.

- [ ] **Step 2: Generate page 03**

Call `image_gen` with this prompt:

```text
Use case: illustration-story
Asset type: Korean toddler picture-book page 03
Primary request: Create page 03 of `준이의 싫어싫어파도` in A5 portrait proportion.
Input images: loaded official exterior/playground and coral tunnel are setting truth; loaded official Jun-i, Banguli, Tori, Mongle, and Lulu references are character identity truth.

Scene/backdrop: outside near the daycare entrance and playground path. Use the official exterior/playground reference and keep the setting warm, readable, and safe.

Main subject: Jun-i's big feeling bursts out. He wears his official blue arrival bag. He stomps/taps in a toddler-safe way or taps his shark tail, showing protest without aggression. Preserve the official Jun-i design: projecting snout, small black oval button eyes, white lower face/belly, gill marks, dorsal fin, side fins, long tail, sailor outfit, blue shorts, and blue bag. His mouth may open for `싫어!`, but do not enlarge teeth or make him predatory.

Story lock: do not show, write, imply, or speech-bubble the idea `밖에 더 있고 싶어`. This page shows only Jun-i's outer protest and the symbolic feeling wave.

Emotion symbol: the `싫어싫어 파도` is a soft symbolic feeling wave around Jun-i: rounded blue water ribbons, bubbles, gentle motion lines, and tiny safe sand/water splashes. It is not a real dangerous wave and should not threaten anyone.

Supporting characters: Banguli bounces in surprise near Jun-i. Tori, Mongle, and Lulu watch from a little distance with concern and surprise, not judgment. Keep them far enough not to crowd or shame Jun-i, but preserve their official silhouettes and details. Lulu must retain her long snout, spiny dotted ridge, head ornament, fin, and curled tail.

Composition/framing: dynamic low toddler-eye view. Jun-i is large enough for official snout, eye shape, gills, fins, tail, and bag to be clear. Keep clean text space at the top or upper side.

Text (verbatim): render exactly:

준이는 발을 쿵쿵 굴렀어요.
"싫어! 싫어!
안 들어갈래!"

준이 마음속에는
커다란 싫어싫어 파도가
출렁였어요.

Constraints: big emotion without fear. Official-reference fidelity over cute simplification. Friends respond with concern, not ridicule.
Avoid: phrase/visual meaning `밖에 더 있고 싶어`, dangerous wave, attack pose, scary teeth, large changed eyes, shaming crowd, generic supporting characters, pseudo-writing, random text, old generated candidate contamination, watermark.
```

- [ ] **Step 3: Save and QA**

Save to `batch_1/03_candidate_2026-06-12_v1.png`, then inspect with `view_image`.

Expected QA pass:

- Text is exact and readable.
- Page does not reveal or imply `밖에 더 있고 싶어`.
- Jun-i remains official, childlike, and safe despite the protest.
- Wave reads as symbolic emotion, not disaster.
- Tori, Mongle, and Lulu are concerned observers, not a crowd.

- [ ] **Step 4: Update worklog**

Append page 03 status. If the page passes, proceed to batch handoff.

### Task 6: Batch 1 Handoff and User Review

**Files:**
- Modify: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/episode_worklog.md`
- Optional create: `series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/HANDOFF_batch_1.md`

- [ ] **Step 1: Verify candidate files**

Run:

```powershell
$files = @(
  'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/00_cover_candidate_2026-06-12_v1.png',
  'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/01_candidate_2026-06-12_v1.png',
  'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/02_candidate_2026-06-12_v1.png',
  'series/coral-town-daycare/images/episodes/준이의_싫어싫어파도/work_2026-06-12/batch_1/03_candidate_2026-06-12_v1.png'
)
$files | ForEach-Object { if (-not (Test-Path -LiteralPath $_)) { throw "Missing candidate: $_" } }
```

Expected: all generated candidate files exist, unless work stopped earlier because a QA gate failed.

- [ ] **Step 2: Write handoff**

Create or append:

```markdown
# HANDOFF - 준이의 싫어싫어파도 - Batch 1 - 2026-06-12

## Generated Candidates

- Cover: `batch_1/00_cover_candidate_2026-06-12_v1.png`
- Page 01: `batch_1/01_candidate_2026-06-12_v1.png`
- Page 02: `batch_1/02_candidate_2026-06-12_v1.png`
- Page 03: `batch_1/03_candidate_2026-06-12_v1.png`

## QA Summary

- Character identity: cover, page 01, page 02, and page 03 passed official-reference identity QA.
- Text: cover, page 01, page 02, and page 03 text is readable and exact, or art candidates needing text repair are listed in the worklog.
- Story locks: page 03 does not reveal or imply `밖에 더 있고 싶어`; pages 01-03 preserve arrival-time blue bag continuity.
- Contamination: no 2026-06-11 page candidate was used as visual truth.

## User Review Needed

Do not promote to `final` until the user approves specific candidates.

## Next Batch If Approved

- Page 04: Mari sits beside Jun-i and waits without scolding.
- Page 05: Jun-i first says `밖에... 더 있고 싶어.`
- Page 06: Mari offers the shell hourglass timed alternative.
```

If work stops before all four candidates pass, use this exact QA summary instead:

```markdown
## QA Summary

- Character identity: batch stopped before completion because one or more candidates failed official-reference identity QA; see `episode_worklog.md` for the failing page and notes.
- Text: batch stopped before completion; no incomplete or failed text candidate is eligible for `final`.
- Story locks: batch stopped before completion; page 03 story-lock status is recorded in `episode_worklog.md` if page 03 was generated.
- Contamination: no 2026-06-11 page candidate was used as visual truth.
```

- [ ] **Step 3: Report to user**

Report:

- script path used
- reference files used
- generated candidate paths
- any failed or held pages
- that no file was promoted to `final`

Expected: the user can approve, reject, or request targeted retries for batch 1.
