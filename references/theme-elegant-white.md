# 公众号排版组件库 —— 极简优雅白

> **使用说明**：本组件库为「极简优雅白（Elegant White）」主题（基金答辩风公众号版），所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：纯白底 + 墨黑 `#1A1A1A` 主色 + 香槟金 `#B08D4C` 小面积点缀 + 衬线字体（Georgia）大标题 + booktabs 学术表格（上下粗黑线 + 行间浅灰线）+ 大量留白。层级靠字重与留白建立，几乎无底色填充，仅引用块用暖灰 `#fafafa`、核心洞察用深色框（全篇 ≤3 处）。适合深度分析、AI 新闻解读、政策解读、学术向评论、财报/数据复盘类文章。
>
> **来源**：2026-08 由「OpenAI 开源 Codex Harness 深度分析」成稿风格沉淀而来，适合 AI 新闻深度分析类公众号文章；现可作为此类文章的默认主题使用。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id/`<div>`、`position:fixed/absolute/sticky`、`float`、`@media`/`@keyframes`、`display:grid`、CSS 变量 `var(--x)`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`border-radius`、`box-shadow`、`position:relative`、`<section>/<p>/<span>/<strong>/<img>/<table>` 等基础标签
> - 正文强调用衬线标题/金下划线/加粗/booktabs 表格，**不用四周虚线框**（dashed），**不用彩色大底块**（深色洞察框除外且 ≤3 处）
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有文字节点用 `<span leaf="">文字</span>` 包裹；装饰性空元素（空线条、间隔）内部放 `<span leaf=""><br></span>` 占位
> - 不要把 `font-size`/`border-bottom` 打在 `<strong>` 上，不要在同一个 `<p>` 里混多个不同 `font-size`——拆成多个 `<p>`，高亮样式挂在外层 `<span>`
> - 中文序号（一、二、三…）用于 `##` 章节；`###` 子标题不加序号不套竖条样式
> - 全角标点；代码块/行内代码内保持半角原样

---

## 设计变量速查表

```
主色（墨黑）：       #1A1A1A（正文 / 标题 / 表格粗线 / 深色洞察框底）
点缀色（香槟金）：   #B08D4C（编号 / 竖线 / 关键数字 / 小标签，小面积点缀，不设硬性配额但克制使用）
辅助文字色：        #888888（副标题）
次要文字色：        #999999（说明 / 标签 / 署名）/ #bbbbbbb（弱说明）/ #666666（表格脚注）
表头/正文支持色：    #555555（引用块次级正文）
暖灰底：            #fafafa（引用块底，正文底保持纯白）
行分隔线：          #eeeeee（booktabs 行间线）/ #dddddd（数据卡次线）
衬线字体：          Georgia,'Times New Roman',serif（大标题 / 章节标题 / 大数字 / 框标题）
正文字号：          16px
行高：              1.9
最大宽度：          677px
内容区边距：        0 15px（左右各 15px）
章节间距：          章节标题 margin:36px 0 16px
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;padding:0 15px;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;font-size:16px;line-height:1.9;color:#1A1A1A;background:#ffffff;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 题头卡（居中题头：金色小标签 + 衬线大标题 + 副标题 + 日期）

> **文案策略**：金色小标签用英文大写（DEEP ANALYSIS / POLICY REVIEW / WEEKLY REPORT…），点明文章类型；大标题两行为佳（主标题 + 冒号或破折号后的解读角度），衬线字体体现学术庄重感；副标题一句概括核心判断；日期行固定格式「撰文 · YYYY年M月D日 ｜ 阅读约N分钟」。

```html
<section style="text-align:center;padding:30px 0 20px;border-bottom:1px solid #1A1A1A;margin-bottom:30px;">
  <p style="font-size:12px;letter-spacing:3px;color:#B08D4C;margin:0 0 12px;font-weight:600;">
    <span leaf="">DEEP ANALYSIS</span>
  </p>
  <p style="font-family:Georgia,'Times New Roman',serif;font-size:24px;font-weight:700;color:#1A1A1A;line-height:1.45;margin:0 0 10px;">
    <span leaf="">{{主标题}}</span><br>
    <span leaf="">{{副题行：解读角度}}</span>
  </p>
  <p style="font-size:15px;color:#888888;line-height:1.6;margin:0;">
    <span leaf="">{{一句话核心判断}}</span>
  </p>
  <p style="font-size:13px;color:#999999;margin:14px 0 0;">
    <span leaf="">撰文 · {{YYYY年M月D日}} ｜ 阅读约{{N}}分钟</span>
  </p>
</section>
```

---

## 组件 3 速览框（上下 2px 墨线 + 键值速览表）

> 深度分析类文章的**标志性组件**：放在引言之后、第一章之前，用键值对表格速览事件要素（事件/时间/主体/关键数据/边界等 5~8 行）。标签列灰色窄列，内容列墨黑。亦可作「本文看点」框使用（值列写精选看点）。

```html
<section style="border:1px solid #1A1A1A;border-top-width:2px;border-bottom-width:2px;padding:20px 24px;margin:28px 0;">
  <p style="font-family:Georgia,'Times New Roman',serif;font-size:15px;font-weight:700;color:#1A1A1A;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">新闻速览</span>
  </p>
  <table style="width:100%;border-collapse:collapse;font-size:14px;line-height:1.8;">
    <tbody>
      <tr>
        <td style="padding:6px 0;color:#999999;width:90px;vertical-align:top;"><span leaf="">{{标签}}</span></td>
        <td style="padding:6px 0 6px 12px;color:#1A1A1A;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:6px 0;border-top:1px solid #eeeeee;color:#999999;vertical-align:top;"><span leaf="">{{标签}}</span></td>
        <td style="padding:6px 0 6px 12px;border-top:1px solid #eeeeee;color:#1A1A1A;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

> 复制 `<tr>` 增行；首行不带 `border-top`，后续行均带。

---

## 组件 4 章节标题（衬线 + 左墨竖条 + 中文序号）

> 核心特征：Georgia 衬线 21px + 左侧 3px 墨黑竖条 + 中文序号（一、二、三…）。序号随 `##` 顺序自动递增。结语章不加序号或保留"结语"字样，样式不变。

```html
<p style="font-family:Georgia,'Times New Roman',serif;font-size:21px;font-weight:700;color:#1A1A1A;margin:36px 0 16px;padding-left:12px;border-left:3px solid #1A1A1A;line-height:1.5;">
  <span leaf="">一、{{章节标题}}</span>
</p>
```

**结语章节变体**（无序号，直接以判断句作题）：

```html
<p style="font-family:Georgia,'Times New Roman',serif;font-size:21px;font-weight:700;color:#1A1A1A;margin:36px 0 16px;padding-left:12px;border-left:3px solid #1A1A1A;line-height:1.5;">
  <span leaf="">结语：{{判断句标题}}</span>
</p>
```

---

## 组件 5 子标题（`###` 小节标题）

> 衬线 17px 半粗，无线条无序号，与 `##` 章节标题拉开层级。

```html
<p style="font-family:Georgia,'Times New Roman',serif;font-size:17px;font-weight:600;color:#1A1A1A;margin:24px 0 12px;line-height:1.5;">
  <span leaf="">1. {{子标题}}</span>
</p>
```

---

## 组件 6 正文段落

> **关键规则**：16px / 行高 1.9 / 两端对齐。每段主动识别 1~3 个关键短语，用**金色下划线（7c）**标记；普通加粗用墨黑 `font-weight:600`（7a）。

**基础段落**：

```html
<p style="margin-bottom:20px;text-align:justify;">
  <span leaf="">{{正文内容}}</span>
</p>
```

**带关键词标记的段落**（推荐默认）：

```html
<p style="margin-bottom:20px;text-align:justify;">
  <span leaf="">{{前半句}}</span><span style="border-bottom:2px solid #B08D4C;font-weight:600;color:#1A1A1A;"><span leaf="">{{关键短语}}</span></span><span leaf="">{{后半句}}</span>
</p>
```

**标记原则**：每段选 1~3 个关键短语（4~15 字）加金色下划线，优先标核心观点、结论判断、关键数据、专有名词；无重点的段落可不标；不要整段都标。

---

## 组件 7 行内高亮样式

### 7a. 墨黑加粗（默认，绝大部分加粗用这个）

```html
<strong style="font-weight:600;color:#1A1A1A;"><span leaf="">加粗强调</span></strong>
```

### 7b. 金色加粗（关键数据 / 关键结论，小面积点缀）

```html
<strong style="font-weight:600;color:#B08D4C;"><span leaf="">7000份</span></strong>
```

### 7c. 金色下划线（标记层，本主题标志性正文标记）

```html
<span style="border-bottom:2px solid #B08D4C;font-weight:600;color:#1A1A1A;"><span leaf="">金色下划线关键词</span></span>
```

### 7d. 行内代码

```html
<span style="background:#f4f4f4;color:#1A1A1A;padding:2px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">code</span></span>
```

---

## 组件 8 引用块（金竖线 + 暖灰底，2 种变体）

### 8a. 释义/结论引用（"一句话定义"式，带加粗引导词）

```html
<section style="border-left:3px solid #B08D4C;padding:12px 20px;margin:20px 0;background:#fafafa;">
  <p style="font-size:15px;color:#1A1A1A;margin:0;line-height:1.9;">
    <strong style="font-weight:600;color:#1A1A1A;"><span leaf="">{{引导词：如"一句话定义："}}</span></strong><span leaf="">{{引用内容}}</span>
  </p>
</section>
```

### 8b. 原文引文（斜体，中英文皆可）

```html
<section style="border-left:3px solid #B08D4C;padding:12px 20px;margin:20px 0;background:#fafafa;">
  <p style="font-size:14px;color:#1A1A1A;margin:0;font-style:italic;line-height:1.9;">
    <span leaf="">"{{原文引文}}"</span>
  </p>
</section>
```

### 8c. 多段说明引用（带小标题，如"开源边界说明"）

```html
<section style="border-left:3px solid #B08D4C;padding:12px 20px;margin:20px 0;background:#fafafa;">
  <p style="font-size:14px;color:#1A1A1A;margin:0 0 6px;">
    <strong style="font-weight:600;color:#1A1A1A;"><span leaf="">{{小标题}}</span></strong>
  </p>
  <p style="font-size:14px;color:#555555;margin:0;line-height:1.9;">
    <span leaf="">{{说明内容}}</span>
  </p>
</section>
```

---

## 组件 9 深色洞察框（墨黑底 + 金标题，全篇 ≤3 处）

> 本主题最强视觉锚点：`#1A1A1A` 深底、金色衬线小标题、浅白正文、金色加粗要点引导词。仅用于全文最关键的 2~3 处判断（如"关键洞察""三步棋""核心判断"）。**严禁滥用**。

```html
<section style="background:#1A1A1A;padding:20px 24px;margin:24px 0;">
  <p style="font-family:Georgia,'Times New Roman',serif;font-size:15px;font-weight:700;color:#B08D4C;margin:0 0 12px;letter-spacing:1px;">
    <span leaf="">{{框标题：如"关键洞察"}}</span>
  </p>
  <p style="font-size:14px;color:#eeeeee;margin:0 0 10px;line-height:1.9;">
    <strong style="color:#B08D4C;font-weight:600;"><span leaf="">{{要点引导词一}}</span></strong><span leaf=""> {{要点内容一}}</span>
  </p>
  <p style="font-size:14px;color:#eeeeee;margin:0;line-height:1.9;">
    <strong style="color:#B08D4C;font-weight:600;"><span leaf="">{{要点引导词二}}</span></strong><span leaf=""> {{要点内容二}}</span>
  </p>
</section>
```

> 增删要点 = 增删 `<p>`；最后一条 `margin:0`。金色收尾句变体：`color:#B08D4C;font-weight:600;`。

---

## 组件 10 booktabs 表格（学术三线表）

> 标志性组件：表头行上下各 2px/1px 墨线、数据行间 1px `#eee` 浅线、末行底部 2px 墨线，**无任何背景填充**。表头 `font-weight:600`，对比类表格可将弱方内容用 `#666666`、强方用 `#1A1A1A`，关键数字金色加粗（7b）。

```html
<table style="width:100%;border-collapse:collapse;font-size:14px;margin:20px 0;">
  <thead>
    <tr>
      <th style="padding:10px 12px;border-top:2px solid #1A1A1A;border-bottom:1px solid #1A1A1A;text-align:left;font-weight:600;color:#1A1A1A;width:20%;"><span leaf="">{{列标题}}</span></th>
      <th style="padding:10px 12px;border-top:2px solid #1A1A1A;border-bottom:1px solid #1A1A1A;text-align:left;font-weight:600;color:#1A1A1A;"><span leaf="">{{列标题}}</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px 12px;border-bottom:1px solid #eeeeee;vertical-align:top;"><strong style="font-weight:600;"><span leaf="">{{条目}}</span></strong></td>
      <td style="padding:10px 12px;border-bottom:1px solid #eeeeee;vertical-align:top;"><span leaf="">{{内容}}</span></td>
    </tr>
    <tr>
      <td style="padding:10px 12px;border-bottom:2px solid #1A1A1A;vertical-align:top;"><strong style="font-weight:600;"><span leaf="">{{末行条目}}</span></strong></td>
      <td style="padding:10px 12px;border-bottom:2px solid #1A1A1A;vertical-align:top;"><span leaf="">{{末行内容}}</span></td>
    </tr>
  </tbody>
</table>
```

> 数据行全部用 `border-bottom:1px solid #eeeeee`，**仅末行**换成 `border-bottom:2px solid #1A1A1A`。双栏对比表可在表尾加整行合并脚注：`<td colspan="2" style="padding:10px 12px;border-bottom:2px solid #1A1A1A;text-align:center;font-size:13px;color:#666666;">`。

---

## 组件 11 数据对比卡（booktabs 双栏大数字）

> 前后对比的杀手锏：左右两栏，旧值灰色衬线大数字、新值墨黑衬线大数字 + 金色标签，上下 booktabs 线，底部整行脚注放反差结论（金色加粗数字）。

```html
<section style="margin:24px 0;text-align:center;">
  <table style="width:100%;border-collapse:collapse;font-size:14px;">
    <tbody>
      <tr>
        <td style="padding:20px 10px;border-top:2px solid #1A1A1A;border-bottom:1px solid #dddddd;text-align:center;width:50%;">
          <p style="font-size:13px;color:#999999;margin:0 0 6px;"><span leaf="">{{旧值标签}}</span></p>
          <p style="font-family:Georgia,'Times New Roman',serif;font-size:36px;font-weight:700;color:#999999;line-height:1;margin:0 0 6px;"><span leaf="">13.3%</span></p>
          <p style="font-size:12px;color:#bbbbbb;margin:0;"><span leaf="">{{旧值说明}}</span></p>
        </td>
        <td style="padding:20px 10px;border-top:2px solid #1A1A1A;border-bottom:1px solid #dddddd;text-align:center;width:50%;">
          <p style="font-size:13px;color:#B08D4C;margin:0 0 6px;"><span leaf="">{{新值标签}}</span></p>
          <p style="font-family:Georgia,'Times New Roman',serif;font-size:36px;font-weight:700;color:#1A1A1A;line-height:1;margin:0 0 6px;"><span leaf="">38.3%</span></p>
          <p style="font-size:12px;color:#999999;margin:0;"><span leaf="">{{新值说明}}</span></p>
        </td>
      </tr>
      <tr>
        <td colspan="2" style="padding:12px 10px;border-bottom:2px solid #1A1A1A;text-align:center;font-size:13px;color:#666666;">
          <span leaf="">{{脚注前缀}} </span><strong style="color:#B08D4C;font-weight:600;"><span leaf="">{{反差结论金色数字}}</span></strong>
        </td>
      </tr>
    </tbody>
  </table>
</section>
```

---

## 组件 12 编号要点框（上下 2px 墨线 + 金/灰编号列表）

> 机遇、局限、步骤、看点等并列要点（3~6 条）。正面/机遇用**金色编号**，负面/局限用**灰色编号**，形成克制的语义区分。

```html
<section style="border:1px solid #1A1A1A;border-top-width:2px;border-bottom-width:2px;padding:20px 24px;margin:24px 0;">
  <p style="font-family:Georgia,'Times New Roman',serif;font-size:15px;font-weight:700;color:#1A1A1A;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">{{框标题：如"值得关注的机遇"}}</span>
  </p>
  <p style="font-size:14px;color:#1A1A1A;line-height:2;margin:0 0 8px;">
    <span style="color:#B08D4C;font-weight:600;"><span leaf="">01</span></span><span leaf="">&nbsp;</span><strong style="font-weight:600;"><span leaf="">{{要点标题}}</span></strong><span leaf=""> — {{要点说明}}</span>
  </p>
  <p style="font-size:14px;color:#1A1A1A;line-height:2;margin:0;">
    <span style="color:#999999;font-weight:600;"><span leaf="">02</span></span><span leaf="">&nbsp;</span><strong style="font-weight:600;"><span leaf="">{{要点标题}}</span></strong><span leaf=""> — {{要点说明}}</span>
  </p>
</section>
```

> 增删要点 = 增删 `<p>`；最后一条 `margin:0`。流程步骤（如工作流演示）同款组件，每条一行、编号 01~06 金色，行间用 `<br>` 连接时可合并为单个 `<p style="font-size:14px;color:#1A1A1A;line-height:2.1;margin:0;">`。

---

## 组件 13 列表（引导词加粗列表）

> 简单并列项，`<ul>` 原生列表 + 引导词加粗，不用复杂结构。

```html
<ul style="margin:14px 0 20px;padding-left:22px;font-size:15px;line-height:2;">
  <li><strong style="font-weight:600;"><span leaf="">{{引导词}}</span></strong><span leaf="">——{{说明}}</span></li>
</ul>
```

---

## 组件 14 分隔线 + 话题标签 + 文末签名区

**分隔线**（结语之后、标签之前）：

```html
<hr style="border:none;border-top:1px solid #1A1A1A;margin:32px 0;">
```

**话题标签**（居中灰字，# 标签 5~8 个）：

```html
<p style="text-align:center;font-size:12px;color:#999999;line-height:2.2;margin:0 0 24px;">
  <span leaf="">#{{标签一}} &nbsp; #{{标签二}} &nbsp; #{{标签三}} &nbsp; #{{标签四}}</span>
</p>
```

**文末签名区**（居中，上 1px 墨线）：

```html
<section style="text-align:center;padding:20px 0 30px;border-top:1px solid #1A1A1A;">
  <p style="font-size:13px;color:#999999;margin:0 0 6px;">
    <span leaf="">本文为原创深度分析，转载请注明出处</span>
  </p>
  <p style="font-size:13px;color:#B08D4C;font-weight:600;margin:0;">
    <span leaf="">关注获取更多AI行业前沿解读</span>
  </p>
</section>
```

> 有作者署名时，签名区第一行替换为 `我是 {{作者名}}，{{一句话简介}}`；引导语"关注获取更多…"可按公众号定位改写。

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:0 15px;font-family:...;font-size:16px;line-height:1.9;color:#1A1A1A;background:#ffffff;">

  <!-- 1. 题头卡（组件2：金色小标签 + 衬线大标题 + 副标题 + 日期） -->
  <!-- 2. 引言正文（组件6 段落 × 2~3，交代事件背景与全文判断） -->
  <!-- 3. 速览框（组件3：事件要素键值表） -->
  <!-- 4. 第一章（组件4 章节标题：一、…） -->
  <!--    章内：组件6 正文 + 5 子标题 + 7 行内高亮 + 8 引用 + 10 booktabs 表 + 11 数据对比卡 -->
  <!-- 5. 第二~N章（组件4，序号二、三…；核心判断章插组件9 深色洞察框 ≤3 处） -->
  <!-- 6. 并列要点章（组件12 编号要点框：机遇金色编号 / 局限灰色编号） -->
  <!-- 7. 结语章（组件4 变体：结语：判断句标题 + 组件9 核心判断收尾） -->
  <!-- 8. 分隔线（组件14 hr）+ 话题标签 + 文末签名区 -->

</section>
```

**骨架铁律**：题头卡在最前；速览框紧跟引言；深色洞察框全篇 ≤3 处（含结语"核心判断"）；一篇只有一个签名区；无独立 END 线（hr + 签名区上边线即收尾）。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 深色洞察框 9（墨黑底+金标题） | 全文最关键判断 | 全篇 ≤3 处 |
| **标记层** | 金色下划线 7c + 墨黑加粗 7a + 金色数字 7b | 正文关键词、关键数据 | 每段 1~3 处 |
| **容器层** | 引用块 8 / 速览框 3 / booktabs 表 10 / 数据卡 11 / 要点框 12 | 结构化信息 | 按需 |

**克制原则**：
- 金色只做小面积点缀（竖线、编号、下划线、关键数字、小标签），**绝不做大面积底色**
- 除深色洞察框与引用块暖灰底外，正文底色保持纯白，无卡片底色
- 层级靠衬线/非衬线字体对比、字重、留白与三线表建立，不靠颜色堆砌
- 数据优先用 booktabs 表格 / 数据对比卡呈现，体现学术庄重感

---

## 文章类型 → 组件组合配方

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 深度分析/AI新闻解读（默认场景） | 题头卡2 + 速览框3 + 章节4 + 正文6 + booktabs表10 + 数据对比卡11 | 引用8、深色洞察框9（≤3）、要点框12 |
| 政策/监管解读 | 题头卡2 + 速览框3 + 章节4 + 正文6 + 要点框12（义务/禁止分金色/灰色编号） | 引用8b 原文引文、booktabs表10 |
| 数据复盘/报告 | 题头卡2 + 速览框3 + 数据对比卡11 + booktabs表10 + 章节4 | 深色洞察框9、金色数字7b |
| 观点/评论 | 题头卡2 + 章节4 + 正文6 + 引用8a | 居中要点框12、深色洞察框9 |
| 案例/实战复盘 | 题头卡2 + 速览框3 + 章节4 + 流程要点框12（金色01~06） + booktabs表10 | 引用8、数据对比卡11 |

---

## Markdown → 极简优雅白排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 组件 2 题头卡 | 公众号外标题在平台设置，题头卡为文内题头 |
| 文章开头背景段 | 组件 6 段落 × 2~3 | 引言正文，交代事件+全文判断 |
| 事件要素速览 | 组件 3 速览框 | 深度分析必备，标签列+内容列 |
| `## 章节标题` | 组件 4 衬线章节标题 | 中文序号一、二、…自动递增 |
| `### 子标题` | 组件 5 衬线子标题 | 无线条无序号 |
| 普通段落 | 组件 6 正文段落 | 每段主动标 1~3 处金色下划线 7c |
| `**加粗文字**` | 组件 7a 墨黑加粗 | 默认 |
| 关键数据 | 组件 7b 金色加粗 | 数字、百分比、金额 |
| `<u>下划线</u>` / `++文字++` | 组件 7c 金色下划线 | 标记层 |
| `==高亮文字==` | 组件 7b 金色加粗 | 核心概念 |
| `> 引用`（定义/结论） | 组件 8a 金竖线引用 | 加粗引导词 |
| `> 引用`（原文） | 组件 8b 斜体引文 | 中英文皆可 |
| `> 引用`（边界/说明） | 组件 8c 多段说明引用 | 带小标题 |
| 核心洞察/战略判断 | 组件 9 深色洞察框 | 全篇 ≤3 处 |
| Markdown 表格 | 组件 10 booktabs 表格 | 三线表，末行粗线 |
| 前后数据对比 | 组件 11 数据对比卡 | 旧灰新黑+金标签 |
| 机遇/要点/局限/流程 | 组件 12 编号要点框 | 正面金色编号、负面灰色编号 |
| 并列要点（轻量） | 组件 13 列表 | 引导词加粗 |
| 行内 `` `code` `` | 组件 7d 行内代码 | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色 / 1b 浅色（左竖条换 `#B08D4C`） | 每行一个 `<p style="margin:0">`，禁 `white-space:pre` |
| `---` | 组件 14 分隔线 | 仅结语后用一次 |
| 话题标签 | 组件 14 话题标签 | # 标签 5~8 个 |
| 文末 | 组件 14 签名区 | 一篇仅一处 |
| `![](图片)` | 通用库 2a 图片组件 | `max-width:100%;height:auto;display:block;margin:0 auto` |
