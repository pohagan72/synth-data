# Synthetic E-Discovery Dataset Generator - Architecture Guide

## Table of Contents

1. [Overview](#overview)
2. [Why This Matters](#why-this-matters)
3. [Core Concepts](#core-concepts)
4. [System Architecture](#system-architecture)
5. [How It Works](#how-it-works)
6. [Key Design Decisions](#key-design-decisions)
7. [Use Cases](#use-cases)
8. [Extension Guide](#extension-guide)

---

## Overview

The Synthetic E-Discovery Dataset Generator is a Python-based tool that creates **realistic, legally-relevant datasets** for testing e-discovery platforms like EAIDA (Epiq's AI-powered document analysis tool). It generates synthetic emails, chat logs, calendar events, and attachments that simulate real corporate investigations.

### What It Does

- **Generates realistic communications** using Azure OpenAI (GPT models)
- **Simulates investigation scenarios** (antitrust, safety fraud, workplace harassment)
- **Creates needle-in-haystack environments** (signal vs. noise)
- **Produces multiple formats** (RFC-compliant .eml, Slack JSON, Teams RSMF, Webex JSON, .ics calendar)
- **Includes stress tests** (large attachments, blast emails, nested containers)
- **Generates protocol documents** describing the investigation and search strategy

### What Makes It Unique

1. **LLM-Powered Realism** - Uses GPT models to generate contextually appropriate, natural-sounding content
2. **Investigation-Specific Customization** - Scenarios adapt to antitrust, safety fraud, or HR contexts
3. **Automatic Privilege Generation** - Every dataset includes attorney-client privileged communications for screening practice
4. **Parallel Execution** - 7-10x faster than serial generation (10 concurrent LLM workers)
5. **Production-Ready** - Handles rate limits, errors gracefully, generates certification reports

---

## Why This Matters

### The E-Discovery Testing Challenge

**Problem:** EAIDA and similar AI-powered e-discovery tools need realistic test data to validate:
- Document classification accuracy
- Privilege screening capabilities
- Timeline reconstruction
- Hot document detection
- Content correlation across formats (email + attachments)
- Scalability with large datasets

**Traditional Approach Limitations:**
- ❌ **Real data has privacy/confidentiality issues** - Can't use actual client data for testing
- ❌ **Manual creation is slow** - Writing 500 realistic emails manually takes weeks
- ❌ **Synthetic data lacks realism** - Lorem ipsum or template-based data doesn't test ML models properly
- ❌ **No investigation narratives** - Random emails don't simulate actual discovery scenarios

**This Tool's Solution:**
- ✅ **Completely synthetic** - No real client data, fully shareable
- ✅ **Fast generation** - 500 items in ~6 minutes with parallel execution
- ✅ **LLM-powered realism** - Natural language, contextual content, realistic patterns
- ✅ **Investigation narratives** - Coherent storylines (price-fixing conspiracy, safety cover-up, harassment pattern)

### Business Impact

1. **EAIDA Development** - Provides consistent test datasets for feature validation
2. **Sales Demos** - Creates compelling, realistic demo environments for prospects
3. **Training** - Generates practice datasets for teaching reviewers and attorneys
4. **ML Model Training** - Provides labeled data for training document classification models
5. **Performance Testing** - Stress tests ingestion, processing, and search at scale

---

## Core Concepts

### 1. Signal vs. Noise (Needle in Haystack)

**Signal (The Needles):**
- Investigation-relevant communications that should be flagged/reviewed
- Examples: Price-fixing discussions, safety test falsification, harassment complaints
- Tags: `(S1)` Antitrust, `(S2)` Safety Fraud, `(S_HR)` Harassment, `(S3)` Privilege

**Noise (The Haystack):**
- Routine business communications that create realistic context
- Examples: Sales chatter, HR announcements, IT tickets, meeting scheduling, personal emails
- Tags: `(S4)` through `(S15)` for various noise types

**Why This Matters:**
Real e-discovery environments have ~1-5% hot documents in 95-99% noise. This tool replicates that ratio to test:
- Precision/recall of document classification
- Reviewer efficiency in finding needles
- Search term effectiveness

### 2. Investigation Types

The tool supports three primary investigation types:

| Type | Scenarios | Key Evidence | Hot Documents |
|------|-----------|--------------|---------------|
| **Antitrust** | Price-fixing, market allocation, bid rigging | Competitor coordination emails, pricing discussions, "market stability" coded language | S1, S1A, S1B |
| **Safety Fraud** | Test falsification, regulatory violations, cover-ups | Altered test reports, evidence destruction emails, FDA non-compliance | S2 |
| **HR Misconduct** | Workplace harassment, discrimination, hostile environment | Witness statements, inappropriate communications, complaint forms | S_HR |

Each investigation type has:
- **Investigation-specific scenarios** customized to that context
- **Automatic privilege scenarios** (legal consultations about the investigation)
- **Contextual noise** (relevant business communications)

### 3. Privilege Screening

**Attorney-Client Privilege (S3) is automatic** in every dataset because:
- Real investigations always include privileged communications
- Privilege screening is a critical e-discovery workflow
- EAIDA must identify privilege in any investigation type

**Privilege Scenario Variations:**
1. **S3 (Obvious)** - Subject line: "ATTORNEY-CLIENT PRIVILEGED"
2. **S3B (Subtle)** - No markers, but body clearly seeks legal advice from General Counsel
3. **S3C (By Recipient)** - Business email to GC becomes privileged when seeking legal guidance
4. **S3D (Mixed Thread)** - Thread starts as business, becomes privileged when GC joins
5. **S3E (Waiver)** - Privileged email improperly forwarded to non-attorney (tests waiver understanding)

### 4. Realism Patterns

**Chat Realism (v2.0.0):**
- Rapid-fire short messages (1-3 sentences)
- Realistic timing based on message length (5-30 sec for short, 1-5 min for long)
- Emoji reactions (👍 30% on confirmations)
- Edit history (10% of longer messages)
- Thread support for branching conversations

**Temporal Realism:**
- Business hours (80% during 8 AM - 6 PM)
- Friday evening → Monday morning gaps (70% of Friday 5pm+ emails wait)
- Weekend avoidance (90% skip Saturday/Sunday)
- Scenario-aware timing (fraud = fast panic OR deliberate delays)

**Content Alignment:**
- Attachments match email descriptions (email says "catastrophic failure" → attachment contains failure data)
- Email threads maintain context and quote previous messages
- Personas remain consistent (same tone, role, knowledge)

---

## System Architecture

### High-Level Flow

```
[YAML Config] → [Python App] → [Azure OpenAI] → [Output Files]
     ↓              ↓              ↓                 ↓
  Scenarios    Parallel       LLM Prompts      .eml, .json,
  Personnel    Execution      with Context     .ics, .rsmf
  Company      (10 workers)   Temperature      Attachments
  Settings                    Control          Containers
```

### Component Breakdown

#### 1. Configuration Layer (YAML Files)

**Purpose:** Define investigation scenarios, personnel, company profiles, attachment types

**Key Files:**
- `config-acme-antitrust.yaml` - Antitrust investigation (5 custodians, S1 scenarios)
- `config-acme-safety-fraud.yaml` - Product safety fraud (5 custodians, S2 scenarios)
- `config-acme-hr-misconduct.yaml` - HR harassment (5 custodians, S_HR scenarios)
- `config-acme.yaml` - All scenarios mixed (50+ custodians, stress testing)

**Structure:**
```yaml
company_profiles:
  - name: "ACME Inc."
    personnel:
      - name: "Jamie Chen"
        title: "VP of Sales"
        email: "jamie.chen@acme.com"

scenarios:
  - type: "thread"
    description: "(S1) Price-fixing email thread"
    base_filename: "antitrust_pricing_thread"
    prompt_variables:
      topic: ["market stability", "pricing alignment", ...]
    prompts:
      - prompt_templates:
          - "Draft an email from Jamie Chen to Rachel Quinn..."
```

#### 2. Generation Engine (app.py)

**Purpose:** Orchestrate scenario selection, LLM calls, file creation, parallel execution

**Key Functions:**

| Function | Purpose | Lines |
|----------|---------|-------|
| `generate_llm_response()` | Call Azure OpenAI with retry logic | 620-636 |
| `call_llm_with_retry()` | Exponential backoff for 429 errors | 351-388 |
| `generate_email_thread()` | Create multi-email conversation threads | ~1200-1350 |
| `generate_standalone_email()` | Create single-email scenario | ~1350-1450 |
| `generate_chat_scenario()` | Create Slack/Teams/Webex chat logs | ~1450-1600 |
| `create_and_save_email()` | Generate .eml file with headers/attachments | ~700-850 |
| `process_scenario_worker()` | Parallel worker for concurrent generation | 1779-1821 |

**Parallel Execution:**
```python
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_scenario_worker, scenario)
               for scenario in scenarios_to_process]
    for future in as_completed(futures):
        result = future.result()
        # Thread-safe stats updates
```

#### 3. LLM Integration (Azure OpenAI)

**Purpose:** Generate realistic, contextually appropriate content

**How It Works:**
1. **System Prompt** - Defines role and output format (JSON with specific keys)
2. **User Prompt** - Provides scenario context, personnel names, investigation details
3. **Temperature Control** - 0.7 for chats (spontaneity), 0.85 for threads (consistency), 0.9-1.3 for noise (variety)
4. **Response Format** - JSON mode ensures parseable output

**Example System Prompt (Email):**
```python
system_message = """You are an AI assistant for generating simulated corporate emails.
Return a single, valid JSON object and nothing else.
The JSON object must have the keys: 'subject', 'body', 'sender_name',
'sender_email', 'recipients'.
Recipients must be a list of lists: [['Name', 'email@example.com']].
"""
```

**Example User Prompt (Antitrust):**
```python
prompt = """Draft an email from Jamie Chen (ACME) to Rachel Quinn (Phoney Tunes)
proposing a 'shared game plan' for pricing strategy. Use subtle, coded language
like 'market stability' instead of 'price fixing'. Make it sound like a routine
business discussion but with clear implications of competitor coordination.

Context: ACME and Phoney Tunes are competitors in the telecommunications industry...
"""
```

#### 4. Output Formats

**Email (.eml):**
- RFC-compliant format with full headers (From, To, Cc, Bcc, Date, Message-ID, In-Reply-To, References)
- MIME multipart for attachments
- Realistic metadata (X-Mailer, Importance, Sensitivity)

**Slack Native Export (JSON):**
```json
{
  "channel_name": "sales-team",
  "messages": [
    {
      "type": "message",
      "user": "U12345",
      "text": "hey can you check this?",
      "ts": "1704067200.000100",
      "reactions": [{"name": "thumbsup", "users": ["U67890"], "count": 1}],
      "edited": {"user": "U12345", "ts": "1704067260.000100"}
    }
  ]
}
```

**Teams RSMF (Relativity Short Message Format):**
```json
{
  "conversationId": "19:abc123...",
  "participants": [...],
  "events": [
    {
      "id": "msg-001",
      "createdDateTime": "2025-01-15T10:30:00Z",
      "from": {"id": "user-001", "displayName": "Jamie Chen"},
      "body": {"content": "checking on this"},
      "reactions": [{"type": "like", "users": [...]}]
    }
  ]
}
```

**Calendar (.ics):**
```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//ACME Inc//Synthetic Data Generator//EN
BEGIN:VEVENT
UID:event-12345@acme.com
DTSTAMP:20250115T103000Z
DTSTART:20250120T140000Z
DTEND:20250120T150000Z
SUMMARY:Strategy Sync
ORGANIZER:mailto:jamie.chen@acme.com
ATTENDEE:mailto:rachel.quinn@phonetunes.com
DESCRIPTION:Discuss pricing strategy for Q2
END:VEVENT
END:VCALENDAR
```

---

## How It Works

### Step-by-Step Generation Workflow

#### Phase 1: Initialization

1. **User selects config file** (e.g., `config-acme-hr-misconduct.yaml`)
2. **User specifies count** (e.g., 500 items)
3. **User selects chat format** (Slack, Teams, Webex, or All)
4. **Config loaded into memory** (scenarios, personnel, company profiles)
5. **Output directory created** with timestamp

#### Phase 2: Scenario Filtering

```python
# Apply investigation-specific filter
if scenario_filter == 'hr_misconduct':
    filtered = [s for s in scenarios if '(S_HR)' in s['description'] or '(S3)' in s['description'] or is_noise(s)]
```

Ensures only relevant scenarios are included (HR harassment + privilege + noise, no antitrust/safety).

#### Phase 3: Parallel Generation Loop

```python
while generated_item_count < target_item_count:
    scenarios = config['scenarios'].copy()
    random.shuffle(scenarios)

    # Process up to 19 scenarios in parallel (10 workers)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for scenario in scenarios:
            if generated_item_count >= target_item_count:
                break
            future = executor.submit(process_scenario_worker, scenario, ...)
            futures.append(future)

        # Collect results as they complete
        for future in as_completed(futures):
            items_created = future.result()
            generated_item_count += items_created
```

**Key Points:**
- Scenarios shuffled for randomness
- Multiple scenarios processed concurrently (10 workers)
- Thread-safe counters track progress
- Continues until target count reached

#### Phase 4: Individual Scenario Processing

For each scenario (e.g., "S_HR Workplace harassment communications"):

1. **Select prompt template** from scenario YAML
2. **Replace variables** (e.g., `{topic}` → "inappropriate comments about appearance")
3. **Build context block** with company info, personnel, investigation details
4. **Call LLM with retry logic:**
   ```python
   response = call_llm_with_retry(
       lambda: client.chat.completions.create(
           model=AZURE_MODEL_NAME,
           messages=[
               {"role": "system", "content": system_message},
               {"role": "user", "content": prompt}
           ],
           temperature=0.85
       )
   )
   ```
5. **Parse JSON response** to extract email fields
6. **Generate attachments** (if applicable) with aligned content
7. **Apply temporal logic** to assign realistic timestamp
8. **Create output file** (.eml, .json, .ics, .rsmf)
9. **Update statistics** (thread-safe)

#### Phase 5: Thread Generation (Special Case)

For email threads (multi-message conversations):

1. **First email generated** from initial prompt
2. **Context accumulated** with previous email content
3. **Reply prompts built** with quoted previous message
4. **Subsequent emails generated** with references to prior context
5. **Email headers linked** (In-Reply-To, References for threading)
6. **Timestamps progress realistically** (30 min to 72 hours based on scenario)

Example:
```
Email 1: [Day 1, 2:30 PM] "Test results show catastrophic failure" (Initial alarm)
Email 2: [Day 1, 3:45 PM] "This data cannot leave this room" (Panic reply - 75 min later)
Email 3: [Day 3, 9:15 AM] "Here's the plan for the report" (Deliberate delay - 43 hours later)
```

#### Phase 6: Chat Generation (Modern Format)

For chat logs (Slack/Teams/Webex):

1. **LLM generates multiple messages** in single response
2. **Rapid-fire timing applied** (5-30 sec gaps for short messages)
3. **Reactions added** (30% chance for short confirmations, random emoji)
4. **Edit history added** (10% chance for messages >50 chars)
5. **Thread support** (thread_ts linking for threaded replies)
6. **Multiple format exports** (Slack JSON + Teams RSMF + Webex JSON)

#### Phase 7: Post-Processing

1. **Nested container creation** (TarGz → Zip → Files) if enabled
2. **Protocol document generation** with search terms and expected hot docs
3. **Certification report generation** with dynamic signal/noise descriptions
4. **Archive creation** (.tar.gz of entire output directory)

---

## Key Design Decisions

### 1. Why LLM-Generated Content Instead of Templates?

**Decision:** Use Azure OpenAI (GPT models) to generate content dynamically

**Rationale:**
- **Realism** - LLMs produce natural-sounding, contextually appropriate language
- **Variety** - Each generation is unique (no repeated template patterns)
- **Adaptability** - Same prompt system works for antitrust, safety fraud, HR contexts
- **ML Training** - Realistic language patterns better train document classifiers

**Trade-offs:**
- ⚠️ **Cost** - Azure OpenAI API usage (~$0.50-$2 per 500 items)
- ⚠️ **Speed** - LLM calls are slower than templates (~3 sec per call vs instant)
- ⚠️ **Consistency** - Requires careful prompt engineering to ensure quality

**Mitigation:**
- Parallel execution (10 workers) reduces wall-clock time by 7-10x
- Retry logic with exponential backoff handles rate limits gracefully
- Detailed system prompts ensure output format consistency

### 2. Why Privilege is Automatic (Not Optional)

**Decision:** Include privilege scenarios (S3) in every investigation config

**Rationale:**
- **Real-world accuracy** - Every real investigation requires privilege screening
- **Workflow testing** - Privilege is a workflow step, not a case type
- **EAIDA requirements** - Must identify privilege docs in any matter type
- **Reviewer training** - Attorneys need practice spotting privilege across contexts

**Previous Approach (Removed):**
- Had separate `config-acme-legal-privilege.yaml` as standalone option
- Users could generate "privilege-only" datasets
- This was unrealistic (privilege doesn't exist in isolation)

**Current Approach:**
- Privilege (S3, S3B, S3C, S3D, S3E) included in all focused configs
- Privilege scenarios customized to investigation context:
  - Antitrust: Legal advice about pricing discussions, Sherman Act violations
  - Safety: Legal advice about FDA reporting, test failure documentation
  - HR: Legal advice about Title VII liability, harassment complaint procedures

### 3. Why Parallel Execution with Thread Pools (Not Async)

**Decision:** Use `ThreadPoolExecutor` with 10 workers instead of `asyncio`

**Rationale:**
- **Simplicity** - Easier to understand and maintain than async/await
- **Library compatibility** - Azure OpenAI SDK works well with threads
- **Sufficient speedup** - 10 workers provide 7-10x performance gain
- **Thread-safe patterns** - Locks protect shared state (stats, counters)

**Why Not Async:**
- ⚠️ Requires rewriting all blocking I/O with `await`
- ⚠️ More complex error handling
- ⚠️ Marginal performance benefit for I/O-bound workload

**Why Not Process Pool:**
- ⚠️ Unnecessary for I/O-bound tasks (LLM API calls)
- ⚠️ Higher memory overhead (separate Python interpreters)
- ⚠️ More complex inter-process communication

### 4. Why Signal/Noise Ratio is ~25/75 (Not 50/50)

**Decision:** Target ratio of ~25% signal (hot docs) to ~75% noise (business context)

**Rationale:**
- **Real-world accuracy** - Actual e-discovery has 1-5% hot documents in 95-99% noise
- **Reviewer training** - Need realistic "needle in haystack" environment
- **EAIDA testing** - Tests precision/recall at realistic signal strength
- **Usability** - 25% signal provides enough hits to be engaging without overwhelming noise

**Comparison:**
| Ratio | Real World | This Tool | Test/Demo | Training |
|-------|-----------|-----------|-----------|----------|
| Signal | 1-5% | 25% | 50%+ | 10-30% |
| Noise | 95-99% | 75% | <50% | 70-90% |

Our ratio is **conservative** compared to real-world (easier for reviewers) but **realistic enough** for meaningful testing.

### 5. Why Multiple Config Files (Not One Universal Config)

**Decision:** Separate configs for antitrust, safety fraud, HR misconduct

**Rationale:**
- **Focused testing** - Each config creates a pure investigation environment
- **Faster onboarding** - Users pick relevant config without YAML editing
- **Clear intent** - Config file name matches investigation type
- **Easier troubleshooting** - Smaller configs are easier to understand/debug

**Trade-off:**
- ⚠️ Some duplication (noise scenarios repeated across configs)
- ✅ Better UX outweighs duplication cost

---

## Use Cases

### 1. EAIDA Feature Validation

**Scenario:** Epiq engineers develop new EAIDA features (e.g., enhanced privilege detection)

**How This Tool Helps:**
- Generate 500-item dataset with subtle privilege scenarios (S3B, S3C, S3D)
- Test EAIDA's ability to identify privilege without obvious markers
- Measure precision/recall on privilege detection
- Compare results across EAIDA versions

**Example Workflow:**
```bash
python app.py
# Select: config-acme-antitrust.yaml
# Items: 500
# Format: All

# Upload to EAIDA test environment
# Run privilege screening workflow
# Analyze: Did EAIDA catch S3B/S3C scenarios? False positive rate?
```

### 2. Sales Demonstrations

**Scenario:** Sales team presents EAIDA to prospect investigating workplace harassment

**How This Tool Helps:**
- Generate HR misconduct dataset (harassment + witness statements + privilege)
- Create realistic investigation narrative with hot documents
- Protocol document provides search terms and expected results
- Demonstrates EAIDA's value in identifying harassment patterns

**Example Workflow:**
```bash
python app.py
# Select: config-acme-hr-misconduct.yaml
# Items: 200 (appropriate for 30-minute demo)
# Format: All

# Import to EAIDA demo instance
# Show: Search for harassment keywords
# Show: Timeline of complaint → escalation → retaliation
# Show: Privilege screening identifies legal consultations
```

### 3. Compliance Training

**Scenario:** Train attorneys on identifying price-fixing communications

**How This Tool Helps:**
- Generate antitrust dataset with coded language ("market stability", "align on approach")
- Trainees practice spotting subtle collusion indicators
- Protocol document provides answer key (expected hot documents)
- Safe environment (no real client data exposure)

**Example Workflow:**
```bash
python app.py
# Select: config-acme-antitrust.yaml
# Items: 100 (manageable for 2-hour training)
# Format: Email only (less distraction than chats)

# Exercise: "Review these 100 emails, flag potential violations"
# Debrief: Show protocol document with correct answers
# Discussion: What coded language patterns did you notice?
```

### 4. ML Model Training

**Scenario:** Train document classification model to detect safety fraud

**How This Tool Helps:**
- Generate large dataset (5,000+ items) with labeled scenarios
- Signal docs tagged as (S2) = positive examples
- Noise docs tagged as (S4-S15) = negative examples
- Train supervised learning model on realistic language patterns

**Example Workflow:**
```bash
# Generate training set
python app.py
# Select: config-acme-safety-fraud.yaml
# Items: 3000

# Generate validation set (different random seed)
python app.py
# Select: config-acme-safety-fraud.yaml
# Items: 1000

# Parse scenario tags from filenames
# Train classifier: Safety Fraud (S2) vs. Noise
# Evaluate: Precision, recall, F1 score
```

### 5. Performance/Stress Testing

**Scenario:** Test EAIDA ingestion performance with large, complex datasets

**How This Tool Helps:**
- Generate datasets with stress test artifacts:
  - 500+ recipient blast emails (metadata explosion)
  - Large log files (10-100 MB, timeout/memory testing)
  - Nested containers (TarGz → Zip → Files, recursion depth testing)
- Measure ingestion time, memory usage, error rates

**Example Workflow:**
```bash
python app.py
# Select: config-acme.yaml (includes stress tests)
# Items: 1000
# Log size: 100 MB
# Nested container: Yes

# Upload to EAIDA staging environment
# Monitor: Ingestion time, CPU/memory, error logs
# Identify: Performance bottlenecks, timeout issues
```

---

## Extension Guide

### Adding a New Investigation Type

**Example:** Add "Intellectual Property Theft" investigation

#### Step 1: Create Config File

```yaml
# config-acme-ip-theft.yaml
general_settings:
  scenario_filter: 'ip_theft'
  output_directory: "demo_ip_theft_investigation"

company_profiles:
  - name: "ACME Inc."
    personnel:
      - name: "Dr. Sarah Chen"
        title: "Chief Technology Officer"
        email: "sarah.chen@acme.com"
      - name: "David Park"
        title: "Senior Engineer"
        email: "david.park@acme.com"
      # ... more personnel

scenarios:
  # Signal: IP Theft
  - type: "thread"
    description: "(S_IP) Trade secret theft email thread"
    base_filename: "ip_theft_trade_secret"
    prompts:
      - prompt_templates:
          - "Draft an email from David Park to competitor@rival.com discussing ACME's proprietary algorithm..."

  # Include privilege scenarios (automatic)
  - type: "thread"
    description: "(S3) Legal consultation about IP theft"
    # ... privilege prompts customized to IP context

  # Include noise scenarios (S4-S15)
  # Copy from other configs or reference shared scenarios
```

#### Step 2: Update Scenario Filtering Logic

```python
# app.py, apply_scenario_filter() function
def apply_scenario_filter(scenarios, scenario_filter, include_noise=True):
    if scenario_filter == 'ip_theft':
        signal_prefixes = ['(S_IP)', '(S3)']  # IP scenarios + privilege
    elif scenario_filter == 'antitrust':
        signal_prefixes = ['(S1)', '(S3)']
    # ... existing filters

    # Rest of filtering logic
```

#### Step 3: Update Report Generation

```python
# app.py, report generation section
if any("(S_IP)" in k for k in signal_scenarios.keys()):
    signal_types.append("Intellectual Property Theft")
```

#### Step 4: Create Quick Start Guide

```markdown
# QUICK_START_IP_THEFT.md
## Intellectual Property Theft Investigation

### What This Generates
- Trade secret theft communications
- Proprietary algorithm discussions
- Competitor solicitation emails
- ...
```

#### Step 5: Update Documentation

Add to:
- `README.md` - List of investigation types
- `CONFIGS_GUIDE.md` - Config file table
- `CHANGELOG.md` - New feature announcement

### Adding a New Scenario to Existing Investigation

**Example:** Add "Retaliation" scenario to HR misconduct

#### Step 1: Define Scenario in Config

```yaml
# config-acme-hr-misconduct.yaml
scenarios:
  - type: "thread"
    description: "(S_HR) Retaliation after harassment complaint"
    base_filename: "hr_retaliation"
    prompt_variables:
      retaliation_action:
        - "negative performance review"
        - "reassignment to less desirable role"
        - "exclusion from key meetings"
        - "increased scrutiny of work"
    prompts:
      - prompt_templates:
          - "Draft an email from {manager} to HR discussing {employee}'s recent {retaliation_action}. The timing is suspiciously close to their harassment complaint filed 2 weeks ago. Make it sound like normal performance management but with subtle vindictive undertones."
```

#### Step 2: Test the Scenario

```bash
python app.py
# Select: config-acme-hr-misconduct.yaml
# Items: 50 (small test run)

# Verify: Are retaliation scenarios generating correctly?
# Check: Prompt variables substituting properly?
# Confirm: Content quality acceptable?
```

### Adding a New Output Format

**Example:** Add "Mattermost" chat format

#### Step 1: Research Format Specification

Study Mattermost's export format:
```json
{
  "team_name": "acme-team",
  "channel_name": "sales",
  "posts": [
    {
      "post_id": "abc123",
      "user": "jamie.chen",
      "message": "checking on this",
      "create_at": 1704067200000,
      "reactions": []
    }
  ]
}
```

#### Step 2: Create Formatting Function

```python
# app.py
def create_and_save_mattermost(chat_content, base_filename, output_dir, personnel_map, start_date):
    """Creates Mattermost export format JSON."""

    # Map users
    users = [p for p in personnel_map.values()]

    # Create posts
    posts = []
    for msg in chat_content['messages']:
        post = {
            "post_id": uuid.uuid4().hex,
            "user": msg['sender_email'].split('@')[0],
            "message": msg['body'],
            "create_at": int(start_date.timestamp() * 1000),
            "reactions": []
        }
        posts.append(post)

    # Create export structure
    export = {
        "team_name": "acme-team",
        "channel_name": base_filename,
        "posts": posts
    }

    # Write file
    filepath = os.path.join(output_dir, f"{base_filename}_mattermost.json")
    with open(filepath, 'w') as f:
        json.dump(export, f, indent=2)
```

#### Step 3: Update Chat Generation

```python
# app.py, generate_chat_scenario() function
def generate_chat_scenario(..., chat_format_pref):
    # ... existing logic

    if chat_format_pref in ['mattermost', 'all']:
        create_and_save_mattermost(chat_content, base_filename, output_dir, personnel_map, start_date)
```

#### Step 4: Update CLI Options

```python
# app.py, get_chat_format_preference() function
print("Select Chat Data Output Format:")
print("  1: Slack Native Export (JSON)")
print("  2: RSMF (Microsoft Teams)")
print("  3: Webex (API/JSON format)")
print("  4: Mattermost")
print("  5: All Formats")
```

---

## Technical Specifications

### Performance Benchmarks

| Dataset Size | Serial Time | Parallel Time (10 workers) | Speedup |
|--------------|-------------|---------------------------|---------|
| 100 items | ~10 minutes | ~1-2 minutes | 5-10x |
| 500 items | ~50 minutes | ~5-7 minutes | 7-10x |
| 1000 items | ~100 minutes | ~10-15 minutes | 7-10x |

**Factors Affecting Speed:**
- Azure OpenAI TPM (tokens per minute) quota
- Attachment generation (slower if many attachments)
- Chat format selection (all formats = 3x slower than single format)
- Network latency to Azure

### Resource Requirements

**Minimum:**
- Python 3.8+
- 2 GB RAM
- Azure OpenAI API access with basic quota

**Recommended:**
- Python 3.10+
- 4 GB RAM (for large log file generation)
- Azure OpenAI API with elevated quota (supports higher TPM)

### Error Handling

**Rate Limits (429):**
- Exponential backoff: 2s, 4s, 8s, 16s, 32s
- Max 5 retries before giving up
- Thread-safe (multiple workers can hit rate limits independently)

**LLM Errors:**
- Invalid JSON response → Retry with same prompt
- Missing required keys → Regenerate entire response
- Non-429 errors → Raise immediately (no retry)

**File I/O Errors:**
- Permission errors → Fail fast with clear message
- Disk space errors → Check before writing large files
- Path errors → Validate output directory exists

---

## Frequently Asked Questions

### How much does it cost to generate a dataset?

**Azure OpenAI API costs** (approximate):
- 100 items: ~$0.10-$0.30
- 500 items: ~$0.50-$1.50
- 1000 items: ~$1.00-$3.00

**Factors affecting cost:**
- Model choice (Sonnet 3.5 more expensive than GPT-4o)
- Attachment generation (adds LLM calls)
- Chat formats (3x calls if "All formats" selected)

### Can I use this with other LLM providers (non-Azure)?

**Currently:** No, code is tightly coupled to Azure OpenAI SDK

**Future:** Could be adapted to support:
- OpenAI API directly (very similar SDK)
- AWS Bedrock (different API structure)
- Local models (Ollama, vLLM) - would need different approach

### How realistic is the generated data?

**Very realistic for:**
- Natural language patterns
- Email threading and headers
- Business communication style
- Investigation narratives

**Less realistic for:**
- Entity consistency (LLM may vary names/titles slightly)
- Deep technical content (requires domain-specific prompts)
- Legal citations (LLM may hallucinate case names)

**Mitigation:**
- Detailed prompts with specific context
- Post-generation review for critical demos
- Treat as "directionally accurate" test data, not perfect replicas

### Can I modify scenarios without editing YAML?

**No built-in UI**, but you can:
1. Edit YAML files with any text editor (VS Code recommended)
2. Copy existing scenario and modify prompts
3. Test with small dataset (50-100 items) before full run

**Future enhancement idea:**
- Web UI for scenario editing
- Scenario "mixer" to combine from library

### How do I ensure GDPR/privacy compliance?

**This tool generates 100% synthetic data:**
- No real people (names are fictional)
- No real companies (ACME, Phoney Tunes are made up)
- No real cases (scenarios are invented)

**Safe to share** with:
- Prospects (sales demos)
- External partners (testing)
- Public repositories (if desired)

**Do not:**
- Use real client names or data in prompts
- Mix synthetic with real data
- Claim it represents actual cases

---

## Conclusion

The Synthetic E-Discovery Dataset Generator is a production-ready tool for creating realistic, investigation-specific test data. Its LLM-powered approach, parallel execution, and comprehensive format support make it ideal for EAIDA testing, sales demonstrations, and compliance training.

**Key Strengths:**
- 🚀 **Fast** - 7-10x speedup with parallel execution
- 🎯 **Realistic** - LLM-generated content with investigation narratives
- 🔒 **Safe** - 100% synthetic, no privacy concerns
- 🛠️ **Extensible** - Easy to add investigation types and scenarios
- 📊 **Comprehensive** - Multiple formats, stress tests, protocol documents

**Future Directions:**
- Additional investigation types (securities fraud, FCPA, insider trading)
- Enhanced entity consistency (stricter name/email enforcement)
- Web UI for scenario editing
- Support for additional LLM providers
- Improved near-duplicate patterns (forward chains, reply-all sprawl)

For questions, issues, or contributions, see:
- [README.md](README.md) - Quick start and usage
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [ENHANCEMENTS_2026-01.md](ENHANCEMENTS_2026-01.md) - Technical enhancements
- [GitHub Issues](https://github.com/epiq/synth-data) - Bug reports and feature requests

---

**Document Version:** 1.0
**Last Updated:** January 15, 2026
**Author:** Claude (Anthropic) with Epiq Engineering Team
