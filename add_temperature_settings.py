#!/usr/bin/env python3
"""
Script to add llm_settings.temperature to all scenarios in focused config files.
Signal scenarios (S1, S2, S_HR, S3, calendar events) get temp 0.4 for consistency.
Noise scenarios (S4-S18) get temp 0.95 for variety.
"""

import re
import sys

def add_temperature_to_file(filepath):
    """Add temperature settings to a single config file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = []
    changes_made = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        modified.append(line)

        # Check if this is a scenario start (type: "...")
        if re.match(r'^\s*-\s+type:\s+"(thread|standalone|chat|calendar_event)"', line):
            # Look ahead to find description and check for llm_settings
            j = i + 1
            description = None
            has_llm_settings = False
            indent_level = len(line) - len(line.lstrip())

            while j < len(lines):
                next_line = lines[j]
                next_indent = len(next_line) - len(next_line.lstrip())

                # If we hit another scenario or same-level key, stop looking
                if next_indent <= indent_level and next_line.strip() and not next_line.strip().startswith('#'):
                    break

                # Check for description
                if 'description:' in next_line:
                    description = next_line

                # Check for llm_settings
                if 'llm_settings:' in next_line:
                    has_llm_settings = True

                j += 1

            # Add llm_settings if not present
            if not has_llm_settings and description:
                # Determine if signal or noise
                is_signal = False
                desc_lower = description.lower()

                # Signal scenarios
                if any(tag in description for tag in ['(S1)', '(S2)', '(S_HR)', '(S3)', '(HR5)', '(HR6)', '(HR7)', '(HR8)', '(S1A)', '(S1B)', '(S2A)', '(S2B)', '(S2C)', '(S2D)']):
                    is_signal = True

                # Choose temperature
                temp = 0.4 if is_signal else 0.95

                # Find insertion point (after description line)
                desc_line_idx = None
                for k in range(i+1, j):
                    if 'description:' in modified[k]:
                        desc_line_idx = k
                        break

                if desc_line_idx:
                    # Insert llm_settings after description
                    indent = ' ' * (indent_level + 2)
                    llm_settings_lines = [
                        f"{indent}llm_settings:\n",
                        f"{indent}  temperature: {temp}  # {'Signal: Lower temp for consistency' if is_signal else 'Noise: Higher temp for variety'}\n"
                    ]

                    # Insert after description line
                    modified[desc_line_idx+1:desc_line_idx+1] = llm_settings_lines
                    changes_made += 1

                    print(f"Added temperature={temp} to scenario: {description.strip()}")

        i += 1

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(modified)

    print(f"\nMade {changes_made} changes to {filepath}")
    return changes_made

if __name__ == "__main__":
    files = [
        "config-acme-hr-misconduct.yaml",
        "config-acme-antitrust.yaml",
        "config-acme-safety-fraud.yaml"
    ]

    total_changes = 0
    for filepath in files:
        print(f"\n{'='*60}")
        print(f"Processing: {filepath}")
        print('='*60)
        try:
            changes = add_temperature_to_file(filepath)
            total_changes += changes
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    print(f"\n\n{'='*60}")
    print(f"Total changes made across all files: {total_changes}")
    print('='*60)
