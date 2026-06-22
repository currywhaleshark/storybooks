# Batch 1 Fixed Seating Rework Prompt Plan - 2026-06-22

## User QA Problem

- Reference fidelity is good.
- The failing issue is continuity: the children keep changing seats from page to page.
- Regenerate pages 01-03 with a fixed seating map. Do not solve this by changing character designs.

## Fixed Seating Map

- Seating map asset: `work_2026-06-21/batch_1/batch_1_fixed_seating_map_v1.png`
- Camera orientation is locked:
  - top of page = back wall / teacher side
  - bottom of page = front edge / reader side
  - do not rotate, mirror, or reinterpret the map
- Same central round/shell toddler table across pages 01, 02, and 03.
- Same chair/stool positions, same neighbor order, same table direction, same tableware positions.

## Seat Assignments

- Mongle: front-left seat, closest to reader. He is the action focus in all three pages.
- Aru: front-right seat.
- Lulu: right-middle seat.
- Sua: back-right seat.
- Popo: back-center seat.
- Jun-i: back-left seat.
- Tori: left-middle seat.
- Banguli: floating near Mongle, not seated.
- Mari teacher: standing/serving/supervising near the back/right service area, not seated with children.

## Generation Locks

- Use the no-bag indoor character references for all visible characters.
- Preserve the improved reference fidelity from the previous pass.
- The only major correction is fixed blocking/seating continuity.
- Characters may change pose and facial expression by page, but they must not swap seats or vanish from the same dining-table arrangement.
- Page 01: friends are already seated; Mongle is at/near the front-left seat, arriving or settling beside his stool, not on the tabletop.
- Page 02: same seating map; Mongle remains front-left and wiggles tentacles from that seat; Mari remains standing/serving/supervising, not seated/eating.
- Page 03: same seating map; Mongle remains front-left and plays with rice ball/soup from that seat; all friends remain seated including Popo.
- Text QA remains deferred to user; no local opaque text panel overlays.

## New Candidate Names

- `01_candidate_text_v7_fixedseats_v1.png`
- `02_candidate_text_v5_fixedseats_v1.png`
- `03_candidate_text_v5_fixedseats_v1.png`