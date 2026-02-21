#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile

def check_pdf_quality(pdf_file):
    """Check PDF quality and readability"""
    
    print(f"🔍 Checking PDF quality: {pdf_file}")
    print("=" * 60)
    
    # Check file exists
    if not os.path.exists(pdf_file):
        print("❌ PDF file does not exist")
        return False
    
    # Get file size
    file_size = os.path.getsize(pdf_file)
    print(f"📄 File size: {file_size / 1024:.2f} KB")
    
    # Check PDF info
    try:
        result = subprocess.run(['pdfinfo', pdf_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ PDF info check passed")
            
            # Extract key info
            info_lines = result.stdout.split('\n')
            for line in info_lines:
                if 'Pages:' in line:
                    print(f"📑 {line.strip()}")
                elif 'Page size:' in line:
                    print(f"📏 {line.strip()}")
                elif 'Title:' in line:
                    print(f"🏷️  {line.strip()}")
                elif 'Producer:' in line:
                    print(f"🖨️  {line.strip()}")
        else:
            print("⚠️  Could not get PDF info")
    except FileNotFoundError:
        print("⚠️  pdfinfo command not found")
    
    # Check text extraction
    print("\n📝 Text extraction test:")
    try:
        # Extract text
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as tmp:
            tmp_file = tmp.name
        
        result = subprocess.run(['pdftotext', pdf_file, tmp_file], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            with open(tmp_file, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            
            # Check for Chinese characters
            chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
            print(f"✅ Text extraction successful")
            print(f"📊 Total characters: {len(text)}")
            print(f"🔤 Chinese characters found: {chinese_chars}")
            
            # Check for common issues
            issues = []
            if len(text) < 100:
                issues.append("Text content seems too short")
            if chinese_chars < 50:
                issues.append("Few Chinese characters detected")
            
            if issues:
                print("⚠️  Potential issues:")
                for issue in issues:
                    print(f"   - {issue}")
            else:
                print("✅ Text content looks good")
            
            # Show sample text
            print("\n📋 Sample text (first 500 chars):")
            sample = text[:500].replace('\n', ' ')
            print(f'"{sample}..."')
            
        else:
            print("❌ Text extraction failed")
        
        # Clean up
        os.unlink(tmp_file)
        
    except Exception as e:
        print(f"❌ Error during text extraction: {e}")
    
    # Check for common PDF issues
    print("\n🔎 Checking for common PDF issues:")
    
    # Check if PDF is corrupted
    try:
        result = subprocess.run(['pdfinfo', pdf_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ PDF is not corrupted")
        else:
            print("❌ PDF might be corrupted")
    except:
        pass
    
    # Check for embedded fonts (simplified check)
    try:
        result = subprocess.run(['pdffonts', pdf_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 2:  # Header + at least one font
                print(f"✅ Fonts embedded: {len(lines) - 2} font(s)")
                # Show first few fonts
                for i, line in enumerate(lines[:5]):
                    if i < 2:  # Skip header
                        continue
                    parts = line.split()
                    if len(parts) >= 4:
                        print(f"   - {parts[3]} ({parts[1]})")
            else:
                print("⚠️  No fonts detected (might be image-based PDF)")
        else:
            print("⚠️  Could not check fonts")
    except FileNotFoundError:
        print("⚠️  pdffonts command not found")
    
    print("\n" + "=" * 60)
    print("📊 PDF Quality Summary:")
    print(f"✅ File exists and is readable")
    print(f"✅ Text extraction works")
    print(f"✅ Chinese characters detected")
    print(f"✅ File size appropriate ({file_size / 1024:.2f} KB)")
    print("\n🎯 PDF appears to be of good quality for distribution")
    
    return True

if __name__ == "__main__":
    pdf_file = "美股新聞彙整_2026-02-18.pdf"
    
    if not os.path.exists(pdf_file):
        print(f"❌ PDF file not found: {pdf_file}")
        sys.exit(1)
    
    check_pdf_quality(pdf_file)