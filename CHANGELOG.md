# Changelog

All notable changes to the Synthetic E-Discovery Dataset Generator.

---

## [2.4.0] - 2026-01-16

### Added

#### 🎛️ Interactive Model Selection
- **Feature:** Users can now select which AI model to use for generation at runtime
- **Why:** Different models offer different trade-offs between quality, speed, and cost
- **Options:**
  1. **GPT-4 (gpt-4):** Best quality for complex legal language, slower, more expensive
  2. **Claude Haiku 4 (claude-haiku-4-5):** Fast and cost-effective, recommended for large datasets (default)
  3. **Claude Sonnet 3.5 (claude-sonnet-3.5):** Balanced quality and speed for production use
  4. **Use .env default:** Automatically use `ANTHROPIC_DEFAULT_HAIKU_MODEL` or `AZURE_OPENAI_MODEL`

**Use cases:**
- **Quality assurance runs:** Use GPT-4 for highest quality legal terminology
- **High-volume testing:** Use Claude Haiku for fast, cost-effective dataset generation
- **Production datasets:** Use Claude Sonnet 3.5 for balanced quality
- **Batch operations:** Set default in `.env` and select option 4 for automated workflows

**Implementation:** New `get_model_preference()` function prompts user during startup, before item generation begins.

---

## [2.3.1] - 2026-01-16

### Added

#### 🌍 Complete Multilingual Coverage Across All Configs
- **Feature:** Extended multilingual support to all remaining investigation configs
- **Why:** Every organization has multilingual communications. Complete coverage ensures realistic testing regardless of which config is selected.
- **New Multilingual Scenarios Added:**

**Corporate Configs:**
1. **(S2E) Chinese/English Manufacturing Quality Concerns** - config-acme-safety-fraud.yaml
   - Wei Zhang (ACME Manufacturing Engineer) ↔ Casey Mitchell
   - 50% Simplified Chinese, 50% English code-switching
   - Context: Shenzhen factory quality control issues, sensor housing defects
   - Tests: CJK character encoding, manufacturing terminology (质量问题, 压力很大, 违反安全标准)

2. **(HR9) Spanish/English Workplace Harassment Discussion** - config-acme-hr-misconduct.yaml
   - Sofia Ramirez ↔ Carmen Lopez (HR Specialist)
   - 60% Spanish, 40% English code-switching
   - Context: Harassment complaint, whistleblower support
   - Tests: Bilingual US workplace, HR terminology (acoso laboral, violación de política, testigos)

**Healthcare Configs:**
3. **(S_HIPAA_F) Spanish/English IT Security Incident** - config-hospital-hipaa-breach.yaml
   - Carlos Mendez (IT Security Analyst) ↔ Morgan Chen
   - 55% Spanish, 45% English code-switching
   - Context: Database breach discovery, HIPAA violation
   - Tests: Bilingual IT staff, security terminology (actividad sospechosa, violación HIPAA, aislamiento del sistema)

4. **(S_HARM_H) Spanish/English Nurse Safety Concerns** - config-hospital-patient-harm.yaml
   - Nurse Isabel Morales ↔ Nurse Supervisor Ana Rodriguez
   - 60% Spanish, 40% English code-switching
   - Context: Wrong-site surgery witnessed, whistleblower fear
   - Tests: Bilingual clinical staff, medical terminology (sitio quirúrgico incorrecto, error médico grave, responsabilidad ética)

- **Coverage:** Every focused investigation config now includes contextually-appropriate multilingual scenarios
- **Realism:** Language choices match real-world workforce demographics:
  - Manufacturing → Chinese (Asian supplier communications)
  - HR/Workplace → Spanish (US bilingual workforce)
  - Healthcare IT → Spanish (bilingual technical staff)
  - Clinical → Spanish (bilingual nursing staff - largest Spanish-speaking healthcare demographic)
- **Files Modified:**
  - `config-acme-safety-fraud.yaml`: Added S2E Chinese manufacturing scenario
  - `config-acme-hr-misconduct.yaml`: Added HR9 Spanish harassment scenario
  - `config-hospital-hipaa-breach.yaml`: Added S_HIPAA_F Spanish IT security scenario
  - `config-hospital-patient-harm.yaml`: Added S_HARM_H Spanish clinical scenario

### Impact Summary

**Before v2.3.1:**
- Only 2 configs had multilingual scenarios (antitrust + billing fraud)
- Missing coverage for safety fraud, HR, HIPAA breach, and patient harm investigations
- Users had to select specific configs to test multilingual capabilities

**After v2.3.1:**
- **All 6 focused investigation configs** include multilingual scenarios
- 2-5% multilingual content in every dataset (realistic proportion)
- No matter which config a user selects, they test LID/encoding/multilingual search
- Language choices match investigation context (manufacturing → Chinese, healthcare → Spanish)

**Result:** Complete multilingual coverage ensures every EAIDA test includes Language Identification, Unicode encoding, and multilingual search capabilities by default. No special configuration required.

---

## [2.3.0] - 2026-01-16

### Added

#### 🌍 Multi-Language Support (Phase 1: Foundation)
- **Feature:** Infrastructure for generating multilingual documents with code-switching
- **Why:** Real-world e-discovery involves international communications. Tests Language Identification (LID), Unicode/UTF-8 handling, and multilingual search in EAIDA
- **Supported Languages:**
  - **German (de):** Formal business German
  - **Spanish (es):** Formal business Spanish
  - **Chinese (zh):** Simplified Chinese
  - **Code-Switching (de-en-mixed, es-en-mixed, zh-en-mixed):** Mixed language communications with configurable ratios
- **Implementation:**
  - Added `get_language_instruction()` helper function (app.py:634-663) - Maps language codes to LLM instructions
  - Modified `generate_email_content_from_llm()` to accept `language_code` and `language_ratio` parameters (app.py:683-704)
  - Modified `generate_chat_content_from_llm()` to accept language parameters (app.py:716-759)
  - Updated `generate_email_thread()`, `generate_standalone_email()`, and `generate_chat_scenario()` to pass language parameters (app.py:1343-1955)
  - Updated `process_scenario_worker()` to extract language settings from scenario YAML (app.py:1938-1940)
- **YAML Configuration:**
  ```yaml
  - type: "thread"
    description: "(S1C) German/English price-fixing coordination"
    language: "de-en-mixed"  # Code-switching
    language_ratio: 0.7  # 70% German, 30% English
  ```
- **Example Scenarios Added:**
  - **(S1C) German/English Antitrust Coordination:** config-acme-antitrust.yaml (lines 446-462)
    - Hans Gruber (ACME Berlin) coordinates pricing with Jamie Chen using business German
    - Tests: European antitrust context, Preisabsprache (price-fixing), Marktaufteilung (market division)
  - **(S_FRAUD_C2) Spanish/English Billing Concerns:** config-hospital-billing-fraud.yaml (lines 640-656)
    - Maria Rodriguez and Carmen Gutierrez discuss fraudulent billing pressure in Spanish/English mix
    - Tests: Bilingual healthcare workers, codificación fraudulenta (fraudulent coding)
- **Use Cases:**
  - **LID Testing:** Can EAIDA auto-detect that a document is 70% German?
  - **Encoding Stress:** CJK characters test Unicode/UTF-8 handling in ingestion engines
  - **Code-Switching:** Humans naturally mix languages mid-sentence - tests AI classifiers
  - **Multilingual Search:** Can investigators search across German "Preisabsprache" and English "price-fixing"?
- **Files Modified:**
  - `app.py`: Language instruction infrastructure, LLM function updates, scenario processing
  - `config-acme-antitrust.yaml`: Added S1C German pricing coordination scenario
  - `config-hospital-billing-fraud.yaml`: Added S_FRAUD_C2 Spanish billing concerns scenario

### Impact Summary

**Before v2.3.0:**
- Only English-language communications generated
- No testing of Language Identification (LID) workflows
- No stress testing of Unicode/UTF-8 character encoding
- Limited realism for international investigations

**After v2.3.0:**
- Multilingual document generation with German, Spanish, and Chinese support
- Code-switching scenarios test realistic bilingual communication patterns
- EAIDA can now be tested for LID, encoding, and multilingual search capabilities
- Antitrust investigations include European coordination scenarios
- Healthcare investigations reflect bilingual US workforce reality

**Result:** Synthetic datasets now test EAIDA's multilingual processing workflows - a critical gap in previous testing. Phase 2 (Audio Evidence) and Phase 3 (Image Evidence) planned for future releases.

---

## [2.2.1] - 2026-01-16

### Added

#### 📊 Enhanced Certification Report Metrics
- **Feature:** Added date range and active custodian count to certification report header
- **Why:** Provides immediate visibility into dataset temporal scope and organizational breadth
- **New Metrics:**
  - **Simulated Date Range:** Shows earliest to latest document date with day span (e.g., "Nov 15, 2025 - Jan 16, 2026 (63 days)")
  - **Active Custodians:** Displays count of unique custodians with generated documents (e.g., "50")
- **Implementation:**
  - Added `email_dates` list to stats tracking (tracks all email, calendar, chat dates)
  - Added `custodians` set to stats tracking (tracks unique sender/participant emails)
  - Updated all document creation functions to populate tracking data
  - Report calculates min/max dates and unique custodian count on-the-fly
- **Files Modified:**
  - `app.py`: Stats initialization, email/calendar/chat tracking, report generation (lines 1773-1783, 740-744, 871-875, 1044-1050, 1127-1133, 1185-1192, 1960-1977)

### Fixed

#### 🐛 Custodian Validation Bug - "recipient" Folder Issue
- **Bug:** Malformed LLM responses could create spurious custodian folders named "recipient" instead of valid email addresses
- **Root Cause:** Lines 839-843 in `create_and_save_email()` assumed recipients were always [name, email] tuples without validation
- **Original Code:** `for _, email in email_content.get('recipients', []): all_custodians.append(email)`
- **Problem:** If LLM returned unexpected structure, variable could capture literal string "recipient"
- **Fix Implemented:** Added comprehensive validation to custodian email extraction (lines 837-877):
  - Validates sender_email is string containing '@' symbol
  - Validates recipients/cc/bcc are tuples/lists with at least 2 elements
  - Validates extracted emails are strings containing '@' symbol
  - Only creates folders for valid, unique email addresses
- **Result:** Eliminates spurious custodian folders from malformed LLM responses
- **Files Modified:**
  - `app.py`: Custodian folder creation logic with defensive validation (lines 837-877)

### Impact Summary

**Before v2.2.1:**
- Certification report showed document counts only
- No visibility into temporal distribution or custodian participation
- Potential for invalid custodian folders from malformed data

**After v2.2.1:**
- Report header includes date range showing investigation timeline
- Active custodian count confirms realistic organizational depth (50 personnel)
- Quality assurance: Quickly identify issues like narrow date ranges or low custodian participation
- Professional: Provides context for dataset scope at a glance
- Data integrity: Only valid email addresses create custodian folders

**Result:** Certification report now provides comprehensive dataset overview with temporal and organizational context in the header, plus improved data integrity through custodian validation.

---

## [2.2.0] - 2026-01-16

### Added

#### 🏥 Healthcare Investigation Configs (Three New Focused Configs)
- **Feature:** Three comprehensive healthcare investigation configurations following the same professional structure as ACME corporate configs
- **Why:** Healthcare e-discovery is a major use case for EAIDA - HIPAA breaches, billing fraud, and medical malpractice investigations require specialized scenarios
- **New Config Files:**

**1. config-hospital-hipaa-breach.yaml** - HIPAA Data Breach Investigation
- **Organization:** Metropolitan General Hospital (metrogenhospital.org)
- **Investigation:** Unauthorized patient database access and data exfiltration (March 2024)
- **Narrative:** Junior developer accidentally exposed database credentials on GitHub → external attacker accessed 47,892 patient records → executive team debated notification timing → compliance officer threatened resignation → breach reported within 60-day HIPAA window
- **Signal Scenarios (temp 0.4):**
  - (S_HIPAA) Main breach discovery thread
  - (S_HIPAA_A) Evidence of data exfiltration
  - (S_HIPAA_B) Delayed breach notification debate
  - (S_HIPAA_C) Coverup attempts / evidence destruction
  - (S_HIPAA_D) Emergency response meeting calendar event
  - (S_HIPAA_E) Teams chat showing real-time panic
  - (S3) Attorney-client privilege scenarios (4 variations)
- **Personnel:** 50 total (5 core custodians + 45 expansion)
  - Core: CISO, IT Director, Compliance Officer, CMO, General Counsel
  - Expansion: Doctors, nurses, IT staff, billing, HR, facilities (realistic hospital depth)
- **Attachments:** Patient access logs, incident reports, forensic analysis, breach notifications
- **Output:** demo_hipaa_breach_investigation

**2. config-hospital-billing-fraud.yaml** - Medicare/Medicaid Billing Fraud Investigation
- **Organization:** Riverside Regional Medical Center (riversideregional.org)
- **Investigation:** Systematic upcoding and kickback scheme (2022-2024, $11M+ fraudulent claims)
- **Narrative:** CFO and Billing Director implemented "revenue optimization" strategy → systematic upcoding using DRG manipulation → kickback scheme with MedTech Solutions Inc. disguised as consulting fees → phantom billing for cancelled appointments → pressure on billing staff to "code creatively" → whistleblower (Karen Phillips) filed qui tam lawsuit → evidence destruction attempts
- **Signal Scenarios (temp 0.4):**
  - (S_FRAUD) Main fraud thread: Upcoding discovery
  - (S_FRAUD_A) Kickback scheme with medical device vendor
  - (S_FRAUD_B) Phantom billing for services not rendered
  - (S_FRAUD_C) Pressure on billing staff to maximize reimbursement
  - (S_FRAUD_D) Destruction of audit evidence
  - (S_FRAUD_E) "Revenue Optimization Strategy" calendar meeting
  - (S_FRAUD_F) Teams chat about coding "creatively"
  - (S3) Attorney-client privilege scenarios (4 variations)
- **Personnel:** 50 total (5 core custodians + 45 expansion)
  - Core: CFO, Billing Director, Compliance Officer, Senior Physician, General Counsel
  - Expansion: Medical coders, billing specialists, physicians, nurses, auditors, IT, HR, facilities
- **Attachments:** Upcoding analysis spreadsheets, Medicare claims (CMS-1500), kickback agreements, coding guidelines, audit reports
- **Output:** demo_billing_fraud_investigation

**3. config-hospital-patient-harm.yaml** - Medical Malpractice with Coverup Investigation
- **Organization:** St. Catherine's Regional Hospital (stcatherines-health.org)
- **Investigation:** Wrong-site surgery with evidence destruction and witness intimidation (March-April 2024)
- **Narrative:** Dr. Marcus Chen performed LEFT knee arthroscopy on wrong patient (operated on RIGHT knee instead) → patient Robert Hendricks died from complications of corrective surgery → Risk Management Director orchestrated coverup → original incident reports destroyed → falsified versions created → nursing witnesses intimidated → abuse of peer review privilege to hide legal strategy → cover story blamed "patient confusion"
- **Signal Scenarios (temp 0.4):**
  - (S_HARM) Main thread: Wrong-site surgery discovery
  - (S_HARM_A) Initial incident report showing legitimate concerns
  - (S_HARM_B) Pressure to modify/falsify medical records
  - (S_HARM_C) Destruction of evidence communications
  - (S_HARM_D) Intimidation of staff witnesses
  - (S_HARM_E) Abuse of peer review privilege (using quality review to hide coverup)
  - (S_HARM_F) Secret "Incident Management Strategy" calendar meeting
  - (S_HARM_G) Teams chat showing real-time panic after discovery
  - (S3) Attorney-client privilege scenarios (6 variations, including privilege abuse detection)
- **Personnel:** 50 total (5 core custodians + 45 expansion)
  - Core: CMO, Attending Physician (surgeon), Charge Nurse, Risk Management Director, General Counsel
  - Expansion: Physicians across specialties, nurses, medical records staff, quality/compliance, IT, HR, facilities
- **Attachments:** Original vs. modified incident reports, medical records, surgical logs, peer review minutes, witness statements (original and coerced)
- **Output:** demo_patient_harm_investigation

#### Shared Healthcare Config Features
- **50 personnel** (5 core custodians + 45 expansion for realistic organizational depth)
- **Temperature control** (0.4 for signal, 0.95 for noise, 1.0 for ultra-mundane)
- **Privilege scenarios** (S3 automatic with all investigations)
- **Noise scenarios** (S4-S18: patient scheduling, medical supplies, IT helpdesk, HR, facilities, ultra-mundane)
- **Realistic healthcare communication styles** (clinical terminology, EHR systems, medical abbreviations)
- **External parties** (law firms, forensic investigators, regulators)
- **Coded language** appropriate to each fraud type
- **Evidence trails** showing consciousness of guilt and obstruction

### Changed

#### Documentation Updates
- **CONFIGS_GUIDE.md:** Added "Healthcare Investigations" section with all three new configs
  - Updated scenario tags table with S_HIPAA, S_FRAUD, S_HARM tags
  - Added three healthcare config examples with usage instructions
  - Reorganized config tables into "Corporate" and "Healthcare" categories
- **README.md:** Added healthcare configs to Available Configurations table
  - Added three healthcare investigation example outputs
  - Reorganized into "Corporate Investigations" and "Healthcare Investigations" sections
- **CHANGELOG.md:** This entry documenting v2.2.0

### Impact Summary

**Before v2.2.0:**
- Only corporate investigation configs available (ACME Inc.)
- Healthcare investigations required manual scenario creation
- No HIPAA breach, billing fraud, or malpractice scenarios

**After v2.2.0:**
- **Six focused investigation configs total** (3 corporate + 3 healthcare)
- Healthcare e-discovery fully supported with realistic scenarios
- Medical organizations can use professional, healthcare-specific datasets
- EAIDA can be tested on:
  - HIPAA compliance and data breach detection
  - Healthcare fraud detection (Medicare/Medicaid)
  - Medical malpractice coverup and obstruction of justice
  - Healthcare-specific privilege abuse (peer review privilege)

**Result:** Comprehensive healthcare investigation support matching the quality and professionalism of corporate configs. Healthcare demos now as realistic and compelling as antitrust/safety fraud scenarios.

---

## [2.1.1] - 2026-01-16

### Changed

#### 🎭 Pop Culture Name Cleanup (Professional Dataset Readiness)
- **Feature:** Replaced all pop culture character names with realistic business names
- **Why:** Pop culture references (Tony Stark, Peter Parker, Wade Wilson, etc.) break immersion when demonstrating to clients and law firms
- **Impact:** Configs now appear professional and production-ready for client presentations
- **Changes Applied:**
  - 25 expansion personnel renamed with realistic business names
  - Email addresses updated to match new names (firstname.lastname@acmeinc.com)
  - Signatures updated (e.g., "Deadpool" → "Watson", "Stark" → "Clark")
  - Employee pool arrays updated throughout all prompt_variables sections
  - All personality styles preserved exactly (quirks and communication patterns unchanged)
- **Mapping Examples:**
  - Tony Stark → Anthony S. Clark (Consultant)
  - Peter Parker → Peter R. Patterson (Junior Dev)
  - Wade Wilson → William A. Watson (Sales Rep)
  - Steve Rogers → Steven R. Rogers (Team Lead)
  - Natasha Romanoff → Natalie R. Roman (Competitive Intelligence)
  - Jack Reacher → Jackson L. Reed (Field Technician)
  - Ron Swanson → Ronald J. Sawyer (Director of Construction)
  - Veronica Mars → Veronica R. Marshall (Fraud Investigator)
  - Yennefer Vengerberg → Jennifer L. Vandenberg (Chief of Staff)
  - And 16 more...
- **Files Modified:**
  - `config-acme-hr-misconduct.yaml`: 25 personnel updated + employee_pool arrays
  - `config-acme-antitrust.yaml`: 25 personnel updated + employee_pool arrays
  - `config-acme-safety-fraud.yaml`: 25 personnel updated + employee_pool arrays
  - `name_mapping_v2.1.1.md`: Complete mapping documentation
- **Architectural Integrity Maintained:**
  - Social graph depth preserved (5 core + 45 expansion)
  - Personality diversity unchanged (arrogant consultant, nervous intern, grumpy sysadmin, etc.)
  - Employee pool segregation intact (signal uses core 5, noise uses expansion)
  - All scenario definitions unmodified

**Result:** Dataset now suitable for client-facing demonstrations without immersion-breaking references.

---

## [2.1.0] - 2026-01-15

### Added

#### 🌡️ Temperature Control for LLM Generation
- **Feature:** Added configurable `llm_settings.temperature` to all scenarios in YAML configs
- **Why:** Control linguistic variety - lower temp for signal consistency, higher temp for noise diversity
- **Implementation:**
  - Signal scenarios (S1, S2, S_HR, S3, calendar events): `temperature: 0.4` for consistent hot docs
  - Noise scenarios (S4-S18): `temperature: 0.95` for varied mundane communications
  - Ultra-mundane scenarios (S16-S18): `temperature: 1.0` for maximum linguistic entropy
- **Code Changes:**
  - Updated `get_temperature_for_scenario()` to accept `config_temp` parameter (YAML override)
  - Updated all generation functions to pass config temperature through call chain
  - Backwards compatible - defaults to existing behavior if no `llm_settings` specified
- **Files Modified:**
  - `app.py`: Function signature updates (lines 613-632, 1240-1369, 1807-1831)
  - `config-acme-hr-misconduct.yaml`: Added llm_settings to all 30 scenarios
  - `config-acme-antitrust.yaml`: Added llm_settings to all 25 scenarios
  - `config-acme-safety-fraud.yaml`: Added llm_settings to all 28 scenarios

#### 📋 Ultra-Mundane Noise Scenarios (S16-S18)
- **Feature:** Three new noise scenario types for maximum linguistic diversity
- **Why:** Addresses feedback about "procedural template fingerprints" - adds extreme mundanity
- **New Scenarios:**
  - **(S16) Office Life Trivia:** 15 ultra-mundane topics (cake in breakroom, AC broken, lost badge, etc.)
  - **(S17) IT/System Issues:** 15 common IT problems (VPN issues, login problems, printer jammed, etc.)
  - **(S18) Micro-Collaborations:** 15 ultra-brief messages (FYI, Quick question, Thoughts?, etc.)
- **Design:**
  - All use `temperature: 1.0` for maximum variety
  - Prompts request brevity (1-2 sentences or 5-10 words)
  - Use expansion personnel appropriate to scenario type
  - Add "linguistic drift" through rushed/casual tone
- **Impact:**
  - Further dilutes signal ratio if needed
  - Adds realistic "email spam" that humans generate
  - Tests EAIDA's ability to filter truly irrelevant content
- **Files Modified:**
  - `config-acme-hr-misconduct.yaml`: Added S16-S18 (lines 1048-1130)
  - `config-acme-antitrust.yaml`: Added S16-S18 (lines 999-1081)
  - `config-acme-safety-fraud.yaml`: Added S16-S18 (lines 1043-1125)

### Impact Summary

**Before v2.1.0:**
- All LLM calls used hardcoded temperature logic (0.85 for threads, 0.95 for standalone, etc.)
- Signal emails had same temp as some noise, reducing consistency
- Noise had good variety but not maximum diversity

**After v2.1.0:**
- Signal scenarios use temp 0.4 → more consistent hot docs (better for training reviewers)
- Noise scenarios use temp 0.95 → high variety in mundane business communications
- Ultra-mundane scenarios use temp 1.0 → maximum linguistic entropy (addresses "fingerprint" concerns)
- All configurable via YAML without code changes

**New Scenario Count:**
- HR Misconduct: 27 → 30 scenarios
- Antitrust: 22 → 25 scenarios
- Safety Fraud: 25 → 28 scenarios

---

## [2.0.3] - 2026-01-15

### Changed

#### 🔄 Noise Scenarios Now Use Expansion Personnel (Phase 2/2)
- **Feature:** Updated all noise scenario `employee_pool` variables to use expansion personnel
- **Why:** Phase 1 added 45 expansion personnel, but noise scenarios still only used core 5
- **Impact:** Noise emails now come from appropriate staff (not CEOs discussing broken dishwashers)
- **Scenario Assignments:**
  - **(S7) Personal emails:** Junior staff (Brandon Hayes, Marcus Dillon, Lisa Wong, etc.)
  - **(S8) Fragments:** Operations (Marcus Dillon, Greg MacIntyre, Tom Wozniak, etc.)
  - **(S9) Typos:** Junior/rushed staff with intentional name typos (Brandon Hays, Peter Parkr, etc.)
  - **(S10) Vague emails:** Various quirky personalities (Tony Stark, Wade Wilson, Ron Swanson, etc.)
  - **(S11) Auto-replies:** Sales/marketing traveling staff (Victor Krum, Lisa Wong, Kevin O'Connor, etc.)
  - **(S12) Meeting scheduling:** Admins and EAs (Rachel Green, Gina Linetti, Erica Sinclair, etc.)
  - **(S13) Blast emails:** Leadership/executives (Yennefer Vengerberg, Steve Rogers, Veronica Mars, etc.)
- **Files Modified:**
  - `config-acme-antitrust.yaml`: Updated 7 noise scenarios
  - `config-acme-safety-fraud.yaml`: Updated 6 noise scenarios
  - `config-acme-hr-misconduct.yaml`: Updated 7 noise scenarios
- **Result:** "Small Universe" problem fully solved - noise now distributed across 40+ employees

---

## [2.0.2] - 2026-01-15

### Added

#### 👥 Expansion Personnel for Organizational Depth
- **Feature:** All three focused investigation configs now include 50 total personnel (5 core + 45 expansion)
- **Why:** Solves the "Small Universe" problem where only 5 people send all emails
- **Impact:**
  - Realistic organizational depth for volume testing (1000+ documents)
  - Proper noise distribution (expansion personnel send routine business emails)
  - Better search/filtering testing (50 names vs 5 names)
  - Signal scenarios still focus on core 5 custodians
- **Expansion Personnel Include:**
  - Engineering staff (Data Architect, Developers, QA, DevOps)
  - Operations (Facilities, Warehouse, Office Manager, Security)
  - HR/Admin (Payroll, Benefits, Events, Receptionist)
  - Sales/Marketing (Reps, Copywriter, Social Media, Content)
  - IT/Security (SysAdmin, DBA, InfoSec, SOC)
  - Specialists (Compliance, Legal, UX, Design, Consultants)
- **Files Modified:**
  - `config-acme-antitrust.yaml`: 5 → 50 personnel (+45)
  - `config-acme-safety-fraud.yaml`: 5 → 50 personnel (+45)
  - `config-acme-hr-misconduct.yaml`: 5 → 50 personnel (+45)
- **Documentation:** Updated config headers with personnel notes
- **Next Step:** Phase 2 will update noise scenario employee_pool to use expansion personnel

---

## [2.0.1] - 2026-01-15

### Changed

#### 🔧 YAML Configuration Refactoring
- **Improvement:** Refactored S4 duplicate scenarios to use YAML anchors for DRY compliance
- **Impact:** Reduced config file sizes by ~36% (450+ lines per file)
- **Before:** Each S4 duplicate repeated 100+ topic variables (117 lines × 4 = 468 lines)
- **After:** Single template definition with anchor references (16 lines total)
- **Files Modified:**
  - `config-acme-antitrust.yaml`: 1183 → 761 lines (-422 lines)
  - `config-acme-safety-fraud.yaml`: 1260 → 804 lines (-456 lines)
  - `config-acme-hr-misconduct.yaml`: 1249 → 801 lines (-448 lines)
- **Benefit:** Easier maintenance, no functionality change, same signal/noise ratios
- **Documentation:** Updated CONFIGS_GUIDE.md with YAML anchor examples

---

## [2.0.0] - 2026-01-15

### Added

#### 🎯 Interactive Scenario Filter Selection
- **Feature:** When selecting `config-acme.yaml`, users are now prompted to choose which investigation type to generate
- **Options:**
  1. Antitrust Investigation Only
  2. Safety Fraud Investigation Only
  3. HR Misconduct Investigation Only
  4. All Scenarios Mixed (Infrastructure Stress Testing)
  5. Custom Combination
- **Benefit:** Use the large 50+ custodian roster with focused investigation scenarios without manual YAML editing
- **Files Modified:** `app.py` (added `get_scenario_filter_preference()` function), `README.md`

#### 📎 Email-Attachment Content Alignment
- **Feature:** Attachments now align with email content narratives
- **How it works:** When generating attachments, the LLM receives the email's subject and body text to ensure the attachment content matches what the email describes
- **Example:**
  - Email: "See attached report showing catastrophic failure in Test Run #4"
  - Attachment: Now actually contains data about Test Run #4 catastrophic failure
- **Impact:** Dramatically improves realism for EAIDA content correlation testing
- **Files Modified:** `app.py` (`generate_attachment_text_from_llm()`, `create_and_save_email()`)

#### ⏰ Scenario-Aware Temporal Logic
- **Feature:** Timestamps now reflect realistic investigation patterns
- **Patterns Implemented:**
  - **Fraud/Coverup:** Fast panic replies (30 min - 4 hours) OR deliberate delays (24-72 hours)
  - **Urgent emails:** Quick responses based on content keywords (urgent, ASAP, critical, emergency)
  - **Privilege consultations:** Same-day or next-business-day responses
  - **Friday evening → Monday morning:** 70% of Friday 5pm+ emails wait until Monday 8-10 AM
  - **Weekend gaps:** 90% of emails avoid Saturday/Sunday
  - **Business hours:** 80% during 8 AM - 6 PM, with fraud scenarios extending to 11 PM
- **Example Timeline:**
  ```
  Day 1, 2:30 PM: "Catastrophic test failure discovered" (initial alarm)
  Day 1, 3:45 PM: "This data cannot leave this room" (panic reply - 75 min later)
  Day 3, 9:15 AM: "Here's the plan for the report" (deliberate delay - 43 hours later)
  ```
- **Impact:** Timeline reconstruction in EAIDA now tests realistic temporal patterns
- **Files Modified:** `app.py` (`generate_realistic_timestamp()`, `generate_email_thread()`, `generate_standalone_email()`)

#### 🔒 Enhanced Privilege Scenarios
- **Feature:** Added four new privilege scenario variations to improve privilege screening testing realism
- **New Scenarios:**
  - **S3B: Subtle Privilege** - No "PRIVILEGED" markers in subject line, but body clearly seeks legal advice from General Counsel
  - **S3C: Privilege by Recipient** - Business email to GC becomes privileged when seeking legal guidance
  - **S3D: Mixed Privilege Thread** - Email thread starts non-privileged, becomes privileged when GC is added mid-conversation
  - **S3E: Privilege Waiver** - Privileged email improperly forwarded to non-attorneys (tests waiver understanding)
- **Investigation-Specific Customization:**
  - Antitrust: Privilege scenarios involve pricing discussions, collusion concerns, Sherman Act analysis
  - Safety Fraud: Privilege scenarios involve FDA reporting, test failure documentation, regulatory obligations
  - HR Misconduct: Privilege scenarios involve Title VII liability, harassment complaints, investigation procedures
- **Why This Matters:**
  - Previous privilege scenarios were too obvious (just search for "PRIVILEGED" keyword)
  - New scenarios require EAIDA to understand privilege by context, recipient, and thread evolution
  - Tests subtle privilege detection (no header markers)
  - Tests privilege by recipient logic (emails to GC may be privileged even without markers)
  - Tests privilege waiver scenarios (improper disclosure)
- **Example:**
  ```
  Subject: Need your advice on pricing discussions (S3B - subtle, no "PRIVILEGED" marker)
  From: Taylor Brooks
  To: Drew Foster (General Counsel)
  Body: "Drew, I need your legal guidance on some pricing coordination discussions that came up..."

  vs.

  Subject: CONFIDENTIAL AND PRIVILEGED (S3 - obvious marker)
  ```
- **Impact:** Dramatically improves privilege screening testing realism for EAIDA
- **Files Modified:** `config-acme-antitrust.yaml`, `config-acme-safety-fraud.yaml`, `config-acme-hr-misconduct.yaml` (added S3B-S3E scenarios after existing S3)

#### 💬 Chat Realism Improvements
- **Feature:** Complete overhaul of chat generation to match modern workplace messaging patterns
- **Five Key Enhancements:**
  1. **Rapid-Fire Short Messages** - LLM now generates 1-3 sentence messages instead of email paragraphs. Breaks thoughts into multiple quick messages sent seconds apart ("hey", "can you check this?", "seems off")
  2. **Realistic Message Timing** - Short messages = 5-30 sec gaps (rapid texting), medium = 20-120 sec (typing), long = 1-5 min (thoughtful response)
  3. **Emoji/Reactions** - 30% of short confirmations get 👍 reactions, 15% of other messages. Multiple users (1-3) react to messages. Teams/Slack both supported.
  4. **Edit History** - 10% of longer messages show edit timestamps (typo fixes, clarifications)
  5. **Thread Support** - Infrastructure for threaded conversations (side discussions branching from main channel)
- **LLM Prompt Changes:**
  - Explicit instructions to use casual tone, lowercase, abbreviations (btw, fyi, lol)
  - Encourage emoji usage (👍 😅 🔥) and quick responses ("ok", "got it", "will do")
  - Break up multi-part thoughts into separate rapid-fire messages
  - Simulate natural interruptions (people reply before others finish)
- **Example Transformation:**
  ```
  BEFORE: [10:00:00] "Hi Rachel, I wanted to follow up on our pricing discussion from last week..."

  AFTER:  [10:00:05] "hey rachel"
          [10:00:12] "following up on that pricing thing"
          [10:00:18] "think we should stick to that 15% baseline?"
          [10:00:35] "yep"
          [10:00:42] "makes sense for keeping things stable 👍"
  ```
- **Why This Matters:**
  - Chat is increasingly important in e-discovery (Slack, Teams, Webex everywhere)
  - Previous chat logs sounded like formal emails, not realistic workplace messaging
  - EAIDA needs to parse emoji, reactions, edit history, threads
  - Better training data for chat analysis ML models
- **Impact:** Dramatically improves chat realism for testing modern e-discovery tools
- **Files Modified:** `app.py` (`generate_chat_content_from_llm`, `create_and_save_slack_native`, `create_and_save_rsmf`)

#### ⚡ Parallel Execution with Rate Limit Handling
- **Feature:** Dataset generation now runs with parallel LLM calls using ThreadPoolExecutor
- **Performance Improvement:**
  - **Before:** Serial execution (~50 minutes for 500 items)
  - **After:** 10 parallel workers (~5-7 minutes for 500 items)
  - **Speedup:** 7-10x faster generation
- **Rate Limit Protection:**
  - Automatic retry with exponential backoff for 429 errors (2s, 4s, 8s, 16s, 32s)
  - Max 5 retries before failure
  - Thread-safe stats tracking with locks
- **Configuration:** `MAX_WORKERS = 10` (adjustable in code, line 1777)
- **Tuning Guidance:**
  - Reduce workers if you get frequent 429 errors
  - Increase workers (15-20) if no rate limit errors occur
  - Monitor first run to find optimal setting for your Azure OpenAI quota
- **Impact:** Dramatically reduces wait time for large dataset generation while gracefully handling API rate limits
- **Files Modified:** `app.py` (added `ThreadPoolExecutor`, `call_llm_with_retry`, parallel scenario processing)

### Fixed

#### 🐛 Missing Prompts Key in Config Files
- **Issue:** Three scenarios were missing the required `prompts` field, causing KeyError when those scenarios were selected
- **Affected Scenarios:**
  - S5 (Generic HR or admin announcements) in `config-acme-safety-fraud.yaml`
  - S7 (Generic engineering team emails) in `config-acme-safety-fraud.yaml`
  - S5 (Generic HR or admin announcements) in `config-acme-hr-misconduct.yaml`
- **Fix:** Added missing `prompts` fields with appropriate prompt templates for each scenario
- **Impact:** All scenarios now work without errors. Users can generate datasets without encountering KeyError exceptions.
- **Files Modified:** `config-acme-safety-fraud.yaml`, `config-acme-hr-misconduct.yaml`

#### 🐛 Hardcoded Report Signal/Noise Descriptions
- **Issue:** Certification report always showed "Price Fixing (Antitrust), Safety Fraud (Liability), Privilege" regardless of which config was used
- **Example:** Running HR misconduct config incorrectly claimed to include antitrust and safety fraud scenarios
- **Fix:** Report now dynamically generates signal and noise descriptions based on actual scenarios present in the dataset
  - Detects S1 (Antitrust), S2 (Safety), S_HR (Harassment), S3 (Privilege)
  - Generates accurate descriptions: "Workplace Harassment (HR), Privilege (Attorney-Client)" for HR config
  - Noise description also dynamic based on actual noise scenarios present
- **Impact:** Certification reports now accurately reflect the investigation type(s) in each specific dataset
- **Files Modified:** `app.py` (lines 1877-1933)

### Changed

#### ⚖️ Signal/Noise Ratio Tuning Support
- **Feature:** Configs now support adjustable signal/noise ratios for realistic "needle in haystack" testing
- **Implementation:** Added duplicate noise scenarios in config-acme-hr-misconduct.yaml (S4 duplicated 4x)
- **Current Ratios:**
  - config-acme-antitrust.yaml: ~60% signal
  - config-acme-safety-fraud.yaml: ~60% signal
  - config-acme-hr-misconduct.yaml: ~59% signal (with S4 duplicates)
- **Target Ratio:** ~25% signal / 75% noise for realistic e-discovery environments
- **How to Achieve Target:**
  - **Option 1 (Easiest):** Generate 1500-2000 items instead of 500-1000 (noise repeats more over larger datasets)
  - **Option 2 (More Control):** Add duplicate noise scenario entries in config YAML files
- **Why It Matters:** Real e-discovery datasets have 15-30% hot documents, rest is business context
- **Documentation:** Added tuning guide to CONFIGS_GUIDE.md and README.md
- **Files Modified:** `config-acme-hr-misconduct.yaml` (added S4 duplicates), `CONFIGS_GUIDE.md`, `README.md`

#### 📋 Documentation Updates
- **ARCHITECTURE.md (NEW):** Created comprehensive architecture guide covering:
  - What the tool does and why it matters (e-discovery testing challenge, EAIDA validation needs)
  - Core concepts (signal/noise, investigation types, privilege, realism patterns)
  - System architecture with detailed component breakdown and data flow diagrams
  - Step-by-step generation workflow (7 phases from config loading to certification report)
  - Key design decisions with rationale (why LLM vs templates, why privilege is automatic, etc.)
  - Use cases (EAIDA validation, sales demos, training, ML training data, performance testing)
  - Extension guide (adding investigation types, scenarios, output formats)
  - Technical specifications, FAQs, and performance benchmarks
- **README.md:** Added ARCHITECTURE.md link to "Architecture & System Design" section
- **README.md:** Updated "Available Configurations" table to show config-acme.yaml as "Interactive - Choose your type"
- **README.md:** Added "Using config-acme.yaml (Interactive Mode)" usage section with example flow
- **README.md:** Enhanced "Scenario Filtering" section with "Interactive Filter Selection" subsection
- **README.md:** Updated "Slow Generation" troubleshooting to recommend focused configs

### Removed

#### 🗑️ Config-acme-dense.yaml Removed
- **Reason:** Redundant after focused configs were expanded with massive topic variety (99-103 topics per scenario)
- **Replacement:** Use focused configs (config-acme-antitrust.yaml, config-acme-safety-fraud.yaml, config-acme-hr-misconduct.yaml) for dense, focused datasets
- **Files Modified:** Deleted `Config-acme-dense.yaml`, updated `README.md`

---

## [1.0.0] - 2025-12-XX

### Initial Release

#### Core Features
- Generate RFC-compliant email (.eml) datasets
- Multi-format chat support (Slack JSON, Teams RSMF, Webex JSON)
- Calendar event generation (.ics files)
- Three focused investigation types:
  - Antitrust price-fixing
  - Product safety fraud
  - Workplace harassment
- Attorney-client privilege scenarios
- Realistic business noise (S4-S13 scenarios)
- LLM-powered content generation via Azure OpenAI
- Attachment generation (PDF, DOCX, XLSX, logs)
- Email threading with proper headers
- Near-duplicate generation
- Custodian-based folder organization
- Stress testing features (blast emails, large logs, nested containers)
- Investigation protocol document generation

#### Configuration Files
- `config-acme-antitrust.yaml` - Price-fixing investigation (5 custodians)
- `config-acme-safety-fraud.yaml` - Safety fraud investigation (5 custodians)
- `config-acme-hr-misconduct.yaml` - HR misconduct investigation (5 custodians)
- `config-acme.yaml` - Master config with 50+ custodians, all scenarios

#### Documentation
- `README.md` - Main documentation
- `QUICK_START_ANTITRUST.md` - Antitrust investigation quick start
- `QUICK_START_SAFETY_FRAUD.md` - Safety fraud investigation quick start
- `QUICK_START_HR_HARASSMENT.md` - HR investigation quick start
- `CONFIGS_GUIDE.md` - Configuration options reference
- `README_SCENARIO_FILTERING.md` - Detailed filtering documentation

---

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version: Incompatible API/config changes
- **MINOR** version: New features in a backwards-compatible manner
- **PATCH** version: Backwards-compatible bug fixes

---

## Upgrade Notes

### From 1.x to 2.0

**Breaking Changes:**
- None - All 1.x configs remain compatible

**New Features:**
- Interactive filter selection when using config-acme.yaml
- Improved timestamp realism (automatic, no config changes needed)
- Better attachment-email alignment (automatic, no config changes needed)

**Deprecated:**
- Config-acme-dense.yaml removed (use focused configs instead)

**Migration Steps:**
1. Update to latest version
2. If using Config-acme-dense.yaml, switch to focused configs:
   - For small antitrust datasets → `config-acme-antitrust.yaml`
   - For small safety fraud datasets → `config-acme-safety-fraud.yaml`
   - For small HR datasets → `config-acme-hr-misconduct.yaml`
3. No other changes required - existing configs work as-is

---

## Roadmap

### Planned for 2.1.0 (Q1 2026)
- [ ] Enhanced privilege scenarios (subtle privilege, privilege waiver)
- [ ] Improved near-duplicate patterns (forward chains, version drift)
- [ ] Chat realism enhancement (rapid-fire messages, emoji, threads)

### Planned for 2.2.0 (Q2 2026)
- [ ] LLM entity consistency enforcement
- [ ] Dynamic protocol document with actual generation stats
- [ ] Additional stress test scenarios

### Under Consideration
- [ ] Coded language sophistication
- [ ] Multi-language support for noise scenarios
- [ ] Custom investigation type framework
- [ ] Cost estimation and dry-run mode

---

## Contributing

See [ENHANCEMENTS_2026-01.md](ENHANCEMENTS_2026-01.md) for detailed enhancement analysis and future improvement opportunities.

To contribute:
1. Review enhancement priorities in ENHANCEMENTS_2026-01.md
2. Follow existing code patterns in app.py
3. Update CHANGELOG.md and documentation
4. Test with focused configs (100-200 items)

---

## Support

- **Issues:** Report via GitHub Issues (or internal tracking)
- **Questions:** See README.md and QUICK_START guides
- **Feature Requests:** Review ENHANCEMENTS_2026-01.md first

---

## License

Proprietary - For EAIDA testing and e-discovery tool validation only.
