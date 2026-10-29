#!/usr/bin/env python3
# cht-zhengliu-skill · scaffold.py
# 一键生成蒸馏 Skill 骨架。用法：
#   python3 scaffold.py --slug karpathy --name "Karpathy" --mode nuwa --out ./skills
# 生成 <out>/<slug>-skill/SKILL.md（基于 references/templates/skill-template.md 的简化版）。
import argparse
import datetime
import os

TEMPLATE = """\
---
name: {slug}-skill
description: {desc}
---

# {name} · {mode} Skill

> 由 cht-zhengliu-skill（正流）蒸馏生成 · 模式：{mode} · 生成于 {date}

## 来源与边界（诚实边界，必填）
- 数据来源：
- 蒸馏时间快照：{date}
- 做不到什么：

## Persona / 人格层
- 硬规则（Hard rules）：
- 身份（Identity）：
- 表达（Expression）：
- 决策（Decisions）：
- 人际（Interpersonal）：
- 纠正（Correction）：

## 能力层 / 心智模型
<!-- 按模式选填：nuwa 心智模型 / colleague Work Skill / yourself Self Memory / cangjie 能力卡 -->

## 使用方式
> 用 {name} 的视角帮我分析：<问题>
"""

MODE_DESC = {
    "colleague": "身边人的工作能力与人格（Work Skill + Persona）",
    "nuwa": "公开人物的心智模型与决策启发式",
    "yourself": "你自己的数字分身（Self Memory + 人格）",
    "cangjie": "书/视频/播客的方法论能力包",
}


def main():
    p = argparse.ArgumentParser(description="生成蒸馏 Skill 骨架")
    p.add_argument("--slug", required=True, help="技能 slug，如 karpathy")
    p.add_argument("--name", required=True, help="对象名，如 Karpathy")
    p.add_argument("--mode", required=True, choices=list(MODE_DESC))
    p.add_argument("--out", default=".", help="输出目录")
    p.add_argument("--desc", default=None, help="自定义 description")
    args = p.parse_args()

    desc = args.desc or (
        f"蒸馏 {args.name} 的{MODE_DESC[args.mode]}，可由 Agent 在相关场景调用"
    )
    date = datetime.date.today().isoformat()
    content = TEMPLATE.format(
        slug=args.slug, name=args.name, mode=args.mode, desc=desc, date=date
    )

    target = os.path.join(args.out, f"{args.slug}-skill")
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "SKILL.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 已生成 {path}")


if __name__ == "__main__":
    main()
