# Tori Tunnel Restart Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restart `토리야, 한 걸음만` by locking the coral tunnel as a consistent straight toddler crawl-through prop before generating any new pages.

**Architecture:** The work is split into a new isolated episode rework folder, a tunnel-lock batch, then page batches. Existing `final` and prior `work_*` folders remain process history only; official references and the newly approved tunnel lock become the visual truth for new candidates.

**Tech Stack:** Markdown production plans, local filesystem episode folders, official PNG reference assets, image-generation workflow with concrete reference-file checklists, manual QA worklogs, Git for plan/spec tracking.

---

### Task 1: Create Rework Workspace Skeleton

**Files:**
- Create: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md`
- Create: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/page_plan.md`
- Create: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md`
- Create directory: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock`
- Create directory: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1`

- [ ] **Step 1: Create directories**

Run:

```powershell
New-Item -ItemType Directory -Force 'series\coral-town-daycare\images\episodes\토리야_한_걸음만\rework_2026-06-18\tunnel_lock'
New-Item -ItemType Directory -Force 'series\coral-town-daycare\images\episodes\토리야_한_걸음만\rework_2026-06-18\batch_1'
```

Expected: both directories exist.

- [ ] **Step 2: Write `episode_worklog.md`**

Content:

```markdown
# Episode Worklog - 토리야, 한 걸음만 - Rework 2026-06-18

## Source

- Script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Design spec: `docs/superpowers/specs/2026-06-18-tori-tunnel-restart-design.md`

## Rework Rule

Existing `final`, `work_2026-06-03`, and `work_2026-06-06` files are process history only. Do not use them as visual truth for generation.

## Current Status

- Status: `setup`
- Current batch: `tunnel_lock`
- Next action: create and QA a straight single-axis toddler crawl-through coral tunnel lock before generating any page.

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

No candidates generated yet.
```

- [ ] **Step 3: Write `page_plan.md`**

Content:

```markdown
# Page Plan - 토리야, 한 걸음만 - Rework 2026-06-18

## Episode

- Script: `series/coral-town-daycare/docs/episodes/tori_tunnel_story_prompts.md`
- Work root: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18`
- Format: A5 portrait, about `1:1.414`
- Text workflow: include exact Korean story text in the first page-generation pass unless a tunnel-lock asset is being generated.

## Reference Rule

Before every generation, list concrete reference image paths for all visible named characters, recurring locations, and props. Do not generate from prose-only descriptions.

## Tunnel Lock Batch

- `tunnel_lock_reference_board.png`: page-specific reference board for the fixed tunnel prop.
- `coral_tunnel_straight_tube_lock_candidate_v1.png`: first candidate for the locked straight toddler crawl-through tunnel.

## Batch 1

- `00_표지.png`: Tori hesitates at the coral tunnel, Banguli peeks from the opposite opening.
- `01_페이지.png`: New tunnel appears in the playground; friends gather, Tori approaches carefully.
- `02_페이지.png`: Friends pass through the tunnel; Tori watches from a distance.
- `03_페이지.png`: Tori looks at the tunnel and worries.

## Batch Gate

Do not generate Batch 1 until the tunnel lock candidate has passed QA and the user has accepted it as the new tunnel visual truth.
```

- [ ] **Step 4: Verify workspace skeleton**

Run:

```powershell
Get-ChildItem -Recurse 'series\coral-town-daycare\images\episodes\토리야_한_걸음만\rework_2026-06-18' | Select-Object FullName
```

Expected: the worklog, page plan, `tunnel_lock`, and `batch_1` paths are present.

- [ ] **Step 5: Commit setup files**

Run:

```powershell
git add -- 'series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md' 'series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/page_plan.md' 'series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md'
git commit -m "Set up Tori tunnel rework workspace"
```

Expected: one commit containing only setup markdown files.

---

### Task 2: Write Tunnel Lock Prompt Plan

**Files:**
- Modify: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md`
- Modify: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md`

- [ ] **Step 1: Write reference checklist**

Add this content to `tunnel_lock_prompt_plan.md`:

```markdown
# Tunnel Lock Prompt Plan - 토리야, 한 걸음만

## Purpose

Create a single visual lock for the coral tunnel before any new storybook page generation. This lock prevents the tunnel from changing into a cave, L-shaped structure, cornered passage, broad interior hallway, or same-facing double-opening structure.

## References To Attach

- Official tunnel location: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Tunnel scale comparison: `series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png`
- Tori scale reference: `series/coral-town-daycare/references/characters/토리.png`
- Playground context: `series/coral-town-daycare/references/배경_전경과_놀이터.png`

## Visual Lock

The coral tunnel is one straight, single-axis toddler crawl-through tube. It is a playground prop, not a cave. It is low enough that Tori must lower his body and head to pass through, but it is safe and warm. It has rounded pastel coral-pink surfaces, thick soft rims, and one clear passage direction.

## Geometry Requirements

- Show one straight tube body.
- Show one near opening clearly.
- If the far opening is visible, it must face the opposite direction as the far end of the same tube.
- Keep the tube low, toddler-scaled, and crawl-through.
- Keep the tube warm, friendly, and softly lit.

## Negative Locks

- No L shape.
- No corner bend.
- No side branch.
- No second separate tunnel.
- No same-facing double arches.
- No giant cave mound.
- No wide hallway interior.
- No dark deep-sea cave.
- No sharp coral spikes near the passage.

## Candidate Prompt

Create a storybook prop reference sheet for the fixed coral tunnel used in `토리야, 한 걸음만`. Use the attached official tunnel, tunnel scale comparison, Tori, and playground references as visual truth.

The main object is a single straight toddler crawl-through coral tunnel, a low playground tube made of soft pastel pink-coral forms. It has one clear near opening with a thick rounded rim. The tube body continues straight backward along one axis. The far opening is either hidden by angle and coral body or barely visible as the opposite end of the same straight tube, never as a second same-facing arch. The tunnel is low enough that Tori must lower his head and shell slightly to pass through, but it is safe, warm, and inviting.

Show the tunnel with a small Tori scale marker beside it: Tori stands upright next to the entrance, making clear that the opening is child-sized and low. Also include a tiny side-view diagram-like vignette showing Tori bending slightly to enter, with Tori remaining the same size as the standing marker. Keep the image in the soft Coral Town Daycare watercolor and colored-pencil style.

Leave clean margins and do not add story text. Add no signs, no pseudo-writing, and no unrelated characters. The result is a prop lock reference, not a finished storybook page.
```

- [ ] **Step 2: Add QA checklist to the prompt plan**

Append:

```markdown
## QA Checklist

- The tunnel reads as one straight pass-through tube.
- The near opening is clear and child-safe.
- No L-turn, side branch, second tunnel, or same-facing double arch appears.
- Tori scale is consistent between standing and bending views.
- Tori must lower body/head to enter, but the tunnel is not a scary cave.
- The style matches the official soft watercolor/colored-pencil Coral Town Daycare look.
- No text, labels, pseudo-writing, or extra signs appear.
```

- [ ] **Step 3: Update worklog status**

Add under `## Candidate Status Log`:

```markdown
## Tunnel Lock Prompt Plan - 2026-06-18

- Status: `prompt plan ready`
- File: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md`
- Next action: generate `coral_tunnel_straight_tube_lock_candidate_v1.png` using the listed reference images.
```

- [ ] **Step 4: Verify prompt plan has no placeholders**

Run:

```powershell
rg -n "미작성|빈칸" 'series\coral-town-daycare\images\episodes\토리야_한_걸음만\rework_2026-06-18\tunnel_lock\tunnel_lock_prompt_plan.md'
```

Expected: no matches.

- [ ] **Step 5: Commit prompt plan**

Run:

```powershell
git add -- 'series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/tunnel_lock_prompt_plan.md' 'series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md'
git commit -m "Plan Tori coral tunnel lock"
```

Expected: one commit containing the prompt plan and worklog update.

---

### Task 3: Generate And QA Tunnel Lock Candidate

**Files:**
- Create: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Modify: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md`

- [ ] **Step 1: Load visual-generation requirements**

Before generating, read the image generation skill and confirm the tool can attach actual reference image files. If reference attachments are unavailable, stop and report that limitation instead of generating a text-only image.

- [ ] **Step 2: Generate the candidate using actual image references**

Use the prompt from `tunnel_lock_prompt_plan.md` and attach these exact files:

```text
series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png
series/coral-town-daycare/references/props/산호_터널_크기비교_레퍼런스_v2.png
series/coral-town-daycare/references/characters/토리.png
series/coral-town-daycare/references/배경_전경과_놀이터.png
```

Save output as:

```text
series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png
```

- [ ] **Step 3: Inspect candidate visually**

Open the image and check:

```text
straight single-axis tube
one clear near opening
no L shape
no corner bend
no side branch
no same-facing double arches
low toddler scale against Tori
Tori scale consistent between standing and bending markers
warm safe playground mood
```

- [ ] **Step 4: Record QA result**

If it passes, append:

```markdown
## Tunnel Lock Candidate v1 - 2026-06-18

- File: `tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Status: `candidate pass`
- QA:
  - Straight single-axis tube: pass
  - Same-facing double opening: pass
  - L shape / corner / branch: pass
  - Toddler scale with Tori: pass
  - Warm safe style: pass
- Next action: ask user to approve the tunnel lock before Batch 1 page generation.
```

If it fails, append:

```markdown
## Tunnel Lock Candidate v1 - 2026-06-18

- File: `tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Status: `fail`
- QA:
  - Straight single-axis tube: fail
  - Same-facing double opening: [pass/fail]
  - L shape / corner / branch: [pass/fail]
  - Toddler scale with Tori: [pass/fail]
  - Warm safe style: [pass/fail]
- Next action: regenerate only the tunnel lock candidate with corrected geometry.
```

- [ ] **Step 5: Stop for user approval**

Do not generate Batch 1 pages until the user approves the tunnel lock candidate.

---

### Task 4: Prepare Batch 1 Prompt Plan After Tunnel Approval

**Files:**
- Create: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_1/batch_1_prompt_plan.md`
- Modify: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/episode_worklog.md`

- [ ] **Step 1: Create Batch 1 reference policy**

Write:

```markdown
# Batch 1 Prompt Plan - 토리야, 한 걸음만 - Rework 2026-06-18

## Batch Scope

- `00_cover_candidate_2026-06-18_v1.png`
- `01_candidate_2026-06-18_v1.png`
- `02_candidate_2026-06-18_v1.png`
- `03_candidate_2026-06-18_v1.png`

## Required Tunnel Lock

Use the user-approved tunnel lock candidate from `../tunnel_lock/` as the tunnel prop truth. The tunnel remains a straight single-axis toddler crawl-through tube. Do not reinterpret the tunnel from earlier failed candidates.

## Global Negative Locks

- No child bags during playground play.
- No L-shaped tunnel, corner tunnel, side branch, same-facing double openings, cave mound, or broad interior corridor.
- No shaming, pushing, pulling, dragging, or scolding Tori.
- No pseudo-writing or extra signage.
```

- [ ] **Step 2: Add page 00 plan**

Add:

```markdown
## 00 Cover

### References To Attach

- `series/coral-town-daycare/references/characters/토리.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- approved tunnel lock candidate from `rework_2026-06-18/tunnel_lock/`

### Required Text

```text
토리야, 한 걸음만

— 무서워도 한 걸음
내디뎌 봐요 —
```

### Scene

Tori hesitates at the near opening of the locked straight coral tunnel. Banguli peeks from the opposite end only if it clearly reads as the far end of the same straight tube. If geometry becomes confusing, show Banguli near the tunnel opening instead of showing both ends.
```

- [ ] **Step 3: Add pages 01-03 plan**

Add page-specific reference lists and required text copied from `tori_tunnel_story_prompts.md`, with page 1 simplified into small readable character groups.

- [ ] **Step 4: Verify prompt plan**

Run:

```powershell
rg -n "미작성|빈칸" 'series\coral-town-daycare\images\episodes\토리야_한_걸음만\rework_2026-06-18\batch_1\batch_1_prompt_plan.md'
```

Expected: no matches.

- [ ] **Step 5: Stop for review before generation**

Ask the user whether to generate Batch 1 after reading the prompt plan. Do not proceed if the tunnel lock has not been approved.

---

## Self-Review

- Spec coverage: The plan creates the rework folder, worklog, page plan, tunnel lock prompt plan, tunnel candidate workflow, QA gate, and Batch 1 prompt plan gate required by the design.
- Placeholder scan: The plan contains no unfilled work items; bracketed pass/fail options appear only in the failure log template where the worker records actual QA results.
- Scope check: The plan stops before Batch 1 image generation until the tunnel lock is user-approved, matching the batch-gate requirement.
