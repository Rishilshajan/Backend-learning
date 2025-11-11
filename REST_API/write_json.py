import json 
from pathlib import Path

path = Path("data.json")
data = json.loads(path.read_text(encoding="utf-8"))

data["last_updated"] = "2025-11-05T10:00:00+05:30"

path.write_text(json.dumps(data, indent=2), encoding="utf-8")
print("Updated data.json")