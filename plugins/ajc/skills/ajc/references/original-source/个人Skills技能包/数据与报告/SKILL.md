---
name: data-and-reporting
description: Use when a task involves structured data, metrics, KPIs, dashboards, statistical analysis, data quality, quantitative visualization, or business reporting.
---

# Data and Reporting

## Core Principle

让每个结论都能从源数据、字段、过滤、转换、公式、聚合和可视化一路追溯；先验证数据和定义，再解释变化。

## Analysis Contract

确定决策问题、受众、数据源、时间窗口、统计粒度、时区、刷新时间、输出格式和允许的推断范围。

## Data Quality Pass

检查来源可信度、模式、类型、单位、主键、重复、缺失、异常、时间边界、连接关系、样本选择、数据新鲜度和访问权限。记录发现的问题、影响范围、处理方式和未解决风险。

## Metric Contract

每个关键指标必须明确：名称、业务含义、分子、分母、过滤条件、排除项、统计人口、粒度、时间基准、窗口、单位、刷新时间、版本和限制。

## Calculation Rules

- 不无依据地平均平均数、比例或不同粒度的值。
- 比较比率前检查分母是否稳定。
- 检查缺失和连接是否改变了统计人口。
- 区分实际值、估计值、预测值和推断分群。
- 区分描述性观察、相关性和因果解释。

## Visualization Rules

图表服务于决策；显示单位、时间范围、筛选条件、样本范围、数据更新时间和指标定义。避免用装饰、双轴、截断坐标或过度聚合制造误导。

## Reporting

报告顺序：结论/决策含义 → 关键指标 → 方法和定义 → 质量与限制 → 图表 → 可复现来源。仪表板要使筛选、刷新和口径可见。

## Specialized Routing

按需要组合 `data-analytics:analyze-data-quality`、`data-analytics:validate-data`、`data-analytics:metric-diagnostics`、`data-analytics:build-dashboard`、`data-analytics:kpi-reporting` 和 `data-analytics:visualize-data`。
