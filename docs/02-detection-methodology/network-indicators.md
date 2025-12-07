# Network Indicators

## Overview

Network indicators are traces of communication between infected devices and NSO Group's command-and-control (C2) infrastructure. These can be detected through DNS monitoring, traffic analysis, and TLS certificate inspection.

## DNS Indicators

### Known C2 Domains

**Historical Domains:**
- infections.pegasusinfections.com
- laxbrodstmedia.com
- usedirectory.com
- cloud-diagnose.com

**Current Domains:** See Amnesty Tech IOC repository for up-to-date list

### DNS Monitoring

```bash
# Monitor DNS queries on network
pi-hole # DNS sinkhole
tcpdump -i any port 53 # Packet capture
```

## IP Addresses

NSO infrastructure IP addresses change frequently. Check IOC databases for current indicators.

## TLS/SSL Indicators

### Certificate Patterns

- Self-signed certificates
- Unusual certificate authorities
- Short-lived certificates
- Domain fronting indicators

### Traffic Analysis

```bash
# Capture TLS connections
tcpdump -i any 'tcp port 443' -w capture.pcap

# Analyze with Wireshark
wireshark capture.pcap
```

## Traffic Patterns

### Suspicious Behaviors

- Encrypted traffic to unknown endpoints
- Regular beaconing (periodic check-ins)
- Large uploads (data exfiltration)
- Traffic at unusual times

## Domain Fronting

Pegasus may disguise C2 traffic as legitimate:

- Appears to connect to Google/AWS
- SNI header differs from actual destination
- Difficult to block without breaking legitimate services

## Defensive Monitoring

### Network-Level Blocking

**DNS Filtering:**
```
# Block known NSO domains
infections.pegasusinfections.com
*.pegasusinfections.com
[Other IOC domains]
```

**Firewall Rules:**
```
# Block known C2 IP addresses
iptables -A OUTPUT -d [NSO_IP] -j DROP
```

### VPN Protection

- Use trusted VPN provider
- Enable DNS over HTTPS/TLS
- Monitor VPN for leaks

## Limitations

- C2 domains change frequently
- Domain fronting hard to detect
- Encryption hides content
- Requires network access to monitor

## References

[1] Amnesty Tech, "Network IOC List," https://github.com/AmnestyTech/investigations

[2] Citizen Lab, "NSO Infrastructure Mapping," 2018-2023.
