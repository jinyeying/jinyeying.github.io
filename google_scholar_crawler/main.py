import json
import os
import urllib.request
from datetime import datetime

# Use Semantic Scholar API — free, reliable, no anti-bot blocking
ss_id = "2141507823"
url = f"https://api.semanticscholar.org/graph/v1/author/{ss_id}?fields=citationCount,paperCount,name,hIndex"

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read())

cited_by = data.get("citationCount", 0)
name = data.get("name", "")
h_index = data.get("hIndex", 0)

print(f"Name: {name}, Citations: {cited_by}, h-index: {h_index}")

os.makedirs("results", exist_ok=True)

gs_data = {
    "name": name,
    "citedby": cited_by,
    "hindex": h_index,
    "updated": str(datetime.now()),
}
with open("results/gs_data.json", "w") as f:
    json.dump(gs_data, f, ensure_ascii=False, indent=2)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(cited_by),
}
with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump(shieldio_data, f, ensure_ascii=False)
