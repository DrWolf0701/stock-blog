#!/usr/bin/env python3
"""
熊抱哥賀歲影片生成
10秒新年祝福影片
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
print("🎬 熊抱哥賀歲影片生成")
print("=" * 70)

# 建立輸出目錄
output_dir = Path("lotso_new_year_video")
output_dir.mkdir(exist_ok=True)

print(f"輸出目錄: {output_dir.absolute()}")

# 影片設定
width, height = 640, 480
fps = 24
duration = 10  # 10秒
total_frames = fps * duration

print(f"影片規格: {width}x{height}, {fps} FPS, {duration}秒 ({total_frames}幀)")

# 建立熊抱哥主題顏色
LOTSO_COLORS = {
    'purple': (180, 100, 200),      # 熊抱哥紫色
    'pink': (255, 150, 200),        # 草莓粉紅
    'red': (255, 50, 50),           # 新年紅色
    'gold': (255, 215, 0),          # 金色
    'green': (100, 200, 100),       # 幸運綠色
}

# 賀歲文字
NEW_YEAR_TEXTS = [
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

def create_lotso_frame(frame_num, total_frames):
    """建立熊抱哥主題影格"""
    # 建立漸變背景
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 計算漸變進度
    progress = frame_num / total_frames
    
    # 背景漸變（紫色到紅色）
    bg_color = np.array([
        int(LOTSO_COLORS['purple'][0] * (1 - progress) + LOTSO_COLORS['red'][0] * progress),
        int(LOTSO_COLORS['purple'][1] * (1 - progress) + LOTSO_COLORS['red'][1] * progress),
        int(LOTSO_COLORS['purple'][2] * (1 - progress) + LOTSO_COLORS['red'][2] * progress)
    ])
    
    frame[:, :] = bg_color
    
    # 加入閃爍星星效果
    if frame_num % 10 < 5:  # 閃爍效果
        star_color = LOTSO_COLORS['gold']
        for i in range(20):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height // 2)
            size = np.random.randint(1, 3)
            cv2.circle(frame, (x, y), size, star_color, -1)
    
    # 加入草莓圖案（簡單圓形代表）
    strawberry_color = LOTSO_COLORS['pink']
    for i in range(5):
        x = 50 + i * 120
        y = height - 100
        cv2.circle(frame, (x, y), 20, strawberry_color, -1)
        # 草莓葉子
        leaf_color = LOTSO_COLORS['green']
        cv2.ellipse(frame, (x, y - 25), (15, 8), 0, 0, 360, leaf_color, -1)
    
    return frame

def add_text_to_frame(frame, frame_num, total_frames):
    """加入文字到影格"""
    # 選擇文字（根據時間變化）
    text_index = (frame_num // (fps * 1)) % len(NEW_YEAR_TEXTS)  # 每1秒換一次文字
    text = NEW_YEAR_TEXTS[text_index]
    
    # 文字位置（上下移動）
    text_y = 100 + int(20 * np.sin(frame_num * 0.1))
    
    # 文字顏色（漸變）
    text_color = (
        int(255 * (0.5 + 0.5 * np.sin(frame_num * 0.05))),
        int(255 * (0.5 + 0.5 * np.sin(frame_num * 0.05 + 2))),
        int(255 * (0.5 + 0.5 * np.sin(frame_num * 0.05 + 4)))
    )
    
    # 加入文字陰影
    shadow_color = (50, 50, 50)
    cv2.putText(frame, text, (52, text_y + 2), cv2.FONT_HERSHEY_SIMPLEX, 
               0.8, shadow_color, 2, cv2.LINE_AA)
    
    # 加入主要文字
    cv2.putText(frame, text, (50, text_y), cv2.FONT_HERSHEY_SIMPLEX, 
               0.8, text_color, 2, cv2.LINE_AA)
    
    # 加入熊抱哥標誌
    lotso_text = "🐻 熊抱哥祝福您！ 🐻"
    cv2.putText(frame, lotso_text, (width // 2 - 150, height - 50), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, LOTSO_COLORS['gold'], 2, cv2.LINE_AA)
    
    # 加入計時器
    time_text = f"{frame_num // fps}.{frame_num % fps:02d}s / {duration}s"
    cv2.putText(frame, time_text, (width - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 
               0.5, (200, 200, 200), 1, cv2.LINE_AA)
    
    return frame

def create_firework_effect(frame, frame_num):
    """建立煙火效果"""
    if frame_num % 15 == 0:  # 每15幀一個煙火
        # 煙火位置
        x = np.random.randint(100, width - 100)
        y = np.random.randint(50, height // 2)
        
        # 煙火顏色
        firework_color = (
            np.random.randint(200, 255),
            np.random.randint(100, 255),
            np.random.randint(50, 255)
        )
        
        # 煙火效果
        for i in range(12):
            angle = i * 30
            length = 30 + frame_num % 10
            end_x = int(x + length * np.cos(np.radians(angle)))
            end_y = int(y + length * np.sin(np.radians(angle)))
            
            cv2.line(frame, (x, y), (end_x, end_y), firework_color, 2)
    
    return frame

def create_confetti_effect(frame, frame_num):
    """建立彩帶效果"""
    if frame_num % 3 == 0:  # 每3幀一些彩帶
        for i in range(5):
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
            color = (
                np.random.randint(100, 255),
                np.random.randint(100, 255),
                np.random.randint(100, 255)
            )
            size = np.random.randint(2, 5)
            cv2.circle(frame, (x, y), size, color, -1)
    
    return frame

# 建立影片
print("\n🎥 開始生成影片...")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_path = output_dir / "lotso_new_year_greeting.mp4"
out = cv2.VideoWriter(str(video_path), fourcc, fps, (width, height))

for i in range(total_frames):
    # 建立基礎影格
    frame = create_lotso_frame(i, total_frames)
    
    # 加入文字
    frame = add_text_to_frame(frame, i, total_frames)
    
    # 加入特效
    if i > fps * 2:  # 2秒後開始特效
        frame = create_firework_effect(frame, i)
        frame = create_confetti_effect(frame, i)
    
    # 寫入影格
    out.write(frame)
    
    # 顯示進度
    if i % (fps * 2) == 0:  # 每2秒顯示一次進度
        seconds = i // fps
        print(f"  生成中... {seconds}秒 / {duration}秒")

out.release()

print(f"\n✅ 影片生成完成: {video_path.name}")

# 建立封面圖片
print("\n🖼️ 建立影片封面圖片...")
try:
    # 使用第一幀作為封面
    cap = cv2.VideoCapture(str(video_path))
    ret, cover_frame = cap.read()
    cap.release()
    
    if ret:
        cover_path = output_dir / "video_cover.jpg"
        cv2.imwrite(str(cover_path), cover_frame)
        print(f"✅ 封面圖片建立完成: {cover_path.name}")
        
        # 建立縮圖版本
        thumbnail_path = output_dir / "video_thumbnail.jpg"
        thumbnail = cv2.resize(cover_frame, (320, 240))
        cv2.imwrite(str(thumbnail_path), thumbnail)
        print(f"✅ 縮圖建立完成: {thumbnail_path.name}")
except Exception as e:
    print(f"⚠️ 封面圖片建立失敗: {e}")

# 建立GIF預覽
print("\n🎞️ 建立GIF預覽...")
try:
    # 讀取影片並建立GIF
    cap = cv2.VideoCapture(str(video_path))
    gif_frames = []
    
    # 每0.5秒取一幀
    for i in range(0, total_frames, fps // 2):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            # 轉換顏色空間 BGR -> RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gif_frames.append(frame_rgb)
    
    cap.release()
    
    if gif_frames:
        gif_path = output_dir / "preview.gif"
        imageio.mimsave(str(gif_path), gif_frames, fps=5)
        print(f"✅ GIF預覽建立完成: {gif_path.name}")
    else:
        print("⚠️ 無法建立GIF預覽")
except Exception as e:
    print(f"⚠️ GIF預覽建立失敗: {e}")

# 檔案資訊
print("\n" + "=" * 70)
print("📊 影片生成結果:")

video_files = list(output_dir.glob("*"))
if video_files:
    total_size = 0
    for file in sorted(video_files):
        size = os.path.getsize(file)
        total_size += size
        
        # 檔案類型圖標
        if file.suffix == '.mp4':
            icon = "🎬"
        elif file.suffix == '.jpg':
            icon = "🖼️"
        elif file.suffix == '.gif':
            icon = "🎞️"
        else:
            icon = "📄"
        
        print(f"  {icon} {file.name}: {size:,} bytes")
    
    print(f"\n📦 總檔案大小: {total_size:,} bytes")
    print(f"📁 檔案數量: {len(video_files)} 個")
    
    # 主要影片資訊
    if video_path.exists():
        video_size = os.path.getsize(video_path)
        print(f"\n🎥 主要影片資訊:")
        print(f"  解析度: {width}x{height}")
        print(f"  幀率: {fps} FPS")
        print(f"  長度: {duration} 秒")
        print(f"  大小: {video_size:,} bytes")
        print(f"  位元率: {video_size * 8 // duration // 1000} kbps")

print("\n" + "=" * 70)
print("💝 影片內容特色:")
print("  1. 🐻 熊抱哥主題配色（紫色、粉紅、紅色）")
print("  2. 🎆 新年煙火和彩帶特效")
print("  3. 🧧 10句不同的新年祝福語")
print("  4. 🍓 草莓圖案裝飾")
print("  5. ✨ 閃爍星星背景")
print("  6. 🎊 動態文字效果")

print("\n🚀 準備傳送影片...")
print("=" * 70)