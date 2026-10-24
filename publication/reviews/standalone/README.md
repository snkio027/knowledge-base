# 出版引擎独立化：KB 消费者集成

2026-10-24 · **IMPLEMENTED / LOCALLY VERIFIED / REVIEW PENDING**。本次是独立化接入，不是内容、视觉或正式出版版本升级。

## 基线与归属

| 对象 | 本批绑定 |
| --- | --- |
| KB Base | `7fb0ad0c85a4835fabe6482a9e73828d81f25b6a` |
| 独立引擎 | [snkio027/publication-engine](https://github.com/snkio027/publication-engine)，公开仓库 |
| 引擎实现 pin | `e740367ac9c382f245bf29a0b86f019982622154` |
| 内容/产品描述 | [standalone.json](../../standalone.json) |
| 消费者入口 | [run.sh](../../run.sh)，只启动独立项目的 uv 环境 |
| 新输出 | `publication/build/standalone/`，不接管历史目录 |
| 原引擎、布局、环境及测试 | 原字节保留，冻结历史入口，不再双线开发 |
| adapter / profile / corpus / 正文 / 历史证据 / release | 保留在 KB |

引擎与内容/产品/输出根目录分别显式绑定，不要求两个仓库相邻。引擎 pin 校验的是精确提交中选定的通用实现、共享布局、工具和环境配置字节，内容 commit 仍从 KB 解析；不把新引擎 commit 当作内容版本。引擎后续的测试/审核记录提交不改变该实现 pin。描述文件摘要、实际根目录、分立 Git 上下文、输入摘要进入准备身份。

产品 adapter 为可信本地输入，不新增不可信插件机制。快照里的 `publication/engine/`、`publication/latex/` 是保留的虚拟渲染接口，不是物理安装目录约束。所有正式身份 profile 仍可用于本地回归，但 **`artifact_channel=PUBLICATION` 不代表授权发布**。

## 实际执行与结果

本机为 macOS 27.0.1 arm64；Python 3.14.8 和 Python 包统一使用独立项目的 uv 环境。精确工具与摘要见独立仓库 `reviews/standalone/environment.json`。未使用系统 Python，也未运行 GitHub CI。

从 KB 根目录执行，`ENGINE` 表示独立仓库的绝对路径；检查输出目录要求尚不存在：

```sh
uv sync --project "$ENGINE" --locked --group review
uv run --project "$ENGINE" --locked --group review python -B publication/integration/check_engine.py \
  --engine "$ENGINE" --output publication/tmp/standalone-adapters-final.json
uv run --project "$ENGINE" --locked --group review python -B publication/integration/qualify.py \
  --engine "$ENGINE" --output publication/tmp/standalone-real-final
uv run --project "$ENGINE" --locked --group review python -B publication/integration/check_navigation.py \
  --results publication/tmp/standalone-real-final/results.json \
  --output publication/tmp/standalone-navigation-final.json
```

以上三个消费者脚本实际退出码均为 0。`qualify.py` 内依次调用真实 preview、candidate、reading-review 和 inspect-pages；每个命令、耗时、路径、结果和摘要均保存在 [builds.json](builds.json)。一次导航检查曾因外层 uv 缓存写权限未能启动；在允许的本机执行环境重跑后完成，不把未启动的调用计为通过。

### 通用协议与源适配

独立仓库最终 66 项 unittest 通过、0 SKIP；其中 native 文件的 14 项由 7 项组合/判据检查和 7 项真实编译类测试构成。具体运行日志、早期失败试跑与最终摘要保留在独立仓库 `reviews/standalone/`，不是沿用 KB 的旧 139 项结果。

[adapters.json](adapters.json) 记录六个历史 profile 的 58 次源适配检查，包含重复产品视图，不称为 58 份不同章节。共享 LaTeX 两文件、Lua filter、链接解析和结构审计文件与 KB Base 逐字节一致；五个编排函数 AST 一致。

### 三份真实 PDF 回归

| 产品视图 | 页数 | 相同 source/AST 文件 | 位置相同的 destinations | 相同链接注释 | PNG 相同页 |
| --- | ---: | ---: | ---: | ---: | ---: |
| C++ Pilot / G6 | 48 | 6 | 932 | 59 | 47 |
| ESD Reference | 58 | 18 | 1,360 | 34 | 57 |
| FM 全书 | 158 | 33 | 3,239 | 307 | 157 |
| 合计 | 264 | 57 | 5,531 | 400 | 261 |

每份均为 `PREVIEW_READY`，并从相同成功字节生成 `CANDIDATE_PREPARED_FOR_REVIEW`，没有再编译候选，也没有正式发布。完整 source、audit、artifact manifest、candidate manifest 与终态见 [builds/](builds/)。新 PDF 摘要如下，**仅标识本次回归产物，不替换原 Release 摘要**：

```text
G6
35b86701c42e6fad223c14961aa279c42acf5a18ee4056f3ca814ada4e6c5f41
ESD Reference
5e6ca350eee4e9ac33b38a6987604d976a7e18b114875c31f1c4e833d3d7a581
FM
321283afc71d0cfa29a69a67d836ba53efe24737bcfa65be8116e3a5b8d0456c
```

比较对象是上一批 `runtime-evidence/builds/` 记录指向的实际本地制品。比较前核对其 manifest 和全部列入文件摘要，不改旧记录。所有源/原始 AST/适配 AST 字节一致；页数、destination 位置一致。逐页提取文本仅容许明确记录的准备 ID 与源 commit 替换，其余一致。[navigation.json](navigation.json) 进一步比较所有书签层级、页码/位置、链接点击矩形和目标，未用目录链接代替正文链接。

### 视觉证据

264 页全部由 Poppler 渲染。三份 PDF 均仅第 2 页 PNG 不同，变化来自生成的来源/准备身份，已实际打开检查。其余 261 页 PNG 字节相同。

实际查看了 17 张代表页：G6 的 1/2/40/41/48 页；ESD 的 2/3/26/27/58 页；FM 的 1/2/108/109/153/154/158 页。覆盖封面、身份、目录、长代码及续页、空模板、FM literal template 和收尾。页图及摘要见 [visual-review.json](visual-review.json) 和 [pages/](pages/)。结果是 **SELF_REVIEWED_NO_NEW_BLOCKER**，不是独立人工接受、逐页精读或阅读器兼容性验收。

既有 corpus 对 G6、ESD 各命中 3 个 fixture，均为 `STRUCTURAL_PASS`；FM 为 0 fixture / `NOT_COVERED`，不因工具退出 0 而写成 PASS。FM 的补充证据是本批完整新旧比较和指定代表页自查。原有大留白、短尾页、历史试件状态措辞不改，没有新 Visual Profile 或 Typography Pass。

## 保护检查与未验证范围

[protected-files.json](protected-files.json) 对批前 1,639 个路径逐字节核对：其中只有获准的 `publication/README.md` 发生变化，其余 **1,638 个保持一致**。集合包含原全部 tracked 文件、四个已有 zig 未跟踪文件，以及 `publication/build/`、`design/build/`、`design/dist/` 内已有 PDF；其中 481 个已有 PDF 全部不变。新集成文件与本批回归输出不计入“批前不变”集合。

本批没有修改正文、历史 profile、旧引擎/布局、已发布 PDF、release/tag 或 zig 文件；没有搬运历史发布物到新引擎仓库。最终提交仅含消费者入口、描述文件、集成检查、README 和本记录/证据。

提交前另以本地检查器验证 22 个 Python 文件语法、31 个 JSON、5 份 Markdown 的 GFM 解析和 36 个本地链接/锚点，均通过；6 个联网链接未检查。两个仓库 `git diff --check`、`sh -n publication/run.sh`、TOML 解析及测试文件摘要复核通过。这里的静态检查数量不与 66 项回归、58 次适配或 264 页渲染相加。

未执行：407 页 C++ 整书重新构建、全部六产品的全量 PDF 重建、C++ 编译/性能/并发实验、Preview/Chromium/Acrobat 兼容性复测、Linux/Windows/CI、正式发布。没有声明 hermetic build、跨机器字节级可复现或精细 layout dependency closure；`.fls` / 字体依赖仍按既有边界作为运行观察。

本批在 macOS + uv 范围内完成独立化并等待集中审核，不自动启动后续排版架构研究、正文修订或发布。
