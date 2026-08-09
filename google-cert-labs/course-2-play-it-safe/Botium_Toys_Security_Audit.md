# Botium Toys: Internal Security Audit

**Company:** Botium Toys  
**Industry:** Toy Retail (E-commerce & Physical Storefront)  
**Audit Date:** August 2026  
**Auditor:** C.K. Kabinda  

---

## 📋 Scope & Goals

**Scope:** The entire security program at Botium Toys, including employee equipment, internal network, systems, and data assets.

**Goals:** Assess existing assets, evaluate controls, and complete the controls/compliance checklist to identify gaps and improve security posture.

---

## ⚙️ Controls Assessment Checklist

*Does Botium Toys currently have this control in place?*

| Yes | No | Control |
| :---: | :---: | :--- |
|   | ✅ | Least Privilege |
|   | ✅ | Disaster recovery plans |
|   | ✅ | Password policies *(Exists but nominal/weak)* |
|   | ✅ | Separation of duties |
| ✅ |   | Firewall |
|   | ✅ | Intrusion detection system (IDS) |
|   | ✅ | Backups |
| ✅ |   | Antivirus software |
|   | ✅ | Manual monitoring, maintenance, and intervention for legacy systems *(No regular schedule)* |
|   | ✅ | Encryption |
|   | ✅ | Password management system |
| ✅ |   | Locks (offices, storefront, warehouse) |
| ✅ |   | Closed-circuit television (CCTV) surveillance |
| ✅ |   | Fire detection/prevention (fire alarm, sprinkler systems) |

---

## 📜 Compliance Checklist

### Payment Card Industry Data Security Standard (PCI DSS)

| Yes | No | Best Practice |
| :---: | :---: | :--- |
|   | ✅ | Only authorized users have access to customers’ credit card information. |
|   | ✅ | Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment. |
|   | ✅ | Implement data encryption procedures to secure credit card transaction touchpoints and data. |
|   | ✅ | Adopt secure password management policies. |

---

### General Data Protection Regulation (GDPR)

| Yes | No | Best Practice |
| :---: | :---: | :--- |
|   | ✅ | E.U. customers’ data is kept private/secured. |
| ✅ |   | There is a plan in place to notify E.U. customers within 72 hours if their data is compromised. |
|   | ✅ | Ensure data is properly classified and inventoried. |
| ✅ |   | Enforce privacy policies, procedures, and processes to properly document and maintain data. |

---

### System and Organizations Controls (SOC type 1, SOC type 2)

| Yes | No | Best Practice |
| :---: | :---: | :--- |
|   | ✅ | User access policies are established. |
|   | ✅ | Sensitive data (PII/SPII) is confidential/private. |
| ✅ |   | Data integrity ensures data is consistent, complete, accurate, and validated. |
| ✅ |   | Data is available to individuals authorized to access it. |

---

## 📊 Risk Assessment Summary

- **Risk Score:** 8/10 (High)
- **Key Risks:**
  - Lack of encryption for sensitive customer data (credit cards, PII/SPII).
  - All employees have access to cardholder data (no least privilege/separation of duties).
  - No disaster recovery plans or backups.
  - Inadequate password policy and no centralized password management.
  - No Intrusion Detection System (IDS) in place.
  - Legacy systems lack a regular maintenance schedule.

---

## 🛠️ Recommendations

### Priority 1 (Immediate – High Risk)

- [ ] **Implement Encryption:** Encrypt all customers’ credit card data at rest and in transit to comply with PCI DSS and protect against data breaches.
- [ ] **Implement Least Privilege & Separation of Duties:** Restrict employee access to cardholder data and PII/SPII to only those who need it for their specific roles.
- [ ] **Implement a Password Management System:** Enforce a strong password policy (complexity, length, rotation) and deploy a centralized password manager to eliminate password sprawl.

### Priority 2 (Short-Term – Medium Risk)

- [ ] **Install an Intrusion Detection System (IDS):** Add a critical "Detect" layer to identify potential threats in real-time.
- [ ] **Deploy a Backup Solution & Disaster Recovery Plan:** Establish regular automated backups and a documented DR plan to ensure business continuity.
- [ ] **Formalize Legacy System Schedule:** Create a clear, regular maintenance schedule for legacy systems to reduce vulnerabilities.

### Priority 3 (Long-Term – Foundational)

- [ ] **Complete Asset Inventory & Classification:** Finish identifying and classifying all assets (NIST CSF Identify function).
- [ ] **Conduct Regular Security Awareness Training:** Train employees on security best practices, especially around phishing and data handling.

---

## ✅ Summary

Botium Toys currently has several critical controls missing, placing the organization at high risk of data breaches, compliance fines, and business disruption. Immediate action should focus on:

1. **Encryption**
2. **Access controls (Least Privilege, Separation of Duties)**
3. **Backup & Disaster Recovery**

Addressing these gaps will significantly improve Botium Toys' security posture and reduce the risk of non-compliance with PCI DSS, GDPR, and SOC standards.

---

> *This audit was conducted as part of the Google Cybersecurity Certificate program and is included in my professional portfolio.*