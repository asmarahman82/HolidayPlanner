# tools/metrics_tool.py
import logging
from datetime import datetime

class MetricsTracker:
    def __init__(self):
        self.events = []

    def log_event(self, name: str, details: dict = None):
        entry = {"time": datetime.utcnow().isoformat(), "event": name, "details": details or {}}
        self.events.append(entry)
        logging.info(f"Metrics: {name} - {details}")

    def get(self):
        return self.events
