#!/usr/bin/env python3
"""
Local Dev & Preview Server for Sothy VANDETH's Portfolio (sothy8.github.io)
Usage: python3 serve.py [port]
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from re import findall

PORT = 8000
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def validate_assets():
    """Verify that all image assets referenced in index.html actually exist on disk."""
    print("🔍 Validating portfolio assets and paths in index.html...")
    index_path = os.path.join(DIRECTORY, "index.html")
    if not os.path.exists(index_path):
        print("❌ Error: index.html not found!")
        return False
    
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find src="assets/..." or href="css/..." or src="js/..."
    sources = findall(r'(?:src|href)=["\']([^"\']+)["\']', content)
    missing = []
    found = 0

    for src in sources:
        # Ignore external links or anchor tags
        if src.startswith("http://") or src.startswith("https://") or src.startswith("#") or src.startswith("mailto:") or src.startswith("tel:"):
            continue

        file_path = os.path.join(DIRECTORY, src)
        if not os.path.exists(file_path):
            missing.append(src)
        else:
            found += 1

    if missing:
        print(f"⚠️ Warning: Found {len(missing)} missing asset file(s):")
        for m in missing:
            print(f"   - {m}")
    else:
        print(f"✅ Asset Validation Passed: All {found} local assets (images, CSS, JS) exist!")

    return len(missing) == 0

class LocalHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    os.chdir(DIRECTORY)
    validate_assets()

    port = PORT
    handler = LocalHandler

    # Try binding to port, if busy increment port
    for p in range(port, port + 10):
        try:
            with socketserver.TCPServer(("", p), handler) as httpd:
                url = f"http://localhost:{p}"
                print(f"\n🚀 Portfolio Preview Server running at: {url}")
                print("Press Ctrl+C to stop the server.\n")
                webbrowser.open(url)
                httpd.serve_forever()
            break
        except OSError:
            print(f"Port {p} is in use, trying {p+1}...")
        except KeyboardInterrupt:
            print("\n👋 Server stopped.")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
