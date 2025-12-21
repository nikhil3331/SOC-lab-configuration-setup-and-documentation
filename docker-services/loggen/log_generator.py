#!/usr/bin/env python3

import os
import time
import random
import json
import requests
import socket

SPLUNK_HEC = os.getenv("SPLUNK_HEC")
SPLUNK_TOKEN = os.getenv("SPLUNK_TOKEN")
SOURCETYPE = os.getenv("SPLUNK_SOURCETYPE", "docker:app")
HOSTNAME = socket.gethostname()

headers = {"Authorization": f"Splunk {SPLUNK_TOKEN}"} if SPLUNK_TOKEN else None
HEC_ENDPOINT = SPLUNK_HEC

events = [
    {"level": "INFO", "msg": "User login successful", "user": "alice"},
    {"level": "WARN", "msg": "Failed password attempt", "user": "unknown"},
    {"level": "ERROR", "msg": "Unhandled exception in webapp", "module": "auth"},
    {"level": "INFO", "msg": "File uploaded", "user": "bob", "size": 12345},
    {"level": "INFO", "msg": "GET /index.html 200"},
    {"level": "WARN", "msg": "POST /login 401"},
    {"level": "INFO", "msg": "Scheduled job started", "job": "backup"},
]

def send_hec(ev):
    payload = {
        "time": ev.get("ts"),
        "host": ev.get("host"),
        "sourcetype": SOURCETYPE,
        "event": ev
    }
    try:
        r = requests.post(HEC_ENDPOINT, headers=headers, json=payload, timeout=5)
        if r.status_code >= 400:
            print(f"[HEC ERROR] status={r.status_code} resp={r.text}")
    except Exception as e:
        print("[HEC EXCEPTION]", str(e))

def main():
    while True:
        ev = random.choice(events).copy()
        ts = int(time.time())
        ev.update({
            "ts": ts,
            "host": HOSTNAME,
            "src_ip": f"10.0.0.{random.randint(2,250)}",
            "dest": random.choice(["dvwa", "web-proxy", "external.site"])
        })

        if HEC_ENDPOINT and SPLUNK_TOKEN:
            send_hec(ev)
        else:
            print(json.dumps(ev, ensure_ascii=False))

        time.sleep(0.6)

if __name__ == "__main__":
    main()
