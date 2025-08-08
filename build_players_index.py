import json, requests, time
r = requests.get("https://api.sleeper.app/v1/players/nfl", timeout=120)
r.raise_for_status()
raw = r.json()
out = []
for pid, p in raw.items():
    name = p.get("full_name") or f"{p.get('first_name','')} {p.get('last_name','')}".strip()
    out.append({
        "id": pid,
        "full_name": name,
        "position": p.get("position",""),
        "team": p.get("team",""),
        "bye_week": p.get("bye_week",""),
        "active": bool(p.get("active")),
        "years_exp": p.get("years_exp"),
        "injury_status": p.get("injury_status",""),
        "updated_at": int(time.time())
    })
with open("players_index.json","w") as f: json.dump(out, f)
print(f"Wrote {len(out)} players to players_index.json")
