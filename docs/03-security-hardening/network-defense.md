# Network Defense

## VPN Usage

### Trusted VPN Provider

Criteria:
- No-logs policy
- Strong encryption
- Jurisdiction outside surveillance alliances
- Proven track record

### Configuration

- Always-on VPN mode
- Kill switch enabled
- DNS leak protection
- IPv6 disabled (if VPN doesn't support)

## DNS Security

### DNS over HTTPS (DoH)

**iOS:**
```
Settings > General > VPN & Network > DNS > Configure DNS > Manual
Add: 1.1.1.1 (Cloudflare) or 8.8.8.8 (Google)
```

**Android:**
```
Settings > Network & Internet > Private DNS
```

### Pi-hole (Network-Wide)

Self-hosted DNS filtering blocking known malicious domains.

## Network Monitoring

Monitor for:
- Connections to unknown servers
- Unusual data transfers
- DNS queries to suspicious domains

## Public WiFi

**Best Practice:** Avoid entirely for sensitive work

**If Necessary:**
- Always use VPN
- Verify network name with staff
- Disable auto-connect
- Forget network after use

## References

[1] EFF, "Choosing a VPN," https://ssd.eff.org/
