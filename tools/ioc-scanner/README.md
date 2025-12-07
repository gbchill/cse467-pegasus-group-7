# Pegasus IOC Scanner - Educational Tool

## Overview

This is a simple educational tool that demonstrates how Indicators of Compromise (IOCs) can be used to detect potential Pegasus infections by pattern matching against log files.

**IMPORTANT:** This is a demonstration tool, not a production security scanner. For actual forensic analysis, use professional tools like MVT (Mobile Verification Toolkit).

## What It Does

The scanner:
1. Loads IOC databases (domains, processes, patterns)
2. Scans log files for matches
3. Reports findings with severity ratings
4. Provides basic recommendations

## Installation

No external dependencies required - uses Python 3 standard library only.

**Requirements:**
- Python 3.6 or higher

**No pip install needed!**

## Usage

### Basic Scan

```bash
python scanner.py --log sample-logs/sample-sysdiagnose.log
```

### Export Results to JSON

```bash
python scanner.py --log sample-logs/sample-sysdiagnose.log --output results.json
```

### Custom IOC Directory

```bash
python scanner.py --log mylog.txt --iocs /path/to/custom/iocs/
```

### Help

```bash
python scanner.py --help
```

## IOC Databases

The scanner uses three types of IOC databases:

### 1. `iocs/domains.txt`
Known NSO Group C2 domains
- One domain per line
- Comments start with #
- Example: `infections.pegasusinfections.com`

### 2. `iocs/processes.txt`
Suspicious process names
- One process per line
- Comments start with #
- Example: `bridgekeeper`

### 3. `iocs/patterns.txt`
Regex patterns for log analysis
- Format: `pattern|severity|description`
- Severities: CRITICAL, HIGH, MEDIUM, LOW
- Example: `.*FORCEDENTRY.*|CRITICAL|Potential FORCEDENTRY exploit`

## Sample Data

Try the scanner with included sample log:

```bash
python scanner.py --log sample-logs/sample-sysdiagnose.log
```

The sample log contains:
- Normal system activity
- Simulated suspicious domain connections
- Fake process indicators
- Example exploitation patterns

**Expected output:** Multiple CRITICAL and HIGH severity findings

## Understanding Results

### Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| CRITICAL | Strong indicator of compromise | Immediate professional analysis recommended |
| HIGH | Suspicious activity warranting investigation | Further analysis needed |
| MEDIUM | Potentially suspicious but likely benign | Review context |
| LOW | Informational | Awareness only |

### False Positives

**Important:** IOC matching produces false positives!

- Legitimate services may use similar domains
- Normal processes may match suspicious names
- Benign crashes can resemble exploitation

**Always verify findings manually.**

## Limitations

This tool:
- ✗ Cannot detect unknown exploits
- ✗ Does not analyze memory
- ✗ Cannot detect zero-days
- ✗ Has no AI/ML capabilities
- ✗ Produces false positives
- ✓ Demonstrates IOC matching concept
- ✓ Useful for education and awareness
- ✓ Shows basic detection methodology

## For Actual Detection

Use professional tools:

### Mobile Verification Toolkit (MVT)
```bash
pip3 install mvt
mvt-ios check-backup --iocs indicators.stix2 /path/to/backup
```

See: https://github.com/mvt-project/mvt

### IOC Databases

- Amnesty Tech: https://github.com/AmnestyTech/investigations
- Citizen Lab reports: https://citizenlab.ca/category/research/

## Customizing IOCs

You can add your own IOCs:

### Add Domain

Edit `iocs/domains.txt`:
```
# My custom domains
suspicious-domain.com
example-c2.net
```

### Add Process

Edit `iocs/processes.txt`:
```
# My custom process names
malware_process
suspicious_daemon
```

### Add Pattern

Edit `iocs/patterns.txt`:
```
.*custom.*pattern.*|HIGH|My custom indicator description
```

## Example Output

```
================================================================================
Pegasus IOC Scanner v1.0 - Educational Tool
================================================================================

WARNING: This is an educational demonstration tool.
For actual forensic analysis, use MVT (Mobile Verification Toolkit).

Scanning: sample-logs/sample-sysdiagnose.log
IOC Database Loaded:
  - Domains: 15
  - Processes: 8
  - Patterns: 22

Analyzing log file...

================================================================================
FINDINGS:

[CRITICAL] Suspicious Domain Detected
  Line 10: Known NSO infrastructure domain: infections.pegasusinfections.com
  Context: DNS query for infections.pegasusinfections.com...

[HIGH] Suspicious Process Detected
  Line 18: Process matches known indicator: bridgekeeper
  Context: Process bridgekeeper started with elevated privileges...

[CRITICAL] Log Pattern Match
  Line 25: Potential FORCEDENTRY exploit indicator
  Context: CoreGraphics: WARNING: Integer overflow in GIF decoder...

================================================================================
SUMMARY:

CRITICAL: 5
HIGH: 3
MEDIUM: 2
LOW: 0

Total Findings: 10

================================================================================
RECOMMENDATIONS:

⚠ CRITICAL indicators detected!
  1. Stop using this device for sensitive communications
  2. Contact professional forensic analysts
  3. See: docs/02-detection-methodology/detection-workflow.md
  4. Report to: Amnesty Tech (security@amnesty.org) or Citizen Lab

IMPORTANT:
  - This is an educational tool, not a comprehensive scanner
  - For actual forensic analysis, use MVT
  - False positives are possible
  - Absence of findings does NOT guarantee device is clean
```

## Educational Value

This tool demonstrates:
- How IOC-based detection works
- Pattern matching in log analysis
- Severity classification
- Basic forensic methodology
- Limitations of signature-based detection

## Project Context

Part of CSE 467 Pegasus Security Toolkit.

Related documentation:
- [Detection Methodology](../../docs/02-detection-methodology/README.md)
- [IOC Analysis](../../docs/02-detection-methodology/ioc-analysis.md)
- [Detection Workflow](../../docs/02-detection-methodology/detection-workflow.md)

## License

MIT License - Educational use only

## References

[1] Amnesty International, "Mobile Verification Toolkit," https://github.com/mvt-project/mvt

[2] Amnesty Tech, "Pegasus IOCs," https://github.com/AmnestyTech/investigations

[3] Citizen Lab, "Pegasus Research," https://citizenlab.ca/
