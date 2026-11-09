# Blender → GPU Runtime：技术生态调查与并行验证路线（2026-11-09）

> **状态：Cloud technical survey / 2026-11-09，非已部署或本机验收。**  
> **目标工程：** Drop Flow Geometry Nodes Simulation Zone、TIMER 音频 Bake 与镜头、KASHIWA 分支、NFIR、REACTOR 的曲线/线框和 HERO DOME 材质，以及 SRE/Entropy 现场控制。  
> **作者需求：** 将已有 Blender 创作逻辑转换成在 Windows RTX / Apple Silicon Mac 上原生运行的 GPU visual instrument，不接受只模仿结果的通用粒子特效。  
> **本报告与正在运行的本地 Agent 工作并行**。不访问、不改动它的 Windows/NAS/Mac 源文件。本地工程的真实节点连接及已有效运行的演出状态必须以后续证据为准。

## 2026-11-09 源工程检查点反馈：对本报告状态设计的必要修正

最新的 [Drop Flow 源工程恢复 Checkpoint 01](https://github.com/ewanqian/art-works/blob/lineage-oral-history-blender-gpu-20261109/lineages/2026-11-09-drop-flow-source-recovery-checkpoint-01.md) 已在 Blender 原件中验证寿命子链与 GPU 的局部数值一致性。该证据只覆盖此子链，未证明完整模拟或画面等价，但应立即更正后文所有通用“粒子模型”假设：

1. **Simulation Zone 声明的 state item ≠ 每帧真正变化的几何属性。** 原作品实际持续状态需由真实几何和有效连线提取，不能按 six slots 生成 six GPU fields。
2. **不要虚构 velocity/acceleration 积分器。** 下方 `position/velocity/age/life` 是候选 ABI 范例，不代表源工程都存在这些字段。移植需以可读的自定义 Geometry Attribute、原始 Curl/Time/Noise 链和实际出生/删除/保留规则为准。
3. **保留作者原工程的 tick-based 更新。** 寿命局部子组的当前已验证条件为按 tick 推进；在 24/60fps 的受控夹具里相同 tick 有相同数值。此事实不能外推为整套现场系统 FPS 无关，也**不能自动把该规则改写为 `delta_time_s` 更新**。先做 `SOURCE_TICK_COMPAT` 完全复现；可选 `REALTIME_DT` 是未来经作者选择的创作性新模式，必须另做对照。
4. **音频控制驱动要辨源。** 有密集采样曲线和同源多个出口并不证明多个独立频段或真正的 beat detector；只可称 `baked-like`，完整音频 Bake 来源另证。
5. **482 个对照 ≠ 482 个独立源演出场景。** 检验的是有限点数、边界条件和连续 tick 的局部机制，不涵盖源出生拓扑、Curl、Wave、实例、原摄像机、音频一段完整驱动和渲染外观。

此修订只包含脱敏研究结论。完整工程节点、原始曲线、精细参数与商业素材继续保留在本地私有研究目录，不能从本报告反向推断源工程配方。

## 一、结论

不存在已证明可直接、完整地将任意 Blender Geometry Nodes + Simulation Zone 项目“一键导出为 Metal/CUDA 的实时引擎”的可靠通用方案。Blender 可使用 GPU 渲染 ≠ Geometry Nodes 及 Simulation Zone 逐帧模拟已完全在 GPU 执行。

但已经有多条非常接近此目标的途径：

- **最接近 Blender Simulation Zone 的现成 GPU 节点程序：TouchDesigner POPs**，特别是 Feedback POP、Particle POP、GLSL POP；适合对照验证状态方程，不等于可以直接导入 Blender 节点树。
- **Mac 原生演出计算：Swift + Metal + MetalKit**；把计算、渲染留在 GPU，音乐/Show Score/OSC 留在 CPU 控制链。
- **Windows/Mac 共用执行契约：Rust wgpu（Metal/Vulkan/DX12）**；先用公共状态格式/曲线数据实现两端机制，再考虑共享同一份 WGSL shader。
- **快速浏览器研究：Three.js WebGPU/TSL**；官方已有 particles、cloth、pingpong 等 Compute 例子。适合快速预览，但不能把网页性能自动外推到独立演出运行时。
- **Apple 的新节点式候选：RealityKit Compute Graph**；Emitter → Initialize → Simulate → Output，适合 Vision Pro / 空间应用研究，仍属于 RealityKit 生态并有 Beta API 标记。
- **Blender 内 GPU 研究：上游 WIP GPU Fields #165697、Warbler / NVIDIA Warp + Newton**；关注上游方向与局部技术复用，但都不等于通用 Simulation Zone 编译器。

## 二、项目比较（基于官方文档，非本地跑分）

| 技术/项目 | Mac Apple Silicon | Windows RTX | Stateful GPU simulation | Blender 源逻辑迁移 | 适用性与限制 |
| --- | --- | --- | --- | --- | --- |
| **TouchDesigner POPs**（POPs / Feedback / Particle / GLSL） | 支持，需核对当前 macOS POP 限制 | 支持 Vulkan GPU | **强**，明确有前帧反馈、粒子出生/死亡 | 手工复刻映射（不是 GN 导入） | **最好的可视化对照沙盒**；商用工具、Mac 特定 POP 操作存在限制 |
| **Native Metal + MetalKit** | **原生 GPU** | 不支持 Metal | 自行定义 state-buffer / compute passes | 手工实现 | **Mac 现场机器首选**；对开发和 GPU 调试要求高 |
| **Rust wgpu / WGSL** | Metal 后端 | Vulkan、D3D12 | compute/storage buffer 自行实现 | 手工实现 | **跨 Windows/Mac 的长线主架构**；需 Rust/图形代码 |
| **Three.js WebGPU / TSL** | 支持 WebGPU 的浏览器与设备，逐机验收 | 同左 | 有 Compute/Ping-pong 示例，自行管理状态 | 手工实现 | **最快可分享预览**；浏览器兼容/时延/性能需实测 |
| **Apple RealityKit Compute Graph** | 仅按相关 Apple OS / RealityKit 具体支持验证 | 不支持 | **强**，四阶段粒子计算图 | 手动移植节点思想 | **特别适合 visionOS 研究**；Beta 和 RealityKit 依赖 |
| **Blender GPU Fields PR #165697** | Metal 开发分支 | Vulkan 开发分支 | **仅部分 Field/Capture GPU**，不等于完整 Simulation Zone | 原生 Blender 内 | 不建议押注该 WIP 直接运行整套 Drop Flow |
| **Warbler / Newton / Warp** | macOS 可回退 CPU | NVIDIA CUDA 可加速 | 特定物理系统，非任意节点 | 在 Blender 用自己的 GN 子系统配置 | **值得研究节点→GPU 编译模型**；WIP，场景范围受限 |
| **Taichi Lang** | Metal（文档 Tier 2） | Vulkan/CUDA | 高度可编程计算 | 需要人工翻译 | **最短 Python GPU 算法实验路线**；Mac Metal 后端成熟度低于 Vulkan Tier 1 |
| **Godot RenderingDevice** | 4.7 有原生 Metal 后端 | Vulkan/DX12 | Compute Shader 可自行实现 | 需人工转换 | 免费开源的现成场景/GUI/摄像机框架，不能直接读取 GN |
| **Notch Builder** | 无计划支持 macOS | **GPU 粒子系统 / Windows** | 强，支持 deterministic、cache/scrub | 需重建 | 大屏演出专业基准；商业工具、Windows-only |
| **Unity VFX Graph** | 依照 HDRP/URP+Compute/SSBO 平台确认 | GPU 粒子 | 强 | 重建 VFX Graph | 可做复杂现场视觉，但大型引擎占用与演出输出链需评估 |
| **Unreal Niagara GPUComputeSim** | 逐平台/渲染路径验证 | 强 | 强 | 重建 Niagara | 已成熟的高质量 3D 视觉，复杂度比你的“忠实移植”目标大 |
| **cables.gl WebGPU** | 浏览器 WebGPU | 浏览器 WebGPU | 可组合 Compute/Storage Buffer | 手动移植 | 可视化浏览器 patch 研究，非原生 GPU 演出引擎 |
| **Slang / SPIRV-Cross** | 生成 MSL；Slang Metal 仍实验 | SPIR-V / HLSL | 只是 shader 编译/转换工具 | **不编译 Blender GN** | 在第二阶段再考虑一套核心 shader 适配多后端 |

上表的“支持”表示官方文档的技术方向，**并非**已经在用户的 M1 Pro、RTX 4080 SUPER、实际现场外设与 Blender 5.3 工程上完成稳定性测试。

## 三、最有价值的几条官方发现

### 1. TouchDesigner POPs 是这轮的重点，不是旧 SOP 粒子

官方说明 POPs 是 GPU point operators；Particle POP 可以按每帧发射率增加粒子，并带位置、速度、质量等属性；Feedback POP 提供**上次 Cook 的结果送回本次**的机制；GLSL POP 可在 GPU 计算结构变形。官方特别提示 GPU 点数/拓扑要避免读回 CPU，否则可能 stall。

**面向 Drop Flow 的最小试验：**
`Emitter POP → Particle POP / Feedback POP → GLSL / Attribute changes → Render TOP`
保留 id / seed / age / lifetime / position / velocity，按 Blender 的波形和噪声门控更新。优先重现生命周期、流动与相机，而非美化外观。2026-09-01 官方版引入了 Time Filter POP，有助于独立研究属性时间滤波。

官网：
- https://docs.derivative.ca/POP
- https://docs.derivative.ca/Feedback_POP
- https://docs.derivative.ca/Particle_POP
- https://docs.derivative.ca/Learning_About_POPs
- https://derivative.ca/UserGuide/Release_Notes
- https://docs.derivative.ca/MacOS

**Mac 限制：** 2025 早期版本出现过 Vulkan→Metal/MoltenVK 驱动问题；当前文档也列出 Apple Silicon POPs 对 Atomic Float / Double Precision / Hardware Ray Tracing 的限制。先在 Mac M1 Pro 上跑最小粒子例子，检查当前驱动和构建版，再决定可靠性；不要沿用旧 crash 记录判定最新版一定有问题。

### 2. Apple Compute Graph 是 2026 新增的高度相关方向

Reality Composer Pro 3 / RealityKit 新 Compute Graph 的标准分段是 Emitter、Initialize、Simulate、Output；Compute Graph 有 API 和图编译机制，属于 GPU-backed 的节点式粒子模拟体系。其关键意义不是“Blender 到 Apple 自动转换”，而是**Apple 自己已经有一个与你想要的按帧模拟创作接近的编排/执行模型**。

适合独立空间研究（Quest/WebXR 不属于该框架的目标平台），不得直接取代舞台用 Swift Metal Renderer。

官方：
- https://developer.apple.com/documentation/ComputeGraph
- https://developer.apple.com/documentation/realitycomposerpro/introducing-compute-graph
- https://developer.apple.com/videos/play/wwdc2026/393/

### 3. Blender 上游 GPU Fields 实验与 Warbler

Blender 官方在 2026-10 的 workshop 强调 GPU resident attribute 与不做 GPU→CPU readback 的高收益场景。WIP PR #165697 使用 GPUMaterial 将受支持的字段编译成 compute shader，Metal/Vulkan 后端；支持种类与域有限，Auto 模式还不意味着全部 GPU。其早期一百万点 field 基准在 M5 Pro/RTX 3090 上报告了不同程度加速，但未在最新修订完整重测，不能外推为 Drop Flow 整套模拟收益。

Warbler 则以 NVIDIA Warp + Newton 编译自有模拟节点，支持 Blender GN 场景里的 particles/ropes/curves/cloth/rigid bodies；WIP，NVIDIA 快，Mac 回退 CPU。它并不是任意 Blender Simulation Zone 的转译器，但很值得对照研究“节点 UI → 后端 GPU Solver”。

资料：
- https://code.blender.org/2026/10/geometry-nodes-workshop-september-2026/
- https://projects.blender.org/blender/blender/pulls/165697
- https://github.com/BradyAJohnston/warbler
- https://github.com/newton-physics/newton

### 4. Mac Vulkan 在 2026 年发生了值得注意的改变

Khronos/MoltenVK 仓库现在有弃用提示，对 **Apple Silicon + macOS 26+** 推荐 Mesa **KosmicKrisp**；它使用 Metal 4，2026-10-01 已取得 Vulkan 1.4 conformance。老版 macOS、Intel Mac 或旧软件的 Vulkan bridge 仍可能依赖 MoltenVK。

这并不意味着旧 TouchDesigner、wgpu 或其他使用 MoltenVK 的软件必须立刻升级——它们的内部后端由各自版本决定；更不代表所有现场软件都通过 KosmicKrisp 测试。

资料：
- https://www.khronos.org/news/permalink/kosmickrisp-achieves-vulkan-1.4-conformance-on-apple-silicon
- https://docs.mesa3d.org/drivers/kosmickrisp.html
- https://github.com/KhronosGroup/MoltenVK

### 5. WebGPU / wgpu：同一个状态契约，多个输出执行体

Three.js 有官方 WebGPU compute particles、cloth、texture ping-pong、sort 等示例；wgpu 则原生支持 Metal/Vulkan/DX12。它们适合共享模拟的**概念状态与输入数据**，但并不保证 Three.js TSL 与 Rust WGSL 完全通用。

适合路线：
- Browser preview: Three.js WebGPU (TSL)；
- Cross-platform native: Rust wgpu；
- Mac stage: Swift Metal 可作为更低层、更容易与 Mac 现场媒体工具配合的独立版本；
- Windows: 保留已有 C++/OpenGL Compute/SSBO 作为对照，未来再决定 Vulkan/wgpu 是否替换它。

资料：
- https://threejs.org/examples/webgpu_compute_particles.html
- https://threejs.org/docs/pages/TSL
- https://wgpu.rs/
- https://wgpu.rs/doc/wgpu/

## 四、推荐架构：先转译作者的数据与逻辑，不是整图节点自动翻译

核心接口 `VisualSimulationContract v0`：

```text
Blender original (.blend)
  |  offline-only metadata/FCurve/attributes/cache/frames
  v
[Work Manifest]  [State Contract]  [Input Curves]  [Golden Frames]
                       |
         -------------------------------------
         |                 |                 |
  TouchDesigner POPs  Rust/wgpu or Metal  Three.js WebGPU
    validation        native stage          web preview
         |                 |                 |
         ---------- comparable states -------
                           |
      shared audio / OSC / Show Score / MIDI driver
```

### 状态契约建议

- `id:u32`, `seed:u32`, `position:vec3`, `velocity:vec3`, `age:f32`, `life:f32`, `radius:f32`, `alive:boolean`。按项目实际节点追加 `direction / r0 / wave_geo / LT` 等。
- `global_time_s`, `delta_time_s`, `frame_index`, `spawn_rate`, `noise_w`, `audio_envelope`, `beat_phase`, `manual_gate`。
- **不得默认把 Blender Simulation Zone 的任何属性/波形名等同于上面示例字段**。本地 Agent 需映射实际属性类型、储存域、发射顺序和输入目标。
- 噪声和分段函数要**留采样测试表**，不同语言/后端的 noise/hash 不一定数值一致。
- 建议一份固定的离线对照 CSV 和 3~5 个连续帧状态样本，分离“数学结果”、“几何拓扑”、“画面渲染”、“人的视觉感受”的误差。
- 推荐固定模拟步长与可独立变化的渲染 FPS；如果源工程行为明确依赖 FPS，则保持兼容模式并记录差异。
- 发射数变化与删除会改变点数/拓扑，需要 GPU append/free list/compaction、indirect dispatch/draw 等机制；**固定 18,000 点槽位不一定等价于源作品的生成方式**。
- 音频可以被 Bake 成曲线、存为 envelope LUT、也可接实时包络和 MIDI/OSC；在 Runtime 里保留同一个参数的 `Baked / Live / Manual` 驱动模式。
- 回放/重启、静音、重置以及断线后的确定性行为是演出系统需要的功能，但不能从 Blender 原始作图中凭空推定它们已经存在。

### 独立 GPU Runtime 核心循环示意

```text
setup:
  load emitter / geometry / camera / material / curve LUT
  allocate state A/B, alive indices, spawn counters, render buffers
  reset seed / simulation time
frame:
  receive bounded control signals (CPU)
  perform fixed simulation steps:
     emit -> update motion -> age -> gate/delete -> compact/alive list
  submit GPU rendering using GPU-resident state buffer
  composite material/line glow/selected images
  display fullscreen; log GPU ms and missed frames
```

REACTOR 的 wire→curve→scan→glow、HERO DOME 的材质合成与点云颜色不属于 Drop Flow 模拟求值本体，优先分别做可复用绘制/材质层，不要强行合并成一条复杂 Compute Kernel。

## 五、平行研究安排：六个独立 Spike（每个有一张具体测试图）

| ID | 设备/路线 | 最小实验 | 成功条件 / 退出 |
|---|---|---|---|
| **S1 / source** | 本地 Windows Blender | 从一条 Drop Flow Simulation Zone 导出真实状态更新/音频来源/连续帧 | 输出状态表、节点链、3~5 个 reference frames；不要求 GPU |
| **S2 / POP** | Windows TouchDesigner POPs | Particle + Feedback，复刻 S1 的出生/删除/扰动；无后期美颜 | 同帧点数、寿命分布、分布形态和速度变化可解释 |
| **S3 / Metal** | Mac M1 Pro | Swift/MetalKit：state A/B、固定步长、compute update→render 3D points | 真 GPU kernel、nonzero animation、GPU 帧时间，能与 S1 对照 |
| **S4 / WebGPU** | 浏览器 | Three.js TSL/Compute，和 S3 读同一个状态/控制样本 | 与 S3 一致的生命周期和基本空间分布；验证 WebGPU 可用性 |
| **S5 / Warbler** | Windows RTX Blender | 用官方演示 particles / curves 理解 GN→GPU 的边界 | 明确支持/不支持的 Drop Flow 机制，不要求全作品移植 |
| **S6 / Apple Compute Graph** | Mac + Reality Composer Pro / RealityKit，适配时再到 AVP | 最少一个 emitter、per-particle life/update 和输出 | 证明节点图可编译并运行；明确 Apple OS/API 版本限制 |

**停止规则**：不得同时做六套风格扩展。S1 的真实算法未拿到之前，只允许 S2~S6 做各自的“工具能不能跑”的空白基准，不允许宣称它们还原了 Drop Flow。S3/S4 只是 CPU→GPU 的路径测试，不代表可登台。

## 六、技术路线的比较与建议

- **一周内可观察结果**：用 POPs / Three.js WebGPU 对照旧版 Processing 的不忠实行为；本地应先给出源工程节点/音乐驱动及原始帧。
- **长期跨平台核心**：倾向 `Blender export contract + Rust wgpu`，以状态与曲线接口复用到 Windows/Metal；用 Swift Metal 专门处理 Apple 本地演出和 RealityKit/visionOS 需求。
- **Mac 原生优先的替代**：若最终只在 Mac 上演出，Swift Metal 的单设备栈可简化依赖；但不应丢弃 Windows RTX 的旧 GPU 工程与性能基线。
- **专业演出参考**：Notch / Unity VFX Graph / Unreal Niagara 可研究复杂粒子与空间场景，但它们的生产流程与授权/运行复杂度意味着不应变成这次 Drop Flow 机制提纯的首个重写目标。
- **研发加速工具**：Taichi 可以快速验证数学场的并行更新；Slang / SPIRV-Cross 在第二阶段可研究多 Shader 后端；不要以这些框架自动“读取 Blender 全部程序”。

## 七、需要本地 Codex 返还的五类证据

1. `gn-state-graph.json`：原始 Simulation Input/Output、每个 state item、跨帧更新、数据类型、属性域、场景引用、外部 Curve/音频 Bake 目标。
2. `control-provenance.csv`：手 K / 音频 Bake / 外部视频 / 时间节点 / 人工录屏，不能凭密集 FCurve 就宣称音频驱动。
3. `golden-states.csv` 与同一摄像机帧图：多个连续时刻，包含点数/关键属性统计、随机种子/时间与哈希。
4. `old-runtime-diff.md`：旧 openFrameworks / SSBO 代码的逐机制缺失，特别是时序、索引身份、噪声域、曲线值、发射/删除、密度、输出几何。
5. `runtime-profile.md`：设备、OS、Blender/驱动版本、GPU ms、render ms、帧时间 p95、点数、显存与控制延时；未测项写“NOT_TESTED”。

## 八、参考资料（以官方/作者为优先）

**Blender**
- Geometry Nodes 2026 Workshop — https://code.blender.org/2026/10/geometry-nodes-workshop-september-2026/
- GPU Fields WIP #165697 — https://projects.blender.org/blender/blender/pulls/165697
- Simulation Zone 5.2 manual — https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/simulation/simulation_zone.html
- Warbler — https://github.com/BradyAJohnston/warbler

**GPU / native / Apple**
- Apple Metal compute sample — https://developer.apple.com/documentation/metal/performing-calculations-on-a-gpu
- Apple Compute Graph — https://developer.apple.com/documentation/ComputeGraph
- WWDC 2026 Reality Composer Pro 3 — https://developer.apple.com/videos/play/wwdc2026/393/
- Khronos 2026 KosmicKrisp — https://www.khronos.org/news/permalink/kosmickrisp-achieves-vulkan-1.4-conformance-on-apple-silicon
- KosmicKrisp Mesa — https://docs.mesa3d.org/drivers/kosmickrisp.html

**Realtime tools**
- TouchDesigner POPs — https://docs.derivative.ca/POP
- Feedback POP — https://docs.derivative.ca/Feedback_POP
- Particle POP — https://docs.derivative.ca/Particle_POP
- TouchDesigner macOS limitations — https://docs.derivative.ca/MacOS
- Notch 2026 particles — https://manual.notch.one/2026.1/en/docs/learning/simulations/particles/overview-of-particles/
- Unity VFX Graph — https://docs.unity.cn/6000.2/Documentation/Manual/VFXGraph.html
- Unreal Niagara GPU simulation — https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-gpu-sprite-effect-in-niagara-for-unreal-engine
- Godot compute shader — https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html

**Portable programming**
- Three.js WebGPU compute particles — https://threejs.org/examples/webgpu_compute_particles.html
- Three.js TSL — https://threejs.org/docs/pages/TSL
- wgpu — https://wgpu.rs/
- Dawn C++/native WebGPU — https://github.com/google/dawn/blob/main/docs/support.md
- Taichi backends — https://docs.taichi-lang.org/docs/master/hello_world
- Slang shader targets — https://github.com/shader-slang/slang
- SPIRV-Cross — https://github.com/KhronosGroup/SPIRV-Cross
- cables.gl WebGPU Ops — https://cables.gl/ops/Ops.Extension.WebGpu

## 九、与已归档的作者口述关系

艺术谱系的主档案正在以下草稿 PR 中审阅：
[art-works / PR #2 — 2026-11-09 first-person creative lineage](https://github.com/ewanqian/art-works/pull/2)

本报告只负责生态与可执行技术比较，不能代替该创作史，也不会把没有完成的 GPU 移植/空间音频/动捕 VR 方案写成已完成作品。

**最终决策建议：Drop Flow GPU Runtime 是长期主项目；TouchDesigner POPs 和 Apple Compute Graph 是最值得平行研究的“现成实现参照”；Mac Swift Metal 与跨平台 wgpu 各做一个最小状态循环后，再决定是否合并或择一。**
