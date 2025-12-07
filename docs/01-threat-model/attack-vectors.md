# Attack Vectors: How Pegasus Infects Devices

## Overview

Attack vectors are the methods by which Pegasus gains initial access to target devices. Understanding these vectors is critical for both threat assessment and defensive planning. Pegasus has evolved through multiple generations of attack vectors, progressing from user-interaction-dependent methods to fully zero-click exploitation techniques.

## Primary Attack Vectors

### 1. iMessage Zero-Click Exploits (Current Primary Vector)

iMessage has become the preferred attack vector for Pegasus targeting iOS devices due to its ubiquity, automatic message processing, and rich attack surface.

#### Why iMessage?

- **Universally enabled:** Every iPhone has iMessage active by default
- **Automatic processing:** Messages are processed before user sees them
- **Complex codebase:** Image rendering, PDF parsing, rich media
- **No user interaction required:** Perfect zero-click target
- **Difficult to disable:** Core iOS communication feature

#### FORCEDENTRY (CVE-2021-30860) - 2021

**Technical Details:**
- **Target:** CoreGraphics image rendering library
- **Vulnerability:** Integer overflow in GIF image decoder
- **Trigger:** Maliciously crafted GIF sent via iMessage
- **Exploitation:** Memory corruption leading to code execution
- **Scope:** iOS 14.8 and earlier, including then-current iOS 14.7.1

**Attack Flow:**
```
1. Attacker sends malicious GIF via iMessage
2. iOS automatically processes image for preview
3. Integer overflow corrupts memory
4. Attacker gains code execution in IMTranscoderAgent process
5. Sandbox escape exploit triggered
6. Kernel exploit achieves full system compromise
7. Pegasus payload deployed
```

**Impact:**
- Affected all iOS devices globally
- Required no user action whatsoever
- Even devices with Lockdown Mode (later introduced) needed protection
- Led to emergency iOS 14.8 security update

#### KISMET (2019-2020)

**Technical Details:**
- Earlier iMessage zero-click exploit chain
- Targeted iOS 13 and earlier
- Combined multiple vulnerabilities
- Less publicly documented than FORCEDENTRY

**Known Characteristics:**
- Exploited interaction between iMessage and system services
- Used crafted messages with special attachments
- Achieved kernel-level compromise
- Worked reliably on iOS 13.5.1 and earlier

### 2. WhatsApp Exploitation (CVE-2019-3568)

WhatsApp became a significant Pegasus vector in 2019, particularly for Android devices.

#### Technical Details

**Vulnerability:** Buffer overflow in WhatsApp VoIP stack
**Trigger:** Specially crafted WhatsApp call
**Affected versions:** WhatsApp for iOS and Android prior to v2.19.134 (iOS) and v2.19.244 (Android)
**Date discovered:** May 2019

**Attack Flow:**
```
1. Attacker initiates WhatsApp call to target
2. Call contains malicious SRTCP (Secure Real-Time Transport Control Protocol) packets
3. Buffer overflow triggered during call setup
4. Code execution achieved before call connects
5. Exploit runs whether call is answered or not
6. Call often deleted from call logs automatically
7. Follow-up exploits escalate to full device compromise
```

**Notable Incidents:**
- 1,400 targets identified by WhatsApp
- Included human rights lawyers, journalists, activists
- Lawsuit filed by WhatsApp against NSO Group
- Led to WhatsApp security advisory and emergency patches

**Why WhatsApp Was Targeted:**
- 2 billion users globally
- Used by high-value targets preferring "secure" messaging
- VoIP implementation had exploitable vulnerabilities
- Call setup happens automatically
- Cross-platform (iOS and Android)

### 3. Network Injection Attacks

Network injection allows infection when target connects to compromised or monitored networks.

#### Man-in-the-Middle (MITM) Deployment

**Mechanism:**
1. Attacker controls or monitors network infrastructure
2. Target connects to WiFi or cellular network
3. Attacker intercepts network traffic
4. Malicious traffic injected into legitimate communications
5. Exploits browser or app vulnerabilities
6. Device compromised

**Common Scenarios:**
- **Malicious WiFi hotspots:** Fake WiFi networks in hotels, airports, cafes
- **ISP-level injection:** Government control of telecommunications infrastructure
- **SS7 exploitation:** Vulnerabilities in cellular network signaling
- **DNS hijacking:** Redirecting traffic to attacker-controlled servers

**Example: Browser Exploitation**
```
1. Target visits website over compromised network
2. Attacker injects exploit code into HTTP response
3. Browser vulnerability exploited
4. Code execution achieved
5. Privilege escalation follows
6. Pegasus deployed
```

#### Advantages for Attackers:
- No direct interaction with target required
- Works against multiple targets simultaneously
- Difficult to attribute
- Can be "always on" for targets in specific locations

### 4. SMS-Based Vectors

While less sophisticated than zero-click, SMS remains a viable vector in some scenarios.

#### Malicious Link Campaigns (Trident Era, 2016-2017)

**Mechanism:**
1. Target receives SMS with convincing pretext
2. Message contains shortened URL
3. URL points to attacker-controlled site
4. Site exploits browser vulnerabilities
5. Device compromised if link is clicked

**Example Messages:**
- "Breaking news from your region: [link]"
- "Important security update required: [link]"
- "Package delivery notification: [link]"

**Trident Exploit Chain (CVE-2016-4657, CVE-2016-4655, CVE-2016-4656):**
- Three zero-day vulnerabilities used together
- WebKit browser engine exploitation
- Kernel information leak
- Kernel memory corruption
- Complete device compromise

**Limitations:**
- Requires user to click link (lower success rate)
- Raises suspicion if poorly crafted
- SMS filtering may block messages
- More easily detected and attributed

### 5. Physical Access Vectors

In some cases, Pegasus can be installed through brief physical access.

#### Scenarios:
- Device temporarily seized at border crossing
- Phone borrowed under false pretense
- Device left unattended
- Corrupted charging station (juice jacking)

#### Process:
1. Attacker gains physical access to unlocked device
2. Connects to computer via USB
3. Exploitation tools run automated attack
4. Pegasus installed within minutes
5. Device returned to target

**Requirements:**
- Device must be unlocked OR attacker has password
- Brief access window (5-10 minutes sufficient)
- Specialized equipment

**Detection Difficulty:**
- No network artifacts
- Minimal forensic traces
- Target may not recall physical access opportunity

## Secondary and Specialized Vectors

### Email Attachments

Less common but documented:

- Malicious PDF or image files
- Exploits document parsers
- Requires user to open attachment
- Similar to SMS link approach but via email

### Cloud Service Exploitation

Indirect access through cloud accounts:

- iCloud account compromise
- Google account takeover
- Access to cloud-backed data
- May enable device infection through cloud sync vulnerabilities

### Supply Chain Compromise

Theoretical but concerning:

- Pre-installation on device before sale
- Compromised app updates
- Malicious apps in official stores (rare, quickly detected)
- Compromised developer certificates

## Vector Selection Criteria

NSO/operators choose vectors based on:

### Target Profile
- **iOS users:** iMessage preferred
- **Android users:** WhatsApp or network injection
- **Technical sophistication:** More sophisticated users require zero-click
- **Location:** Network infrastructure access varies by country

### Operational Security
- **Stealth requirements:** Zero-click for undetectable infection
- **Scale:** Network injection for multiple targets
- **Attribution concerns:** Physical access has highest attribution risk

### Resource Availability
- **Zero-day costs:** iMessage exploits most expensive
- **Infrastructure control:** Network injection requires network access
- **Technical expertise:** More sophisticated vectors require specialized skills

## Evolution of Attack Vectors (Timeline)

### 2016-2017: User Interaction Era
- **Primary Vector:** SMS with malicious links
- **Example:** Trident exploit chain
- **User Action Required:** Click link
- **Success Rate:** Moderate (depends on social engineering)

### 2018-2019: Transition Period
- **Primary Vector:** Network injection + WhatsApp
- **User Action Required:** Minimal (answer call or connect to network)
- **Success Rate:** High
- **Detection Risk:** Medium

### 2019-2021: Zero-Click Dominance
- **Primary Vector:** iMessage (KISMET)
- **User Action Required:** None
- **Success Rate:** Very high
- **Detection Risk:** Low

### 2021-Present: Advanced Zero-Click
- **Primary Vector:** iMessage (FORCEDENTRY)
- **User Action Required:** None
- **Success Rate:** Very high
- **Detection Risk:** Very low
- **Defenses:** Lockdown Mode (iOS 16) provides some protection

## Platform-Specific Considerations

### iOS Attack Vectors

**Preferred:**
- iMessage zero-click (highest success, lowest detection)
- Network injection (when infrastructure available)

**Secondary:**
- Safari browser exploitation
- FaceTime vulnerabilities (less documented)

**Challenges for Attackers:**
- Frequent iOS security updates
- Code signing and sandboxing
- Increasingly sophisticated exploit mitigations

### Android Attack Vectors

**Preferred:**
- WhatsApp exploitation
- Network injection
- SMS with malicious links (still more effective than iOS)

**Secondary:**
- Malicious apps (rare, requires user installation)
- Browser exploitation
- Email attachments

**Advantages for Attackers:**
- More diverse attack surface (multiple vendors)
- Fragmented update ecosystem
- Varies significantly by manufacturer

## Detection Indicators by Vector

Different vectors leave different forensic traces:

| Vector | Network Traces | Log Indicators | File System Artifacts |
|--------|---------------|----------------|----------------------|
| iMessage Zero-Click | C2 domains | Crash logs (sometimes) | Minimal |
| WhatsApp | Unusual call patterns | WhatsApp database anomalies | Call log manipulation |
| Network Injection | MITM artifacts | Browser crashes | Cache anomalies |
| SMS Links | SMS records | Browser history | Downloaded files |

## Defensive Implications

Understanding attack vectors informs defense priorities:

### Vector-Specific Defenses

**iMessage:**
- Disable iMessage (drastic but effective)
- Enable iOS Lockdown Mode (partial mitigation)
- Keep iOS updated
- Monitor for unusual message activity

**WhatsApp:**
- Update to latest version
- Monitor call logs for suspicious patterns
- Consider alternative messaging platforms
- Disable automatic call answering

**Network:**
- Use VPN with trusted provider
- Avoid public WiFi
- Verify TLS certificates
- Use DNS over HTTPS/TLS

**General:**
- Keep all software updated
- Minimize app installations
- Review app permissions regularly
- Practice good operational security

## Key Takeaways

1. **Zero-Click is King:** Modern Pegasus relies primarily on zero-click vectors, making user awareness insufficient.

2. **iMessage Most Targeted:** For iOS users, iMessage represents the highest-risk attack surface.

3. **Continuous Evolution:** As vectors are exposed and patched, new ones are developed.

4. **Multiple Vectors Available:** Attackers choose from a menu of options based on target and circumstances.

5. **No Perfect Defense:** Every vector has some defensive measures, but none provide complete protection.

6. **Updates Are Critical:** Keeping devices updated patches known vectors but cannot stop zero-days.

## References

[1] Citizen Lab, "The Million Dollar Dissident: NSO Group's iPhone Zero-Days used against a UAE Human Rights Defender," August 2016.

[2] WhatsApp Security Advisory, "WhatsApp VOIP Stack Buffer Overflow," May 2019.

[3] Apple Security Updates, "About the security content of iOS 14.8 and iPadOS 14.8," September 2021.

[4] Citizen Lab, "FORCEDENTRY: NSO Group iMessage Zero-Click Exploit Captured in the Wild," September 2021.

[5] Google Project Zero, "A very deep dive into iOS Exploit chains found in the wild," December 2021.

[6] Amnesty International, "Forensic Methodology Report: How to catch NSO Group's Pegasus," July 2021.
