# Data Extraction Targets

## Overview

Once Pegasus achieves kernel-level access to a device, it can extract virtually any data stored on or passing through the device. This document catalogs the types of information Pegasus collects, methods of collection, and the privacy implications of such comprehensive surveillance.

## Complete Communications Access

### Traditional Communications

**Phone Calls:**
- Real-time call interception
- Call recording (both sides of conversation)
- Call metadata (duration, participants, timing)
- Call history (all past calls)
- Voicemail messages

**SMS and MMS:**
- All text messages (sent and received)
- MMS media content (photos, videos, audio)
- Message metadata (timestamps, sender/recipient)
- Deleted messages (if still in database)
- Draft messages

### Encrypted Messaging Applications

Pegasus bypasses end-to-end encryption by accessing data at the endpoint:

**WhatsApp:**
- All messages (text, voice, media)
- WhatsApp calls (audio and video)
- Contact list
- Group memberships and messages
- Status updates
- Media library

**Signal:**
- Messages and calls
- Contact list
- Disappearing message settings
- Media shared through Signal

**Telegram:**
- Messages and media
- Secret chats (if device compromised during active session)
- Channels and groups
- Bot interactions

**iMessage:**
- All iMessage conversations
- FaceTime calls
- Shared media
- Message effects and reactions

**Other Platforms:**
- Facebook Messenger
- Instagram Direct
- Twitter DMs
- Snapchat messages (if captured before deletion)
- Any messaging platform installed

**Why Encryption Doesn't Protect:**
```
Normal Encrypted Messaging:
Device A → [Encrypted] → Network → [Encrypted] → Device B
         ↑ Data readable here             ↑ Data readable here

Pegasus Compromise:
Device A [PEGASUS] → Reads data before encryption
Device B [PEGASUS] → Reads data after decryption

Encryption protects data in transit, not at endpoints.
```

## Location and Movement Tracking

### GPS Data

**Real-Time Location:**
- Continuous GPS tracking
- Coordinates with high precision
- Altitude information
- Speed and direction of movement

**Location History:**
- Historical GPS coordinates
- Places frequently visited
- Movement patterns
- Time spent at locations

### Network-Based Location

**Wi-Fi Networks:**
- Networks connected to (SSID and BSSID)
- Saved network credentials
- Network location data
- Public Wi-Fi usage patterns

**Cell Tower Information:**
- Connected cell towers (Cell ID)
- Cell-based location approximation
- Roaming information
- Network provider data

### Location Metadata

**Photo Geotagging:**
- GPS coordinates embedded in photos
- When and where photos taken
- Camera location history

**App-Based Location:**
- Maps app history and saved places
- Ride-sharing trip history
- Food delivery addresses
- Travel booking information

## Environmental Surveillance

### Camera Access

**Remote Activation:**
- Front camera (covert selfie capture)
- Rear camera (environmental surveillance)
- Photo capture without notification
- Video recording
- No camera indicator light activation (bypassed)

**Photo Library:**
- All existing photos
- Recently deleted photos
- Hidden photos
- Shared albums
- Photo metadata (EXIF data)

### Microphone Access

**Ambient Audio Recording:**
- Room audio when phone is idle
- Conversations near phone
- Extended recording sessions
- Audio activated remotely

**Call Recording:**
- Both sides of phone conversations
- VoIP call audio
- Video call audio

### Environmental Data

**Sensor Data:**
- Accelerometer (movement patterns, activity)
- Gyroscope (device orientation)
- Proximity sensor (phone near face)
- Barometer (elevation changes)
- Magnetometer (compass direction)

## Device Contents and Files

### Document Access

**File System:**
- All documents (PDF, Word, Excel, etc.)
- Downloads folder
- Cloud sync folders (Dropbox, iCloud, Google Drive)
- Email attachments
- Work documents

**Media Files:**
- All videos on device
- Audio recordings
- Voice memos
- Screen recordings
- Downloaded media

### Application Data

**Social Media:**
- Facebook data cache
- Twitter cache and credentials
- Instagram photos and DMs
- LinkedIn messages and data
- TikTok videos and interactions

**Productivity Apps:**
- Notes and memos
- Calendar events
- Reminders and tasks
- Email (all accounts)
- Password managers (if decrypted)

**Financial Data:**
- Banking app data
- Payment app information
- Cryptocurrency wallet data
- Financial document scans

## Credentials and Authentication

### Stored Credentials

**Keychain/Keystore Access:**
- Saved passwords
- Authentication tokens
- API keys
- Encryption keys
- Certificate private keys

**Session Tokens:**
- Active login sessions
- OAuth tokens
- API authentication
- Cookies

### Biometric and Authentication

**Login Credentials:**
- Unlock PIN/password
- Screen lock patterns
- App passwords
- Website login credentials

**Biometric Data:**
- Fingerprint scans (stored templates)
- Face ID data (mathematical representation)
- Voice recognition data

## Web Activity and Browsing

### Browser Data

**Safari/Chrome/Firefox:**
- Complete browsing history
- Bookmarks
- Saved passwords
- Autofill information
- Open tabs and tab history

**Private Browsing:**
- Contrary to common belief, private browsing data accessible if Pegasus active during session
- No protection against kernel-level access

### Web-Based Communications

**Webmail:**
- Gmail, Yahoo, Outlook accessed via browser
- Email content and attachments
- Sent and received messages
- Contacts

**Social Media Web Access:**
- Facebook web sessions
- Twitter web activity
- Any social platform accessed via browser

## Metadata and Behavioral Analysis

### Contact Information

**Contact Database:**
- All contacts (names, numbers, emails)
- Contact photos
- Social network connections
- Frequently contacted people
- Recent communication patterns

### Communication Patterns

**Metadata Analysis:**
- Who communicates with whom
- Frequency of contact
- Timing of communications
- Communication method preferences
- Social network mapping

**Behavioral Patterns:**
- Sleep schedule (device usage patterns)
- Daily routines
- Social interactions
- Work patterns
- Travel habits

## Email and Professional Communications

### Email Accounts

**All Email Providers:**
- Corporate email (Exchange, Office 365)
- Personal email (Gmail, iCloud, Yahoo)
- Email metadata (sender, recipient, subject, time)
- Full email content
- Attachments

**Email Metadata:**
- Contact networks
- Professional relationships
- Organizational structure
- Communication timing

## Cloud and Backup Data

### Cloud Account Access

**Via Stored Credentials:**
- iCloud account access
- Google account access
- Microsoft OneDrive
- Dropbox
- Other cloud storage

**Synced Data:**
- Cloud-backed photos
- Document sync
- Backup data
- Cross-device information

## Exfiltration Methods

### Data Transmission

**Real-Time Streaming:**
- Active calls and conversations
- Current location
- Live camera/microphone feed

**Batch Uploads:**
- Collected messages
- Photo library
- Document files
- Historical data

**Selective Exfiltration:**
- Operators choose what data to extract
- Bandwidth-conscious transmission
- Prioritization of high-value data

### Network Channels

**Communication Methods:**
- HTTPS to C2 servers
- Encrypted channels
- Domain fronting (disguised as legitimate traffic)
- Scheduled transmissions (avoid suspicion)

## Data Usage and Analysis

### Operator Capabilities

**NSO Operator Interface:**
- Search collected data
- Filter by date, person, keyword
- Real-time monitoring dashboard
- Historical timeline view

**Analysis Tools:**
- Contact network visualization
- Location history maps
- Communication pattern analysis
- Keyword searching across all data

### Intelligence Value

**High-Value Data:**
- Source relationships (for journalists)
- Legal strategy (for lawyers)
- Political planning (for activists)
- Personal information for blackmail
- Financial information
- Travel plans

## Privacy Implications

### Complete Loss of Privacy

Once infected, assume:
- **No private conversations** (all communications monitored)
- **No private location** (constant tracking)
- **No private thoughts** (notes, drafts, memos accessible)
- **No private relationships** (all contacts and communications known)

### Secondary Impacts

**Professional Consequences:**
- Source confidentiality destroyed (journalists)
- Attorney-client privilege breached (lawyers)
- Activist networks exposed (human rights defenders)
- Business secrets compromised (executives)

**Personal Safety:**
- Physical location known to adversaries
- Daily routines mapped
- Travel plans exposed
- Personal relationships known

**Psychological Impact:**
- Awareness of surveillance chilling speech
- Self-censorship
- Paranoia and mistrust
- Emotional distress

## Data Retention

### Operator-Side Storage

**NSO Infrastructure:**
- Collected data stored on NSO servers
- Retention policies vary by customer
- Data may be stored indefinitely
- Multiple copies across infrastructure

**Customer Systems:**
- Customers receive collected data
- Storage under customer control
- Retention depends on local laws and policies
- Potential for data leaks or breaches

## Key Takeaways

1. **Complete Device Access:** Kernel-level compromise provides access to essentially all data on device.

2. **Encryption Bypassed:** End-to-end encryption ineffective against endpoint compromise.

3. **No Private Communications:** All messaging, calling, and email accessible regardless of platform.

4. **Continuous Surveillance:** Location, audio, video monitoring possible 24/7.

5. **Metadata as Valuable as Content:** Communication patterns reveal social networks and relationships.

6. **Cloud Not Safe:** Cloud account credentials enable access beyond just the device.

## References

[1] Amnesty International, "Forensic Methodology Report: How to catch NSO Group's Pegasus," July 2021.

[2] Citizen Lab, "The Pegasus Project: NSO Group's Surveillance Capabilities," 2021.

[3] WhatsApp Inc. v. NSO Group, Court Documents detailing surveillance capabilities, 2019.

[4] Forbidden Stories, "The Pegasus Project: Detailed Analysis of Surveillance," July 2021.

[5] Privacy International, "The Lifecycle of a Revolution: Surveillance and Counter-Surveillance," 2020.
