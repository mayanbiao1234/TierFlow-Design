<div align="center">

<a href="https://mayanbiao1234.github.io/gzh-design/"><img src="docs/assets/cover.svg" alt="gzh-design · 让好内容，有好排版。7 套主题，给 AI Agent 的公众号排版技能。" width="100%"></a>

**公众号排版技能 · 清枢定制增强版**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-254d3e?style=flat-square)](LICENSE)
[![Themes: 7](https://img.shields.io/badge/主题-7_套_＋_生成器-7b8b5c?style=flat-square)](references/theme-index.md)
[![Checks](https://github.com/mayanbiao1234/gzh-design/actions/workflows/check.yml/badge.svg)](https://github.com/mayanbiao1234/gzh-design/actions/workflows/check.yml)

[**在线体验 ↗**](https://mayanbiao1234.github.io/gzh-design/) · [主题展厅](https://mayanbiao1234.github.io/gzh-design/#themes) · [快速开始](#快速开始) · [English](README.en.md)

</div>

把 Markdown 交给 AI Agent，按主题组件库生成适合微信公众号的 HTML：自动组织章节、标记关键词、处理引用与代码块，再通过脚本检查平台限制，输出带「复制到公众号」按钮的预览页。

> 本项目基于 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)（甲木 × 摸鱼小李）定制，保留上游历史与署名，沿用 **AGPL-3.0**。本版新增内容见[变更记录](CHANGELOG.md)。

## 快速开始

准备好支持 Skills 的 AI Agent、Node.js（用于安装器）和 Python 3（用于校验脚本），在终端运行：

```bash
npx skills add mayanbiao1234/gzh-design
```

按安装器提示选择你的 Agent。安装完成后，把文章交给它：

```text
用摸鱼绿把 article.md 排成公众号 HTML，完成校验后生成带复制按钮的预览页。
```

也可以让 Agent 安装：

```text
请从 https://github.com/mayanbiao1234/gzh-design 安装 gzh-design 技能。
```

**手动安装**：克隆本仓库，将完整目录放入目标 Agent 支持的技能目录；入口是根目录的 `SKILL.md`，请保留 `references/`、`scripts/` 与 `assets/` 的相对位置。

```bash
git clone https://github.com/mayanbiao1234/gzh-design.git
```

它是一套由 Agent 执行的工作流与组件库，**不是独立的 Markdown 编译器或在线编辑器**。网站用于预览；文章排版在你的 Agent 中完成。

## 七套主题，七种阅读气质

| 主题 | 气质 | 适合内容 | 预览 |
|---|---|---|---|
| **摸鱼绿** · 默认 | 翡翠绿、丰富卡片、清晰层次 | 教程、清单、工具盘点 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=moyu-green#themes) |
| **红白色系** | 红色点睛、经典编辑风 | 观点、深度分析 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=red-white#themes) |
| **石墨极简** | 灰阶、留白、理性克制 | 科技评论、专业观点 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=graphite-minimal#themes) |
| **留白禅意** | 墨绿、大留白、舒展节奏 | 生活、深度随笔 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=zen-whitespace#themes) |
| **摸鱼票据** | 票据元素、编号、趣味卡片 | 工具对比、创意评测 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=moyu-ticket#themes) |
| **橄榄手记** | 墨黑与橙、编辑部内刊感 | 评测、案例复盘 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=olive-journal#themes) |
| **极简优雅白** · 本版新增 | 衬线标题、香槟金、三线表 | 深度分析、数据复盘 | [打开 ↗](https://mayanbiao1234.github.io/gzh-design/?theme=elegant-white#themes) |

每套主题都包含设计变量、组件 HTML 与文章类型配方。主题的完整定义以 [`references/theme-index.md`](references/theme-index.md) 为准。

想要自己的风格？可以说：

> 按「黑白杂志、克莱因蓝点睛、衬线标题」的气质，为公众号生成一套新主题并保存复用。

## 从文章到公众号

1. **提供文章**：Markdown 可直接处理；Word、PDF、纯文本先按[格式归一化规则](references/format-normalize.md)提取和确认结构，具体提取能力取决于 Agent 工具。
2. **选主题、装配组件**：使用所选主题与通用组件库，处理章节、关键词、引用、图片、代码块和作者署名。
3. **检查 HTML**：运行 `validate_gzh_html.py`；对直引号问题使用 `fix_quotes.py`，修复后重新校验。
4. **复制发布**：打开生成的预览页 →「复制到公众号」→ 粘贴进公众号编辑器 → 检查图片、字体、表格等最终效果。

主题组件使用内联样式，并尽量避开微信会过滤的写法。校验覆盖已知规则，微信编辑器仍可能调整样式，发布前请预览。

## 本版增加了什么

| 增强 | 具体内容 |
|---|---|
| 第七套主题 | [极简优雅白](references/theme-elegant-white.md)：墨黑与香槟金，衬线标题、三线表和克制的洞察框 |
| 安全修复引号 | [fix_quotes.py](scripts/fix_quotes.py)：处理文本节点内的成对引号，内置内容保留和控制字符检查 |
| 摸鱼绿默认装配 | [主题文档](references/theme-moyu-green.md)：无框居中封面、无目录、正文零侧边距 |
| 交付纪律 | [SKILL.md](SKILL.md)：文本变换写入脚本、变换后检查内容保留、抽读实际句子 |
| 开源展示页 | 响应式首页、七套主题切换、手机／宽屏预览、安装命令与提示词复制 |

展厅中的原有六套示例保留上游文章和版式；新生成的文章以当前主题配方为准。

## 本地查看与验证

网站是纯 HTML / CSS / JavaScript，无需构建或安装前端依赖：

```bash
python -m http.server 4173 --directory docs
```

打开 `http://localhost:4173`，也可直接用浏览器打开 `docs/index.html`。剪贴板不可用时，复制按钮会选中文本供手动复制。

```bash
python scripts/component_lint.py .
python scripts/check_project.py
python scripts/validate_gzh_html.py your-article.html
python scripts/wrap_preview.py your-article.html
```

组件库检查要求 **0 ERROR**；部分上游虚线边框组件会触发提示，需结合用途审查。生成文章还需单独检查标点与内容完整性。

## 项目结构

```text
gzh-design/
├── SKILL.md                # Agent 的工作流入口
├── references/             # 七套主题、通用组件、生成器与格式规则
├── scripts/                # HTML 校验、组件检查、引号修复、预览包装
├── assets/                 # 演示文章与预览模板
├── docs/                   # 项目网站和主题展厅
├── archive/                # 上游早期主题与历史画廊
└── .github/                # 自动校验与 Issue / PR 模板
```

## 参与贡献

欢迎新增主题、改进微信兼容性和文档。请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，附上可复现的文章片段与预览效果；请勿提交真实账号凭据、未公开稿件或个人信息。

部署说明见 [docs/deployment.md](docs/deployment.md)。通用改进也欢迎回馈[上游项目](https://github.com/isjiamu/gzh-design-skill)。

## 致谢与许可证

原始项目与组件设计：**甲木 × 摸鱼小李**。清枢定制增强版继续使用 **GNU AGPL-3.0**；保留原有版权声明与提交历史。详细条款以 [LICENSE](LICENSE) 为准，来源与改动说明见 [NOTICE](NOTICE)。
