# TTS Audio Tag Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a broad, Korean-labeled audio tag catalog to the TTS web app script editor.

**Architecture:** Keep the feature frontend-only. Store the catalog as structured constants in `tools/tts-video/public/app.js`, render it into a new sidebar panel in `tools/tts-video/public/index.html`, and style it in `tools/tts-video/public/styles.css`.

**Tech Stack:** Vanilla HTML, CSS, JavaScript, Python `unittest` static checks.

---

### Task 1: Frontend Test Coverage

**Files:**
- Modify: `tools/tts-video/tests/test_episode_selection.py`

- [ ] Add a failing static test that expects `AUDIO_TAG_CATALOG`, `renderAudioTagCatalog`, `audioTagCatalog`, category labels such as `감정`, and visible tag labels such as `[excitedly] · 신나게`.

- [ ] Run `python -m unittest tools.tts-video.tests.test_episode_selection` from the repository root and confirm the new test fails because the catalog does not exist yet.

### Task 2: Catalog Markup And Rendering

**Files:**
- Modify: `tools/tts-video/public/index.html`
- Modify: `tools/tts-video/public/app.js`

- [ ] Add `<section id="audioTagCatalog" class="tag-catalog gemini-only">` below the character preset panel.

- [ ] Add a broad `AUDIO_TAG_CATALOG` array in `app.js`, grouped by Korean category labels.

- [ ] Add helpers to display `[tag] · 번역` while inserting only `[tag] ` into the active textarea.

- [ ] Render the catalog from `renderSettingsVisibility()` and startup initialization so it appears whenever Gemini mode is visible.

### Task 3: Styling And Verification

**Files:**
- Modify: `tools/tts-video/public/styles.css`
- Test: `tools/tts-video/tests/test_episode_selection.py`

- [ ] Add compact sidebar styles for catalog groups and tag buttons.

- [ ] Run `python -m unittest tools.tts-video.tests.test_episode_selection` and confirm all tests pass.

- [ ] Optionally run the local server and inspect the UI if a browser check is needed.
