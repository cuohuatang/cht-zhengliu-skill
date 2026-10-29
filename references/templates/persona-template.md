# Persona 结构模板（人物类五~六层）

> 正流统一用下面 6 槽位表达人格层。nuwa 的"五层心智模型"、yourself 的"5 层人格结构"
> 都可映射到这里。生成蒸馏 Skill 时按需填充，空槽位标注"暂无数据"，不要编造。

```
Persona:
  hard_rules:        # 硬规则：绝对不做的底线
    - <规则 1>
    - <规则 2>
  identity:          # 身份：我是谁、角色定位
    - <身份描述>
  expression:        # 表达：语气、节奏、用词偏好（表达 DNA）
    tone: <语气>
    rhythm: <节奏>
    vocab: <用词偏好>
  decisions:         # 决策：怎么判断、决策启发式
    heuristics:
      - <启发式 + 触发场景>
  interpersonal:     # 人际：怎么与人互动
    - <互动模式>
  correction:        # 纠正：对话纠偏层（持续追加）
    - <YYYY-MM-DD 用户纠正：...>
```

## 映射说明

| 正流槽位 | nuwa 对应 | yourself 对应 |
| --- | --- | --- |
| hard_rules | 什么不做 / 反模式 | 硬规则 |
| identity | 身份 | 身份 |
| expression | 怎么说话（表达 DNA） | 说话风格 |
| decisions | 怎么想 + 怎么判断（心智模型/启发式） | （并入记忆与风格） |
| interpersonal | （隐含于表达） | 人际行为 |
| correction | （隐含于诚实边界） | 情感模式 + 纠正层 |

> 情感模式（yourself）可并入 interpersonal 或单独成段；诚实边界并入 hard_rules / 已知局限。
