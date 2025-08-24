import requests

MAX_RETRIES = 2
TIMEOUT = 5

def fetch_activity():
    url = "https://bored-api.appbrewery.com/random"
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        return {
            "id": data.get("key"),
            "activity": data.get("activity"),
            "type": data.get("type"),
            "participants": data.get("participants"),
            "price": data.get("price"),
            "accessibility": data.get("accessibility"),
            "link": data.get("link"),
        }
    except Exception:
        return None

def fetch_activities(n=20):
    ideas = []
    attempts = 0
    while len(ideas) < n and attempts < n * 5:
        idea = fetch_activity()
        attempts += 1
        if idea and idea["id"] not in {i["id"] for i in ideas}:
            ideas.append(idea)
    if len(ideas) < n:
        print(f"[WARN] Could only fetch {len(ideas)} unique ideas out of requested {n}.")
    return ideas