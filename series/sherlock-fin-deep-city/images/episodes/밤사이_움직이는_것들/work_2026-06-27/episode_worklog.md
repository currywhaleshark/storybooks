# 밤사이 움직이는 것들 작업로그

- 날짜: 2026-06-27
- 시리즈: 심해탐정 셜록 핀
- 원본 대본: `C:/Users/yurib/Downloads/밤 사이 움직인 것들.md`
- 로컬 대본: `series/sherlock-fin-deep-city/docs/episodes/밤사이_움직이는_것들.md`
- 작업 폴더: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27`
- 최종 폴더 예정: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/final`

## 현재 상태

- 다운로드 폴더의 Markdown 대본을 프로젝트 에피소드 대본 폴더로 복사했다.
- 대본은 00 표지 + 01-11 본문으로 총 12페이지 구성이다.
- `page_plan.md`를 생성해 페이지별 장면 기능, 등장 요소, 레퍼런스 의존, 필수 텍스트를 정리했다.
- `reference_setup/reference_setup_plan.md`를 생성해 본편 생성 전 사무소 내부, 조개 문, 문틈, 밤 물살 연속성 점검 항목을 정리했다.
- 문틈/밤 물살 레퍼런스 v1은 node 방출 방식으로 생성했다.
- 본편 페이지 이미지는 아직 생성하지 않았다.

## 규칙서 확인

- 이미지 규칙서: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_이미지_생성_디자인_규칙서.md`
- 사건 규칙서: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_사건생성_규칙서.md`
- 인물/배경 설정집: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_딥시티_인물배경_설정집.docx`

## 공식 참조 감사

사용 가능한 고정 참조:

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 딥시티 공통: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- 탐정 사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- 텍스트박스: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`

이번 에피소드 특이 사항:

- 신규 캐릭터는 없다. 셜록 핀 단독 막간극이다.
- 주 무대는 탐정 사무소 내부이며, 기존 탐정 사무소 내부 레퍼런스를 1차 기준으로 사용한다.
- 조개 문, 헐거운 경첩, 문 아래 작은 틈, 밤 물살, 가벼운 서류/카드/깃털 펜의 이동 방향이 핵심 연속성 요소다.
- 전용 문틈/밤 물살 레퍼런스 v1이 있다. 공식 사무소 내부, 셜록 핀, 딥시티 공통 레퍼런스를 `nodeRepl.emitImage`로 방출한 뒤 생성했다.

## 이야기 핵심

- 사건 유형: 현상 / 원인형. 셜록 핀이 혼자 겪고 혼자 해결하는 자연현상 규명 막간극.
- 진상: 헐거워진 조개 문 경첩 때문에 아래쪽에 새 틈이 생겼고, 밤이 되면 방향이 바뀌는 약한 물살이 그 틈으로 들어와 가벼운 물건만 조금씩 밀었다.
- 표면 사건: 문과 잠금쇠는 그대로인데 아침마다 사무소 안의 서류, 카드, 깃털 펜이 옮겨져 있다.
- 단서 1: 움직인 것은 가벼운 물건뿐이고 무거운 돋보기, 두꺼운 책, 잉크병, 책상은 그대로다.
- 단서 2: 물건들이 모두 문 쪽에서 책상 쪽으로 같은 방향으로 쏠려 있다.
- 단서 3: 문 아래쪽에 새로 생긴 틈과 솔솔 들어오는 작은 물살이 있다.
- 해결: 셜록 핀이 조개 공구로 경첩을 조여 문틈을 없애고, 메모지와 다음 날 아침 상태로 해결을 확인한다.

## 다음 단계

1. 사용자 QA로 문틈/밤 물살 레퍼런스 v1을 승인/수정한다.
2. 승인되면 Batch 1(00-03) prompt plan을 작성한다.
3. 본편 생성 전 각 페이지에 사용할 실제 공식 참조 이미지를 `nodeRepl.emitImage`로 방출한다.
4. 본문 페이지는 텍스트 포함 완성 페이지로 생성하고, 생성 후 필수 텍스트를 대본과 대조한다.

## 현재 중단점

- 대본 복사와 제작 준비는 완료.
- 본편 페이지 이미지는 아직 생성하지 않는다.
- 다음 작업은 문틈/밤 물살 레퍼런스 v1 사용자 QA 또는 Batch 1 prompt plan 작성부터 시작하면 된다.

## Reference Generation - 문틈/밤 물살 v1 - 2026-06-27

- 사용자 피드백: "레퍼런스 그렇게 하면 안됨 / node방출로".
- 실제 이미지 입력을 `nodeRepl.emitImage`로 방출:
  - 탐정 사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
  - 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
  - 딥시티 공통: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- Generated source: `C:/Users/yurib/.codex/generated_images/019f0970-f6b5-77e3-b220-e3da37132ce0/ig_08d33837be6da828016a3fe06d5898819191875e718fa823d4.png`
- Saved candidate: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v1.png`
- Saved reference copy: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `EDFBFD80C2EC643A64AAEF3C8437398CE19307547E83FA324865FFD8F76F0042`
- QA note: v1 separates the office corner, shell door, lower hinge/gap, gentle current inset, and light/heavy item comparison. Treat it as the visual truth for door/gap mechanics unless the user asks for revision.
- Next: user QA for this reference, then Batch 1 prompt plan. For Batch 1, emit this new reference image through `nodeRepl.emitImage` with the official office and Sherlock Fin references.

## Reference QA Update - 문틈/밤 물살 v2 승인 - 2026-06-27

- User identified v1 failure: the current read like music entering the room, not water current.
- User marked the physically correct gap location on the office door: lower-right closing edge of the shell door, not the center bottom and not the hinge side.
- Regenerated v2 after node-emitting only:
  - official detective office interior reference
  - user annotated correction image with the red circle marking the correct gap location
- Deliberately did not emit the Deep City/jazz reference for v2 to avoid music-note contamination.
- Saved v2 candidate: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/reference_setup/door_gap_reference_candidate_v2.png`
- Replaced official reference copy with v2: `series/sherlock-fin-deep-city/references/locations/밤사이_움직이는_것들_탐정사무소_문틈_레퍼런스.png`
- v2 dimensions: 1536x1024.
- v2 SHA256: `12C71646516BA6BB88554D35A93C1D34EB1D619E2E99FD738C9061118F23C669`
- v1 status: rejected/hold for music contamination and wrong gap placement. Keep only as history.
- v2 status: user approved for moving to the next step.
- New global lock: show actual water current only as translucent blue water ribbons, ripples, and small bubbles. No music notes, staff lines, sound-wave graphics, saxophone shapes, neon music icons, or decorative audio symbols.
- New door lock: the gap belongs at the lower-right closing edge of the door leaf where it meets the frame/floor area.

## Batch 1 User QA Corrections - 2026-06-28

- Page 00 cover: title has a stray/incorrect glyph between `사` and `이` in `밤사이`; regenerate with exact title `밤사이 움직이는 것들` and no inserted mark, space, or extra character between `사` and `이`.
- Page 00 cover: Sherlock Fin has three arms; regenerate with exactly two arms and two hands.
- Page 01: candidate is mostly okay, but the door handle became a round knob attached near the middle of the door. Regenerate with the handle/latch attached at the proper side/closing-edge area, not a central round knob.
- Page 02: text is acceptable; issue is visual. Sherlock Fin holding the magnifying glass feels odd here. Regenerate with the magnifying glass not in hand, preferably resting on the desk or absent from the focal action.
- Page 03: Sherlock Fin again has three arms. Regenerate with exactly two arms and two hands.
- Page 03: because the text ends with `셜록 핀은 모자를 살짝 눌러썼어요.`, Sherlock Fin should hold or press the brim of the detective hat with one hand.

### New Batch 1 Locks

- Sherlock Fin anatomy: exactly two arms and two hands, no extra arms, no extra gloves, no duplicated hand silhouettes.
- Page 03 pose: one hand must be on the detective hat brim, gently pressing it down; the other hand should rest naturally or point subtly, but must not create a third arm.
- Door handle/latch: do not invent a central round knob. Keep a side-mounted brass latch/handle consistent with the office door reference.
- Page 02: no magnifying glass in Sherlock Fin's hand.

## Cover Regeneration Update - 2026-06-28

- User rejected the local text-overlay direction for the cover and requested a generation-only retry because the generated title lettering is desirable.
- Re-emitted official references with `nodeRepl.emitImage` before retrying:
  - official detective office interior
  - approved door/gap reference v2
  - Sherlock Fin character sheet
- Saved generated cover retry: `batch_1/00_candidate_text_v2.png`
  - QA: fixes the stray mark in `밤사이` and the extra-arm issue, but the main logo reads close to `셜록핀` without enough visible spacing.
- Saved generated cover retry: `batch_1/00_candidate_text_v3.png`
  - QA: preferred current cover candidate. Generated title keeps the hand-lettered feel, `밤사이 움직이는 것들` appears correct, and Sherlock Fin has two arms/two hands.
  - Still requires user approval before promotion to final.
## Page 01-03 Object Continuity QA - 2026-06-28

- User identified a story-logic continuity issue across pages 01-03: only light objects should move overnight, while heavy objects must stay fixed.
- Baseline before-state: `01_candidate_text_v2.png`.
- Heavy object lock from page 01 to pages 02-03:
  - desk, chair, lamp, file holder, thick book/notebook, magnifying glass, ink bottle, and large desk tools must remain in the same locations and should not imply overnight movement.
- Light object movement lock from page 01 to pages 02-03:
  - loose papers, small cards, and the feather pen are the only objects that move.
  - They must look displaced from their page 01 positions, not duplicated as extra new floor props while originals remain untouched.
  - The pen holder/desk position should show the feather pen no longer neatly in place if the feather pen appears on the floor/rug.
- Page 03 must continue the same post-disturbance arrangement from page 02 while Sherlock Fin inspects the door and presses the detective hat brim.
## Batch 1 Continuity Regeneration Candidates - 2026-06-28

- `01_candidate_text_v2.png`: current page 01 baseline candidate. Door hardware corrected to a side latch/handle. Treat this as the tidy before-state item layout.
- `02_candidate_text_v2.png`: generated continuity retry; saved as history, but text looked slightly unstable on review.
- `02_candidate_text_v3.png`: current page 02 candidate. Sherlock Fin no longer holds the magnifying glass; heavy objects remain on/around the desk; loose papers, cards, and the feather pen are the moved light objects.
- `03_candidate_text_v2.png`: current page 03 candidate. Continues the page 02 disturbed light-object arrangement, removes the hand-held magnifying glass, uses exactly two arms/hands, and adds the hat-brim press pose.
- Current Batch 1 review set: `00_candidate_text_v3.png`, `01_candidate_text_v2.png`, `02_candidate_text_v3.png`, `03_candidate_text_v2.png`.
## Page 01-03 Desk-Locked Rework Prep - 2026-06-28

- New user direction: rework pages 01-03 only; do not touch the cover.
- Priority lock: the desk must remain fixed across pages 01-03.
- Heavy object lock expanded: desk, chair, lamp, file holder, thick book/notebook stack, magnifying glass, ink bottle, pen holder, and large desk tools must not move.
- Light object lock refined: only loose papers, small cards, thin notes, and the feather pen move.
- New scattering logic: in pages 02-03, the moved light objects should look as if they fell/slid from the desk to the floor and spread from the door/lower-right gap area toward the desk, forming a gentle fan/trail that supports the later deduction scene.
- Continuity target: regenerate 01-03 as a linked mini-batch, using page 01 as the tidy anchor, page 02 as the first post-disturbance state, and page 03 as the same post-disturbance state plus closed-door inspection/hat-brim pose.
- Prompt plan updated: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/batch_1/batch_1_prompt_plan.md`
- Next candidates should use version names such as:
  - `01_candidate_text_v3_desk_lock.png`
  - `02_candidate_text_v4_desk_lock_door_fan.png`
  - `03_candidate_text_v3_desk_lock_door_fan.png`
## Page 03 Door Handle Correction - 2026-06-28

- User QA: page 03 door handle/latch appeared attached to the hinge side and looked physically wrong.
- Applied correction: regenerate page 03 with hinges on viewer-left and handle/latch/lock on viewer-right closing edge of the shell door.
- Rejected candidate: `batch_1/03_candidate_text_v4_reject_handle_on_hinge.png`.
- Current page 03 candidate: `batch_1/03_candidate_text_v5_desk_lock_door_right_handle.png`.
- QA note: v5 keeps the desk/heavy objects fixed, keeps the light-object fan/trail on the floor, removes duplicate feather-pen issue, and places the door handle/latch away from the hinge side.
- Current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v4_desk_lock_door_fan.png`
  - `batch_1/03_candidate_text_v5_desk_lock_door_right_handle.png`
## Mobile Review Upload - Google Drive - 2026-06-28

- Uploaded current 01-03 review candidates to Google Drive for mobile review.
- Folder: `https://drive.google.com/drive/folders/1SV0e33Q9HTi6nrV9FHzpwd4-WmVQvkwL`
- Files:
  - `01_candidate_text_v3_desk_lock.png`: `https://drive.google.com/file/d/1Tl2iLbvg7iFiSs1xftZRibvv3Eapc-KV/view?usp=drivesdk`
  - `02_candidate_text_v4_desk_lock_door_fan.png`: `https://drive.google.com/file/d/1B6DgLaslXZ9v6XF12BZsq0xKwpvdeaaW/view?usp=drivesdk`
  - `03_candidate_text_v5_desk_lock_door_right_handle.png`: `https://drive.google.com/file/d/1UltDaMUpKYRy7OHc5yYPMtgwmkd--xUU/view?usp=drivesdk`
## Page 02-03 Paper Stack Reduction Correction - 2026-06-28

- User QA: pages 02-03 still keep the desk paper bundle intact while adding scattered papers only on the floor. This reads as duplicated extra papers, not actual movement.
- New light-paper lock:
  - The neat loose document stack from page 01 must be visibly reduced in pages 02-03.
  - Some of those same thin documents should be partly slid off the desk edge, some should remain askew on the desk, and some should continue onto the floor/rug.
  - Do not preserve a full neat stack of loose papers while also adding many floor papers.
  - It should look like the floor papers came from the desk paper stack.
- Heavy-object clarification:
  - Thick book/notebook stack, file holder, lamp, magnifying glass, ink bottle, pen holder, large desk tools, chair, and desk remain fixed.
  - Thin loose papers, small cards, notes, and the single feather pen are light moving objects.
- Page 02 next filename: `02_candidate_text_v5_reduced_desk_papers_door_fan.png`.
- Page 03 next filename: `03_candidate_text_v6_reduced_desk_papers_right_handle.png`.
## Handoff Created - 2026-06-28
- Created handoff for clean-session continuation after image-generation contamination: $handoffPath
- Stop current-session generation. Next session should regenerate pages 02 and 03 with reduced desk paper stack and door-centered scatter continuity.

## Clean-Session Page 02-03 Paper Stack Regeneration - 2026-06-28

- Continued from `handoff_2026-06-28_page02_03_paper_stack.md` after prior generation contamination.
- Emitted actual references with `nodeRepl.emitImage` before generation:
  - official detective office interior
  - approved door/gap reference v2
  - Sherlock Fin character sheet
  - textbox layout reference
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - old 02/03 candidates as negative examples only
- Saved new page 02 candidate: `batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0f129ffd3fc33319016a4100e256cc8191869a17294520b996.png`
  - Dimensions: 1054x1492.
  - SHA256: `D4B07D61CBBEEE3247E33BFCE579DEA7AFB9658EAC089335D874215FA8D68FD9`.
  - QA: desk loose-paper pile is visibly reduced; several sheets remain askew on the desk, several hang/slide over the edge, and floor/rug papers read as a continuation from the desk. Heavy objects remain on the desk. Text panel is present and readable.
- Saved new page 03 candidate: `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0a9dbad8733d0976016a4102498fe08191b594a7b0173caf16.png`
  - Dimensions: 1054x1492.
  - SHA256: `2FFB31C7BEBB13972D06824BC35BA4661CE62DA84ABA8E2FE88F3A4D3602DA15`.
  - QA: continues the reduced desk-paper arrangement with sheets on desk, over the edge, and on floor/rug; Sherlock Fin presses the hat brim with two-arm anatomy; door handle/latch is on the viewer-right closing edge, opposite the viewer-left hinges; no duplicate feather pen observed.
- New current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`
  - `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`
- Next: upload the new page 02 and page 03 candidates to the existing mobile review Google Drive folder and report links. Do not promote to final until user approval.

## Mobile Review Upload Blocked - 2026-06-28

- Attempted to upload `02_candidate_text_v6_reduced_desk_papers_regen.png` to the existing Google Drive mobile review folder.
- Google Drive connector blocked the upload because the destination folder visibility is unverified/external (`source_visibility_status: access_not_verified`).
- No workaround attempted. Explicit user approval is required before retrying upload of the generated PNGs to that Drive folder.

## Batch 2 Page 06 Anatomy Correction - 2026-06-28

- User QA: page 06 text is acceptable; visual failure is Sherlock Fin has three visible hands/arms in `batch_2/06_candidate_text_v1_hold_text.png`.
- Cause identified: crouching pose plus two assigned hand actions caused the model to add a third support/knee hand.
- Saved corrected page 06 candidate: `batch_2/06_candidate_text_v2_two_hands.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0f6da4594c33ec6b016a410cfe45b4819189bd49b45f12a657.png`
  - Dimensions: 1054x1492.
  - SHA256: `56AAB61DBD827BF0CAC408892B87AB8F69AEB12EAACD171E295EA81402D65DF9`.
  - QA: exactly two visible hands: one holds the magnifying glass and one touches the door-gap/current area. No knee/lap/support third hand visible. Door gap and small blue current remain readable.
- Status: use `06_candidate_text_v2_two_hands.png` instead of `06_candidate_text_v1_hold_text.png` for page 06 review.

## Batch 3 Generation - Pages 07-09 - 2026-06-28

- Created Batch 3 prompt plan: `batch_3/batch_3_prompt_plan.md`.
- Emitted actual references with `nodeRepl.emitImage` before generation:
  - official detective office interior
  - approved door/gap/water-current v2
  - Sherlock Fin character sheet
  - textbox layout reference
  - Batch 2 clue anchors: 04, 05, and corrected 06 v2
- Saved page 07 candidate: `batch_3/07_candidate_text_v1.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_088af2698c9e0931016a4112833c088191bf3c29bb578e9b0d.png`
  - Dimensions: 1054x1492.
  - SHA256: `666935B701E537675C97B2E42495B78FE502A089BC9BBA61D0054471E437437B`.
  - QA: clue-board synthesis is readable, with three separated clue cards and a central water-current/door-gap/light-object diagram. No obvious music-note contamination observed.
- Saved page 08 candidate: `batch_3/08_candidate_text_v1.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0b22514c4446b57b016a411452ef3081949381365c4efc13d8.png`
  - Dimensions: 1055x1491.
  - SHA256: `61C13AB560117B455693C2A5D5D903075F3CF3BF7A6FC6F359D98CB1D5A2EDAE`.
  - QA: two thought bubbles clearly compare before sealed door vs now loose hinge/gap; Sherlock Fin anatomy appears controlled. Dimension differs from nearby candidates by 1px and can be normalized at final packaging if needed.
- User corrected page 09 layout before generation: split into two cuts, one repair cut and one test cut.
- Saved page 09 candidate: `batch_3/09_candidate_text_v1_split_repair_test.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0d94fc47aec45a62016a41186579f48191ba5c991f865bce36.png`
  - Dimensions: 1054x1492.
  - SHA256: `1F00E324C38D8C188CC1D172C8D9D49844E03D3625A74C2B855B13773DDCBD0E`.
  - QA: page is split into two clear cuts: upper repair cut and lower memo-note test cut. Test cut shows no entering water current; memo note remains still. Door hardware remains plausible. No extra hands obvious on review.
- Current Batch 3 review set:
  - `batch_3/07_candidate_text_v1.png`
  - `batch_3/08_candidate_text_v1.png`
  - `batch_3/09_candidate_text_v1_split_repair_test.png`

## Page 09 Repair Cut Contact/Hand Correction - 2026-06-28

- User QA on v2: the intended left hand read as a right hand, and the screwdriver/tool still appeared to pierce the door panel rather than sit in the hinge screw.
- Saved rejected v2 for history: `batch_3/09_candidate_text_v2_split_repair_contact_reject.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_0710f0435c7514c7016a41215934548191be5527dca00f6f09.png`
  - Dimensions: 1054x1492.
  - SHA256: `66B19F1EBA668F01F85593B02AE34061856F9ECE3EECF1915ACBDB6BAB1F5DBA`.
  - Status: reject/hold. Do not use for final.
- Regenerated the smallest failing unit only: a replacement repair panel.
  - Saved panel: `batch_3/09_repair_panel_v3_left_hand_hinge_screw.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0dde-b7fb-7b71-8149-b882c9259432/ig_09f0d43230918484016a4123db5fb88191a04c2363eeba7464.png`
  - Dimensions: 1536x1024.
  - SHA256: `73C6E052647E364E3A9A91045FD66085A0A02F74CD67D1907689C998DE9593FA`.
- Composited the new repair panel into the accepted split-page base, preserving the existing memo-test cut and the existing text panel.
  - Current page 09 candidate: `batch_3/09_candidate_text_v3_split_repair_left_hand_hinge_screw.png`
  - Dimensions: 1054x1492.
  - SHA256: `F39FAC1C4825BA668B83DF18C4A34BE18F5D3CA441315802ED0CF1351C8A27C0`.
  - QA: upper repair cut now shows the tool tip seated in the visible hinge screw slot instead of piercing the door panel; Sherlock Fin's gaze is directed at the screw/tool contact point; lower memo-test cut remains unchanged and shows the memo still with no water current.
- Current Batch 3 review set:
  - `batch_3/07_candidate_text_v1.png`
  - `batch_3/08_candidate_text_v1.png`
  - `batch_3/09_candidate_text_v3_split_repair_left_hand_hinge_screw.png`

## Page 09 Repair-Cut Natural Scale / Perpendicular Screw Correction - 2026-06-28

- User QA on v3: the hinge and screws became too large compared with the original door hardware, so the screwdriver no longer matched the screw scale.
- Generated and saved rejected v4 for history:
  - `batch_3/09_repair_panel_v4_natural_screw_reject_angle_door_scale.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_04cb5bb93f393b6a016a412a948d00819187b5a04891d749f5.png`
  - Dimensions: 1536x1024.
  - SHA256: `1FBF972AC62CF6E9C71FD6268FE20B139E94237821EA95324BF88EA1BE200361`.
  - Status: reject/hold. Door scale became too small and screwdriver/screw angle still did not read correctly.
- User QA on v4: the door became too small, and the screwdriver must be perpendicular to the screw head.
- Generated new repair panel v5:
  - `batch_3/09_repair_panel_v5_perpendicular_screw.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_019ea4cc266214fd016a412b58070881918d2b748130d63bd3.png`
  - Dimensions: 1536x1024.
  - SHA256: `DAFAEF6E1B49F8197D533288D3A042E13C68A8738186418F5A9266A0ACFDC704`.
- Composited v5 into the accepted split-page base, preserving the existing memo-test cut and text panel:
  - Current page 09 candidate: `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`
  - Dimensions: 1054x1492.
  - SHA256: `6B85EB9DE9D0F71DF994BA2318E33A17080AABF01E3FF2A05928871E17C8DDFB`.
  - QA: upper repair cut now keeps the door large in frame; hinge hardware is normal-sized on the door; the small shell screwdriver is aimed straight into a small slotted hinge screw, close to perpendicular to the screw face; Sherlock Fin uses exactly two visible hands and looks at the repair point.
  - Verification: lower region from y=780 compared against v1 and had zero differing pixels, confirming the text panel and memo-test cut were preserved.
- Current Batch 3 review set:
  - `batch_3/07_candidate_text_v1.png`
  - `batch_3/08_candidate_text_v1.png`
  - `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`

## Page 09 User Approval / Proceed to Batch 4 - 2026-06-28

- User response after reviewing `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`: "좋았어 이제 다음으로 가자".
- Treat page 09 v5 as the current accepted review candidate for moving onward.
- Started Batch 4 for pages 10-11 and created prompt plan: `batch_4/batch_4_prompt_plan.md`.

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

## Page 02 Gaze Direction Correction - 2026-06-29

- User QA on `02_candidate_text_v6_reduced_desk_papers_regen.png`: Sherlock Fin looks toward empty space rather than actually looking at the messy office.
- Regenerate page 02 only.
- Preserve from v6:
  - fixed desk/heavy-object continuity,
  - reduced loose-paper stack on the desk,
  - thin papers/cards continuing from desk to floor,
  - moved feather pen/card evidence,
  - text panel position and story text as much as possible.
- New page 02 lock:
  - Sherlock Fin's face direction and pupils must turn into the office interior, aimed clearly at the scattered papers/cards and the desk mess.
  - Do not let Sherlock Fin look at the viewer, toward the outside doorway, toward the text panel, or into empty air.
  - Use a slight side/three-quarter head turn, lowered gaze line, or leaning-in discovery pose so the eyeline is unambiguous.
- Next candidate: `02_candidate_text_v7_gaze_into_office.png`.

## Page 02 Gaze Direction Regeneration - 2026-06-29

- User QA on `batch_1/02_candidate_text_v6_reduced_desk_papers_regen.png`: Sherlock Fin's face/gaze looked like she was staring into empty space rather than looking into the messy office.
- Regenerated page 02 only.
- Intermediate candidate:
  - `batch_1/02_candidate_text_v7_gaze_into_office.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0180cb1eefecc665016a413974545c8191afe7e8b704577051.png`
  - Dimensions: 1054x1492.
  - SHA256: `F8976CB6C803B66E6F9AB136E0FF94E176A907A9C55C59D98A69FCEA4FB452DC`.
  - Status: hold. Gaze direction improved, but QA found possible duplicate feather-pen reading, with one feather on the floor and another quill-like object near the desk holder.
- Current page 02 candidate:
  - `batch_1/02_candidate_text_v8_gaze_into_office_single_feather.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0f56315c43eb5f16016a413aac7a6c8191bbb224b154c66f70.png`
  - Dimensions: 1054x1492.
  - SHA256: `DA6F2879BB6B0CC2969C02C30BFFBD8C3980BC9D04E91F971BE663E8E2DCE477`.
  - QA: Sherlock Fin's face and pupils now read as looking inward/downward toward the messy floor papers and desk, not into empty air; one feather pen appears displaced on the floor/rug; desk/heavy objects remain fixed; loose papers/cards still read as a trail from the desk.
- Updated current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v8_gaze_into_office_single_feather.png`
  - `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

## Page 02 Mixed Preference Correction - 2026-06-29

- User QA after v7/v8 comparison: desk/table state is better in the second candidate (v8), while Sherlock Fin is better in the first candidate (v7).
- Next candidate should combine:
  - Sherlock Fin from v7: better facial direction, pose, and discovery feeling.
  - Desk/paper state from v8: better desk state, paper trail, and single displaced feather pen logic.
- Avoid local cut-and-paste compositing unless necessary; prefer full-page regeneration so character and room lighting remain natural.
- Next candidate: `02_candidate_text_v9_v7_sherlock_v8_desk.png`.

## Page 02 Door Hinge Visibility Correction - 2026-06-29

- User QA on `batch_1/02_candidate_text_v9_v7_sherlock_v8_desk.png`: the open door angle should not expose the door hinges, but v9 shows visible hinge hardware.
- Status of v9: hold/reject for door-hinge geometry, even though the Sherlock pose and desk state were close.
- Regenerate page 02 only as a full page.
- Carry forward:
  - v7 Sherlock Fin pose/expression/gaze into the office,
  - v8 desk/table state and single-feather logic,
  - fixed heavy objects and reduced desk-paper stack,
  - exact page 02 text.
- New door geometry lock: no visible hinge barrels, hinge plates, or vertical hinge hardware on the viewer-facing door/frame for this open-door angle; show only the closing-edge handle/latch.
- Next candidate: `batch_1/02_candidate_text_v10_no_visible_hinge.png`.

## Page 02 No-Visible-Hinge Regeneration - 2026-06-29

- Saved page 02 candidate: `batch_1/02_candidate_text_v10_no_visible_hinge.png`
  - Generated source: `C:/Users/yurib/.codex/generated_images/019f0e88-6119-7d21-9ebf-47d091aad23c/ig_0efbb8c848a5eb19016a413f9f096c819195ee65be34070aee.png`
  - Dimensions: 1054x1492.
  - SHA256: `C6C820FAA1C4DB28345527F72120A10802F174F4172199321493564191A7DCD8`.
  - QA: open shell door no longer shows exposed hinge barrels, hinge plates, or vertical brass hinge hardware; the door angle reads more physically natural. Visible hardware is limited to the closing-edge handle/latch area. Sherlock Fin keeps a v7-like surprised inward gaze toward the messy office. Desk/table state remains close to v8 with fixed heavy objects, a reduced/askew paper state, floor cards/papers, and a single displaced feather pen.
- Current page 02 candidate: `batch_1/02_candidate_text_v10_no_visible_hinge.png`.
- Updated current 01-03 review set:
  - `batch_1/01_candidate_text_v3_desk_lock.png`
  - `batch_1/02_candidate_text_v10_no_visible_hinge.png`
  - `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`

## Final Promotion - 2026-06-29

- User approved finishing and promoting the candidates to final.
- Final folder: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/final`
- Final page count: 12 files, `00_표지.png` through `11_페이지.png`.
- All final pages are 1054x1492 PNG. Page 08 was normalized from 1055x1491 to 1054x1492 during final copy.
- Selected source mapping:
  - `00_표지.png` <= `batch_1/00_candidate_text_v3.png`
  - `01_페이지.png` <= `batch_1/01_candidate_text_v3_desk_lock.png`
  - `02_페이지.png` <= `batch_1/02_candidate_text_v10_no_visible_hinge.png`
  - `03_페이지.png` <= `batch_1/03_candidate_text_v7_reduced_desk_papers_right_handle_regen.png`
  - `04_페이지.png` <= `batch_2/04_candidate_text_v1.png`
  - `05_페이지.png` <= `batch_2/05_candidate_text_v1_hold_text.png`
  - `06_페이지.png` <= `batch_2/06_candidate_text_v2_two_hands.png`
  - `07_페이지.png` <= `batch_3/07_candidate_text_v1.png`
  - `08_페이지.png` <= `batch_3/08_candidate_text_v1.png - normalized from 1055x1491 to 1054x1492`
  - `09_페이지.png` <= `batch_3/09_candidate_text_v5_split_repair_perpendicular_screw.png`
  - `10_페이지.png` <= `batch_4/10_candidate_text_v4_fullregen_no_current_lights_off_lamp_visible.png`
  - `11_페이지.png` <= `batch_4/11_candidate_text_v1_morning_success.png`
- QA closeout: current final set uses the latest approved/held-good candidates, including page 02 v10 with no visible hinge, page 09 v5 perpendicular screw repair, and page 10 v4 with no internal current and lights off while keeping the ceiling lamp visible.

- Final manifest saved at: `series/sherlock-fin-deep-city/images/episodes/밤사이_움직이는_것들/work_2026-06-27/final_manifest.md`.
- Final folder verification: 12 PNG files only, no non-image files, all 1054x1492.
