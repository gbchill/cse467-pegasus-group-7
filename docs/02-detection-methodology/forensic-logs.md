# Forensic Log Collection

## iOS Log Collection

### sysdiagnose Collection

**Method 1: On Device**
```
1. Press Volume Up + Volume Down + Power button
2. Hold until device vibrates
3. Wait 10 minutes for generation
4. Connect to Mac
5. Open Finder > Device > Files
6. Navigate to sysdiagnose folder
```

**Method 2: Mac Trigger**
```
1. Connect iPhone to Mac
2. Open Terminal
3. Run: sudo sysdiagnose -u [UDID]
```

**What's Included:**
- System logs
- Crash reports
- Network diagnostics
- Process information
- Installed apps list

### iOS Backup

**Using Finder (macOS Catalina+):**
```
1. Connect device
2. Open Finder
3. Select device
4. Check "Encrypt local backup"
5. Set password
6. Click "Back Up Now"
```

**Backup Location:**
```
~/Library/Application Support/MobileSync/Backup/
```

## Android Log Collection

### ADB Logcat

```bash
# Real-time logs
adb logcat

# Save to file
adb logcat -d > logcat.txt

# Filtered logs
adb logcat -s TAG_NAME
```

### Bug Report

```bash
# Generate comprehensive bug report
adb bugreport bugreport.zip
```

### Full Backup

```bash
# Backup all apps and data
adb backup -all -f backup.ab -apk -shared
```

## What Logs Reveal

- Network connections (C2 domains)
- Process crashes (exploitation attempts)
- Suspicious file access
- Unusual system calls
- Installation patterns

## Preservation Best Practices

1. Create multiple copies
2. Store on encrypted drives
3. Document collection timestamp
4. Maintain chain of custody
5. Hash files for integrity verification
