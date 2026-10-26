# Knowledge Base

面向高级工程师的系统工程知识与技术手册：通过深入的原理讲解、可运行实验与明确的证据边界，连接系统编程、架构设计和工程实践。

仓库现名为 [`snkio027/knowledge-base`](https://github.com/snkio027/knowledge-base)，由 `snkio027/kb` 原仓库更名，Git 历史不变。旧文档 ID、冻结提交、书名、版本及已发布 PDF 不因仓库更名而改写。

## 项目架构

本项目负责知识内容、内容验证及书籍发布事实；全部活动出版工程由独立 `publication-engine` 承担。在这一边界上，资产管理拟采用开放文件、Git、少量 JSON 资产卡、现有出版证据、字面量检索与可恢复归档，不建立第二套出版系统。

- [架构设计](docs/architecture.md)：当前能力、职责划分、数据流与技术取舍。
- [资产与归档约定](docs/asset-contract.md)：稳定身份、字段权威、路径安全和归档提交边界。
- [实施与验收计划](docs/implementation-plan.md)：能力批次、反例与恢复验收，以及本地目录更名说明。

以上为 `v0.1.0` 设计草案；目录工具、统一归档导入及备份接入尚未实施。

## 阅读入口

| 主题 | 内容 | 入口 |
| --- | --- | --- |
| 系统设计与工程保证 | 方法论、工程手册、治理、证据与运行韧性 | [文档导航与 PDF](design/README.md) |
| Atlas 平台架构 | 平台总体架构、GitOps 控制面与 AI Agent 控制面 | [总体架构](<atlas/Atlas Architecture Design.md>) · [GitOps](<atlas/Atlas GitOps Control Plane Design.md>) · [AI 控制面](<atlas/AI-Native Platform Control Plane Architecture Standard.md>) |
| C++ 学习手册 | G0～G12 系统编程主线与 FM 失败模型专题 | [学习导航](c++/README.md) · [失败模型](c++/failure-model/README.md) |
| 机器人学习与实践 | 从电子测量、单轴控制到桌面交互机器人与学习实验 | [学习导航与手册](robotics/README.md) |
| Zig 项目架构 | 源码组织、模块边界、包生命周期与构建图 | [架构标准](<zig/Zig Project Architecture Standard.md>) |

## PDF 与目录约定

- [design/dist/](design/dist/)：双卷 PDF、构建清单和 SHA-256 校验和。
- [atlas/pdf_build/](atlas/pdf_build/)、[c++/pdf_build/](c++/pdf_build/) 与 [zig/pdf_build/](zig/pdf_build/)：各主题已有的 PDF 及配套 LaTeX 源文件。
- Markdown 保留各文档的版本、适用范围与工程约束；PDF 用于阅读与分享。
- 编译中间文件、渲染预览、系统元数据及本地环境不纳入版本控制。

## 出版与历史资产

出版实现、书籍 profile、adapter、模板、运行环境及活动回归已全部移出本仓库，由独立 [publication-engine 的 knowledge-base 产品包](https://github.com/snkio027/publication-engine/tree/8552be9a80732479195f270b1d5a353690a20233/products/knowledge-base) 接管。显式指定内容 checkout，在内容、产品及活动实现输入之外的专用工作区准备、构建和冻结候选；本仓库不再提供出版命令、Python 出版环境或兼容执行入口。

本仓库仍负责内容验证代码、编辑规范和书籍发布事实，不以“有可执行代码”作为迁出依据。内容、产品、通用引擎与工作区的单一职责合同见 [Repository boundaries](https://github.com/snkio027/publication-engine/blob/8552be9a80732479195f270b1d5a353690a20233/docs/repository-boundaries.md)。

- [出版接管与归档说明](publication/README.md)：获取入口、版本锁定、历史路径与恢复方式。
- [Modern C++ 工程学习手册 v1.0.0](https://github.com/snkio027/knowledge-base/releases/tag/cpp-handbook-v1.0.0)。
- [C++23 失败语义工程手册 v1.0.0](https://github.com/snkio027/knowledge-base/releases/tag/cpp-failure-model-v1.0.0)。

`publication/` 仅保留说明、出版工程经验、设计研究及历史审核/发布资产；其中的历史脚本属于原始证据，不是当前运行入口。已发布 PDF 不随活动正文变化自动更新，也不因重新构建而被替换。
