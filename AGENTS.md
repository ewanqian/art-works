# AGENTS.md — Art Works 研究与作品生产约定

This repository is the **artistic source of truth**, not the user's binary Blender archive and not an audio/GPU runtime source repository. Read README.md and the specific project lineages before editing.

## Route requests by intent

- "调查原 Blender / Simulation Zone / 是否真实复刻" → .agents/skills/artwork-evidence-review/SKILL.md
- "从旧工程提取节点 / 做 Blender Asset Browser 库 / 换音乐复用" → .agents/skills/blender-component-harvesting/SKILL.md and assets/artworks-component-registry.v1.json
- "按照我之前的品味做新视觉" → .agents/skills/artwork-style-memory/SKILL.md
- "灯光九种、批量方案 A/B 对比" → .agents/skills/nine-way-visual-audition/SKILL.md
- "下一部更完整 / 更大尺度的作品 / 史诗级视听体验" → .agents/skills/artwork-composition-architect/SKILL.md

## Non-negotiable rules

1. Keep ARTIST_RECALLED separate from SOURCE_OBSERVED, MECHANISM_TESTED, CLEAN_SCENE_TESTED, VISUAL_COMPARED and ARTIST_SELECTED.
2. Check the original artwork, source version, artist/collaborator credits, media rights, actual renderer and author's final selection. Never silently call a plan a released work.
3. Public GitHub contains source IDs, publicly discussable methods, safe documentation and original non-sensitive helper scripts. Private .blend, detailed proprietary graphs/curves, licensed audio/motion, partner scans, internal paths and customer assets remain local or in explicitly approved private storage.
4. Simulation Zone belongs in Blender GN Modifier context; do not claim a source simulation asset is a generic Node Tool. Preserve source-tick semantics before optionally designing real-time seconds handling.
5. A hundred variations are not a hundred completed works. Prefer a single strong mechanism, one source-aligned capture, two thoughtful alternatives and an explicit author KEEP/REJECT record.
6. Reuse existing performance code in ewanqian/performable-music; do not start a competing runtime in this art archive.
7. Never reset/clean another local Agent's branch or edit the same source .blend while a source-recovery job is active. Use separate working copies/branches. Public drafts are reviewable but not automatically merged.
8. A repo-level Skill is an instruction file, not proof that the Blender component, Python runner or visual output has been executed. Respect artifact readiness status.
