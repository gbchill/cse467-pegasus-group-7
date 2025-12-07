# Mobile Verification Toolkit (MVT)

## What is MVT?

MVT is an open-source forensic tool developed by Amnesty International's Security Lab specifically for detecting Pegasus spyware on iOS and Android devices.

**Repository:** https://github.com/mvt-project/mvt

## Installation

### Requirements
- Python 3.6+
- pip3
- libusb (for iOS)

### Install via pip

```bash
pip3 install mvt
```

### Verify Installation

```bash
mvt-ios --help
mvt-android --help
```

## Basic Usage

### iOS Analysis

**Check Backup:**
```bash
mvt-ios check-backup \
  --iocs indicators.stix2 \
  --output ./results \
  /path/to/backup
```

**Check Filesystem:**
```bash
mvt-ios check-fs \
  --iocs indicators.stix2 \
  --output ./results \
  /path/to/filesystem
```

### Android Analysis

**Check Backup:**
```bash
mvt-android check-backup \
  --iocs indicators.stix2 \
  --output ./results \
  backup.ab
```

**Check via ADB:**
```bash
mvt-android check-adb \
  --iocs indicators.stix2 \
  --output ./results
```

## IOC Database

Download Amnesty Tech IOC repository:

```bash
git clone https://github.com/AmnestyTech/investigations.git
```

Use IOCs:
```bash
--iocs investigations/indicators/pegasus.stix2
```

## Interpreting Results

### Output Files

- **timeline.csv** - All events chronologically
- **timeline_detected.csv** - Flagged events only
- **[module].json** - Raw data per analysis module

### Detection Levels

- **RED**: Strong indicator of compromise
- **YELLOW**: Suspicious activity warranting investigation
- **GREEN**: Clean / no detections

## Common Detections

- Suspicious domains in browser history
- Known Pegasus processes
- Exploitation artifacts in crash logs
- C2 infrastructure connections

## Limitations

- Cannot detect unknown exploits
- Requires device access/backup
- May produce false positives
- IOC database may be incomplete

## References

[1] MVT Documentation: https://docs.mvt.re/

[2] Amnesty International, "Forensic Methodology Report," 2021.
