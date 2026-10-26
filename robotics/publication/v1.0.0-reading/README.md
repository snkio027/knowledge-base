# 机器人学习与实践手册 PDF 阅读版

[下载或打开 PDF](output/pdf/Robotics-Learning-Handbook-v1.0.0-reading.pdf)。本件共 **28 页**，包含封面、版本说明、可点击目录及全部正文。2026-10-26 构建，2026-10-27 保存到知识库。

内容来自固定提交 `2b90ad93f29800f08d1bc8f6b9083c8904dae7da` 的[原稿](../../robotics-learning-handbook-v1.0.md)。23 个主题、R0—R7 八个阶段、30 项参考资料及四个字面块均保留；没有改写正文或补造实验结果。

## 文件身份

| 项目 | 记录 |
| --- | --- |
| 出版视图 | `ROBOTICS-HANDBOOK / 1.0.0 / PREVIEW` |
| 正文状态 | `proposed-learning-baseline`，不是技术验收基线 |
| PDF 大小 | 872,798 字节 |
| PDF SHA-256 | `af995ba9a2ab09e4c8e126c20458cf1222bde4e6486793f07b826b371628e876` |
| 原稿 SHA-256 | `bb7e3b010fce93a9eb338271264467bc177c70a21cdeb3bb0123d9e5d781663b` |
| 外部产品交付 | [publication-engine@21958db](https://github.com/snkio027/publication-engine/commit/21958dbf9ccb375c8058986cf4ab4db61b01db57) |
| 产品与引擎 | `knowledge-base / 1.2.0`；实现 pin `f809e51d15dc7b5937aac02aee4dcbba31f40098` |
| 版式 | 复用 Visual Profile v1.0；机器人身份页和参考条目分页在产品侧配置 |
| 冻结候选 ID | `8e149eedd3995083794dfa3198770fe8444572da37052c129635755e4210b8d7` |
| 正式分发 | 未创建 GitHub Release 或 tag；`publish` 未执行 |

[build-record.json](build-record.json)列出输入、制品及随件证据摘要；[SHA256SUMS](SHA256SUMS)供下载后校验。构建、模板、adapter 和测试继续在独立出版项目维护，本目录只保存阅读资产与事实记录。

## 阅读与检查结果

PDF 的主题目录、书签、阶段回查与 S 编号支持跳转。先读定位、硬件和环境，再按 R0—R7 实践；任何上电或运动前先读第 18 节，并核对实际板卡及接线。

自动检查覆盖 28 页渲染、95 个源标题区域、491 个有序内容单元、10 处 inline literal 和 130 条表格行关系。另对 54 个显式源目标和 88 处正文内部链接的实际点击区域逐项核对，30 个参考 URL 均有链接区域。30 项参考资料的标题与说明保持同页，没有以目录或书签链接替代正文链接。

视觉自查包括全页缩略图，以及封面、控制页、目录、阅读导航、采购表、公式与 PI 骨架、安全、代码目录、学习单元、实验模板、参考资料的详细页检；未发现裁切、重叠或缺字。参考条目曾在初次试排跨页，已在新产品配置中修正并重新构建。九类语义 fixture 结果为 `STRUCTURAL_PASS`。

- [构建审计](evidence/preview-audit.json)与[源保真结果](evidence/source-fidelity.json)。
- [正文导航核对](evidence/navigation-check.json)与[阅读样本页表](evidence/page-map.json)。
- [第 1—20 页缩略图](evidence/pages-01-20.png)与[第 21—28 页缩略图](evidence/pages-21-28.png)。
- [独立产品审核记录](https://github.com/snkio027/publication-engine/blob/21958dbf9ccb375c8058986cf4ab4db61b01db57/reviews/robotics-reading/README.md)：9 项定向回归、13 项配置回归及 59 项源适配检查。

这些是本机自动检查和视觉自查，不是 CI 或独立接受；没有执行 Preview、Chromium、Acrobat 的交互兼容性测试。文献核验日期仍是原稿声明，本次没有联网重验资料，也没有进行硬件、控制算法或学习策略实验。PDF 不是采购建议的重新核准、实机安全认证或正式发布批准。

## 证据与保护边界

本目录保存**精选证据**，不是完整可执行候选包。候选清单及 artifact manifest 仍描述原始工作区的完整集合；未随本目录复制的输入、全尺寸页图和日志可以按其摘要在原候选中核对，不能据本目录的子集宣称已独立重验整个运行快照。原始工作区路径保留为历史事实，不作为新的运行入口。

本批没有修改权威 Markdown、共享出版引擎、旧 profile、历史已发布 PDF 或 `design/dist/`。517 份历史 PDF 及相关受保护资产的摘要核对通过，四个 Zig 未跟踪文件保持原样。新的阅读资产从冻结候选复制后再次核对摘要，不覆盖任何旧制品。
