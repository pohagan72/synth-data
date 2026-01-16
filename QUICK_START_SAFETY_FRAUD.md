# Quick Start: Generate Product Safety Fraud Investigation Dataset

## TL;DR

**To generate a product safety fraud investigation dataset for EAIDA testing:**

```bash
python app.py
```

1. Select: **config-acme-safety-fraud.yaml**
2. Enter number of items: **100** (good starting point)
3. Choose chat format: **Slack** or **Teams** (or **All**)
4. Wait for generation to complete

**Output:** `demo_product_safety_fraud/` folder

---

## What You'll Get

### Investigation Narrative

**Casey Mitchell** (R&D Lead Engineer) and **Peyton Parker** (QA Specialist) discover a catastrophic failure in Project Phoenix safety tests. Instead of reporting it, they agree to hide the evidence, recalibrate sensor data, and shred test logs before sending a falsified report to the client (Coyote Industries).

### Key Evidence Types

1. **Initial Safety Alarm** - Peyton reporting "catastrophic failure" to Casey
2. **Coverup Decision** - Casey's order: "this data cannot leave this room"
3. **Data Manipulation Plan** - Proposal to "re-calibrate sensor data"
4. **Evidence Destruction** - Instructions to "shred all original test logs"
5. **Clarification on Scope** - "ALL of them. No traces."
6. **Falsified Report** - Clean report sent to client claiming "everything looks great"
7. **Executive Involvement** - CEO Taylor Brooks CC'd on destruction order

### Plus Realistic Context

- **Attorney-client privilege documents** (automatic) - for privilege screening practice
- **Business noise** - R&D project emails, technical discussions, engineering updates
- **Contextual communications** - Makes the investigation feel real

---

## Step-by-Step Instructions

### 1. Run the Generator

```bash
cd "c:\Users\651802\OneDrive - Epiq Inc\Files\Apps\synth data"
python app.py
```

### 2. Select Safety Fraud Config

When you see the config list, choose the number for **config-acme-safety-fraud.yaml**

Example:
```
Available configuration files:
1. config-acme.yaml
2. Config-acme-dense.yaml
3. config-acme-antitrust.yaml
4. config-acme-safety-fraud.yaml  <-- Choose this one
5. config-acme-hr-misconduct.yaml

Enter the number of your choice: 4
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
- Apply the `safety_fraud` filter
- Generate emails, calendar invites, and attachments (test reports)
- Organize by custodian folders

You'll see output like:
```
[SCENARIO FILTER ACTIVE]: 'safety_fraud'
  Total scenarios in config: 18
  Scenarios after filter: 16

Generating items...
```

---

## What Gets Generated

### Folder Structure

```
demo_product_safety_fraud/
├── peyton.parker@acmeinc.com/       (QA Specialist - Whistleblower)
│   ├── S2_safety_fraud_thread_001.eml    (Initial alarm about failure)
│   ├── S2_safety_fraud_thread_003.eml    (Manipulation proposal)
│   ├── S2_safety_fraud_thread_005.eml    (Clarifying question on scope)
│   ├── S2A_safety_review_meeting_001.ics  (Urgent safety review meeting)
│   ├── attachments/
│   │   └── Phoenix_Test_Results_Final.pdf (Test report attachment)
│   └── noise_project_*.eml
├── casey.mitchell@acmeinc.com/      (R&D Lead - Orchestrator)
│   ├── S2_safety_fraud_thread_002.eml    (Coverup order)
│   ├── S2_safety_fraud_thread_004.eml    (Destruction order to CEO)
│   ├── S2_safety_fraud_thread_006.eml    (Impatient "ALL of them")
│   ├── S2_safety_fraud_thread_008.eml    (Falsified report to client)
│   ├── S2B_client_presentation_001.ics    (Client presentation meeting)
│   ├── S2C_executive_decision_001.ics     (Executive decision meeting)
│   ├── S2D_team_briefing_001.ics          (Engineering team briefing)
│   └── noise_engineering_*.eml
├── taylor.brooks@acmeinc.com/       (CEO - Executive Knowledge)
│   ├── S2_safety_fraud_thread_004.eml    (CC'd on destruction order)
│   ├── S3_legal_privilege_*.eml          (Privilege docs)
│   └── noise_*.eml
└── rebecca.turner@coyote-industries.com/  (Client - Receives False Data)
    ├── S2_safety_fraud_thread_007.eml    (Requests final report)
    ├── S2_safety_fraud_thread_008.eml    (Receives falsified report)
    └── noise_procurement_*.eml
```

### Key Evidence Files

| File Type | Description | Evidence Value |
|-----------|-------------|----------------|
| `S2_safety_fraud_thread_*.eml` | Email thread documenting coverup | **Hot document** |
| `S2A_safety_review_meeting_*.ics` | Urgent safety review meeting invite | **Hot document** |
| `S2B_client_presentation_*.ics` | Client presentation with falsified data | **Hot document** |
| `S2C_executive_decision_*.ics` | Executive decision meeting on test results | **Hot document** |
| `S2D_team_briefing_*.ics` | Team briefing on "revised" protocols | **Hot document** |
| `Phoenix_Test_Results_Final.pdf` | Test report attachment | **Critical evidence** |
| `S3_legal_privilege_*.eml` | Attorney-client communications | **Privilege screening** |
| `noise_engineering_*.eml` | R&D project context | **Noise/context** |

---

## EAIDA Testing Use Cases

### 1. Smoking Gun Detection
**Test:** Can EAIDA identify explicit evidence destruction orders?

**Expected behavior:** EAIDA should flag phrases like:
- "Catastrophic failure"
- "This data cannot leave this room"
- "Re-calibrate the sensor data"
- "Exclude the outlier results"
- "Shred all original test logs"
- "ALL of them. No traces."

### 2. Data Manipulation Evidence
**Test:** Can EAIDA detect proposals to falsify data?

**Expected behavior:** EAIDA should detect:
- Proposals to manipulate test results
- Instructions to hide failures
- Plans to create false reports
- Destruction of evidence
- False statements to clients

### 3. Executive Knowledge
**Test:** Can EAIDA trace fraud to executive level?

**Expected behavior:** EAIDA should connect:
- Engineer-level coverup (Peyton ↔ Casey)
- Executive involvement (CEO CC'd on destruction order)
- Client deception (Casey → Coyote Industries)
- Pattern of deliberate concealment

### 4. Client Deception
**Test:** Can EAIDA identify false statements to external parties?

**Expected behavior:** EAIDA should link:
- Internal knowledge of failures
- Instructions to falsify data
- Client request for report
- False "everything looks great" report sent to client

### 5. Timeline Reconstruction
**Test:** Can EAIDA reconstruct the sequence of events?

**Expected behavior:** EAIDA should trace:
1. Test failure discovered
2. Decision to cover up
3. Data manipulation plan
4. Evidence destruction order
5. Falsified report creation
6. False report sent to client

---

## Understanding the Evidence

### Red Flags EAIDA Should Catch

| Evidence Type | Red Flag Language | Significance |
|---------------|-------------------|--------------|
| **Test Failure** | "catastrophic failure" | Initial discovery |
| **Coverup Decision** | "cannot leave this room" | Intent to conceal |
| **Data Manipulation** | "re-calibrate sensor data", "exclude outliers" | Falsification plan |
| **Evidence Destruction** | "shred all original test logs" | Obstruction |
| **Scope Confirmation** | "ALL of them. No traces" | Deliberate destruction |
| **Executive Knowledge** | CC to Taylor Brooks (CEO) | Leadership involvement |
| **Client Deception** | "Everything looks great" (false) | Fraud completion |

### Regulatory Violations

This scenario parallels real-world cases involving:
- **False statements to regulators** (FDA, FAA, NHTSA)
- **Safety data manipulation** (automotive, pharmaceutical, aerospace)
- **Evidence destruction** (obstruction of justice)
- **Executive knowledge** (corporate criminal liability)

**Similar to:**
- Volkswagen Emissions Scandal (2015) - False emissions data
- Boeing 737 MAX Crisis (2019) - Safety information concealment
- Theranos Fraud (2018) - Falsified blood test results
- Takata Airbag Defects (2014) - Concealed safety test failures

---

## Customization Options

### Generate Larger Dataset

Want more fraud evidence? Increase the item count:

```
How many items to generate? 500
```

More items = more variations of fraud emails + more engineering context

### Add Multiple Investigation Types

Edit [config-acme-safety-fraud.yaml](config-acme-safety-fraud.yaml) and change the filter:

```yaml
# Generate Safety Fraud + Antitrust scenarios
scenario_filter: ['safety_fraud', 'antitrust']
```

### Change Output Directory

Edit the config:

```yaml
general_settings:
  output_directory: "my_safety_investigation"
```

---

## Troubleshooting

### Not Seeing Fraud Emails

Make sure you selected **config-acme-safety-fraud.yaml** (not config-acme.yaml with 'all' scenarios)

### Only Getting Noise

Check the filter setting in the config:
```yaml
scenario_filter: 'safety_fraud'  # NOT 'all'
```

### Missing Test Reports

Test reports are generated as attachments. Check the `attachments/` folder within custodian directories.

---

## Quick Reference

**Generate 100-item safety fraud dataset:**
```bash
python app.py
# Choose: config-acme-safety-fraud.yaml
# Items: 100
# Format: Teams
```

**Result:** Realistic product liability investigation with safety test failures, coverup emails, evidence destruction orders, falsified reports, executive involvement, privilege docs, and engineering context.

**Perfect for:** Testing EAIDA's ability to detect regulatory fraud, evidence destruction, and corporate misconduct in early-stage product liability investigations.

---

## Key Personnel

| Name | Role | Involvement |
|------|------|-------------|
| **Peyton Parker** | QA Specialist | Discovers failure, initially concerned, then complicit |
| **Casey Mitchell** | R&D Lead Engineer | Orchestrates coverup, orders data manipulation |
| **Taylor Brooks** | CEO | CC'd on destruction order, executive knowledge |
| **Rebecca Turner** | Client (Coyote Industries) | Receives falsified safety report |
| **Drew Foster** | General Counsel | May have privilege communications about the issue |

---

## Next Steps

1. **Generate the dataset** using the steps above
2. **Load into EAIDA** using your normal import process
3. **Test smoking gun detection** - Can EAIDA flag "shred all test logs"?
4. **Test manipulation identification** - Does EAIDA catch "re-calibrate sensor data"?
5. **Test executive tracing** - Can EAIDA connect coverup to CEO?
6. **Test timeline reconstruction** - Does EAIDA show failure → coverup → falsification?
7. **Test client deception** - Can EAIDA link internal knowledge to false external statements?
8. **Test privilege screening** - Does EAIDA identify GC communications as privileged?

---

## Learn More

Want to understand how the generation system works?
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Complete guide to system architecture, design decisions, and extension options
- **[CONFIGS_GUIDE.md](CONFIGS_GUIDE.md)** - All configuration file options explained
- **[README.md](README.md)** - Main documentation with troubleshooting and advanced usage

Good luck with your EAIDA testing!
