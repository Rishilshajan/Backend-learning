import json 
from pathlib import Path

path = Path("data.json")
with path.open("r", encoding="utf-8") as f:
	data = json.load(f)
print("Loaded Data Type: ",type(data))
print(json.dumps(data, indent=0))	