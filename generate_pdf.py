#!/usr/bin/env python3
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def html_to_pdf(html_file, pdf_file):
    """Convert HTML file to PDF using Chrome headless"""
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Set up print options for PDF
    print_options = {
        'printBackground': True,
        'paperWidth': 8.27,  # A4 width in inches
        'paperHeight': 11.69,  # A4 height in inches
        'marginTop': 0.4,
        'marginBottom': 0.4,
        'marginLeft': 0.4,
        'marginRight': 0.4,
        'scale': 0.9,
        'preferCSSPageSize': True
    }
    
    try:
        # Initialize driver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Get absolute path to HTML file
        html_path = os.path.abspath(html_file)
        
        # Load HTML file
        driver.get(f'file://{html_path}')
        
        # Wait for page to load completely
        time.sleep(3)
        
        # Execute JavaScript to ensure all content is loaded
        driver.execute_script("""
            // Force layout calculation
            document.body.style.zoom = '1';
            // Wait for images to load
            var images = document.getElementsByTagName('img');
            var promises = Array.from(images).map(img => {
                if (img.complete) return Promise.resolve();
                return new Promise(resolve => {
                    img.onload = resolve;
                    img.onerror = resolve;
                });
            });
            return Promise.all(promises);
        """)
        
        time.sleep(2)
        
        # Generate PDF
        result = driver.execute_cdp_cmd('Page.printToPDF', print_options)
        
        # Save PDF
        with open(pdf_file, 'wb') as f:
            f.write(base64.b64decode(result['data']))
        
        print(f"✅ PDF successfully generated: {pdf_file}")
        print(f"📄 File size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False
        
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    import base64
    
    html_file = "美股新聞彙整_2026-02-18.html"
    pdf_file = "美股新聞彙整_2026-02-18.pdf"
    
    print(f"📊 Converting {html_file} to {pdf_file}...")
    
    if html_to_pdf(html_file, pdf_file):
        sys.exit(0)
    else:
        sys.exit(1)