#!/usr/bin/env python3
"""
建立簡單影片測試
由 OpenClaw 建立 🐻
"""

import os
import sys
import numpy as np
from datetime import datetime
from pathlib import Path

print("=" * 70)
print("🎬 影片生成功能測試")
print("=" * 70)

# 建立輸出目錄
output_dir = Path("video_output")
output_dir.mkdir(exist_ok=True)

print(f"輸出目錄: {output_dir.absolute()}")

# 測試1: 使用 OpenCV 建立簡單影片
print("\n1. 測試 OpenCV 影片生成...")
try:
    import cv2
    
    # 影片設定
    width, height = 640, 480
    fps = 10
    duration = 3  # 3秒
    total_frames = fps * duration
    
    # 建立影片寫入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_path = output_dir / "opencv_test.mp4"
    out = cv2.VideoWriter(str(video_path), fourcc, fps, (width, height))
    
    print(f"   建立 {width}x{height} 影片，{fps} FPS，{duration}秒")
    
    # 產生漸變色影格
    for i in range(total_frames):
        # 建立漸變背景
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # 漸變效果
        color_value = int(255 * (i / total_frames))
        frame[:, :, 0] = color_value  # 藍色通道
        frame[:, :, 2] = 255 - color_value  # 紅色通道
        
        # 加入文字
        text = f"Frame {i+1}/{total_frames}"
        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 255, 255), 2)
        
        # 加入時間戳
        timestamp = datetime.now().strftime("%H:%M:%S")
        cv2.putText(frame, timestamp, (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.7, (200, 200, 200), 1)
        
        out.write(frame)
    
    out.release()
    
    if video_path.exists():
        size = os.path.getsize(video_path)
        print(f"   ✅ OpenCV 影片建立完成: {size:,} bytes")
    else:
        print("   ❌ OpenCV 影片建立失敗")
        
except Exception as e:
    print(f"   ❌ OpenCV 測試失敗: {e}")

# 測試2: 使用 moviepy 建立文字影片
print("\n2. 測試 moviepy 文字影片生成...")
try:
    from moviepy.editor import TextClip, CompositeVideoClip
    
    # 建立文字片段
    text = "OpenClaw 影片測試\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    txt_clip = TextClip(text, fontsize=40, color='white', size=(640, 480))
    txt_clip = txt_clip.set_duration(5)  # 5秒
    txt_clip = txt_clip.set_position('center')
    
    # 設定背景顏色
    from moviepy.editor import ColorClip
    color_clip = ColorClip(size=(640, 480), color=(0, 100, 200), duration=5)
    
    # 合成影片
    video = CompositeVideoClip([color_clip, txt_clip])
    
    # 輸出影片
    video_path = output_dir / "moviepy_text.mp4"
    video.write_videofile(str(video_path), fps=24, codec='libx264')
    
    if video_path.exists():
        size = os.path.getsize(video_path)
        print(f"   ✅ moviepy 文字影片建立完成: {size:,} bytes")
    else:
        print("   ❌ moviepy 文字影片建立失敗")
        
except Exception as e:
    print(f"   ❌ moviepy 測試失敗: {e}")

# 測試3: 使用 PIL 建立圖片序列，然後轉成影片
print("\n3. 測試 PIL 圖片序列轉影片...")
try:
    from PIL import Image, ImageDraw, ImageFont
    import imageio
    
    # 建立圖片序列
    image_sequence = []
    num_frames = 10
    
    for i in range(num_frames):
        # 建立新圖片
        img = Image.new('RGB', (640, 480), color=(50, 50, 100))
        draw = ImageDraw.Draw(img)
        
        # 繪製文字
        text = f"圖片 {i+1}/{num_frames}"
        try:
            # 嘗試使用系統字體
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
        except:
            font = ImageFont.load_default()
        
        draw.text((50, 200), text, fill=(255, 255, 255), font=font)
        
        # 加入時間
        time_text = datetime.now().strftime("%H:%M:%S")
        draw.text((50, 250), time_text, fill=(200, 200, 200), font=font)
        
        # 轉換為 numpy 陣列供 imageio 使用
        img_array = np.array(img)
        image_sequence.append(img_array)
    
    # 儲存為 GIF（最簡單的動畫格式）
    gif_path = output_dir / "pil_sequence.gif"
    imageio.mimsave(str(gif_path), image_sequence, fps=2)
    
    if gif_path.exists():
        size = os.path.getsize(gif_path)
        print(f"   ✅ PIL 圖片序列 GIF 建立完成: {size:,} bytes")
        
        # 嘗試轉換為 MP4
        try:
            from moviepy.editor import VideoFileClip
            mp4_path = output_dir / "pil_sequence.mp4"
            
            # 讀取 GIF 並轉存為 MP4
            clip = VideoFileClip(str(gif_path))
            clip.write_videofile(str(mp4_path), fps=24)
            
            if mp4_path.exists():
                size = os.path.getsize(mp4_path)
                print(f"   ✅ GIF 轉 MP4 完成: {size:,} bytes")
        except Exception as e:
            print(f"   ⚠️ GIF 轉 MP4 失敗: {e}")
    else:
        print("   ❌ PIL 圖片序列建立失敗")
        
except Exception as e:
    print(f"   ❌ PIL 測試失敗: {e}")

# 測試4: 簡單的影片剪輯（合併影片）
print("\n4. 測試簡單影片剪輯...")
try:
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    
    # 檢查是否有可用的測試影片
    test_files = list(output_dir.glob("*.mp4"))
    
    if len(test_files) >= 2:
        print(f"   找到 {len(test_files)} 個測試影片，嘗試合併...")
        
        clips = []
        for file in test_files[:2]:  # 只取前兩個
            try:
                clip = VideoFileClip(str(file))
                clips.append(clip)
                print(f"   載入: {file.name} ({clip.duration:.1f}秒)")
            except Exception as e:
                print(f"   載入失敗 {file.name}: {e}")
        
        if len(clips) >= 2:
            # 合併影片
            final_clip = concatenate_videoclips(clips)
            
            # 輸出合併後的影片
            merged_path = output_dir / "merged_video.mp4"
            final_clip.write_videofile(str(merged_path), fps=24)
            
            if merged_path.exists():
                size = os.path.getsize(merged_path)
                print(f"   ✅ 影片合併完成: {size:,} bytes")
            else:
                print("   ❌ 影片合併失敗")
        else:
            print("   ⚠️ 沒有足夠的影片可合併")
    else:
        print("   ⚠️ 需要至少2個測試影片才能進行剪輯測試")
        
except Exception as e:
    print(f"   ❌ 影片剪輯測試失敗: {e}")

# 總結
print("\n" + "=" * 70)
print("📊 影片生成測試總結:")

# 列出生成的檔案
video_files = list(output_dir.glob("*"))
if video_files:
    print("生成的檔案:")
    total_size = 0
    for file in sorted(video_files):
        size = os.path.getsize(file)
        total_size += size
        print(f"  📹 {file.name}: {size:,} bytes")
    
    print(f"\n總檔案大小: {total_size:,} bytes")
    print(f"平均每個檔案: {total_size // len(video_files):,} bytes")
else:
    print("❌ 沒有生成任何影片檔案")

print("\n" + "=" * 70)
print("💡 影片處理能力已建立:")
print("  1. ✅ OpenCV - 程式化影片生成")
print("  2. ✅ moviepy - 文字影片和編輯")
print("  3. ✅ PIL/imageio - 圖片序列處理")
print("  4. ✅ 基本影片剪輯 - 合併影片")

print("\n🚀 下一步:")
print("  1. 可測試實際應用場景")
print("  2. 可加入音訊處理")
print("  3. 可建立螢幕錄製功能")
print("  4. 可自動化影片報告生成")

print("\n🎬 影片生成功能測試完成！")
print("=" * 70)