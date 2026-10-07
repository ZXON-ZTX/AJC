# AJC

AJC 是一个面向 Codex 的个人工作流 Skill。它帮助 Codex 在复杂项目中自动选择并加载合适的 Skill，按阶段协调执行、控制改动，并用与风险匹配的证据验证结果。当前插件版本：**1.2.1**。

仓库内包含完整的原始详细资料：个人 Skills 说明书（00–16）及模块化 Skill。安装 Plugin 后，Codex 可以按任务查阅这些资料；导航见 [原始资料索引](plugins/ajc/skills/ajc/references/原始资料索引.md)。

## 安装

将这个 GitHub 仓库添加为 Codex Plugin Marketplace：

```powershell
codex plugin marketplace add ZXON-ZTX/AJC
```

然后在 Codex 或 ChatGPT 桌面端的 Plugins 页面选择 **AJC Marketplace**，安装 **AJC**。仓库 Marketplace 的可用性可能因客户端而异。

## 使用

安装后可直接调用：

```text
使用 $ajc 完成这个项目，自动选择合适的技能，并给出验证结果。
```

AJC 会按需路由到以下工作流：

- 需求、假设、范围与最小改动
- 代码、研究、数据、文档、设计和媒体任务
- 插件、外部操作、自动化与协作
- 验证、状态表达和中文交付

简单问题不会被强制套入复杂流程。

## 自动选择 Skill

描述你要得到的结果即可，不必逐个指定 Skill。AJC 激活后会：

1. 按交付物和依赖拆分项目阶段。
2. 从当前环境的技能清单，按实际动作、格式和平台匹配主技能及必要的辅助技能。
3. 执行前真正加载所选技能的说明，并简短说明用途。
4. 在进入下一阶段、需求变化或能力不可用时重新选择，保留已完成的成果。
5. 找不到对应技能时检查可行的工具替代；核心能力缺失则说明具体阻塞。

例如：

```text
使用 $ajc 分析这份销售数据，做一个交互式仪表板，再生成汇报 PPT。
使用 $ajc 完成这个 Web 项目，从需求、实现到浏览器验证自动选择技能。
使用 $ajc 制作产品宣传片，并自动选择当前可用的视频和素材技能。
```

实际选择取决于你的已安装技能和工具。数据分析阶段、仪表板阶段和 PPT 阶段会分别匹配；你的自定义技能也可以成为候选。AJC 保持隐式调用启用，宿主可在复杂项目请求匹配其描述时自动选择 AJC；明确写 `$ajc` 是直接调用入口。

AJC 提供协调规则，其他专项技能、连接器和账号仍须在当前环境可用。自动选择不等于自动安装所有插件，也不增加发送、发布或删除权限。完整规则见 [自动技能路由](plugins/ajc/skills/ajc/references/自动技能路由.md)，设计依据见 [GitHub 学习来源](plugins/ajc/skills/ajc/references/技能路由学习来源.md)。

## 仓库结构

```text
.agents/plugins/marketplace.json
plugins/ajc/
├── .codex-plugin/plugin.json
└── skills/ajc/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── 自动技能路由.md       # 动态选择、加载与阶段切换
        ├── 技能路由学习来源.md
        ├── 原始资料索引.md
        └── original-source/  # 完整详细说明书与模块化 Skills
```

## 官方参考

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Skills](https://developers.openai.com/plugins/concepts/skills)
