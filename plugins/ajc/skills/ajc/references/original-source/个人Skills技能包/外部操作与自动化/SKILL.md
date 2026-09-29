---
name: external-actions-and-automation
description: Use when a task may send messages, modify cloud data, publish, share, delete, schedule, monitor, create a recurring automation, install a plugin, or otherwise change state outside the current analysis.
---

# External Actions and Automation

## Core Principle

把准备阶段和变更阶段分开。先读取、起草、预览、验证目标和副作用；只有用户对该具体外部效果拥有明确授权且对象无歧义时才执行。

## Action Classes

| 类型 | 默认处理 |
|---|---|
| Read | 可在范围内查看并引用 |
| Draft/Preview | 可生成内容或 payload，不发送、不发布 |
| Reversible write | 执行前确认目标、范围、权限和结果 |
| Irreversible/delete | 精确确认对象，优先可恢复替代方案 |
| Send/publish/share | 确认收件人、可见范围、内容、时间和通知 |
| Schedule/monitor | 确认时区、频率、停止条件和通知策略 |
| Plugin install | 仅在用户明确要求且路由规则满足时建议/安装 |

## Preflight

确认账号、工作区、项目、文件、记录集合、目标对象、收件人、频道、公开范围、版本、时间、时区、通知策略、重试行为、幂等键和撤销方式。先查找同名或同目的已有任务，避免重复创建。

## Tool Result Handling

工具返回“调用成功”只证明请求被接受，不证明业务效果完成。需要核对返回状态、对象标识、实际可见结果、权限结果、通知结果和重复风险。结果不确定时暂停，不盲目重试。

## Automation Rules

- 优先更新已有自动化，不重复创建。
- 心跳监控在状态未变化时保持安静，只在有意义变化、完成、失败或需要用户行动时通知。
- 保留用户的通知偏好；“不要通知”不应被擅自扩展为“隐藏失败”。
- 保存停止条件、下一次运行时间和修改/删除方式。

## Stop Conditions

目标不明确、授权缺失、权限异常、内容超范围、不可逆目标未确认、工具结果不确定、重试可能产生重复副作用、或凭据/隐私出现风险时停止。

## Closeout

报告实际执行的动作、目标、状态、标识/链接、通知和可见范围、未确认事项以及回滚/停止路径。
