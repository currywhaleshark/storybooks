# Reference Asset Plan - 수아의 잘 보는 눈

## Special Coral Hairpin

Purpose: recurring episode prop. Lulu wears this special one-day accessory, loses it in the yard sand, and Sua finds it with her careful eyes.

Approved design direction:
- Mint/aqua soft coral twigs with rounded child-safe tips.
- Cream star-shell accent near the center.
- Two or three tiny pale-yellow bead-like nubs.
- Clearly different from Lulu's coral-pink body so it reads on her head and in sand.
- Preschool-appropriate, not a gold crown, gemstone tiara, adult jewelry, or exaggerated princess accessory.

Approved reference inputs for generation:
- Official Lulu no-bag reference: `series/coral-town-daycare/references/characters/no_bag/루루_no_bag.png`
- Standalone hairpin reference: `reference_assets/special_coral_hairpin_ref_v1.png`

Node-emitted candidate for user QA:
- `reference_assets/lulu_node_emitted_special_hairpin_candidate_v1.png`
- Generated after emitting the official Lulu no-bag PNG and standalone hairpin PNG into the chat context with `nodeRepl.emitImage`.
- Status: user approved as the Lulu-wearing-special-hairpin reference on 2026-06-24. Use it for Lulu wearing the accessory; still use the standalone hairpin reference for loose-prop scenes.

Usage locks:
- Use `special_coral_hairpin_ref_v1.png` whenever the loose accessory is visible: cover/page 00, page 05, page 06, page 07, and page 08.
- For Lulu wearing the accessory, load the official Lulu no-bag reference and the standalone `special_coral_hairpin_ref_v1.png` together.
- Use `lulu_node_emitted_special_hairpin_candidate_v1.png` when Lulu must be shown wearing the special accessory; use official Lulu/no-bag plus standalone hairpin if a fresh page generation needs stricter identity control.
- Keep the accessory small enough for a 3-year-old seahorse child, but readable as mint coral plus cream star-shell.
- Do not recolor it pink; it must not blend into Lulu's body.

Rejected/unused direction:
- Earlier pink coral ornament draft was rejected because it was too close to Lulu's body color and too similar to her ordinary decoration.
- Generated wearing-Lulu candidate was rejected because it drifted from official Lulu.
- Local composite wearing-Lulu candidates were rejected because they looked awkward.
- Current approved wearing reference: `lulu_node_emitted_special_hairpin_candidate_v1.png`. Keep rejected generated/composite files as history only.



Lost-prop continuity lock:
- When the story image shows the hairpin as lost/found in sand, do not also show Lulu wearing the same special hairpin.
- Cover/page lost-object scenes should use the standalone hairpin as the only special mint/aqua star-shell hairpin in the image.
