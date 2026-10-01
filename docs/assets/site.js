/* TierFlow-Design · AGPL-3.0 */
(() => {
  "use strict";
  const themes = {
    "moyu-green": [
      "摸鱼绿",
      "鲜活的绿色与丰富卡片，适合教程、清单和工具盘点。",
    ],
    "red-white": ["红白色系", "克制的红色强调，为观点与深度分析增加力量。"],
    "graphite-minimal": ["石墨极简", "以灰阶与留白，承载设计和科技评论。"],
    "zen-whitespace": ["留白禅意", "舒展的节奏，留给生活与深度随笔。"],
    "moyu-ticket": ["摸鱼票据", "用票据式组件，为工具对比增加趣味。"],
    "olive-journal": ["橄榄手记", "编辑部内刊气质，适合案例复盘与评测。"],
    "elegant-white": ["极简优雅白", "墨黑与香槟金，让深度内容沉静下来。"],
  };
  const explorer = document.querySelector(".theme-explorer");
  if (explorer) {
    const iframe = document.getElementById("theme-preview");
    const options = Array.from(document.querySelectorAll("[data-theme]"));
    const selectTheme = (slug) => {
      if (!Object.hasOwn(themes, slug)) return;
      const [name, description] = themes[slug];
      const source = `${explorer.dataset.galleryBase}${slug}.html`;
      options.forEach((button) =>
        button.setAttribute(
          "aria-pressed",
          String(button.dataset.theme === slug),
        ),
      );
      iframe.src = source;
      iframe.title = `${name}主题排版示例`;
      document.getElementById("preview-link").href = source;
      document.getElementById("preview-name").textContent = name;
      document.getElementById("preview-description").textContent = description;
      document.getElementById("preview-status").textContent = `已切换到${name}`;
    };
    options.forEach((button) =>
      button.addEventListener("click", () => selectTheme(button.dataset.theme)),
    );
    const requestedTheme = new URLSearchParams(location.search).get("theme");
    if (requestedTheme) selectTheme(requestedTheme);
    document.querySelectorAll("[data-width]").forEach((button) => {
      button.addEventListener("click", () => {
        document
          .querySelectorAll("[data-width]")
          .forEach((item) =>
            item.setAttribute("aria-pressed", String(item === button)),
          );
        document
          .querySelector(".preview-frame")
          .classList.toggle("wide", button.dataset.width === "wide");
      });
    });
  }
  let statusTimer;
  const announceCopy = (message) => {
    const status = document.getElementById("copy-status");
    clearTimeout(statusTimer);
    status.textContent = message;
    statusTimer = setTimeout(() => {
      status.textContent = "";
    }, 6000);
  };
  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const target = document.getElementById(button.dataset.copy);
      try {
        await navigator.clipboard.writeText(
          target.textContent.replace(/\s+/g, " ").trim(),
        );
        announceCopy(
          button.dataset.copy === "install-command"
            ? "安装命令已复制。"
            : "已复制。发给你的智能体，再附上文章即可。",
        );
      } catch {
        target.scrollIntoView({ block: "center", behavior: "instant" });
        const range = document.createRange();
        range.selectNodeContents(target);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        announceCopy("已选中文本，请按 Ctrl+C（Mac：⌘C）或长按手动复制。");
      }
    });
  });
})();
