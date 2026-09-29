---
name: coordination-and-threads
description: Use when work can be split into independent tasks, needs another Codex task, requires waiting or handoff, or involves consolidating progress from multiple workers.
---

# Coordination and Threads

## Core Principle

只有真正独立且边界清楚的工作才并行；主任务始终负责范围、权限、合并、验证和最终交付。

## Split Test

拆分前确认每个子任务都有独立输入、明确输出、低耦合依赖、可隔离副作用和合并方式。无法做到这些条件时保持单线程，避免并行制造协调成本。

## Dispatch Contract

每个任务提示必须包含：目标、背景、允许读取的资源、允许的写入范围、禁止的外部动作、成功标准、返回格式和遇到阻塞时的报告方式。不要将完整无关历史复制给子任务。

## Codex Task Routes

- 用户明确要求新任务：`mcp__codex_app__create_thread`
- 继续已有任务：`mcp__codex_app__send_message_to_thread`
- 观察一个或多个任务：`mcp__codex_app__wait_threads`
- 读取任务摘要/状态：`mcp__codex_app__read_thread`
- 移动任务和 Git 状态：`mcp__codex_app__handoff_thread`
- 任务标题/置顶/归档：对应 `mcp__codex_app__set_thread_*`
- 打开文件、终端或审查：`mcp__codex_app__open_in_codex`

## Waiting

使用有界等待和返回的 cursor/hostId。一次等待最多覆盖工具支持的任务数；不要重复轮询未变化状态；只在完成、失败、需要输入或计划发生实质变化时更新用户。

## Merge and Review

收集每个任务的结果、证据、未完成项和副作用；按原始成功标准重新验证。冲突结论要保留并解释，不得静默选取。子任务完成不等于主任务完成。

## Safety

任务创建、消息发送、交接、归档和打开界面也要遵守用户意图和权限边界。涉及外部服务或定时动作时组合 `external-actions-and-automation`。
