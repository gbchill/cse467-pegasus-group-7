# Security Hardening

## Overview

While no defense provides complete protection against sophisticated threats like Pegasus, implementing multiple security layers significantly reduces attack surface and increases exploitation costs for attackers.

## Defense-in-Depth Strategy

Security hardening requires multiple overlapping controls:

1. **Device-Level Controls** - OS features and settings
2. **Network-Level Controls** - VPN, DNS protection, traffic monitoring
3. **Operational Security** - Behavior and practices
4. **Physical Security** - Device protection

## Platform-Specific Hardening

### iOS Defense

See: [ios-defense.md](ios-defense.md)

**Key Measures:**
- Enable Lockdown Mode (iOS 16+)
- Configure iMessage security settings
- Manage app permissions
- Regular updates

### Android Defense

See: [android-defense.md](android-defense.md)

**Key Measures:**
- Google Play Protect
- Permission management
- SafetyNet verification
- Consider GrapheneOS for high-risk users

## Network Hardening

See: [network-defense.md](network-defense.md)

**Key Measures:**
- Trusted VPN usage
- DNS over HTTPS/TLS
- Avoid public WiFi
- Network traffic monitoring

## Operational Security

See: [opsec-practices.md](opsec-practices.md)

**Key Practices:**
- Device compartmentalization
- Communication channel selection
- Regular device rotation
- Travel security protocols

## High-Risk User Guidance

See: [high-risk-users.md](high-risk-users.md)

Special considerations for:
- Journalists
- Activists
- Political opposition
- Human rights lawyers

## Key Principles

1. **Updates are Critical** - Patch zero-days quickly
2. **Reduce Attack Surface** - Disable unnecessary features
3. **Assume Breach** - Plan for compromise
4. **Defense in Depth** - Multiple overlapping controls
5. **Operational Security** - Technology alone insufficient

## Effectiveness Against Pegasus

| Control | Effectiveness | Notes |
|---------|--------------|-------|
| Lockdown Mode | High | Significant attack surface reduction |
| Regular Updates | Medium-High | Patches known exploits |
| VPN | Medium | Protects against network injection |
| Disable iMessage | High | Removes primary attack vector |
| Operational Security | High | Reduces targeting effectiveness |

## References

[1] Apple, "iOS Security Guide," 2023.

[2] Citizen Lab, "Security Recommendations for High-Risk Users," 2022.

[3] EFF, "Surveillance Self-Defense," https://ssd.eff.org/
