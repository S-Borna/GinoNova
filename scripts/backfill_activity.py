#!/usr/bin/env python3
"""
Backfill last_activity_at for all users.
Run this script after deploying the online tracking fix.

Usage:
    1. Login to the app as admin
    2. Open browser dev tools → Application → Local Storage
    3. Copy the 'auth_token' value
    4. Run: python scripts/backfill_activity.py YOUR_TOKEN

Or run against local backend:
    python scripts/backfill_activity.py YOUR_TOKEN --local
"""
import requests
import sys

PROD_URL = "https://saas-project-production-31f8.up.railway.app"
LOCAL_URL = "http://localhost:8000"

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    token = sys.argv[1]
    use_local = "--local" in sys.argv
    
    base_url = LOCAL_URL if use_local else PROD_URL
    
    print(f"🔄 Running backfill against {base_url}...")
    
    try:
        response = requests.post(
            f"{base_url}/api/admin/backfill-activity",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success!")
            print(f"   Updated: {data.get('updated', 'N/A')} users")
            print(f"   Total: {data.get('total_users', 'N/A')} users")
        elif response.status_code == 403:
            print("❌ Access denied - make sure you're using an admin token")
        elif response.status_code == 401:
            print("❌ Invalid or expired token")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to {base_url}")
        print("   Make sure the server is running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
