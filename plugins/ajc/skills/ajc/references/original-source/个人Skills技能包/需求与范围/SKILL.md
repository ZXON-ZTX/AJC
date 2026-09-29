---
name: requirements-and-scope
description: Use when a request is ambiguous, broad, underspecified, contains competing interpretations, or could change the deliverable, authorization, data, recipient, or platform.
---

# Requirements and Scope

## Core Principle

任何会改变结果的未知信息，都必须在行动前显式化。把不确定性分为可继续推进的假设和必须由用户决定的开放选择。

## Requirement Record

维护以下五栏：

| 栏位 | 内容 |
|---|---|
| Outcome | 用户最终要得到什么 |
| Confirmed | 用户明确说过或环境中可验证的事实 |
| Assumed | 为继续推进采用的可逆解释 |
| Open choice | 需要用户选择且会改变结果的内容 |
| Acceptance | 可观察的完成条件 |

## Scope Test

将请求放入以下范围：

- 读：查阅、分析、解释、审查、比较。
- 写：修改本地文件、生成文件、改变代码或配置。
- 外写：发送、发布、分享、创建、删除、调度、购买或改变第三方状态。

若新发现的内容改变数据源、账号、受众、权限、平台、预算、法律风险、不可逆副作用或核心验收标准，任务范围立即升级并暂停越过该边界。

## Clarification Rule

- 低风险、可逆、只影响形式：声明假设后继续。
- 影响核心产物或权限：只问一个最小阻塞问题。
- 存在多个合理解释：列出解释、推荐一个并说明依据。
- 用户已经给出足够约束：复述关键理解，不重复提问。

## Scope Control

记录明确的 non-goals。把“顺便优化”“以后可能有用”“全面支持”视为范围扩张信号。只有在它们是当前成功标准的必要条件时才纳入执行；否则单独列为建议。

## Output Contract

任何复杂任务开始前，内部或对用户形成短版任务契约：目标、边界、假设、待定项、交付物、验证和停止条件。
