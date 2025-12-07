# Detection Workflow: Step-by-Step Process

## Overview

This workflow provides a systematic approach to detecting Pegasus infections using the Mobile Verification Toolkit (MVT) and forensic analysis techniques.

## 10-Step Detection Process

### Step 1: Initial Suspicion Assessment

**Objective:** Determine if forensic analysis is warranted

**Actions:**
- Evaluate risk profile (journalist, activist, political figure?)
- Document suspicious behaviors (battery drain, data usage, device heating)
- Identify recent events (travel to high-risk country, colleagues infected)
- Assess urgency (active targeting vs. historical check)

**Decision Point:** Proceed if medium-to-high risk or clear indicators present

### Step 2: Device Preparation

**Objective:** Prepare device for analysis without destroying evidence

**Critical Rules:**
- **DO NOT REBOOT** - Clears memory-only infections
- DO NOT install new apps
- DO NOT perform factory reset
- DO minimize device use during preparation

**Actions:**
- Enable airplane mode (prevents remote wipe)
- Charge device to 100%
- Note current device state (iOS version, apps installed, settings)
- Photograph device condition

### Step 3: Log Collection

**For iOS:**
```
1. Connect device to computer
2. Open Settings > Privacy > Analytics & Improvements > Analytics Data
3. Generate sysdiagnose:
   - Press Volume Up + Volume Down + Power button simultaneously
   - Hold until device vibrates
   - Wait 10 minutes for generation
4. Connect to Mac and sync to retrieve sysdiagnose
5. Create encrypted backup using Finder/iTunes
```

**For Android:**
```
1. Enable USB debugging (Settings > Developer Options)
2. Connect to computer via USB
3. Extract logs using adb:
   adb pull /sdcard/
   adb logcat -d > logcat.txt
   adb bugreport
4. Create full backup:
   adb backup -all -f backup.ab
```

### Step 4: MVT Installation and Setup

**Install MVT:**
```bash
# Install via pip
pip3 install mvt

# Verify installation
mvt-ios --help
mvt-android --help
```

**Download Latest IOC Database:**
```bash
# Clone Amnesty Tech IOC repository
git clone https://github.com/AmnestyTech/investigations.git

# Note the path to indicators/pegasus.stix2
```

### Step 5: IOC Database Update

**Update to Latest Indicators:**
```bash
cd investigations
git pull origin main
```

**IOC Location:**
```
investigations/
└── indicators/
    └── pegasus.stix2
```

### Step 6: Scan Execution

**iOS Analysis:**
```bash
# Analyze backup
mvt-ios check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output /path/to/output/ \
  /path/to/ios/backup/

# Analyze filesystem dump (if available)
mvt-ios check-fs \
  --iocs investigations/indicators/pegasus.stix2 \
  --output /path/to/output/ \
  /path/to/filesystem/
```

**Android Analysis:**
```bash
# Analyze backup
mvt-android check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output /path/to/output/ \
  /path/to/android/backup/

# Analyze ADB dump
mvt-android check-adb \
  --iocs investigations/indicators/pegasus.stix2 \
  --output /path/to/output/
```

**Analysis Time:** 15-60 minutes depending on device data volume

### Step 7: Results Analysis

**MVT Output Files:**
```
output/
├── command.txt          # Command executed
├── timeline.csv         # Chronological events
├── timeline_detected.csv # Suspicious events only
├── *.json               # Raw data for each check
└── logs/                # Detailed logs
```

**Key Files to Review:**
- `timeline_detected.csv` - Start here for flagged items
- `sms.json` - Suspicious SMS messages
- `chrome_history.json` - Suspicious domains
- `calls.json` - Unusual call patterns

**Interpretation:**
- **RED FLAGS**: Multiple detections from different data sources
- **WARNING**: Single detection or unusual patterns
- **INFO**: Items matching IOCs but may be false positives

### Step 8: False Positive Elimination

**Common False Positives:**
- Apple/Google legitimate services appearing in network logs
- Corporate VPN or MDM solutions
- News websites that were previously compromised (but visited legitimately)
- Crash logs from legitimate app bugs

**Validation Steps:**
1. Cross-reference detections across multiple data sources
2. Check timing (coordinated activity more suspicious)
3. Research flagged domains (legitimate service vs. known C2)
4. Consider context (journalist visiting news sites vs. random domain)

**High-Confidence Indicators:**
- Multiple NSO-linked domains across different timeframes
- Pegasus-specific process names in logs
- Crash logs matching known exploit patterns
- Coordinated suspicious activity

### Step 9: Reporting and Response

**If Infection Detected:**

**Immediate Actions:**
1. **Stop using device** for sensitive communications
2. **Document findings** thoroughly
3. **Preserve evidence** (all logs and MVT output)
4. **Notify relevant parties** (organization, colleagues)

**Reporting:**
- Contact Amnesty Tech: security@amnesty.org
- Contact Citizen Lab: info@citizenlab.ca
- File report with Access Now Digital Security Helpline
- Contact local digital rights organizations

**Legal Considerations:**
- Evidence preservation for potential legal action
- Attorney-client privilege if applicable
- Privacy laws regarding data sharing

**If Clean:**
- Results do not guarantee device is uninfected
- Unknown exploits may not be in IOC database
- Consider implementing security hardening measures

### Step 10: Evidence Preservation

**Critical Evidence:**
- Original device logs (sysdiagnose, adb logs)
- MVT output directory
- Screenshots of MVT results
- Timeline of suspicious events
- Notes on device behaviors

**Storage:**
- Encrypted external drive
- Multiple backups
- Secure cloud storage (encrypted)
- Chain of custody documentation

**Sharing:**
- With trusted security researchers only
- Remove personal identifying information if required
- Use secure file transfer methods
- Document who received what information

## Advanced Analysis (Optional)

### Memory Forensics

For active infections:
```bash
# iOS: Requires jailbreak
# Checkra1n or similar to gain access
# Dump memory using forensic tools

# Android: Requires root
adb shell su -c "cat /proc/kcore > /sdcard/memory.dump"
```

**Warning:** Advanced techniques risk destroying evidence

### Network Traffic Analysis

**Real-Time Capture:**
```bash
# On device with packet capture capability
tcpdump -i any -w capture.pcap

# Or use VPN with logging to capture device traffic
```

**Analysis:**
- Look for connections to known NSO C2 domains
- Identify suspicious TLS certificates
- Check for domain fronting patterns
- Analyze traffic timing and volume

## Workflow Checklist

- [ ] Risk assessment completed
- [ ] Device prepared (not rebooted)
- [ ] Logs collected (sysdiagnose/adb)
- [ ] Backup created
- [ ] MVT installed
- [ ] IOC database updated
- [ ] MVT scan executed
- [ ] Results reviewed
- [ ] False positives eliminated
- [ ] Findings documented
- [ ] Incident reported (if infection found)
- [ ] Evidence preserved
- [ ] Response actions initiated

## Timeline Expectations

| Step | Time Required |
|------|--------------|
| Risk Assessment | 15-30 minutes |
| Device Preparation | 10-15 minutes |
| Log Collection | 20-60 minutes |
| MVT Installation | 5-10 minutes |
| Scan Execution | 15-60 minutes |
| Results Analysis | 30-120 minutes |
| Reporting | 60-180 minutes |
| **Total** | **2.5-8 hours** |

## Key Takeaways

1. **Don't Reboot:** Memory-only infections disappear on reboot
2. **MVT is Primary Tool:** Best free tool available for Pegasus detection
3. **False Positives Common:** Careful analysis required
4. **Professional Help Available:** Contact Citizen Lab or Amnesty Tech
5. **Document Everything:** Thorough documentation critical for any follow-up

## References

[1] Amnesty International Security Lab, "MVT Documentation," https://docs.mvt.re/

[2] Citizen Lab, "Pegasus Detection Guide," Various technical reports.

[3] Access Now, "Digital Security Helpline," https://www.accessnow.org/help/
