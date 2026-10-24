# 独立引擎 P1/P2 修复：KB 集成回归

2026-10-24 · **IMPLEMENTED / LOCALLY VERIFIED / REVIEW PENDING**。这是安全边界修复和消费者重锁，不是正文、Visual Profile 或手册出版版本升级。

## 基线与修改边界

- KB Base：`ffd2db9999a79bb237954ad45a6c59117baa38e6`。
- 引擎审核 Base：`5acfa5448957cf7c9ad755db510c48042b5c91fa`；旧选定实现 pin：`e740367ac9c382f245bf29a0b86f019982622154`。
- [standalone.json](../../standalone.json) 的最终新 pin：`df3fcc238f03a3832de55bc128049adebe323969`。后续引擎说明/证据提交不改变被选定实现字节。
- KB 只更新 pin、两个会导入引擎的集成检查、README 和本批记录。正文、历史 profile、旧引擎/布局、旧审核记录、release 和 zig 文件均不变。

引擎 P1 修复在受支持脚本的第一次文件系统模块导入前安装源码策略，timestamp/hash 缓存不执行，无源码字节码拒绝；策略自身从原始源码加载。P2 修复让 preview / candidate 共用完整路径逐级 no-follow，候选保持同一个验证后的输出根句柄直到完成。详细反例、信任边界及 75 项最终回归见[独立引擎审核记录](https://github.com/snkio027/publication-engine/tree/main/reviews/safety-boundaries)。这不是对任意 Python、被篡改解释器或不可信插件的隔离承诺。

## 本机实际执行

下列命令均退出 0。`ENGINE` 是 `/Users/nekoreb/Workspace/03_Projects/publication-engine`；工作目录是 KB。临时路径只标识这次执行，不是新的仓库依赖。

```sh
uv run --project "$ENGINE" --locked --group review python -B publication/integration/check_engine.py \
  --engine "$ENGINE" --output /private/tmp/publication-safety-fix.nv4n7E/adapters-guard-final.json
uv run --project "$ENGINE" --locked --group review python -B publication/integration/qualify.py \
  --engine "$ENGINE" --output /private/tmp/publication-safety-fix.nv4n7E/real-guard-final
uv run --project "$ENGINE" --locked --group review python -B publication/integration/check_navigation.py \
  --results /private/tmp/publication-safety-fix.nv4n7E/real-guard-final/results.json \
  --output /private/tmp/publication-safety-fix.nv4n7E/navigation.json
```

macOS 27.0.1 arm64、uv-managed CPython 3.14.8；工具链与引擎环境记录相同。未使用系统 Python，不声明 CI 结果。

[adapters.json](adapters.json)：六个历史 profile 共 58 次适配检查通过；这是多产品视图检查，不是 58 份不同章节。共享 LaTeX、Lua filter、链接/结构审计文件与抽取前字节相同；五个视觉编排函数的 AST 相同。引擎唯一 preview 改动是启动导入策略，未改编排函数。

### 最终三份真实 PDF

| 视图 | 页数 | 相同源/AST 文件 | 相同 destination 位置 | 相同链接注释 | 相同 PNG 页 |
| --- | ---: | ---: | ---: | ---: | ---: |
| G6 | 48 | 6 | 932 | 59 | 47 |
| ESD Reference | 58 | 18 | 1,360 | 34 | 57 |
| FM 全书 | 158 | 33 | 3,239 | 307 | 157 |
| 合计 | 264 | 57 | 5,531 | 400 | 261 |

[builds.json](builds.json) 保存精确命令、耗时、attempt、候选路径和摘要；[builds/](builds/) 保存对应 run / ready / audit / artifact manifest / candidate manifest。三份均 `PREVIEW_READY`，再以相同字节生成 `CANDIDATE_PREPARED_FOR_REVIEW`，没有在候选阶段重编译。[navigation.json](navigation.json) 比较书签、页码、链接矩形与目标，不用 TOC 链接代替正文链接。

比较基线仍为上一批实际使用的 `runtime-evidence` 制品，先核验旧 manifest 与列入文件摘要，再进行比较。源/AST、分页及 destination 位置不变；文本只允许明确登记的生成身份替换；所有页图只有各书第 2 页改变。最终 PDF 摘要仅标识本次回归，**不替代 Release 摘要**：

```text
G6:  a5c0568f3bc55e8e0fe308679eb7d7dfafad64b3a9059639079fea651ac19b9d
ESD: 8f939349cc6019d07e5abfc8a82ebc730e1c75f40cf8688ea29f68d9c772b5c1
FM:  3369c28bc68786d0652a177ecf947802f915cd37b57d6b8c372fd1d14c0e6f17
```

实际查看 11 张代表页：G6 2/40/41，ESD 2/26/27，FM 2/108/109/153/154。覆盖三处生成身份变化、长代码与续页、空模板和 FM literal template。样张与摘要见 [visual-samples.json](visual-samples.json)，观察见 [visual-review.json](visual-review.json)。结论是自查未见新增 blocker，不是逐页精读、独立接受或阅读器兼容性重测。原有留白、短尾、历史 profile 状态措辞保持不动。

G6 / ESD 既有 corpus 各覆盖 3 项，均 `STRUCTURAL_PASS`；FM 为 0 项 / `NOT_COVERED`。不把 FM 的工具退出 0 写成 corpus 通过，其补充证据是全页比较与上述代表页自查。

## 历史保护、试跑与未验证范围

[protected-files.json](protected-files.json) 核对批前 **1,700 个路径**。仅四个授权集成文件变化，其余 **1,696 个逐字节一致**；其中 **493 个已有 PDF** 全部不变，四个 zig 文件仍未跟踪且字节不变。该集合包含批前 tracked 文件、已有 PDF 和 zig 未跟踪文件，新回归产物不混入“原有文件不变”计数。

本批先在 `438b015` 完成一次三产品试跑，其记录单独保留于 [trials/438b015-builds.json](trials/438b015-builds.json)。自查补齐启动同名缓存反例后，最终按 `df3fcc2` 全量重跑，当前审核包只绑定后者。收集时明确校验 final test count、构建 engine pin 和原始结果摘要；早期试跑不替代最终结果，也没有回写旧独立化证据。

未执行：407 页整书和全部六产品全量重建、C++ 编译/性能/并发实验、外部阅读器 smoke、Linux/Windows/CI、正式发布。没有改 release/tag，没有开启 `publish`，正式身份 profile 的本地回归也不构成发布授权。本批完成后停止，等待集中审核。

提交前静态核对：23 个 Python 文件语法、34 个 JSON、4 份 Markdown 的 GFM 解析和 40 个本地链接/锚点通过；4 个外链未检查。两个仓库的差异空白检查、既有入口 shell 语法、TOML 解析、被测文件摘要与实现 pin 核对通过。见 [static-checks.json](static-checks.json)；这些数量不与回归测试、适配次数或 PDF 页数相加。
