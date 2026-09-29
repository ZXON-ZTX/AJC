---
name: task-orchestration
description: Use when a request spans multiple steps, domains, files, tools, plugins, external services, or unclear execution boundaries and needs a single coordinated plan.
---

# Task Orchestration

## Core Principle

把用户目标转换成“可执行、可验证、权限边界清楚”的最小工作流。先判断结果类型，再选择专业技能；不要因为工具存在就调用工具。

## First Pass

1. 写出最终目标、目标受众和成功标准。
2. 区分：只读回答、本地变更、外部变更。
3. 标记事实、假设、开放选择和风险。
4. 选择一个主领域技能；只加载真正需要的辅助技能。
5. 确定产物、验证方式、停止条件和交付格式。

## Route Table

| 信号 | 必要路由 |
|---|---|
| 多步骤、范围不清、跨领域 | 本技能 → `requirements-and-scope` |
| 代码、Bug、测试、重构、审查 | `code-engineering` |
| 当前事实、指定来源、高风险信息 | `research-and-evidence` |
| 指标、数据、报表、仪表板 | `data-and-reporting` |
| Word、PDF、表格、演示、云端文件 | `documents-and-artifacts` |
| UX、Figma、前端、截图、视觉实现 | `design-and-frontend` |
| 图片、视频、音频、动画、资产处理 | `media-and-assets` |
| 插件、连接器、第三方服务 | `plugin-and-connector-routing` + `external-actions-and-automation` |
| 并行、交接、等待、调度、监控 | `external-actions-and-automation` |
| 中文说明、报告、交付、状态汇报 | `communication-and-output` |

## Control Loop

目标确认 → 范围确认 → 专业执行 → 结果验证 → 风险收尾。

发现隐藏复杂度时升级范围；发现不确定性只影响可逆细节时声明假设后继续；发现不确定性影响权限、核心产物、收件人、数据或删除目标时暂停提问。

## Non-Goals

不替用户做未授权的外部写入；不把建议扩展成需求；不把“全面”理解为添加所有可能功能；不重复执行已经存在的自动化或任务。
