#!/usr/bin/env python3
"""
主程式範例 - 展示 Python 開發環境功能
由 OpenClaw 建立 🐻
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime


def data_science_demo():
    """資料科學功能展示"""
    print("🎯 資料科學功能展示")
    
    # 建立範例資料
    data = {
        '日期': pd.date_range('2026-01-01', periods=10),
        '銷售額': np.random.randint(100, 1000, 10),
        '客戶數': np.random.randint(10, 100, 10),
        '滿意度': np.random.uniform(3.0, 5.0, 10)
    }
    
    df = pd.DataFrame(data)
    print("\n📊 資料框範例:")
    print(df)
    
    # 基本統計
    print("\n📈 基本統計:")
    print(df.describe())
    
    return df


def web_api_demo():
    """網頁 API 功能展示"""
    print("\n🌐 網頁 API 功能展示")
    
    try:
        # 測試 API 請求
        response = requests.get('https://api.github.com', timeout=5)
        print(f"GitHub API 狀態碼: {response.status_code}")
        print(f"請求耗時: {response.elapsed.total_seconds():.2f}秒")
        
        # 顯示部分回應
        if response.status_code == 200:
            data = response.json()
            print(f"GitHub API 版本: {data.get('current_user_url', 'N/A')}")
        return True
    except Exception as e:
        print(f"API 請求失敗: {e}")
        return False


def visualization_demo(df):
    """資料視覺化展示"""
    print("\n🎨 資料視覺化展示")
    
    # 建立圖表
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # 銷售額趨勢
    axes[0, 0].plot(df['日期'], df['銷售額'], marker='o', color='blue')
    axes[0, 0].set_title('銷售額趨勢')
    axes[0, 0].set_xlabel('日期')
    axes[0, 0].set_ylabel('銷售額')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 客戶數長條圖
    axes[0, 1].bar(range(len(df)), df['客戶數'], color='green', alpha=0.7)
    axes[0, 1].set_title('客戶數分布')
    axes[0, 1].set_xlabel('索引')
    axes[0, 1].set_ylabel('客戶數')
    
    # 滿意度散布圖
    axes[1, 0].scatter(df['銷售額'], df['滿意度'], c='red', alpha=0.6)
    axes[1, 0].set_title('銷售額 vs 滿意度')
    axes[1, 0].set_xlabel('銷售額')
    axes[1, 0].set_ylabel('滿意度')
    
    # 圓餅圖（客戶數比例）
    axes[1, 1].pie(df['客戶數'], labels=df['日期'].dt.strftime('%m-%d'), autopct='%1.1f%%')
    axes[1, 1].set_title('客戶數日期分布')
    
    plt.tight_layout()
    
    # 儲存圖片
    plt.savefig('data_visualization.png', dpi=150, bbox_inches='tight')
    print("✅ 圖表已儲存為 data_visualization.png")
    
    plt.show()


def environment_info():
    """顯示環境資訊"""
    print("\n🔧 環境資訊")
    print(f"Python 版本: {pd.__version__}")
    print(f"Pandas 版本: {pd.__version__}")
    print(f"NumPy 版本: {np.__version__}")
    print(f"Matplotlib 版本: {plt.matplotlib.__version__}")
    print(f"Requests 版本: {requests.__version__}")
    print(f"當前時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """主程式"""
    print("=" * 60)
    print("🐻 Python 開發環境測試程式")
    print("=" * 60)
    
    # 顯示環境資訊
    environment_info()
    
    # 執行各功能展示
    df = data_science_demo()
    
    if web_api_demo():
        print("✅ 網路連線正常")
    
    # 詢問是否顯示圖表
    print("\n📊 是否顯示資料視覺化圖表？ (y/n): ", end="")
    show_plot = input().strip().lower()
    
    if show_plot == 'y':
        visualization_demo(df)
    
    print("\n" + "=" * 60)
    print("🎉 程式執行完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()