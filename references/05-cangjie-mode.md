# 05 · 仓颉模式（cangjie-skill / 知识精馏）

上游：[kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)。
**定位**：把书 / 长视频 / 播客 / 访谈 / 课程等**内容**蒸馏成可执行的 Agent Skills。
注意：仓颉蒸馏的是"内容"，与前三个蒸馏"人"的技能不同类，互为补充。

## 它解决什么问题

- 读了/看了/听了不用——知识停留在"已读"层，不能在真实决策里被调用；
- 摘要/笔记/整理稿都是"压缩"，不是"结构化复用"——读完仍不知道"什么时候用什么"；
- 只有一小部分高价值内容值得变成工具——需要严格筛选，而非全盘收录；
- 现有阅读/学习方式是为"人"设计的，蒸馏必须为"Agent"服务——执行导向而非消费导向。

## 核心流水线：RIA-TV++（七阶段）

| 阶段 | 名称 | 做什么 |
| --- | --- | --- |
| 1 | 整书理解（Adler 分析） | 用 Mortimer Adler 四层阅读法做结构/解释/批判/适用性分析，产出 `BOOK_OVERVIEW.md` |
| 2 | 并行提取 | 5 个专门提取器（框架 / 原则 / 案例 / 反例 / 术语）同时跑，从原文拉候选单元 |
| 3 | 三重验证 + 晋升门 | 按候选类型检查：来源充分性、可执行性、任务效用。重复或作者原创非强制 |
| 4 | RIA++ 能力构建 | 验证内容结构为 R/I/A1/A2/E/B 能力卡，存入 `.cangjie/capabilities/` |
| 5 | 卡片盒链接 | 依赖/对比/组合编码进 Bundle 的能力图与共享术语表 |
| 6 | 压力测试 | 为每个 Skill 设计诱饵问题（含跨 Skill 混淆测试）；失败则回炉重建 |
| 7 | 确定性编译交付 | 同一 Bundle 编译为单包/紧凑包，附读者向 `DIGEST.md`、验证结果、可安装产物 |

> RIA 源自赵周的便签拆书法（Reading / Interpretation / Appropriation）；
> TV = Triple Verification（三重验证）；++ = Agent 导向扩展（E 执行 + B 边界）。

## 能力卡六维（每个 Skill 的结构）

| 维度 | 含义 |
| --- | --- |
| **R** Original evidence | 原始证据（出处） |
| **I** Reconstructed explanation | 重构解释 |
| **A1** Book-sourced examples | 书中示例 |
| **A2** Trigger scenarios | 触发场景 |
| **E** Executable steps | 可执行步骤 |
| **B** Known limitations | 已知局限 |

## 输出形态（不是一篇摘要，而是一套仓库）

```
BOOK_OVERVIEW.md      # 整书理解
INDEX.md              # 索引
DIGEST.md             # 读者向精华长文
GLOSSARY.md           # 核心词典
*/SKILL.md            # 多个原子化 Skill（取决于知识密度）
test-prompts.json     # 触发/压力测试
```

## 实战样本

已蒸馏：《认知红利》《穷查理宝典》《大道：段永平投资问答录》《不拘一格：网飞的自由与责任工作法》
《巴菲特致股东的信(1957–2024)》（从中蒸馏出 20 个 Skill）。

## 局限与注意

- 只处理**系统性表达过的内容**；对没有沉淀材料的人/事无效。
- 一本书产出多个 Skill，**管理成本**高（多文件仓库 + capabilities 图）。
- 重方法论，上手成本高于"输入一个名字"的女娲。
- 依赖源文本质量：需要字幕/转录/文本；视频建议配合 video-downloader 先下载提取字幕。
- 仍较新，community 规模相对早期；兼容 50+ runtime + DeepSeek Harness 插件，MIT。
