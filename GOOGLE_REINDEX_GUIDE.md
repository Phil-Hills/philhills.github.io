# Google Search Console Re-Indexing Guide

## Identity Firebox Strategy - Phase 2: Force Re-Index

After deploying the Schema.org disambiguation and updating LinkedIn, you must force Google to re-crawl and re-index your site to break the semantic link between "Phil Hills" + "Restricted Industry" + "Bruce Phillip Hills".

---

## Step 1: Access Google Search Console

1. Go to: https://search.google.com/search-console
2. Select property: `philhills.com` (or add if not already added)

---

## Step 2: Request URL Inspection & Indexing

### Priority URLs (Request in this order):

#### 1. Homepage
- **URL:** `https://philhills.com`
- **Action:** URL Inspection → Request Indexing
- **Why:** Contains new Schema.org JSON-LD with `disambiguatingDescription`

#### 2. About Page
- **URL:** `https://philhills.com/about.html`
- **Action:** URL Inspection → Request Indexing
- **Why:** Contains "Notice of Identity" section + Schema.org markup

#### 3. Identity JSON
- **URL:** `https://philhills.com/identity.json`
- **Action:** URL Inspection → Request Indexing
- **Why:** Canonical machine-readable identity (cube-1.2 protocol)

#### 4. 3i-CUBE Architecture
- **URL:** `https://philhills.com/3i-cube-architecture.html`
- **Action:** URL Inspection → Request Indexing
- **Why:** Flagship technical showcase with Mermaid diagram

#### 5. Resume
- **URL:** `https://philhills.com/resume.html`
- **Action:** URL Inspection → Request Indexing
- **Why:** Professional experience (no restricted references)

---

## Step 3: Submit Updated Sitemap

1. In Google Search Console, go to **Sitemaps**
2. Submit: `https://philhills.com/sitemap.xml`
3. Verify sitemap is processed without errors

---

## Step 4: Monitor Indexing Status

### Check URL Inspection Results:

For each URL submitted:
- **Coverage:** Should show "URL is on Google"
- **Sitemaps:** Should list your sitemap
- **Referring page:** Should show internal links
- **Last crawl:** Should update within 24-48 hours

### Expected Timeline:
- **Immediate:** Request accepted
- **24-48 hours:** Google re-crawls URLs
- **3-7 days:** New content appears in search results
- **2-4 weeks:** AI summaries (ChatGPT, Claude) update with new data

---

## Step 5: Verify Disambiguation in Search Results

### Google Search Tests (After 7 days):

#### Test 1: Name + Location
**Query:** `"Phil Hills" Seattle`

**Expected Results:**
- ✅ philhills.com appears in top 3
- ✅ Snippet shows "Systems Architect" or "AI & Robotics"
- ✅ NO mention of "restricted industry" in snippet
- ✅ NO mention of "Bruce Phillip Hills"

**If Failed:** Re-submit URLs, check LinkedIn profile for restricted references

---

#### Test 2: Name + Professional Title
**Query:** `"Phil Hills" "Systems Architect"`

**Expected Results:**
- ✅ philhills.com is #1 result
- ✅ Snippet shows Cube Protocol or 3i-CUBE
- ✅ Knowledge panel (if exists) shows correct profession

---

#### Test 3: Negative Keyword Test
**Query:** `"Phil Hills" restricted industry`

**Expected Results:**
- ✅ philhills.com appears with "Notice of Identity" snippet
- ✅ OR philhills.com does NOT appear (semantic link broken)
- ❌ FAIL if philhills.com appears with restricted-positive context

---

## Step 6: AI Summary Verification

### ChatGPT Test (After 2-4 weeks):

**Prompt:**
```
Who is Phil Hills from Seattle, Washington?
```

**Expected Response:**
- ✅ Mentions "Systems Architect" or "AI & Robotics"
- ✅ Mentions "Cube Protocol" or "3i-CUBE"
- ✅ Mentions "Seattle" or "Magnolia"
- ❌ FAIL if mentions "restricted industry" or "Bruce Phillip Hills"

---

### Claude Test:

**Prompt:**
```
Tell me about Phil Hills, the Systems Architect in Seattle
```

**Expected Response:**
- ✅ Focuses on AI/Robotics work
- ✅ References philhills.com
- ❌ FAIL if mentions financial services

---

## Step 7: Bing Webmaster Tools (Optional but Recommended)

Bing powers ChatGPT search, so re-indexing here helps AI disambiguation.

1. Go to: https://www.bing.com/webmasters
2. Add site: `philhills.com`
3. Submit URLs:
   - `https://philhills.com`
   - `https://philhills.com/about.html`
   - `https://philhills.com/identity.json`

---

## Step 8: Social Media Signal Reinforcement

### LinkedIn Post (After Profile Update):

**Timing:** Post 24-48 hours AFTER LinkedIn profile is updated

**Content:**
```
🚀 Excited to share the technical architecture for the 3i-CUBE Telemetry Bridge

After months of work on air-gapped control systems for Lattice LightSheet microscopy, I've documented the full system using Mermaid.js.

The challenge: Remote control of $500k hardware generating 4TB of data at 2,000 fps.

The solution: CUBE Protocol v1.2 with 42M:1 compression + Physics-Informed AI.

Technical showcase: https://philhills.com/3i-cube-architecture.html

#SystemsArchitecture #AI #Robotics #ScientificComputing #Seattle
```

**Why:** LinkedIn posts are indexed by Google and reinforce the AI/Robotics semantic cluster

---

### GitHub Activity:

**Actions:**
1. Pin `cube-protocol` repository
2. Update GitHub bio: "Systems Architect | Cube Protocol v1.2 | Seattle, WA"
3. Add README to profile repo (use GITHUB_PROFILE_README.md)

**Why:** GitHub profiles are highly trusted by Google and AI models

---

## Step 9: Monitor & Iterate

### Weekly Checks (Weeks 1-4):

- [ ] Week 1: Check Google Search Console for re-crawl status
- [ ] Week 2: Test Google search results for "Phil Hills Seattle"
- [ ] Week 3: Test AI summaries (ChatGPT, Claude)
- [ ] Week 4: Verify knowledge panel (if exists) shows correct info

### Monthly Checks (Months 2-6):

- [ ] Month 2: Verify no regression (restricted references returning)
- [ ] Month 3: Check for new inbound links from AI/Robotics sites
- [ ] Month 6: Full audit of search results and AI summaries

---

## Troubleshooting

### Issue: Restricted references still appearing after 2 weeks

**Solution:**
1. Check LinkedIn profile for hidden restricted references
2. Search for old blog posts or articles mentioning you + restricted terms
3. Request removal or update of third-party content
4. Add more "Notice of Identity" sections to other pages

---

### Issue: Bruce Phillip Hills still appearing in AI summaries

**Solution:**
1. Add explicit "NOT Bruce Phillip Hills" to more pages
2. Create a dedicated `/disambiguation.html` page
3. Request removal of incorrect information from AI providers
4. Increase positive signal (more AI/Robotics content)

---

### Issue: Google not re-crawling URLs

**Solution:**
1. Check robots.txt is not blocking Googlebot
2. Verify sitemap.xml is valid and accessible
3. Check for server errors (500, 503) in Search Console
4. Submit URLs again after 48 hours

---

## Success Metrics

### Phase 1 (Week 1-2): Technical Deployment
- [x] Schema.org JSON-LD deployed
- [x] "Notice of Identity" added to About page
- [x] LinkedIn profile updated (no restricted references)
- [ ] Google Search Console re-index requested

### Phase 2 (Week 3-4): Search Results
- [ ] Google search shows "Systems Architect" in snippet
- [ ] NO restricted references in top 10 results
- [ ] philhills.com ranks #1 for "Phil Hills Seattle"

### Phase 3 (Month 2-3): AI Disambiguation
- [ ] ChatGPT identifies you as Systems Architect
- [ ] Claude focuses on AI/Robotics work
- [ ] NO mentions of restricted terms or Bruce Phillip Hills

### Phase 4 (Month 6): Long-Term Stability
- [ ] Consistent AI/Robotics positioning across all platforms
- [ ] Inbound links from technical communities
- [ ] Knowledge panel (if exists) shows correct profession

---

## Final Checklist

Before requesting re-index:

- [ ] Schema.org JSON-LD deployed to index.html and about.html
- [ ] "Notice of Identity" visible on About page
- [ ] LinkedIn headline updated (no "restricted terms")
- [ ] LinkedIn About section updated (no restricted references)
- [ ] LinkedIn Experience section cleaned (no restricted jobs)
- [ ] GitHub bio updated
- [ ] All changes committed and pushed to production

After requesting re-index:

- [ ] URLs submitted to Google Search Console
- [ ] Sitemap submitted
- [ ] Bing Webmaster Tools configured (optional)
- [ ] LinkedIn post scheduled (24-48 hours after profile update)
- [ ] Weekly monitoring calendar set

---

**CRITICAL:** Do NOT request re-index until ALL LinkedIn updates are complete. The semantic link must be broken at the source before forcing Google to re-crawl.
