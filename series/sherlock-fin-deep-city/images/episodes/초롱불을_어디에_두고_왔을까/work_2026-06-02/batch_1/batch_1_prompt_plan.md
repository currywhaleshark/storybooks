# Batch 1 Prompt Plan - 초롱불을 어디에 두고 왔을까

## Scope

- Episode: `초롱불을 어디에 두고 왔을까`
- Batch: cover + pages 1-3
- Work folder: `series/sherlock-fin-deep-city/images/episodes/초롱불을_어디에_두고_왔을까/work_2026-06-02/batch_1`
- Candidate filenames:
  - `00_candidate_text_v1.png`
  - `01_candidate_text_v1.png`
  - `02_candidate_text_v1.png`
  - `03_candidate_text_v1.png`

## Official References

Use the actual image files as visual truth.

- Characters:
  - `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - `series/sherlock-fin-deep-city/references/characters/초롱불을_어디에_두고_왔을까_초롱이_레퍼런스.png`
- Props:
  - `series/sherlock-fin-deep-city/references/props/초롱불을_어디에_두고_왔을까_불씨구슬_레퍼런스.png`
- Background and style:
  - `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
  - `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`

## Shared Visual Rules

- A5 portrait page proportion, about `1:1.414`, for all cover and interior page candidates.
- Include the approved Korean page text directly in the image from the first generation pass.
- Use one clean cream or shell-light text panel with rounded corners, thin border, and generous margins, following the text layout reference.
- Keep the Sherlock Fin series style: bright warm underwater Deep City, coral buildings, shell doors, bubble streetlamps, gentle neon, warm window lights, no horror.
- Evening darkness must feel cozy and safe, not scary.
- Chorong must follow the approved reference: round dark-blue baby anglerfish body, big eyes, teal/gold fins, head lantern shape. Tiny cute teeth are allowed only if harmless; do not enlarge the mouth or make teeth sharp.
- Chorong's lantern state must be clear:
  - Cover/page 2/page 3: lantern empty or dark.
  - Page 1: lantern glowing warm yellow-gold with bead inside.
- Sherlock Fin must follow the official sheet: teal hair, brown detective hat and coat, teal mermaid tail, black gloves, yellow magnifying glass or small notebook as the scene requires.
- Avoid extra signage, pseudo-writing, invented labels, speech bubbles outside the approved text, watermarks, unrelated prior-episode details, and over-glossy neon drift.

## Page Prompt Records

### 00 Cover

- Candidate: `00_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, Deep City, flame bead, layout.
- Scene prompt: Evening Deep City. Chorong stands beside Sherlock Fin with Chorong's head lantern dark and empty. Chorong looks slightly tearful but cute and safe. Sherlock Fin gently looks at Chorong while holding a small notebook. Cozy coral alley, warm windows, bubble streetlamps, deep blue-violet evening. A tiny warm hint of the flame bead may sparkle subtly at one side, but do not reveal it as the answer too strongly.
- Text:

```text
심해탐정 셜록 핀

초롱불을 어디에 두고 왔을까
```

### 01 Page 1

- Candidate: `01_candidate_text_v1.png`
- Required references: Chorong, Deep City, flame bead inside lantern, layout.
- Scene prompt: Daytime Deep City wide establishing view. Chorong swims happily with the head lantern glowing warm yellow-gold. Coral alley, jazz plaza, and seaweed forest entrance are visible far in the background, showing Chorong's busy happy day. Chorong's expression is bright and happy. Text panel in lower left.
- Text:

```text
딥시티에 작은 친구가 살아요.

초롱이예요.

머리 위 초롱이
반짝반짝 환하게 빛나요.

오늘 초롱이는
이곳저곳 신나게 다녔어요.

정말 즐거운 하루였어요!
```

### 02 Page 2

- Candidate: `02_candidate_text_v1.png`
- Required references: Chorong, Deep City, empty lantern, layout.
- Scene prompt: Evening coral alley. Chorong stops with the head lantern dark and empty. The surrounding alley is gently getting darker, with warm windows and bubble streetlamps turning on. Chorong looks up at the lantern with teary worried eyes. Close medium shot. Text panel in upper right.
- Text:

```text
그런데 저녁이 되자······

초롱이의 초롱불이
켜지지 않았어요.

초롱 안이 텅 비어 있었어요.

'불씨 구슬이 없어졌어!

어디에 두고 왔는지
기억이 안 나······'

초롱이는 눈물이 났어요.
```

### 03 Page 3

- Candidate: `03_candidate_text_v1.png`
- Required references: Sherlock Fin, Chorong, detective office interior, empty lantern, layout.
- Scene prompt: Sherlock Fin's detective office. Chorong stands in front of Sherlock Fin and tearfully explains what happened. Chorong's lantern is dark/empty. Sherlock Fin sits or floats calmly with a kind listening expression, detective hat and coat, small notebook on desk. Warm bubble lamp, shell desk, clue board, cozy office. Medium shot showing the room. Text panel in lower right.
- Text:

```text
초롱이는 셜록 핀에게 갔어요.

'오늘 너무 여러 곳을 다녀서
어디서 두고 왔는지 모르겠어요.

곧 어두워지는데······'

셜록 핀이 모자를 살짝 눌러썼어요.

'괜찮아. 같이 찾아보자.'
```

## QA Checklist

- [x] Text is included in each image.
- [x] Chorong follows the official reference and lantern state is correct.
- [x] Sherlock Fin follows the official reference on cover and page 3.
- [x] Page 1 is bright daytime and shows glowing lantern.
- [x] Page 2 is safe evening, not scary, and shows empty/dark lantern.
- [x] Page 3 uses the detective office reference and shows gentle listening.
- [ ] No unrelated prior-episode content, random signage, pseudo-writing, or answer reveal.

## Batch 1 QA Notes

| Candidate | Status | QA notes |
| --- | --- | --- |
| `00_candidate_text_v1.png` | Candidate pass with caution | Flame bead is visible near the bottom and may reveal the answer more strongly than intended. |
| `01_candidate_text_v1.png` | Candidate pass with caution | Background includes readable English signage; otherwise the day/glowing-lantern logic is strong. |
| `02_candidate_text_v1.png` | Candidate pass | Dark lantern and worried-but-safe Chorong read clearly. |
| `03_candidate_text_v1.png` | Candidate pass with text caution | Text is readable but slightly normalized/paraphrased against exact script punctuation and line breaks. |

## Mobile Review

- Google Doc review link:
  - `https://docs.google.com/document/d/1_r_49N-0KUMc1w57IuoA7S8zBaH-k360ItkB4nro7Aw`
