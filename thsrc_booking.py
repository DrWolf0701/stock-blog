#!/usr/bin/env python3
"""
台灣高鐵訂票嘗試
由於高鐵網站有複雜的驗證機制，這只是一個概念驗證
"""

import requests
import json
from datetime import datetime

# 高鐵訂票相關資訊
booking_info = {
    "passenger_name": "蕭毓則",
    "id_number": "A120872165",
    "travel_date": "2026-02-19",  # 下禮拜四
    "from_station": "板橋",
    "to_station": "田中",
    "departure_time": "10:00",
    "ticket_type": "標準車廂",
    "pickup_method": "車站窗口取票"
}

def check_thsrc_availability():
    """檢查高鐵訂票系統可用性"""
    print("🧸 開始嘗試台灣高鐵訂票...")
    print(f"乘客: {booking_info['passenger_name']}")
    print(f"身分證: {booking_info['id_number']}")
    print(f"行程: {booking_info['from_station']} → {booking_info['to_station']}")
    print(f"日期: {booking_info['travel_date']} {booking_info['departure_time']}")
    print(f"取票方式: {booking_info['pickup_method']}")
    print("-" * 50)
    
    # 嘗試訪問高鐵網站
    try:
        # 高鐵主網站
        response = requests.get("https://www.thsrc.com.tw", timeout=10)
        print(f"✅ 高鐵網站可訪問 (狀態碼: {response.status_code})")
        
        # 嘗試訪問訂票頁面
        booking_page = "https://irs.thsrc.com.tw/IMINT/"
        try:
            booking_response = requests.get(booking_page, timeout=10)
            print(f"✅ 訂票頁面可訪問 (狀態碼: {booking_response.status_code})")
        except:
            print("⚠️  訂票頁面訪問可能有問題，需要瀏覽器操作")
            
    except Exception as e:
        print(f"❌ 無法訪問高鐵網站: {e}")
        return False
    
    return True

def simulate_booking_process():
    """模擬訂票流程（概念）"""
    print("\n📋 模擬訂票流程：")
    print("1. 查詢班次時刻...")
    print("   板橋→田中，2026-02-19，10:00左右")
    print("   預計行車時間: 約1小時10分鐘")
    
    print("\n2. 選擇班次（範例）：")
    print("   - 車次 203: 10:05 板橋 → 11:15 田中")
    print("   - 車次 205: 10:35 板橋 → 11:45 田中")
    print("   - 車次 207: 11:05 板橋 → 12:15 田中")
    
    print("\n3. 填寫乘客資料：")
    print(f"   姓名: {booking_info['passenger_name']}")
    print(f"   身分證: {booking_info['id_number']}")
    
    print("\n4. 選擇取票方式：")
    print(f"   {booking_info['pickup_method']}")
    
    print("\n5. 產生訂位代碼：")
    print("   訂位完成後會取得一組訂位代碼")
    print("   憑代碼+身分證到高鐵窗口取票")
    
    print("\n💰 預計票價：")
    print("   標準車廂: NT$ 750-850")
    print("   早鳥優惠可能: NT$ 550-650")

def get_manual_instructions():
    """提供手動訂票指引"""
    print("\n" + "="*50)
    print("🧸 由於自動化限制，建議手動訂票方式：")
    print("\n📱 手機App訂票（推薦）：")
    print("1. 下載「高鐵T-EX」App")
    print("2. 選擇「板橋→田中」、日期「2026-02-19」")
    print("3. 選擇「10:00」左右班次")
    print("4. 輸入乘客: 蕭毓則 (A120872165)")
    print("5. 選擇「車站窗口取票」")
    print("6. 完成訂位取得「訂位代碼」")
    
    print("\n💻 網站訂票：")
    print("1. 訪問 https://irs.thsrc.com.tw/IMINT/")
    print("2. 依上述步驟操作")
    
    print("\n🏪 超商訂票：")
    print("1. 到7-11/全家/萊爾富/OK多媒體機")
    print("2. 選擇高鐵訂票")
    print("3. 依指示操作")

if __name__ == "__main__":
    print("="*60)
    print("台灣高鐵訂票助手")
    print("="*60)
    
    # 檢查可用性
    if check_thsrc_availability():
        # 模擬流程
        simulate_booking_process()
        
        # 提供手動指引
        get_manual_instructions()
        
        print("\n" + "="*60)
        print("⚠️  注意事項：")
        print("- 訂位後需在乘車前完成取票")
        print("- 車站窗口取票需出示身分證")
        print("- 建議提前30分鐘到車站")
        print("- 早鳥票需提前購買（通常28天前）")
        print("="*60)
    else:
        print("\n❌ 無法進行自動訂票，請使用手動方式。")