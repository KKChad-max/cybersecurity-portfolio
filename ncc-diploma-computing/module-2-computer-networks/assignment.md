# Computer Networks Assignment: TechSolutions Inc. Network Design

**Module:** Computer Networks  
**Institution:** ZCAS University  
**Programme:** NCC Level 4 Diploma in Computing  
**Year:** 2025  

---

## Overview

This assignment involved the design of a scalable and secure network infrastructure for **TechSolutions Inc.** , a technology company with 150 employees across three floors. The design accommodates future growth to 300 employees and includes network topology, equipment selection, IP addressing, security, and management strategies.

---

## Task 1: Project Requirements Analysis

### a) Key Requirements

| Category | Details |
| :--- | :--- |
| **Employee Count** | 150 current, 300 future (3–5 years) |
| **Device Types** | 150 laptops/desktops, 50+ smartphones/tablets, 10+ servers, 15 IP cameras, 30 VoIP phones, 4 high-speed printers |
| **Specialised Hardware** | GPU clusters for AI/ML, NAS for code repositories |
| **Department-Specific Needs** | Software Development (60 employees): high bandwidth for Git, low-latency to VM clusters, dedicated VLAN for testing. <br><br> Finance/HR (20 employees): isolated network segment for compliance (GDPR/HIPAA), encrypted file transfers. <br><br> Management (15 employees): QoS for video conferencing, secure VPN for remote work. <br><br> IT Support (10 employees): administrative access, network monitoring tools. |
| **Remote Work** | 50+ remote employees needing secure VPN access, bandwidth for RDP and cloud services. |

---

### b) Scalability & Network Traffic Analysis

| Factor | Detail |
| :--- | :--- |
| **Growth Projections** | Headcount: 150 → 300 employees (4 years). <br> Devices: 250 → 500+ endpoints. <br> Bandwidth: 1 Gbps → 10 Gbps backbone. |
| **High-Bandwidth Applications** | Video Conferencing: 4 Mbps/user – QoS tagging required. <br> Code Repository: 1 Gbps peak – 10 Gbps uplinks to server room. <br> VoIP: 100 Kbps/call – PoE switches with LLDP-MED for QoS. <br> Virtualization: 5 Gbps/cluster – spine-leaf architecture for east-west traffic. |
| **Traffic Patterns** | East-West Traffic: 70% (server-to-server, VM migrations). <br> North-South Traffic: 30% (user-to-internet, cloud services). |
| **Design Impact** | Core Layer: 40 Gbps spine switches. <br> Wireless: Wi-Fi 6E (6 GHz band). <br> Redundancy: Dual ISP links (primary fibre, backup 5G). |

---

## Task 2: Network Topology Design

### a) Floor Plan Layout

| Floor | Description |
| :--- | :--- |
| **Floor 1 (Open Workspace)** | 75 developer workstations, 10 IP cameras, 5 network printers. <br> Access Layer: 3x Cisco Catalyst 9200L-48P-4G switches (48-port PoE+). <br> AP Placement: 15x Cisco Catalyst 9136AX (Wi-Fi 6E), spaced 15m apart. |
| **Floor 2 (Server Room & Core)** | Core Layer: 2x Cisco Nexus 9504 switches (40 Gbps spine). <br> Distribution Layer: 4x Cisco Catalyst 9300 switches (10 Gbps uplinks). <br> Server Racks: 2x Dell PowerEdge R750 (VM hosts), 1x QNAP TS-h2490FU (NAS). <br> Cooling: Redundant HVAC systems. |
| **Floor 3 (Management & Conference Rooms)** | 15x Cisco IP Phone 8865 (VoIP), 4x Cisco Webex Room Kits (4K video conferencing). <br> AP Placement: 8x ceiling-mounted APs with directional antennas. |
| **Common Areas** | 4x Cisco APs in mesh mode for BYOD coverage. |

---

### b) Logical Network Topology

```text
+-------------------+
|   Internet (ISP)  |
|  (Primary + Backup)|
+-------------------+
          |
          | (Dual WAN links)
          v
+-------------------+
|   Firewall Pair   |
| (Palo Alto PA-3260|
|   Active/Passive) |
+-------------------+
          |
          | (10 Gbps)
          v
+-------------------+
|   Core Switches   |
| (Cisco Nexus 9504)|
|   Redundant Pair  |
+-------------------+
          |
 +--------+--------+
 |                 |
 | (40 Gbps fiber) |
 v                 v
+-----------+     +-----------+
|Distrib SW |     |Distrib SW |
|(Cisco 9300|     |(Cisco 9300|
|  Stack)   |     |  Stack)   |
+-----------+     +-----------+
     |                   |
 +---+---+           +---+---+
 |       |           |       |
 v       v           v       v
+---+   +---+       +---+   +---+
|F1 |   |F1 |       |F3 |   |F3 |
|SW |   |SW |       |SW |   |SW |
+---+   +---+       +---+   +---+
 |       |           |       |
 v       v           v       v
APs     APs         APs     APs
(Dev)   (Guest)     (VoIP)  (Mgmt)

```

---

## Key Design Features

- **Hierarchical Design:** Core, Distribution, Access layers.
- **Core Layer:** Cisco Nexus 9504 with VXLAN and OSPF routing.
- **Distribution Layer:** Cisco Catalyst 9300 stacked (80 Gbps throughput), inter-VLAN routing with HSRP.
- **Access Layer:** Cisco Catalyst 9200 (PoE+ for APs/IP cameras), port security.
- **VLAN Segmentation:**
  - VLAN 10 (Development): `10.0.1.0/24`
  - VLAN 20 (Finance/HR): `10.0.2.0/26`
  - VLAN 30 (VoIP): `10.0.3.0/27`
  - VLAN 40 (Guest): `10.0.4.0/28`

---

## Task 3: Equipment Selection & Specification

### a) Equipment List

| Device | Model | Quantity | Specifications |
| :--- | :--- | :--- | :--- |
| **Core Switch** | Cisco Nexus 9504 | 2 | 40 Gbps, VXLAN, 576 GB buffer |
| **Access Switch** | Cisco Catalyst 9200L | 10 | 48-port PoE+, 4x 10 Gbps uplinks |
| **Wireless AP** | Cisco Catalyst 9136AX | 30 | Wi-Fi 6E, 8x8 MU-MIMO, OFDMA |
| **Router** | Cisco ISR 4431 | 1 | SD-WAN, dual 1 Gbps WAN, VPN support |
| **Firewall** | Palo Alto PA-3260 | 2 | 20 Gbps throughput, threat prevention |
| **Cabling** | Cat6a | – | 10 Gbps up to 100m, shielded for EMI |

---

### b) Justification

| Device | Justification |
| :--- | :--- |
| **Cisco Nexus 9504** | Scalability (576x 40 Gbps ports), N+1 power supplies, hot-swappable fans. |
| **Wi-Fi 6E APs** | 6 GHz band reduces interference; OFDMA improves throughput in high-density areas. |
| **Palo Alto Firewalls** | Application-ID for granular traffic control; SSL decryption for threat inspection. |

---

## Task 4: IP Addressing & Subnetting

### a) Addressing Plan

- **Primary Network:** `10.0.0.0/16` (65,534 hosts)

### b) Subnet Allocation

| Department | Subnet | Subnet Mask | Hosts | Reserved for Growth |
| :--- | :--- | :--- | :--- | :--- |
| **Development** | `10.0.1.0/24` | `255.255.255.0` | 254 | 254 → 510 (future /23) |
| **Finance/HR** | `10.0.2.0/26` | `255.255.255.192` | 62 | 62 → 126 (future /25) |
| **VoIP** | `10.0.3.0/27` | `255.255.255.224` | 30 | 30 → 62 (future /26) |
| **IT Infrastructure** | `10.0.4.0/28` | `255.255.255.240` | 14 | 14 → 30 (future /27) |
| **Guest Network** | `10.0.5.0/28` | `255.255.255.240` | 14 | Isolated VLAN |

**Subnetting Strategy:** VLSM (Variable-Length Subnet Masking) optimises IP space for departments with smaller needs. Private IP range (`10.0.0.0/8`) offers flexibility for multi-site expansion.

---

## Task 5: Network Security Design

### a) Threats & Vulnerabilities

| Threat Type | Examples |
| :--- | :--- |
| **External Threats** | DDoS attacks targeting public-facing servers; phishing campaigns. |
| **Internal Threats** | Unauthorised access to finance VLAN; rogue APs compromising Wi-Fi security. |

---

### b) Security Plan

| Control | Implementation |
| :--- | :--- |
| **Network Segmentation** | VLANs isolate departments (ACLs block inter-VLAN traffic by default). DMZ for public servers behind firewalls. |
| **Access Control** | 802.1X Authentication (Cisco ISE for NAC). Role-Based Access (AD/LDAP integration). |
| **Encryption** | WPA3-Enterprise (AES-256 for Wi-Fi). IPsec VPN for remote employees. |
| **Threat Prevention** | Palo Alto WildFire for sandboxing unknown files. Cisco Umbrella for DNS-layer security. |

---

## Task 6: Network Management & Monitoring

### a) Tools & Software

| Tool | Purpose |
| :--- | :--- |
| **Cisco DNA Center** | Automated device provisioning; assurance analytics for Wi-Fi performance. |
| **SolarWinds NPM** | SNMP monitoring of switches/routers; alerts for CPU/RAM thresholds (>80%). |
| **PRTG Network Monitor** | NetFlow analysis for traffic patterns; SLA monitoring for ISP links. |

---

### b) Reliability Strategies

| Strategy | Implementation |
| :--- | :--- |
| **Redundancy** | Dual power supplies in core switches; RAID-10 for NAS storage. |
| **Disaster Recovery** | Daily backups to offsite AWS S3; cold spare switches in IT storage. |

---

## Reflection

This assignment strengthened my understanding of:

- **Network Design:** Hierarchical network architecture with core, distribution, and access layers.
- **Scalability Planning:** Accommodating future growth through modular design and VLSM subnetting.
- **Security Implementation:** Network segmentation, access control, encryption, and threat prevention.
- **Equipment Selection:** Justifying hardware choices based on performance, scalability, and redundancy.
- **Network Management:** Monitoring tools and reliability strategies for business continuity.

---

## How This Connects to Cybersecurity

| Network Concept | Cybersecurity Application |
| :--- | :--- |
| **Network Segmentation (VLANs)** | Limiting lateral movement and isolating sensitive data. |
| **Firewalls & ACLs** | Controlling traffic and preventing unauthorised access. |
| **Encryption (WPA3, IPsec)** | Protecting data in transit from interception. |
| **802.1X Authentication** | Enforcing device-level access control. |
| **DNS Security (Cisco Umbrella)** | Blocking malicious domains and preventing phishing. |
| **Monitoring (SNMP, NetFlow)** | Detecting anomalies and responding to incidents. |

---

## References

**Books:**
- Stallings, W. (2021). *Network Security Essentials: Applications and Standards*. 7th ed. Pearson.

**Standards & Guidelines:**
- NIST. (2020). *Guidelines for Network Segmentation*. SP 800-207.
- IEEE. (2021). *802.11ax-2021 (Wi-Fi 6) Standard*.

**Vendor Documentation:**
- Cisco. (2025). *Catalyst 9200 Series Switches Datasheet*.
- Palo Alto Networks. (2025). *Next-Generation Firewall Best Practices*.

---

> *This assignment was completed as part of the NCC Level 4 Diploma in Computing – Computer Networks module.*