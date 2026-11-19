# lionkoimap

臻臻的新加坡美食攻略：肉骨茶篇、叻沙篇。可在网页里切换篇目和比例（3:4 / 2:3 / 9:16 / 4:5）、进入编辑态改字换图，并导出 PNG 图片。

## 目录结构

```
public/index.html   部署用的成品网页（单文件，字体和图片都已内嵌）
src/template.html   网页模板：样式、店铺数据、交互逻辑都在这里改
src/build.py        把模板和素材打包成 public/index.html
assets/插画/        角色插画、纹理、logo
assets/图片/        店铺照片、二维码（照片来源与授权见网页「说明」）
assets/字体/        纳米老宋子集（常用 7500 字，免费商用授权）
vercel.json         Vercel 部署配置
```

## 修改内容

1. 改 `src/template.html`（店铺信息在 `PAGES` 数组里）。
2. 重新生成：

   ```bash
   pip install pillow
   python3 src/build.py
   ```

3. 提交并推送，Vercel 会自动重新部署。

`public/index.html` 是生成出来的文件，提交进仓库，所以 Vercel 不需要执行构建。

## 部署到 Vercel

1. 在 Vercel 点 **Add New → Project**，导入 GitHub 仓库 `corrinezine/lionkoimap`。
2. Framework Preset 选 **Other**，其他设置保持默认（`vercel.json` 已指定直接发布 `public/` 目录，不需要构建命令）。
3. 点 **Deploy**。之后每次推送到 `main` 都会自动更新。

也可以用命令行：

```bash
npx vercel --prod
```

## 本地预览

直接双击打开 `public/index.html` 即可。
