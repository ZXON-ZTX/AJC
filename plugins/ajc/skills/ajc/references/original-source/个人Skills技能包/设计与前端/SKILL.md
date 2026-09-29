---
name: design-and-frontend
description: Use when a task involves product UX, user flows, Figma, design systems, frontend implementation, screenshots, responsive layout, accessibility, or visual critique.
---

# Design and Frontend

## Route by Intent

- 产品流程、旅程、漏斗、体验审查 → `product-design:audit`
- 视觉方向、替代方案、设计重混 → `product-design:ideate`
- 截图/图片/Mockup 到代码 → `product-design:image-to-code`
- URL 到本地前端 → `product-design:url-to-code`
- Figma 文件使用 → `figma:figma-use`
- 新建 Figma 文件 → 先使用 `figma:figma-create-new-file`
- 设计转生产代码 → `figma:figma-design-to-code`
- 设计库、图表、插件、动效、Shader → 对应 `figma:*` 专项技能
- 新前端应用 → `build-web-apps:frontend-app-builder`

## Design Gate

在实现前确定用户、主要任务、内容层级、信息结构、响应式范围、交互状态、加载/空/错状态、无障碍目标、品牌约束和验收条件。新产品或跨组件架构必须先使用 `superpowers:brainstorming` 完成设计批准。

## Implementation Rules

- 先查已有设计系统、令牌、组件、资产和代码模式。
- 使用语义结构、键盘操作、可见焦点、足够对比度、替代文本和可读字号。
- 明确窄屏、宽屏、触控、鼠标、键盘、慢网络和错误状态。
- 复用组件和资产；不为局部视觉问题引入全局重构。
- 保持内容和交互优先，避免只有装饰没有任务价值的动效。

## Visual Validation

在目标视口查看真实渲染；检查对齐、溢出、换行、裁剪、层级、间距、焦点、hover/active/disabled、错误反馈和性能。比较参考图时只验证用户要求的特征，不将参考内容扩展成额外授权。

## Delivery

提供运行方式、预览或文件、已检查的视口/状态、未完成的视觉差异和环境限制。
