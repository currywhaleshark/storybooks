# Batch 2 Prompt Plan - 2026-06-08

## Scope

- Episode: `루루야, 약속했잖아`
- Script: `series/coral-town-daycare/docs/episodes/루루야_약속했잖아.md`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Page plan: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/page_plan.md`
- Worklog: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/episode_worklog.md`
- Work folder: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/batch_2`
- Batch 2 scope: `04_페이지.png` through `06_페이지.png`
- Candidate filenames: `04_candidate_text_v1.png`, `05_candidate_text_v1.png`, `06_candidate_text_v1.png`

## Approved Prior Batch

- User approved batch 1 on 2026-06-08.
- Final-promoted files:
  - `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final/00_표지.png`
  - `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final/01_페이지.png`
  - `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final/02_페이지.png`
  - `series/coral-town-daycare/images/episodes/루루야_약속했잖아/final/03_페이지.png`
- Do not use failed/held candidates as visual references. Official character/location references remain the source of truth.

## Official References To Attach

- Classroom: `series/coral-town-daycare/references/배경_교실.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Favorite picture book prop: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`
- Messy art-time state: `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/messy_art_time_state_ref.png`

## Preflight

- `messy_art_time_state_ref.png` is required for pages 5 and 6, but is not currently present in this workspace as of this handoff.
- First concrete action in the next thread: restore or regenerate `messy_art_time_state_ref.png` using `reference_assets/reference_asset_plan.md`, then inspect it before page 05 generation.
- Page 04 can be generated before the messy reference if needed, because it depends on Lulu, Jun-i, Banguli, Mari teacher, classroom, and the picture book prop.

## Shared Hard Locks

- A5 portrait page proportion, about `1:1.414`.
- Generate illustration and exact Korean story text together on the first pass.
- Use actual reference image files as visual truth.
- Preserve official-reference silhouettes over extra cuteness; do not over-round characters.
- No worn bags in indoor classroom scenes. If bags appear, place them only in muted storage/background.
- Keep the delicate watercolor/colored-pencil reference style. Avoid plastic 3D texture, neon, dense clutter, extra signs, pseudo-writing, and unrelated prior-episode details.
- If exact Korean text cannot be rendered cleanly, leave a clean blank text area instead of inventing wrong Korean.
- Keep conflict gentle. No yelling, harsh anger, blame, or scary expressions.

## Page 04 - 약속은 지키는 거야

### Output

`04_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/준이.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/lulu_favorite_picture_book_ref.png`

### Exact Page Text

```text
루루가 준이에게
다가갔어요.

"준이야,
약속했잖아.

약속은
지키는 거야."

"아, 맞다!
미안해, 루루."

준이가 얼른
그림책을 가져다줬어요.

루루는 마음이
조금 풀렸어요.
```

### Prompt Focus

- Lulu approaches Jun-i and clearly says promises are meant to be kept.
- Lulu is firm but not angry; no shouting.
- Jun-i remembers, looks sorry, and returns the favorite picture book.
- The book handoff/return gesture is visible.
- Banguli nods nearby.
- Mari teacher watches gently from farther away.
- Medium shot of Lulu and Jun-i facing each other, with one clean text area.

## Page 05 - 신나는 미술 놀이

### Output

`05_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/messy_art_time_state_ref.png`

### Exact Page Text

```text
오후에는
미술 놀이!

색종이 오리고,
물감 칠하고,
조개도 붙이고.

"이것도!"
"저것도!"
"반짝이도 조금만!"

루루가 제일
신났어요.

색종이가 여기저기.
붓도 여기저기.

마리 선생님이
물었어요.

"다 놀고 나면
누가 정리할까?"
```

### Prompt Focus

- Wide lively classroom art-corner scene.
- Lulu is the most excited, chattering and fluttering.
- Mongle and Aru join art play while preserving their reference silhouettes.
- Safe art mess: color paper, brushes, round paint pots, coral-powder paint, shell decorations, small safe craft pieces.
- The mess should be clearly growing, but leave child walkable space.
- Mari teacher approaches and asks gently.
- Banguli floats nearby.

## Page 06 - 내가 할게요! 내가!

### Output

`06_candidate_text_v1.png`

### References To Attach

- `series/coral-town-daycare/references/characters/루루.png`
- `series/coral-town-daycare/references/characters/방울이.png`
- `series/coral-town-daycare/references/characters/마리_선생님.png`
- `series/coral-town-daycare/references/characters/몽글이.png`
- `series/coral-town-daycare/references/characters/아루.png`
- `series/coral-town-daycare/references/배경_교실.png`
- `series/coral-town-daycare/images/episodes/루루야_약속했잖아/work_2026-06-07/reference_assets/messy_art_time_state_ref.png`

### Exact Page Text

```text
루루가 손을
번쩍 들었어요.

"내가 할게요!
내가 정리할게요!"

"색종이도!
붓도!
조개도!
반짝이도 전부 다요!"

재잘재잘.
빠르게.

마리 선생님이
방긋 웃었어요.

"그래,
루루가 약속했네."
```

### Prompt Focus

- Lulu is centered, raising a fin/hand brightly and promising too quickly.
- The tone is cheerful but slightly lightweight: she is excited and not thinking deeply.
- Mari teacher smiles warmly and confirms the promise, not scolding.
- Banguli nods but tilts slightly with a subtle puzzled reaction.
- Friends keep playing in the background.
- Use the same art mess identity from page 05.

## Batch 2 QA Checklist

- Exact Korean text or intentionally blank text area.
- A5 portrait ratio.
- No worn bags.
- Lulu reference fidelity: head ridge, bead tips, dotted texture, snout, head ornament, sailor outfit, translucent fin, curled tail.
- Jun-i on page 04 keeps shark body, white belly, fins, tail, small teeth, and avoids human-like legs/feet.
- Aru on pages 05-06 remains one true pufferfish body with scarf only; no human torso/limbs.
- Mongle on pages 05-06 keeps octopus body, eight legs, yellow beret, sailor collar.
- Mari teacher keeps mermaid teacher structure, yellow apron, star hairpin, gentle expression.
- Banguli stays a soft transparent droplet.
- Art mess is safe and readable, not dangerous or chaotic.
- Page 05 and 06 art mess continuity matches.
- No previous episode contamination.
