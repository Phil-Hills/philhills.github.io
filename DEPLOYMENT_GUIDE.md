# Deep Tech Portfolio Deployment Guide

## Pre-Deployment Verification

### 1. Local Visual Inspection

Start a local server to review all changes:

```bash
cd /Users/SoundComputer/philhills/ai-summary-cube/portfolio_site
python3 -m http.server 8000
```

Open in browser: `http://localhost:8000`

**Pages to Review:**
- ✅ **Homepage** (`index.html`)
  - Hero: "Phil Hills // Systems Architect"
  - Subtitle: "I build protocols for high-velocity data"
  - Core Technology section features CUBE Protocol v1.2 (primary)
  - Applications section positions 3i-CUBE as "Case Study"
  
- ✅ **Projects** (`projects.html`)
  - Title: "Deep Tech Projects"
  - Featured: 3i-CUBE Bridge, Cube Protocol v1.2, AI Summary Cube
  - Core Technologies: Air-Gapped Proxy, Z-Order Compression, Physics-Informed Synthetic Data
  - NO fintech references

- ✅ **About** (`about.html`)
  - Opens with "Based in the Magnolia neighborhood of Seattle"
  - References TruFusion for personal discipline
  - Current Focus: 3i-CUBE, Synthetic Data, Seattle Tech Ecosystem

- ✅ **Resume** (`resume.html`)
  - Professional Summary emphasizes Scientific Telemetry, Physics-Informed AI
  - Skill categories: Robotics & Scientific Computing, Physics-Informed AI, Security & Verification
  - Top project: 3i-CUBE Telemetry Bridge

### 2. Link Validation

Test all critical links:

```bash
# 3i-CUBE Bridge
curl -I https://service-3i-cube-intelligent-imaging-control-768405504263.us-west1.run.app

# Cube Protocol GitHub
curl -I https://github.com/Phil-Hills/cube-protocol

# AI Summary Cube
curl -I https://cube-protocol-app-422805462249.us-central1.run.app

# Identity JSON
curl https://philhills.com/identity.json
```

### 3. Content Audit Checklist

**Fintech/Marketing References (MUST BE REMOVED):**
- [ ] "Restricted Organizations" - VERIFY REMOVED
- [ ] "Client journeys" - VERIFY REMOVED
- [ ] "Fintech" - VERIFY REMOVED
- [ ] "Marketing automation" - VERIFY REMOVED
- [ ] "Financial Dataset Cubes" - VERIFY REMOVED

**Deep Tech Keywords (MUST BE PRESENT):**
- [ ] Scientific Telemetry
- [ ] Physics-Informed AI
- [ ] Quantum-Ready Data Structures
- [ ] Air-Gapped Proxy Pattern
- [ ] Z-Order Spatial Compression
- [ ] BLAKE3 Cryptographic Hashing
- [ ] Lattice LightSheet Microscopy
- [ ] Magnolia, Seattle

---

## Deployment Steps

### Step 1: Commit Changes

```bash
cd /Users/SoundComputer/philhills/ai-summary-cube/portfolio_site

# Check status
git status

# Review changes
git diff

# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Deep Tech reconstruction: System & Applications architecture

- Updated identity.json with Seattle-native positioning
- Created philhills_project_state.json for AI agent context
- Restructured homepage: Core Technology + Applications sections
- Positioned CUBE Protocol v1.2 as primary technology
- Moved 3i-CUBE to Applications as flagship case study
- Updated all pages with Deep Tech positioning
- Removed all fintech/marketing references
- Added Magnolia/TruFusion context for local Seattle presence"
```

### Step 2: Push to GitHub

```bash
# Push to main branch
git push origin main

# Verify push succeeded
git log -1
```

### Step 3: Monitor GitHub Pages Deployment

GitHub Pages should automatically deploy after push. Monitor at:
- Repository: https://github.com/Phil-Hills/philhills.github.io
- Actions tab: Check workflow status

**Expected workflow:**
1. GitHub Actions triggers on push
2. Builds site
3. Deploys to `gh-pages` branch
4. Site live at https://philhills.com

---

## Post-Deployment Verification

### 1. Live Site Checks

```bash
# Verify homepage
curl -I https://philhills.com

# Verify identity.json
curl https://philhills.com/identity.json | python3 -m json.tool

# Check canonical URLs
curl https://philhills.com | grep "canonical"
```

### 2. Visual Verification

Open in browser: https://philhills.com

**"Genius Friend" Test:**
- [ ] First impression: "Systems Architect" (not fintech)
- [ ] Hero section emphasizes CUBE Protocol
- [ ] 3i-CUBE positioned as case study, not primary brand
- [ ] NO mentions of "marketing automation"

**Technical Credibility Audit:**
- [ ] Bio leads with Magnolia, Seattle location
- [ ] References TruFusion for personal discipline
- [ ] Tech stack features Rust, BLAKE3, Z-Order Curves
- [ ] Projects page showcases scientific computing

### 3. Mobile Responsiveness

Test on mobile device:
- [ ] Hero section readable
- [ ] Project cards stack properly
- [ ] Navigation works
- [ ] No horizontal scrolling

### 4. Cross-Browser Testing

Test in:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari

---

## Post-Deployment Actions

### 1. Update External Profiles

**LinkedIn:**
- Update headline to: "AI & Robotics Systems Architect"
- Update summary to match new bio (Magnolia, Seattle focus)

**GitHub Profile:**
- Update bio to: "Systems Architect | CUBE Protocol v1.2 | Scientific Telemetry & Robotics"
- Pin repositories: cube-protocol, ai-summary-cube

**Twitter/X (if applicable):**
- Update bio to match new positioning

### 2. Search Engine Updates

**Google Search Console:**
```bash
# Submit updated sitemap
# URL: https://search.google.com/search-console
# Submit: https://philhills.com/sitemap.xml
```

**IndexNow:**
```bash
# Notify search engines of update
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "philhills.com",
    "key": "YOUR_INDEXNOW_KEY",
    "urlList": [
      "https://philhills.com/",
      "https://philhills.com/about.html",
      "https://philhills.com/projects.html",
      "https://philhills.com/resume.html",
      "https://philhills.com/identity.json"
    ]
  }'
```

### 3. Verify AI Agent Scraping

Test how AI agents interpret the site:

**ChatGPT/Claude Test:**
Ask: "What does Phil Hills do professionally?"

**Expected Response:**
- Should mention "Systems Architect"
- Should reference CUBE Protocol v1.2
- Should mention 3i-CUBE as case study
- Should reference Magnolia, Seattle location
- Should NOT mention fintech or marketing

---

## Rollback Plan (If Needed)

If issues are discovered post-deployment:

```bash
cd /Users/SoundComputer/philhills/ai-summary-cube/portfolio_site

# View commit history
git log --oneline

# Rollback to previous commit
git revert HEAD

# Or reset to specific commit
git reset --hard <commit-hash>

# Force push (use with caution)
git push origin main --force
```

---

## Success Metrics

### Immediate (24-48 hours)
- [ ] Site loads correctly at philhills.com
- [ ] All internal links work
- [ ] identity.json returns valid JSON
- [ ] No console errors in browser DevTools

### Short-term (1-2 weeks)
- [ ] Google Search Console shows updated pages indexed
- [ ] AI agents (ChatGPT, Claude) correctly describe Phil as "Systems Architect"
- [ ] No references to fintech/marketing in AI-generated summaries

### Long-term (1-3 months)
- [ ] Search results for "Phil Hills" emphasize Robotics/Deep Tech
- [ ] LinkedIn profile views from Robotics/AI industry
- [ ] Inbound inquiries reference CUBE Protocol or 3i-CUBE

---

## Troubleshooting

### Issue: GitHub Pages not deploying

**Solution:**
1. Check GitHub Actions tab for errors
2. Verify `CNAME` file contains: `philhills.com`
3. Check repository settings > Pages > Source is set to `gh-pages` branch

### Issue: identity.json not accessible

**Solution:**
1. Verify file is in root directory
2. Check `.gitignore` doesn't exclude `.json` files
3. Verify CORS headers allow cross-origin requests

### Issue: Styles not loading

**Solution:**
1. Hard refresh browser: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
2. Clear browser cache
3. Verify `style.css` path is correct in HTML files

---

## Contact for Issues

If deployment issues persist:
- GitHub Issues: https://github.com/Phil-Hills/philhills.github.io/issues
- Check GitHub Pages status: https://www.githubstatus.com/

---

## Deployment Complete Checklist

- [ ] Local visual inspection passed
- [ ] All links validated
- [ ] Content audit passed (no fintech references)
- [ ] Changes committed to git
- [ ] Pushed to GitHub
- [ ] GitHub Pages deployment succeeded
- [ ] Live site verified
- [ ] Mobile responsiveness confirmed
- [ ] Cross-browser testing passed
- [ ] External profiles updated
- [ ] Search engines notified
- [ ] AI agent scraping verified

**Once all items checked, deployment is COMPLETE.**
