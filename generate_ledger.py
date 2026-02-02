import json
import blake3
from datetime import datetime

def generate_ledger():
    # Simulated Agent Actions
    actions = [
        {"agent": "Henry", "task": "DEPLOY: A2AC_ENTERPRISE -> CLOUD_RUN", "type": "OPS", "tokens_saved": 1250},
        {"agent": "Sentinel", "task": "VERIFY: DOMAIN_MAPPING 'a2ac.ai'", "type": "SEC", "tokens_saved": 300},
        {"agent": "Pulse", "task": "INGEST: GITHUB_REPOS (Q-SDK)", "type": "DATA", "tokens_saved": 4500},
        {"agent": "Sidewinder", "task": "SCAN: COLLISION_DETECTION", "type": "SEC", "tokens_saved": 120},
        {"agent": "Biographer", "task": "UPDATE: GLASS_SERVER_UI", "type": "DOCS", "tokens_saved": 850},
        {"agent": "Henry", "task": "REFAC: PHYSICS.PY -> BLAKE3", "type": "CODE", "tokens_saved": 600}
    ]

    ledger = []
    
    for action in actions:
        # Create a verifiable hash using BLAKE3
        # Payload = Agent + Task + Timestamp (Simulated as current for freshness)
        timestamp = datetime.utcnow().isoformat() + "Z"
        payload = f"{action['agent']}:{action['task']}:{timestamp}"
        
        # BLAKE3 Hash
        action_hash = blake3.blake3(payload.encode()).hexdigest()
        
        entry = {
            "hash": action_hash,
            "agent": action["agent"],
            "task": action["task"],
            "type": action["type"],
            "timestamp": timestamp,
            "tokens_saved": action["tokens_saved"],
            "status": "VERIFIED"
        }
        ledger.append(entry)

    # Write to ledger.json
    with open('ledger.json', 'w') as f:
        json.dump(ledger, f, indent=2)
    
    print(f"Generated {len(ledger)} blocks with BLAKE3 hashes.")

if __name__ == "__main__":
    generate_ledger()
