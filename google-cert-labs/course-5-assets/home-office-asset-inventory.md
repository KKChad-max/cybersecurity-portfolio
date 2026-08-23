# Home Office Asset Inventory

**Date:** August 23, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Scenario

I am operating a small business from my home and need to create an inventory of my network devices. This inventory helps determine which devices contain sensitive information requiring extra protection, and helps me understand the risk landscape of my home office network.

---

## Asset Inventory

| Asset | Network Access | Owner | Location | Sensitivity | Notes / Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Network Router** | Continuous | ISP / Homeowner | On-premises | **Restricted** | Central gateway to the entire network. If compromised, all traffic can be intercepted or redirected. Configuration should be limited to the owner/ISP. |
| **Desktop** | Occasional | Homeowner | On-premises | **Confidential** | Contains sensitive personal and business documents (e.g., invoices, client data, photos). Needs strong password protection and encryption. |
| **Guest Smartphone** | Occasional | Friend | On & Off-premises | **Internal-Only** | Only has access to the guest Wi-Fi (isolated network). Does not contain business data, but its presence on the network needs monitoring. |
| **Work Laptop** | Continuous | Homeowner | On & Off-premises | **Confidential / Restricted** | Contains core business files, access to banking, and customer PII. Taken off-premises (travel), increasing physical risk. Requires disk encryption and a VPN. |
| **Network Attached Storage (NAS) / Backup Drive** | Continuous | Homeowner | On-premises | **Restricted** | Stores local backups of all devices and critical business archives. Loss or ransomware encryption would cause severe business disruption. Must have the highest access controls. |
| **Smart TV / Streaming Device** | Occasional | Homeowner | On-premises | **Public / Internal-Only** | An IoT device that lacks advanced security patches. Although it contains no business data, it can be a weak entry point (pivot point) for attackers if not placed on a separate IoT VLAN. |

---

## Why These Classifications Make Sense

| Sensitivity Level | Definition | Devices |
| :--- | :--- | :--- |
| **Public** | No impact if disclosed | Smart TV / Streaming Device |
| **Internal-Only** | Minor impact if disclosed | Guest Smartphone |
| **Confidential** | Moderate to severe impact if breached | Desktop, Work Laptop |
| **Restricted** | Severe to critical impact if breached | Network Router, NAS / Backup Drive |

---

## Reflection

This activity highlights the importance of asset management in cybersecurity. By identifying and classifying each device connected to my home office network, I can prioritize security controls where they matter most:

- **Restricted devices** (Router, NAS) require the highest level of protection – strong passwords, firmware updates, and limited access.
- **Confidential devices** (Desktop, Work Laptop) need encryption, endpoint protection, and secure backup.
- **Internal-Only and Public devices** (Guest Smartphone, Smart TV) still need monitoring, as they can be used as entry points for attackers seeking to pivot to more sensitive assets.

Regularly updating this inventory and reviewing access controls is essential for maintaining a strong security posture as the business grows.

---

## Next Steps

- Implement **network segmentation** (VLANs) to isolate IoT devices from business systems.
- Enable **full-disk encryption** on the Work Laptop and Desktop.
- Enforce **strong, unique passwords** and **MFA** for all administrative accounts.
- Maintain a **backup schedule** for the NAS and Desktop to ensure business continuity.