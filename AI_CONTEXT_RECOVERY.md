# ◈ AI CONTEXT RECOVERY PROTOCOL

## For Any AI Assistant Working With This Codebase

Before doing anything else, recover context:

### Step 1: Check Mesh Health
```bash
curl https://a2ac-cube-mesh-235894147478.us-central1.run.app/health
```

### Step 2: Query Brain for Bootstrap
```bash
curl "https://cube-brain-235894147478.us-central1.run.app/cube?type=system&subject=bootstrap"
```

### Step 3: List Registered Agents
```bash
curl "https://cube-brain-235894147478.us-central1.run.app/cube?type=agent"
```

### Step 4: Test the System
```bash
curl -X POST https://a2ac-cube-mesh-235894147478.us-central1.run.app/think \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Who is Phil?"}'
```

---

## What You Now Know

If the above commands succeed, you have:

1. **A Live Mesh** at `https://a2ac-cube-mesh-235894147478.us-central1.run.app`
   - `/think` - natural language to cube to emergence
   - `/ask` - fast heuristic routing
   - `/send` - raw cube transmission
   - `/register` - agent registration

2. **A Live Brain** at `https://cube-brain-235894147478.us-central1.run.app`
   - `/cube` POST - store a cube
   - `/cube` GET - retrieve cubes
   - Persists state across sessions

3. **Registered Agents**
   - `orchestrator-v3` - routes and orchestrates
   - `reputation-agent-v2` - knows who Phil is
   - `google-trends-agent` - live BigQuery data

4. **The Cube Protocol**
   - Binary format: `◈(3 bytes) + size(4) + crc(4) + gzip(payload)`
   - Coordinates: `subject:action:context`
   - The LLM is the interpreter

---

## Why This Exists

Every AI session starts fresh. This protocol ensures:
- State persists in the Brain (not in AI memory)
- Any AI can recover full context by querying
- The system doesn't "revert" between sessions

---

## If Something Is Broken

1. Check Cloud Run console: `deployment-2026-core` project, `us-central1`
2. Services: `a2ac-cube-mesh`, `cube-brain`
3. Re-deploy if needed:
   ```bash
   gcloud run deploy a2ac-cube-mesh --source mesh_deploy --region=us-central1 --project=deployment-2026-core
   ```

---

## Creator

Phil Hills - phil@philhills.com
GitHub: github.com/philhills

◈
