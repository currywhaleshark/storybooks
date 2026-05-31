# Batch 3 Prompt Plan - 광장에 떨어진 알록달록한 것

## Scope

- Episode: 광장에 떨어진 알록달록한 것
- Batch: pages 8-11
- Work folder: `series/sherlock-fin-deep-city/images/episodes/광장에_떨어진_알록달록한_것/work_2026-05-31/batch_3`
- Candidate filenames:
  - `08_candidate_text_v1.png`
  - `09_candidate_text_v1.png`
  - `10_candidate_text_v1.png`
  - `11_candidate_text_v1.png`

## Official References

- Sherlock Fin: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- Friends:
  - `series/sherlock-fin-deep-city/references/characters/펄리.png`
  - `series/sherlock-fin-deep-city/references/characters/크랩슨.png`
  - `series/sherlock-fin-deep-city/references/characters/팝팝.png`
  - `series/sherlock-fin-deep-city/references/characters/모모.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- Prop: `series/sherlock-fin-deep-city/references/props/알록달록한_우산_레퍼런스.png`

## Shared Locks

- A5 portrait page proportion.
- Render Korean story text in the image, using a cream rounded story panel with warm dashed border.
- Preserve official character identities and the recurring umbrella prop.
- Avoid random signage, pseudo-writing, watermark, and unrelated prior-episode details.
- Page 8 has board labels as part of the scene; keep board labels short and readable.

## Page Prompt Records

### 08 Page 8

- Scene prompt: Sherlock Fin points to a two-column deduction board in the plaza or detective office corner. Left column title: `알아낸 것`. Right column title: `아직 모르는 것`. Left column has simple icons for handle, folding/opening, and roof/protection. Right column has one big question mark. Friends watch.
- Required story text:

```text
단서를 하나로 모아 보자.

손에 들고 다녀요.
접었다 폈다 해요.
펴면 위를 막아줘요.

‘이만큼은 알아냈어!’

그런데······
한 가지 질문이 남았어요.

‘위에서······ 뭐가 내려오는데?’
```

### 09 Page 9

- Scene prompt: The friends and Sherlock Fin look upward in the plaza. Above them is only blue water and sparkling star-sand, nothing falling. Sherlock Fin has an honest expression and lightly lifts or touches his hat.
- Required story text:

```text
친구들은 위를 올려다보았어요.

그런데 바닷속 위에는
파란 물과 별모래뿐,

아무것도 내려오지 않았어요.

셜록 핀이 말했어요.

’이건······ 나도 모르겠어.

윗세상에는
우리가 모르는 무언가가
있나 봐!’
```

### 10 Page 10

- Scene prompt: Sherlock Fin warmly smiles and talks to the friends in the plaza. Friends' expressions change from puzzled to bright smiles. Umbrella can stand nearby as a clue object.
- Required story text:

```text
셜록 핀이 환하게 웃었어요.

’모든 걸 다 알 수는 없어.

그래도 봐,
우리는 이만큼이나 알아냈잖아!

손에 들고,
접었다 폈다 하고,
위를 막아주는 물건!

모르는 건······
앞으로 알아가면 되지!’
```

### 11 Page 11

- Scene prompt: Final warm scene. Friends set the umbrella upright at one side of the plaza and sit in a circle under it. The umbrella becomes a cozy shelter. Warm light glows under the canopy; blue water and star-sand sparkle above. Everyone peacefully imagines the upper world.
- Required story text:

```text
친구들은 우산을 세웠어요.

그 아래 둥글게 모여 앉으니
아늑한 쉼터가 되었어요.

‘윗세상 어딘가에
이 물건의 주인이 있겠지?’

세상에는
우리가 아직 모르는 것이
가득해요.

그건 무서운 게 아니라
설레는 일이에요.

꼬마 탐정단,
오늘도 성공!
```

## Batch 3 QA Notes

- `08_candidate_text_v1.png`: hold. It included rain/drop-like marks on the known-facts board, which weakens the "still unknown" logic.
- `08_candidate_text_v2.png`: pass with text caution. Board logic is corrected; no rain answer is shown. Text punctuation glyphs are not exact.
- `09_candidate_text_v1.png`: pass with text caution. Upward-looking scene and "nothing falls" logic are clear. Text punctuation glyphs are not exact.
- `10_candidate_text_v1.png`: pass with text caution. Warm reassurance scene works. Text punctuation glyphs are not exact.
- `11_candidate_text_v1.png`: pass. Cozy ending under the umbrella reads well; text is readable and matches the ending content.

Use `08_candidate_text_v2.png` for any later final pass, not `08_candidate_text_v1.png`.
