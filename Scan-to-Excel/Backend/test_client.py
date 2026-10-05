import requests
import os
import time

url = "http://127.0.0.1:5001/upload"

base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "single-info.png")

t0 = time.time()
with open(image_path, "rb") as f:
    response = requests.post(url, files={"file": f}, timeout=60)
dt = time.time() - t0

print(f"Status: {response.status_code} in {dt:.2f}s")
data = response.json()
rows = data.get("data", [])
print(f"Extracted {len(rows)} rows:")
for r in rows[:6]:
    print("  ", r)