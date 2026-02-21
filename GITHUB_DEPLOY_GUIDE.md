# GitHub Pages 部署指南

## 📋 已完成的工作

我已經為你準備好了：
1. ✅ **部落格檔案**：精美的 HTML 網頁、Markdown 報告、PDF 檔案
2. ✅ **本地 Git 倉庫**：所有檔案已提交到 Git
3. ✅ **部署目錄**：`/tmp/stock-blog-gh-pages`

## 🚀 部署步驟

### 步驟 1：創建 GitHub 倉庫
1. 訪問 https://github.com/new
2. 填寫以下資訊：
   - **Repository name**: `stock-blog`
   - **Description**: `美股新聞每日分析報告`
   - **Public** (選擇公開)
   - **不要**初始化 README、.gitignore、license
3. 點擊 **Create repository**

### 步驟 2：生成 Personal Access Token
由於 GitHub 已禁用密碼認證，你需要：
1. 訪問 https://github.com/settings/tokens
2. 點擊 **Generate new token** → **Generate new token (classic)**
3. 填寫：
   - **Note**: `Stock Blog Deployment`
   - **Expiration**: 90天（建議）
   - **Select scopes**: 勾選 `repo`（全部權限）
4. 點擊 **Generate token**
5. **立即複製 token**（只會顯示一次）

### 步驟 3：推送到 GitHub
打開終端機，執行以下指令：

```bash
# 1. 進入部署目錄
cd /tmp/stock-blog-gh-pages

# 2. 設定遠端倉庫（使用你的 token）
git remote add origin https://<YOUR_TOKEN>@github.com/DrWolf0701/stock-blog.git

# 3. 推送到 GitHub
git push -u origin main
```

將 `<YOUR_TOKEN>` 替換為你剛剛生成的 token。

### 步驟 4：啟用 GitHub Pages
1. 訪問 https://github.com/DrWolf0701/stock-blog/settings/pages
2. 在 **Source** 部分：
   - 選擇 **Deploy from a branch**
   - 分支選擇 **main**
   - 資料夾選擇 **/ (root)**
3. 點擊 **Save**

### 步驟 5：訪問你的部落格
等待約1-2分鐘，然後訪問：
```
https://drwolf0701.github.io/stock-blog/
```

## 📁 檔案說明

部署目錄包含：
- `index.html` - 部落格主頁面（精美設計）
- `report.md` - Markdown 格式報告
- `report.pdf` - PDF 完整報告（1.6MB）
- `404.html` - 自訂404錯誤頁面
- `README.md` - 專案說明
- `.nojekyll` - 禁用 Jekyll 處理

## 🎨 部落格特色

你的部落格包含：
- ✅ **專業設計**：金融分析風格
- ✅ **響應式**：手機、平板、電腦完美顯示
- ✅ **互動功能**：策略切換、動畫效果
- ✅ **完整內容**：市場概覽、新聞分析、投資建議
- ✅ **社交優化**：支援分享到社交媒體
- ✅ **打印友好**：支援高品質打印

## 🔧 自動化部署（未來）

如果你想每天自動更新，我可以幫你設定：
1. **GitHub Actions**：自動生成每日報告
2. **定時任務**：每天下午4點自動更新
3. **歸檔系統**：歷史報告分類整理
4. **RSS 訂閱**：讓讀者訂閱更新

## 📞 需要幫助？

如果遇到問題：
1. **GitHub 問題**：檢查 token 權限和倉庫名稱
2. **部署問題**：確保所有檔案都在正確位置
3. **網頁問題**：檢查瀏覽器控制台錯誤

## 🎉 完成！

你的專業美股分析部落格即將上線！
網址：https://drwolf0701.github.io/stock-blog/

**立即開始部署，與世界分享你的市場見解！** 🐻📈🌐