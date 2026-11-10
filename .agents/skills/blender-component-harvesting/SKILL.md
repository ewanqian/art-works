---
name: blender-component-harvesting
description: Turn an existing verified Blender artwork source into reusable Geometry Nodes, Materials, Actions or Camera/Scene assets in a new local Asset Browser library. Use when an existing work should be modularized, reused with another song, or translated to GPU. Never claim a package exists before extracting and clean-scene testing it.
---

# Blender Component Harvesting / 从作品中提取可调用的组件

Read the project's source recovery report, [component registry](../../../assets/artworks-component-registry.v1.json), [assets README](../../../assets/README.md), and [artwork evidence review](../../artwork-evidence-review/SKILL.md). This public skill does not include binary assets or the user's private local paths.

## First test: extract only what source evidence supports

1. Match an asset ID to a source file through **the private local manifest**. Use the actual Blender version where possible. Hash source before/after. Open a copy in a separate process, never overwrite source or invalidate original caches.
2. Recursively trace the original active output chain, including nested node groups and Geometry attributes. Mark clearly which sockets are persistent state, initial values, externally driven controls and unconnected declarations. Do not use a generic velocity/resurrection algorithm unless present in the source.
3. Partition **mechanism / presentation / control**: Geometry Nodes simulation may need Modifier wrapper; Shader/Compositor groups, cameras, materials and sampled FCurves are separate asset types. A KASHIWA music branch may be a recipe of multiple components rather than a new simulation graph.
4. Preserve source-tick update semantics. Name any new per-second or real-time behaviour separately and test it against original.
5. Create a new local .blend asset package, registering only the chosen data-block and reviewed dependencies via Blender Mark as Asset / bpy asset_mark. Do not batch-export every referenced object; Blender library writes also gather indirect dependencies. Check licensing and hidden images/audio/scans.
6. **Clean-scene test**: append/link the asset to a fresh untethered .blend and prove useful output, deterministic state reset and geometry/material compatibility. A node subgroup might need a wrapper and cannot be expected to render on its own.
7. **Music swap test**: replay the original curve, then a separate new allowed music envelope through one declared control adapter, without changing the original simulation core. Source image/audio rights remain private. Show both time-matched output sequences, never infer approval.
8. Record author selection: choose or reject, with two reasons. Only then promote to ARTIST_SELECTED / REUSABLE in registry.

## Immediate asset candidates

- DF-LIFETIME-001 — original lifetime subnode numerically tested locally (482 tick comparisons); **NOT yet packaged**. Extract group with minimal GN Simulation Zone wrapper, source-tick compatibility and clean-scene proof. Do not rerun this old test to claim new asset validation.
- DF-BIRTH-001 / DF-FEEDBACK-001 — already observed real path, not yet tested for full GPU or visual parity. Packaging requires source and shape/state verification.
- DF-AUDIO-001 — original sampled curves are not automatically a “real beat detector.” Keep original curve data local. New Track/MIDI/OSC is a separately authored adapter with explicit time mapping.
- RCT-CURVES-001 / HERO-WAVE-001 — currently author-recalled, local recovery still needed. Do not fabricate a similar structure and label it a recovered asset.

## Deliverable (short)

For each component: `COMPONENT_ID / SOURCE_ID / PRIVATE_PACKAGE_PATH / PACKAGE_SHA256 / Blender version / extracted dependency list / interface sockets / timing / clean-scene status / short video or frame proof / music-swap evidence / rights / author decision`.

The public GitHub response gets only component ID, method and verification tier; exact original source names, hard-coded parameters, commercial node recipes and private media stay local. Do not overwrite an active parallel Codex/Blender file or change another Agent's source branch.
