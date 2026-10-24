# KB Publication System v2

**2026-10-24：Mac + uv 运行基线与证据闭环修订，待集中审核。** 新入口使用 uv 管理的 Python 3.14.8；成功预览必须绑定完整机器证据和全页渲染。详情与实际验证范围见[本批实施记录](reviews/runtime-evidence/README.md)。不改正文、历史 profile、视觉规则或已发布资产；不实现新布局、缓存或正式发布入口。

状态：**STABLE / READING EDITION ACCEPTED / VISUAL_PROFILE_FROZEN v1.0**。用户于 2026-09-27 确认冻结最新视觉实现 `1c11c5940c05fe29c46c4500935d5efb673d46a7`；ESD 与 C++ Handbook Visual Profile 同步冻结，语义视觉回归 corpus 成为基线。通用 `publish` 命令保持关闭；已明确授权的 C++ v1.0.0 通过 GitHub Releases 发布，见下文。

已接受的 12 份制品、八组组件 A/B、语义样页、接受记录与已知非阻塞限制见[阅读版定稿化审核入口](reviews/reading-finalization/README.md)。[上一轮阅读版](reviews/reading-edition/README.md)与 [v2 架构交付记录](reviews/v2-pilot/README.md)作为历史证据保持原字节。它们均不是 release 或可维护的正文源。

**Modern C++ 工程学习手册 v1.0.0 已正式发布**：[GitHub Release](https://github.com/snkio027/kb/releases/tag/cpp-handbook-v1.0.0) · [发布记录](releases/cpp-handbook/v1.0.0/README.md) · [公开状态与下载回验](releases/cpp-handbook/v1.0.0/publication-receipt.json)。407 页；最终 PDF SHA-256 为 `ce4f6d5f6e4b8c1e2789eedd1fc151462d31e929b724ce2eb95c780f90766510`。签名标签固定到 `54f193f46a3af12266acc898829e23f4ab27dbde`；四个资产在公开前后均完整下载回验，未替换旧候选或历史制品。

历史链条保留：[Full Handbook](reviews/full-handbook/README.md) → [f288051 发布准备](reviews/release-qualification/README.md) → [v1.0.0 RC1](reviews/rc1/README.md)。正式版只修正生成身份与来源状态提示，正文和视觉规则不变。最终字节另获用户“通过”反馈，但阅读器名称未注明；不把旧 RC1 的 Preview／Chrome 记录改写成新字节自动化结果。112 项回归为本地出版证据，不是 C++ 重跑或 CI。

方法与经验见[技术手册出版工程复盘](lessons-learned.md)：结合源稿编辑、隔离反例、语义排版、全书导航及实际发布，整理可复用做法与证据边界；不替代下文操作说明或各批次原始记录。

后续布局研究见 [Next Generation Design Study](layout-architecture-next.md)：仅冻结信息边界、职责、依赖闭包及变更验证问题；优先研究布局选择与身份隔离。现有 v2 系统、Visual Profile v1.0 和两本已发布手册保持不动；下一代实现及实验均 **NOT STARTED**。

**C++23 失败语义工程手册 v1.0.0 已正式发布**：[GitHub Release](https://github.com/snkio027/kb/releases/tag/cpp-failure-model-v1.0.0) · [158 页发布记录](releases/cpp-failure-model/v1.0.0/README.md) · [下载回验与回执](releases/cpp-failure-model/v1.0.0/publication-receipt.json)。签名标签固定于 `d5629f05d00fd902c0462de181b3e359c4270cc1`；四个资产在公开前后均完整下载核验。PDF SHA-256 为 `2957aab0ad153873307a83af9383f08dabcfb3caae8c5f27750a6f48ee3c4e9c`，与 `4f8fe84` 候选完全一致。内容仍为 `45b305e` 的 series guide＋FM-0～FM-9；正文、共享视觉规则和候选证据不改，授权分发元数据单独保存。[候选批次审核](reviews/failure-model/README.md)保留历史状态；阅读器部分覆盖与其他未验证边界不升级为全矩阵通过。

## 分层与权威

| 层 | 责任 | 不承担的责任 |
| --- | --- | --- |
| Markdown / Git source | 权威字节、路径、版本与冻结提交 | 不为排版改正文、代码或 Gate |
| `engine/` | 快照、隔离、编译、通用结构与保真检查、渲染、终态、候选 | 不识别 ESD、G6/G7 或某条业务条款 |
| `profiles/<id>/` | 源适配、产品视图、元数据、模板、主题、导航与审计策略 | 不绕过引擎的输入或输出边界 |
| `latex/` | 共享字体和排版机械、代码/表格续页、链接与标题机制 | 不定义产品权威或接受状态 |
| `build/` | 独立尝试、预览、渲染和已检查字节的候选副本 | 不等于发布目录；全部本地忽略 |

产品配置采用 `profile.json`（包含 source catalog 与 views），避免为两个产品引入配置语言或插件发现框架。`adapter.py` 只在受限 worker 中从冻结输入加载；产品模板与 theme 可以覆盖共享默认样式。可信仓库 profile 仍是执行输入，不承诺运行任意不可信 Python 插件。

当前 ESD profile 读取六篇工作树 Markdown 的 Front Matter。C++ Pilot `cpp-handbook` 固定读取 `8f479deaf660533b2ad82e1f721eb41a363112b6` 下 G6/G7；`cpp-handbook-full` 读取同一冻结提交的 G0–G12，解析书名式 H1、正文版本与稳定锚点。不把当前 HEAD 当作 C++ 内容版本，不把 C++ 文件复制到 `design/` 充当新来源。

## 运行

依赖：macOS `sandbox-exec`、Git、uv、Pandoc、LuaLaTeX、Poppler `pdftoppm`、`kpsewhich` 和 TeX 字体。Python 及 Python 包由独立的 [uv 项目](pyproject.toml)、[锁文件](uv.lock)与 `.python-version` 固定，不使用系统 Python。原 [requirements.txt](requirements.txt)仅保留历史依赖说明，不是当前安装入口。缺少隔离后端时失败，不回退到无沙箱编译。不提供 Linux/CI 或 PDF/UA 保证。

从仓库根目录执行。环境同步在沙箱外完成；worker 使用父进程的同一解释器，不自行安装依赖或联网。`--locked` 会检查声明与锁文件的一致性，不以 `--frozen` 替代：

```sh
uv sync --project publication --locked --group review
uv run --project publication --locked --group review python -B publication/engine/pub.py doctor
uv run --project publication --locked python -B publication/engine/pub.py preview --profile esd
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook-full
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook-rc1
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook-v1
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-failure-model

# 仅选择一个逻辑视图；省略 --view 时构建该 profile 的全部视图。
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook --view G6
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook --view CPP-PILOT-G6-G7

# 只准备，不编译。
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook --prepare-only
```

`doctor` 报告实际选中的工具路径、版本和摘要、uv Python、锁文件、字体/TeX 包解析，以及一次真实 Seatbelt 写入拒绝。构建前后比较所选环境；`.fls` 中额外发现的运行依赖仍只标为事后观察，不声称完整只读输入沙箱、原生工具链全闭包或跨机器确定性 PDF。

主制品为 ESD 六份独立版与一份合订版，以及 C++ G6、G7 与 G6+G7 三份 PDF。默认构建还包含两份 Compact 对照样张：`ESD-REFERENCE-001-COMPACT` 和 `CPP-PILOT-G6-G7-COMPACT`；两个 profile 合计 12 份。Compact 只改变留白、目录和表格行距，不缩小正文或代码字号。合订版由多源 AST 组成一个逻辑视图后编译，不拼接独立 PDF。

新增 `cpp-handbook-full` 只生成一份 Balanced 全书 `CPP-HANDBOOK`，不重建旧 12 份，不增加全书 Compact 比较或十三份独立版。

`cpp-handbook-rc1` 使用同一冻结源与视觉规则，只生成身份一致的 `Modern-Cpp-Engineering-Handbook-v1.0.0.pdf`。内部预览／候选终态不是正式发布状态；RC1 封面、页脚与元数据明确“尚未发布”。既有 profile 的默认命名与 PREVIEW 身份不变。

`cpp-handbook-v1` 生成中性 `PUBLICATION EDITION` 正式版身份，通用构建终态仍不表示发布。下载正式版请使用 Release 的已固定字节；重新构建不保证同一摘要，也不得覆盖已发布资产。

`cpp-failure-model` 以同一冻结视觉规则构建一份正式身份全书，不另做 Pilot。它显式选用 `source_format: gfm`；省略时仍用旧 `markdown-smart`。FM 的非打印锚点转换为文档命名空间内的块级目标，保留中文／数字 ID 与原块位置，正文点击直接指向目标，不以父标题或目录链接代替。实验注释与显式反例标签的产品识别只存在于 adapter。

输出路径固定为 `publication/build/preview/<preparation-id>/<attempt-id>/`。`inputs/sources/<repository-path>` 保留嵌套源身份；`work/output/pdf/` 是 PDF，`work/output/source/` 为同路径原始源码，`work/renders/<view>/` 为所有页面 PNG。本次尝试入口为 `work/output/README.md`。

## 身份与链接

准备身份绑定 Git 实现上下文、Python 身份、源 revision/path/bytes、profile、视图选择及引擎/LaTeX 输入。实际执行身份另外绑定准备 ID、工具可执行文件与版本、pypdf 文件及 `.fls` 所列 TeX/字体依赖。制品摘要由预览终态绑定；准备 ID 单独不是完整工具链执行身份。

源与实现可能来自不同提交：C++ 内容固定于 `8f479de`，引擎来自后续实现或明确记录的工作树输入。运行期间读取的是输入副本，profile/renderer 或 WORKTREE 源在准备后漂移会拒绝成功；固定 Git 源不因工作树或 HEAD 漂移切换 revision。

同视图引用变成内部 destination；独立版到其他文档按策略链接到固定仓库源或随附源副本。视图外的仓库链接核对固定提交下的文件/锚点，无法解析时失败；已有网页 URL 保持外链，不把联网可达性当作本轮通过项。C++ 原始 HTML anchor 作为 PDF destination alias 保留，实验注释明确登记为非打印语义对象；未知 raw markup 不静默删除。生成目的地、别名、源路径和链接分类均有审计记录。

## 终态与候选

`result.json: PREPARED` 仅是输入准备；`preview-result.json: PREVIEW_READY` 才表示本次所有声明视图完成自动检查和全页渲染。两者均不是视觉批准、内容重新验收或发布批准。失败、取消、缺少终态或 `.pending` 文件不等于成功；提交点之后保留已提交事实，不生成矛盾终态。

新协议在 worker 退出且日志关闭后，生成 `work/artifact-manifest.json`，绑定输出、原始/打印 AST、保真审计、引用/表格映射、TeX/日志和全页 PNG 的完整文件集合、大小与 SHA-256。每张 PNG 另绑定 PDF 摘要、页号、DPI 和渲染器。成功终态绑定清单摘要；候选与阅读工具均复核清单和准备计划中的视图集合，任何缺失、增加或改写均拒绝。快速检查或旧协议预览不能冒充 `FULL_PREVIEW`；本批没有新增快速模式。

源保真在 adapter 之前保存原始 AST，adapter 只收到独立副本。引擎单独核对正文字符顺序、原有 inline code、代码字节/语言、标题、列表、表格单元格关系、链接与锚点位置。注释/锚点转换和字面量处理形成显式记录；普通正文不能由 adapter 自报“允许删除”。普通 prose 的空白/段落边界可调整，代码空白不可变；这仍不是任意语义等价或视觉正确性的形式证明。

历史预览、profile 和已发布文件不回写、不补签。缺少新清单的旧尝试可通过其历史版本工具查阅，但当前冻结/阅读入口会拒绝升级资格。衍生的 `reading-regression/`、`visual-inputs/` 及人工阅读记录不混入已提交的机器证据；它们另绑定 PDF/清单身份。

候选只复制已检查原字节，不重新编译：

```sh
uv run --project publication --locked python -B publication/engine/pub.py candidate --profile cpp-handbook \
  --from-preview publication/build/preview/<preparation-id>/<attempt-id>
```

输出为 `publication/build/candidate/<candidate-id>/<attempt-id>/`；只有 `CANDIDATE_PREPARED_FOR_REVIEW` 表示本地冻结完成。生成时候选状态为 `AWAITING_INDEPENDENT_REVIEW`；后续用户接受由外置记录登记，不回写原 JSON 或 PDF 内的候选标记，也不宣称新增独立技术验证。其身份保留源 revision/path、视图集合、准备/执行身份和制品摘要，而非通过 basename 找源文件。

可在预览尝试根目录附 `reading-review.json`，用 `artifacts`、`audit_sha256` 与 `artifact_manifest_sha256` 绑定该次终态，分别记录查看页、观察与未检查项。缺失时记为 `NOT_ATTACHED`，不推定人工检查已经执行。全部流程不写历史 `design/dist/`；本地提交协议不声称断电后的目录树持久性。

## 迁移与验证

原 `design/scripts/pub.py preview` 只转发至 v2 的 ESD profile；旧内部 worker 不再运行。旧六个危险写入入口继续拒绝，通用发布入口仍关闭。原 `design/build/` 预览和候选不移动、不重写；v1 记录不自动升级为 v2 合格记录，新候选入口只接收 v2 路径。历史工具可在精确 Git 版本中查阅，不保留第二套可漂移的活动构建器。

```sh
uv run --project publication --locked --group review python -B publication/tests/run.py \
  --output publication/tmp/local-check-new
```

输出目录必须尚不存在。执行器检查登记集合等于全部 `test-*.py`，包括 FM 套件；逐套保存命令、退出码、数量、SKIP 和完整日志。可选 `--group logic`（文件协议与反例）、`--group adapters`（Pandoc／产品／阅读组件）、`--group native`（含真实 Seatbelt、TeX、失败与取消），未运行组明确列出。人工阅读不由测试执行器代办。测试夹具通过不替代真实产品构建。

自动提取采用有界的文本、顺序、行内字面量、表格关系和定位检查，不声称逐字形、代码缩进、所有视觉缺陷或可访问性认证。人工阅读必须查看实际渲染，且单独注明范围。当前视觉基线已获用户接受；既有本地执行与自查证据保留原身份。全书构建是接受登记之后单独获授权的批次，出版回归不等于重跑 C++ 技术实验，也不等于正式发布。

可选视觉辅助命令为 `uv run --project publication --locked --group review python -B publication/tools/inspect-pages.py <preview-attempt>`。Pillow 属于锁定的 review 组；它只从逐页摘要验证后的渲染字节生成 contact sheets，并记录衍生图片摘要，不自动授予人工阅读通过状态。

阅读回归使用[语义样本目录](tools/reading-corpus.json)，不把物理页码作为样本身份：

```sh
uv run --project publication --locked python -B publication/tools/reading-review.py <completed-preview-attempt>
uv run --project publication --locked python -B publication/tools/reading-review.py --density-compare <page-map.json>
uv run --project publication --locked python -B publication/tools/reading-review.py --compare <old-page-map.json> <new-page-map.json>
```

第一条从绑定的 PDF 生成 `work/reading-regression/`（新目录，拒绝覆盖），输出样本语义目的、目标、物理页、120 dpi PNG 和摘要。后两条只读比较相同语义目标，不把像素不同判为失败。`STRUCTURAL_PASS` 表示所定义的阅读信号未触发；没有适用 fixture 时为 `NOT_COVERED`，不是通过。实际查看图片另记 `VISUAL_REVIEWED_SELF_REVIEW_NOT_APPROVAL`。冻结不改变这些证据标签的含义。规则与冻结边界见[Visual Profile v1.0](reviews/reading-finalization/visual-profile.md)。
