import json, os
from datetime import datetime

def save_report(results, folder="reports"):
    os.makedirs(folder, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fn = os.path.join(folder, f"report_{ts}.json")
    with open(fn, "w") as f:
        json.dump(results, f, indent=2)
    return fn

