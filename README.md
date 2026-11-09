# Art Works / 艺术创作档案

Ewan Qian · 2026– · **Artistic concepts, works in development, lineages and editorial planning**.

This repository is the **artistic source of truth** for original work concepts and relationships between works. It is **not** a substitute for source-code repositories, a release archive, or the public portfolio.

## Where things live

| Subject | Canonical repository | This repository records |
| --- | --- | --- |
| Artwork concepts, ideas, artistic research lineages | **art-works** | Concept, intent, evolution, references, dependencies and status |
| Performable compositions, realtime AV, Metal/OSC, Show Score | [performable-music](https://github.com/ewanqian/performable-music) | Artistic meaning and relationship to works only |
| Individual work implementations | Existing individual project repositories, e.g. `no-further-input-required` | Pointer and creative brief; no duplicated code |
| Selected work, CV, published articles and evidence | [portfolio](https://github.com/ewanqian/portfolio) | Links to published presentation, no automatic claim of completion |
| Drop Flow source motion data | [dropflow-biennale-mocap](https://github.com/ewanqian/dropflow-biennale-mocap) | Attribution and reuse decisions only |
| Private performance originals | Their existing **private** repositories | Public-safe abstract descriptions only; never copy unapproved assets |

## Organizing principle

- `works/` — one file per artwork or artistic proposal; preserve original identity over time.
- `lineages/` — recurring visual, sonic and conceptual languages across works.
- `plans/` — priorities and proposed work, explicitly differentiated from completed results.
- `references/` — ownership, evidence and cross-repository routing.

Do **not** classify an idea as a finished work because an agent generated a prompt, a prototype exists, or a website placeholder was created. Each record should distinguish **PROPOSED**, **IN DEVELOPMENT**, **PRESENTED (with evidence)** and **UNVERIFIED**; different versions of one work may have different states.

## Scope and rights

This is a **public** repository. No private client assets, unlicensed media/code, credentials, private messages, raw personal information, or private-performance source exports. An external artist's method is a study reference, not authorization to copy their materials. Keep fact, inference and future creative intention separate.

## 2026-11-09 作者口述：从 Blender 到实时视觉

- [TIMER → Drop Flow → KASHIWA → NFIR → SRE / Entropy](lineages/2026-11-09-timer-drop-flow-realtime-author-account.md) — 作者一手创作史料；区分旧作品、未完成探索与代码机制。
- [Entropy → REACTOR → HERO DOME / Ableton / 二砂](lineages/2026-11-09-reactor-hero-dome-audio-ersha-author-account.md) — 模型 Reveal、线框曲线、Shader、音乐质量及点云复用。
- [可供 Agent 查询的创作偏好 JSON](lineages/2026-11-09-creative-preferences.json) — 情境性喜好与明确避免的错误归因。
- [Drop Flow Simulation Zone → GPU 技术交接](plans/2026-11-09-simulation-zone-gpu-local-agent-brief.md) / [REACTOR-Ableton-二砂恢复交接](plans/2026-11-09-reactor-audio-ersha-local-agent-followup.md) — 本地代理只读取证、实际资产发现与私密素材保护。

- [Drop Flow 源工程恢复核验 01](lineages/2026-11-09-drop-flow-source-recovery-checkpoint-01.md) — 实际状态链取证、局部 GPU 数值对照与旧复现偏差；完整工程与配方保留本地私有目录。

以上为作者口述及研究交接，未确认的 Blender 节点、工程版本与交付情况不得自动升为已发表作品事实。

## 2026-11-09 艺术复利与 Blender 节点资产库（待审核）

- [Artworks System 01 — 从原工程到可演奏的完整作品](plans/2026-11-09-artworks-compounding-system.md) — 区分原作、组件、Runtime、作品编排与正式呈现。
- [Blender Node / Material / Camera 资产目录与清洁工程验收](assets/README.md)；[22 个候选组件机器可读索引](assets/artworks-component-registry.v1.json) — **均尚未包装交付为独立 .blend 资产**。
- [源工程验收 Skill](.agents/skills/artwork-evidence-review/SKILL.md)、[组件提取 Skill](.agents/skills/blender-component-harvesting/SKILL.md)、[创作风格记忆 Skill](.agents/skills/artwork-style-memory/SKILL.md)、[九方案对比 Skill](.agents/skills/nine-way-visual-audition/SKILL.md)、[完整作品编排 Skill](.agents/skills/artwork-composition-architect/SKILL.md)。
- [Blender 私有资产侦测与选择性导出脚本](tools/blender_asset_scout.py) — 需在 Blender 本机运行，**仅执行代码静态编写、未在实机执行或验证导出**；默认仅查阅，明确授权后才可将选择的 group 导出到新的私有 .blend。
- [本地研究成果审阅准则](references/2026-11-09-local-research-quality-check.md)。

## Initial cross-repository index

- 《无需进一步输入 / No Further Input Required》 — see `works/no-further-input-required.md` (artistic identity); original implementation remains separate.
- 《反向神经谱 / Reverse Neural Score》 — see `works/reverse-neural-score.md` (provisional concept for a musical/neurological-feedback performance).
- Artistic grammar and reuse principles — `lineages/2026-creative-vocabulary.md`.
- Planning and status — `plans/2026-work-register.md`.

**Last established:** 2026-11-09. Implementation and release status must be verified against the relevant project repositories before public use.
