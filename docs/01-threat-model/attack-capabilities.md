# Attack Capabilities: What Pegasus Can Do

## Overview

Pegasus represents the state-of-the-art in mobile surveillance technology. Unlike traditional malware that relies on user interaction or has limited system access, Pegasus achieves complete device compromise with kernel-level privileges, enabling total surveillance of the target device. This document analyzes the technical capabilities that make Pegasus one of the most sophisticated mobile threats ever documented.

## Core Capabilities Summary

Once successfully deployed, Pegasus provides attackers with:

- **Complete data access:** All files, messages, photos, and stored information
- **Real-time communications monitoring:** Calls, messages, and encrypted app communications
- **Location tracking:** Continuous GPS monitoring and location history
- **Environmental surveillance:** Camera and microphone activation
- **Credential harvesting:** Passwords, authentication tokens, and encryption keys
- **Persistent access:** Survives reboots and maintains long-term presence
- **Covert operation:** Evades detection through anti-forensics techniques

## Zero-Click Remote Code Execution

### Definition and Significance

Zero-click exploitation means the target device can be compromised without any user interaction. The target does not need to click a link, open a file, or even unlock their device. This represents the most sophisticated class of mobile exploits.

**Traditional Malware:** Requires user to click malicious link, download file, or install application

**Pegasus Zero-Click:** Automatically exploits vulnerability when message is received, even if never opened

### Technical Implementation

Pegasus zero-click exploits target vulnerabilities in code that automatically processes data:

#### iMessage Exploits
The most documented Pegasus zero-click vector:

1. **Automatic Message Processing**
   - iMessage automatically processes incoming messages
   - Image rendering, PDF parsing, and file preview happen in background
   - No user interaction required for code to parse attacker-controlled data

2. **FORCEDENTRY Exploit (CVE-2021-30860)**
   - Exploits image rendering library (CoreGraphics)
   - Sends malicious GIF file via iMessage
   - Triggers integer overflow in image decoder
   - Achieves code execution when iOS processes image
   - Works even if message is never opened by user

3. **KISMET Exploit Chain (2019)**
   - Earlier zero-click iMessage exploit
   - Targeted iOS 13.5 and earlier
   - Exploited interaction between iMessage and other system services
   - Full chain from message receipt to kernel compromise

#### SMS/MMS Message Parsing
- Targets vulnerabilities in SMS/MMS processing
- Media parsing (images, videos) in messages
- Contact card (.vcf file) parsing
- Link preview generation

#### WhatsApp Exploits (CVE-2019-3568)
- Exploited WhatsApp call handling
- Missed call could trigger infection
- Calls often automatically deleted from logs
- Used against Amnesty International researcher

### Impact of Zero-Click Capability

The zero-click capability fundamentally changes the threat landscape:

**For Attackers:**
- No social engineering required
- Higher success rate
- Target may never know infection occurred
- Enables mass targeting if desired

**For Defenders:**
- User awareness training ineffective
- Traditional phishing indicators irrelevant
- Detection extremely challenging
- Prevention requires OS-level mitigations

## Kernel-Level Access

### Understanding Privilege Levels

Modern mobile operating systems use privilege levels to isolate processes:

| Level | iOS Name | Android Name | Typical Access |
|-------|----------|--------------|----------------|
| User | Sandboxed App | Unprivileged App | Limited to app data only |
| Elevated | System Service | System App | Some OS functionality |
| Root | Root Process | Root Process | All OS functionality |
| **Kernel** | **Kernel** | **Kernel** | **Complete hardware control** |

Pegasus achieves **kernel-level access**, the highest privilege level.

### Kernel Capabilities

With kernel-level access, Pegasus can:

#### 1. Bypass All Security Controls
- Disable code signing verification
- Circumvent sandboxing
- Override permission restrictions
- Disable security logging
- Modify system files

#### 2. Access All Data
- Read any file on the device
- Access encrypted storage
- Extract keychain/keystore credentials
- Access secure enclave data (attempted)
- Read memory of any process

#### 3. Persistent Modification
- Install kernel rootkit components
- Modify system frameworks
- Hook kernel functions
- Intercept system calls
- Persist across reboots (with re-exploitation)

#### 4. Covert Operation
- Hide processes from user-space tools
- Conceal network connections
- Remove forensic evidence
- Disable security alerts
- Operate invisibly to user

### Achieving Kernel Access

Pegasus uses exploit chains to escalate from initial code execution to kernel privileges:

```
1. Initial Exploit (e.g., FORCEDENTRY)
   ↓
2. User-space Code Execution (inside message parsing process)
   ↓
3. Sandbox Escape (break out of restricted process)
   ↓
4. Memory Corruption (exploit kernel vulnerability)
   ↓
5. Kernel Code Execution
   ↓
6. Kernel Privilege Acquisition
```

Each step requires exploitation of additional vulnerabilities, creating an "exploit chain."

## Complete Device Compromise

### Communications Access

Pegasus monitors all communication channels:

#### Traditional Communications
- **Phone calls:** Real-time call interception
- **SMS/MMS:** Complete message history and real-time monitoring
- **Voicemail:** Access to all voicemails
- **Call logs:** Complete history of calls made and received

#### Encrypted Messaging Applications
Pegasus bypasses end-to-end encryption by accessing data on the device before encryption or after decryption:

- **WhatsApp:** Messages, calls, media, contacts
- **Signal:** Messages, calls, media (if device compromised)
- **Telegram:** Messages, media, contacts
- **iMessage:** Complete message history
- **Facebook Messenger:** All communications
- **Other apps:** Any messaging app data accessible

**Key Point:** End-to-end encryption protects data in transit but cannot protect against endpoint compromise. Pegasus operates at the endpoint, accessing data before encryption or after decryption.

#### Email
- All email accounts configured on device
- Email content, attachments, and metadata
- Real-time monitoring of new emails
- Access to webmail through saved credentials

### Location Tracking

Comprehensive location surveillance:

- **Real-time GPS tracking:** Continuous location monitoring
- **Location history:** Historical movement patterns
- **Wi-Fi network information:** Networks device has connected to
- **Cell tower data:** Cell-based location information
- **Geolocation metadata:** Locations embedded in photos and files

### Environmental Surveillance

Pegasus can activate device sensors covertly:

#### Camera Access
- Front and rear camera activation
- Photo capture without user notification
- Video recording
- Access to existing photo library
- Metadata extraction (time, location, device info)

#### Microphone Access
- Real-time audio recording
- Room audio surveillance (even when phone not in use)
- Call recording
- Environmental noise monitoring

#### Other Sensors
- Accelerometer and gyroscope data
- Proximity sensor
- Ambient light sensor
- Magnetometer (compass)

### Data Extraction

Complete access to device data:

- **Files:** All documents, downloads, media
- **App data:** Data from all installed applications
- **Passwords:** Keychain (iOS) or Keystore (Android) credentials
- **Browsing history:** Complete web browsing activity
- **Calendars:** Schedule and meeting information
- **Contacts:** Complete contact database
- **Notes:** All notes and memos
- **Social media:** Cached data from social apps

## Anti-Forensics and Evasion

### Detection Evasion

Pegasus employs multiple techniques to avoid detection:

#### System-Level Hiding
- Process name impersonation (appears as legitimate system process)
- Rootkit techniques to hide from process lists
- Network connection concealment
- File hiding capabilities

#### Behavioral Evasion
- Minimal disk writes (operates mostly in memory)
- Throttled network traffic to avoid anomaly detection
- Timing attacks to avoid triggering behavior-based detection
- Legitimate API usage patterns

#### Anti-Debugging
- Debugger detection and prevention
- Virtualization and emulation detection
- Prevents analysis in security research environments
- Code obfuscation and encryption

### Forensic Counter-Measures

Pegasus actively impedes forensic analysis:

#### Log Manipulation
- Deletion or modification of system logs
- Selective log entry removal
- Timestamp manipulation
- Creation of false log entries

#### Evidence Removal
- Self-deletion capabilities
- Temporary file cleanup
- Network artifact removal
- Cache clearing

#### Limited Forensic Traces
- Primarily memory-resident operation
- Minimal persistent files
- Encrypted network communications
- Steganography in some data transmissions

## Command and Control Infrastructure

### Communication Channels

Pegasus maintains contact with operator infrastructure:

- **Domain fronting:** Disguises C2 traffic as legitimate HTTPS
- **Multiple redundant servers:** Fallback communication channels
- **Encrypted communications:** All data exfiltration is encrypted
- **Legitimate cloud services:** May use major cloud providers for C2

### Update Mechanisms

Pegasus can be remotely updated:

- New exploit modules
- Updated evasion techniques
- Modified data collection priorities
- Enhanced anti-forensics capabilities

### Data Exfiltration

Stolen data is transmitted to NSO infrastructure:

- **Batch uploads:** Collected data uploaded periodically
- **Real-time streaming:** Active communications monitored in real-time
- **Selective exfiltration:** Operators choose what data to extract
- **Bandwidth throttling:** Avoids suspicion from unusual data usage

## Comparison to Traditional Mobile Malware

| Capability | Traditional Malware | Pegasus |
|-----------|-------------------|---------|
| **Infection Method** | Requires user interaction | Zero-click |
| **Privilege Level** | Sandboxed app | Kernel-level |
| **Detection** | Often caught by antivirus | Evades detection |
| **Persistence** | Limited | Sophisticated |
| **Data Access** | App-specific only | Complete device |
| **Target Selection** | Broad/opportunistic | Highly targeted |
| **Development Cost** | Thousands to millions | Tens of millions |
| **Operator Skill** | Varies widely | Government intelligence |

## Platform-Specific Capabilities

### iOS-Specific

Pegasus exploits iOS-specific features and vulnerabilities:

- **iMessage ecosystem:** Primary infection vector
- **Keychain access:** iOS password storage compromise
- **FaceTime:** Potential surveillance vector
- **App Store restrictions:** Less relevant with kernel access
- **iCloud sync exploitation:** Access to cloud-backed data

### Android-Specific

Different capabilities on Android:

- **System diversity:** More exploitation targets but more variation
- **Permission model:** Bypassed with kernel access
- **Google Play Services:** Potential attack surface
- **Vendor customizations:** Additional vulnerabilities in OEM software
- **Bootloader status:** Locked bootloaders provide some protection

## Limitations and Constraints

Despite sophisticated capabilities, Pegasus has some limitations:

### Technical Limitations

1. **Requires Current Exploits**
   - Patched vulnerabilities stop working
   - Constant need for new zero-days
   - OS updates can break existing implants

2. **Some Data Remains Inaccessible**
   - Secure Enclave protected data (partial protection)
   - Strong hardware-backed encryption
   - Specialized secure devices (e.g., some government phones)

3. **Detection Is Possible**
   - Forensic analysis can identify some infections
   - Anomaly detection may spot unusual behavior
   - Network monitoring can identify C2 traffic

### Operational Limitations

1. **Cost**
   - Zero-day exploits are expensive
   - Per-target licensing fees
   - Infrastructure maintenance costs

2. **Exposure Risk**
   - Each deployment risks exploit disclosure
   - Captured samples enable analysis
   - Public disclosure damages effectiveness

3. **Collateral Damage**
   - Device instability from aggressive exploitation
   - Battery drain from continuous surveillance
   - Network usage patterns may be noticed

## Evolution Over Time

Pegasus capabilities have evolved significantly:

| Era | Primary Vector | Privilege Level | Detection Difficulty |
|-----|---------------|-----------------|---------------------|
| **2016-2017** | SMS links (Trident) | Root/Kernel | Medium |
| **2018-2019** | WhatsApp calls | Kernel | High |
| **2019-2021** | iMessage (KISMET) | Kernel | Very High |
| **2021-2023** | iMessage (FORCEDENTRY) | Kernel | Extremely High |

Each generation became more sophisticated, more difficult to detect, and required less (or zero) user interaction.

## Key Takeaways

1. **Unprecedented Capabilities**: Pegasus represents the most sophisticated mobile malware publicly documented, combining zero-click infection with kernel-level access.

2. **Complete Compromise**: Once infected, the device should be considered completely compromised with no reasonable expectation of privacy.

3. **Evasion by Design**: Anti-forensics and evasion capabilities are core features, making detection extremely challenging.

4. **Bypasses Encryption**: End-to-end encryption is irrelevant when the endpoint itself is compromised.

5. **Continuous Evolution**: Pegasus capabilities evolve as new vulnerabilities are discovered and old exploits are patched.

6. **Defense is Difficult**: Traditional security controls are largely ineffective against such sophisticated threats.

## References

[1] Citizen Lab, "The Million Dollar Dissident: NSO Group's iPhone Zero-Days used against a UAE Human Rights Defender," August 2016.

[2] Google Project Zero, "A very deep dive into iOS Exploit chains found in the wild," December 2021.

[3] Amnesty International, "Forensic Methodology Report: How to catch NSO Group's Pegasus," July 2021.

[4] Marczak, B., et al., "Hide and Seek: Tracking NSO Group's Pegasus Spyware to Operations in 45 Countries," Citizen Lab, September 2018.

[5] WhatsApp, "WhatsApp Security Advisory," May 2019.

[6] Apple, "About the security content of iOS 14.8 and iPadOS 14.8," September 2021.

[7] Ars Technica, "How iMessage's 'BlastDoor' feature is securing your iPhone," March 2021.
