# Expose key helpers for simple imports elsewhere
from .crawler import get_all_forms, get_all_links
from .scanner import scan_xss
from .reporter import save_report

__all__ = ["get_all_forms", "get_all_links", "scan_xss", "save_report"]

