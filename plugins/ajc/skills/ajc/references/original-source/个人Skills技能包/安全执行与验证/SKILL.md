---
name: safe-execution-and-verification
description: Use when a task is being implemented, changed, delivered, published, fixed, or called complete and the result needs proportional evidence and honest status.
---

# Safe Execution and Verification

## Core Principle

“完成”必须由与风险匹配的证据证明。执行、验证、交付是三个不同状态，不能用“已经调用工具”代替“结果已经成立”。

## Verification Ladder

| 风险/产物 | 最低验证 |
|---|---|
| 只读答案 | 依据、来源、不确定性 |
| 文本或配置 | 语法/解析、关键字段、目标内容 |
| 代码行为 | 失败测试先行、目标测试、项目级测试 |
| 数据结论 | 来源、质量、定义、计算、样本和图表审计 |
| 文档/幻灯片/PDF | 实际打开或渲染、布局、内容、兼容性 |
| 媒体 | 最终尺寸/格式、可读性、伪影、时序和播放 |
| 外部变更 | 目标、返回状态、对象标识、实际可见效果 |

## Execution Loop

1. 将成功标准改写成可检查的断言。
2. 运行最小的针对性检查。
3. 根据影响范围运行更广检查。
4. 检查是否引入未使用引用、错误链接、敏感信息或范围外变更。
5. 以使用者视角查看最终产物。
6. 记录通过、失败、跳过和无法执行的检查。

## Status Vocabulary

- 已验证：相关证据已经产生且通过。
- 已实现：改动存在，但验证仍不完整。
- 未验证：缺少环境、服务、凭据、依赖或测试条件。
- 有条件完成：核心路径通过，但有明确限制。
- 阻塞：安全替代方案耗尽，需要用户或外部状态改变。

## Integrity Rules

不隐藏失败、警告、预先存在的错误或跳过的检查；不把推测写成结果；不因时间压力降低不可逆操作的验证门槛；不在未验证时使用“已修复”“已发布”“完全兼容”等绝对表述。

## Closeout Contract

结果 → 变更文件/外部效果 → 验证证据 → 未验证事项/风险 → 下一步。若生成了本地文件，提供绝对路径；若改变了外部状态，提供安全的标识或链接。
