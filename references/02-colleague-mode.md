# 02 · 同事模式（colleague-skill / Distilly）

上游：[titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)（已演进为 Distilly 多家族框架）。
**定位**：把身边人（同事 / 关系 / 名人 / 自己）蒸馏成可复用 Person Profile。

## 核心特点

- **双层架构开创者**：Work Skill（能力层）+ Persona（人格层）。
- **多家族**：colleague（同事）/ relationship（关系）/ celebrity（名人）/ owner（自己）。
- **文化标签**：内置字节范 / 阿里味等组织文化标签，便于团队知识沉淀。
- **跨平台数据接入**：飞书（Lark，API 全自动）、钉钉（DingTalk，浏览器半自动）、
  Slack（API 需管理员装 Bot）、微信（SQLite 导出）、邮件（.eml/.mbox）、PDF/截图/Markdown。
- **演化成熟**：追加文件增量合并、对话纠正、版本归档回滚。
- **跨宿主**：8+ runtime（Claude Code / Codex / Cursor / OpenClaw / Hermes / DeepSeek Harness / Gemini CLI / OpenCode）。

## 工作流

```
源材料（飞书/钉钉/Slack/微信/邮件/文档） + 你的描述
   → 选择家族（colleague / relationship / celebrity / owner）
   → Distilly 生成 Person Profile（Persona + 家族特定模块）
   → 安装到任意支持的宿主
```

## 产物结构（colleague 家族示例）

- **Work Skill**：技术能力、代码习惯、Review 风格、工作流。
- **Persona（6 层）**：hard rules → identity → expression → decisions → interpersonal → Correction。
- 命名约定：`{character}-{slug}`（如 `celebrity-karpathy`）。

## 局限与注意

- 钉钉 API 不支持消息历史；Slack 免费版限 90 天且需管理员；微信需先导出。
- 作者明确标注"仍是 demo 版本"，名人/关系家族方法论文档仍为 planned。
- 质量高度依赖原材料；喂错数据降级。
- Grok 等部分 Bot 不支持直接本地 SKILL.md 导入，需手动迁移。

## 什么时候选它而不是女娲/自己

- 你有**可追溯的私人协作数据**（飞书/钉钉/邮件）→ 选 colleague。
- 你只有对象的**公开材料**、且对象是名人/思想家 → 选 nuwa。
- 对象就是**你自己** → 选 yourself（解析器更专精私聊/日记/照片）。
