# Configuration Files Guide

## Available Configurations

This project includes multiple YAML configuration files optimized for different use cases.

### General Purpose Configs

| Config File | Purpose | Personnel | Best For |
|------------|---------|-----------|----------|
| [config-acme.yaml](config-acme.yaml) | Interactive - choose your investigation type | 50+ employees | Stress testing, large investigations with focused scenarios |

**Note:** Config-acme-dense.yaml was removed in v2.0.0. Use the focused investigation configs below for smaller, targeted datasets.

### Focused Investigation Configs

| Config File | Investigation Type | Key Scenarios | Output Directory |
|------------|-------------------|---------------|------------------|
| [config-acme-antitrust.yaml](config-acme-antitrust.yaml) | Antitrust/Price-Fixing | S1, S1A, S1B + privilege + noise | demo_antitrust_investigation |
| [config-acme-safety-fraud.yaml](config-acme-safety-fraud.yaml) | Product Safety Fraud | S2 + privilege + noise | demo_product_safety_fraud |
| [config-acme-hr-misconduct.yaml](config-acme-hr-misconduct.yaml) | HR/Workplace Misconduct | (S_HR)* + privilege + noise | demo_hr_misconduct_investigation |

*Note: HR misconduct config requires adding (S_HR) tagged scenarios to your YAML

## Important: Privilege is Now Automatic

**Attorney-client privilege scenarios (S3) are now included with ALL investigation types**, not as a standalone option.

**Why?** In real e-discovery:
- Every investigation requires privilege screening
- Privilege review is a workflow step, not a case type
- You don't "investigate privilege" - you protect privileged communications
- EAIDA needs to identify privilege docs in any matter type

**What changed:**
- ~~config-acme-legal-privilege.yaml~~ (REMOVED)
- Privilege (S3) moved to contextual noise (S3-S15)
- All focused configs now include privilege automatically

## Which Config Should You Use?

### For EAIDA Demos

**Use the focused investigation configs** - they create realistic, single-scenario datasets:

- **Antitrust Demo:** Use `config-acme-antitrust.yaml`
  - Shows price-fixing collusion between competitors
  - Includes coded language and meeting coordination
  - **Plus privilege docs to screen** (realistic!)
  - Perfect for compliance training

- **Product Liability Demo:** Use `config-acme-safety-fraud.yaml`
  - Shows safety test manipulation and coverup
  - Includes falsified reports and evidence destruction
  - **Plus privilege docs to screen** (realistic!)
  - Perfect for regulatory violation scenarios

- **HR Investigation Demo:** Use `config-acme-hr-misconduct.yaml`
  - **Requires adding (S_HR) tagged scenarios first**
  - Would show harassment, discrimination, abuse of resources
  - **Plus privilege docs to screen** (realistic!)
  - Perfect for workplace investigations

### For Stress Testing

**Use `config-acme.yaml` with "All Scenarios Mixed" option:**
- 50+ personnel for high volume
- All scenario types mixed
- Stress test features (blast emails, large logs)
- Interactive selection when you run the tool

### For Training/Development

**Use the focused investigation configs:**
- Only 5 core custodians each
- Deep data (many emails per person)
- Single investigation type per config
- Easier to review and understand
- **Recommended:** config-acme-antitrust.yaml, config-acme-safety-fraud.yaml, or config-acme-hr-misconduct.yaml

## How to Use

1. Select a config file from the list above
2. When running `app.py`, choose the number corresponding to your config
3. Enter the number of items to generate
4. Choose chat format (Slack/Teams/Webex)
5. Run and wait for generation to complete

## Customizing Configs

All configs support these customizations:

### Change the Scenario Filter

Edit the `scenario_filter` line in any config:

```yaml
general_settings:
  scenario_filter: 'antitrust'  # Options: 'all', 'antitrust', 'safety_fraud', 'hr_misconduct'
```

### Change Output Directory

```yaml
general_settings:
  output_directory: "my_custom_dataset"
```

### Adjust Attachment Probabilities

```yaml
attachments:
  types:
    - name: "contract"
      probability: 0.5  # 50% chance of attachment
```

### Tune Signal/Noise Ratio

The "needle in haystack" ratio can be adjusted for realistic e-discovery testing:

**Target:** ~25% signal (hot docs) / 75% noise (contextual business communications)

**Current Ratios (with S4 duplicates + calendar events):**
- **config-acme-antitrust.yaml:** ~27% signal (6 signal / 22 total scenarios)
- **config-acme-safety-fraud.yaml:** ~40% signal (10 signal / 25 total scenarios)
- **config-acme-hr-misconduct.yaml:** ~48% signal (13 signal / 27 total scenarios)

**Notes:**
- **Antitrust:** Closest to target at ~27% signal (includes 1 calendar event)
- **Safety Fraud:** Higher at ~40% signal (includes 4 calendar events for investigation meetings)
- **HR Misconduct:** Highest at ~48% signal (includes 4 calendar events for investigation workflow)
- All three configs now include calendar (.ics) files for realistic investigation timelines
- Higher signal ratios still realistic for focused investigations vs. broad document collections

**To further adjust signal/noise ratio:**

**Option 1: Generate More Items (Recommended)**
```bash
# Generate 1500-2000 items instead of 500-1000
# Noise scenarios repeat more frequently, naturally diluting the ratio
python app.py
# Enter: 1500 (instead of 500)
```

**Option 2: Add More Noise Scenario Duplicates**

All focused configs use **YAML anchors** for efficient scenario duplication. S4 is duplicated 4x using:

```yaml
# Define once with anchor
- &noise_s4_template
  type: "standalone"
  description: "(S4) Generic project management emails"
  base_filename: "noise_project_mgmt"
  # ... full scenario definition ...

# Reuse with just filename changes
- <<: *noise_s4_template
  base_filename: "noise_project_mgmt_dup1"
```

To add more duplicates, follow the same pattern for other noise scenarios (S5-S13). Each duplicate lowers the signal ratio further.

## Quick Reference: Scenario Tags

| Tag | Description | Included In |
|-----|-------------|-------------|
| (S1) | Price-fixing email thread | config-acme-antitrust.yaml |
| (S1A) | Collusion meeting calendar invite | config-acme-antitrust.yaml |
| (S1B) | Teams/Slack pricing chat | config-acme-antitrust.yaml |
| (S2) | Safety test manipulation thread | config-acme-safety-fraud.yaml |
| (S2A-D) | **Safety investigation calendar events** | config-acme-safety-fraud.yaml |
| (S3) | **Attorney-client privilege** | **ALL focused configs (automatic)** |
| (S4-S15) | Contextual noise | ALL focused configs (automatic) |
| (S_HR) | HR misconduct scenarios | config-acme-hr-misconduct.yaml |
| (HR5-8) | **HR investigation calendar events** | config-acme-hr-misconduct.yaml |

## Examples

### Generate 200-item Antitrust Dataset with Privilege Screening
```bash
python app.py
# Select: config-acme-antitrust.yaml
# Enter: 200
# Format: Slack (or your preference)
```

**Result:** Price-fixing investigation emails + privilege docs to screen + business noise

### Generate 500-item Safety Fraud Dataset with Privilege Screening
```bash
python app.py
# Select: config-acme-safety-fraud.yaml
# Enter: 500
# Format: Teams
```

**Result:** Safety test manipulation emails + privilege docs to screen + R&D noise

### Generate All Scenarios (Stress Test)
```bash
python app.py
# Select: config-acme.yaml
# Enter: 1000
# Format: All
```

**Result:** Mixed antitrust, safety fraud, privilege, and noise scenarios

## Tips

1. **Start small** - Generate 50-100 items first to test
2. **Use focused configs for demos** - Single investigation per dataset
3. **Privilege is automatic** - Every focused config includes privilege docs
4. **Name outputs clearly** - Use descriptive folder names
5. **Test before presenting** - Verify scenarios match your needs

## Comparing Configs Side-by-Side

| Feature | config-acme.yaml | config-acme-antitrust.yaml | config-acme-safety-fraud.yaml |
|---------|------------------|---------------------------|------------------------------|
| Personnel | 50+ | 5 core | 5 core |
| Investigation Types | Interactive choice | Antitrust only | Safety fraud only |
| Privilege Docs | **Yes (automatic)** | **Yes (automatic)** | **Yes (automatic)** |
| Noise | **Yes (automatic)** | **Yes (automatic)** | **Yes (automatic)** |
| Best For | Large datasets, stress testing | Antitrust demos | Product liability demos |

## Need Help?

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Understand what the tool does, how it works, and why it matters
- **[README_SCENARIO_FILTERING.md](README_SCENARIO_FILTERING.md)** - Detailed filtering documentation
- **Check the comments in each YAML file** - Specific guidance for each config
- All configs use the same personnel and company structure (ACME Inc.)
- Privilege (S3) is now part of every focused investigation - no standalone filter needed
