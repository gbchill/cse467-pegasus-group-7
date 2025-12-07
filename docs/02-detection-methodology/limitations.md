# Detection Limitations

## Technical Limitations

### Unknown Exploits

- Zero-day exploits not yet discovered
- New Pegasus versions may use undocumented techniques
- IOC databases lag behind active deployment

### Memory-Only Operation

- Infections cleared on reboot
- Must analyze running device
- Minimal persistent artifacts

### Anti-Forensics

- Log deletion
- Evidence tampering
- Process hiding
- Network concealment

## Practical Limitations

### Expertise Required

- Forensic analysis is complex
- Interpretation requires training
- False positive elimination needs experience

### Resource Constraints

- Analysis is time-consuming
- Professional tools expensive
- Specialized hardware may be needed

### Timing Issues

- Device must be analyzed while infected
- Rebooting clears memory-only infections
- Delayed analysis may miss evidence

## False Negatives

### Device May Be Infected Despite Clean Scan

- Using unknown exploit chain
- IOC database incomplete
- Infection occurred after log collection
- Anti-forensics successfully hid traces

### Confidence Levels

- Clean scan = "No known indicators found"
- Does NOT mean "Device is definitely clean"
- Unknown threats cannot be detected

## False Positives

### Legitimate Activity Flagged

- Corporate VPN/MDM software
- Security tools
- Legitimate app crashes
- News sites previously compromised

### Requires Manual Verification

- Automated tools flag potential issues
- Human analysis necessary
- Context matters

## Detection Windows

### Temporary Infections

- Memory-only = cleared on reboot
- Analysis window limited
- Must capture while active

### Historical Infections

- File-based artifacts may persist
- But sophisticated malware cleans up
- Historical detection unreliable

## Platform-Specific Limitations

### iOS

- Closed system limits forensic access
- Encrypted backups may hide data
- System logs can be incomplete

### Android

- Device diversity complicates analysis
- Vendor modifications vary
- Root access may be needed

## No Silver Bullet

### Combination Required

No single method detects all infections:
- MVT scans
- Network monitoring
- Behavioral analysis
- Professional forensics

All together provide best coverage but still not guaranteed.

## Recommendations

1. **Accept Limitations** - No detection is perfect
2. **Use Multiple Methods** - Combine approaches
3. **Update Regularly** - IOCs and tools evolve
4. **Seek Expertise** - Professional help when needed
5. **Focus on Prevention** - Hardening better than detection

## Key Takeaway

Detection is an imperfect science. Prevention through security hardening and operational security provides stronger protection than relying on detection alone.

## References

[1] Amnesty International, "Forensic Methodology Report," 2021.

[2] Citizen Lab, "Detection Challenges," Various reports.
