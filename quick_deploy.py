#!/usr/bin/env python3
"""
快速部署腳本 - 使用 GitHub API 創建倉庫並推送
"""

import subprocess
import json
import sys
import os

# 設定
GITHUB_TOKEN = "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"
GITHUB_USER = "DrWolf0701"
REPO_NAME = "stock-blog"
DEPLOY_DIR = "/tmp/stock-blog-gh-pages"

def run_command(cmd, cwd=None):
    """執行命令並返回結果"""
    print(f"執行: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"錯誤: {result.stderr}")
    return result

def create_github_repo():
    """使用 GitHub API 創建倉庫"""
    print("🔧 創建 GitHub 倉庫...")
    
    # 檢查倉庫是否已存在
    check_cmd = f'curl -s -H "Authorization: token {GITHUB_TOKEN}" https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}'
    result = run_command(check_cmd)
    
    if '"message":"Not Found"' not in result.stdout:
        print("✅ 倉庫已存在")
        return True
    
    # 創建新倉庫
    repo_data = {
        "name": REPO_NAME,
        "description": "美股新聞每日分析報告",
        "private": False,
        "auto_init": False,
        "has_issues": False,
        "has_wiki": False,
        "has_projects": False,
        "has_downloads": False
    }
    
    create_cmd = f'''curl -X POST \
      -H "Authorization: token {GITHUB_TOKEN}" \
      -H "Accept: application/vnd.github.v3+json" \
      https://api.github.com/user/repos \
      -d '{json.dumps(repo_data)}' '''
    
    result = run_command(create_cmd)
    
    if result.returncode == 0 and '"name":"stock-blog"' in result.stdout:
        print("✅ 倉庫創建成功")
        return True
    else:
        print("❌ 倉庫創建失敗")
        print(f"輸出: {result.stdout}")
        return False

def setup_git_and_push():
    """設定 Git 並推送到 GitHub"""
    print("🔄 設定 Git 並推送...")
    
    # 進入部署目錄
    if not os.path.exists(DEPLOY_DIR):
        print(f"❌ 部署目錄不存在: {DEPLOY_DIR}")
        return False
    
    os.chdir(DEPLOY_DIR)
    
    # 檢查是否已經是 Git 倉庫
    if not os.path.exists(".git"):
        print("❌ 不是 Git 倉庫")
        return False
    
    # 設定遠端倉庫 URL（使用 token）
    remote_url = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
    
    # 移除現有的遠端倉庫
    run_command("git remote remove origin 2>/dev/null || true")
    
    # 添加新的遠端倉庫
    result = run_command(f"git remote add origin {remote_url}")
    if result.returncode != 0:
        return False
    
    # 推送到 GitHub
    print("📤 推送到 GitHub...")
    result = run_command("git push -u origin main --force")
    
    if result.returncode == 0:
        print("✅ 推送成功！")
        return True
    else:
        print("❌ 推送失敗")
        return False

def enable_github_pages():
    """啟用 GitHub Pages（需要手動操作）"""
    print("\n🌐 啟用 GitHub Pages：")
    print(f"1. 訪問 https://github.com/{GITHUB_USER}/{REPO_NAME}/settings/pages")
    print("2. 在 'Source' 部分選擇 'Deploy from a branch'")
    print("3. 分支選擇 'main'，資料夾選擇 '/ (root)'")
    print("4. 點擊 'Save'")
    print(f"\n🎉 你的部落格網址：https://{GITHUB_USER}.github.io/{REPO_NAME}/")

def main():
    print("🚀 開始部署美股新聞部落格到 GitHub Pages")
    print(f"📋 GitHub 帳號: {GITHUB_USER}")
    print(f"📦 倉庫名稱: {REPO_NAME}")
    
    # 步驟 1: 創建 GitHub 倉庫
    if not create_github_repo():
        print("\n⚠️  無法創建倉庫，請手動創建：")
        print(f"   訪問 https://github.com/new")
        print(f"   倉庫名稱: {REPO_NAME}")
        print(f"   描述: 美股新聞每日分析報告")
        print(f"   選擇: Public (公開)")
        print(f"   不要初始化 README、.gitignore、license")
        print("\n創建完成後按 Enter 繼續...")
        input()
    
    # 步驟 2: 推送到 GitHub
    if setup_git_and_push():
        # 步驟 3: 啟用 GitHub Pages
        enable_github_pages()
        
        # 打開本地預覽
        print("\n📱 打開本地預覽...")
        index_path = os.path.join(DEPLOY_DIR, "index.html")
        if os.path.exists(index_path):
            run_command(f"open '{index_path}' 2>/dev/null || echo '請手動開啟: {index_path}'")
    else:
        print("\n❌ 部署失敗")
        print("請檢查：")
        print("1. GitHub token 是否有效")
        print("2. 倉庫名稱是否正確")
        print("3. 網路連線是否正常")
        
        # 提供替代方案
        print("\n🔧 替代方案：手動部署")
        print(f"cd {DEPLOY_DIR}")
        print(f"git remote add origin https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO_NAME}.git")
        print("git push -u origin main")

if __name__ == "__main__":
    main()