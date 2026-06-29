# 밤사이 움직이는 것들 - Batch 4 Prompt Plan

## Batch Scope

- Pages: 10-11
- Output folder: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_4`
- Candidate filenames:
  - `10_candidate_text_v1_night_current_blocked.png`
  - `11_candidate_text_v1_morning_success.png`

## Actual References To Emit Before Generation

Use `nodeRepl.emitImage` for actual PNGs before generation.

- Official office interior: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- Approved door/gap/water-current v2: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- Sherlock Fin character: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Textbox layout: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Page 09 approved repair/test candidate: `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`
- Tidy-state anchors:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`

Do not emit the broad Deep City jazz reference for this batch; avoid music-note contamination.

## Shared Visual Rules

- A5 portrait children's picture book page, warm polished Korean illustration.
- Match the official detective office and current episode pages: shell/coral architecture, shell desk, clue board, shell door, bubble lamps, cozy deep blue-purple walls.
- Sherlock Fin must match the official character sheet: teal hair, detective cap, brown coat, teal mermaid tail, curious child detective expression.
- Use cream/shell-colored rounded text panels following the textbox reference.
- Keep the story safe and non-scary. No intruder, culprit shadow, horror lighting, or threat.
- Water current must be gentle and safe: translucent pale-blue ribbons, faint ripples, tiny bubbles. No waves/flood.
- No music notes, staff lines, sound-wave graphics, saxophone shapes, or neon audio symbols.
- Door state after repair: shell door closes tightly. No visible lower-right gap. No water current entering the office.
- Sherlock Fin anatomy: exactly two arms and two hands. Avoid support/knee/lap extra hands, duplicate glove silhouettes, and extra limbs.
- Door hardware remains physically plausible: hinges on viewer-left, handle/latch/lock on viewer-right closing edge, no central knob, no handle on hinge side.

## Page 10 Prompt

Generate A5 portrait page 10 for the children's picture book episode `밤사이 움직이는 것들`.

Scene: night verification after Sherlock Fin repaired the door. The detective office is cozy and dim-blue at night, with warm bubble lamp light inside. The shell door is tightly closed with no visible lower gap. Outside or just in front of the door, the gentle night water current changes direction and flows toward the door, then softly splits and slides around/past the closed door instead of entering.

Visual center: make the fixed closed door and blocked current clear. The current should be outside/at the threshold only, shown as pale-blue ribbons, ripples, and small bubbles that bend away from the door. Inside the office, the desk, papers, cards, feather pen, books, magnifying glass, and ink bottle remain still and tidy. No fluttering objects inside.

Composition: show both the door/threshold and a calm interior so the viewer understands the water is blocked and the office stays quiet. It may be a night cutaway or slightly wider office view, but do not shrink the door too much. Text panel at upper right or right side, not covering the blocked-current evidence.

Render exact Korean text in the cream rounded panel:

```text
그날 밤이 되었어요.

밤 물살이
다시 방향을 바꾸어
흘러왔어요.

사르르—
솔솔—

그런데 이번에는······

꼭 닫힌 문이
물살을 막아주었어요.

물살은 문 앞에서
부드럽게 비껴 흘렀어요.

사무소 안은
조용하고 아늑했어요.
```

Avoid: water entering the room, visible door gap, papers fluttering, flood, big waves, scary nighttime lighting, intruder/cullprit silhouette, music-note contamination, unreadable text, central doorknob.

## Page 11 Prompt

Generate A5 portrait page 11 for the children's picture book episode `밤사이 움직이는 것들`.

Scene: next morning conclusion in Sherlock Fin's detective office. Sherlock Fin opens or stands beside the shell door and sees that the office stayed exactly tidy. The documents are neatly stacked, the feather pen is in its holder or fixed place, small cards are straight and stacked, the desk is organized, and heavy objects are where they belong. Sherlock Fin smiles proudly and warmly, happy but calm.

Visual center: the tidy office should be unmistakable. This page mirrors the tidy-state logic from page 01 after the successful repair. Show a repaired, tightly closed shell door with normal hardware and no gap. No water current. No scattered papers.

Composition: warm morning light, satisfying final page. Sherlock Fin may stand in the foreground with two hands on hips or one hand near the door, but exactly two arms and two hands. Text panel at bottom center or lower band, with enough space for the longer closing text. Do not cover Sherlock Fin's face or the neat desk evidence.

Render exact Korean text in the cream rounded panel:

```text
다음 날 아침이에요.

셜록 핀이 문을 열었어요.

서류는 가지런히,
깃털 펜은 제자리에,
카드는 반듯하게.

어젯밤 그대로였어요!

'누가 들어온 게 아니었어.

바뀐 건 문 하나였지!'

이상한 일에는
무서운 누군가가 아니라
작은 이유가 숨어 있을 때가 있어요.

전에는 괜찮았는데
지금부터 이상하다면,

무엇이 달라졌는지
찾아보면 돼요.

꼬마 탐정 셜록 핀,
오늘도 성공!
```

Avoid: scattered papers, moved cards, feather pen on the floor, visible water current, visible door gap, scary mood, extra arms/hands, central doorknob, unreadable over-dense text.

## Batch 4 QA Checklist

- Page 10 shows the night current blocked by the tightly closed door and flowing around/outside, not entering.
- Page 10 keeps the office interior calm, tidy, and still.
- Page 10 uses water ribbons/ripples/bubbles only; no music/audio symbols.
- Page 11 clearly returns to the tidy state: papers stacked, feather pen in place, cards straight, heavy objects fixed.
- Page 11 shows repaired closed door with no gap and no current.
- Sherlock Fin has exactly two arms and two hands where visible.
- Text panels are present, readable, and match the script as closely as generator text allows.

## Page 10 User Correction - No Visible Current / Lights Off - 2026-06-28

- User QA on `10_candidate_text_v1_night_current_blocked.png`: page 10 should not show any water-current expression because the current cannot enter at all.
- Additional user correction: turn off the interior lights.
- Page 10 v2 locks:
  - Show no visible blue water ribbons, ripples, bubbles, waves, current lines, or glow inside or in front of the office door.
  - The repaired shell door is tightly closed with no gap.
  - Interior lamps/bubble lights are off. The office is dark but safe and calm, lit only by dim night ambient light from the window/Deep City outside if needed.
  - The tidy desk and papers/cards/feather pen remain completely still.
  - The visual proof is quietness/stillness, not a visible current being deflected.
- Next candidate: `10_candidate_text_v2_no_current_lights_off.png`.

## Page 10 Full Regeneration Direction - No Panel Replacement - 2026-06-28

- User correction after text-panel repair attempts: panel replacement tends to look strange; regenerate the whole page instead.
- Additional visual correction: the ceiling spherical bubble lamp disappeared in the lights-off version. Keep the ceiling spherical lamp visible, but switched off/dark, with no glow.
- Page 10 next regeneration locks:
  - Full-page regeneration, not local text-panel replacement.
  - No visible water-current expression at all: no ribbons, waves, bubbles, ripples, blue streaks, current trails, or glow anywhere.
  - Interior lights are off, including desk/shelf/bubble lamps.
  - The ceiling spherical bubble lamp must remain present and visible as a dark glass sphere hanging from the ceiling, not glowing.
  - The repaired shell door is tightly closed with no gap.
  - The office remains tidy and still.
- Next candidate: `10_candidate_text_v4_fullregen_no_current_lights_off_lamp_visible.png`.

## Page 10 Full Regeneration - No Current / Lights Off / Ceiling Lamp Visible - 2026-06-28

- User rejected local panel replacement direction: text-panel patches looked unnatural; regenerate the whole page instead.
- User also noted the lights-off version removed the ceiling spherical bubble lamp; the lamp must remain visible but switched off.
- Prior page 10 candidates status:
  - `10_candidate_text_v1_night_current_blocked.png`: hold/reject for visible water-current expression and lit interior.
  - `10_candidate_text_v2_no_current_lights_off.png`: visual direction improved, but generated text had a small issue.
  - `10_candidate_text_v2_no_current_lights_off_textfix.png`, `10_candidate_text_v3_no_current_lights_off_textfix.png`, and `10_candidate_text_v2_no_current_lights_off_linefix.png`: hold/reject as local text-panel repair attempts; do not use unless explicitly requested.
- New full-regeneration candidate:
  - `batch_4/10_candidate_text_v4_fullregen_no_current_lights_off_lamp_visible.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0eec0aed046449b2016a413476043c8191b7fbafcc47a2a5e5.png`
  - Dimensions: 1054x1492.
  - SHA256: `264C042F7CA86F42ECCFA42D2B1A49FC05C1E0C27C46B70BA729547A95AC32B4`.
  - QA: no visible water-current ribbons/ripples/bubbles/flow marks; repaired shell door is closed with no visible gap; interior lamps are off; ceiling spherical bubble lamp is present as a dark glass sphere with no glow; tidy desk and objects remain still. Text panel appears readable and close to script.
- Current Batch 4 review set:
  - `batch_4/10_candidate_text_v4_fullregen_no_current_lights_off_lamp_visible.png`
  - `batch_4/11_candidate_text_v1_morning_success.png`
