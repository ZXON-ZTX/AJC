# 自动路由的学习来源

调研日期：2026-10-07。以下是设计依据；没有复制第三方技能正文，也没有把这些项目变成 AJC 的运行依赖。

| 来源 | 查阅内容 | 在 AJC 中的应用 |
|---|---|---|
| [obra/superpowers：using-superpowers](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/using-superpowers/SKILL.md) | 先调用适用技能，再行动；方法与专项技能的顺序；已委派子任务的边界 | 在专业执行前实际加载技能；尊重已批准的原子任务，不重新启动项目流程 |
| [agentskills/agentskills：Adding skills support](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/client-implementation/adding-skills-support.mdx) | 元数据发现、模型判断相关性、文件/工具激活、调用限制过滤、按需读取和去重 | 使用当前技能目录；按动作与产物匹配；仅加载所选技能及必要资源；防递归和重复 |
| [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills) | 显式/隐式调用、清单预算与截断、技能文件位置、调用策略 | 改进 AJC 描述并保持隐式调用启用；清单不足时通过宿主支持的发现方式补查候选 |

AJC 的适配选择：根据实际任务判断技能相关性，不沿用 Superpowers 的低概率即强制调用规则；自动选择依赖宿主能力，不使用启动钩子修改用户全局配置。不同宿主的同名解析与发现位置可能不同，以当前环境为准。

`openai/skills` 的 README 在此次调研时已提示仓库弃用并指向 [openai/plugins](https://github.com/openai/plugins)。因此不把旧仓库里的示例名单当成最新或已安装技能清单。
