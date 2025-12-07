# Optional Technical Tools

## Overview

This directory contains optional technical demonstration tools that complement the documentation. These tools are educational implementations showing how certain detection concepts work in practice.

## Available Tools

### IOC Scanner

**Location:** `ioc-scanner/`

**Purpose:** Demonstrates how Indicators of Compromise (IOCs) can be used to detect potential Pegasus infections through pattern matching in log files.

**Type:** Educational demonstration

**Usage:**
```bash
cd ioc-scanner
python scanner.py --log sample-logs/sample-sysdiagnose.log
```

**See:** [ioc-scanner/README.md](ioc-scanner/README.md) for detailed documentation

## Important Disclaimers

### Not Production Tools

These tools are educational demonstrations:
- Not intended for actual security use
- Simplified implementations
- Limited capabilities compared to professional tools
- May produce false positives/negatives

### For Actual Detection

Use professional forensic tools:
- **MVT (Mobile Verification Toolkit):** https://github.com/mvt-project/mvt
- **Professional forensic services:** Contact Citizen Lab or Amnesty Tech
- **Commercial forensic tools:** Cellebrite, Magnet AXIOM, etc.

## Educational Value

These tools demonstrate:
1. How IOC-based detection works conceptually
2. Pattern matching in log analysis
3. Severity classification systems
4. Basic forensic methodology
5. Limitations of signature-based detection

## Adding New Tools

Future tool ideas (not implemented):
- Attack flow visualizer (generate diagrams from JSON)
- Risk assessment quiz (interactive web tool)
- Network IOC checker (DNS monitoring simulation)

Contributions welcome from team members.

## References

[1] Amnesty International, "MVT Documentation," https://docs.mvt.re/

[2] Citizen Lab, "Digital Forensics," Various publications.
