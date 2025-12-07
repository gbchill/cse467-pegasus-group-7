# Threat Actors: NSO Group and Pegasus Customers

## Overview

Understanding the threat actors behind Pegasus is essential for comprehensive threat modeling. Unlike typical malware distributed broadly by cybercriminals, Pegasus is a commercial surveillance product sold exclusively to government clients. This creates a unique threat landscape where the attackers are nation-states with legal authority in their jurisdictions, virtually unlimited resources, and sophisticated targeting capabilities.

## NSO Group: The Developer

### Background

NSO Group Technologies is an Israeli cybersecurity and surveillance company founded in 2010 by Niv Carmi, Omri Lavie, and Shalev Hulio. The company specializes in developing sophisticated surveillance technologies sold exclusively to government intelligence and law enforcement agencies.

**Key Facts:**
- Founded: 2010 in Herzliya, Israel
- Employees: Estimated 500-700 (mostly former Israeli intelligence personnel)
- Valuation: Approximately $1 billion USD (as of 2019)
- Ownership: Private equity (Francisco Partners, Novalpina Capital)
- Regulation: Operates under Israeli Ministry of Defense export license requirements

### Business Model

NSO Group operates on a commercial model with government-only customers:

1. **Licensing Structure**
   - Fixed setup fee ($500,000 - $650,000 reported)
   - Per-target monitoring fees ($5,000 - $15,000 per device)
   - Minimum contract values in millions of dollars
   - Technical support and updates included

2. **Customer Selection Criteria** (claimed)
   - Government intelligence agencies only
   - Law enforcement organizations
   - Compliance with Israeli export regulations
   - Human rights vetting process (disputed effectiveness)

3. **Service Delivery**
   - Cloud-based exploitation infrastructure
   - Technical training for operators
   - Target selection and management interfaces
   - Data collection and analysis tools

### Stated Purpose vs. Documented Use

**NSO's Official Position:**
- Tools designed for counter-terrorism and serious crime investigation
- Prevents child abuse, drug trafficking, and violent crime
- Saves lives through legitimate law enforcement use
- Has robust human rights compliance programs

**Documented Reality:**
- Widespread targeting of journalists, activists, and dissidents
- Abuse by authoritarian regimes for political surveillance
- Targeting of lawyers, NGO workers, and opposition politicians
- Minimal evidence of effective oversight or human rights compliance

## Customer Governments

### Confirmed Customers

Based on forensic analysis, leaked documents, and investigative journalism:

| Country | Confirmation Source | Notable Targeting |
|---------|-------------------|-------------------|
| **Saudi Arabia** | Forensic evidence | Jamal Khashoggi associates, dissidents |
| **UAE** | Forensic evidence | Activists, journalists, diplomats |
| **Mexico** | Forensic evidence | Journalists, anti-corruption investigators |
| **Morocco** | Forensic evidence | Journalists, politicians |
| **Azerbaijan** | Forensic evidence | Opposition politicians, activists |
| **Bahrain** | Forensic evidence | Human rights activists |
| **Kazakhstan** | Forensic evidence | Journalists, activists |
| **Rwanda** | Forensic evidence | Opposition figures in exile |
| **Hungary** | Forensic evidence | Journalists, political opposition |
| **India** | Forensic evidence | Journalists, opposition politicians |
| **Togo** | Leaked documents | Unknown targets |
| **Panama** | Leaked documents | Unknown targets |

**Additional suspected customers based on various evidence:** Spain, Poland, Thailand, Kenya, Uzbekistan, Oman, and others.

### Customer Categories

NSO's government customers generally fall into three categories:

#### 1. Democratic Nations with Rule of Law
**Examples:** European democracies, some developed nations

**Justifications:**
- Counter-terrorism operations
- Organized crime investigation
- Child exploitation prevention

**Concerns:**
- Judicial oversight may be insufficient
- Mission creep beyond original authorization
- Vulnerability to political pressure

#### 2. Hybrid Regimes with Limited Press Freedom
**Examples:** India, Hungary, Mexico

**Documented Uses:**
- Surveillance of investigative journalists
- Monitoring political opposition
- Targeting corruption investigators
- Intimidation of civil society

#### 3. Authoritarian States with Poor Human Rights Records
**Examples:** Saudi Arabia, UAE, Bahrain, Azerbaijan

**Documented Uses:**
- Silencing dissent and political opposition
- Tracking and threatening exiled activists
- Monitoring family members of dissidents
- Facilitating physical violence against targets

## Targeting Patterns

### Primary Target Categories

Analysis of confirmed Pegasus infections reveals consistent targeting patterns:

#### 1. Journalists (Most Common)
- Investigative reporters covering corruption
- Reporters documenting human rights abuses
- Journalists covering conflicts and government activities
- Media organization staff and editors

**Notable Cases:**
- Jamal Khashoggi circle (Washington Post)
- Roula Khalaf (Financial Times editor)
- Siddharth Varadarajan (The Wire, India)
- Carmen Aristegui (Mexican investigative journalist)

#### 2. Human Rights Activists
- Activists documenting government abuses
- Women's rights advocates
- LGBTQ+ rights organizers
- Environmental activists

#### 3. Political Opposition
- Opposition party leaders
- Political campaign staff
- Lawyers representing opposition figures
- Family members of political opponents

#### 4. Lawyers and Legal Professionals
- Defense attorneys in sensitive cases
- Human rights lawyers
- Prosecutors investigating corruption
- International criminal court staff

#### 5. Civil Society Organizations
- NGO leadership and staff
- Academic researchers
- Think tank personnel
- International organization employees

#### 6. Diplomats and Government Officials
- Foreign diplomats
- International organization staff
- Government officials from rival factions
- Military and intelligence personnel (from rival nations)

### Geographic Patterns

Pegasus targeting shows global reach:

- **Middle East:** Extensive use by Gulf states for regional influence
- **Latin America:** Mexico shows highest concentration of known targets
- **Europe:** Increasing detection in EU member states
- **South Asia:** Significant activity in India
- **Africa:** Multiple authoritarian regimes deploy Pegasus
- **Global:** Targeting of exiles and diaspora communities worldwide

## Motivations and Objectives

### Government Customer Motivations

Different customers deploy Pegasus for varying objectives:

#### 1. Political Control
- Monitoring opposition movements
- Identifying dissent before it organizes
- Gathering compromising information on rivals
- Intimidating critics and activists

#### 2. Geopolitical Advantage
- Espionage against other nations
- Monitoring diplomatic negotiations
- Economic intelligence gathering
- Tracking rival government officials

#### 3. Public Relations Management
- Identifying sources of negative media coverage
- Tracking journalists investigating government
- Monitoring activists planning protests
- Preventing whistleblowing and leaks

#### 4. Legitimate Law Enforcement (Claimed)
- Counter-terrorism investigations
- Organized crime disruption
- Child exploitation prevention
- Drug trafficking investigations

**Note:** While NSO claims predominant use for legitimate purposes, the vast majority of documented cases involve political targeting rather than criminal investigation.

## Legal and Regulatory Context

### Israeli Export Control

NSO Group operates under Israeli government oversight:

- **Export License Required:** Israeli Ministry of Defense must approve all sales
- **Review Process:** Claimed vetting of customer human rights records
- **Effectiveness Questioned:** Multiple sales to documented human rights abusers
- **Ongoing Investigation:** Israeli government reviewing NSO operations (as of 2021)

### International Legal Challenges

Pegasus has faced numerous legal challenges:

#### WhatsApp v. NSO Group (US, 2019)
- WhatsApp sued NSO for exploiting vulnerability
- Alleged targeting of 1,400 users including diplomats and activists
- Case ongoing; NSO claims sovereign immunity

#### Apple v. NSO Group (US, 2021)
- Apple sued NSO for targeting Apple users
- Seeks permanent injunction against NSO using Apple products
- Part of broader effort to protect users from state-sponsored attacks

#### French Investigation (2021)
- French prosecutors investigating potential surveillance of French officials
- Includes President Macron's phone number in leaked target list
- Diplomatic tensions with Morocco and Israel

#### European Parliament Inquiry (2021-2022)
- Investigation into Pegasus use in EU member states
- Focus on Poland, Hungary, Spain deployments
- Questions about rule of law and press freedom

## Ethical Considerations

The Pegasus ecosystem raises fundamental ethical questions:

### Dual-Use Technology Dilemma
- Can powerful surveillance tools exist without abuse?
- Is effective oversight possible for secretive intelligence tools?
- Should such capabilities be commercially available?

### Corporate Responsibility
- Does NSO bear responsibility for customer misuse?
- Are human rights vetting processes meaningful?
- Should companies sell to governments with poor human rights records?

### Democratic Governance
- How can democracies balance security needs with civil liberties?
- Are judicial oversight mechanisms sufficient?
- What transparency is appropriate for intelligence capabilities?

### International Norms
- Should there be international regulation of surveillance technology?
- What constitutes legitimate use of such tools?
- How can cross-border abuses be prevented?

## Evolution of Threat Actor Landscape

### NSO Group's Current Status (2024-2025)

Following extensive media exposure and legal challenges:

- **US Commerce Department Blacklist** (November 2021): Added to Entity List, restricting US technology access
- **Apple Lawsuit** (2021): Ongoing litigation restricting NSO's access to Apple infrastructure
- **Financial Difficulties**: Reported restructuring and financial challenges
- **Ownership Changes**: Ongoing reorganization of company ownership
- **Continued Operations**: Despite challenges, NSO reportedly continues developing surveillance tools

### Emerging Competitors

The commercial surveillance market extends beyond NSO:

- **Candiru (Israel):** Similar capabilities, exposed by Citizen Lab and Microsoft
- **Cytrox (North Macedonia/Israel):** Predator spyware, similar to Pegasus
- **QuaDream (Israel):** REIGN spyware targeting iOS and Android
- **Intellexa (Greece/Israel):** Alliance of surveillance vendors
- **Government In-House Capabilities:** Major powers developing similar tools internally

## Key Takeaways

1. **Sophisticated Threat Actor**: NSO Group represents a well-resourced, technically capable adversary with state backing and intelligence community expertise.

2. **Government Customers Vary Widely**: From democratic nations to authoritarian regimes, with vastly different accountability levels and targeting patterns.

3. **Political Targeting Predominates**: Despite claims of focus on terrorism and serious crime, documented use overwhelmingly targets journalists, activists, and political opponents.

4. **Global Reach**: Pegasus operations span multiple continents with targeting of individuals far from customer countries.

5. **Limited Accountability**: Despite media exposure and legal challenges, effective oversight and accountability remain elusive.

6. **Evolving Threat Landscape**: Even if NSO Group faces consequences, the commercial surveillance market continues with multiple competitors.

## Implications for Defense

Understanding threat actors informs defensive strategies:

- **High-Risk Individuals** should assume persistent, sophisticated targeting
- **Traditional Trust Models Fail** when attackers are governments with legal authority
- **Technical Defenses Essential** as legal protections may be unavailable
- **Operational Security Critical** to avoid providing targeting triggers
- **International Mobility Considerations** when traveling to countries with known Pegasus deployments

## References

[1] Citizen Lab, "The Pegasus Project," University of Toronto, 2021.

[2] Forbidden Stories and Amnesty International, "The Pegasus Project," July 2021.

[3] Marczak, B., and Scott-Railton, J., "Hide and Seek: Tracking NSO Group's Pegasus Spyware to Operations in 45 Countries," Citizen Lab, September 2018.

[4] WhatsApp Inc. v. NSO Group Technologies Limited, Case No. 19-cv-07123-PJH (N.D. Cal. 2019).

[5] Apple Inc. v. NSO Group Technologies Limited, Case No. 21-cv-09388 (N.D. Cal. 2021).

[6] Huillet, M., "NSO Group: The Company Behind Pegasus," Le Monde, July 2021.

[7] Kirchgaessner, S., et al., "Revealed: leak uncovers global abuse of cyber-surveillance weapon," The Guardian, July 2021.

[8] European Parliament Committee of Inquiry on Pegasus, "Draft Report," 2022.
