# 出版接管与历史资产

2026-10-26：仓库由 `snkio027/kb` 更名为 [`snkio027/knowledge-base`](https://github.com/snkio027/knowledge-base)。出版系统及书籍专用配置已迁出，当前目录不是可执行的出版项目。

## 当前入口

请使用独立 [publication-engine / knowledge-base 产品包](https://github.com/snkio027/publication-engine/tree/9d82561f3881d467879e7d5c9676c3f6905b37d0/products/knowledge-base)，checkout 接管版本 `9d82561f3881d467879e7d5c9676c3f6905b37d0`，不自动跟随 main。该提交包含产品与审核记录；选定引擎实现仍固定并校验为 `df3fcc238f03a3832de55bc128049adebe323969` 的字节。产品包的迁入身份绑定本仓库 `a022de309c0ce5c3af0d306e57691f036d869698`。本次不是引擎升级、版式修订或正式发布。

产品包包含六个 profile、adapter、模板、主题、ESD 出版依赖、阅读 corpus 与消费端检查。配置时显式指定本仓库 checkout 和外部工作区，不依赖仓库相邻，不在本仓库写入新预览、环境或缓存。使用命令与回归入口只在独立项目维护，本仓库不保留 `run.sh`、`standalone.json` 或第二套实现。

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

## 删除与恢复边界

本轮从当前 checkout 删除内嵌 `engine/`、`latex/`、`tests/`、`tools/`、`profiles/`、`integration/`、Python 环境声明及旧启动配置；同时删除 `design/scripts/`、`design/publication/` 及其三个环境/字体记录。34 份仍需运行的产品文件逐字节迁入独立产品包；过时引擎和 v1 脚本不再作为另一套活动实现复制过去。

完整删除清单与文件摘要登记在独立产品包的 `migration.json`。所有被删除的已跟踪文件仍可在[迁移前精确提交](https://github.com/snkio027/knowledge-base/tree/a022de309c0ce5c3af0d306e57691f036d869698)中查看或恢复。历史记录中的本地链接若指向已删除实现，应在这个提交或记录所指定的更早提交中解析；不为保持当前工作树链接而伪造占位实现，也不改写历史证据。

正文、实验、Gate、旧 PDF/LaTeX 制品、`design/dist/`、审核记录和未跟踪 Zig 材料保持原字节。迁移验证结果见 [2026-10 接管记录](handoff-2026-10.md)。
