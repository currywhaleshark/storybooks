# TTS Audio Tag Catalog Design

Date: 2026-06-17

## Goal

Add a broad audio tag catalog to the TTS web app so script editing supports more than character-specific tag presets. The catalog should show the original English tag and a Korean meaning, then insert the selected tag into the active script textarea.

## Context

The app already loads series-level character presets from `series/<series>/docs/tts_voice_presets.yaml` and shows per-character tag buttons in `tools/tts-video/public/app.js`. Gemini TTS documentation says audio tags are flexible, non-exhaustive inline modifiers and recommends English tags even when the transcript is not English. The catalog should therefore include official common examples, tags currently used by presets, and picture-book-friendly exploratory tags.

## Design

Add a `Gemini`-only catalog panel below the existing character preset panel. The catalog is a frontend-only feature for now because it does not need per-series persistence or server work. Tags are grouped by category so the sidebar remains scannable: emotion, delivery, pace, volume, pauses, reactions, and character/performance color.

Each catalog row displays the tag and Korean translation together, for example `[excitedly] · 신나게`. Clicking the row inserts only the original tag plus a trailing space into the active TTS manuscript textarea. Existing character preset tags should continue to work and may reuse the same display helper so the original and translation are visible there too.

## Testing

Extend `tools/tts-video/tests/test_episode_selection.py` with static frontend checks that prove the catalog exists, includes broad categories, displays original and translated labels, and reuses the existing insertion behavior.
