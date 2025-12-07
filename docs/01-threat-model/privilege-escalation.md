# Privilege Escalation: From Initial Access to Kernel Control

## Overview

Privilege escalation is the process by which Pegasus transforms initial code execution in a restricted process into complete kernel-level control. This is accomplished through exploit chains that systematically bypass each layer of mobile operating system security. Understanding privilege escalation techniques is essential for comprehending how sophisticated malware defeats modern security architectures.

## Mobile Security Model

### Privilege Levels

Modern mobile operating systems implement multiple privilege levels:

```
┌─────────────────────────────────────┐
│         Kernel Space                │  ← Highest Privilege
│  (Complete hardware & memory access) │     (Pegasus Goal)
├─────────────────────────────────────┤
│       System Services               │
│  (Core OS functionality, elevated)   │
├─────────────────────────────────────┤
│      User Applications              │
│  (Sandboxed, restricted access)      │  ← Typical Initial Access
└─────────────────────────────────────┘
```

**User Space:**
- Applications run with minimal privileges
- Sandboxed (isolated from other apps and system)
- Limited to accessing own data
- Cannot directly access hardware

**Kernel Space:**
- Complete access to all hardware
- Can read/write any memory
- Controls all processes
- Enforces security policies

### Security Boundaries

Multiple security mechanisms must be bypassed:

1. **Sandboxing:** Isolates applications from each other and system
2. **Code Signing:** Ensures only authorized code executes
3. **Address Space Layout Randomization (ASLR):** Randomizes memory addresses
4. **Data Execution Prevention (DEP/W^X):** Prevents code execution in data segments
5. **Pointer Authentication (iOS):** Validates pointer integrity
6. **Kernel Patch Protection:** Prevents kernel memory modification

## Exploit Chain Methodology

Pegasus uses multi-stage exploit chains to progressively gain privileges:

### Stage 1: Initial Code Execution

**Objective:** Execute attacker code within restricted process

**Common Entry Points:**
- iMessage rendering process (IMTranscoderAgent on iOS)
- WhatsApp call handling
- Browser rendering engine
- Media file parsers

**Techniques:**
- Memory corruption (buffer overflows, use-after-free)
- Integer overflows in image/document parsing
- Type confusion vulnerabilities
- Logic errors in protocol implementations

**Example: FORCEDENTRY Initial Execution**
```
1. Malicious GIF delivered via iMessage
2. CoreGraphics processes GIF automatically
3. Integer overflow in GIF decoder
4. Heap memory corruption
5. Attacker controls program execution
6. Payload executed within IMTranscoderAgent process
```

**Limitations at This Stage:**
- Still sandboxed (limited file access)
- Cannot access other apps' data
- Cannot modify system
- Cannot persist across reboot

### Stage 2: Sandbox Escape

**Objective:** Break out of application sandbox restrictions

**iOS Sandbox Model:**
- Each app runs in isolated container
- Limited to reading/writing own directory
- Inter-process communication (IPC) strictly controlled
- System services accessible only through approved APIs

**Sandbox Escape Techniques:**

#### 1. IPC Vulnerability Exploitation
- Target system services that communicate with sandboxed apps
- Exploit parsing vulnerabilities in IPC messages
- Gain code execution in less-restricted system service

#### 2. Mach Port Confusion
- iOS uses Mach ports for IPC
- Exploit vulnerabilities in port handling
- Send malicious messages to privileged services

#### 3. XPC Service Exploitation
- XPC is iOS IPC mechanism
- Privileged XPC services handle requests from apps
- Exploit validation errors in XPC services
- Achieve code execution outside sandbox

**Example Sandbox Escape Flow:**
```
1. From sandboxed process, craft malicious IPC message
2. Send to system service with elevated privileges
3. Trigger vulnerability in service's message parsing
4. Gain code execution in system service
5. Now operating outside original sandbox
```

**Capabilities After Sandbox Escape:**
- Access to more system resources
- Ability to communicate with more services
- Access to some shared data
- Still not kernel-level

### Stage 3: Kernel Memory Disclosure

**Objective:** Learn kernel memory addresses to defeat ASLR

**Challenge:**
- ASLR randomizes kernel memory addresses
- Exploits need to know memory layout
- Kernel addresses change on each boot

**Information Leak Techniques:**

#### 1. Kernel Information Leak Vulnerabilities
- Exploit bugs that disclose kernel memory
- System calls that return more data than intended
- Race conditions revealing kernel pointers
- Timing side-channels leaking address information

#### 2. Speculative Execution Side Channels
- Meltdown/Spectre-class vulnerabilities
- Use CPU speculative execution to read kernel memory
- Works even from unprivileged processes

**Example: Trident Information Leak (CVE-2016-4655)**
```c
// Simplified concept
1. Call kernel function with specific parameters
2. Function leaks kernel memory address in return value
3. Calculate other kernel addresses from known offsets
4. ASLR defeated - exploit now knows where kernel code is
```

### Stage 4: Kernel Exploitation

**Objective:** Execute code in kernel mode with full privileges

**Common Kernel Vulnerabilities:**

#### 1. Memory Corruption
- Buffer overflows in kernel code
- Use-after-free in kernel memory management
- Heap overflow in kernel allocators
- Double-free vulnerabilities

#### 2. Race Conditions
- Time-of-check to time-of-use (TOCTTOU)
- Multiple threads accessing kernel resources
- Exploit timing windows in kernel code

#### 3. Logic Errors
- Incorrect privilege checks
- Missing validation in system calls
- Flawed state machine implementations

**Example Kernel Exploit Flow:**
```
1. Allocate kernel memory through system call
2. Trigger use-after-free vulnerability
3. Allocate new object in freed memory location
4. Achieve type confusion in kernel
5. Overwrite kernel function pointer
6. Trigger function pointer call
7. Kernel executes attacker code
8. Full kernel privileges achieved
```

### Stage 5: Persistence and Payload Deployment

**Objective:** Maintain access and deploy full Pegasus payload

Once kernel control is achieved:

1. **Disable Security Controls**
   - Turn off code signing enforcement
   - Disable security logging
   - Bypass integrity checks

2. **Install Pegasus Payload**
   - Load kernel extension/module
   - Hook system calls for monitoring
   - Inject into system processes

3. **Establish Persistence**
   - Modify system files (if re-infection needed)
   - Hook boot process (limited by Secure Boot)
   - Monitor for OS updates

4. **Begin Surveillance**
   - Activate data collection
   - Establish C2 communications
   - Start exfiltration

## Platform-Specific Escalation

### iOS Privilege Escalation

#### Unique Challenges
- Strong code signing
- Secure Boot chain
- System integrity protection
- Pointer Authentication (A12+ chips)

#### Common Techniques

**Kernel Cache Exploitation:**
```
iOS kernelcache is compiled binary containing kernel + extensions
Exploit targets vulnerabilities in:
- IOKit drivers (common attack surface)
- Network stack
- File system implementations
- IPC mechanisms
```

**IOKit User Client Exploitation:**
- IOKit provides user-space access to drivers
- User clients handle communication with kernel drivers
- Many documented vulnerabilities
- Excellent target for privilege escalation

**Mach Port Confusion:**
- Exploit Mach IPC message handling
- Confuse kernel about message contents
- Achieve arbitrary kernel memory read/write

#### Example: iOS Exploit Chain
```
1. iMessage zero-click exploit (FORCEDENTRY)
   ↓
2. Code execution in IMTranscoderAgent (sandboxed)
   ↓
3. XPC service exploitation for sandbox escape
   ↓
4. IOKit user client info leak (kernel addresses)
   ↓
5. IOKit driver memory corruption (kernel exploit)
   ↓
6. Kernel code execution
   ↓
7. Disable code signing, install persistence
   ↓
8. Full Pegasus payload deployment
```

### Android Privilege Escalation

#### Unique Challenges
- SELinux mandatory access control
- Verified Boot
- SafetyNet attestation
- Diversity of kernels (vendor-specific)

#### Common Techniques

**Linux Kernel Exploitation:**
```
Android uses Linux kernel
Target vulnerabilities in:
- Device drivers (especially vendor-specific)
- Binder IPC mechanism
- Memory management
- Networking stack
```

**SELinux Policy Bypass:**
- Exploit kernel vulnerabilities to bypass SELinux
- Modify SELinux policy in memory
- Disable SELinux enforcement

**Binder Exploitation:**
- Binder is Android's primary IPC mechanism
- Complex codebase with history of vulnerabilities
- Excellent escalation target

#### Example: Android Exploit Chain
```
1. WhatsApp RCE or network injection
   ↓
2. Code execution in app context (restricted)
   ↓
3. Android system service exploitation (sandbox escape)
   ↓
4. Kernel memory disclosure
   ↓
5. Linux kernel memory corruption
   ↓
6. SELinux bypass
   ↓
7. Root/kernel privileges
   ↓
8. Pegasus payload deployment
```

## Advanced Escalation Techniques

### Heap Spraying

Technique to make exploitation more reliable:

```
1. Allocate many memory objects with controlled data
2. "Spray" heap memory with exploit payload
3. Trigger vulnerability
4. Higher probability of landing in controlled memory
5. Execute payload
```

### Return-Oriented Programming (ROP)

Bypass DEP/W^X protections:

```
1. Cannot execute data as code (DEP prevents this)
2. Instead, chain together existing code snippets ("gadgets")
3. Each gadget ends with RETURN instruction
4. String together to perform desired operations
5. All code comes from legitimate signed binaries
```

### JOP/COP (Jump/Call-Oriented Programming)

Similar to ROP but using jump or call instructions:

```
Use jump or call instructions instead of returns
More flexible than ROP
Can bypass some ROP-specific mitigations
Requires more sophisticated exploit development
```

## Exploit Reliability Techniques

### Information Leaks

Essential for reliable exploitation:

```
Stage 1: Leak user-space addresses (defeat app ASLR)
Stage 2: Leak kernel addresses (defeat kernel ASLR)
Stage 3: Use leaked addresses for precise memory operations
Result: Highly reliable exploitation
```

### Race Condition Exploitation

When timing matters:

```
1. Create race condition window
2. Spray multiple threads
3. Increase probability of winning race
4. Achieve desired memory state
5. Trigger vulnerability
```

## Mitigations and Evasions

### Operating System Mitigations

| Mitigation | Purpose | Pegasus Bypass Method |
|-----------|---------|----------------------|
| ASLR | Randomize memory addresses | Information leak vulnerabilities |
| DEP/W^X | Prevent data execution | ROP/JOP techniques |
| Code Signing | Only run authorized code | Kernel exploit disables checking |
| Sandboxing | Isolate applications | Sandbox escape exploits |
| Kernel Patch Protection | Protect kernel memory | Kernel vulnerability exploitation |
| Pointer Authentication | Validate pointers | PAC bypass vulnerabilities |

### Pegasus Evasion Techniques

**Against Static Analysis:**
- Code obfuscation
- Encryption of exploit code
- Polymorphic shellcode

**Against Dynamic Analysis:**
- Anti-debugging checks
- Emulation detection
- Behavior modification in analysis environments

**Against Crash Detection:**
- Carefully crafted exploits avoid most crashes
- Cleanup after exploitation
- Graceful handling of edge cases

## Vulnerability Acquisition

### Zero-Day Exploits

Pegasus relies heavily on zero-days:

**Sources:**
- In-house exploit development team
- Purchase from vulnerability brokers
- Offensive security research partnerships

**Costs:**
- iOS zero-click chain: $1-5 million
- Android zero-day: $100,000 - $1 million
- Varies by complexity and reliability

### Exploit Lifecycle

```
1. Vulnerability discovered
2. Exploit developed and tested
3. Integrated into Pegasus
4. Deployed against targets
5. Eventually discovered and patched
6. New exploit needed
```

**Average Lifespan:**
- Zero-click exploits: 6-18 months before discovery
- User-interaction exploits: 1-3 years
- Network injection: Varies widely

## Key Takeaways

1. **Multi-Stage Process:** Privilege escalation requires multiple exploits chained together, each bypassing a different security layer.

2. **Information Leaks Critical:** Defeating ASLR through information leaks is essential for reliable exploitation.

3. **Platform Differences:** iOS and Android require different escalation techniques due to architectural differences.

4. **Continuous Arms Race:** As mitigations improve, exploit techniques evolve in response.

5. **Expensive and Complex:** Developing reliable privilege escalation chains requires significant expertise and resources.

6. **Zero-Days Essential:** Modern mobile security requires previously unknown vulnerabilities for successful escalation.

## References

[1] Google Project Zero, "A very deep dive into iOS Exploit chains found in the wild," December 2021.

[2] Citizen Lab, "The Million Dollar Dissident: NSO Group's iPhone Zero-Days," August 2016.

[3] Apple, "iOS Security Guide," 2023.

[4] Google, "Android Security & Privacy 2021 Year in Review," 2022.

[5] Azimuth Security, "The Exploit Development Life Cycle," Black Hat 2018.

[6] Pangu Team, "iOS Kernel Exploitation Archaeology," POC 2020.
