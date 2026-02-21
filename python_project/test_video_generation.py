#!/usr/bin/env python3
"""
影片生成功能測試
由 OpenClaw 建立 🐻
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# 檢查環境
print("🔧 檢查影片處理環境...")

# 檢查 FFmpeg
print("1. 檢查 FFmpeg...")
ffmpeg_available = False
try:
    result = os.popen('which ffmpeg').read().strip()
    if result:
        ffmpeg_available = True
        ffmpeg_version = os.popen('ffmpeg -version 2>/dev/null | head -1').read().strip()
        print(f"   ✅ FFmpeg 可用: {ffmpeg_version}")
    else:
        print("   ❌ FFmpeg 未安裝")
except:
    print("   ❌ 無法檢查 FFmpeg")

# 檢查 ImageMagick
print("2. 檢查 ImageMagick...")
imagemagick_available = False
try:
    result = os.popen('which convert').read().strip()
    if result:
        imagemagick_available = True
        print("   ✅ ImageMagick 可用")
    else:
        print("   ❌ ImageMagick 未安裝")
except:
    print("   ❌ 無法檢查 ImageMagick")

# 檢查 Python 套件
print("3. 檢查 Python 影片處理套件...")

def check_python_package(package_name, import_name=None):
    """檢查 Python 套件是否可用"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        version = "未知版本"
        try:
            module = sys.modules[import_name]
            if hasattr(module, '__version__'):
                version = module.__version__
        except:
            pass
        print(f"   ✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"   ❌ {package_name}: 未安裝")
        return False

# 檢查主要套件
packages_to_check = [
    ("moviepy", "moviepy"),
    ("opencv-python", "cv2"),
    ("imageio", "imageio"),
    ("PIL/Pillow", "PIL"),
    ("numpy", "numpy"),
    ("pydub", "pydub"),
]

available_packages = {}
for display_name, import_name in packages_to_check:
    available = check_python_package(display_name, import_name)
    available_packages[display_name] = available

print("\n" + "=" * 60)
print("📊 環境檢查總結:")

# 核心依賴檢查
core_dependencies = {
    "FFmpeg": ffmpeg_available,
    "ImageMagick": imagemagick_available,
    "moviepy": available_packages.get("moviepy", False),
    "OpenCV": available_packages.get("opencv-python", False),
}

all_core_available = all(core_dependencies.values())

for name, available in core_dependencies.items():
    status = "✅" if available else "❌"
    print(f"  {status} {name}")

if all_core_available:
    print("\n🎉 所有核心依賴都可用！可以開始測試影片生成。")
else:
    print("\n⚠️ 部分核心依賴缺失，需要安裝後才能完整測試。")

print("\n" + "=" * 60)
print("💡 建議安裝命令:")

if not ffmpeg_available:
    print("  brew install ffmpeg")

if not imagemagick_available:
    print("  brew install imagemagick")

missing_python_packages = []
for display_name, available in available_packages.items():
    if not available:
        if display_name == "moviepy":
            missing_python_packages.append("moviepy")
        elif display_name == "opencv-python":
            missing_python_packages.append("opencv-python")
        elif display_name == "imageio":
            missing_python_packages.append("imageio")
        elif display_name == "pydub":
            missing_python_packages.append("pydub")

if missing_python_packages:
    print(f"  pip install {' '.join(missing_python_packages)}")

print("\n" + "=" * 60)
print("🚀 準備測試影片生成功能...")

# 如果核心依賴都可用，嘗試建立簡單測試
if all_core_available:
    print("\n嘗試建立簡單影片測試...")
    
    # 建立測試目錄
    test_dir = Path("video_test_output")
    test_dir.mkdir(exist_ok=True)
    
    print(f"測試輸出目錄: {test_dir.absolute()}")
    
    # 嘗試不同的影片生成方法
    test_methods = []
    
    # 方法1: 使用 OpenCV 建立簡單影片
    if available_packages.get("opencv-python", False):
        test_methods.append("OpenCV 影片生成")
    
    # 方法2: 使用 moviepy 建立文字影片
    if available_packages.get("moviepy", False):
        test_methods.append("moviepy 文字影片")
    
    # 方法3: 使用 PIL 建立圖片序列
    if available_packages.get("PIL/Pillow", False):
        test_methods.append("PIL 圖片序列")
    
    print(f"\n可測試的方法: {', '.join(test_methods)}")
    
    if test_methods:
        print("\n建議測試順序:")
        for i, method in enumerate(test_methods, 1):
            print(f"  {i}. {method}")
        
        print("\n輸入對應數字選擇測試方法，或按 Enter 跳過測試:")
        try:
            choice = input().strip()
            if choice and choice.isdigit():
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(test_methods):
                    selected_method = test_methods[choice_idx]
                    print(f"\n選擇測試: {selected_method}")
                    # 這裡可以根據選擇執行對應測試
                else:
                    print("無效選擇，跳過測試")
            else:
                print("跳過測試")
        except:
            print("跳過測試")
    else:
        print("沒有可用的測試方法")

print("\n" + "=" * 60)
print("🎬 影片處理環境檢查完成！")
print("=" * 60)