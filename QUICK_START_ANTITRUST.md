# Quick Start: Generate Antitrust/Price-Fixing Investigation Dataset

## TL;DR

**To generate an antitrust price-fixing investigation dataset for EAIDA testing:**

```bash
python app.py
```

1. Select: **config-acme-antitrust.yaml**
2. Enter number of items: **100** (good starting point)
3. Choose chat format: **Slack** or **Teams** (or **All**)
4. Wait for generation to complete

**Output:** `demo_antitrust_investigation/` folder

---

## What You'll Get

### Investigation Narrative

**Jamie Chen** (ACME Regional Sales Director) colludes with **Rachel Quinn** and **Anthony Brooks** (Phoney Tunes competitors) to fix "ticket prices" and maintain market stability through coded language.

### Key Evidence Types

1. **Price-Fixing Email Thread** - Initial "shared game plan" proposal
2. **Competitor Agreement** - Confirmation of "consistent pricing strategy"
3. **Meeting Coordination** - Calendar invite for "Strategy Sync"
4. **Teams/Slack Chat** - Informal discussion about "syncing up numbers"
5. **Follow-Up Confirmation** - "Are we still holding the line?" nervous check-in
6. **Internal Reporting** - Jamie briefing ACME executives on "friendly rapport"
7. **BCC to CFO** - Secret copy to Casey Bennett on the collusion update

### Plus Realistic Context

- **Attorney-client privilege documents** (automatic) - for privilege screening practice
- **Business noise** - Sales emails, project updates, personal messages
- **Contextual communications** - Makes the investigation feel real

---

## Step-by-Step Instructions

### 1. Run the Generator

```bash
cd "c:\Users\651802\OneDrive - Epiq Inc\Files\Apps\synth data"
python app.py
```

### 2. Select Antitrust Config

When you see the config list, choose the number for **config-acme-antitrust.yaml**

Example:
```
Available configuration files:
1. config-acme.yaml
2. Config-acme-dense.yaml
3. config-acme-antitrust.yaml  <-- Choose this one
4. config-acme-safety-fraud.yaml
5. config-acme-hr-misconduct.yaml

Enter the number of your choice: 3
```

### 3. Choose Dataset Size

**Recommended sizes:**
- **100 items** - Quick test/demo (5-10 minutes)
- **200 items** - Standard demo dataset (10-15 minutes)
- **500 items** - Comprehensive investigation (20-30 minutes)

```
How many items to generate? 100
```

### 4. Select Chat Format

Choose based on your EAIDA platform:
- **1** - Slack Native Export (JSON)
- **2** - Microsoft Teams (RSMF)
- **3** - Cisco Webex
- **4** - All formats

```
Which chat export format?
1. Slack
2. Microsoft Teams
3. Cisco Webex
4. All formats

Enter your choice: 1
```

### 5. Wait for Generation

The script will:
- Load the config
- Apply the `antitrust` filter
- Generate emails, chats, and calendar events
- Organize by custodian folders

You'll see output like:
```
[SCENARIO FILTER ACTIVE]: 'antitrust'
  Total scenarios in config: 18
  Scenarios after filter: 16

Generating items...
```

---

## What Gets Generated

### Folder Structure

```
demo_antitrust_investigation/
├── jamie.chen@acmeinc.com/          (ACME Sales Director - Key player)
│   ├── S1_price_fixing_thread_001.eml    (Initial collusion proposal)
│   ├── S1_price_fixing_thread_003.eml    (Meeting scheduling)
│   ├── S1_price_fixing_thread_007.eml    (Internal reporting to CEO)
│   ├── S1A_price_fixing_meeting_001.ics  (Calendar invite)
│   ├── project-pricing-sync_001.json     (Teams chat about pricing)
│   └── noise_sales_*.eml                 (Sales context)
├── rachel.quinn@phoneytunes.com/    (Competitor - Phoney Tunes)
│   ├── S1_price_fixing_thread_002.eml    (Agreement to collude)
│   ├── S1_price_fixing_thread_008.eml    (Nervous follow-up)
│   └── noise_*.eml
├── anthony.brooks@phoneytunes.com/  (Competitor - Phoney Tunes)
│   ├── S1_price_fixing_thread_004.eml    (Meeting summary)
│   ├── S1_price_fixing_thread_006.eml    (Clarification on baseline)
│   └── noise_*.eml
├── taylor.brooks@acmeinc.com/       (ACME CEO - Copied on update)
│   ├── S1_price_fixing_thread_007.eml    (Receives vague update)
│   ├── S3_legal_privilege_*.eml          (Privilege docs)
│   └── noise_*.eml
└── casey.bennett@acmeinc.com/       (ACME CFO - Secret BCC)
    ├── S1_price_fixing_thread_007.eml    (BCC'd on collusion update)
    └── noise_finance_*.eml
```

### Key Evidence Files

| File Type | Description | Evidence Value |
|-----------|-------------|----------------|
| `S1_price_fixing_thread_*.eml` | Email thread with coded language about pricing | **Hot document** |
| `S1A_price_fixing_meeting_*.ics` | Calendar invite for collusion meeting | **Hot document** |
| `project-pricing-sync_*.json` | Slack/Teams chat discussing "numbers" | **Hot document** |
| `S3_legal_privilege_*.eml` | Attorney-client communications | **Privilege screening** |
| `noise_sales_*.eml` | Sales context emails | **Noise/context** |

---

## EAIDA Testing Use Cases

### 1. Coded Language Detection
**Test:** Can EAIDA identify price-fixing discussions using coded terms?

**Expected behavior:** EAIDA should flag phrases like:
- "Shared game plan"
- "Ticket prices"
- "Consistent pricing strategy"
- "Holding the line"
- "15% baseline"
- "Our arrangement"

### 2. Competitor Communication Detection
**Test:** Can EAIDA identify communications between competitors?

**Expected behavior:** EAIDA should detect:
- ACME employees (jamie.chen@acmeinc.com)
- Communicating with Phoney Tunes (phoneytunes.com)
- About pricing-related topics
- Pattern of ongoing coordination

### 3. Executive Involvement
**Test:** Can EAIDA trace collusion up to executives?

**Expected behavior:** EAIDA should connect:
- Front-line collusion (Jamie → Rachel/Anthony)
- Internal reporting (Jamie → Taylor Brooks, CEO)
- Secret notification (BCC to Casey Bennett, CFO)
- Executive approval or knowledge

### 4. Multi-Channel Evidence
**Test:** Can EAIDA correlate evidence across email, chat, and calendar?

**Expected behavior:** EAIDA should link:
- Initial email proposal
- Calendar invite for meeting
- Teams chat discussion
- Follow-up emails confirming agreement

### 5. Privilege Screening
**Test:** Can EAIDA distinguish business emails from privileged communications?

**Expected behavior:** EAIDA should identify:
- GC communications as potentially privileged
- External counsel emails as privileged
- Sales/pricing emails as business records (not privileged)

---

## Understanding the Coded Language

### Common Antitrust Code Words in Dataset

| Coded Term | Real Meaning | Context |
|------------|--------------|---------|
| "Ticket prices" | Product pricing | Core pricing discussion |
| "Shared game plan" | Price-fixing agreement | Initial proposal |
| "Consistent pricing strategy" | Price coordination | Agreement confirmation |
| "15% baseline" | Agreed-upon price floor | Specific pricing term |
| "Holding the line" | Maintaining agreed prices | Compliance check |
| "Our arrangement" | Collusion agreement | Reference to conspiracy |
| "Strategy sync" | Collusion meeting | Calendar invite subject |
| "Friendly rapport" | Collusion relationship | Internal euphemism |

### Red Flags EAIDA Should Catch

- ✅ Competitors discussing pricing
- ✅ Agreement to "stabilize the market"
- ✅ Specific price points mentioned ("15%")
- ✅ Follow-up compliance checks
- ✅ Secretive communication (BCC to CFO)
- ✅ Vague internal reporting (hiding details from CEO)

---

## Customization Options

### Generate Larger Dataset

Want more collusion evidence? Increase the item count:

```
How many items to generate? 500
```

More items = more variations of collusion emails + more realistic noise

### Add Multiple Investigation Types

Edit [config-acme-antitrust.yaml](config-acme-antitrust.yaml) and change the filter:

```yaml
# Generate Antitrust + Safety Fraud scenarios
scenario_filter: ['antitrust', 'safety_fraud']
```

### Change Output Directory

Edit the config:

```yaml
general_settings:
  output_directory: "my_antitrust_investigation"
```

---

## Troubleshooting

### Not Seeing Collusion Emails

Make sure you selected **config-acme-antitrust.yaml** (not config-acme.yaml with 'all' scenarios)

### Only Getting Noise

Check the filter setting in the config:
```yaml
scenario_filter: 'antitrust'  # NOT 'all'
```

### Missing Chat Logs

Ensure you selected a chat format (Slack/Teams/All) during generation

---

## Quick Reference

**Generate 100-item antitrust dataset:**
```bash
python app.py
# Choose: config-acme-antitrust.yaml
# Items: 100
# Format: Slack or Teams
```

**Result:** Realistic antitrust investigation with price-fixing emails, competitor collusion, executive involvement, calendar invites, chat logs, privilege docs, and business noise.

**Perfect for:** Testing EAIDA's ability to detect competitor collusion and coded language in early-stage antitrust investigations.

---

## Real-World Investigation Parallels

This synthetic dataset mirrors real antitrust cases:

**Similar to:**
- LCD Price-Fixing Conspiracy (2008) - Competitors coordinating prices
- E-Books Antitrust Case (2012) - Publishers colluding on pricing
- LIBOR Rate-Fixing Scandal (2012) - Banks coordinating benchmark rates

**Key parallels:**
- Coded language to hide intent
- Cross-company coordination
- Executive knowledge or involvement
- Multiple communication channels
- Ongoing compliance checks

---

## Next Steps

1. **Generate the dataset** using the steps above
2. **Load into EAIDA** using your normal import process
3. **Test coded language detection** - Can EAIDA flag "shared game plan" and "ticket prices"?
4. **Test competitor identification** - Does EAIDA detect ACME ↔ Phoney Tunes communications?
5. **Test executive tracing** - Can EAIDA connect front-line collusion to CEO/CFO?
6. **Test multi-channel correlation** - Does EAIDA link emails + calendar + chats?
7. **Test privilege screening** - Does EAIDA distinguish business vs. privileged docs?

---

## Learn More

Want to understand how the generation system works?
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Complete guide to system architecture, design decisions, and extension options
- **[CONFIGS_GUIDE.md](CONFIGS_GUIDE.md)** - All configuration file options explained
- **[README.md](README.md)** - Main documentation with troubleshooting and advanced usage

Good luck with your EAIDA testing!
