# MVT Setup and Usage Guide

## What is MVT?

Mobile Verification Toolkit (MVT) is the official forensic tool developed by Amnesty International's Security Lab for detecting Pegasus and similar spyware on mobile devices.

## Installation

### Requirements

- Python 3.6 or higher
- pip3
- libusb (for iOS)

### macOS Installation

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 libusb

# Install MVT
pip3 install mvt
```

### Linux (Ubuntu/Debian) Installation

```bash
# Update package lists
sudo apt update

# Install dependencies
sudo apt install python3 python3-pip libusb-1.0-0

# Install MVT
pip3 install mvt
```

### Windows Installation

```bash
# Install Python 3 from python.org
# Then in PowerShell or Command Prompt:

pip3 install mvt
```

### Verify Installation

```bash
mvt-ios --help
mvt-android --help
```

## iOS Analysis

### Step 1: Create Device Backup

**Using Finder (macOS Catalina or later):**
1. Connect iPhone to Mac
2. Open Finder
3. Select iPhone in sidebar
4. Check "Encrypt local backup"
5. Set strong password (remember it!)
6. Click "Back Up Now"

**Backup Location:**
```
~/Library/Application Support/MobileSync/Backup/
```

### Step 2: Download IOC Database

```bash
# Clone Amnesty Tech IOC repository
git clone https://github.com/AmnestyTech/investigations.git

# IOC file location
cd investigations/indicators/
ls pegasus.stix2
```

### Step 3: Run MVT Analysis

```bash
# Basic analysis
mvt-ios check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output ./mvt-results \
  ~/Library/Application\ Support/MobileSync/Backup/[BACKUP_ID]/

# With specific modules
mvt-ios check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output ./mvt-results \
  --module chrome \
  --module sms \
  ~/Library/Application\ Support/MobileSync/Backup/[BACKUP_ID]/
```

### Step 4: Analyze Results

Check output directory:
```
mvt-results/
├── command.txt              # Command executed
├── timeline.csv             # All events chronologically
├── timeline_detected.csv    # Flagged events only
└── logs/                    # Detailed module logs
```

**Review:**
1. Open `timeline_detected.csv` first
2. Check for CRITICAL or HIGH severity findings
3. Cross-reference with raw logs
4. Investigate flagged domains/processes

## Android Analysis

### Step 1: Enable USB Debugging

On Android device:
```
Settings > About Phone > Tap "Build Number" 7 times
Settings > System > Developer Options > USB Debugging > Enable
```

### Step 2: Install ADB

**macOS:**
```bash
brew install android-platform-tools
```

**Linux:**
```bash
sudo apt install adb
```

**Verify:**
```bash
adb devices
```

### Step 3: Run MVT Analysis

**Check via ADB (recommended):**
```bash
mvt-android check-adb \
  --iocs investigations/indicators/pegasus.stix2 \
  --output ./mvt-results
```

**Or check backup:**
```bash
# Create backup
adb backup -all -f backup.ab

# Analyze backup
mvt-android check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output ./mvt-results \
  backup.ab
```

## Interpreting Results

### Detection Levels

| Indicator | Meaning | Action |
|-----------|---------|--------|
| Multiple detections | High confidence | Contact professional analysts immediately |
| Single domain match | Moderate concern | Cross-reference, investigate further |
| Process match only | Low-medium concern | Context dependent, may be false positive |
| No detections | Unclear | Does NOT guarantee clean device |

### Common False Positives

- Legitimate CDN domains
- Corporate VPN/MDM software
- News websites previously compromised
- Crash logs from normal app bugs

### Verification Steps

1. Check timing - coordinated suspicious activity?
2. Research flagged domains - legitimate service or known C2?
3. Cross-reference multiple data sources
4. Consider user context (journalist vs. regular user)

## Advanced Usage

### Update IOCs

```bash
cd investigations
git pull origin main
```

### Export Specific Modules

```bash
mvt-ios check-backup \
  --iocs investigations/indicators/pegasus.stix2 \
  --output ./results \
  --module sms \
  --module chrome_history \
  --module safari_history \
  /path/to/backup
```

### List Available Modules

```bash
mvt-ios check-backup --help
mvt-android check-adb --help
```

## Troubleshooting

### "Command not found: mvt-ios"

Solution:
```bash
# Add to PATH
export PATH=$PATH:~/.local/bin

# Or reinstall
pip3 install --user --upgrade mvt
```

### "Unable to find backup"

Find backup location:
```bash
# macOS
ls ~/Library/Application\ Support/MobileSync/Backup/

# Look for directories with alphanumeric names
```

### "Permission denied"

```bash
# Fix permissions (macOS/Linux)
chmod +x ~/.local/bin/mvt-*

# Or run with python
python3 -m mvt.ios.check_backup [options]
```

## When to Contact Experts

Contact professional analysts if:
- Multiple CRITICAL detections found
- You are a high-risk user (journalist, activist)
- Coordinated suspicious activity detected
- Need legal-grade forensic analysis

**Resources:**
- Amnesty Tech: security@amnesty.org
- Citizen Lab: info@citizenlab.ca
- Access Now Digital Security Helpline

## References

[1] MVT Documentation: https://docs.mvt.re/

[2] Amnesty Tech IOCs: https://github.com/AmnestyTech/investigations

[3] Amnesty International, "Forensic Methodology Report," 2021.
