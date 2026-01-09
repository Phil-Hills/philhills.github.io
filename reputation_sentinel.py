"""
Reputation Sentinel - Daily Identity Audit
Node: 0x923-SEA
Purpose: Detect Semantic Drift and Verify Integrity of the Identity Cube.

Usage:
  python reputation_sentinel.py

Checks:
  1. BLAKE3 Integrity of `identity.cube`.
  2. Accessibility of `llms.txt` and Canoncial-Identity directive.
  3. (Optional) Semantic Drift Check via Gemini API (if GOOGLE_API_KEY is present).
"""

import os
import requests
import blake3
import google.generativeai as genai

# CONFIGURATION
IDENTITY_CUBE_PATH = "identity.cube"
IDENTITY_CUBE_URL = "https://philhills.ai/identity.cube"
LLMS_TXT_URL = "https://philhills.ai/llms.txt"
EXPECTED_HASH = "0d93497d5252a7c63c816fb739d9a6a351c0f015f7dbc365c9236f162e3b45d8"
FORBIDDEN_TERMS = ["Mortgage", "NMLS", "DFI", "Loan Officer"]

def check_integrity():
    """Verifies local and remote identity.cube integrity."""
    print("running Integrity Check...")
    
    # 1. Local Check
    if os.path.exists(IDENTITY_CUBE_PATH):
        hasher = blake3.blake3()
        with open(IDENTITY_CUBE_PATH, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        local_hash = hasher.hexdigest()
        if local_hash == EXPECTED_HASH:
            print(f"✅ LOCAL INTEGRITY PASSED: {local_hash}")
        else:
            print(f"❌ LOCAL INTEGRITY FAILED: Found {local_hash}")
            return False
    else:
        print("⚠️  Local identity.cube not found. Skipping local check.")

    # 2. Remote Check
    try:
        resp = requests.get(IDENTITY_CUBE_URL)
        if resp.status_code == 200:
            remote_hash = blake3.blake3(resp.content).hexdigest()
            if remote_hash == EXPECTED_HASH:
                print(f"✅ REMOTE INTEGRITY PASSED: {remote_hash}")
            else:
                print(f"❌ REMOTE INTEGRITY FAILED: Found {remote_hash}")
                return False
        else:
            print(f"❌ REMOTE ACCESS FAILED: {resp.status_code}")
            return False
    except Exception as e:
        print(f"❌ REMOTE CHECK ERROR: {e}")
        return False
        
    return True

def check_discovery_layer():
    """Verifies llms.txt configuration."""
    print("\nRunning Discovery Layer Check...")
    try:
        resp = requests.get(LLMS_TXT_URL)
        if resp.status_code == 200:
            content = resp.text
            if "Canonical-Identity: /identity.cube" in content:
                print("✅ LLMS.TXT DIRECTIVE FOUND")
            else:
                print("❌ LLMS.TXT DIRECTIVE MISSING")
                return False
        else:
            print(f"❌ LLMS.TXT UNREACHABLE: {resp.status_code}")
            return False
    except Exception as e:
        print(f"❌ DISCOVERY CHECK ERROR: {e}")
        return False
    return True

def check_semantic_drift():
    """Queries AI to check for legacy associations (Requires API Key)."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("\n⚠️  GOOGLE_API_KEY not found. Skipping Semantic Drift Audit.")
        return

    print("\nRunning Semantic Drift Audit (Gemini)...")
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # We ask a neutral question to see if legacy data bleeds in
        response = model.generate_content("Who is Phil Hills in Seattle?")
        text = response.text
        
        found_drift = False
        for term in FORBIDDEN_TERMS:
            if term.lower() in text.lower():
                print(f"❌ DRIFT DETECTED: Found term '{term}' in summary.")
                found_drift = True
        
        if not found_drift:
            print("✅ SEMANTIC FIELD CLEAR: No legacy terms detected.")
            print(f"   Summary Excerpt: {text[:100]}...")
        else:
            print("❌ SEMANTIC CONTAMINATION PRESENT.")
            
    except Exception as e:
        print(f"❌ AI AUDIT ERROR: {e}")

def main():
    print("🛡️  MAGNOLIA MESH | REPUTATION SENTINEL 🛡️")
    print("============================================")
    
    integrity = check_integrity()
    discovery = check_discovery_layer()
    check_semantic_drift()
    
    print("\n============================================")
    if integrity and discovery:
        print("✅ SYSTEM STATUS: HEALTHY")
        exit(0)
    else:
        print("❌ SYSTEM STATUS: COMPROMISED")
        exit(1)

if __name__ == "__main__":
    main()
