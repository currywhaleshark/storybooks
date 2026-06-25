# Batch 2 Prompt Plan - 수아의 잘 보는 눈 - 2026-06-25

## Scope

- Batch range: pages 04-07.
- Story movement: outdoor play foreshadowing -> Lulu loses the special hairpin -> Sua observes carefully -> Sua finds it.
- Source: `series/coral-town-daycare/sua-different-is-good/script/main.md`, lines 256-436 in the 2026-06-25 UTF-8 read.
- Note: `series/coral-town-daycare/sua-different-is-good/script/pages.json` currently contains only pages 0-3.

## Shared Batch 2 Reference Checklist

Before each generation, emit or inspect the actual image files that correspond to visible characters, location, and the special hairpin.

Core files:

- Playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Sua no-bag: `series/coral-town-daycare/references/characters/no_bag/수아_no_bag.png`
- Lulu wearing special hairpin for pre-loss pages: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- Lulu no-bag without the special hairpin for post-loss pages: `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
- Special hairpin loose/found prop: `series/coral-town-daycare/images/episodes/수아의_잘_보는_눈/work_2026-06-24/reference_assets/special_coral_hairpin_ref_v1.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Jun-i no-bag: `series/coral-town-daycare/references/characters/no_bag/준이_no_bag.png`
- Aru no-bag: `series/coral-town-daycare/references/characters/no_bag/아루_no_bag.png`
- Mongle no-bag: `series/coral-town-daycare/references/characters/no_bag/몽글이_no_bag.png`

## Page 04 - 마당으로 나가요

### Output Target

`batch_2/04_candidate_text_v1.png`

### Scene Summary

Outdoor play time. Friends rush into the yard for sand play and tag among coral. Lulu is still wearing the special hairpin and plays energetically. Sua remains a little quiet on one side, naturally foreshadowing her observational strength by lowering her head and collecting small shells. Banguli stays near Sua.

### References To Load

- Playground/yard background
- Sua no-bag
- Lulu wearing special hairpin
- Banguli
- Jun-i no-bag
- Aru no-bag
- Mongle no-bag

### Key Locks

- Lulu still wears the special hairpin on page 04. Do not draw it loose yet.
- Sua's looking-down shell-collecting pose is the foreshadowing. Keep it gentle, not gloomy.
- Keep Jun-i, Aru, and Mongle secondary so the scene does not become crowded.
- Mongle tentacles only, no human hands. Aru pufferfish body only, no human feet or hands.
- Keep a clean text area.

### Exact Page Text

```text
바깥놀이 시간이에요.

친구들이
마당으로 우르르.

루루는 신나게
뛰어놀았어요.

수아는 한쪽에서
조용히—

고개를 숙이고
작은 조개를
하나, 둘
모았어요.
```

## Page 05 - 앗, 루루의 산호 장식이!

### Output Target

`batch_2/05_candidate_text_v1.png`

### Scene Summary

The incident. Lulu's cherished special coral hairpin falls while she is playing, rolls over the sand, and disappears into a sand gap. Lulu notices, becomes upset, and friends gather to search. Banguli looks around too.

### References To Load

- Playground/yard background
- Lulu wearing special hairpin for identity and pre-loss continuity
- Lulu no-bag if drawing her after the accessory has fallen
- Special loose hairpin prop
- Banguli
- Jun-i no-bag
- Aru no-bag
- Mongle no-bag

### Key Locks

- The dynamic focus is the special hairpin falling/rolling into sand.
- Do not duplicate the hairpin: only one special hairpin in the scene, either falling/rolling or partly disappearing into sand.
- Lulu should look worried/upset but not scary or melodramatic.
- Keep searching friends secondary and physically distinct.
- Mongle tentacles only, no human hands. Aru pufferfish body only, no human feet or hands.
- Preserve exact Korean text even though the visual prop remains the approved mint/aqua special hairpin.

### Exact Page Text

```text
그때
루루가 놀다가—

톡!

분홍 산호 장식이
또르르 굴러

모래 틈으로
쏙—

"어? 내 산호 장식!"

루루는
울상이 됐어요.

친구들이 찾았지만
보이지 않았어요.
```

## Page 06 - 수아가 가만히 들여다봐요

### Output Target

`batch_2/06_candidate_text_v1.png`

### Scene Summary

Everyone else cannot find the hairpin. Sua quietly comes closer, lowers her head near the sand, and slowly examines the small gaps between grains. Her small eyes begin to shine with focus. Banguli looks with her. Lulu and friends may be in the background watching.

### References To Load

- Playground/yard background
- Sua no-bag
- Banguli
- Lulu no-bag without special hairpin
- Optional secondary friends if visible: Jun-i no-bag, Mongle no-bag, Aru no-bag

### Key Locks

- Sua's concentration is the visual center. This is not a big heroic pose yet; it is quiet attention.
- Keep Sua's eyes small and official, only subtly sparkling with focus.
- Lulu must not wear the special hairpin on page 06.
- Avoid showing the lost hairpin too obviously before page 07 unless it is hidden in sand and not readable as found.
- Keep background friends worried and secondary.

### Exact Page Text

```text
그때 수아가
조용히 다가왔어요.

수아는 고개를
모래 가까이
숙였어요.

작은 눈으로
천천히,
자세히—

모래 틈을
가만히
들여다봤어요.

수아의 눈이
반짝
빛났어요.
```

## Page 07 - 찾았다! 여기 있어!

### Output Target

`batch_2/07_candidate_text_v1.png`

### Scene Summary

Sua finds the special hairpin deep in the sand gap and carefully lifts it. Her mouth opens brightly and her little fin flutters. Friends react with surprise, Lulu brightens, and Banguli pops upward with happy droplets.

### References To Load

- Playground/yard background
- Sua no-bag
- Special loose/found hairpin prop
- Lulu no-bag without special hairpin
- Banguli
- Jun-i no-bag
- Mongle no-bag
- Optional Aru no-bag only if it remains safe and secondary

### Key Locks

- Sua is centered holding the found hairpin carefully.
- Lulu's head is still missing the special hairpin; the found hairpin is in Sua's fin/hand area, not back on Lulu yet.
- Sua is proud and helpful, not transformed into a different body or personality.
- Friend reactions should be varied and distinct, no same-face repetition.
- Keep Mongle tentacles and Aru pufferfish anatomy correct if included.
- Banguli can pop upward happily with two or three droplets.

### Exact Page Text

```text
"여기 있어!"

수아가 모래 틈에서
분홍 산호 장식을
조심스럽게
집어 들었어요.

"우와—!"

친구들이
깜짝 놀랐어요.

루루의 얼굴이
환해졌어요.

"수아야,
정말 고마워!"
```