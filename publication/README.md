# 出版接管与历史资产

2026-10-26：仓库由 `snkio027/kb` 更名为 [`snkio027/knowledge-base`](https://github.com/snkio027/knowledge-base)。出版系统及书籍专用配置已迁出，当前目录不是可执行的出版项目。

## 当前入口

请使用独立 [publication-engine / knowledge-base 产品包](https://github.com/snkio027/publication-engine/tree/8552be9a80732479195f270b1d5a353690a20233/products/knowledge-base)，checkout 交付版本 `8552be9a80732479195f270b1d5a353690a20233`，不自动跟随 main。当前产品为 `knowledge-base / 1.1.0`，由产品清单显式锁定实现 `f809e51d15dc7b5937aac02aee4dcbba31f40098`。交付提交、引擎 pin、产品版本、内容 revision 与书籍出版版本不能互相代替。

原迁入来源 `a022de309c0ce5c3af0d306e57691f036d869698` 和接管版本 `9d82561…` 仍是历史事实，migration.json 不再充当日常配置。当前清单绑定 34 份产品输入，配置生成工作区中的 project.json；每次准备重新核对产品身份与字节。职责、写入及验证规则只在 [Repository boundaries](https://github.com/snkio027/publication-engine/blob/8552be9a80732479195f270b1d5a353690a20233/docs/repository-boundaries.md) 维护，本仓库不复制另一套规范。

产品包包含六个 profile、adapter、模板、主题、ESD 出版依赖、阅读 corpus 与消费端检查。配置时显式指定本仓库 checkout 和外部工作区，不依赖仓库相邻，不在本仓库写入新预览、环境或缓存。“外部”指内容、产品与活动实现输入之外，引擎 checkout 的忽略目录 tmp 可以作为专用工作区。使用命令与回归入口只在独立项目维护，本仓库不保留 `run.sh`、`standalone.json` 或第二套实现。内容实验与技术验证脚本继续属于本仓库。

本轮[集中验收记录](https://github.com/snkio027/publication-engine/blob/8552be9a80732479195f270b1d5a353690a20233/reviews/repository-boundaries/README.md)：84 项通用回归、13 项配置回归和 58 项适配检查通过；两个不含旧本机构建目录的干净 checkout 完成 G6、ESD Reference、FM 三份制品，共 264 页。历史比较另外显式指定基线，不再是日常验收的隐式依赖。FM 阅读 fixture 仍为 0 / NOT_COVERED；这些是本地证据和代表页自查，不是 CI、全书技术重验或新发布。本次只更新本仓库的两份入口说明，正文与历史资产不变。

历史 profile 保持原字节，其中的 `https://github.com/snkio027/kb` 仍表示更名前的同一来源仓库，依赖 GitHub 更名重定向；新产品说明使用当前名称。不要重新创建同账号下的 `kb` 仓库，以免历史链接重定向失效。

## 本目录保留什么

| 路径 | 身份 |
| --- | --- |
| [releases/](releases/) | 已发布 PDF、摘要、授权与分发回执；不可覆盖 |
| [reviews/](reviews/) | 原始构建/审核证据，保持当时路径、命令和摘要 |
| [lessons-learned.md](lessons-learned.md) | 出版工程复盘，作为知识内容保留 |
| [layout-architecture-next.md](layout-architecture-next.md) | 历史设计研究；不是实施授权或活动配置 |
| 本地忽略的 `build/`、`tmp/` | 已有尝试与衍生证据，仅供历史回查，不被新入口接管 |

`reviews/`、`releases/` 内已有脚本是证据附件，不是受支持的当前构建入口。其依赖、命令和相对链接属于原提交语境，不能直接用新引擎运行，也不补写成新协议成功记录。

## 已发布手册

- [Modern C++ 工程学习手册 v1.0.0](https://github.com/snkio027/knowledge-base/releases/tag/cpp-handbook-v1.0.0)：[发布记录](releases/cpp-handbook/v1.0.0/README.md)。407 页，PDF SHA-256 `ce4f6d5f6e4b8c1e2789eedd1fc151462d31e929b724ce2eb95c780f90766510`。
- [C++23 失败语义工程手册 v1.0.0](https://github.com/snkio027/knowledge-base/releases/tag/cpp-failure-model-v1.0.0)：[发布记录](releases/cpp-failure-model/v1.0.0/README.md)。158 页，PDF SHA-256 `2957aab0ad153873307a83af9383f08dabcfb3caae8c5f27750a6f48ee3c4e9c`。

更名和迁移不改变这些制品、tag、内容基线或发布身份。通过构建检查不代表新的发布授权；通用 `publish` 仍关闭。

## 初次迁出与恢复边界

初次接管提交 `be9ec52…` 从当前 checkout 删除内嵌 `engine/`、`latex/`、`tests/`、`tools/`、`profiles/`、`integration/`、Python 环境声明及旧启动配置；同时删除 `design/scripts/`、`design/publication/` 及其三个环境/字体记录。34 份仍需运行的产品文件逐字节迁入独立产品包；过时引擎和 v1 脚本不再作为另一套活动实现复制过去。

完整删除清单与文件摘要登记在独立产品包的 `migration.json`。所有被删除的已跟踪文件仍可在[迁移前精确提交](https://github.com/snkio027/knowledge-base/tree/a022de309c0ce5c3af0d306e57691f036d869698)中查看或恢复。历史记录中的本地链接若指向已删除实现，应在这个提交或记录所指定的更早提交中解析；不为保持当前工作树链接而伪造占位实现，也不改写历史证据。

正文、实验、Gate、旧 PDF/LaTeX 制品、`design/dist/`、审核记录和未跟踪 Zig 材料保持原字节。迁移验证结果见 [2026-10 接管记录](handoff-2026-10.md)。
