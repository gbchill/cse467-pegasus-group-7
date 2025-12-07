# iOS Security Hardening

## Lockdown Mode (iOS 16+)

**Most Effective Defense Against Zero-Click Exploits**

### What It Does

- Disables complex message attachments in iMessage
- Blocks link previews
- Disables most web technologies
- Restricts incoming FaceTime calls
- Blocks configuration profiles
- Disables wired connections when locked

### How to Enable

```
Settings > Privacy & Security > Lockdown Mode > Turn On Lockdown Mode
```

### Impact

**Protections:**
- Significantly reduces attack surface
- Blocks many zero-click vectors
- Makes exploitation much more difficult

**Limitations:**
- Some websites may not work correctly
- Certain features disabled
- May impact usability

**Recommendation:** Enable for high-risk users

## iMessage Security

### Option 1: Disable iMessage (Most Secure)

```
Settings > Messages > Toggle off iMessage
```

**Impact:** Cannot send/receive iMessages, primary Pegasus vector eliminated

### Option 2: Harden iMessage

If disabling not feasible:

```
Settings > Messages > Send & Receive
- Use only phone number, remove email addresses
- Disable "Share Name and Photo"

Settings > Messages > Filter Unknown Senders > Enable
```

## Link Preview Disabling

```
Settings > Messages > Link Previews > Disable
Safari > Settings > Disable link previews
```

Link previews automatically process content - potential attack vector.

## App Permissions Audit

### Review and Minimize

```
Settings > Privacy & Security > Review each category:
- Location Services (disable for non-essential apps)
- Contacts (minimal access)
- Photos (only apps that need it)
- Microphone (review regularly)
- Camera (review regularly)
```

**Principle:** Only grant necessary permissions

## Update Management

### Automatic Updates

```
Settings > General > Software Update > Automatic Updates > Enable
```

**Critical:** Security updates patch zero-days

### Manual Update Check

Check daily for high-risk users:
```
Settings > General > Software Update
```

## Additional Hardening

### Disable Unused Features

```
Settings > FaceTime > Toggle off (if not needed)
Settings > Safari > Block All Cookies > Enable
Settings > Safari > Fraudulent Website Warning > Enable
```

### Bluetooth Security

```
Settings > Bluetooth > Off when not in use
```

Bluetooth exploits less common but possible.

### Password Security

```
Settings > Face ID & Passcode > Require 6-digit or alphanumeric passcode
- Enable "Erase Data" after 10 failed attempts (if comfortable with risk)
```

## Backup Strategy

### Encrypted Backups

Always encrypt iPhone backups:

```
Finder > iPhone > Encrypt local backup > Set strong password
```

### Cloud Backup Considerations

iCloud backups:
- Convenient but accessible to Apple (and governments with warrants)
- Consider disabling for extremely sensitive data
- Enable Advanced Data Protection (iOS 16.2+) for stronger encryption

## Emergency Actions

If infection suspected:

1. Enable Airplane Mode immediately
2. Document current state (photos of screen)
3. Do NOT factory reset yet (destroys evidence)
4. Contact security experts
5. Collect forensic logs
6. Only then: Factory reset + new device + new phone number

## Key Takeaways

1. **Lockdown Mode** - Single most effective iOS defense
2. **Updates Critical** - Install immediately
3. **Disable iMessage** - If can tolerate impact
4. **Minimize Permissions** - Principle of least privilege
5. **Regular Audits** - Review settings periodically

## References

[1] Apple, "iOS Security Guide," 2023.

[2] Apple Support, "Lockdown Mode," https://support.apple.com/en-us/HT212650
