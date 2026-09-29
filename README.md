# AJC

AJC 是一个面向 Codex 的个人工作流 Skill。它帮助 Codex 在复杂任务中明确范围、控制改动、选择合适的领域流程，并用与风险匹配的证据验证结果。

## 安装

将这个 GitHub 仓库添加为 Codex Plugin Marketplace：

```powershell
codex plugin marketplace add ZXON-ZTX/AJC
```

然后在 Codex 或 ChatGPT 桌面端的 Plugins 页面选择 **AJC Marketplace**，安装 **AJC**。仓库 Marketplace 的可用性可能因客户端而异。

## 使用

安装后可直接调用：

```text
使用 $ajc 完成这个任务，并明确范围、最小改动和验证证据。
```

AJC 会按需路由到以下工作流：

- 需求、假设、范围与最小改动
- 代码、研究、数据、文档、设计和媒体任务
- 插件、外部操作、自动化与协作
- 验证、状态表达和中文交付

简单问题不会被强制套入复杂流程。

## 仓库结构

```text
.agents/plugins/marketplace.json
plugins/ajc/
├── .codex-plugin/plugin.json
└── skills/ajc/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
```

## 官方参考

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Skills](https://developers.openai.com/plugins/concepts/skills)
