# 두 갈래 발자국 작업로그

- 날짜: 2026-06-29
- 시리즈: 심해탐정 셜록 핀
- 원본 대본: `C:/Users/yurib/Downloads/두_갈래_발자국_수정본 (2).md`
- 로컬 대본: `series/sherlock-fin-deep-city/docs/episodes/두_갈래_발자국.md`
- 작업 폴더: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29`
- 최종 폴더 예정: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/final`

## 현재 상태

- 다운로드 폴더의 Markdown 대본을 프로젝트 에피소드 대본 폴더로 복사했다.
- 대본은 00 표지 + 01-11 본문으로 총 12페이지 구성이다.
- 사건 구조와 페이지 흐름은 시리즈 규칙에 맞다: 잘 보기(발자국 깊이/모양), 잘 듣기(모래 말미잘 증언), 잘 생각하기(깊은 발자국 -> 목걸이 -> 얕은 발자국).
- 본편 페이지 이미지는 아직 생성하지 않았다.
- 신규 캐릭터와 신규 장소가 많으므로 본편 생성 전에 레퍼런스 세트를 먼저 만든다.

## 규칙서 확인

- 이미지 규칙서: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_이미지_생성_디자인_규칙서.md`
- 사건 규칙서: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_사건생성_규칙서.md`
- 대본 작성법: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_그림책_대본_작성방법.md`
- 인물/배경 설정집: `series/sherlock-fin-deep-city/docs/심해탐정_셜록핀_딥시티_인물배경_설정집.docx`

## 공식 참조 감사

사용 가능한 고정 참조:

- 셜록 핀: `series/sherlock-fin-deep-city/references/characters/셜록핀.png`
- 딥시티 공통: `series/sherlock-fin-deep-city/references/심해탐정_셜록핀_딥시티_레퍼런스.png`
- 탐정 사무소 내부: `series/sherlock-fin-deep-city/references/locations/웃고_있는데_슬픈_얼굴_탐정사무소_내부_레퍼런스.png`
- 텍스트박스: `series/sherlock-fin-deep-city/references/layouts/텍스트박스_레이아웃_레퍼런스.png`
- 크랩슨: `series/sherlock-fin-deep-city/references/characters/크랩슨.png`

이번 에피소드에서 새로 필요하거나 미보유인 참조:

- 두두: 기존 작업물 `series/sherlock-fin-deep-city/references/characters/거꾸로_도서관_신규인물_레퍼런스.png`의 2번 패널에 공식에 가까운 덤보 문어 아기 두두 레퍼런스가 있다. 이번 에피소드에서는 이 외형을 시각 기준으로 삼고, 대본 지시에 맞춰 작은 베레모만 추가한 복장 업데이트 시트를 만든다. 작업용 crop은 `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/두두_existing_reference_crop.png`이고, 현재 후보는 `두두_beret_reference_candidate_v1.png`이다.
- 가비: 신규 가시배새우 캐릭터. 본편 전 공식 캐릭터 시트가 필요하다.
- 모래 말미잘: 신규 단역 목격자. 간단한 캐릭터 레퍼런스가 필요하다.
- 은모래 언덕: 새 주요 장소. 발자국 단서가 흔들리지 않도록 장소/표면 레퍼런스가 필요하다.
- 산호 종 약속 장소: 페이지 09-11에서 반복되는 목적지. 은모래 언덕과 연결된 장소 레퍼런스가 필요하다.
- 조개 목걸이 + 새우 발자국 단서 세트: 깊은 콕콕 자국, 얕은 콕콕 자국, 두 갈래 착시, 목걸이 기준점이 핵심이므로 별도 단서 레퍼런스가 필요하다.

## 이야기 핵심

- 사건 유형: 분실 / 이동형 + 친구 찾기형.
- 진상: 가비가 조개 목걸이를 더듬이에 걸고 가다가 약속이 생각나 방향을 틀었고, 그 순간 목걸이를 떨어뜨렸다.
- 표면 사건: 두두가 목걸이를 주웠지만 발자국이 두 갈래처럼 보여 어느 쪽으로 가야 할지 헷갈린다.
- 단서 1: 목걸이를 기준으로 한쪽 발자국은 깊고 다른 쪽은 얕다.
- 단서 2: 두 쪽 모두 같은 새우 발자국이다.
- 단서 3: 모래 말미잘이 가비가 목걸이를 걸고 지나가다 약속 때문에 몸을 휙 돌렸다고 증언한다.
- 해결: 얕은 발자국을 따라가 산호 종 약속 장소에서 가비를 만나고 목걸이를 돌려준다.

## 다음 단계

1. `reference_setup/reference_setup_prompt_plan.md` 기준으로 신규 레퍼런스 후보를 먼저 생성한다.
2. 생성 전 실제 공식 참조 이미지를 방출/첨부한다. 로컬 경로 텍스트만으로 참조하지 않는다.
3. 사용자 QA로 레퍼런스 후보를 승인하거나 수정한다.
4. 레퍼런스 승인 후 Batch 1(00-03) prompt plan을 작성한다.
5. 본문 페이지는 텍스트 포함 완성 페이지로 생성하고, 생성 후 필수 텍스트를 대본과 대조한다.

## 현재 중단점

- 대본 복사와 제작 준비는 완료.
- 본편 생성은 시작하지 않는다.
- 다음 작업은 신규 레퍼런스 생성부터 시작한다.

## Reference Generation - 가비 v1 - 2026-06-29

- Generated next reference after Dudu approval direction.
- Candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v1.png`
- Generated source remained under `C:/Users/yurib/.codex/generated_images/019f137a-afc8-7203-a6a6-e4b272d8ed9f/`.
- Dimensions: 1536x1024.
- SHA256: `4ADA90D759E51DA40336A63CE542202BCACE76A6E4AA6CA7C684B357ED2172AF`.
- QA note: v1 includes a cute coral-pink rounded shrimp body, soft back bumps, long antennae with ribbon, suspenders, shell-necklace carrying/slipping action, and small-leg/footprint detail. Await user QA before copying to `references/characters/두_갈래_발자국_가비_레퍼런스.png`.
## Reference QA / Regeneration - 가비 v2 - 2026-06-29

- User QA on v1: real 가시배새우 has a longer shrimp profile with armored head, segmented abdomen, tail fan, walking legs, long antennae, and dorsal spines; v1 was too baby-faced and too generic-round.
- v1 status: hold/reject for weak shrimp identity and overly infant-like face.
- User provided biological shape reference image from clipboard: `C:/Users/yurib/AppData/Local/Temp/codex-clipboard-cc487fbd-dfef-4a40-8e61-7c22c726aaaf.png`.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v2_spiny_shrimp.png`
- Dimensions: 1536x1024.
- SHA256: `ADABBFB7AFA5CD9A016988EECDDAC37F11A41F5B5C7E6A6E2BE3E9031E1FA66A`.
- QA note: v2 is more shrimp-accurate, with a longer side profile, segmented abdomen, tail fan, long antennae, small eyes, visible small legs, shell necklace action, and suspenders/ribbon. Check user QA for whether dorsal spines are soft enough and whether the face is now the right age/tone.
## Reference QA / Regeneration - 가비 v3 - 2026-06-29

- User QA on v2: shrimp anatomy improved, but the result went too realistic/specimen-like for the picture-book series.
- v2 status: hold/reject for overly realistic rendering.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v3_storybook_shrimp.png`
- Dimensions: 1536x1024.
- SHA256: `290782E238881BE7070BAEA9E7C6E1ED656B11D52581744979415C07821E8C54`.
- QA note: v3 keeps the elongated shrimp silhouette, antennae, segmented abdomen, tail fan, small legs, shell necklace action, suspenders, and ribbon, while moving back toward the soft watercolor storybook-reference style. Review whether it is now stylized enough and still recognizably 가시배새우.
## Reference QA / Regeneration - 가비 v4 - 2026-06-29

- User QA on v3: remove some leg spikes/spikiness.
- v3 status: hold for leg/spine area being a little too busy or sharp.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v4_soft_legs.png`
- Dimensions: 1536x1024.
- SHA256: `7C26FA79CDB18BD116CE28BC2B828053E70A46A442EE7C167544500A59FF6DE8`.
- QA note: v4 keeps the storybook shrimp silhouette while simplifying underside legs into fewer rounded feet and softening dorsal bumps. Current review candidate unless user requests another anatomy/style adjustment.
## Reference QA / Regeneration - 가비 v5 - 2026-06-29

- User QA on v4: do not reduce the leg count; if the number of legs drops, Gabi stops reading as a shrimp.
- v4 status: hold/reject for over-simplified underside legs.
- Style reference: `series/sherlock-fin-deep-city/references/characters/크랩슨.png` for rounded, soft segmented storybook leg language only. Keep Gabi as a shrimp, not a crab.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v5_crabson_leg_style.png`
- Dimensions: 1536x1024.
- SHA256: `C79FEF37D2C4B7249104F5190A916918F9779C20C786BD48FF4519FFE9AC8070`.
- QA note: v5 locks multiple visible shrimp leg pairs while simplifying each leg into rounded, non-spiky segments inspired by Crabson's leg style. Await user QA for whether the leg count and softness now balance correctly.
## Reference QA / Regeneration - 가비 v6 - 2026-06-29

- User QA on v5: eyes are crooked/misaligned.
- v5 status: hold/reject for eye alignment issue.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v6_eye_alignment.png`
- Dimensions: 1536x1024.
- SHA256: `972964170F7D20F4C96D9CCCC5876CB556D7451F291C030C3359F6C90730C083`.
- QA note: v6 preserves the v5 shrimp silhouette, multiple rounded legs, ribbon, suspenders, and shell necklace direction while explicitly correcting eye height, size, and shared gaze alignment. Await user QA.
## Reference QA / Regeneration - 가비 v7 - 2026-06-29

- User direction after v6: stop chasing realistic spiny-belly shrimp anatomy; make Gabi a Crabson-like deformed shrimp in suspender/overall pants.
- Face lock: cute but not baby-faced. Avoid huge watery infant eyes, giant forehead, and toddler proportions.
- Design lock: compact rounded shrimp character, warm brown suspenders/overalls, shrimp antennae, tail fan, small rounded legs, no crab claws.
- v6 status: hold as transitional anatomy candidate; replaced by new simplified character direction.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v7_crabson_overall_shrimp.png`
- Dimensions: 1536x1024.
- SHA256: `C20B1699395F2FD857FFB28A11574D19791F1091FFF5F16FC03894D8BDC74666`.
- QA note: v7 prioritizes Crabson-family deformation and suspender-shrimp readability over biological accuracy. Await user QA.
## Reference QA / Regeneration - 가비 v8 - 2026-06-29

- User QA on v7: eyes are too pretty.
- v7 status: hold for overly beautiful/glamorous eyes, despite good Crabson-like overall-shrimp direction.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v8_simple_oval_eyes.png`
- Dimensions: 1536x1024.
- SHA256: `BBA5FEAEE58F6402791A206621AD9521E1E5E26A0CF013EF6AF9F5E653FC4A6D`.
- QA note: v8 preserves the deformed suspender-shrimp direction while reducing eye glamour toward smaller, plainer Crabson-like oval eyes. Await user QA on whether the expression is now plain enough without becoming too flat.
## Reference QA / Regeneration - 가비 v9 - 2026-06-29

- User QA on v8: eyes became too simple, and antenna positions are inconsistent, with one at the side of the head and one near the center.
- v8 status: hold for over-simplified eyes and antenna origin mismatch.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v9_balanced_eyes_aligned_antennae.png`
- Dimensions: 1536x1024.
- SHA256: `F21B6D17326BE5EBFD7D30CF374FE7BC643DED126EC58C731224C1D3B8955A72`.
- QA note: v9 aims for a middle point between v7's overly pretty eyes and v8's overly plain eyes, while locking both antennae to paired, believable bases on the same head plane. Await user QA on whether the antenna bases are sufficiently aligned.
## Reference Approval - 가비 direction v9 - 2026-06-29

- User accepted the v9 feeling/direction: "그래 이런 느낌으로 가보자".
- Approved direction copy: series/sherlock-fin-deep-city/references/characters/두_갈래_발자국_가비_레퍼런스.png
- Source candidate: series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/가비_reference_candidate_v9_balanced_eyes_aligned_antennae.png
- Dimensions: 1536x1024.
- SHA256: F21B6D17326BE5EBFD7D30CF374FE7BC643DED126EC58C731224C1D3B8955A72.
- Main-page lock: use a Crabson-like deformed shrimp wearing warm brown suspenders/overall pants; avoid realistic spiny-belly anatomy, baby face, overly pretty/glamorous eyes, over-simple blank eyes, and mismatched antenna origins. Both antennae should start from paired positions on the same head plane.
## Reference Generation - 모래말미잘 v1 - 2026-06-29

- Generated next missing reference after Gabi direction approval.
- Candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/모래말미잘_reference_candidate_v1.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/characters/두_갈래_발자국_모래말미잘_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `C2A59182A0E7E7D7F23B94D94588239F647BB908EBCD6741B455ADECD1379F6A`.
- QA note: v1 is a small sand-rooted anemone witness with soft rounded tentacles, friendly expressions, and an empty flashback/thought bubble pose. Check user QA for whether it is distinctive enough, not too flower-like, and not too visually busy beside speech/flashback bubbles.
## Reference Approval - 모래말미잘 v1 - 2026-06-29

- User approved the v1 direction: "좋아 괜찮아".
- Approved official reference: `series/sherlock-fin-deep-city/references/characters/두_갈래_발자국_모래말미잘_레퍼런스.png`
- Source candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/모래말미잘_reference_candidate_v1.png`
- Dimensions: 1536x1024.
- SHA256: `C2A59182A0E7E7D7F23B94D94588239F647BB908EBCD6741B455ADECD1379F6A`.
- Main-page lock: use a small sand-rooted anemone witness with soft rounded tentacles, friendly expression, and simple silhouette that will not compete with speech or flashback bubbles.

## Reference Generation - 은모래언덕 v1 - 2026-06-29

- Generated next missing location reference after 모래말미잘 approval.
- Candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/은모래언덕_reference_candidate_v1.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/locations/두_갈래_발자국_은모래언덕_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `1584BAFED16C435ED250709CEF40040C084A3E503BA0CB41476F0E1B1E3317F2`.
- QA note: v1 is a recurring-location sheet for a quiet silver-sand path outside Deep City, including panoramic view, sand-surface closeup, footprint-depth test patch, and distant city/neon/coral-bell direction hints. Await user QA before official copy.
## Reference QA / Regeneration - 은모래언덕 v2 - 2026-06-29

- User QA on v1: the central mystery is not knowing which way the owner went, so a one-way/single-path location undermines the case logic.
- v1 status: hold/reject for reading too much like a single path.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/은모래언덕_reference_candidate_v2_open_sandfield.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/locations/두_갈래_발자국_은모래언덕_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `5ACB1647AA76D5257C4E3C791950239335B66DC1B37C7CBCA361BEB67F405570`.
- QA note: v2 reframes the location as a broad open silver-sand hill field rather than a path. The surface should allow multiple possible directions, with footprints as the actual directional evidence.
## Reference Approval - 은모래언덕 v2 - 2026-06-29

- User approved the v2 direction: "좋아".
- Approved official reference: `series/sherlock-fin-deep-city/references/locations/두_갈래_발자국_은모래언덕_레퍼런스.png`
- Source candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/은모래언덕_reference_candidate_v2_open_sandfield.png`
- Dimensions: 1536x1024.
- SHA256: `5ACB1647AA76D5257C4E3C791950239335B66DC1B37C7CBCA361BEB67F405570`.
- Main-page lock: use a broad open silver-sand hill field, not a single path. The location should allow multiple possible directions; footprints and the necklace are the only directional clues.

## Reference Generation - 산호종 약속장소 v1 - 2026-06-29

- Generated next missing location reference after 은모래언덕 approval.
- Candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/산호종_약속장소_reference_candidate_v1.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/locations/두_갈래_발자국_산호종_약속장소_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `ACA272469801A6EB68F069A13EB245733EC118396F8015D683FACEE3A20C38CB`.
- QA note: v1 is a warm small meeting spot beyond the open silver-sand hill, with a cute coral bell landmark, shell memo hooks, and safe standing space for Gabi. Check that it feels like a friendly meetup place and not a religious bell tower or one-way route marker.
## Reference Approval - 산호종 약속장소 v1 - 2026-06-29

- User approved the v1 direction: "음 좋아".
- Approved official reference: `series/sherlock-fin-deep-city/references/locations/두_갈래_발자국_산호종_약속장소_레퍼런스.png`
- Source candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/산호종_약속장소_reference_candidate_v1.png`
- Dimensions: 1536x1024.
- SHA256: `ACA272469801A6EB68F069A13EB245733EC118396F8015D683FACEE3A20C38CB`.
- Main-page lock: use a warm small meeting spot beyond the open silver-sand hill, anchored by a cute coral bell landmark. Keep it friendly and non-religious; do not make it a one-way route marker that solves the mystery.

## Reference Generation - 조개목걸이 + 새우발자국 단서 v2 - 2026-06-29

- First generated attempt was held because the footprints read too much like paw prints.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/조개목걸이_새우발자국_단서_reference_candidate_v2.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/props/두_갈래_발자국_조개목걸이_새우발자국_단서_레퍼런스.png`
- Dimensions: 1536x1024.
- SHA256: `0D90DBDDDE530D1E49BCBA0492C0F43C6F350F20E65740CFFA26BE4F193133DC`.
- QA note: v2 uses tiny repeated oval/comma shrimp-leg impressions instead of paw, human, boot, or crab tracks. It should preserve the mystery logic: same track shape on both sides of the necklace, with deeper marks before the necklace and shallower marks after it.
## Reference QA / Regeneration - 조개목걸이 + 새우발자국 단서 v3 - 2026-06-29

- User QA on v2: footprint shapes are acceptable, but both directions still ultimately read as the same direction; the two-branch tracks should spread into a V shape.
- v2 status: hold for insufficient two-way fork direction.
- Regenerated candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/조개목걸이_새우발자국_단서_reference_candidate_v3_v_split.png`
- Planned official destination after approval: `series/sherlock-fin-deep-city/references/props/두_갈래_발자국_조개목걸이_새우발자국_단서_레퍼런스.png`
- QA note: v3 preserves the tiny oval/comma shrimp-leg footprint language while making the two branches diverge clearly as a V from the necklace area. Await user QA before official copy.
## Reference Approval - 두두 베레모 v1 - 2026-06-30

- User approved continuing from the Dudu beret direction and moved on to the next reference.
- Approved official reference: `series/sherlock-fin-deep-city/references/characters/두_갈래_발자국_두두_베레모_레퍼런스.png`
- Source candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/두두_beret_reference_candidate_v1.png`
- Dimensions: 1536x1024.
- SHA256: `C8164126314DF1DA21CD7C5F98A73F943BB0D893D7170F474CA978518C8BA043`.
- Main-page lock: preserve the existing Dudu dumbo-octopus proportions from the previous reference, with the episode-specific small beret added. Do not redesign Dudu as a new octopus character.

## Reference Approval - 조개목걸이 + 새우발자국 단서 v3 - 2026-06-30

- User approved v3 after requesting that the two branches spread as a V shape.
- Approved official reference: `series/sherlock-fin-deep-city/references/props/두_갈래_발자국_조개목걸이_새우발자국_단서_레퍼런스.png`
- Source candidate: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/reference_setup/조개목걸이_새우발자국_단서_reference_candidate_v3_v_split.png`
- Dimensions: 1536x1024.
- SHA256: `125BAE44865C98F174820A27BB7F03A36CC80302AF323E1E81C9D37F75BE5C4F`.
- Main-page lock: use tiny repeated oval/comma shrimp-leg impressions, not paw/human/boot/crab tracks. The clue must read as two V-shaped branches around the necklace, with one deeper branch and one shallower branch.

## Batch 1 Prep - 2026-06-30

- Prepared Batch 1 prompt plan only; no page images generated.
- Batch scope: pages 00-03.
- Prompt plan: `series/sherlock-fin-deep-city/images/episodes/두_갈래_발자국/work_2026-06-29/batch_1/batch_1_prompt_plan.md`
- Candidate filenames planned: `00_candidate_text_v1.png`, `01_candidate_text_v1.png`, `02_candidate_text_v1.png`, `03_candidate_text_v1.png`.
- Batch 1 reference set: Sherlock Fin, Dudu beret, 은모래언덕, 조개목걸이/새우발자국 단서, 텍스트박스 layout, optional distant Deep City glow for cover.
- QA gate before generation: attach/inspect actual PNG references, preserve Dudu identity, keep the sandfield broad/open, keep page 03's clue as a V-shaped shrimp-footprint fork, and render exact Korean text from the script.