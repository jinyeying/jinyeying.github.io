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
cited_by = 0
for entry in data.get("cited_by", {}).get("table", []):
    if "citations" in entry:
        cited_by = entry["citations"].get("all", 0)
        break

print(f"[SerpAPI] {name}: {cited_by} citations")

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as f:
    json.dump({"name": name, "citedby": cited_by, "updated": str(datetime.now())},
              f, ensure_ascii=False, indent=2)

with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": str(cited_by)},
              f, ensure_ascii=False)
