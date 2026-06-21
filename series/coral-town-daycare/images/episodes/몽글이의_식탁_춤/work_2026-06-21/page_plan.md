# Page Plan - 몽글이의 식탁 춤

## Episode

- Script: `series/coral-town-daycare/docs/episodes/몽글이의_식탁_춤.md`
- Drive source: `https://drive.google.com/file/d/1-X0NirjhHy9w9EqpJYtqmiScTwibZ6UP/view?usp=drivesdk`
- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Work root: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/work_2026-06-21`
- Final folder: `series/coral-town-daycare/images/episodes/몽글이의_식탁_춤/final`
- Page format: A5 portrait, about `1:1.414`
- Text workflow: generate illustration and exact Korean story text together on the first pass. If text fails but art passes, keep the art candidate separate for text repair.

## Script Audit

- Total images: cover + pages 01-12 = 13 images.
- Audience and tone: 3-year-old toddler picture book; warm, non-scolding meal-time manners story.
- Core message: `신나는 건 좋아요. 밥 먹을 땐 잠깐 모아 두고, 다 먹고 실컷 놀아요.`
- Main risk: Mongle's eight legs must read clearly without making the table scene chaotic or unsafe.
- Rulebook conflict to override: the source prompt mentions bags in some indoor character descriptions. The official rulebook says bags are not worn during indoor eating scenes unless specifically required. For this episode, omit body-worn bags in the dining room and yard scenes; if a bag appears, place it on hooks, shelves, cubbies, or beside chairs.

## Locked References

- Rulebook: `series/coral-town-daycare/docs/산호마을_어린이집_이미지_규칙서.md`
- Dining room: `series/coral-town-daycare/references/배경_식당.png`
- Exterior/playground/yard: `series/coral-town-daycare/references/배경_전경과_놀이터.png`
- Coral tunnel for yard continuity if visible: `series/coral-town-daycare/references/locations/산호_터널_레퍼런스.png`
- Mari teacher: `series/coral-town-daycare/references/characters/마리_선생님.png`
- Mongle: `series/coral-town-daycare/references/characters/몽글이.png`
- Banguli: `series/coral-town-daycare/references/characters/방울이.png`
- Jun-i: `series/coral-town-daycare/references/characters/준이.png`
- Aru: `series/coral-town-daycare/references/characters/아루.png`
- Lulu: `series/coral-town-daycare/references/characters/루루.png`
- Sua: `series/coral-town-daycare/references/characters/수아.png`
- Tori: `series/coral-town-daycare/references/characters/토리.png`
- Popo: `series/coral-town-daycare/references/characters/포포.png`

## Character Fidelity Locks

- Mongle must remain the official purple octopus child with eight visible legs, yellow beret, and sailor collar. Do not add human legs or feet. Do not turn the legs into arms only; the eight-leg meal-time behavior is the story core.
- Mari teacher must match the official reference: human upper body, purple mermaid tail, half-up bob, star hairpin, yellow apron, name tag, and warm daycare-teacher posture. No scolding finger or princess-mermaid styling.
- Banguli is a small pale sky-blue transparent droplet with a simple face and tiny companion droplets. It is not a jellyfish, crystal, hard bead, or toy.
- Aru must stay a round orange pufferfish with spikes and fins. Never add human hands, feet, legs, or a separate human torso.
- Lulu and Sua must keep their seahorse silhouettes, long tube snouts, curled tails, small fins, head ridges, and official clothing details.
- Popo must keep the translucent moon-jelly dome, subtle inner pattern, soft tentacles, and small sailor collar. Eyes stay hidden or barely visible unless the page explicitly needs a tiny expression.
- Jun-i and Tori are supporting friends; preserve their official species structures if shown.

## Continuity Locks

- Pages 00-10 are dining-room continuity. Use the official dining-room background and keep tableware consistent: shell table, shell plates, soup bowl, water cup, small side dishes.
- Pages 04-06 show a small spill. It must be cute and safe: no injuries, no scary splash, no dirty or gross food mess.
- Pages 07-09 are the learning/practice sequence: Mongle's energy is accepted first, then he learns when to gather his legs.
- Pages 11-12 move to the bright yard/playground where Mongle can dance freely.
- All pages need clean text space that does not cover faces, key leg positions, or the spill.
- Do not use prior generated episode images as visual truth. Use only official references and this script.

## Batch Split

### Batch 1

- `00_표지.png`: Mongle sits at the shell table with eight excited legs; Banguli floats nearby.
- `01_페이지.png`: lunchtime begins; Mongle enters the dining room with excited legs.
- `02_페이지.png`: Mongle struggles to sit still; one leg rises toward the table.
- `03_페이지.png`: Mongle plays with rice balls and seaweed soup; food becomes a toy.

### Batch 2

- `04_페이지.png`: Mongle bumps the soup bowl; a small safe spill happens.
- `05_페이지.png`: everyone pauses; Mari checks whether anyone is hurt.
- `06_페이지.png`: Mari and Mongle clean together; friends help.

### Batch 3

- `07_페이지.png`: Mari names Mongle's lively energy as good.
- `08_페이지.png`: Mari teaches that legs gather during meals, then dance after eating.
- `09_페이지.png`: Mongle eats calmly with legs gathered.

### Batch 4

- `10_페이지.png`: meal is finished; children prepare to go to the yard.
- `11_페이지.png`: Mongle dances freely with eight legs in the yard.
- `12_페이지.png`: warm ending; Mongle understands the right time for energy.

## Page Targets

### 00 - 표지

- Output: `00_표지.png`
- Scene: warm dining room; Mongle seated at a shell table, eight legs happily wiggling, Banguli nearby.
- References: dining room, Mongle, Banguli.
- Exact text:

```text
몽글이의 식탁 춤

— 밥 먹을 땐
다리를 가지런히 —
```

### 01 - 다리가 여덟 개나 신났어요

- Output: `01_페이지.png`
- Scene: lunchtime begins; friends gather in the dining room; Mongle enters with lively eight-leg motion.
- References: dining room, Mongle, Mari, Banguli, Jun-i, Aru, Lulu, Sua, Tori, Popo.
- Exact text:

```text
점심 시간이에요.

오늘은 따뜻한 미역국과
동글동글 주먹밥!

몽글이는
다리가 여덟 개나
신났어요.

통통! 통통!

"맛있겠다—!"

다리들이
꼬물꼬물
춤을 췄어요.
```

### 02 - 가만히 앉기가 힘들어요

- Output: `02_페이지.png`
- Scene: children eat calmly; Mongle's legs tap, rise, and wiggle because he is excited.
- References: dining room, Mongle, Banguli, visible nearby friends.
- Exact text:

```text
다들 자리에 앉아
냠냠 먹기 시작했어요.

그런데 몽글이는……

가만히 앉아 있기가
힘들었어요.

한 다리는 식탁 위로
슬쩍—

한 다리는 의자를
톡톡톡—

엉덩이가
들썩들썩.

"히히, 신난다!"
```

### 03 - 주먹밥으로 통통통

- Output: `03_페이지.png`
- Scene: Mongle rolls a rice ball and stirs soup playfully; friends notice; Mari starts approaching.
- References: dining room, Mongle, Mari, Banguli, Aru, Sua.
- Exact text:

```text
몽글이는
밥을 먹는 대신—

주먹밥을 통통통
굴리고,

미역국을 휘휘
저었어요.

"이건 공놀이!
이건 빙글빙글!"

국물이 찰랑찰랑.
주먹밥이 데구르르.

친구들이
"어어—" 했어요.
```

### 04 - 앗! 국그릇이 휘청

- Output: `04_페이지.png`
- Scene: Mongle stands suddenly and one leg bumps the soup bowl; small safe spill.
- References: dining room, Mongle, Banguli, Aru or Sua.
- Exact text:

```text
그러다
몽글이가

의자에서
벌떡—!

그때
한 다리가

국그릇을
툭!

앗!

미역국이
주르륵—

물컵도
톡!

식당이
조용해졌어요.
```

### 05 - 모두 깜짝, 즐거움이 멈췄어요

- Output: `05_페이지.png`
- Scene: the room pauses; Mongle shrinks inward; Mari checks safety first.
- References: dining room, Mongle, Mari, Banguli, Jun-i, Aru, Sua, Tori.
- Exact text:

```text
친구들이 모두
동작을 멈췄어요.

까르르 웃던 식당이
조용—

몽글이의 다리가
움츠러들었어요.

"어……
내가 너무
신났나……?"

마리 선생님이
다가왔어요.

"다친 사람
없니?"
```

### 06 - 괜찮아, 같이 닦자

- Output: `06_페이지.png`
- Scene: Mari and Mongle clean the table together; friends help gently.
- References: dining room, Mongle, Mari, Banguli, Jun-i or Lulu.
- Exact text:

```text
마리 선생님은
혼내지 않았어요.

"괜찮아.
쏟을 수도 있지.

같이 닦을까?"

몽글이는
다리 하나하나로

식탁을
야무지게 닦았어요.

쓱쓱, 싹싹.

친구들도
같이 거들었어요.
```

### 07 - 다리에 신나는 기운이 가득해

- Output: `07_페이지.png`
- Scene: Mari sits at Mongle's eye level and names his energy kindly.
- References: dining room, Mongle, Mari, Banguli.
- Exact text:

```text
마리 선생님이
몽글이 옆에 앉았어요.

"몽글이 다리에
신나는 기운이
가득하구나."

"그건 정말
좋은 거야."

몽글이는 자기 다리를
내려다봤어요.

여덟 다리가
여전히 꼬물꼬물.

"신난 게……
잘못은 아니에요?"

"그럼!"
```

### 08 - 밥 먹을 땐 다리를 가지런히

- Output: `08_페이지.png`
- Scene: Mari demonstrates gathering; Mongle gathers eight legs below the chair.
- References: dining room, Mongle, Mari, Banguli.
- Exact text:

```text
"신나는 건
정말 좋아.

그런데 밥 먹을 땐—"

마리 선생님이
두 손을 모았어요.

"다리를 잠깐
가지런히 모아 두는 거야.

그리고 다 먹고 나서
실컷 춤추자!"

몽글이는
여덟 다리를

의자 아래로
가지런히—

"오……
이렇게요?"
```

### 09 - 냠냠, 끝까지 맛있게

- Output: `09_페이지.png`
- Scene: Mongle eats calmly, using one leg while the other legs stay gathered.
- References: dining room, Mongle, Mari, Banguli, Jun-i, Aru, Sua.
- Exact text:

```text
몽글이는
한 다리로

주먹밥을
콩—

미역국도
한 입,
또 한 입.

다리들은
얌전히 아래로.

이번엔
쏟아지지 않았어요.

"얌전히 먹어도
맛있다!"
```

### 10 - 다 먹었다! 이제 놀러 가자

- Output: `10_페이지.png`
- Scene: Mongle finishes the meal and the class prepares to go to the yard.
- References: dining room, Mongle, Mari, Banguli, Jun-i, Lulu.
- Exact text:

```text
몽글이는
그릇을 싹—

깨끗이
다 먹었어요!

"다 먹었다!"

마리 선생님이
말했어요.

"다 먹은 친구는
마당에 나가
놀까?"

몽글이의 다리가
다시 꼬물꼬물!

"이제
놀 시간이다—!"
```

### 11 - 마당에서 여덟 다리로 춤을!

- Output: `11_페이지.png`
- Scene: bright yard; Mongle freely dances with eight legs while friends join.
- References: playground/yard, coral tunnel if visible, Mongle, Mari, Banguli, Jun-i, Aru, Lulu, Sua, Tori, Popo.
- Exact text:

```text
마당에 나오자—

몽글이는
여덟 다리를
활짝!

빙글빙글!
폴짝폴짝!

여기서는
마음껏 신나도 돼요.

"이게 진짜
식탁 춤이 아니라—

마당 춤이다!"

친구들도 다 같이
빙글빙글.
```

### 12 - 신나는 건 신나는 때에

- Output: `12_페이지.png`
- Scene: warm ending in the yard; Mongle smiles with friends.
- References: playground/yard, Mongle, Mari, Banguli, Jun-i, Aru, Lulu, Sua, Tori, Popo.
- Exact text:

```text
몽글이가
환하게 웃었어요.

"밥 먹을 땐
다리를 가지런히.

놀 땐
신나게!"

"신나는 건
신나는 때에 하면

더 신나요!"

산호마을 어린이집은
오늘도 맑음.

몽글이의 식탁도,
몽글이의 마당 춤도
반짝반짝 맑음.
```
