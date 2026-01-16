# Quick Start: Generate HR Harassment Investigation Dataset

## TL;DR

**To generate a workplace harassment investigation dataset for EAIDA testing:**

```bash
python app.py
```

1. Select: **config-acme-hr-misconduct.yaml**
2. Enter number of items: **100** (good starting point)
3. Choose chat format: **Slack** or **Teams** (or **All**)
4. Wait for generation to complete

**Output:** `demo_hr_misconduct_investigation/` folder

---

## What You'll Get

### Investigation Narrative

**Peyton Parker** (QA Specialist) reports workplace harassment to **Drew Foster** (General Counsel) about inappropriate behavior from **Jamie Chen** (Regional Sales Director).

### Key Evidence Types

1. **Initial Complaint Email** - Peyton reporting the issue to GC
2. **Detailed Incident Documentation** - Three specific incidents with dates
3. **Executive Communication** - GC escalating to CEO (Taylor Brooks)
4. **Investigation Approval** - CEO approving formal investigation
5. **Witness Statement** - Casey Mitchell corroborating the allegations
6. **HR Investigation Report** - Formal findings and recommendation
7. **Inappropriate Chat Logs** - Teams/Slack messages crossing boundaries
8. **Confrontation Email** - GC requesting meeting with accused

### Plus Realistic Context

- **Attorney-client privilege documents** (automatic) - for privilege screening practice
- **Business noise** - HR announcements, project emails, personal messages
- **Contextual communications** - Makes the investigation feel real

---

## Step-by-Step Instructions

### 1. Run the Generator

```bash
cd "c:\Users\651802\OneDrive - Epiq Inc\Files\Apps\synth data"
python app.py
```

### 2. Select HR Config

When you see the config list, choose the number for **config-acme-hr-misconduct.yaml**

Example:
```
Available configuration files:
1. config-acme.yaml
2. Config-acme-dense.yaml
3. config-acme-antitrust.yaml
4. config-acme-safety-fraud.yaml
5. config-acme-hr-misconduct.yaml  <-- Choose this one

Enter the number of your choice: 5
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

Enter your choice: 2
```

### 5. Wait for Generation

The script will:
- Load the config
- Apply the `hr_misconduct` filter
- Generate emails, chats, calendar invites, and documents
- Organize by custodian folders

You'll see output like:
```
[SCENARIO FILTER ACTIVE]: 'hr_misconduct'
  Total scenarios in config: 18
  Scenarios after filter: 16

Generating items...
```

---

## What Gets Generated

### Folder Structure

```
demo_hr_misconduct_investigation/
├── peyton.parker@acmeinc.com/
│   ├── S_HR_harassment_thread_001.eml  (Initial complaint)
│   ├── S_HR_harassment_thread_002.eml  (Detailed incidents)
│   ├── S_HR_complaint_meeting_001.ics  (Initial complaint meeting invite)
│   ├── S_HR_followup_meeting_001.ics   (Follow-up meeting invite)
│   └── noise_*.eml                     (Contextual emails)
├── drew.foster@acmeinc.com/
│   ├── S_HR_harassment_thread_003.eml  (Escalation to CEO)
│   ├── S_HR_investigation_docs_001.eml (HR report)
│   ├── S_HR_witness_interview_001.ics  (Witness interview invite)
│   ├── S_HR_executive_review_001.ics   (Executive review meeting)
│   └── S3_legal_privilege_*.eml        (Privilege docs)
├── jamie.chen@acmeinc.com/
│   ├── S_HR_harassment_thread_007.eml  (Defensive response)
│   ├── hr-inappropriate-chat.json      (Inappropriate Teams chat)
│   └── noise_*.eml
├── casey.mitchell@acmeinc.com/
│   ├── S_HR_witness_statement_001.eml  (Witness corroboration)
│   ├── S_HR_witness_interview_001.ics  (Witness interview invite)
│   └── noise_*.eml
└── taylor.brooks@acmeinc.com/
    ├── S_HR_harassment_thread_004.eml  (CEO response)
    ├── S_HR_executive_review_001.ics   (Executive decision meeting)
    └── noise_*.eml
```

### Key Evidence Files

| File Type | Description | Evidence Value |
|-----------|-------------|----------------|
| `S_HR_harassment_thread_*.eml` | Email thread documenting the complaint and investigation | **Hot document** |
| `S_HR_complaint_meeting_*.ics` | Initial complaint meeting calendar invite | **Hot document** |
| `S_HR_witness_interview_*.ics` | Witness interview meeting invite | **Hot document** |
| `S_HR_executive_review_*.ics` | Executive disciplinary decision meeting | **Hot document** |
| `S_HR_followup_meeting_*.ics` | Follow-up meeting with complainant | **Hot document** |
| `hr-inappropriate-chat.json` | After-hours chat with boundary violations | **Hot document** |
| `S_HR_witness_statement_*.eml` | Corroborating witness account | **Supporting evidence** |
| `S_HR_investigation_docs_*.eml` | Formal HR investigation findings | **Critical evidence** |
| `S3_legal_privilege_*.eml` | Attorney-client communications | **Privilege screening** |
| `noise_*.eml` | Business context emails | **Noise/context** |

---

## EAIDA Testing Use Cases

### 1. Hot Document Detection
**Test:** Can EAIDA identify the harassment complaint emails?

**Expected behavior:** EAIDA should flag emails with:
- Harassment allegations
- "Confidential HR Matter"
- Detailed incident descriptions
- Investigation recommendations

### 2. Pattern Recognition
**Test:** Can EAIDA find related communications across custodians?

**Expected behavior:** EAIDA should connect:
- Initial complaint (Peyton → Drew)
- Escalation (Drew → Taylor)
- Witness statement (Casey → Drew)
- Investigation report (Drew → Taylor)

### 3. Privilege Identification
**Test:** Can EAIDA distinguish privileged from non-privileged?

**Expected behavior:** EAIDA should identify:
- GC communications as potentially privileged
- External counsel emails as privileged
- HR investigation docs as business records (not privileged)

### 4. Chat Analysis
**Test:** Can EAIDA analyze inappropriate Teams/Slack messages?

**Expected behavior:** EAIDA should flag:
- After-hours personal messages
- Comments about appearance
- Requests for personal meetings/dates
- Pattern of boundary violations

---

## Customization Options

### Generate More HR Scenarios

Want additional harassment evidence? Increase the item count:

```
How many items to generate? 500
```

More items = more variations of the same scenario + more noise

### Add More Investigation Types

Edit [config-acme-hr-misconduct.yaml](config-acme-hr-misconduct.yaml) and change the filter:

```yaml
# Generate HR + Antitrust scenarios
scenario_filter: ['hr_misconduct', 'antitrust']
```

### Change Output Directory

Edit the config:

```yaml
general_settings:
  output_directory: "my_custom_hr_dataset"
```

---

## Troubleshooting

### "No scenarios match the filter!"

This means HR scenarios aren't in your config. **This has been fixed** - HR scenarios are now in:
- [config-acme.yaml](config-acme.yaml)
- [Config-acme-dense.yaml](Config-acme-dense.yaml)
- [config-acme-hr-misconduct.yaml](config-acme-hr-misconduct.yaml)

### Empty Dataset Generated

Make sure you selected **config-acme-hr-misconduct.yaml** (not an older version)

### Want Different Scenarios

The current scenarios cover workplace harassment. To add other HR issues:

1. Open the config file
2. Add new scenarios tagged with `(S_HR)`
3. Examples: discrimination, retaliation, time theft, expense fraud

---

## Quick Reference

**Generate 100-item HR harassment dataset:**
```bash
python app.py
# Choose: config-acme-hr-misconduct.yaml
# Items: 100
# Format: Teams
```

**Result:** Realistic HR investigation with harassment complaints, witness statements, investigation reports, inappropriate chats, privilege docs, and business noise.

**Perfect for:** Testing EAIDA's ability to identify workplace misconduct in early-stage investigations.

---

## Next Steps

1. **Generate the dataset** using the steps above
2. **Load into EAIDA** using your normal import process
3. **Test hot document detection** - Can EAIDA find the harassment complaint?
4. **Test relationship mapping** - Does EAIDA connect Peyton → Drew → Taylor?
5. **Test privilege screening** - Does EAIDA flag GC communications?
6. **Test chat analysis** - Does EAIDA identify inappropriate Teams messages?

---

## Learn More

Want to understand how the generation system works?
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Complete guide to system architecture, design decisions, and extension options
- **[CONFIGS_GUIDE.md](CONFIGS_GUIDE.md)** - All configuration file options explained
- **[README.md](README.md)** - Main documentation with troubleshooting and advanced usage

Good luck with your EAIDA testing!
