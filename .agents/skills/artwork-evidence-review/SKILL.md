---
name: artwork-evidence-review
description: Review Blender artwork archaeology, source asset recovery, Geometry Nodes or Simulation Zone extraction, GPU port claims, and audiovisual reproduction. Use when judging whether a local Agent truly recovered an existing artwork rather than merely making a plausible new effect.
---

# Existing Artwork Evidence Review / 原作调查验证

**Purpose:** Give one bounded independent review of **what was actually verified**. Never open/rewrite original sources unless the user explicitly asks and access/rights allow it. Prefer the source report, diffs, frame captures, code/test output and private manifest available locally. A public summary alone does not establish independent test reproduction.

## Inspect only the necessary evidence

1. **Original identity:** exact project/version, source SHA-256, Blender build, dependency state, read-only preservation. Different saved frame settings alone do not establish an algorithm change.
2. **Active mechanism:** trace the actual output-reaching node chain recursively. Separate Simulation State socket declarations from Geometry attributes; distinguish source birth, persistence, transform, deletion, input curves and render output. Do **not** add assumed velocity integrators or respawn rules.
3. **Input provenance:** classify each curve as `observed sampled FCurve`, `documented audio bake`, `manual keyframe`, `object transform`, `scene time` or `unknown`. Do not call shared outputs independent audio bands. Do not call rhythmic response a beat detector without proof.
4. **Numerical result:** capture source program, comparison implementation, specific variables, sample count, valid ranges, tolerance, random seed and whether the result came from a true Blender operation or a rewritten reference. A frame-rate x frame checkpoint count is not a count of independent artworks.
5. **Visual/performance result:** require consistent source/runtime camera and frame, matching input control window, consecutive frames or video, aligned geometry and material distinctions. Separate mechanism parity, render parity, and **artist approval**. Do not confuse cached playback with live simulation.
6. **Conflicts and privacy:** do not publish raw commercial source, fine-grained shader recipes, music, motion capture, private paths, licensing information, or unapproved source assets.

## Decision: label the *claim*, not the entire project

Use only:
- `SOURCE_OBSERVED` — exact source node or asset observed, not independently run.
- `MECHANISM_TESTED` — bounded test with stated input, output and tolerance.
- `VISUAL_COMPARED` — source/runtime paired captures under same conditions.
- `ARTIST_SELECTED` — real author selection and reason recorded.
- `NOT_TESTED` / `CONFLICT` — open items.

For Drop Flow 2026-11-09: treat the 482 reported lifetime-GPU comparisons as **bounded mechanism evidence**, NOT a full Simulation Zone migration, visual pass or FPS benchmark. The source lifetime subchain advanced by **tick** in that test; respect source-tick behaviour until a separate time-seconds mode is chosen and compared.

## Return concise review

```
Original: version / evidence ID
What is genuinely established: [one or two claims with evidence]
What remains unknown or contradicted: [one or two]
Artist-experience risk: [why a technically correct result might still lose the work's character]
One smallest next test: [a concrete source/runtime paired comparison]
Public-safe record: [short summary, with no proprietary values]
```

Do not invent a numeric score or a calendar. Avoid re-requesting the lifetime test once a valid report already establishes it; advance to birth, Curl/Wave gating, geometry topology, camera and auditory conditions. To assess visual style rather than source truth, use the separate `artwork-style-memory` skill.
