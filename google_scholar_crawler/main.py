import json
import os
import urllib.request
from datetime import datetime

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
serpapi_key = os.environ['SERPAPI_KEY']

url = (
    f"https://serpapi.com/search.json"
    f"?engine=google_scholar_author"
    f"&author_id={scholar_id}"
    f"&api_key={serpapi_key}"
)
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read())

name = data.get("author", {}).get("name", "")

# SerpAPI returns cited_by.table as a list of single-key dicts, one per metric:
# [{"citations": {...}}, {"h_index": {...}}, {"i10_index": {...}}]
metrics = {}
for entry in data.get("cited_by", {}).get("table", []):
    for key, value in entry.items():
        if isinstance(value, dict) and "all" in value:
            metrics[key] = value["all"]

cited_by = metrics.get("citations", 0)
h_index = metrics.get("h_index", 0)
i10_index = metrics.get("i10_index", 0)

print(f"[SerpAPI] {name}: {cited_by} citations, h-index {h_index}, i10 {i10_index}")

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as f:
    json.dump({"name": name, "citedby": cited_by,
               "h_index": h_index, "i10_index": i10_index,
               "updated": str(datetime.now())},
              f, ensure_ascii=False, indent=2)

with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": str(cited_by)},
              f, ensure_ascii=False)

# Keep the h-index in its own endpoint file so the badge can be added
# without touching the citations badge.
with open("results/gs_hindex_shieldsio.json", "w") as f:
    json.dump({"schemaVersion": 1, "label": "h-index", "message": str(h_index)},
              f, ensure_ascii=False)
