import requests, re
from urllib.parse import urljoin
from .crawler import get_all_forms
from .payloads import XSS

def _injected(resp_text, payload):
    return payload in resp_text

def scan_xss(url):
    hits = []
    for form in get_all_forms(url):
        action = form.get("action") or url
        method = (form.get("method") or "get").lower()
        inputs = [i for i in form.find_all("input") if i.get("name")]
        for payload in XSS:
            data = {inp["name"]: payload for inp in inputs}
            dest = urljoin(url, action)
            resp = requests.post(dest, data=data, timeout=10) if method == "post" \
                   else requests.get(dest, params=data, timeout=10)
            if _injected(resp.text, payload):
                hits.append(
                    {"type": "XSS", "url": dest, "payload": payload}
                )
    return hits

