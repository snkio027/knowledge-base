# Mac + uv 运行基线与出版证据闭环

2026-10-24；Base `9e446f62616c959c8b90b762cfe981aa00e0352c`。本批只实施已批准的前两个工作包，不推进布局重构、输入身份拆分、缓存、提速或正式发布。正文、历史 profile、视觉实现和已发布 PDF 保留原字节。

## 实现边界

运行环境由 `publication/pyproject.toml`、`uv.lock`、`.python-version` 管理：uv only-managed，CPython 3.14.8，pypdf 6.10.0；review 组为 Pillow 12.0.0。worker 继承父解释器，联网和安装仅发生在环境同步阶段。`doctor` 核对本机原生工具、选定字体/TeX 包和 Seatbelt 可用性。Git 取源与元数据探测统一禁用 replace refs。

保真链分成两段：冻结 Markdown → 原始 AST → 独立 adapter 副本，由引擎检查转换；随后打印 AST → PDF 仍由既有结构、顺序、字面量、表格和导航检查负责。新增检查不允许 adapter 同时删除正文和修改预期基准。普通 prose 空白与段落边界不视为字节相同，代码字节、原有 inline code、链接目标、表格所属关系和锚点位置必须保留。转换记录保存在每篇 `.fidelity.json`，原始与打印 AST 分别保存。

worker 退出且 `worker.log` 关闭后，父进程收集 `artifact-manifest.json`。清单列出 `output/`、`source-ast/`、`typeset/`、`renders/` 的完整集合及顶层审计、catalog、worker 日志；PNG 另记 PDF 摘要、页号、DPI 与渲染器。成功终态绑定清单摘要；候选只复制已核对的清单字节，并再次核对预览未漂移。候选不重编译，也不发布。

阅读工具使用同一校验入口，资格判断不使用可被 `-O` 移除的 `assert`。语义 fixture 要求明确绑定且非空；没有适用 fixture 的视图记为 `NOT_COVERED`，不能产生空样本的 `STRUCTURAL_PASS`。contact sheet 从验证后的 PNG 字节生成，自身另记摘要。人工阅读仍是独立附加证据。

旧尝试没有新终态/清单时明确拒绝，不升级或回写历史成功记录。历史工具可在原提交查阅。当前不实现快速模式；伪装成快速结果的终态不能进入完整候选。

## 验证记录

状态：**LOCAL QUALIFICATION COMPLETE / AWAITING REVIEW**。以下均为 2026-10-24 的本机执行与页图自查，不是 CI 或用户接受记录。[机器汇总](validation.json)绑定实际实现文件摘要；[完整测试输出](test-output.txt)、[环境诊断](doctor.json)和[保护范围核对](protection.json)随本提交保存。构建时实现尚在工作树，不能把 Base commit 当成新实现身份。

### 环境与统一回归

实际环境为 macOS 27.0.1 arm64、uv 0.13.4、uv CPython 3.14.8、pypdf 6.10.0、Pillow 12.0.0、Pandoc 3.12.1、LuaHBTeX 1.24.0 / TeX Live 2026、Poppler 26.05.0。工具路径、所选字体/TeX 包与摘要在 `doctor.json`；Seatbelt 先确认能启动，再确认受保护写入被拒绝，不能把沙箱启动失败当作隔离成功。

从仓库根目录执行的最终回归命令：

```sh
UV_CACHE_DIR=/tmp/kb-uv-cache uv run --project publication --locked --group review \
  python -B publication/tests/run.py --output publication/tmp/qualification-complete
UV_CACHE_DIR=/tmp/kb-uv-cache uv lock --project publication --check
git diff --check
```

输出目录已存在时不能直接重用；再次执行应指定新目录。临时 cache 只是本次执行位置，不是项目运行要求。

两份修改的 Markdown 经 Pandoc GFM 解析、标题层级/重复锚点、代码围栏闭合和本地文件链接检查；TOML 锁一致性、JSON 解析与 diff whitespace 检查通过。具体计数见[文档检查记录](document-checks.json)，不包含联网 URL 或正文技术正确性检查。

| 测试文件 | 用例数 | 结果 |
| --- | ---: | --- |
| `test-publication-isolation.py` | 43 | PASS |
| `test-candidate.py` | 8 | PASS |
| `test-evidence.py` | 18 | PASS |
| `test-products.py` | 15 | PASS |
| `test-reading.py` | 13 | PASS |
| `test-full-handbook.py` | 6 | PASS |
| `test-release-identity.py` | 8 | PASS |
| `test-publication-identity.py` | 5 | PASS |
| `test-failure-model.py` | 9 | PASS |
| `test-preview.py` | 14 | PASS |
| 合计 | **139** | **0 SKIP，登记文件全部执行** |

数量单位为 unittest test method，不是 TeX 编译次数。`logic` / `adapters` / `native` 是文件级运行分组：证据套件也调用 Pandoc，native 套件也含组件单元检查，不能把分组数量直接解释成纯逻辑或真实编译次数。人工阅读不计入 139 项。

新增反例覆盖 adapter 删段/重排、表格关系变化、代码及 inline code 空白、锚点移位、机器证据/PNG 改写、证据文件增删、符号链接、视图缺失/重复/空集合、旧协议/快速模式伪装、Git replace refs 和环境锁不匹配。两个阅读入口分别在 `PYTHONOPTIMIZE=0/1/2` 下拒绝四类无效输入，共 **24 个子场景**；它们包含在 18 项证据测试内，不另加总。每次要求目标诊断，不以无关异常或单纯非零退出码替代判据。

原生套件实际执行了受限编译、写入拒绝、编译失败、内容/身份错误，以及 SIGINT/SIGTERM/SIGKILL 与子进程清理检查。测试日志保留每项结果，不把成功路径替代失败与取消证据。

### 三个真实产品

在同一 uv 环境运行以下预览，随后分别使用 `candidate --profile <同一 profile> --from-preview <对应 attempt>` 冻结原字节。精确 argv、耗时、输入记录、审计、终态及完整 attempt/candidate 路径见下表的构建记录。

```sh
uv run --project publication --locked --group review python -B publication/engine/pub.py doctor
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-handbook --view G6
uv run --project publication --locked python -B publication/engine/pub.py preview --profile esd --view ESD-REFERENCE-001
uv run --project publication --locked python -B publication/engine/pub.py preview --profile cpp-failure-model
uv run --project publication --locked python -B publication/tools/reading-review.py <attempt>
uv run --project publication --locked --group review python -B publication/tools/inspect-pages.py <attempt>
```

| 真实产品 | 全页渲染 | 完成状态 | 阅读 fixture 信号 |
| --- | ---: | --- | --- |
| [G6](builds/cpp-handbook.json) | 48 页 | PREVIEW_READY；候选已冻结 | STRUCTURAL_PASS，3 个 fixture |
| [ESD Reference](builds/esd.json) | 58 页 | PREVIEW_READY；候选已冻结 | STRUCTURAL_PASS，3 个 fixture |
| [FM 全书](builds/cpp-failure-model.json) | 158 页 | PREVIEW_READY；候选已冻结 | **NOT_COVERED，0 个 fixture** |

合计 **264 页**。FM 不在既有 reading corpus 内，零样本不能报告通过；其结构、保真、导航及全页渲染仍由正常预览链检查，视觉另按下面的实际页图自查登记。本轮不新增 corpus 来掩盖未覆盖，也不重建全部 ESD 视图或 407 页 C++ 全书。

三份 PDF 的 SHA-256：

```text
G6-draft.pdf
df435236bed16a692bf40766028728e2c28e2c2e40da940564011bc4086fc73b

ESD-REFERENCE-001-draft.pdf
45df7f1b8ba001e12436903bd6742e75121027e4dca106825f38d0cf76c4181d

Modern-Cpp-Failure-Semantics-Handbook-v1.0.0.pdf
6f1b2c76d923f2f232e9dc9b3ff8797b45237b8f1b494bc4655ddd76abdf42c0
```

最后一份仅为历史正式身份 profile 的**本地回归重建**，不是重新发布的 v1.0.0；Release 的原始 PDF 与摘要保持不动。新 PDF 和候选位于忽略的 `publication/build/`，没有写入 release/dist。

成功终态所绑定的原始清单按字节保存为 [G6 manifest](manifests/cpp-handbook.json)、[ESD manifest](manifests/esd.json)、[FM manifest](manifests/cpp-failure-model.json)。记录整理时再次校验全部清单文件、当前实现/工作树源输入、冻结候选与预览字节、候选 ID 及终态。该校验不重新编译。

此外，用最终 G6 尝试的一次性完整副本做四次改写：源 AST、reference map、worker 日志、单张 PNG。四次均由 `candidate.payload` 报告具体 `artifact digest changed` 而拒绝；原尝试未改动。记录在 `validation.json` 的 `real_product_mutations`，与协议夹具测试分开。

### 页图自查与检查边界

依 PDF skill 查看实际渲染页，合计 **14 页**，状态为 `VISUAL_REVIEWED_SELF_REVIEW_NOT_APPROVAL`：

| 产品 / 物理页 | 实际观察 |
| --- | --- |
| G6：1、40、41、48 | 封面、长实验及续页身份、末页可读；41/48 页的已知较大留白保留 |
| ESD Reference：3、26、27、58 | 目录、空模板字段、末页；抽查未见裁切或字段身份丢失 |
| FM：1、108、109、153、154、158 | 正式身份封面、T17 代码续页、Failure Contract 模板及 continuation、末页；抽查未见新的阻断问题 |

120 dpi 阅读样页与 72 dpi 全页渲染并用；构建记录列出对应完整渲染页的摘要以定位输入。没有声称逐页人工检查、全部模板视觉验证或重跑 Preview/Chrome/Acrobat 兼容性。既有局部留白和 soft-wrap 瑕疵不在本轮调整。

### 批内修复与范围保护

最终结果之前保留了失败试跑：旧视觉锁测试误把候选协议文件也视为排版实现，现改为核对共享 LaTeX、历史 profile、Lua、链接/审计实现及五个实际排版函数；锚点负例的夹具修正了 Pandoc 拆分的空 HTML anchor 表示；独立 AST 检查补齐不同合法节点形态；环境检查补上已安装 pypdf 与锁版本的一致性。一次真实 G6 构建因运行中实现输入发生变化而明确 FAILED，未进入最终候选。最终 139 项和三个产品均重新执行，不沿用这些试跑的成功项拼接结果。

运行前登记 1,593 个既有文件；收尾重算后，只有本批授权的 9 个既有实现/说明文件改变，**其余 1,584 个原文件完全相同**。其中 **455 份既有 PDF**、正文、历史 profile、共享 LaTeX/Lua 和 4 个用户未跟踪 zig 文件均保持原字节。新增文件限于 uv 配置/锁、引擎验证模块、测试入口/反例及本目录记录。核对集合与逐文件原摘要在 `protection.json`；这不将新建的本地预览误算成历史文件。

## 限制与后续

- 此批为本机 macOS arm64 证据，不是 CI、跨平台或跨机器字节级可复现证明。
- 所选 Python 包、工具、字体和直接 TeX 包在前后核对；额外 `.fls` 输入仍是运行后观察。系统读取不是完整白名单沙箱，同账号恶意并发攻击也不在保证范围内。
- 原始 AST 保真是有界结构契约，不证明任意语义等价；PDF 文本检查不替代逐字形或全页人工阅读。
- 缓存/tmp 不纳入成功证据；它们不是可用于候选或阅读判断的输入。衍生视觉资料独立绑定已提交清单，不回写成功终态。
- 本批不重验 C++ 技术实验，不提升正文接受状态，不重开 Visual Profile，不覆盖历史制品。

uv 行为依据官方 [Python selection](https://docs.astral.sh/uv/concepts/python-versions/) 与 [locked sync](https://docs.astral.sh/uv/concepts/projects/sync/)；这里采用的是本机验收后的固定版本，不把工具升级当作自动兼容。
