# Pop Culture Name Cleanup - v2.1.1 Mapping

This document maps all pop culture character names to realistic business names while preserving personality styles.

## Mapping Table

| Original Name (Pop Culture) | New Name (Realistic) | Title | Rationale |
|----------------------------|---------------------|-------|-----------|
| Tony Stark | Anthony S. Clark | Consultant | Keeps "Tony" → Anthony, Stark → Clark |
| Peter Parker | Peter R. Patterson | Junior Dev (Web) | Keeps "Peter", Parker → Patterson |
| Steve Rogers | Steven R. Rogers | Team Lead | "Steve Rogers" is common enough, just formalize to "Steven" |
| Natasha Romanoff | Natalie R. Roman | Competitive Intelligence | Natasha → Natalie, Romanoff → Roman |
| Wade Wilson | William A. Watson | Sales Rep | Wade → William, Wilson → Watson |
| Jack Reacher | Jackson L. Reed | Field Technician | Jack → Jackson, Reacher → Reed |
| Ron Swanson | Ronald J. Sawyer | Director of Construction | Ron → Ronald, Swanson → Sawyer |
| Rachel Green | Rachel M. Greene | Executive Assistant | Keep Rachel, Green → Greene (common spelling) |
| Gina Linetti | Gina M. Lindsey | Admin Assistant | Linetti → Lindsey |
| Kara Danvers | Kara J. Daniels | Receptionist | Danvers → Daniels |
| Oliver Queen | Oliver T. Quinn | CSR Lead | Queen → Quinn |
| Bruce Banner | (Not in config) | - | N/A |
| Ursula Buffay | Ursula K. Buffington | HR Generalist | Buffay → Buffington |
| Veronica Mars | Veronica R. Marshall | Fraud Investigator | Mars → Marshall |
| Xena Lawless | Xena R. Lawrence | Security Guard | Lawless → Lawrence |
| Victor Krum | Victor D. Kramer | Regional Sales Director (EU) | Krum → Kramer |
| Leonard Hofstadter | Leonard M. Hoffman | Experimental Physicist | Hofstadter → Hoffman |
| Meredith Grey | Meredith L. Gray | Corporate Health Officer | Grey → Gray (spelling variation) |
| Derek Shepherd | Derek J. Sheffield | Solutions Architect | Shepherd → Sheffield |
| Iris West | Iris M. Westfield | Content Marketing | West → Westfield |
| Frank Castle | Franklin R. Castillo | Physical Security | Frank → Franklin, Castle → Castillo |
| Harry Bosch | Harrison P. Boswell | Legal Counsel (Contract) | Harry → Harrison, Bosch → Boswell |
| Clara Oswin | Clara J. Osborne | QA Tester | Oswin → Osborne |
| Alice Chen | Alice R. Chen | Frontend Developer | Keep (common name, no pop culture) |
| Bob Drax | Robert L. Drake | Database Admin | Bob → Robert, Drax → Drake |
| Zack Morris | Zachary T. Morrison | Sales Intern | Zack → Zachary, Morris → Morrison |
| Yennefer Vengerberg | Jennifer L. Vandenberg | Chief of Staff | Yennefer → Jennifer, Vengerberg → Vandenberg |
| Quentin Beck | Quentin R. Becker | VFX / Media Specialist | Beck → Becker |
| Erica Sinclair | Erica M. Sinclair | Office Manager | Keep (common name) |
| Samantha Power | Samantha K. Powers | Benefits Coordinator | Power → Powers (common surname) |

## Names to Keep (Not Pop Culture)

These names are common enough or ambiguous enough to not break immersion:

- Elena Rostova ✅
- Marcus J. Dillon ✅
- Sarah Jenkins ✅
- Dr. Aris Thorne ✅
- Kevin O'Connor ✅
- Priya Desai ✅
- Tom Wozniak ✅
- Lisa Wong ✅
- Brandon Hayes ✅
- Fatima Al-Sayed ✅
- Greg 'Mac' MacIntyre ✅
- Jenny Kim ✅
- Oscar Martinez ✅
- David Mueller ✅
- Ian Fletcher ✅
- Holly Vance ✅

## Email Address Changes

All email addresses will be updated to match new last names while preserving firstname.lastname format:

- tony.stark@acmeinc.com → anthony.clark@acmeinc.com
- peter.parker@acmeinc.com → peter.patterson@acmeinc.com
- steve.rogers@acmeinc.com → steven.rogers@acmeinc.com (no change needed)
- wade.wilson@acmeinc.com → william.watson@acmeinc.com
- etc.

## Signature Changes

Signatures will be updated to match new names but preserve style:
- "Stark" → "Clark"
- "Deadpool" → "Watson"
- etc.

## Implementation Plan

1. Update config-acme-hr-misconduct.yaml (30 scenarios, 50 personnel)
2. Update config-acme-antitrust.yaml (25 scenarios, 50 personnel)
3. Update config-acme-safety-fraud.yaml (28 scenarios, 50 personnel)
4. Update config-acme.yaml (if needed)
5. Commit as v2.1.1 with clear changelog entry
