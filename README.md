> 🤝 **本仓库是 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)（甲木 × [摸鱼小李](https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ) 联名，AGPL-3.0）的定制增强版** —— 上游的核心组件库与质量标准完整保留；本版在其基础上新增第 7 套主题、引号安全修复脚本与实测打磨的定版装配规则，并遵循 AGPL-3.0 同协议开源。感谢上游两位作者的出色工作。

<div align="center">

# gzh-design · 公众号排版技能（定制增强版）

**把 Markdown 一键排成可直接粘贴进微信公众号编辑器的精致 HTML**

7 套精选主题 + 主题生成器 · 代码块/图片/GIF · 自动章节编号与关键词标记 · 双关卡校验 + 引号安全修复

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![upstream](https://img.shields.io/badge/upstream-isjiamu%2Fgzh--design--skill-8b5cf6.svg)](https://github.com/isjiamu/gzh-design-skill)
[![Themes](https://img.shields.io/badge/themes-7%20+%20generator-059669)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

一个给 AI Agent（Claude Code / Codex / Cursor 等）用的公众号排版 Skill。你写完 Markdown，它按你选的主题，生成**样式全内联、粘贴到公众号编辑器不掉格式**的 HTML——自动编章节号、标关键词下划线、配引言卡与目录、处理代码块和图片、合并作者签名，并用脚本确定性地兜住公众号平台的各种限制。

## 🆕 相比上游的定制增量

| 增量 | 说明 | 位置 |
|---|---|---|
| **第 7 套主题：极简优雅白** | 基金答辩风：纯白底 + 墨黑 `#1A1A1A` + 香槟金 `#B08D4C` 点缀，衬线大标题、booktabs 三线表、深色洞察框（全篇 ≤3 处），适合深度分析、AI 新闻解读、政策解读、数据复盘 | `references/theme-elegant-white.md` |
| **引号安全修复脚本** | `fix_quotes.py`：只转换文本节点内的成对直引号、跳过代码块，**自带内容保留校验**（剔除引号后的纯文本与处理前逐字一致）与控制字符扫描，杜绝静默吞字 | `scripts/fix_quotes.py` |
| **摸鱼绿定版装配** | 无框居中封面 + 无目录 + 内容区零侧边距的「定版」规则（含微信编辑器会自动"纠正"混字号 `<p>` 的规避写法），长文深度分析实测打磨 | `references/theme-moyu-green.md` 顶部 ⭐ |
| **交付物变换三条铁律** | 一起真实排版事故（内联 `python -c` 正则替换导致 `\1` 降级为八进制转义、31 处引号词组被静默吞掉）沉淀出的工程纪律：变换写成 `.py` 文件、变换后必须校验内容保留、抽查要读实际句子 | `SKILL.md` Gotchas 首条 |

## ✨ 核心特性

- **7 套精选主题**：摸鱼绿（默认）· 红白 · 石墨极简 · 留白禅意 · 摸鱼票据 · 橄榄手记 · 极简优雅白（本版新增）—— 每套都是自成体系的厚组件库（设计变量 + 数十个精细组件 + 视觉层级表 + 文章类型配方表）。
- **主题生成器**：不满足现成主题？用一句话描述或一张参考图，生成一套全新组件库并保存本地复用（见 `references/theme-generator.md`）。
- **内容全兼容**：代码块（深/浅色，等宽不折行）、图片、GIF（带动图角标）、行内代码、引用、列表、产品徽章。
- **智能排版**：章节自动编号（末章 ∞ / ///）、每段主动标 1–3 个关键词下划线、从正文提炼引言卡与目录、作者签名去重合并。
- **中文全角标点**：正文自动规范全角，代码块内原样保留；直引号问题用 `fix_quotes.py` 安全修复。
- **不掉格式**：所有样式内联、文字 `<span leaf="">` 包裹，规避 `<style>/<div>/class/grid/position` 等公众号会过滤的写法。
- **双关卡质量校验**：`component_lint.py`（组件库源头）+ `validate_gzh_html.py`（最终产物），构成可复现的「改→验→修」闭环。
- **一键复制**：生成带「复制」按钮的预览页，点一下把富文本复制到剪贴板，直接粘进公众号，免手动全选。

## 🎨 7 套精选主题

| 主题 | 主色 | 适合 |
|---|---|---|
| **摸鱼绿**（默认） | `#059669` emerald | 教程、测评、清单、工具盘点、AI 新闻深度分析（卡片丰富、信息密度高） |
| **红白色系** | `#DC2626` 正红 | 深度分析、观点、力量感话题（经典编辑风） |
| **石墨极简风** | `#52525B` 石墨灰 | 设计、科技评论、专业观点、高端品牌 |
| **留白禅意风** | `#4A5D52` 墨绿 | 禅意、极简生活、深度随笔（呼吸感最强） |
| **摸鱼票据风** | `#059669` emerald | 工具对比、创意评测（票据视觉隐喻） |
| **橄榄手记** | `#1e1f23` 墨黑 + 橙 `#ed7b2f` | 内刊手记、深度评测、案例复盘（编辑部内刊质感） |
| **极简优雅白**（新增） | `#B08D4C` 香槟金 + 墨黑 `#1A1A1A` | 深度分析、AI 新闻解读、政策解读、数据复盘（基金答辩风） |

> 每套主题的英文标识、组件库文件、下划线 CSS 见 [`references/theme-index.md`](references/theme-index.md)。效果预览图与完整长图见上游 [docs/all-themes.md](docs/all-themes.md)；克隆后浏览器打开 `docs/gallery/index.html` 可看可交互的完整 HTML。

## 🚀 快速开始

### 方式一：一行安装

```bash
npx skills add https://github.com/<你的GitHub用户名>/<仓库名>
```

> 部署后请把本文件及 docs/index.html 中所有 `<你的GitHub用户名>/<仓库名>` 占位符替换为实际仓库地址（共 3 处：此处、下方方式三、分享页安装区块）。

### 方式二：让 AI 自己装

对**任意 Agent**（Claude Code / Codex / Cursor 等）说一句：

> 请帮我查找并自动安装 https://github.com/<你的GitHub用户名>/<仓库名> 这个 skill

### 方式三：手动 clone

```bash
git clone https://github.com/<你的GitHub用户名>/<仓库名>.git ~/.claude/skills/gzh-design
```

装好后，直接对 Agent 说：

> 用摸鱼绿把这篇文章排成公众号 HTML：`article.md`

## 📖 使用流程

1. **选主题** — 按题材自动推荐最契合的主题并请你一步确认（默认摸鱼绿）；也可直接指定，或让 AI 生成新主题。
2. **读组件库** — 读所选主题库 + 通用增量库（代码块/图片/小标签）。
3. **解析 Markdown** — 识别标题、章节、加粗、高亮、引用、图片、代码块、列表。
4. **装配 HTML** — 用组件库里的真实组件拼装，落实编号、下划线、全角、签名。
5. **校验** — 跑 `validate_gzh_html.py`，ERROR 清零才交付；直引号问题用 `fix_quotes.py` 安全修复。
6. **输出** — 生成干净正文 + 带「复制」按钮的预览页；浏览器打开预览页点右上角「复制到公众号」，再去编辑器粘贴即可。

## 🗂 常见使用场景

| 你的内容 | 推荐怎么排 |
|---|---|
| AI 新闻 / 深度长文 | 摸鱼绿（定版装配）或 极简优雅白 |
| 产品测评 / 工具盘点 | 摸鱼绿 或 摸鱼票据；step/tool-label + 卡片，按配方表走 |
| 教程 / 操作指南 | 摸鱼绿；step-label + 代码块 + 编号列表 |
| 数据复盘 / 年度报告 | 摸鱼绿 或 橄榄手记；数据卡 + 表格 |
| 禅意 / 极简随笔 | 留白禅意；大留白 + 居中衬线引用 |
| Word / PDF 稿转公众号 | 先自动格式归一化 → 再按题材选主题 |
| 想要现成之外的风格 | 主题生成器：一句话或参考图现造一套 |

## 🧩 公众号平台限制（已内置兜底）

生成的 HTML 严格遵守：禁 `<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`、`display:grid`、CSS 变量、外部字体；样式全部内联；所有文字用 `<span leaf="">` 包裹。这些由校验脚本确定性检查，而非靠模型自觉。

## 🔁 可验证循环

改组件库或工作流后，用双关卡闭环防回归：

```bash
python3 scripts/component_lint.py .            # 源头关：扫组件库反模式
python3 scripts/validate_gzh_html.py out.html  # 产物关：扫最终 HTML 合规
python3 scripts/fix_quotes.py out.html         # 引号修复：只动成对直引号，自带内容保留校验
```

- **源头关** 查 `white-space:pre`（大空白）、正文四周虚线框、平台禁用项 —— 须 0 ERROR。
- **产物关** 查禁用标签、`<span leaf>` 包裹、半角标点 —— 须 0 ERROR / 半角 0 WARN。
- 逻辑：源头干净 → 产物必然干净。详见 `references/eval-cases.md`。

## 📁 目录结构

```
gzh-design/
├── SKILL.md                    # 排版工作流主文档（Agent 入口）
├── references/
│   ├── theme-index.md          # 7 套主题索引（主色/适用/下划线，单一来源）
│   ├── theme-*.md              # 7 套主题组件库（theme-moyu-green.md 等）
│   ├── theme-generator.md      # 主题生成器（按描述/参考图生成新主题）
│   ├── common-components.md    # 跨主题通用增量组件（代码块/图片/小标签）
│   ├── format-normalize.md     # 格式归一化（docx/pdf/纯文本 → Markdown）
│   └── eval-cases.md           # 触发用例 + 可验证循环
├── scripts/
│   ├── validate_gzh_html.py    # 产物合规校验
│   ├── component_lint.py       # 组件库源头检查
│   └── fix_quotes.py           # 直引号安全修复（本版新增）
├── assets/
│   ├── sample-article.md       # 演示输入
│   └── theme-previews/         # 主题生成器产出的区块库预览
└── docs/                       # Pages 分享页 + 主题画廊
```

## ❓ FAQ

**Q：粘贴到公众号后样式会掉吗？**
A：不会。所有样式内联、文字 `<span leaf="">` 包裹，这正是校验脚本强制的重点。

**Q：能自己加主题吗？**
A：两种方式。① **让 AI 生成**：说「按这个风格 / 这张图生成一套公众号主题」，它会走 `references/theme-generator.md` 的流程生成组件库、登记并复用。② **手写贡献**：照 `CONTRIBUTING.md` 的「新增一套主题风格」，跑通可验证循环即可提 PR。

**Q：只能在 Claude Code 用吗？**
A：不限。任何能读取 Skill 目录的 Agent（Codex / Cursor 等）都能用，工作流在 `SKILL.md`。

**Q：对模型有要求吗？国产模型行不行？**
A：不挑模型。排版逻辑全部沉淀在组件库和校验脚本里，模型只负责按规则填充内容，硬约束由脚本确定性兜底，换模型不走样。

**Q：fix_quotes.py 和直接全局替换有什么区别？**
A：三个本质区别：只处理文本节点（标签属性永不动）、只转换成对引号（落单的报出来人工处理）、转换后做**内容保留校验**——剔除引号后的纯文本必须与处理前逐字一致，任何静默吞字都会被拦下。

## 🧠 方法论：不止 7 套，自己造主题

内置主题不够用时不必等更新——让 AI 现造一套：

> 按「黑白杂志、克莱因蓝点睛、衬线字体」的气质，给公众号排版生成一套新主题

流程：收集偏好（一次问全）→ 生成 45~75 个区块的预览库 → 你确认风格后转标准主题库并登记 → 跑 `component_lint.py` 到 0 ERROR → 与内置主题同权使用。详见 [`references/theme-generator.md`](references/theme-generator.md)。

## 🤝 贡献与上游

- 本定制版欢迎 Issue 与 PR（新主题、修复、文档改进），请先读 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 通用性增量（如新主题、校验规则）建议同步回馈上游 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill)，让主线一起变好。
- 上游官方交流群与作者联系方式见上游 README。

## 📄 License

**AGPL-3.0 © 2026 甲木 × 摸鱼小李（上游）· 本仓库修改部分同样以 AGPL-3.0 开源**

本项目（含上游代码与所有修改）采用 **GNU AGPL-3.0** 协议：必须保留署名；衍生品、Fork、二次分发必须以 AGPL-3.0 公开源代码；把修改版本部署成网络服务同样需要公开源代码；不允许闭源或专有化。完整条款见 [LICENSE](LICENSE)。

---

<div align="center">

**gzh-design 定制增强版** · 基于上游 AGPL-3.0 衍生 · [在线画廊](docs/index.html)

</div>
