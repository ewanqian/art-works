# Artworks Component Registry / Blender Assets

2026-11-09 · candidate registry and extraction contract, NOT a delivered .blend library.

Machine-readable catalog: [artworks-component-registry.v1.json](./artworks-component-registry.v1.json) — 22 component candidates, each with source evidence, expected output type, reusable control ports, status and limitations. All start at NOT_EXTRACTED even where a local submechanism has been numerically tested.

## Why this exists

In the next Blender project, retrieve a proven Node Group / Material / Action / Camera by asset ID, not by searching old project folders or recreating a plausible effect from a written prompt. Keep original author compositions and source version separate from reusable mechanics.

One component has five stages:

1. Trace source paths and dependencies in a read-only source copy.
2. Extract the output-reaching node group and identify input ports and time semantics.
3. Package as a Blender Asset in a **new local private .blend**; do not write to the original.
4. Open a completely clean Blender scene; add the asset and prove a nonzero output and stable operation.
5. If useful, switch the music control or camera **without changing the source core**, capture comparison and record artist selection.

Blender Asset Browser supports Node Group, Material, Collection, Scene and other datablocks. A **Simulation Zone belongs in the Geometry Nodes Modifier context**, not the Node Tool context; provide a modifier wrapper and test scene for source Drop Flow.

Relevant Blender references:
- https://docs.blender.org/manual/en/5.0/files/asset_libraries/introduction.html
- https://docs.blender.org/manual/en/5.0/modeling/geometry_nodes/tools.html
- https://docs.blender.org/api/5.0/bpy.types.ID.html
- https://docs.blender.org/api/5.1/bpy.types.BlendDataLibraries.html

## Recommended first assets

| Candidate | Evidence so far | Extract as | First proof |
| --- | --- | --- | --- |
| DF-LIFETIME-001 | source lifetime subchain: 482 reported GPU checkpoint comparisons | GN subgroup + source-tick simulation wrapper | independent new file, surviving IDs and lifetime timing |
| DF-BIRTH-001 | actual birth path observed | GN Modifier subgraph | source-aligned birth and geometry count over consecutive frames |
| DF-AUDIO-001 | sampled curves seen, original bake provenance not proven | private Action/FCurve + adapter | same visual core, different offline music envelope |
| RCT-CURVES-001 | author account; selected source not yet recovered | scene rig / Curves / GN | exact authored structure reveal and local light |
| HERO-WAVE-001 | author account; original shader uninspected | Material | scan appearance with neutral permitted geometry |
| TMR-SCREEN-001 | author account | Camera/Collection | actual square-to-wide reprojection, not image crop |

Do not assume every KASHIWA branch is a separate Node Group: several may be one stable core plus different control curves, materials, lighting and camera. Do not package unidentified copyrighted audio, customer scans or proprietary source materials into a public repository.

## Folder convention (local/private, not yet created)

    ARTWORKS_LOCAL_PRIVATE/
      originals/               read-only source + hashes
      extraction/              test and dependency review
      blender-asset-library/   Artworks_GN_Core.blend, Materials.blend, Camera_Rigs.blend
      validation/              independent-source and music-swap tests
      author-selections/       accepted and rejected comparisons

Official Blender Python library.write also saves indirectly referenced datablocks. Packaging automatically can therefore expose linked objects, images and original customer materials. The local agent MUST inspect dependencies and rights before bundling or sharing. The public registry contains only generic references and IDs; exact private curves, nodes and paths remain local.

### Delivery contract

COMPONENT_ID; SOURCE_VERSION; EXTRACTION_STATUS; PACKAGE_TYPE; PUBLIC_SAFE_MECHANISM; CONTROL_PORTS; TIME_SEMANTIC; DEPENDENCIES; NEW_CLEAN_FILE_TEST; SOURCE_PARITY_EVIDENCE; MUSIC_SWAP_EVIDENCE; AUTHOR_CHOICE; RIGHTS_STATUS.

Status advances only from NOT_EXTRACTED to PACKAGED to CLEAN_SCENE_TESTED to ARTIST_SELECTED, on real tested artifacts. A visually good new effect without origin evidence must be labeled NEW_STUDY, never recovered source.

See [the overall Artworks system](../plans/2026-11-09-artworks-compounding-system.md), [source verification skill](../.agents/skills/artwork-evidence-review/SKILL.md), and [component extraction skill](../.agents/skills/blender-component-harvesting/SKILL.md).
