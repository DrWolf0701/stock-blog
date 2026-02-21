# 🚀 一鍵部署指令
# 請複製以下指令到終端機執行

## 第一步：登入 GitHub CLI
```bash
gh auth login
```
按照提示完成授權（選擇 GitHub.com → HTTPS → 是）

## 第二步：創建倉庫
```bash
gh repo create stock-blog --public --description "美股新聞每日分析報告" --disable-wiki --disable-issues
```

## 第三步：推送到 GitHub
```bash
cd /tmp/stock-blog-gh-pages
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/DrWolf0701/stock-blog.git
git push -u origin main
```

## 第四步：啟用 GitHub Pages
```bash
# 方法 A：使用 GitHub CLI
gh api -X POST "/repos/DrWolf0701/stock-blog/pages" -f "source={\"branch\":\"main\",\"path\":\"/\"}"

# 或方法 B：手動開啟
open https://github.com/DrWolf0701/stock-blog/settings/pages
```

## 第五步：訪問你的部落格
```bash
open https://drwolf0701.github.io/stock-blog/
```

# 📋 替代方案：網頁上傳

如果終端機指令遇到問題，使用網頁上傳：

## 1. 創建倉庫
訪問：https://github.com/new
- 名稱：stock-blog
- 描述：美股新聞每日分析報告
- 選擇：Public
- 不要初始化 README、.gitignore、license

## 2. 上傳檔案
訪問：https://github.com/DrWolf0701/stock-blog/upload/main
將 `/tmp/stock-blog-gh-pages/` 的所有檔案拖曳上傳

## 3. 啟用 Pages
訪問：https://github.com/DrWolf0701/stock-blog/settings/pages
- Source: Deploy from a branch
- Branch: main
- Folder: / (root)
- 點擊 Save

# 🌐 你的部落格網址
https://drwolf0701.github.io/stock-blog/

# 📁 本地預覽
/tmp/stock-blog-gh-pages/index.html

# ⏱️ 預計時間
- 登入 GitHub：2分鐘
- 創建倉庫：1分鐘
- 推送檔案：1分鐘
- 啟用 Pages：1分鐘
- **總計：約5分鐘**

# 🎉 立即開始！
複製上面的指令到終端機執行，5分鐘後你的部落格就上線了！