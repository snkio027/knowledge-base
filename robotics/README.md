# 机器人学习与实践

[《机器人学习与实践手册：从电子与控制基础走向智能机器宠物》](robotics-learning-handbook-v1.0.md)以可测量的单轴运动系统为起点，逐步连接反馈控制、固件、感知、交互与机器人学习。Markdown 是长期维护正文；本次接收保留原稿字节，不重写内容，也不将建议学习基线升级为技术验收或正式出版基线。

## 阅读顺序

首次阅读从[定位与目标](robotics-learning-handbook-v1.0.md#sec01)、[硬件选择](robotics-learning-handbook-v1.0.md#sec05)和[开发环境](robotics-learning-handbook-v1.0.md#sec07)开始，再按阶段进入练习。涉及真实上电或运动前，先阅读[实验安全与故障响应边界](robotics-learning-handbook-v1.0.md#sec18)，并核对实际设备资料。

| 阶段 | 主题入口 |
| --- | --- |
| R0 | [电气基础与可调试执行](robotics-learning-handbook-v1.0.md#sec08) |
| R1 | [电机、编码器与测量误差](robotics-learning-handbook-v1.0.md#sec09) |
| R2 | [从模型到闭环控制](robotics-learning-handbook-v1.0.md#sec10) |
| R3 | [可靠固件与本地故障响应](robotics-learning-handbook-v1.0.md#sec11) |
| R4 | [坐标、感知、时间与状态估计](robotics-learning-handbook-v1.0.md#sec12) |
| R5 | [ROS 2、仿真与真实硬件集成](robotics-learning-handbook-v1.0.md#sec13) |
| R6 | [桌面机器宠物原型](robotics-learning-handbook-v1.0.md#sec14) |
| R7 | [数据、模仿学习与任务评测](robotics-learning-handbook-v1.0.md#sec15) |

[前十次学习单元](robotics-learning-handbook-v1.0.md#sec21)用于安排练习；[实验与决策模板](robotics-learning-handbook-v1.0.md#sec22)用于保存预测、条件和结果；[一手参考资料](robotics-learning-handbook-v1.0.md#references)用于回查来源。这里的 R0—R7 是本手册的学习阶段，不是 ESD 项目试点编号。

## 与已有内容的关系

[C++ G11 机器人系统工程](../c++/g11-robotics.md)侧重时间、状态、并发与执行合同；本手册补充从电子测量到实体机器人学习的实践路线。两者保持独立身份，本次不修改 G11 或既有手册的接受记录。

手册中的 `robotics-lab/` 是未来实践项目的目录示例，不是本次已创建的工程。接收正文不启动硬件实验、采购、软件安装或周期任务，也不新增出版 profile。

## 原稿接收记录

| 项目 | 记录 |
| --- | --- |
| 接收日期 | 2026-10-26 |
| 来源 | 用户提供的 Markdown 文件 `robotics-learning-handbook-v1.0.md` |
| 原稿 ID | `robotics-learning-handbook` |
| 原稿版本 | Front Matter：`1.0.0`；封面简称：`v1.0` |
| 原稿状态 | `proposed-learning-baseline`，原样保留 |
| 维护入口 | [robotics-learning-handbook-v1.0.md](robotics-learning-handbook-v1.0.md) |
| 接收字节数 | 64,208 |
| 接收 SHA-256 | `bb7e3b010fce93a9eb338271264467bc177c70a21cdeb3bb0123d9e5d781663b` |
| 原稿声明的资料核验日 | 2026-10-26；属于原稿声明，不是本次独立重验 |
| Word 及 PDF | 本轮未接收、未生成、未检查；“28 页”不登记为 Markdown 页数或已核验制品页数 |

本次只进行原件一致性与文档结构检查：核对 23 个编号主题、R0—R7 八个阶段、S01—S30 参考条目，以及本地链接和锚点。外链可用性、硬件参数、软件兼容性、前沿研究结论和实机安全未在本次重新验证；原稿声明的验证边界继续保留。

接收检查中，原稿比较、Markdown/YAML 解析和 122 处本地链接／锚点检查通过。默认 `git diff --cached --check` 报告原稿第 1015 行存在文件末尾空行；为保持原始字节，此项作为接收例外保留，不登记为默认空白检查全部通过。导航文件不适用这一例外。

接收提交中的文件字节作为原稿快照由 Git 保存，当前路径作为后续维护入口，不另造一份并行正文。未来修改遵循原稿的版本约定，保留固定提交与审核范围；Word 批注应回收至 Markdown 后再生成阅读版本。本次不触发出版或发布。
