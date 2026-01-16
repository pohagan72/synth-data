# Synthetic E-Discovery Dataset Generator

Generate realistic email, chat, and document datasets for testing e-discovery tools like EAIDA. Create focused investigation scenarios with authentic evidence, contextual noise, and privilege screening challenges.

## 🚀 Quick Start Guides

**New to this tool? Start here:**

| Investigation Type | Quick Start Guide | Best For |
|-------------------|-------------------|----------|
| 🏢 **Antitrust/Price-Fixing** | [QUICK_START_ANTITRUST.md](QUICK_START_ANTITRUST.md) | Competitor collusion, coded language detection |
| ⚠️ **Product Safety Fraud** | [QUICK_START_SAFETY_FRAUD.md](QUICK_START_SAFETY_FRAUD.md) | Regulatory fraud, evidence destruction |
| 👥 **HR Misconduct** | [QUICK_START_HR_HARASSMENT.md](QUICK_START_HR_HARASSMENT.md) | Workplace harassment, hostile environment |

**Each guide includes:**
- Step-by-step instructions
- EAIDA testing use cases
- Evidence type explanations
- Customization options
- Troubleshooting tips

---

## What This Tool Does

Generates synthetic e-discovery datasets with:

✅ **Realistic Communications**
- RFC-compliant emails (.eml)
- Slack/Teams/Webex chat logs
- Calendar invites (.ics)
- Email threading and metadata

✅ **Focused Investigation Scenarios**
- Antitrust price-fixing
- Product safety fraud
- Workplace harassment
- (Extensible to other scenarios)

✅ **Authentic Evidence**
- Hot documents with smoking gun language
- Witness statements
- Executive involvement
- Multi-custodian coordination

✅ **Privilege Screening Challenges**
- Attorney-client communications (automatic)
- External counsel emails
- Mixed privileged/non-privileged content

✅ **Realistic Context**
- Business noise (HR announcements, project emails)
- Personal communications
- Meeting scheduling
- Sales chatter

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- Azure OpenAI API access (for LLM-generated content)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Azure OpenAI

Set environment variables or update the config:

```bash
export AZURE_OPENAI_API_KEY="your-key-here"
export AZURE_OPENAI_ENDPOINT="your-endpoint-here"
```

---

## Usage

### Basic Usage

```bash
python app.py
```

1. **Select a config file** - Choose investigation type
2. **Enter item count** - How many emails/chats to generate
3. **Choose chat format** - Slack, Teams, Webex, or All
4. **Wait for generation** - ~1 minute per 100 items (parallel execution)

### Using config-acme.yaml (Interactive Mode)

When you select config-acme.yaml, you'll be prompted to choose your investigation type:

```bash
python app.py

# 1. Select config-acme.yaml
# 2. Enter item count (e.g., 500)
# 3. Choose chat format

# You'll then see:
================================================================================
You selected config-acme.yaml (Master Configuration with All Scenarios)
================================================================================

This config contains ALL investigation types mixed together.
For realistic investigation testing, you should focus on ONE investigation type.

[Investigation Type Selection]
Which investigation type do you want to generate?

  1: Antitrust / Price-Fixing Investigation
  2: Product Safety Fraud Investigation
  3: HR / Workplace Harassment Investigation
  4: All Scenarios Mixed (Infrastructure Stress Testing)
  5: Custom Combination

# Choose your option (1-5)
# The tool will then generate only the selected investigation type(s)
```

**Result:** You get a focused dataset using the large 50+ custodian roster, perfect for testing EAIDA with realistic organizational scale.

### Available Configurations

#### Corporate Investigations

| Config File | Investigation | Personnel | Output Directory |
|------------|---------------|-----------|------------------|
| [config-acme-antitrust.yaml](config-acme-antitrust.yaml) | Price-fixing | 50 (5 core + 45 expansion) | demo_antitrust_investigation |
| [config-acme-safety-fraud.yaml](config-acme-safety-fraud.yaml) | Safety fraud | 50 (5 core + 45 expansion) | demo_product_safety_fraud |
| [config-acme-hr-misconduct.yaml](config-acme-hr-misconduct.yaml) | HR harassment | 50 (5 core + 45 expansion) | demo_hr_misconduct_investigation |
| [config-acme.yaml](config-acme.yaml) | **Interactive** - Choose your type | 50+ | ediscovery_dataset_stress_test |

#### Healthcare Investigations

| Config File | Investigation | Personnel | Output Directory |
|------------|---------------|-----------|------------------|
| [config-hospital-hipaa-breach.yaml](config-hospital-hipaa-breach.yaml) | HIPAA data breach | 50 (5 core + 45 expansion) | demo_hipaa_breach_investigation |
| [config-hospital-billing-fraud.yaml](config-hospital-billing-fraud.yaml) | Medicare/Medicaid fraud | 50 (5 core + 45 expansion) | demo_billing_fraud_investigation |
| [config-hospital-patient-harm.yaml](config-hospital-patient-harm.yaml) | Medical malpractice coverup | 50 (5 core + 45 expansion) | demo_patient_harm_investigation |

**Note on config-acme.yaml:** When you select this config, you'll be prompted to choose which investigation type(s) to generate:
- Antitrust only
- Safety fraud only
- HR misconduct only
- All scenarios mixed (for infrastructure stress testing)
- Custom combination

This allows you to use the large personnel roster (50+ custodians) with focused investigation scenarios.

---

## Documentation

### For New Users

- **[QUICK_START_ANTITRUST.md](QUICK_START_ANTITRUST.md)** - Generate antitrust datasets
- **[QUICK_START_SAFETY_FRAUD.md](QUICK_START_SAFETY_FRAUD.md)** - Generate safety fraud datasets
- **[QUICK_START_HR_HARASSMENT.md](QUICK_START_HR_HARASSMENT.md)** - Generate HR misconduct datasets

### For Advanced Users

- **[CONFIGS_GUIDE.md](CONFIGS_GUIDE.md)** - All configuration options explained
- **[README_SCENARIO_FILTERING.md](README_SCENARIO_FILTERING.md)** - Detailed filtering documentation

### Architecture & System Design

- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Comprehensive architecture guide (what it does, how it works, why it matters)
- **[ENHANCEMENTS_2026-01.md](ENHANCEMENTS_2026-01.md)** - Technical details on v2.0.0 enhancements
- **[app.py](app.py)** - Main application logic
- **Config YAML files** - Scenario definitions and personnel

---

## Example Outputs

### Antitrust Investigation (100 items, ~15 minutes)

```
demo_antitrust_investigation/
├── jamie.chen@acmeinc.com/
│   ├── S1_price_fixing_thread_001.eml  (Collusion proposal)
│   ├── project-pricing-sync_001.json   (Teams chat)
│   └── noise_sales_*.eml               (Business context)
├── rachel.quinn@phoneytunes.com/
│   ├── S1_price_fixing_thread_002.eml  (Agreement)
│   └── noise_*.eml
└── taylor.brooks@acmeinc.com/
    ├── S1_price_fixing_thread_007.eml  (Executive update)
    ├── S3_legal_privilege_*.eml        (Privilege docs)
    └── noise_*.eml
```

### Safety Fraud Investigation (100 items, ~15 minutes)

```
demo_product_safety_fraud/
├── peyton.parker@acmeinc.com/
│   ├── S2_safety_fraud_thread_001.eml  (Initial alarm)
│   ├── S2_safety_fraud_thread_003.eml  (Manipulation proposal)
│   └── attachments/
│       └── Phoenix_Test_Results_Final.pdf
├── casey.mitchell@acmeinc.com/
│   ├── S2_safety_fraud_thread_002.eml  (Coverup order)
│   ├── S2_safety_fraud_thread_004.eml  (Destruction order)
│   └── noise_engineering_*.eml
└── taylor.brooks@acmeinc.com/
    ├── S2_safety_fraud_thread_004.eml  (CEO CC'd)
    └── S3_legal_privilege_*.eml
```

### HR Harassment Investigation (100 items, ~15 minutes)

```
demo_hr_misconduct_investigation/
├── peyton.parker@acmeinc.com/
│   ├── S_HR_harassment_thread_001.eml  (Complaint to GC)
│   ├── S_HR_harassment_thread_002.eml  (Incident details)
│   └── noise_*.eml
├── drew.foster@acmeinc.com/
│   ├── S_HR_harassment_thread_003.eml  (Escalation to CEO)
│   ├── S_HR_investigation_docs_001.eml (HR report)
│   └── S3_legal_privilege_*.eml
├── jamie.chen@acmeinc.com/
│   ├── hr-inappropriate-chat.json      (Teams chat logs)
│   └── noise_*.eml
└── casey.mitchell@acmeinc.com/
    ├── S_HR_witness_statement_001.eml  (Corroboration)
    └── noise_*.eml
```

### HIPAA Breach Investigation (100 items, ~15 minutes)

```
demo_hipaa_breach_investigation/
├── p.williams@metrogenhospital.org/
│   ├── S_HIPAA_breach_thread_001.eml  (Breach discovery)
│   ├── S_HIPAA_A_exfiltration_001.eml (Forensic evidence)
│   └── attachments/
│       └── Patient_Access_Logs_March_2024.csv
├── m.chen@metrogenhospital.org/
│   ├── S_HIPAA_E_teams_chat_001.json  (Late night panic)
│   └── noise_it_helpdesk_*.eml
└── d.foster@metrogenhospital.org/
    ├── S_HIPAA_B_delayed_notification_001.eml  (Coverup debate)
    ├── S3_legal_privilege_*.eml                (Attorney-client)
    └── noise_*.eml
```

### Billing Fraud Investigation (100 items, ~15 minutes)

```
demo_billing_fraud_investigation/
├── r.brennan@riversideregional.org/
│   ├── S_FRAUD_thread_001.eml         (Upcoding scheme)
│   ├── S_FRAUD_A_kickback_001.eml     (Device vendor kickback)
│   └── attachments/
│       └── Upcoding_Analysis_Q4_2023.xlsx
├── s.walsh@riversideregional.org/
│   ├── S_FRAUD_C_pressure_001.eml     (Pressure on billing staff)
│   ├── S_FRAUD_F_teams_chat_001.json  ("Code creatively")
│   └── noise_billing_*.eml
└── t.harper@riversideregional.org/
    ├── S_FRAUD_D_evidence_destruction_001.eml  (Coverup)
    └── S3_legal_privilege_*.eml
```

### Medical Malpractice Investigation (100 items, ~15 minutes)

```
demo_patient_harm_investigation/
├── dr.hart@stcatherines-health.org/
│   ├── S_HARM_thread_001.eml          (Wrong-site surgery)
│   ├── S_HARM_F_calendar_001.ics      (Secret meeting)
│   └── noise_*.eml
├── dr.chen@stcatherines-health.org/
│   ├── S_HARM_A_incident_report_001.eml  (Initial concerns)
│   ├── S_HARM_B_falsify_records_001.eml  (Pressured to alter)
│   └── attachments/
│       └── Surgical_Log_March_15_2024_ORIGINAL.pdf
└── p.vasquez@stcatherines-health.org/
    ├── S_HARM_C_evidence_destruction_001.eml  (Destroy originals)
    ├── S_HARM_D_intimidation_001.eml          (Witness threats)
    └── S3_legal_privilege_*.eml
```

---

## Features

### 🆕 Recent Enhancements (v2.0 - January 2026)

#### Email-Attachment Content Alignment
Attachments now align with email narratives. If an email says "see attached report showing catastrophic failure", the attachment will actually contain that failure data. This dramatically improves realism for testing content correlation in EAIDA.

#### Scenario-Aware Temporal Logic
Timestamps now reflect realistic investigation patterns:
- **Fraud scenarios:** Fast panic replies (30 min - 4 hours) OR deliberate delays (24-72 hours)
- **Urgent emails:** Quick responses based on content (keywords: urgent, ASAP, critical)
- **Friday evening → Monday morning:** 70% of Friday 5pm+ emails wait until Monday 8-10 AM
- **Business hours:** 80% during 8 AM - 6 PM, fraud scenarios extend to 11 PM

#### Enhanced Privilege Scenarios
Privilege screening now tests realistic detection challenges:
- **Subtle privilege:** No "PRIVILEGED" markers - requires understanding context (e.g., "Need your advice on pricing discussions" to GC)
- **Privilege by recipient:** Business emails to General Counsel become privileged when seeking legal guidance
- **Mixed privilege threads:** Email threads that start as business discussions and become privileged mid-conversation
- **Privilege waiver:** Privileged emails improperly forwarded to non-attorneys (tests waiver understanding)

#### Chat Realism Improvements
Modern workplace messaging patterns for Slack, Teams, and Webex:
- **Rapid-fire messages:** Short 1-3 sentence messages sent seconds apart ("hey", "checking", "got it") instead of email paragraphs
- **Emoji and reactions:** 👍 reactions on short confirmations (30%), multiple users reacting (1-3 per message)
- **Realistic timing:** 5-30 sec gaps for short messages, 1-5 min for thoughtful responses
- **Edit history:** 10% of longer messages show edit timestamps (typo fixes)
- **Thread support:** Infrastructure for threaded conversations branching from main channel

#### Parallel Execution with Rate Limiting
Fast dataset generation with intelligent API rate limit handling:
- **Performance:** 7-10x speedup using 10 parallel workers (500 items in ~6 minutes vs ~50 minutes)
- **Rate limit protection:** Automatic retry with exponential backoff for 429 errors (2s, 4s, 8s, 16s, 32s)
- **Configurable:** Adjust `MAX_WORKERS` in app.py (line 1777) based on your Azure OpenAI quota
- **Thread-safe:** Protected stats and counters for concurrent execution

#### Signal/Noise Ratio Tuning
Adjust the "needle in haystack" ratio for realistic e-discovery testing:
- **Target:** ~25% signal (hot docs) / 75% noise (business context)
- **Current ratios:** Antitrust ~27%, Safety Fraud ~40%, HR ~48% (all include calendar events)
- **How to adjust:** Generate 1500-2000 items instead of 500 (noise repeats more), or duplicate noise scenarios in config YAML
- **See:** [CONFIGS_GUIDE.md](CONFIGS_GUIDE.md#tune-signalnoise-ratio) for detailed tuning instructions

See [CHANGELOG.md](CHANGELOG.md) and [ENHANCEMENTS_2026-01.md](ENHANCEMENTS_2026-01.md) for details.

---

### Realistic Metadata

- **Email headers** - From, To, Cc, Bcc, Date, Message-ID
- **Threading** - In-Reply-To and References headers
- **Timestamps** - Scenario-aware business hours, realistic patterns
- **Signatures** - Role-appropriate email signatures

### Multi-Format Support

- **Email** - RFC-compliant .eml files
- **Slack** - Native JSON export format
- **Microsoft Teams** - RSMF format
- **Cisco Webex** - API JSON format
- **Calendar** - .ics event files

### Smart Content Generation

- **LLM-powered** - Uses Azure OpenAI for contextually realistic content
- **Persona-aware** - Each person has unique communication style
- **Context-driven** - Emails reference company projects and personnel
- **Near-duplicates** - Automatic generation for deduplication testing

### Attachments

- **PDFs** - Contracts, test reports, presentations
- **Office docs** - Word documents, Excel spreadsheets
- **Log files** - Debug logs, server logs (configurable size)
- **Context-aware** - Attachments match scenario types

---

## Scenario Filtering

Generate focused datasets for specific investigation types.

### Interactive Filter Selection (config-acme.yaml)

When you select **config-acme.yaml**, the tool will automatically prompt you to choose which investigation type(s) to generate:

```
[Investigation Type Selection]
Which investigation type do you want to generate?

  1: Antitrust / Price-Fixing Investigation
  2: Product Safety Fraud Investigation
  3: HR / Workplace Harassment Investigation
  4: All Scenarios Mixed (Infrastructure Stress Testing)
  5: Custom Combination
```

**Benefits:**
- Use the large 50+ custodian roster with focused scenarios
- Generate realistic investigations without manual config editing
- Choose stress testing mode (all scenarios mixed) when needed
- Create custom combinations for specific testing needs

### Manual Filter Configuration (YAML)

For focused configs, the filter is pre-set in the YAML file:

```yaml
# In your config YAML file
general_settings:
  scenario_filter: 'antitrust'  # or 'safety_fraud', 'hr_misconduct', 'all'
```

**How it works:**
- `'antitrust'` - Only price-fixing scenarios + privilege + noise
- `'safety_fraud'` - Only safety fraud scenarios + privilege + noise
- `'hr_misconduct'` - Only HR scenarios + privilege + noise
- `'all'` - All investigation types mixed together
- `['antitrust', 'safety_fraud']` - Multiple types combined

**Why filtering matters:**
- Focused datasets for specific demo/testing needs
- Realistic investigation scope (one matter type per dataset)
- Cleaner training data for EAIDA
- Attorney-client privilege automatically included with all filters

See [README_SCENARIO_FILTERING.md](README_SCENARIO_FILTERING.md) for details.

---

## Use Cases

### EAIDA Testing

Perfect for testing:
- Hot document detection
- Pattern recognition across custodians
- Privilege screening accuracy
- Coded language identification
- Timeline reconstruction
- Relationship mapping
- Multi-channel correlation (email + chat + calendar)

### E-Discovery Training

Use for:
- Review workflow training
- Privilege identification practice
- Early case assessment demos
- Tool evaluation and comparison
- Performance benchmarking

### Research & Development

Useful for:
- Machine learning model training
- NLP algorithm testing
- Deduplication algorithm validation
- Thread reconstruction evaluation
- Sentiment analysis testing

---

## Customization

### Add New Scenarios

Edit the YAML config to add custom scenarios:

```yaml
scenarios:
  - type: "thread"
    description: "(S_CUSTOM) Your custom scenario"
    base_filename: "custom_scenario"
    prompts:
      - prompt_templates:
          - "Your email generation prompt here"
```

Tag with `(S_HR)`, `(S1)`, etc. to enable filtering.

### Add New Personnel

Extend the `company_profiles` section:

```yaml
personnel:
  - name: "New Person"
    title: "Job Title"
    email: "new.person@company.com"
    style: "Communication style description"
    signature: "Email signature"
```

### Adjust Probabilities

Control how often scenarios appear:

```yaml
prompts:
  - prompt_templates:
      - "Your prompt"
    probability: 0.5  # 50% chance of appearing
```

---

## Troubleshooting

### "No scenarios match the filter!"

- Check spelling: `'antitrust'` not `'anti-trust'`
- Verify YAML syntax (proper quotes and spacing)
- Ensure config has scenarios with matching tags

### Empty or Small Dataset

- Increase item count (try 200-500 items)
- Check scenario probabilities in config
- Verify scenario_filter is not too restrictive

### LLM Generation Errors

- Check Azure OpenAI API key and endpoint
- Verify rate limits aren't exceeded
- Ensure prompts are well-formed in YAML

### Slow Generation

- Reduce item count for testing
- All configs now use 50 personnel for realistic organizational depth
- LLM API calls are the bottleneck (normal)

---

## Contributing

### Adding New Investigation Types

1. Create scenarios in YAML with unique tag (e.g., `(S_NEW)`)
2. Add tag to `scenario_mappings` in [app.py](app.py#L131-135)
3. Create focused config file (e.g., `config-acme-newtype.yaml`)
4. Write quick start guide (e.g., `QUICK_START_NEWTYPE.md`)
5. Update this README

### Improving Existing Scenarios

1. Edit prompts in YAML config files
2. Test with small dataset (50-100 items)
3. Verify output quality
4. Document changes in config comments

---

## Technical Details

### File Formats

- **Email**: RFC 2822 compliant .eml files
- **Chat (Slack)**: Native JSON export format with channels and threads
- **Chat (Teams)**: RSMF (Rich Site Summary Format) XML
- **Chat (Webex)**: JSON API response format
- **Calendar**: iCalendar .ics files (RFC 5545)
- **Attachments**: Real file types (PDF, DOCX, XLSX) or mathematical placeholders for large files

### Custodian Organization

Files organized by email address:

```
output_directory/
├── person1@company.com/
│   ├── emails/
│   ├── chats/
│   └── attachments/
└── person2@company.com/
    └── ...
```

### Metadata Standards

- **Message-ID**: RFC 2822 compliant unique identifiers
- **Threading**: In-Reply-To and References headers for proper threading
- **Timestamps**: Realistic business hours (9 AM - 6 PM, weekdays)
- **Domains**: Realistic company domains (acmeinc.com, phoneytunes.com, etc.)

---

## License & Disclaimer

**This tool generates synthetic data for testing purposes only.**

- Not real communications
- Fictional companies and personnel
- For e-discovery tool testing and training
- Do not use for malicious purposes

---

## Support

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Questions**: See documentation files in this directory
- **Quick Start**: Use the `QUICK_START_*.md` guides for specific scenarios

---

## Summary

This tool helps you generate realistic e-discovery datasets for testing EAIDA and other e-discovery tools. Choose your investigation type, run the generator, and get a complete dataset with hot documents, privilege challenges, and realistic business context.

**Get started in 3 steps:**
1. Choose a [quick start guide](#-quick-start-guides)
2. Run `python app.py`
3. Load the output into EAIDA

Happy testing! 🎯
