# Pegasus Security Toolkit

A comprehensive educational resource for understanding, detecting, and defending against Pegasus-like mobile spyware threats.

## Project Context

**Course:** CSE 467 - Data Security
**Institution:** Arizona State University
**Team:** Group 7 - Ayush Singh, Chaitanya Singh, Cyler Minkus, Allan Binu, Nirek Shah, George Badulescu 
**Academic Year:** 2025

## Overview

This toolkit serves as an educational resource designed to provide in-depth analysis of sophisticated mobile spyware threats, specifically focusing on NSO Group's Pegasus surveillance software. The project emphasizes threat modeling, detection methodologies, and defensive strategies rather than implementing production-grade security tools.

Pegasus represents a class of advanced persistent threats (APTs) that exploit zero-day vulnerabilities in mobile operating systems to achieve complete device compromise. Understanding such threats is critical for security professionals, researchers, and high-risk individuals including journalists, activists, and political figures.

## What This Toolkit Provides

### 1. Threat Model Analysis
Comprehensive examination of Pegasus attack patterns, including:
- Threat actor profiling and targeting patterns
- Technical capabilities analysis (zero-click RCE, kernel-level access)
- Attack vector documentation (iMessage, WhatsApp, network injection)
- Privilege escalation and persistence mechanisms
- Data extraction targets and exfiltration methods

### 2. Detection Methodology
Practical guidance for identifying potential infections:
- Forensic log collection procedures for iOS and Android
- Mobile Verification Toolkit (MVT) usage guide
- Indicators of Compromise (IOC) analysis
- Step-by-step detection workflows
- Limitations and challenges in spyware detection

### 3. Security Hardening Recommendations
Actionable defense strategies:
- iOS security controls (Lockdown Mode, iMessage hardening)
- Android security configurations
- Network-layer defenses (VPN, DNS security)
- Operational security (OpSec) practices for high-risk users
- Device compartmentalization strategies

### 4. Technical Case Studies
Deep analysis of real-world exploits:
- CVE exploitation chain analysis (FORCEDENTRY, Trident)
- Zero-click attack technical deep dives
- Platform security comparison (iOS vs Android)
- Evolution of attack vectors (2016-2023)
- Why traditional antivirus solutions fail

### 5. Optional Technical Tools
Demonstration implementations:
- IOC Scanner: Pattern-matching tool for log analysis
- Educational proof-of-concept showing detection principles

## Repository Structure

```
cse467-pegasus-group-7/
├── docs/                              # Core documentation
│   ├── 01-threat-model/               # Threat analysis
│   ├── 02-detection-methodology/      # Detection workflows
│   ├── 03-security-hardening/         # Defense strategies
│   ├── 04-case-studies/               # Real-world analysis
│   ├── 05-technical-reference/        # Technical resources
│   └── images/                        # Diagrams and visuals
│
├── tools/                             # Optional technical components
│   └── ioc-scanner/                   # Simple IOC detection tool
│
├── resources/                         # Supporting materials
│   ├── mvt-setup-guide.md            # MVT installation
│   ├── sample-workflows.md            # Example scenarios
│   └── external-links.md              # Curated resources
│

```

## How to Use This Toolkit

### For Security Students and Researchers

1. **Start with Threat Modeling**
   Read [docs/01-threat-model/README.md](docs/01-threat-model/README.md) to understand the threat landscape, actor motivations, and attack capabilities.

2. **Understand Detection Methods**
   Review [docs/02-detection-methodology/README.md](docs/02-detection-methodology/README.md) to learn forensic analysis techniques and detection workflows.

3. **Apply Security Hardening**
   Implement recommendations from [docs/03-security-hardening/README.md](docs/03-security-hardening/README.md) to improve your security posture.

4. **Study Real-World Cases**
   Examine [docs/04-case-studies/README.md](docs/04-case-studies/README.md) for technical analysis of actual Pegasus exploits.

### For High-Risk Individuals

If you are a journalist, activist, or individual at elevated risk:

1. Review [docs/03-security-hardening/high-risk-users.md](docs/03-security-hardening/high-risk-users.md)
2. Implement iOS or Android defensive measures immediately
3. Follow operational security practices in [docs/03-security-hardening/opsec-practices.md](docs/03-security-hardening/opsec-practices.md)
4. Consider professional forensic analysis if infection is suspected

### For Instructors and Teaching Assistants

This project demonstrates understanding of:
- Advanced threat modeling for nation-state malware
- Mobile platform security architectures
- Forensic analysis methodologies
- Real-world exploit chain analysis
- Defense-in-depth security strategies

## Quick Start

### Reading the Documentation

All documentation is in Markdown format and can be read directly on GitHub or in any text editor.

Navigate to specific sections:
```bash
cd docs/01-threat-model/        # Threat analysis
cd docs/02-detection-methodology/  # Detection guides
cd docs/03-security-hardening/    # Defense strategies
cd docs/04-case-studies/          # Technical analysis
```

### Using the IOC Scanner (Optional)

The IOC Scanner is a simple educational tool demonstrating detection principles.

Requirements:
- Python 3.8 or higher
- No external dependencies (uses standard library only)

Basic usage:
```bash
cd tools/ioc-scanner
python scanner.py --log sample-logs/sample-sysdiagnose.log
```

For detailed instructions, see [tools/ioc-scanner/README.md](tools/ioc-scanner/README.md)

## Technical Components

### IOC Scanner

A lightweight pattern-matching tool that demonstrates how Indicators of Compromise (IOCs) are used to detect potential Pegasus infections. This tool:

- Scans log files for known malicious domains, processes, and patterns
- Compares findings against curated IOC databases
- Generates severity-rated reports (Critical/High/Medium/Low)
- Provides educational insight into detection methodology

**Important:** This is an educational demonstration, not a production security tool. For actual forensic analysis, use professional tools like MVT (Mobile Verification Toolkit).

## Educational Value

This project demonstrates mastery of:

1. **Threat Modeling** - Systematic analysis of sophisticated APT threats, including actor profiling, capability assessment, and attack surface analysis.

2. **Mobile Security Architecture** - Understanding iOS and Android security models, including sandboxing, code signing, exploit mitigation techniques, and platform-specific vulnerabilities.

3. **Exploit Analysis** - Technical breakdown of CVE exploitation chains, zero-click attack mechanisms, and modern exploitation techniques.

4. **Detection Methodology** - Forensic approaches to identifying advanced malware, including log analysis, IOC matching, and behavioral analysis.

5. **Defense Strategies** - Multi-layered security controls, from OS-level hardening to operational security practices.

6. **Research Skills** - Synthesis of academic research, industry reports, and technical publications into actionable security guidance.

## Key Learning Outcomes

After engaging with this toolkit, users will be able to:

- Explain how advanced mobile spyware like Pegasus operates at a technical level
- Identify indicators of compromise in mobile device logs
- Implement evidence-based security hardening measures
- Analyze CVE exploitation chains and zero-day vulnerabilities
- Understand limitations of traditional security tools against targeted attacks
- Apply threat modeling principles to real-world scenarios

## Important Disclaimers

### Educational Purpose

This toolkit is designed exclusively for educational and research purposes. All information is derived from publicly available sources, including academic research, industry reports, and responsible security disclosures.

### Not a Production Tool

The technical components provided (including the IOC Scanner) are educational demonstrations. They are not intended for production use or as replacements for professional security tools. For actual threat detection, consult professional forensic analysts and use established tools like MVT.

### Ethical Considerations

Users must:
- Obtain proper authorization before conducting any security testing
- Respect privacy and legal boundaries
- Use this knowledge for defensive purposes only
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

### Detection Limitations

No detection method is foolproof. Pegasus and similar tools:
- Continuously evolve to evade detection
- May leave minimal forensic traces
- Can employ anti-forensics techniques
- Require specialized expertise to identify

Professional forensic analysis is recommended for suspected infections.

## Key References

This toolkit synthesizes information from authoritative sources including:

1. **Citizen Lab** - University of Toronto Munk School research on Pegasus targeting and technical analysis
2. **Amnesty International Security Lab** - Forensic methodology and MVT tool development
3. **Apple/Google Security Bulletins** - Official vulnerability disclosures and patches
4. **Project Zero** - Google's elite security team research on mobile exploitation
5. **Academic Research** - Peer-reviewed papers on mobile security and spyware detection

For complete references, see [docs/05-technical-reference/references.md](docs/05-technical-reference/references.md)

## Contributing

This is an academic project for CSE 467. Contributions are limited to team members:

- George Badulescu
- [Additional team members]

For questions or feedback, please contact the course instructor or teaching assistants.

## Project Timeline

- **Week 1-2:** Threat model documentation and research
- **Week 3:** Detection methodology and security hardening guides
- **Week 4:** Case studies and technical analysis
- **Week 5:** IOC Scanner implementation and testing
- **Week 6:** Documentation review and presentation preparation

## License

This project is released under the MIT License with an educational use notice. See [LICENSE](LICENSE) for complete terms.

## Acknowledgments

This educational project builds upon the critical work of:

- The Citizen Lab at the University of Toronto Munk School
- Amnesty International Security Lab and the MVT project
- Security researchers who responsibly disclosed Pegasus vulnerabilities
- Journalists and civil society organizations documenting surveillance abuses

## Contact

**Course:** CSE 467 - Data Security
**Institution:** Arizona State University
**Repository:** https://github.com/gbchill/cse467-pegasus-group-7

For academic inquiries, please contact through official university channels.

---

**Last Updated:** December 2025
**Documentation Status:** Complete
**Code Status:** Educational demonstration
