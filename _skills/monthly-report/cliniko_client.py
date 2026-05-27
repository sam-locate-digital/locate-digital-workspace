"""Cliniko API client — read-only helpers for monthly reporting."""
from base64 import b64encode
from datetime import datetime
import urllib.request
import urllib.parse
import json
from typing import Optional

USER_AGENT = "Locate Digital Reports (sam@locatedigital.io)"
TS_FMT = "%Y-%m-%dT%H:%M:%SZ"


class ClinikoClient:
    def __init__(self, api_key: str, shard: str):
        self.base_url = f"https://api.{shard}.cliniko.com/v1"
        auth = b64encode(f"{api_key}:".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        }

    def _get(self, url: str):
        req = urllib.request.Request(url, headers=self.headers)
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())

    def get(self, path: str, params: Optional[dict] = None):
        url = f"{self.base_url}{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params, doseq=True)
        return self._get(url)

    def paginate(self, path: str, params: Optional[dict] = None, key: Optional[str] = None):
        """Follow `links.next` until exhausted. Returns merged list from `key`."""
        if key is None:
            key = path.strip("/").split("/")[0]
        params = dict(params or {})
        params.setdefault("per_page", 100)
        url = f"{self.base_url}{path}?" + urllib.parse.urlencode(params, doseq=True)
        out = []
        while url:
            data = self._get(url)
            out.extend(data.get(key, []))
            url = (data.get("links") or {}).get("next")
        return out

    def appointments_in_range(self, start: datetime, end: datetime):
        """Active (non-cancelled) appointments scheduled in the window."""
        return self.paginate("/appointments", {
            "q[]": [
                f"starts_at:>{start.strftime(TS_FMT)}",
                f"starts_at:<{end.strftime(TS_FMT)}",
            ],
        })

    def cancellations_in_range(self, start: datetime, end: datetime):
        """Appointments cancelled in the window (cancelled_at, not starts_at)."""
        return self.paginate("/appointments", {
            "q[]": [
                f"cancelled_at:>{start.strftime(TS_FMT)}",
                f"cancelled_at:<{end.strftime(TS_FMT)}",
            ],
        })

    def patients_created_in_range(self, start: datetime, end: datetime):
        return self.paginate("/patients", {
            "q[]": [
                f"created_at:>{start.strftime(TS_FMT)}",
                f"created_at:<{end.strftime(TS_FMT)}",
            ],
        })

    def businesses(self):
        return self.paginate("/businesses")

    def practitioners(self):
        return self.paginate("/practitioners")
