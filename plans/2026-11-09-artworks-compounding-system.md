# Artworks System 01 — 从旧作品到可演奏的新作品

**记录**：2026-11-09 · 艺术策略 / 可执行研究框架，非新作品发布声明。  
**问题**：如何让 TIMER、Drop Flow、KASHIWA、NFIR、Entropy、REACTOR、HERO DOME 与二砂的既有知识，不止以档案形式存活，而是形成长期可以生产更高完成度、规模化实时作品的**作者资产和编排系统**？

> **总原则：不是将所有旧作品合成一种风格，而是将“已发生的机制、作者选择和时间方法”转换为可以再次组合的新材料。** 有的作品应保留独立身份，有的只提供技术/审美模块。拥有一组节点 ≠ 完成一件作品；拥有更大的 GPU ≠ 形成更强的艺术叙事。

## 1. 五层体系：档案 → 组件 → 乐器 → 编排 → 作品

| 层 | 内容与作者控制权 | 机器可做 | 何谓成果 |
|---|---|---|---|
| **Memory / Original** | 原工程、版本、署名、片段、回忆、选择与拒绝的理由 | 搜索、核验、分辨来源 | 一项能定位到原工程的事实，或经过明确标识的作者回忆 |
| **Components / Grammar** | 可重用的发射、寿命、波场、线框 Reveal、扫描材质、相机与控制数据 | 递归拆图、清理外部依赖、包装、测试 | 独立新 Blender 文件里能调用的节点/材质/镜头，并能复现机制 |
| **Instrument / Runtime** | 将作者选择过的视觉规则变为能“停、变、等、续、触发”的演出乐器 | GPU kernel、事件桥、录制回放和故障恢复 | 同一视觉核心可以由离线曲线和至少一种新输入驱动；有真实画面 |
| **Composition / Dramaturgy** | 声音、镜头、层次、变化、停顿、冲突及空间关系 | 为同一作者意图生成 A/B 候选、计时、镜头预演 | 一个没有屏幕说明也能被观看、愿意看下去的完整段落 |
| **Artwork / Public** | 最终挑选、命名、署名、作品哲学、情感冲击、展演形式 | 对齐不同屏幕/设备输出、保存工程、证据和访谈素材 | 作者认可且有准确技术/演出证据的一件独立作品 |

层与层之间只传**清楚的契约**。艺术家对原始风格、构图、音乐判断和最终选择保有权力；Agent 是取证、探索和技术生产的协作者，不是以模型默认美学替代作者。已有 [Hybrid Authoring Architecture](https://github.com/ewanqian/performable-music/blob/main/visual-runtime-lab/HYBRID_AUTHORING_ARCHITECTURE.md) 明确“作者内容优先、镜头默认 HOLD、Runtime 负责切换与同步”；这份规划继承它，不建立第二个冲突的音乐中控。

## 2. 从已有作品抽出的不是“风格名”，而是可以组合的语法

一个可继承的 **Method Card / 方法卡** 至少要存：

- **Source**：哪一件作品、源版本及确切场景/镜头/节点入口；
- **Mechanism**：实际的数学/几何/渲染过程，哪些已验证；
- **Time grammar**：按 tick、连续曲线、乐句、人工触发还是关键帧；不要自动把一切改成 BPM；
- **Spatial composition**：摄像机、尺度、方向、屏幕画幅、留白与观众距离；
- **Sound relation**：与已烘焙的原始音频曲线、可替代的新音乐、实时节拍/人工事件的关系；
- **Chosen/Rejections**：作者认为动人的片段、失败版本及为什么不保留；
- **Reuse boundary**：可以更换什么、不能更换什么、授权许可及依赖；
- **Next mutation**：它可以朝哪些与旧作品有辨识关联、但具有新意的作品方向发展。

### 用一张真实的创作谱系表指导提取

| 源作品 | 可继承主干 | 可以改变的部分 | 一次有意义的“进化” |
|---|---|---|---|
| **TIMER** | 俯拍钟面场景、圆形→宽屏几何/镜头转译、时间线与音乐 Bake | 新的播放空间/屏幕关系、时间控制曲线 | 将空间转译独立成镜头/屏幕乐器，而非再造一个钟 |
| **Drop Flow** | 带状态的每帧出生、几何反馈、寿命与场/删除规则 | 音频曲线、相机、密度、时间方式，须保护原本运动机制 | 从“难以控制的模拟”变成可调可演奏且忠于源规则的状态系统 |
| **KASHIWA Amb / Ice** | 同一母系统的分支、从音乐结构到视觉的控制经验 | 情绪、卡点/流动节奏、光和演奏角度 | 一套主干服务不同曲目的差异化编排，不是给每首歌套同款粒子 |
| **NFIR** | 简化规则持续生成 + 作者观察/操作两个时间层 | 边数、角度、观察轨迹、对比剪辑 | 让人的注意、观察和选择成为作品可被感知的第二个系统 |
| **Entropy → REACTOR** | 合理机械拓扑由线出现、转换为 Curve、高亮/局部材质 | 结构主题、Reveal 相位、灯位、镜头、投影位置 | 从单一华丽 Reveal 发展到能分析、拆解、改变状态的可演奏机器 |
| **HERO DOME** | 超宽空间中的 Wave/ColorRamp/线框/噪声合成、亮度组织 | 演出尺寸、扫描方向与时间、光的主次 | 不只是扩大画布，而是让空间与音乐编排有清晰层次 |
| **二砂 / ERSHA** | 扫描色彩属性、深度穿行的相机、点云影像 | 选取已授权建筑内容、相机速度与新灯光 | 把采集现实世界与生成图像建立新的“空间内外”关系 |
| **Motion Capture** | 舞蹈动作时序资料（已知部分公开版；新 VR 实验未完成） | 多时间片复制、观察者/舞者视角、实时输入 | 让身体的时间留下可重排的空间痕迹，前提是素材和许可通过 |

**以上的状态不相同**：DF 的局部寿命数学有已报告的本机验证，REACTOR/HERO DOME 具体 Shader 尚待本地取证；Mocap 360° VR 是方案，不是成片。素材确权前不得将商业源工程“模块化”后公开。

## 3. 近期就能使用的 Blender 资产路线

**先有一个可用的 `.blend` 资产包，而不是先建一个抽象节点平台。**

建议本地工作空间（实际路径由本地 Agent 选定；不在公共仓库记录机器地址）：

```text
ARTWORKS_LOCAL_PRIVATE/
  originals/              # 只读源工程+校验表
  extraction/             # 逐作品副本、节点组、依赖检查
  blender-asset-library/
    Artworks_GN_Core.blend
    Artworks_Materials.blend
    Artworks_Cameras_and_Rigs.blend
    Artworks_Showcase_Tests.blend
  validation/
    DF-LIFETIME-001/      # 清洁工程+数值/可视对照
    RCT-CURVES-001/       # 恢复后才能打包
  author-selections/      # 被选中和被淘汰的证据
```

公共 **[`assets/artworks-component-registry.v1.json`](../assets/artworks-component-registry.v1.json)** 只保存候选模块 ID、源项目、证据等级、准备方式、可交换控制与尚未完成的验证；精细节点和商业文件保存在本地私有工作空间。所有候选初始为 `NOT_EXTRACTED`，包括在 GPU 数值对照已通过但尚未作为 Blender 资产打包的 `DF-LIFETIME-001`。

**第一个可证明完成的资产：DF-LIFETIME-001。** 采用真实 lifetime 子组，加一个小型 Simulation Zone 测试 wrapper，使它能在新的独立 .blend 场景里自行推进。复验原始按 tick 的更新/删除后标为 `CLEAN_SCENE_TESTED`。不需要先复原整套 Drop Flow 的场、音乐和大型渲染；这一步就是把技术考古转成可用资产。

**第二个资产（并行恢复，不要求已经完成）：RCT-CURVES-001。** 本地 Agent 找到真实 REACTOR Reveal 和作者选中版本后，抽离 Curve/材质/时间控制，配一个中性机器结构作为测试，输出一段有线条、局部高亮、相机与完成质感的短视频。不要从口述重新编一个“类似的”动画冒充抽取。

**第三个资产（作者构造，可后做）：COMMON-CTRL-001。** 一个与艺术形态分离的音乐输入转换层：`ORIGINAL_CURVE / NEW_TRACK_ENVELOPE / MIDI_BPM / OSC / MANUAL`，映射成统一的数值曲线，允许随音乐改编而保留原核心的实际更新机制。注意 source tick 与实时 seconds 是不同语义，必须显式选择。

Blender 官方可将 Node Group / Material / Collection / Scene 作为 Asset，在新文件中引用。Simulation Zone 只适合 Geometry Nodes Modifier 上下文；不能说把它标成资产就能在 Node Tool 环境直接运行。

## 4. 自己的 Runtime：不要从零再造另一个 Blender

你的独立 Runtime **不必复制 Blender 编辑器、节点 UI 或所有渲染功能**。它的第一版只需要能将“已验证的源机制”准确跑起来，并提供能在演出中控制的输入和画面输出。

```text
BLENDER AUTHORING                     AUTHOR / MUSIC
GN core, curves, cameras, materials   Ableton / Show Score / MIDI / OSC
        |                                      |
  offline export                           control mapping
        |                                      |
        +-- [Artworks Component Contract] -----+
                         |
                deterministic time/state
                         |
                Native GPU Compute (Mac Metal / Windows API)
                         |
                Draw / composite / stage output
                         |
                  Record/replay + fallback
```

**分层是关键：**

- `Asset/Compiler`：解析真实源工程，抽取结构与规则；初期人工挑选节点/重建映射，不承诺通用 GN 编译器。
- `Simulation Kernel`：具体的出生、状态与 Curl/Wave 等可并行部分；保留 `SOURCE_TICK_COMPAT`，另设 `REALTIME_DT` 可选演奏模式。
- `Rendering`：粒子、线、实体、材质、发光/扫描和视频；REACTOR Curve/Shader 不必硬塞进模拟 Kernel。
- `Conductor/Events`：接现有 Performable Music 的 Show Score、MIDI、OSC、音频，不建立互相打架的第二个“节拍中枢”。
- `Performance`：手动 CUT/HOLD/REVEAL/FREEZE、失联回退、独立黑场和回放；舞台角色明确。

**跨平台建议**：Windows 的 RTX/Compute 实现继续用于源机制对照；Mac Swift+Metal 做原生表演输出的最小真实试验；长期若需要单份通用 shader，可以考虑 Rust/wgpu 或共用数据协议。现在先保证数据契约一致，不抢先承诺三套程序全部写完。

已有 [Performable Music Hybrid Authoring Architecture](https://github.com/ewanqian/performable-music/blob/main/visual-runtime-lab/HYBRID_AUTHORING_ARCHITECTURE.md)、[Visual Runtime Build Brief](https://github.com/ewanqian/performable-music/blob/main/visual-runtime-lab/AGENT_RUNTIME_BUILD_BRIEF.md) 负责现场运行代码；art-works 只负责创作语法与复用契约。避免新建重复工程。

## 5. 何为更高完成度、甚至具有“史诗感”的作品

不要把史诗感定义为更多粒子、更多文字、24 个自称原创的片段或更长时长。作品需要从**漂亮镜头**走向**能被观看的结构**：

1. **世界和矛盾**：一个有内在规则的视觉世界，在什么条件下变得不稳定、需要回应、产生变化？
2. **可读的变化**：观众能看到“原来是什么 → 发生了什么 → 代价/后果是什么”，不必理解技术参数。
3. **时间设计**：不只是 Build→Drop→闪烁，也有停顿、积累、接近崩塌与意外恢复。
4. **空间设计**：镜头与人的尺度关系、巨物和细节、前景和远景、LED/XR/穹顶之间真正不同的观看关系。
5. **音乐有独立生命**：声音先能独立成立；视觉不只是给音乐可视化“加背景”，而是和声部、节奏/段落共同推进。
6. **人能介入**：作者或表演者知道何时等待、何时触发、何时将运行中的系统带到意外状态；一次演出不是播放 UI Demo。
7. **留下证据**：从排练片段、试演到正式作品，都能保留原工程、决定过程、输出版本与准确署名。

### 一个可选的未来旗舰方向（不是新建已完成作品）

临时研究题目：**The Instrument That Remembers / 记忆仪器**。这只是把已有独特语法做一次有效结合的构想，可以不采用。

- **Act A / Structure**：从 Entropy/REACTOR 的真实机械拓扑逐步显形，建立一个可信且庞大的空间结构；
- **Act B / State**：Drop Flow 的有记忆状态改变机器/环境，让积累下来的时间变成空间中的现象；
- **Act C / Observer**：NFIR 的作者观察或身体时间介入；相同系统因观察方式/时间重排而变成另一种画面；
- **Act D / Performance**：声音与空间输入共同控制系统的命运，系统可以继续演奏、停止或返回；
- **Resolution**：一段真正由作者选择的结尾，不依赖无休止的重复高潮。

它成立的条件是四幕有**必要因果关系**，而非把四个旧作品的视觉拼贴在一起。若无法说明每幕改变了世界中的什么，那就不应该进入旗舰作品。

## 6. 当下产物：一条最小可用的艺术-技术闭环

与本地正在查找 REACTOR 的 Agent 并行，独立建立：

**First reuse proof / 同一资产、不同音乐、两个状态：**

- 一个原始且有证据的视觉组件（首先用 DF 的寿命节点测试 wrapper；若需要观众可读的画面，可先用现有合法的作者渲染画面）。
- 一段经过作者挑选而非 Agent 假定“高质量”的音乐片段。
- 同一组视觉核心分别接**原始音频曲线 / 一组不同的音乐控制曲线**，控制方式分开，不改变核心状态语义。
- 一个清洁 Blender 工程能加载该核心，并截取两个连续输出片段。
- 作者只回答：哪一段值得留、为什么？如果都不值得，记录明确的淘汰理由，而不是新增九套无效方案。

以上证明“原作积累能够进入下一轮音乐与画面创作”，才开始把同一段逻辑搬入 Mac/Windows 原生 Runtime。

## 7. 近日可以做的 / 暂存为长期研究的

### 现在就做（不干扰正在进行的本地调查）

- 公开保存这份**方法与架构**以及机器可读候选资产目录；精细真实配方不公开；
- 本地 Agent 完成 `DF-LIFETIME-001` 单节点组资产的清洁工程验证，及 `RCT-CURVES-001` 的真实源定位；
- 现有用户最满意的 Ableton 版本先恢复音轨/工程，选一个唯一可听段落；不继续批量生成无效音色；
- 用同一段音乐和一组源画面，制作一个具有明确音乐/视觉状态改变的 **30–90s** 小段；作者对照选择；
- 本地原始工程与公开资产目录通过脱敏 ID 关联，避免未来模型找不到曾经的好镜头。

### 存作中长期研究（有专属文件，不立刻开工）

- 更完整的 Blender GN / Simulation Zone→ GPU 编译或半自动转译；
- 多 GPU 后端与 Apple Metal / wgpu / TouchDesigner POPs 的机制、性能对照；
- 从作品源资产中自动提取“阶段、变化、镜头与作者选择”的研究知识图谱；
- Drop Flow × Motion Capture 的多时间轴舞者复制、360° VR 身体观看；
- 复杂信息密度与结构感足够强、能够真正按音乐剧场式编排的跨屏幕旗舰作品；
- 长期维护可搜寻的作品采访/出版/研究记录与作者口述，禁止混入未经确认的事实。

**唯一晋级原则**：来源清楚 → 机制正确 → 能在新文件独立使用 → 视觉/听觉由作者认可 → 才进入正式 Runtime 与新作品。缺任一项，不自动“宣布成功”。

## 8. 存放分工

- **art-works（公开）**：原创作品身份、谱系、方法、风格选择、组件 ID、演化路线与脱敏技术证据；
- **私有 Blender 工作区**：真实 `.blend` Node Group、Material/Collection、模型、Curve、源音频控制数据和截图/片段；
- **performable-music**：实际的 Show Score、合成/音频/控制适配器、原生 Metal/WebGPU/OSC Runtime 与演出版本；
- **portfolio**：经过公开权利/署名/审美与技术审阅的发布版本、精选片段及 Writing。

与 [Artifact Evidence Review](../.agents/skills/artwork-evidence-review/SKILL.md)、[Style Memory](../.agents/skills/artwork-style-memory/SKILL.md) 和未来的 `blender-component-harvesting`、`artwork-composition-architect` 两个 Agent Skills 协作；这些是**工作的操作程序**，不是一种预设的美学滤镜。
