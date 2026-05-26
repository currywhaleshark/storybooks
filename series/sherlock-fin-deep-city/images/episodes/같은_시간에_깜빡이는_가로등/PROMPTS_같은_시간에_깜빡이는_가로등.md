# PROMPTS - 같은 시간에 깜빡이는 가로등

## 공통 프롬프트

Use case: illustration-story  
Asset type: children's picture-book page with Korean text panel  
Series: 『심해탐정 셜록 핀』  
Page ratio: vertical A5 portrait, 148:210, about 1:1.414  
Style/medium: warm children's picture-book illustration, cute rounded animation-inspired characters, painterly clean finish, not photorealistic, not scary  
Scene world: bright neon jazz underwater city Deep City, coral buildings, shell doors, bubble streetlamps, water bubbles, warm window lights  
Palette: deep blue, cobalt, violet, emerald, pink, gold, warm cream text panels  
Text panel: use the official shell-cream text box style with rounded corners, thin border, generous padding, readable Korean text  
Constraints: preserve official character identities from reference sheets; keep pages vertical A5 portrait; no random English; no watermark; no unrelated previous-episode objects; no frightening deep sea mood  
Pop Pop constraint: Pop Pop is a round yellow pufferfish. Never give Pop Pop arms, hands, fingers, human-like limbs, or extra front/chest fins. Only small natural side fins and a small tail fin are allowed.
Composition note: if a page description says wide shot or wide middle shot, reinterpret it as a spacious vertical A5 scene using foreground/midground/background depth rather than a horizontal canvas.

Official reference roles:

- `references/characters/셜록핀.png`: character identity reference for Sherlock Fin.
- `references/characters/팝팝.png`: character identity reference for Pop Pop.
- `references/characters/모모.png`: character identity reference for Momo.
- `references/characters/크랩슨.png`: character identity reference for Crabson.
- `references/characters/펄리.png`: character identity reference for Pearly.
- `references/심해탐정_셜록핀_딥시티_레퍼런스.png`: Deep City and jazz plaza background style.
- `references/layouts/텍스트박스_레이아웃_레퍼런스.png`: Korean text panel layout.

## 신규 레퍼런스 1 - 빵집 주인

Save as:

`series/sherlock-fin-deep-city/references/characters/같은_시간에_깜빡이는_가로등_빵집_주인_레퍼런스.png`

Status: generated at 1054x1492, matching vertical A5 ratio.

Prompt:

Create an official character reference sheet for the new baker character in 『심해탐정 셜록 핀』. The baker is a round, soft, pink sea sponge creature, cute and plush, with a large white chef hat, a small apron, warm smiling eyes, chubby hands with a little flour on them. Show front view, 3/4 view, side view, back view, and several expressions: surprised, gentle smile, apologetic, delighted. Children's picture-book illustration style, rounded friendly shapes, warm Deep City palette, clean white or pale cream background, no story scene, no text except a tiny Korean label "빵집 주인" if text is reliable.

## 신규 레퍼런스 2 - 버블 베이커리

Save as:

`series/sherlock-fin-deep-city/references/locations/같은_시간에_깜빡이는_가로등_버블_베이커리_레퍼런스.png`

Status: generated at 1054x1492, matching vertical A5 ratio.

Prompt:

Create an official location reference sheet for "버블 베이커리", a tiny bakery in Deep City's jazz plaza. The bakery is a round bubble-shaped coral building with a cute bread-shaped hanging sign, shell door, warm pink window light, display shelves of underwater bread, and a large oven inside. Show both exterior and interior. Include a simple cutaway showing that one bubble streetlamp outside shares the same coral wall with the bakery oven behind it. Warm, cozy, non-scary underwater jazz city mood, children's picture-book illustration, no random English, no watermark.

## 00 표지

Save as `00_표지.png`.

Scene: 재즈 광장 한쪽 벤치. 팝팝이 헤드폰을 끼고 벤치에 앉아 있고, 그 옆에 셜록 핀이 작은 수첩을 들고 함께 앉아 있다. 두 친구 머리 위로 노란 음표 세 개가 둥둥 떠 있고, 그 너머 광장에 버블 가로등 하나가 살짝 깜빡이는 표현이 있다. 멀리 버블 베이커리의 둥근 거품 모양 지붕이 보인다.  
Composition: 광장 한쪽을 비스듬히 보여주는 와이드 샷, 화면 위쪽에 제목 자리.  
Text:

```text
심해탐정 셜록 핀

같은 시간에 깜빡이는 가로등
```

## 01 페이지

Save as `01_페이지.png`.

Scene: 딥시티의 재즈 광장. 광장 한쪽 작은 벤치에 팝팝이 헤드폰을 끼고 평화로운 오후를 즐긴다. 버블 가로등 여러 개가 부드럽게 켜져 있고, 한쪽에는 버블 베이커리에서 따뜻한 분홍빛이 새어 나온다.  
Composition: 광장 전체를 보여주는 따뜻한 도입 전경, 텍스트 여백은 왼쪽 아래.  
Text:

```text
딥시티에
포근한 오후가 왔어요.

팝팝은 매일 같은 시간에
이 벤치에 앉아요.

좋아하는 라디오 방송이
시작되는 시간이거든요.

'오늘도 행복한 시간!'
```

## 02 페이지

Save as `02_페이지.png`.

Scene: 월요일. 광장 벤치에서 팝팝이 헤드폰을 끼고 앉아 있다. 헤드폰에서 노란 음표 세 개가 떠오르고, 같은 순간 버블 가로등 하나가 `깜빡!` 한다. 물빛은 푸르스름하고, 분홍 별모래가 살짝 떠다니며, 멀리 작은 물고기 떼가 지나간다.  
Composition: 벤치와 깜빡이는 가로등을 함께 담는 중간샷. 03, 04와 거의 같은 구도. 텍스트 여백은 오른쪽 위.  
Text:

```text
음악이 시작되었어요.

도—

그때였어요.

저쪽 가로등 하나가
깜빡! 했어요.

'어? 가로등이 왜?'

팝팝은 고개를 갸웃했어요.
```

## 03 페이지

Save as `03_페이지.png`.

Scene: 화요일. 02와 같은 벤치, 같은 자세의 팝팝, 같은 노란 음표 세 개, 같은 가로등 깜빡임. 물빛은 에메랄드빛, 보라 거품이 동동, 멀리 해파리 한 마리.  
Composition: 02와 거의 같은 구도. 텍스트 여백은 오른쪽 위.  
Text:

```text
다음 날.

같은 시간,
같은 벤치,
같은 음악.

도—

또 깜빡!

'어? 어제도 그랬는데?'

팝팝의 눈이 더 동그래졌어요.
```

## 04 페이지

Save as `04_페이지.png`.

Scene: 수요일. 02, 03과 같은 반복 구도. 팝팝은 깨달은 듯 입을 작게 벌리고, 작은 깨달음 별이 머리 위에 있다. 물빛은 살짝 보랏빛, 황금색 반짝임, 멀리 작은 거북이.  
Composition: 02, 03과 거의 같은 구도. 텍스트 여백은 오른쪽 위.  
Text:

```text
또 다음 날.

같은 시간,
같은 벤치,
같은 음악.

도—

또또 깜빡!

'세 번이나 같은 일이 일어났어!
이건······ 우연이 아닌 것 같아!'
```

## 05 페이지

Save as `05_페이지.png`.

Scene: 셜록 핀의 탐정 사무소. 팝팝이 헤드폰을 한 손에 들고 진지하게 의뢰한다. 셜록 핀은 모자를 매만지며 듣고, 추리 칠판은 아직 비어 있다.  
Composition: 사무소 안을 한눈에 보는 중간샷, 텍스트 여백은 오른쪽 아래.  
Text:

```text
팝팝은 셜록 핀에게 달려갔어요.

'셜록 핀, 이상한 일이 있어요.

매일 같은 시간에
가로등이 깜빡여요.

세 번이나요!'

셜록 핀이 모자를 살짝 눌러썼어요.

'세 번이나? 그건······
우연이 아닐 수 있어.

같이 알아보자!'
```

## 06 페이지

Save as `06_페이지.png`.

Scene: 탐정 사무소 안. 셜록 핀이 수첩에 월요일, 화요일, 수요일 세 칸을 그리고 각 칸마다 노란 음표 세 개와 가로등 깜빡임 그림을 정리한다. 팝팝이 옆에서 진지하게 본다.  
Composition: 수첩을 함께 들여다보는 위에서 살짝 내려다보는 시점, 텍스트 여백은 위쪽.  
Text:

```text
먼저 잘 정리해 보자.

월요일, 음악이 시작될 때 깜빡.
화요일, 음악이 시작될 때 깜빡.
수요일, 음악이 시작될 때 깜빡.

'세 번 모두 같은 시간이야!'

라디오 방송은 매일
정해진 시간에 시작되니까,

깜빡이는 시간도
매일 같은 시간이야.

첫 번째 단서를 찾았어요.
```

## 07 페이지

Save as `07_페이지.png`.

Scene: 광장 곳곳. 셜록 핀이 수첩을 들고 모모와 크랩슨에게 묻는다. 모모 말풍선에는 미역잎이 살짝 떨리는 그림, 크랩슨 말풍선에는 색소폰 받침대가 잠깐 흔들리는 그림. 두 말풍선 위에는 같은 노란 음표 세 개.  
Composition: 두 탐문 장면을 옆으로 길게 담는 와이드 중간샷, 텍스트 여백은 왼쪽 아래.  
Text:

```text
이번에는 잘 들어 보자.

모모가 말했어요.
'그 시간쯤에
미역 숲 잎이 살짝 떨렸어요.'

크랩슨도 말했어요.
'그 시간에 색소폰 받침대가
잠깐 흔들렸어요.'

'어? 가로등만이 아니구나.

광장 여기저기에서
같은 시간에 작은 흔들림이
함께 일어나고 있어!'

두 번째 단서를 찾았어요.
```

## 08 페이지

Save as `08_페이지.png`.

Scene: 다음 날 같은 시간의 광장 벤치. 셜록 핀이 팝팝 옆에 앉아 헤드폰 한쪽을 나눠 끼고 있다. 노란 음표 세 개, 가로등 깜빡임, 동시에 버블 베이커리 창문에서 따뜻한 분홍빛과 빵 냄새가 퍼지고 큰 오븐이 켜지는 모습이 보인다.  
Composition: 벤치의 두 친구와 빵집 창문을 한 화면에 담는 와이드 중간샷, 텍스트 여백은 위쪽.  
Text:

```text
때로는 직접 보고
직접 듣는 게
가장 좋은 방법이야.

셜록 핀은 다음 날 같은 시간에
팝팝 옆에 앉았어요.

헤드폰 한쪽을 나눠 끼고
함께 들었어요.

도—

깜빡!

바로 그 순간······
저쪽 빵집에서
따뜻한 빵 냄새가 확—

'아! 같은 시간에
빵집 오븐이 켜졌어!'

세 번째 단서를 찾았어요.
```

## 09 페이지

Save as `09_페이지.png`.

Scene: 탐정 사무소 추리 칠판 정면. 카드 1 `월·화·수 같은 시간 가로등 깜빡`, 카드 2 `같은 시간에 광장 여기저기 작은 흔들림`, 카드 3 `같은 시간에 빵집 오븐 켜짐`. 세 카드 위에 노란 음표 세 개. 셜록 핀이 큰 화살표를 그린다.  
Composition: 추리 칠판 정면, 텍스트 여백은 아래쪽.  
Text:

```text
단서를 하나로 모아 보자.

세 단서 모두에
같은 점이 있었어요.

같은 시간.

같은 시간에 가로등이 깜빡여요.
같은 시간에 광장이 살짝 흔들려요.
같은 시간에 빵집 오븐이 켜져요.

'아, 그런 이유가 있었구나!

빵집 오븐이 켜질 때
진동이 벽을 따라 가로등까지
전해진 거야!'
```

## 10 페이지

Save as `10_페이지.png`.

Scene: 버블 베이커리 안. 따뜻한 분홍빛, 갓 구운 빵 진열대, 큰 오븐. 빵집 주인은 놀란 얼굴. 셜록 핀이 가게 벽을 가리키고, 한쪽에는 벽 너머 가로등이 등을 맞대고 있는 작은 단면도 표시.  
Composition: 가게 안 전체를 보여주는 중간샷, 텍스트 여백은 오른쪽 위.  
Text:

```text
셜록 핀과 친구들이
빵집을 찾아갔어요.

'안녕하세요!
오븐이 켜질 때마다
가로등이 깜빡여요.'

빵집 주인이 깜짝 놀랐어요.

'정말요?
내 오븐이 가로등에
영향을 주는지 몰랐어요!

가게 벽과 가로등이
등을 맞대고 있었구나······'
```

## 11 페이지

Save as `11_페이지.png`.

Scene: 빵집 안. 빵집 주인이 큰 오븐 아래에 부드러운 산호 쿠션을 깐다. 셜록 핀과 팝팝이 거들고, 모모와 크랩슨은 갓 구운 빵 냄새에 행복한 얼굴. 펄리도 별진주로 가게 안을 비춰 본다.  
Composition: 모두가 함께 일하는 따뜻한 와이드 중간샷, 텍스트 여백은 왼쪽 아래.  
Text:

```text
빵집 주인이 말했어요.

'오븐 아래에
부드러운 산호 쿠션을 깔게요.

그러면 진동이 줄어들 거예요.'

셜록 핀과 친구들이
함께 거들었어요.

가게 안에는
갓 구운 빵 냄새가
가득했어요.
```

## 12 페이지

Save as `12_페이지.png`.

Scene: 다음 날 같은 시간, 광장 벤치. 팝팝이 헤드폰을 끼고 앉아 있고 노란 음표 세 개가 떠오른다. 옆 가로등은 깜빡이지 않고 그대로 환하다. 버블 베이커리에서 빵집 주인이 갓 구운 빵 바구니를 들고 나와 셜록 핀, 팝팝, 모모, 크랩슨, 펄리에게 나눠준다. 따뜻한 황금빛 오후.  
Composition: 광장을 따뜻하게 담는 마무리 전경, 텍스트 여백은 아래쪽 가운데.  
Text:

```text
다음 날, 같은 시간.

도—

음악이 시작되었어요.

가로등은······
그대로 환했어요!

빵집에서는
따뜻한 빵 냄새가
평소처럼 퍼져 나왔어요.

'갓 구운 빵 드세요!'

음악과 빵 냄새가
함께 어우러진 따뜻한 오후.

한 번은 우연,
두 번도 우연일 수 있어요.

그런데 같은 일이
같은 시간에 자꾸 일어나면?

그건 우연이 아니라
이유가 있는 거예요!

꼬마 탐정단,
오늘도 성공!
```
