#!/usr/bin/env python3
"""Stage the 7 Instagram slides at public direct URLs via here.now.

Instagram fetches each carousel item from a public URL, so the PNGs must be
reachable with no query string. Publishes a clean dir of just the slides.

Prints one URL per line as: slide-N=<url>
"""
import hashlib
import json
import mimetypes
import os
import sys
from pathlib import Path

import requests

BASE_URL = "https://here.now"
HERE = Path(__file__).resolve().parent
STAGE_DIR = HERE / "_stage"
CRED_FILE = Path.home() / ".herenow" / "credentials"
STATE_FILE = HERE / "_stage" / ".herenow" / "state.json"
N = 7


def api_key() -> str:
    k = os.environ.get("HERENOW_API_KEY", "").strip()
    if k:
        return k
    if CRED_FILE.exists():
        return CRED_FILE.read_text().strip()
    return ""


def content_type(p: Path) -> str:
    ct, _ = mimetypes.guess_type(str(p))
    return ct or "application/octet-stream"


def main() -> int:
    key = api_key()
    if not key:
        print("error: no here.now API key", file=sys.stderr)
        return 1

    STAGE_DIR.mkdir(exist_ok=True)
    for i in range(1, N + 1):
        src = HERE / f"slide-{i}.png"
        if not src.exists():
            print(f"error: missing {src}", file=sys.stderr)
            return 1
        (STAGE_DIR / src.name).write_bytes(src.read_bytes())

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "X-HereNow-Client": "hermes-agent/stage-py",
    }

    files, local = [], {}
    for f in sorted(STAGE_DIR.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(STAGE_DIR).as_posix()
        if rel.startswith(".herenow/"):
            continue
        data = f.read_bytes()
        files.append({
            "path": rel,
            "size": len(data),
            "contentType": content_type(f),
            "hash": hashlib.sha256(data).hexdigest(),
        })
        local[rel] = data

    if not files:
        print("error: nothing to publish", file=sys.stderr)
        return 1

    print(f"creating publish ({len(files)} files)...", file=sys.stderr)
    r = requests.post(f"{BASE_URL}/api/v1/publish", headers=headers,
                      json={"files": files}, timeout=60)
    resp = r.json()
    if resp.get("error"):
        print(f"error: {resp.get('error')} {resp.get('details','')}", file=sys.stderr)
        return 1

    site_url = resp["siteUrl"].rstrip("/")
    uploads = resp["upload"].get("uploads", [])
    print(f"uploading {len(uploads)} files...", file=sys.stderr)
    for u in uploads:
        h = dict(u.get("headers", {}))
        h.pop("Content-Length", None)
        ur = requests.put(u["url"], data=local[u["path"]], headers=h, timeout=120)
        if not (200 <= ur.status_code < 300):
            print(f"error: upload failed {u['path']} HTTP {ur.status_code}", file=sys.stderr)
            return 1

    fr = requests.post(resp["upload"]["finalizeUrl"], headers=headers,
                       json={"versionId": resp["upload"]["versionId"]}, timeout=60).json()
    if fr.get("error"):
        print(f"error: finalize failed: {fr.get('error')}", file=sys.stderr)
        return 1

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(
        {"slug": resp["slug"], "siteUrl": site_url}, indent=2))

    print(f"site: {site_url}", file=sys.stderr)
    for i in range(1, N + 1):
        url = f"{site_url}/slide-{i}.png"
        # verify the URL is really reachable and is a PNG
        try:
            vr = requests.get(url, timeout=30)
            ok = vr.status_code == 200 and vr.headers.get("content-type", "").startswith("image/")
            note = f"{vr.status_code} {vr.headers.get('content-type','')} {len(vr.content)//1024}KB"
        except Exception as e:
            ok, note = False, str(e)[:60]
        print(f"slide-{i}={url}  [{note}]{'' if ok else '  <-- CHECK'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
