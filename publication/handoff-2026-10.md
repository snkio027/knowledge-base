# Knowledge Base 更名与出版接管

日期：2026-10-26。状态：**IMPLEMENTED / PENDING REVIEW**。

本轮依据用户“全部迁出，仅留内容与历史资产”的确认执行。Base 为 `a022de309c0ce5c3af0d306e57691f036d869698`；仓库由 `snkio027/kb` 更名为 `snkio027/knowledge-base`，稳定 repository ID 仍为 `1334077602`，保持公开。`knowledge-base` 是“知识库”的正确拼写。

## 接管结果

- 活动出版实现、环境声明、兼容入口、书籍 profile/adapter/template/theme、corpus 和消费端检查全部迁出。当前 checkout 删除 107 个文件，Git 历史保留可恢复的原件。
- [publication-engine 产品包](https://github.com/snkio027/publication-engine/tree/9d82561f3881d467879e7d5c9676c3f6905b37d0/products/knowledge-base) 接管 34 份逐字节迁入文件及适配后的检查入口；接管提交固定为 `9d82561f3881d467879e7d5c9676c3f6905b37d0`。通用引擎不增加书籍分支，选定实现仍锁定并逐字节校验为 `df3fcc238f03a3832de55bc128049adebe323969`。
- 新描述文件、预览、渲染、候选与回归输出全部在内容仓库外；本地 `publication/build/`、`design/build/` 和既有证据不接管、不覆盖。
- 本仓库只更新根/设计/出版导航、接管说明及资产登记的历史链接。六篇 ESD、C++/FM/Zig 正文、实验与 Gate 不变。

完整机器证据、命令、迁移清单、页图与范围见独立项目的[本批审核入口](https://github.com/snkio027/publication-engine/tree/9d82561f3881d467879e7d5c9676c3f6905b37d0/reviews/content-handoff)。其中 migration 清单固定迁入来源，本记录不复制第二套可执行检查或环境。

## 实际验证

| 维度 | 结果 |
| --- | --- |
| 通用引擎回归 | 75 PASS / 0 SKIP，包含原 P1/P2 反例 |
| 外部配置边界 | 10 PASS；拒绝覆盖、链接路径、错误 root 和版本/产品漂移 |
| 产品迁移 | 34 文件字节相同，58 项源适配检查通过，六个 profile 输入准备通过 |
| 真实构建 | G6 48 页、ESD Reference 58 页、FM 158 页；264 页全页渲染并冻结候选 |
| 保真与导航 | 57 份 source/AST 相同，5,531 个目标位置与 400 个链接及书签相同 |
| 视觉回归 | 261 张 PNG 相同；三份第 2 页仅生成身份变化；9 页代表样张自查无迁移新增阻断 |
| 文档检查 | 原检查器检查 72 份 Markdown、977 处本地链接，无错误 |
| 本地保护 | 1,678 个受保护文件字节相同，含 517 份已有 PDF；四个 Zig 未跟踪文件不变 |
| 远端保护 | 两组 tag、两条 Release、八个资产 ID/大小/GitHub 摘要相同；旧 URL 重定向至同一仓库 |

首次文档检查发现旧资产登记中的四个脚本链接随删除失效；本轮仅把其五处实现链接（含模板目录）改为登记原语境的 `6ad0ade` 固定提交，并添加迁移注记，随后复跑通过。未放宽检查器，也未把旧核对结果改写成新执行。

## 历史资产与恢复

`publication/releases/`、`publication/reviews/`、`design/dist/` 及已有 PDF/LaTeX 保持原路径、原字节。目录中的历史脚本是证据附件，不是当前构建系统；使用历史命令须回到对应提交，不能自动授予新资格。

被删除的跟踪文件可在[迁移前提交](https://github.com/snkio027/knowledge-base/tree/a022de309c0ce5c3af0d306e57691f036d869698)恢复。本机旧 `publication/.venv` 和移除目录中的 macOS 元数据转入 `/private/tmp/knowledge-base-migration.xcEwi6/` 临时归档，没有递归删除历史构建目录。临时归档不是长期备份；环境可按历史锁文件重建。

本地工作目录仍为原 `kb` 路径，仅 GitHub 名称和 origin 已更新，避免打断现有工具/证据中的本机路径。旧名称不可重新占用，否则历史 URL 重定向可能失效。

本轮没有重新发布、替换 PDF 或改变书籍版本；没有重跑 C++、性能、并发实验或阅读器兼容测试。没有重新下载 GitHub Release 资产；远端保护是更名前后元数据与 tag 的核对。本批本地结果不声明 CI 或用户审核通过。
