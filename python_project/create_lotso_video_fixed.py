#!/usr/bin/env python3
"""
修正版熊抱哥賀歲影片 - 確保文字顯示
由 OpenClaw 建立 🐻
"""

import os
import sys
import numpy as np
from datetime import datetime
from pathlib import Path
import cv2
from PIL import Image, ImageDraw, ImageFont
import imageio

print("=" * 70)
print("🎬 修正版熊抱哥賀歲影片 (確保文字顯示)")
print("=" * 70)

# 建立輸出目錄
output_dir = Path("lotso_video_fixed")
output_dir.mkdir(exist_ok=True)

print(f"輸出目錄: {output_dir.absolute()}")

# 影片設定
width, height = 640, 480
fps = 24
duration = 10  # 10秒
total_frames = fps * duration

print(f"影片規格: {width}x{height}, {fps} FPS, {duration}秒")

# 測試中文字體
print("\n🔤 測試中文字體支援...")

# 嘗試不同的字體路徑
font_paths = [
    "/System/Library/Fonts/PingFang.ttc",      # macOS 系統字體
    "/System/Library/Fonts/STHeiti Medium.ttc", # 黑體
    "/System/Library/Fonts/Supplemental/Songti.ttc", # 宋體
    "/System/Library/Fonts/Helvetica.ttc",     # 英文字體（備用）
]

available_fonts = []
for font_path in font_paths:
    if os.path.exists(font_path):
        available_fonts.append(font_path)
        print(f"  ✅ 找到字體: {os.path.basename(font_path)}")

if not available_fonts:
    print("  ⚠️ 未找到系統字體，使用 PIL 預設字體")
    available_fonts.append(None)

# 方法1: 使用 PIL 繪製文字（確保中文字體）
def create_frame_with_pil_text(frame_num, total_frames):
    """使用 PIL 建立包含中文字的影格"""
    # 建立 PIL 圖片
    img = Image.new('RGB', (width, height), color=(50, 0, 100))
    draw = ImageDraw.Draw(img)
    
    # 嘗試使用中文字體
    font_size = 30
    font = None
    
    for font_path in available_fonts:
        try:
            if font_path:
                font = ImageFont.truetype(font_path, font_size)
                # 測試中文字體
                test_text = "測試"
                bbox = draw.textbbox((0, 0), test_text, font=font)
                if bbox[2] - bbox[0] > 0:  # 文字有寬度
                    print(f"   使用字體: {os.path.basename(font_path)}")
                    break
            else:
                font = ImageFont.load_default()
                print("   使用預設字體")
                break
        except:
            continue
    
    if font is None:
        font = ImageFont.load_default()
        print("   使用預設字體")
    
    # 計算漸變進度
    progress = frame_num / total_frames
    
    # 背景漸變
    bg_color = (
        int(50 + 100 * progress),
        int(100 * progress),
        int(100 + 100 * (1 - progress))
    )
    
    # 重新建立圖片
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # 賀歲文字
    new_year_texts = [
        "🐻 熊抱哥賀新年 🎉",
        "新年快樂！萬事如意！",
        "恭喜發財！紅包拿來！",
        "龍年行大運！好運龍總來！",
        "福氣滿滿！幸福滿滿！",
        "🧧 財源廣進 🧧",
        "🎊 吉祥如意 🎊",
        "🍓 草莓香香好運到 🍓",
        "🐾 熊抱哥送祝福 🐾",
        "🎇 新年新氣象 🎇"
    ]
    
    # 選擇文字
    text_index = (frame_num // (fps * 1)) % len(new_year_texts)
    text = new_year_texts[text_index]
    
    # 文字位置（置中）
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = 100 + int(20 * np.sin(frame_num * 0.1))
    
    # 文字顏色（對比色）
    text_color = (255, 255, 255)  # 白色
    
    # 加入文字陰影
    shadow_color = (0, 0, 0)
    draw.text((text_x + 2, text_y + 2), text, fill=shadow_color, font=font)
    
    # 加入主要文字
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    # 加入底部文字
    bottom_text = "熊抱哥祝福您新年快樂！"
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font)
    bottom_width = bottom_bbox[2] - bottom_bbox[0]
    bottom_x = (width - bottom_width) // 2
    bottom_y = height - 80
    
    draw.text((bottom_x, bottom_y), bottom_text, fill=(255, 215, 0), font=font)
    
    # 轉換為 OpenCV 格式
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    return frame

# 方法2: 使用 OpenCV 繪製文字（測試）
def create_frame_with_opencv_text(frame_num, total_frames):
    """使用 OpenCV 建立影格"""
    # 建立漸變背景
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    progress = frame_num / total_frames
    
    # 背景漸變
    frame[:, :, 0] = int(100 + 100 * progress)  # 藍色
    frame[:, :, 1] = int(50 * progress)         # 綠色
    frame[:, :, 2] = int(100 + 100 * (1 - progress))  # 紅色
    
    # 簡單的英文文字（確保顯示）
    text = f"Happy New Year! {frame_num // fps}.{frame_num % fps:02d}s"
    
    # 使用 OpenCV 繪製英文文字
    cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
               0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    # 測試中文字元（可能無法顯示）
    test_chinese = "新年快樂"
    cv2.putText(frame, test_chinese, (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
               0.8, (255, 255, 0), 2, cv2.LINE_AA)
    
    return frame

# 方法3: 混合方法（PIL + OpenCV）
def create_mixed_frame(frame_num, total_frames):
    """混合使用 PIL 和 OpenCV"""
    # 使用 PIL 建立基礎影格和文字
    img = Image.new('RGB', (width, height), color=(30, 0, 60))
    draw = ImageDraw.Draw(img)
    
    # 使用可用字體
    font = None
    for font_path in available_fonts:
        try:
            if font_path:
                font = ImageFont.truetype(font_path, 36)
                break
        except:
            continue
    
    if font is None:
        font = ImageFont.load_default()
    
    # 漸變背景
    progress = frame_num / total_frames
    r = int(30 + 100 * progress)
    g = int(50 * progress)
    b = int(60 + 100 * (1 - progress))
    
    img = Image.new('RGB', (width, height), color=(r, g, b))
    draw = ImageDraw.Draw(img)
    
    # 繪製裝飾元素
    for i in range(5):
        x = 50 + i * 120
        y = height - 100
        # 草莓
        draw.ellipse([x-20, y-20, x+20, y+20], fill=(255, 150, 200))
        # 葉子
        draw.ellipse([x-15, y-40, x+15, y-25], fill=(100, 200, 100))
    
    # 文字內容
    texts = [
        "🎉 新年快樂 🎉",
        "🐻 熊抱哥祝福 🐻",
        "🧧 恭喜發財 🧧",
        "🍓 好運連連 🍓",
        "🎊 萬事如意 🎊"
    ]
    
    text_index = (frame_num // (fps * 2)) % len(texts)
    text = texts[text_index]
    
    # 計算文字位置
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (width - text_width) // 2
    text_y = 100
    
    # 文字陰影
    draw.text((text_x + 3, text_y + 3), text, fill=(0, 0, 0), font=font)
    # 主要文字
    draw.text((text_x, text_y), text, fill=(255, 255, 0), font=font)
    
    # 底部文字
    bottom_text = f"影片時間: {frame_num // fps}.{frame_num % fps:02d}s / {duration}s"
    draw.text((width - 200, 30), bottom_text, fill=(200, 200, 200), font=ImageFont.load_default())
    
    # 轉換為 OpenCV 格式
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # 使用 OpenCV 加入特效
    if frame_num % 20 == 0:
        # 加入閃光
        cv2.circle(frame, (width//2, height//2), 50, (255, 255, 255), -1)
    
    return frame

print("\n🎥 開始生成測試影片...")

# 測試1: 使用 PIL 確保中文字體
print("\n1. 測試 PIL 中文字體影片...")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video1_path = output_dir / "test_pil_chinese.mp4"
out1 = cv2.VideoWriter(str(video1_path), fourcc, fps, (width, height))

for i in range(total_frames):
    frame = create_frame_with_pil_text(i, total_frames)
    out1.write(frame)
    
    if i % (fps * 2) == 0:
        print(f"  進度: {i // fps}秒 / {duration}秒")

out1.release()
print(f"  ✅ PIL 影片生成完成: {video1_path.name}")

# 測試2: 使用 OpenCV 文字
print("\n2. 測試 OpenCV 文字影片...")
video2_path = output_dir / "test_opencv_text.mp4"
out2 = cv2.VideoWriter(str(video2_path), fourcc, fps, (width, height))

for i in range(total_frames):
    frame = create_frame_with_opencv_text(i, total_frames)
    out2.write(frame)

out2.release()
print(f"  ✅ OpenCV 影片生成完成: {video2_path.name}")

# 測試3: 混合方法
print("\n3. 測試混合方法影片...")
video3_path = output_dir / "test_mixed_method.mp4"
out3 = cv2.VideoWriter(str(video3_path), fourcc, fps, (width, height))

for i in range(total_frames):
    frame = create_mixed_frame(i, total_frames)
    out3.write(frame)
    
    if i % (fps * 2) == 0:
        print(f"  進度: {i // fps}秒 / {duration}秒")

out3.release()
print(f"  ✅ 混合方法影片生成完成: {video3_path.name}")

# 建立預覽圖片
print("\n🖼️ 建立預覽圖片...")
for i, video_path in enumerate([video1_path, video2_path, video3_path], 1):
    if video_path.exists():
        cap = cv2.VideoCapture(str(video_path))
        ret, frame = cap.read()
        cap.release()
        
        if ret:
            preview_path = output_dir / f"preview_{i}.jpg"
            cv2.imwrite(str(preview_path), frame)
            print(f"  ✅ 預覽圖 {i}: {preview_path.name}")

print("\n" + "=" * 70)
print("📊 測試結果總結:")

video_files = list(output_dir.glob("*"))
if video_files:
    print("生成的檔案:")
    for file in sorted(video_files):
        size = os.path.getsize(file)
        if file.suffix == '.mp4':
            icon = "🎬"
        elif file.suffix == '.jpg':
            icon = "🖼️"
        else:
            icon = "📄"
        
        print(f"  {icon} {file.name}: {size:,} bytes")

print("\n" + "=" * 70)
print("🔧 文字顯示問題解決方案:")
print("  1. ✅ PIL 方法 - 使用 PIL 繪製中文字體")
print("  2. ⚠️ OpenCV 方法 - 可能無法顯示中文")
print("  3. ✅ 混合方法 - PIL 文字 + OpenCV 特效")

print("\n💡 建議:")
print("  • 使用 PIL 處理中文字體")
print("  • 確保字體路徑正確")
print("  • 使用對比色確保文字可見")
print("  • 測試文字位置和大小")

print("\n🚀 準備傳送測試影片...")
print("=" * 70)