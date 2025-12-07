#!/usr/bin/env python3
"""
Pegasus IOC Scanner - Educational Tool
A simple demonstration of how Indicators of Compromise (IOCs) can be used
to detect potential Pegasus infections by scanning log files.

WARNING: This is an educational tool, not a production security scanner.
For actual forensic analysis, use professional tools like MVT (Mobile Verification Toolkit).
"""

import argparse
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set

# ANSI color codes for terminal output
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class IOCScanner:
    def __init__(self, ioc_dir: str):
        """Initialize scanner with IOC databases"""
        self.ioc_dir = Path(ioc_dir)
        self.domains: Set[str] = self._load_domains()
        self.processes: Set[str] = self._load_processes()
        self.patterns: List[Dict] = self._load_patterns()
        self.findings: List[Dict] = []

    def _load_domains(self) -> Set[str]:
        """Load malicious domain indicators"""
        domains = set()
        domain_file = self.ioc_dir / 'domains.txt'

        if domain_file.exists():
            with open(domain_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        domains.add(line.lower())
        return domains

    def _load_processes(self) -> Set[str]:
        """Load suspicious process name indicators"""
        processes = set()
        process_file = self.ioc_dir / 'processes.txt'

        if process_file.exists():
            with open(process_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        processes.add(line.lower())
        return processes

    def _load_patterns(self) -> List[Dict]:
        """Load regex pattern indicators"""
        patterns = []
        pattern_file = self.ioc_dir / 'patterns.txt'

        if pattern_file.exists():
            with open(pattern_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Format: pattern|severity|description
                        parts = line.split('|')
                        if len(parts) == 3:
                            patterns.append({
                                'pattern': parts[0],
                                'severity': parts[1],
                                'description': parts[2]
                            })
        return patterns

    def scan_file(self, log_file: str) -> None:
        """Scan a log file for IOC matches"""
        print(f"\n{Colors.BOLD}Scanning:{Colors.END} {log_file}")
        print(f"{Colors.BOLD}IOC Database Loaded:{Colors.END}")
        print(f"  - Domains: {len(self.domains)}")
        print(f"  - Processes: {len(self.processes)}")
        print(f"  - Patterns: {len(self.patterns)}")
        print(f"\n{Colors.BOLD}Analyzing log file...{Colors.END}\n")

        with open(log_file, 'r', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                # Check domains
                for domain in self.domains:
                    if domain in line.lower():
                        self._add_finding(
                            'CRITICAL',
                            'Suspicious Domain Detected',
                            f"Known NSO infrastructure domain: {domain}",
                            line_num,
                            line.strip()
                        )

                # Check processes
                for process in self.processes:
                    if process in line.lower():
                        self._add_finding(
                            'HIGH',
                            'Suspicious Process Detected',
                            f"Process matches known indicator: {process}",
                            line_num,
                            line.strip()
                        )

                # Check patterns
                for pattern_dict in self.patterns:
                    try:
                        if re.search(pattern_dict['pattern'], line, re.IGNORECASE):
                            self._add_finding(
                                pattern_dict['severity'],
                                'Log Pattern Match',
                                pattern_dict['description'],
                                line_num,
                                line.strip()
                            )
                    except re.error:
                        pass  # Skip invalid regex patterns

    def _add_finding(self, severity: str, title: str, description: str,
                    line_num: int, content: str) -> None:
        """Add a finding to the results"""
        self.findings.append({
            'severity': severity,
            'title': title,
            'description': description,
            'line': line_num,
            'content': content[:200]  # Truncate long lines
        })

    def _get_severity_color(self, severity: str) -> str:
        """Get color code for severity level"""
        colors = {
            'CRITICAL': Colors.RED,
            'HIGH': Colors.YELLOW,
            'MEDIUM': Colors.BLUE,
            'LOW': Colors.GREEN
        }
        return colors.get(severity, '')

    def print_results(self) -> None:
        """Print scan results to console"""
        if not self.findings:
            print(f"{Colors.GREEN}{Colors.BOLD}No IOC matches found.{Colors.END}")
            print(f"\nNote: This does not guarantee the device is clean.")
            print(f"Unknown exploits and new Pegasus versions may not be detected.\n")
            return

        # Group findings by severity
        severity_order = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']
        severity_counts = {s: 0 for s in severity_order}

        print(f"\n{Colors.BOLD}{'='*80}{Colors.END}")
        print(f"{Colors.BOLD}FINDINGS:{Colors.END}\n")

        for finding in self.findings:
            severity = finding['severity']
            severity_counts[severity] += 1
            color = self._get_severity_color(severity)

            print(f"{color}{Colors.BOLD}[{severity}]{Colors.END} {finding['title']}")
            print(f"  Line {finding['line']}: {finding['description']}")
            print(f"  Context: {finding['content'][:100]}...")
            print()

        # Summary
        print(f"{Colors.BOLD}{'='*80}{Colors.END}")
        print(f"{Colors.BOLD}SUMMARY:{Colors.END}\n")

        for severity in severity_order:
            count = severity_counts[severity]
            if count > 0:
                color = self._get_severity_color(severity)
                print(f"{color}{severity}:{Colors.END} {count}")

        print(f"\n{Colors.BOLD}Total Findings: {len(self.findings)}{Colors.END}")

        # Recommendations
        print(f"\n{Colors.BOLD}{'='*80}{Colors.END}")
        print(f"{Colors.BOLD}RECOMMENDATIONS:{Colors.END}\n")

        if severity_counts['CRITICAL'] > 0:
            print(f"{Colors.RED}⚠ CRITICAL indicators detected!{Colors.END}")
            print(f"  1. Stop using this device for sensitive communications")
            print(f"  2. Contact professional forensic analysts")
            print(f"  3. See: docs/02-detection-methodology/detection-workflow.md")
            print(f"  4. Report to: Amnesty Tech (security@amnesty.org) or Citizen Lab")
        elif severity_counts['HIGH'] > 0:
            print(f"{Colors.YELLOW}⚠ HIGH severity indicators found.{Colors.END}")
            print(f"  1. Further investigation recommended")
            print(f"  2. Cross-reference with other detection methods")
            print(f"  3. Consider professional forensic analysis")
        else:
            print(f"  1. Review findings for false positives")
            print(f"  2. Monitor device for suspicious behavior")
            print(f"  3. Implement security hardening measures")

        print(f"\n{Colors.BOLD}IMPORTANT:{Colors.END}")
        print(f"  - This is an educational tool, not a comprehensive scanner")
        print(f"  - For actual forensic analysis, use MVT: https://github.com/mvt-project/mvt")
        print(f"  - False positives are possible - manual verification required")
        print(f"  - Absence of findings does NOT guarantee device is clean\n")

    def export_json(self, output_file: str) -> None:
        """Export results to JSON file"""
        results = {
            'scan_time': datetime.now().isoformat(),
            'total_findings': len(self.findings),
            'findings': self.findings,
            'summary': {
                severity: sum(1 for f in self.findings if f['severity'] == severity)
                for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']
            }
        }

        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"\n{Colors.GREEN}Results exported to: {output_file}{Colors.END}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Pegasus IOC Scanner - Educational tool for demonstrating IOC-based detection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scanner.py --log sample-logs/sample-sysdiagnose.log
  python scanner.py --log mylog.txt --output results.json

For more information, see: docs/02-detection-methodology/README.md
        """
    )

    parser.add_argument(
        '--log',
        required=True,
        help='Path to log file to scan'
    )

    parser.add_argument(
        '--iocs',
        default='iocs',
        help='Directory containing IOC databases (default: iocs/)'
    )

    parser.add_argument(
        '--output',
        help='Export results to JSON file'
    )

    args = parser.parse_args()

    # Validate inputs
    if not Path(args.log).exists():
        print(f"{Colors.RED}Error: Log file not found: {args.log}{Colors.END}")
        sys.exit(1)

    if not Path(args.iocs).exists():
        print(f"{Colors.RED}Error: IOC directory not found: {args.iocs}{Colors.END}")
        sys.exit(1)

    # Banner
    print(f"\n{Colors.BOLD}{'='*80}{Colors.END}")
    print(f"{Colors.BOLD}Pegasus IOC Scanner v1.0 - Educational Tool{Colors.END}")
    print(f"{Colors.BOLD}{'='*80}{Colors.END}")
    print(f"\n{Colors.YELLOW}WARNING:{Colors.END} This is an educational demonstration tool.")
    print(f"For actual forensic analysis, use MVT (Mobile Verification Toolkit).")
    print(f"See: https://github.com/mvt-project/mvt\n")

    # Run scan
    scanner = IOCScanner(args.iocs)
    scanner.scan_file(args.log)
    scanner.print_results()

    # Export if requested
    if args.output:
        scanner.export_json(args.output)

if __name__ == '__main__':
    main()
