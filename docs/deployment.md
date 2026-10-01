# 展示网站部署

本项目的网站入口是 `docs/index.html`，全部为静态文件，无构建步骤。

## GitHub Pages

1. 将项目推送到公开 GitHub 仓库。
2. 打开仓库 **Settings → Pages**。
3. Source 选择 **Deploy from a branch**。
4. Branch 选择 **main**，目录选择 **/docs**，保存。
5. 等待 Pages 构建成功，访问 `https://mayanbiao1234.github.io/TierFlow-Design/`。

注意选择 `/docs`，仓库根目录没有网站入口。`docs/.nojekyll` 用于按静态文件部署。

## 本地预览

```bash
python -m http.server 4173 --directory docs
```

打开 `http://localhost:4173`。也可直接打开 `docs/index.html`；剪贴板权限不足时，页面会选中文本，供手动复制。

## Fork 后修改

将 `README.md`、`README.en.md`、`docs/` 中的 `mayanbiao1234/TierFlow-Design` 与 `mayanbiao1234.github.io/TierFlow-Design` 换成自己的仓库和 Pages 地址。保留上游来源说明与许可证。

修改主题展厅时，应同步维护 `docs/index.html`、`docs/gallery/index.html` 和 `docs/assets/site.js` 中的主题清单；运行 `python scripts/check_project.py` 验证文件和示例。
