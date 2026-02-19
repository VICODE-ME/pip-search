#!/usr/bin/env python3
import sys
import json
import urllib.request
import urllib.error

def get_package_details(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    
    try:
        # Fetch data from PyPI JSON API
        req = urllib.request.Request(url, headers={'User-Agent': 'Termux-PyPI-CLI/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        info = data.get("info", {})
        
        # Format and print the output
        print(f"📦 Name:      {info.get('name')}")
        print(f"🏷️  Version:   {info.get('version')}")
        print(f"📖 Summary:   {info.get('summary')}")
        print(f"👤 Author:    {info.get('author')}")
        print(f"📜 License:   {info.get('license')}")
        print(f"🔗 Home Page: {info.get('home_page') or info.get('project_url')}")
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Error: Package '{package_name}' was not found on PyPI. Check the spelling.")
        else:
            print(f"❌ HTTP Error: {e.code}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pypi-search <package_name>")
        sys.exit(1)
        
    # Grab the package name from the command line argument
    package = sys.argv[1]
    get_package_details(package)
