# Batch 4 Prompt Plan - 토리야, 한 걸음만 - Rework 2026-06-18

## Batch Scope

- Output folder: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_4`
- Pages:
  - `10_candidate_2026-06-19_v1.png`
  - `11_candidate_2026-06-19_v1.png`
  - `12_candidate_2026-06-19_v1.png`
- Workflow:
  - Generate one page at a time.
  - Before each generation, emit the actual reference image files into the conversation with `nodeRepl.emitImage`.
  - Do not generate from local file paths in prompt text alone.
  - Reset or carefully clear active visual context before each page so failed attempts do not contaminate the next page.
  - After generation, copy the latest built-in image from `C:/Users/USER/.codex/generated_images/...` into this folder with the stable candidate filename.

## Approved Continuity Context

- Batch 3 approved pages:
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/07_candidate_2026-06-18_v1.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/08_candidate_2026-06-19_v8_smaller_tunnel_final_retry.png`
  - `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/09_candidate_2026-06-19_v1.png`
- Use approved page 9 as the immediate continuity reference for page 10.
- Use approved page 10 as the immediate continuity reference for page 11 after it is accepted.
- Use approved page 11 as the immediate continuity reference for page 12 after it is accepted.
- Official character and tunnel images remain the visual truth. Approved episode pages are continuity support only.
- Failed, held, or superseded page 8 candidates are process history only and must not be used as visual references.

## Shared Visual Rules

- Format: A5 portrait, about `1:1.414`.
- Style: low-saturation pastel watercolor, warm Coral Town Daycare mood, soft safe toddler picture-book lighting.
- Text workflow: include the exact Korean story text in the first generation pass, with readable spacing and a clean side or upper text area.
- Keep Tori's recovered official design: small dark oval eye with no white sclera, yellow hat with flower, sailor outfit, visible shell, soft matte green watercolor skin, toddler turtle proportions.
- No school bag on Tori during playground/tunnel play.
- Banguli must stay a pale-blue transparent water-drop friend with a simple small face.
- Do not use earlier `final`, `work_2026-06-03`, or `work_2026-06-06` episode images as visual truth.
- No unrelated character substitutions, no fake character duplicates, no human legs or cropped adult body parts, no decorative pseudo-writing, no paraphrased story text.

## Shared Tunnel Locks

- Required tunnel reference: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- The tunnel must remain a single straight, low toddler crawl-through tube.
- Prioritize side-view/crawling-view scale: Tori must lower his head/body to pass.
- Page 10 may show the opposite exit because the script explicitly says Tori comes out the other side.
- Page 11 can show the tunnel in the background or side area, but it must not dominate or become cave-like.
- Page 12 may show both bright sides only if it remains clearly one straight toddler tunnel, not two same-facing entrances or an L-shaped prop.
- Forbidden: L shape, corner bend, side branch, second tunnel, same-facing double openings, cave mound, oversized corridor, dark scary cave.

## Page 10 - 반대편으로 빼꼼!

### Candidate

- Save as: `10_candidate_2026-06-19_v1.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Immediate continuity: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/batch_3/09_candidate_2026-06-19_v1.png`

### Exact Page Text

```text
그리고……

빼꼼!

토리가 반대편으로
나왔어요!

환한 햇살이
토리를 안아 줬어요.

"나왔다!
내가 해냈어!"

토리는 두 손을
번쩍 들었어요.
```

### Prompt

Attach the official references listed above as actual image inputs. Create an A5 portrait Korean children's picture-book page in the same approved pastel watercolor style. Show Tori finally coming out of the far side of the same low straight coral tunnel. Tori's head and upper body peek out of the round exit into bright warm playground light. His mouth is open in delighted surprise and pride, his small dark official eyes are bright, and his front flippers/hands lift up in a small victorious gesture. Banguli floats beside him, smiling brightly, with two or three small bubbles bouncing upward. The tunnel interior behind Tori is softly darker and warm, while the outside is bright and safe. This page may show the opposite exit because Tori is coming out, but keep it as one straight toddler-sized tunnel, not a second separate tunnel or oversized cave. Leave a clean readable text area and render the exact Korean page text verbatim.

### QA Focus

- Tori is emerging from the far side, not still hesitating at the first entrance.
- Tori's joy and achievement are clear.
- Banguli celebrates beside him.
- Tunnel remains one low straight toddler tunnel and does not become a cave or building-sized arch.
- Text is exact and readable enough for review.

## Page 11 - 토리야, 정말 멋져!

### Candidate

- Save as: `11_candidate_2026-06-19_v1.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Juni: `series/coral-town-daycare/references/characters/준이.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Immediate continuity: approved page 10 candidate after user acceptance.

### Exact Page Text

```text
친구들이
우르르 모였어요.

"토리야, 멋져!"
"우와— 해냈다!"

준이가 주먹을 불끈.
루루는 짝짝짝.

토리는 쑥스러워
방긋 웃었어요.

마리 선생님이 말했어요.

"무서운 마음을
안고도 한 걸음 내디뎠지.

그게 진짜
용기란다."
```

### Prompt

Attach the official references listed above as actual image inputs. Create an A5 portrait Korean children's picture-book page in the same approved pastel watercolor style. In the bright Coral Town Daycare playground, Tori stands near the low coral tunnel after coming through. Friends gather warmly around him in a loose semicircle, celebrating without crowding him. Juni makes a cheerful little fist-pump, Lulu claps, Aru bounces happily, and Mongle lifts several arms in celebration. Mari teacher kneels or leans at Tori's eye level with a warm proud expression, speaking gently. Tori smiles shyly but proudly, his official face and small dark eyes preserved. Banguli floats near Tori with a bright smile and a few round bubbles. Keep the tunnel visible as a small low prop in the background or side area, not the main cave-like focus. Leave a clean readable text area and render the exact Korean page text verbatim.

### QA Focus

- Tori is the emotional center and looks shy/proud, not overwhelmed.
- Friends celebrate kindly; no pushing, grabbing, or crowding.
- Mari teacher is warm and eye-level.
- Each friend keeps their official identity; avoid same-face duplicates.
- Tunnel remains small and low if visible.
- Text is exact and readable enough for review.

## Page 12 - 이번엔 토리가 먼저 슝!

### Candidate

- Save as: `12_candidate_2026-06-19_v1.png`

### References To Attach

- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Juni: `series/coral-town-daycare/references/characters/준이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`
- Playground: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Tunnel lock: `series/coral-town-daycare/images/episodes/토리야_한_걸음만/rework_2026-06-18/tunnel_lock/coral_tunnel_straight_tube_lock_candidate_v1.png`
- Immediate continuity: approved page 11 candidate after user acceptance.

### Exact Page Text

```text
며칠 뒤—

이번에는
토리가 먼저
터널로 갔어요.

슝—

더 이상
무섭지 않았어요.

"얘들아, 같이 가자!"

토리가 앞장섰어요.

무서웠던 터널이
이제는
제일 좋아하는
놀이가 됐어요.

산호마을 어린이집은
오늘도 맑음.

토리의 용기도
반짝반짝 맑음.
```

### Prompt

Attach the official references listed above as actual image inputs. Create an A5 portrait Korean children's picture-book finale page in the same approved pastel watercolor style. A few days later, Tori confidently leads the group toward and through the same low straight coral tunnel. He is still gentle and turtle-like, but no longer frozen with fear; his posture is forward, warm, and brave. Friends follow in a joyful line: Juni, Aru, Lulu, Mongle, Sua, and Popo, each keeping their official character design. Mari teacher watches nearby with a proud, calm smile. Banguli travels beside Tori and gives a tiny wink with two or three bubbles. The whole page feels bright, warm, and resolved. The tunnel can show bright light from both ends only if it clearly remains one straight toddler-sized tube; do not make two separate tunnels, same-facing duplicate entrances, an L shape, or a giant cave. Leave generous top text space and render the exact Korean page text verbatim.

### QA Focus

- Tori leads first with calm confidence.
- Friends follow happily and remain visually distinct.
- Mari teacher is proud but not dominating the scene.
- Banguli stays beside Tori and remains official water-drop shape.
- Tunnel remains one low straight toddler crawl-through prop.
- Finale feels bright, safe, and complete.
- Text is exact and readable enough for review.