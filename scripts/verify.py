#!/usr/bin/env python3
# cht-zhengliu-skill · verify.py
# 结构自检：检查一个蒸馏 Skill 目录是否达标。用法：
#   python3 verify.py <skill_dir> [--mode colleague|nuwa|yourself|cangjie]
# 返回 0 表示通过，1 表示有缺失，2 表示用法错误。
#
# 说明：未指定 --mode 时只做基础校验（frontmatter + 诚实边界），避免对编排器
# 自身（会提及各类术语）误报。指定模式后按该模式做针对性结构校验。
import argparse
import os
import re

REQUIRED_FRONTMATTER = ["name", "description"]
PERSON_MODES = {"colleague", "nuwa", "yourself"}
PERSON_SLOTS = ["硬规则", "身份", "表达", "决策", "人际"]
CONTENT_DIMS = ["R 原始证据", "I 重构解释", "A1", "A2", "E 可执行步骤", "B 已知局限"]


def basic_check(text, problems):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        problems.append("缺少 YAML frontmatter")
        return
    fm = m.group(1)
    for field in REQUIRED_FRONTMATTER:
        if not re.search(rf"^{field}\s*:", fm, re.M):
            problems.append(f"frontmatter 缺少字段：{field}")
    if not re.search(r"诚实边界|已知局限|做不到什么", text):
        problems.append("缺少诚实边界/已知局限声明")


def main():
    p = argparse.ArgumentParser(description="蒸馏 Skill 结构自检")
    p.add_argument("dir", help="Skill 目录")
    p.add_argument("--mode", choices=sorted(PERSON_MODES) + ["cangjie"], default=None)
    args = p.parse_args()

    skill_md = os.path.join(args.dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        print(f"❌ 缺少 SKILL.md：{skill_md}")
        return 1
    text = open(skill_md, encoding="utf-8").read()

    problems = []
    basic_check(text, problems)

    if args.mode in PERSON_MODES:
        missing = [s for s in PERSON_SLOTS if s not in text]
        if missing:
            problems.append("人格层缺失槽位：" + "、".join(missing))
    elif args.mode == "cangjie":
        missing = [d for d in CONTENT_DIMS if d not in text]
        if missing:
            problems.append("能力卡缺失维度：" + "、".join(missing))

    if problems:
        print(f"❌ {args.dir} 自检未通过：")
        for pr in problems:
            print(f"   - {pr}")
        return 1
    print(f"✅ {args.dir} 结构自检通过（mode={args.mode or 'basic'}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
