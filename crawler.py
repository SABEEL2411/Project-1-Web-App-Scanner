import requests, tldextract
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_links(url):
    """Return a set of same‑site links to crawl further."""
    domain = tldextract.extract(url).registered_domain
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])
        if domain in urlparse(href).netloc:
            links.add(href.split("#")[0])   # drop fragments
    return links

def get_all_forms(url):
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.find_all("form")

