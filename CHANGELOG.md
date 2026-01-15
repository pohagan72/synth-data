# Changelog

All notable changes to the Synthetic E-Discovery Dataset Generator.

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
