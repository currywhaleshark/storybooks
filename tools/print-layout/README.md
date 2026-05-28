# 그림책 인쇄 레이아웃 웹툴

완성된 그림책 이미지를 인쇄용 PDF로 정리하는 로컬 웹툴입니다.

## 기능

- `series` 아래의 그림책 이미지 폴더 자동 탐색
- `00_표지.png` 표지 분리
- 본문 이미지를 A4 가로 좌우 2페이지 또는 A4 세로 상하 2페이지로 배치
- 표지를 포함하고 표지 뒷면을 공백으로 둔 책자형 PDF 생성
- 모든 이미지를 자르지 않고 전체 표시
- 브라우저 미리보기
- 표지 PDF, 본문 PDF, 통합 PDF, 책자 PDF 생성

## 실행

저장소 루트에서 실행합니다.

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' tools/print-layout/server.js
```

브라우저에서 표시된 주소를 엽니다.

기본 주소:

```text
http://localhost:4173
```

## PDF 출력 위치

선택한 이미지 폴더 아래 `print-output` 폴더에 저장됩니다.

```text
cover.pdf
body-a4-landscape-2up.pdf
body-a4-portrait-2up.pdf
print-ready-combined-landscape.pdf
print-ready-combined-portrait.pdf
booklet-a4-landscape.pdf
```

## 명령어로 바로 PDF 만들기

```powershell
& 'C:\Users\USER\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m tools.print_layout.pdf_layout 'series/coral-town-daycare/images/episodes/산호마을_어린이집' --target booklet --layout landscape
```

`--target` 값:

- `cover`
- `body`
- `both`
- `booklet`

`--layout` 값:

- `landscape`: A4 가로, 좌우 2페이지
- `portrait`: A4 세로, 상하 2페이지

책자 PDF는 `landscape` A4 좌우 배치로 생성됩니다. 페이지 구성은 표지, 빈 표지 뒷면, 본문 순서이며 전체 페이지 수가 4의 배수가 되도록 빈 페이지가 자동으로 추가됩니다.
