import time, requests, sys
WEB = "http://web:5000"
def wait_for_web(timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(WEB + "/")
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False
print("⏳ waiting for web...")
if not wait_for_web():
    print("❌ web did not become ready in time"); sys.exit(1)
r = requests.post(WEB + "/tasks", json={"title":"first task"}, timeout=5)
if r.status_code != 201:
    print("❌ POST /tasks failed:", r.status_code, r.text); sys.exit(1)
r = requests.get(WEB + "/tasks", timeout=5)
if r.status_code != 200:
    print("❌ GET /tasks failed:", r.status_code, r.text); sys.exit(1)
tasks = r.json()
if not any(t.get("title") == "first task" for t in tasks):
    print("❌ Created task not found in list:", tasks); sys.exit(1)
print("✅ server test passed"); sys.exit(0)
