---
name: cht-zhengliu-skill
description: 统一的人物与知识蒸馏编排技能（正流 / Zhengliu）。把"同事、公开人物、你自己、书籍/视频/播客"四类对象蒸馏成可执行的 Agent Skill。整合 colleague-skill（同事）、nuwa-skill（女娲）、yourself-skill（自己）、cangjie-skill（仓颉）四套方法论，提供模式路由、双层架构、三重验证与版本演化，做到"装一次、处处可用"。
---

# cht-zhengliu-skill · 蒸馏总编排

> **正流（Zhengliu）**：把散落的经验、思想与知识，整理成一条可复用、可调用、可验证的"正确流程"。
> 本 Skill 是 cuohuatang 出品的**蒸馏编排器**——它不直接"替代"四套上游技能，而是把它们统一成
> 一个入口：**你告诉它要蒸馏什么，它路由到正确的方法论，并按统一标准产出可被 Agent 加载的 Skill。**

## 它能做什么

把任意一种"值得被复用"的对象，蒸馏成一个结构化的 Agent Skill：

| 模式 | 蒸馏对象 | 上游方法论 | 典型产物 |
| --- | --- | --- | --- |
| **colleague（同事）** | 身边人 / 工作搭档 | colleague-skill（已演进为 Distilly） | Work Skill（能力层）+ Persona（人格层） |
| **nuwa（女娲）** | 公开人物 / 思想家 | nuwa-skill | 五层心智模型（怎么想 / 怎么判断 / 什么不做 / 诚实边界） |
| **yourself（自己）** | 你自己 | yourself-skill | Self Memory（自我记忆）+ 5 层人格结构（数字分身） |
| **cangjie（仓颉）** | 书 / 长视频 / 播客 / 课程 | cangjie-skill | 能力包 Capability Bundle（R/I/A1/A2/E/B 能力卡） |

> 前三种蒸馏"人"，第四种蒸馏"内容"。两者共用本 Skill 的**验证层**与**演化层**。

## 路由决策（先判断模式，再开工）

收到"帮我蒸馏 XXX"类请求时，按下面顺序判定模式：

1. 对象是一个**你身边、有聊天/邮件/文档数据可喂的人**（同事、前任、朋友）→ `colleague`
2. 对象是一个**公开人物，你手里只有他公开留下的著作/访谈/社媒**（芒格、费曼、马斯克…）→ `nuwa`
3. 对象是**你自己**，要用自己的聊天记录/日记/照片造分身 → `yourself`
4. 对象是一份**系统性表达过的内容**（一本书、一场长访谈、一期播客）→ `cangjie`

判定不清时，先问用户一句话："你要蒸馏的是**一个人**，还是**一份内容**？如果是人，是你身边的人还是公开人物？"

## 通用工作流（四步）

无论哪种模式，都走这条统一流水线：

1. **采集（Collect）**——按模式选择数据源（见各模式参考文档），强调"来源实证"，不编造。
2. **提炼（Extract）**——用对应方法论把原材料拆成可复用单元；人物类用**双层架构**（能力层 + 人格层），内容类用 **RIA-TV++**。
3. **验证（Verify）**——强制过**三重验证**（跨域出现 / 预测力 / 排他性）+ 拿真实问题做压力测试，不过不收录。
4. **产出 & 演化（Emit & Evolve）**——写入 `SKILL.md`，支持**追加数据增量合并、对话纠正、版本回滚**。

## 目录与参考

- `references/00-overview.md` —— 总览与路由决策表
- `references/01-person-layer.md` —— 人物建模通用层（双层架构 + 演化/回滚）
- `references/02-colleague-mode.md` —— 同事模式（数据源、Work Skill + Persona）
- `references/03-nuwa-mode.md` —— 女娲模式（6 路并行 + 五层心智模型）
- `references/04-yourself-mode.md` —— 自己模式（Self Memory + 5 层人格 + 解析器）
- `references/05-cangjie-mode.md` —— 仓颉模式（RIA-TV++ 七阶段 + 能力卡）
- `references/06-verification.md` —— 三重验证 + 保真度评分卡
- `references/templates/skill-template.md` —— 生成 Skill 的骨架模板
- `references/templates/persona-template.md` —— 人格/Persona 结构模板
- `scripts/scaffold.py` —— 一键生成蒸馏 Skill 骨架
- `scripts/verify.py` —— 结构与保真度自检
- `assets/architecture.svg` —— 蒸馏编排架构图（总览用）

## 安装方式

```bash
# 方式一：放到任意 skills 兼容 runtime（目录名必须严格等于 name 字段）
git clone https://github.com/cuohuatang/cht-zhengliu-skill ~/.codebuddy/skills/cht-zhengliu-skill
# 或 Claude Code / Codex / Cursor 等的 skills 目录

# 方式二：一行命令（skills 兼容安装器）
npx skills add cuohuatang/cht-zhengliu-skill
```

装好后，对 Agent 说：

```
> 用正流帮我蒸馏一个同事：把飞书聊天记录 + 他的设计文档喂进去
> 用正流蒸馏芒格的心智模型
> 用正流造我的数字分身（导入微信聊天记录 + 日记）
> 用正流把《穷查理宝典》蒸馏成一组可执行的 Skill
```

## 诚实边界（必读）

- 人物蒸馏**不宣称克隆人**，只是来源实证的"认知镜像"。
- 公开人物蒸馏基于**公开信息**：公开表达 ≠ 真实想法，且是调研时间点的快照，捕捉不了突变与直觉。
- 自己蒸馏还原的是**被蒸馏时的那个你**，人会变，snapshot 有时效性。
- 所有产物质量 = **原材料质量**。喂错数据直接降级。
- 仓颉只处理**系统性表达过的内容**，对没沉淀材料的人/事无效。

## 许可证与归属

MIT License。本 Skill 整合自以下开源项目（均 MIT），方法论文档与思路归属原作者，
使用时请保留署名：

- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)（同事 / Distilly，双层架构开创者）
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)（女娲，公开人物心智模型）
- [notdog1998/yourself-skill](https://github.com/notdog1998/yourself-skill)（自己，数字分身）
- [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)（仓颉，知识精馏 RIA-TV++）

© cuohuatang · 正流 Zhengliu
