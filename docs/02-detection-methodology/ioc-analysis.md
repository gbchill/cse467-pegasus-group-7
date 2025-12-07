# Indicators of Compromise (IOC) Analysis

## What are IOCs?

Indicators of Compromise are artifacts that suggest a system has been compromised. For Pegasus, IOCs include network indicators, file system artifacts, process names, and behavioral patterns.

## Types of Pegasus IOCs

### Network Indicators

**Domains:**
- `.pegasusinfections.com` (early versions)
- Various NSO-controlled domains
- See Amnesty Tech repository for full list

**Example Domains:**
```
infections.pegasusinfections.com
laxbrodstmedia.com
usedirectory.com
cloud-diagnose.com
```

**IP Addresses:**
- NSO C2 infrastructure IPs
- Regularly updated in IOC databases

### Process Indicators

**Suspicious Processes:**
- `bridgekeeper` (Android)
- Unusual system daemon names
- Modified legitimate process names

### File System Indicators

**iOS:**
- Modified system files
- Unusual cache entries
- Suspicious .plist files

**Android:**
- `/system/app/` modifications
- Unusual APK installations
- Modified SELinux policies

### Log Indicators

**Crash Logs:**
- CoreGraphics crashes (FORCEDENTRY)
- iMessage crashes
- WhatsApp crash patterns

**System Logs:**
- Unusual kernel panics
- Memory warnings during exploitation
- Deleted security logs

## Using IOC Databases

### Amnesty Tech Repository

Primary source for Pegasus IOCs:

```bash
git clone https://github.com/AmnestyTech/investigations.git
cd investigations/indicators/
```

**Main IOC File:** `pegasus.stix2`

### IOC Updates

```bash
# Update to latest indicators
cd investigations
git pull origin main
```

**Update Frequency:** Check weekly for new indicators

## IOC Matching Process

### Automated Matching (MVT)

MVT automatically compares device artifacts against IOC database:

1. Extracts device data
2. Compares against IOC patterns
3. Flags matches
4. Generates report

### Manual Matching

For advanced analysis:

1. Extract network logs
2. Search for known C2 domains
3. Check process lists against known names
4. Examine crash logs for exploit patterns

## False Positives

### Common Causes

- Legitimate services using similar domains
- Corporate VPN/MDM software
- Legitimate app crashes
- News websites previously compromised

### Verification

1. Cross-reference multiple IOC types
2. Check timing correlations
3. Research flagged items
4. Assess context

## IOC Limitations

### Cannot Detect

- Zero-day exploits not yet discovered
- New Pegasus versions
- IOCs not yet documented
- Heavily customized implementations

### Aging IOCs

- Older IOCs may be from decommissioned infrastructure
- NSO regularly changes domains and IPs
- Some IOCs may represent past not current threats

## Building Custom IOCs

For organizations:

1. Baseline normal network activity
2. Document suspicious events
3. Correlate with known Pegasus activity
4. Share with security community (if appropriate)

## Key Takeaways

1. IOCs are clues, not definitive proof
2. Multiple IOC matches increase confidence
3. IOC databases require regular updates
4. False positives are common
5. Absence of IOC matches doesn't guarantee clean device

## References

[1] Amnesty Tech, "Pegasus IOC Repository," https://github.com/AmnestyTech/investigations

[2] Citizen Lab, "Indicator Tracking," Various technical reports 2016-2023.
