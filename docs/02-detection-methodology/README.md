# Detection Methodology

## Overview

Detecting Pegasus and similar sophisticated spyware is extremely challenging. Unlike traditional malware that can be identified through signature-based antivirus scanning, Pegasus is designed to evade detection through anti-forensics capabilities, memory-only operation, and kernel-level hiding techniques. This section provides comprehensive guidance on detection approaches, methodologies, and tools.

## Why Detection is Challenging

### Technical Obstacles

1. **Zero-Click Infection**
   - No suspicious links or files for user to report
   - Target may be completely unaware of infection

2. **Kernel-Level Access**
   - Can hide from user-space detection tools
   - Bypasses traditional antivirus

3. **Memory-Only Operation**
   - Minimal persistent files
   - Cleared on reboot

4. **Anti-Forensics**
   - Log deletion and modification
   - Process hiding
   - Network connection concealment

5. **Targeted Deployment**
   - Limited infection prevalence
   - Signature databases incomplete

### Practical Challenges

1. **Expertise Required**
   - Forensic analysis needs specialized skills
   - Interpretation of results complex

2. **Timing Critical**
   - Must analyze while device is running
   - Reboot clears memory-only infections

3. **Resource Intensive**
   - Analysis takes significant time
   - Specialized tools and hardware needed

4. **False Positives**
   - Legitimate system activity can appear suspicious
   - IOC databases contain both true and false indicators

## Detection Approaches

### 1. Forensic Analysis (Primary Method)

Systematic examination of device artifacts for infection indicators.

**See:** [forensic-logs.md](forensic-logs.md) for log collection procedures

**Advantages:**
- Can identify historical infections
- Works on powered-off devices (for file-based analysis)
- Comprehensive evidence collection

**Limitations:**
- Requires specialized expertise
- Time-consuming
- May miss memory-only infections
- Ineffective after reboot (for memory-resident malware)

### 2. Mobile Verification Toolkit (MVT)

Open-source tool developed by Amnesty International for Pegasus detection.

**See:** [mvt-toolkit.md](mvt-toolkit.md) for detailed usage guide

**What MVT Does:**
- Scans iOS/Android backups and logs
- Compares findings to IOC database
- Identifies suspicious artifacts
- Generates analysis reports

**Advantages:**
- Free and open-source
- Regularly updated IOC database
- Relatively easy to use
- Documented methodology

**Limitations:**
- Cannot detect all Pegasus versions
- Requires device backup or system logs
- May produce false positives
- Cannot detect zero-day exploits not yet in IOC database

### 3. Network Monitoring

Analyzing network traffic for C2 communications.

**See:** [network-indicators.md](network-indicators.md)

**Methods:**
- DNS query monitoring
- TLS/SSL connection analysis
- Traffic pattern analysis
- Known C2 domain detection

**Advantages:**
- Can detect active infections
- Works without device access
- Real-time monitoring possible

**Limitations:**
- Encryption hides C2 content
- Domain fronting disguises traffic
- Requires network access
- C2 domains constantly change

### 4. Behavioral Analysis

Monitoring for unusual device behavior.

**Indicators:**
- Unusual battery drain
- Unexpected data usage
- Device heating when idle
- Performance degradation
- Strange background processes

**Advantages:**
- User can perform basic checks
- No specialized tools required
- May provide early warning

**Limitations:**
- Many false positives
- Sophisticated malware mimics normal behavior
- Difficult to distinguish from legitimate issues
- Not definitive

## Detection Workflow

### Step-by-Step Process

**See:** [detection-workflow.md](detection-workflow.md) for detailed procedures

1. **Initial Suspicion Assessment**
   - Determine if forensic analysis is warranted
   - Evaluate risk factors
   - Gather preliminary information

2. **Device Preparation**
   - Document device state
   - Prevent modifications
   - Plan analysis approach

3. **Log Collection**
   - Extract iOS sysdiagnose or Android logs
   - Create full device backup
   - Preserve evidence integrity

4. **MVT Analysis**
   - Install and configure MVT
   - Update IOC database
   - Run scans on collected data

5. **Results Interpretation**
   - Analyze MVT findings
   - Eliminate false positives
   - Assess confidence level

6. **Advanced Analysis** (if needed)
   - Memory forensics
   - Network traffic analysis
   - Manual artifact examination

7. **Reporting**
   - Document findings
   - Assess confidence level
   - Provide recommendations

8. **Response Actions**
   - Device replacement (if infected)
   - Incident reporting
   - Security hardening

## Indicators of Compromise (IOCs)

**See:** [ioc-analysis.md](ioc-analysis.md) for comprehensive IOC documentation

### Types of IOCs

1. **Network Indicators**
   - C2 domains and IP addresses
   - SSL/TLS certificate fingerprints
   - DNS query patterns

2. **File System Indicators**
   - Suspicious file paths
   - Modified system files
   - Unusual directory structures

3. **Process Indicators**
   - Suspicious process names
   - Unexpected system daemons
   - Process injection artifacts

4. **Log Indicators**
   - Crash logs from exploitation
   - System log anomalies
   - Deletion of security logs

## Detection Tools and Resources

### Mobile Verification Toolkit (MVT)

**Installation:**
```bash
pip3 install mvt
```

**Basic Usage:**
```bash
# iOS
mvt-ios check-backup --output /path/to/output /path/to/backup

# Android
mvt-android check-backup --output /path/to/output /path/to/backup
```

**Resources:**
- Official repository: https://github.com/mvt-project/mvt
- Documentation: https://docs.mvt.re/
- IOC repository: https://github.com/AmnestyTech/investigations

### Other Tools

**iOS:**
- libimobiledevice (device backup)
- iMazing (commercial backup tool)
- Cellebrite (professional forensics - expensive)

**Android:**
- Android Debug Bridge (adb)
- Android Backup Extractor
- JADX (APK analysis)

**Network Analysis:**
- Wireshark (packet capture)
- Pi-hole (DNS monitoring)
- Little Snitch (macOS firewall)

## When to Suspect Infection

### High-Risk Indicators

Immediate forensic analysis recommended if:

1. **You are a high-value target:**
   - Journalist covering sensitive topics
   - Human rights activist
   - Political opposition member
   - Lawyer in sensitive cases
   - Government official

2. **You observe suspicious activity:**
   - Unexplained battery drain
   - Significant data usage increases
   - Device heating when idle
   - Unexpected reboots

3. **You have circumstantial evidence:**
   - Colleagues or associates found infected
   - Working in country with known Pegasus deployment
   - Experiencing coordinated harassment
   - Information leaks suggest surveillance

### Medium-Risk Indicators

Consider analysis if:
- Multiple behavioral anomalies
- Recent travel to high-risk countries
- Work involves sensitive information
- Unexplained knowledge of private activities by adversaries

## Limitations of Detection

### What Detection Cannot Do

1. **Cannot Guarantee Device is Clean**
   - Unknown exploits not in IOC database
   - New Pegasus versions may be undetectable
   - Memory-only infections invisible after reboot

2. **Cannot Detect Future Infections**
   - Clean now ≠ clean forever
   - Re-infection possible
   - Zero-day exploits unknown

3. **Cannot Identify Attacker with Certainty**
   - Attribution is intelligence/legal work
   - Multiple governments use Pegasus
   - C2 infrastructure provides limited attribution

### False Negatives

Infection may be present but undetected if:
- Using unknown exploit chain
- Device rebooted before analysis
- Logs deleted by anti-forensics
- IOC database incomplete
- Infection occurred long ago (artifacts deleted)

### False Positives

Non-malicious activity may appear suspicious:
- Legitimate crash logs
- Normal system processes
- Corporate MDM software
- Security tools themselves
- iOS/Android debugging features

## Best Practices for Detection

### For Individuals

1. **Regular Monitoring**
   - Periodic MVT scans
   - Monitor data usage
   - Watch for behavioral anomalies

2. **Prompt Analysis**
   - Don't delay if infection suspected
   - Analyze before rebooting
   - Preserve evidence

3. **Professional Assistance**
   - Consult security experts
   - Consider commercial forensics
   - Contact organizations like Citizen Lab or Amnesty Tech

### For Organizations

1. **Baseline Establishment**
   - Document normal device behavior
   - Regular forensic snapshots
   - Network traffic baseline

2. **Monitoring Infrastructure**
   - DNS monitoring
   - Network traffic analysis
   - Endpoint detection and response (EDR)

3. **Incident Response Plan**
   - Defined procedures for suspected infections
   - Chain of custody protocols
   - Legal and PR considerations

## Next Steps

After understanding detection methodology:

1. **Learn Log Collection:** Read [forensic-logs.md](forensic-logs.md)
2. **Practice with MVT:** Follow [mvt-toolkit.md](mvt-toolkit.md)
3. **Study IOCs:** Review [ioc-analysis.md](ioc-analysis.md)
4. **Understand Workflow:** Follow [detection-workflow.md](detection-workflow.md)
5. **Implement Prevention:** See [../03-security-hardening/README.md](../03-security-hardening/README.md)

## Key Takeaways

1. **Detection is Difficult:** Pegasus is designed to evade detection; no method is foolproof.

2. **MVT is Best Starting Point:** Free, documented, and regularly updated detection tool.

3. **Early Analysis Critical:** Memory-only infections disappear on reboot.

4. **Expertise Helps:** Professional forensic analysis increases detection accuracy.

5. **Prevention Better Than Detection:** Security hardening reduces infection risk.

6. **No Guarantees:** Clean result doesn't guarantee device is uncompromised.

## References

[1] Amnesty International, "Forensic Methodology Report: How to catch NSO Group's Pegasus," July 2021.

[2] Amnesty International Security Lab, "Mobile Verification Toolkit Documentation," 2023.

[3] Citizen Lab, "Pegasus Detection Methods," Various reports 2016-2023.

[4] Marczak, B., et al., "Analyzing Pegasus Spyware Forensics," Citizen Lab, 2021.

[5] Lookout Security, "Pegasus Detection Best Practices," 2019.
