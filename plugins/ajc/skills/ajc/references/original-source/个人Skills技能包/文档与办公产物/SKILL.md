---
name: documents-and-artifacts
description: Use when creating, editing, converting, inspecting, rendering, or delivering Word documents, PDFs, spreadsheets, presentations, images, or connected cloud artifacts.
---

# Documents and Artifacts

## Routing

| 产物 | 路由 |
|---|---|
| Word / `.docx` | `documents:documents` |
| PDF | `pdf:pdf` |
| Excel / 表格 | `spreadsheets:Spreadsheets` |
| PowerPoint / Slides | `presentations:Presentations` |
| Google Drive 生态 | `google-drive:*` |
| 图片或视频 | `media-and-assets` |

本地处理文档、表格、演示文稿或 PDF 前，使用 `mcp__codex_app__load_workspace_dependencies` 加载工作区依赖和可用库。

## Intake

确认源文件、最终格式、受众、内容范围、版式要求、品牌资产、语言、可编辑性、兼容性、保存位置和是否允许覆盖原件。

## Preservation Rule

保留未被要求改变的内容、结构、样式、公式、批注、链接、元数据和权限。只做最小的完整编辑；需要重排时先确认重排范围。

## Validation

- 文档：内容、标题层级、分页、目录、页眉页脚、表格、链接、字体和可访问性。
- PDF：文字、页面尺寸、字体嵌入、图像清晰度、裁剪、溢出和打印效果。
- 表格：公式、引用、格式、合计、筛选、隐藏项、工作表名称、刷新和数据范围。
- 演示：版式、层级、可读性、图表、动画、字体、屏幕比例和讲演顺序。
- 云端：账号、文件、文件夹、版本、权限、分享范围和外部通知。

## External Safety

云端编辑、共享、发布、移动和删除都属于外部变更，必须组合 `external-actions-and-automation`。优先新建版本或导出副本，避免破坏唯一原件。

## Delivery

提供实际文件或安全链接、绝对路径、修改摘要、视觉/语义验证结果和兼容性限制。
