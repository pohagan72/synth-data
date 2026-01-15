# Scenario Filtering Feature

## Overview

The synthetic data generator supports **scenario filtering** to create focused datasets for specific investigation types. This allows you to generate demo data tailored to a single legal matter rather than mixing multiple unrelated scenarios.

## Why Use Scenario Filtering?

**Before:** One dataset contained price-fixing, safety fraud, privilege, AND HR misconduct scenarios mixed together - unrealistic for demo purposes.

**After:** Generate separate focused datasets:
- **Antitrust Investigation Dataset** - Price-fixing communications
- **Product Liability Dataset** - Safety test manipulation
- **HR Investigation Dataset** - Workplace misconduct (requires custom scenarios)

## Important: Investigation Types vs Review Tasks

**Investigation Types** (what you're investigating):
- **Antitrust** - Price-fixing, collusion
- **Safety Fraud** - Test manipulation, regulatory violations
- **HR Misconduct** - Harassment, discrimination, abuse of resources

**Review Tasks** (screening done in EVERY investigation):
- **Attorney-Client Privilege (S3)** - Now included automatically with all investigation types
- Privilege screening is a workflow step, not an investigation scenario
- Every real e-discovery project needs privilege review, regardless of the matter type

## How to Use

### In Your YAML Config File

Add the `scenario_filter` setting under `general_settings`:

```yaml
general_settings:
  output_directory: "ediscovery_dataset_antitrust"
  scenario_filter: 'antitrust'  # Focus on price-fixing investigation
```

### Available Filters

| Filter Value | What It Includes | Best For |
|-------------|------------------|----------|
| `'all'` | All scenarios (default) | Testing variety, stress testing |
| `'antitrust'` | S1, S1A, S1B + privilege (S3) + noise | Price-fixing investigations |
| `'safety_fraud'` | S2 + privilege (S3) + noise | Product liability, regulatory violations |
| `'hr_misconduct'` | (S_HR) + privilege (S3) + noise | HR/workplace investigations* |
| `'antitrust_only'` | S1, S1A, S1B (NO noise or privilege) | Signal-only testing |
| `['antitrust', 'safety_fraud']` | Multiple types + privilege + noise | Combined investigations |

*Note: HR misconduct scenarios require custom (S_HR) tagged scenarios to be added to your YAML

### What is "Noise"?

Contextual noise scenarios (S3-S15) include:
- **Attorney-client privilege communications (S3)** - Now part of noise!
- Project management emails
- HR announcements
- Personal/non-work emails
- Meeting scheduling
- Sales chatter
- Foreign language communications
- Email fragments and typos

**By default, noise (including privilege) is included** to make the dataset realistic.

To exclude noise and privilege, add `_only` suffix:
```yaml
scenario_filter: 'antitrust_only'  # Only S1, S1A, S1B - no noise or privilege
```

## Examples

### Example 1: Antitrust Investigation Demo
```yaml
general_settings:
  output_directory: "demo_antitrust_investigation"
  scenario_filter: 'antitrust'
```

**Result:** Price-fixing emails PLUS privilege documents to screen PLUS business noise.

### Example 2: Product Safety Liability
```yaml
general_settings:
  output_directory: "demo_product_safety_fraud"
  scenario_filter: 'safety_fraud'
```

**Result:** Safety test manipulation PLUS privilege documents PLUS R&D/engineering noise.

### Example 3: HR Misconduct (Custom)
```yaml
general_settings:
  output_directory: "demo_hr_investigation"
  scenario_filter: 'hr_misconduct'
```

**Result:** Requires adding (S_HR) tagged scenarios to your YAML first.

### Example 4: Multiple Investigation Types
```yaml
general_settings:
  output_directory: "demo_combined_investigation"
  scenario_filter: ['antitrust', 'safety_fraud']
```

**Result:** Both price-fixing AND safety fraud scenarios (useful for complex matters).

## Scenario Tag Reference

| Tag | Description | Key Personnel | Included In |
|-----|-------------|---------------|-------------|
| (S1) | Price-fixing email thread | Jamie Chen, Rachel Quinn | 'antitrust' filter |
| (S1A) | Calendar invite for collusion meeting | Jamie Chen | 'antitrust' filter |
| (S1B) | Teams/Slack chat about pricing | Jamie Chen, Rachel Quinn | 'antitrust' filter |
| (S2) | Safety test result manipulation | Casey Mitchell, Peyton Parker | 'safety_fraud' filter |
| (S3) | **Attorney-client privilege** | Drew Foster, Eleanor Vance | **ALL filters (noise)** |
| (S4-S15) | Contextual noise scenarios | Various employees | ALL filters (noise) |
| (S_HR) | HR misconduct (custom) | To be added | 'hr_misconduct' filter |

## Tips for EAIDA Demos

1. **Use focused filters** - One investigation type per demo dataset
2. **Keep noise enabled** - Makes the investigation realistic
3. **Privilege is automatic** - Every investigation now includes privilege docs to screen
4. **Adjust output_directory** - Use descriptive folder names
5. **Generate multiple datasets** - One per investigation type
6. **Match the scenario to your audience** - Antitrust for compliance, safety fraud for product liability

## Why This Change?

**Old approach:** `legal_privilege` was a standalone filter, implying you only screen for privilege on "privilege investigations"

**New approach:** Privilege (S3) is now included with ALL investigations, because in real e-discovery:
- Every investigation requires privilege screening
- You don't "investigate privilege" - you protect privileged documents
- Privilege review is a workflow step, not a case type
- EAIDA would need to identify privilege docs in any matter

## Troubleshooting

**"No scenarios match the filter!"**
- Valid filters: `'all'`, `'antitrust'`, `'safety_fraud'`, `'hr_misconduct'`
- `'legal_privilege'` removed - privilege now included with all filters
- Check your spelling and YAML syntax
- For `'hr_misconduct'`, you need to add (S_HR) tagged scenarios first

**Filter isn't working**
- Make sure `scenario_filter` is under `general_settings` in YAML
- Restart the app after changing the config file
- Check for typos in the filter value

## Summary

The scenario filtering feature lets you create **focused, realistic datasets** for specific investigation types - with attorney-client privilege documents automatically included in every dataset, just like real e-discovery workflows.
