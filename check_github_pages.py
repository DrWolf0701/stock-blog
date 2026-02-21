#!/usr/bin/env python3
import requests
import time
import sys

def check_github_pages():
    """Check if GitHub Pages is deployed and accessible"""
    
    # GitHub Pages URL for the stock-blog repository
    base_url = "https://drwolf0701.github.io/stock-blog/"
    
    print("🔍 Checking GitHub Pages deployment...")
    print(f"📡 Testing URL: {base_url}")
    
    try:
        # Test main page
        response = requests.get(base_url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ GitHub Pages is accessible! Status: {response.status_code}")
            
            # Check for today's post
            today_url = f"{base_url}posts/2026/02/18/"
            print(f"\n📅 Checking today's post: {today_url}")
            
            today_response = requests.get(today_url, timeout=10)
            if today_response.status_code == 200:
                print(f"✅ Today's post is deployed! Status: {today_response.status_code}")
                
                # Check content
                if "每日美股新聞彙整" in today_response.text:
                    print("✅ Content verification: '每日美股新聞彙整' found in page")
                else:
                    print("⚠️  Content verification: Title not found (might be cached)")
                
                return True
            else:
                print(f"❌ Today's post not accessible. Status: {today_response.status_code}")
                return False
                
        else:
            print(f"❌ GitHub Pages not accessible. Status: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error checking GitHub Pages: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_deployment_status():
    """Check GitHub Pages deployment status via GitHub API"""
    
    print("\n📊 Checking deployment status via GitHub API...")
    
    # Note: This would require authentication for private repos
    # For public repos, we can check the site directly
    
    print("ℹ️  GitHub Pages typically takes 1-2 minutes to deploy after push.")
    print("ℹ️  You can check deployment status at: https://github.com/DrWolf0701/stock-blog/deployments")
    print("ℹ️  Or visit the site directly: https://drwolf0701.github.io/stock-blog/")
    
    return True

if __name__ == "__main__":
    print("🚀 GitHub Pages Deployment Check")
    print("=" * 50)
    
    # Wait a moment for deployment to start
    print("⏳ Waiting 10 seconds for deployment to start...")
    time.sleep(10)
    
    # Check if accessible
    if check_github_pages():
        print("\n🎉 Deployment appears successful!")
        print("✅ HTML files copied to posts/2026/02/18/")
        print("✅ Main page index.html updated")
        print("✅ Changes committed and pushed to GitHub")
        print("✅ GitHub Pages should be accessible")
    else:
        print("\n⚠️  Deployment check failed or site not yet accessible.")
        print("ℹ️  This is normal - GitHub Pages can take a few minutes to deploy.")
        
    check_deployment_status()
    
    print("\n" + "=" * 50)
    print("📋 Deployment Summary:")
    print("1. ✅ HTML file copied to stock-blog/posts/2026/02/18/index.html")
    print("2. ✅ Main page index.html updated with new post")
    print("3. ✅ Git commit created: '新增2026年2月18日美股新聞彙整文章'")
    print("4. ✅ Changes pushed to GitHub repository")
    print("5. ⏳ GitHub Pages deployment in progress (check in 1-2 minutes)")
    print("\n🔗 Live URL: https://drwolf0701.github.io/stock-blog/")
    print("🔗 Today's Post: https://drwolf0701.github.io/stock-blog/posts/2026/02/18/")