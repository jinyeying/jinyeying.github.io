import json
import os
import signal
from datetime import datetime

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
cited_by = None
name = ""

# Try Google Scholar via scholarly (basics + indices only, NO publications list)
try:
    def _timeout(signum, frame):
        raise TimeoutError("scholarly timed out")

    signal.signal(signal.SIGALRM, _timeout)
    signal.alarm(90)  # 90-second hard timeout

    from scholarly import scholarly
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices'])  # skip publications — that's what was slow
    cited_by = author.get('citedby')
    name = author.get('name', '')
    signal.alarm(0)
    print(f"[Google Scholar] {name}: {cited_by} citations")

except Exception as e:
    signal.alarm(0)
    print(f"scholarly failed ({e}), falling back to Semantic Scholar")

# Fallback: Semantic Scholar (fast, reliable, different count)
if cited_by is None:
    import urllib.request
    ss_url = "https://api.semanticscholar.org/graph/v1/author/2141507823?fields=citationCount,name"
    req = urllib.request.Request(ss_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    cited_by = data.get("citationCount", 0)
    name = data.get("name", "")
    print(f"[Semantic Scholar fallback] {name}: {cited_by} citations")

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as f:
    json.dump({"name": name, "citedby": cited_by, "updated": str(datetime.now())},
              f, ensure_ascii=False, indent=2)

with open("results/gs_data_shieldsio.json", "w") as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": str(cited_by)},
              f, ensure_ascii=False)
