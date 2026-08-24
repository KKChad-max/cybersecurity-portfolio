# Parking Lot USB Exercise

**Date:** August 24, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Scenario

I arrived at Rhetorical Hospital and found a USB stick with the hospital's logo printed on it in the parking lot. I used a virtualized workstation to safely inspect its contents without risking infection to the hospital's network. The USB appeared to belong to Jorge Bailey, the Human Resource Manager.

---

## Contents

The USB drive contained a mix of personal and work‑related files. Personal files included folders labeled "Family photos," "Our dog pics," and "Vacation ideas," while work files included "New hire letter," "Shift schedules," "Employee budget," and "JBL_Resume." This combination of personal and professional data creates a significant risk, as it exposes personally identifiable information (PII) such as employee names, schedules, and potentially salary details.

---

## Attacker Mindset

An attacker could use this information to impersonate Jorge or other employees, craft convincing phishing emails, or social engineer their way into the hospital's systems. The shift schedules and employee details could also be used to coordinate a physical intrusion or to blackmail individuals. Additionally, the resume and personal photos could be used to build a detailed profile of Jorge for more targeted attacks.

---

## Risk Analysis

To mitigate USB bashing attacks, organizations should implement the following controls:

- **Technical controls:** Disable Autorun on all workstations to prevent malicious code from executing automatically when a USB is inserted. Install and maintain updated antivirus and anti‑malware software on all systems.
- **Operational controls:** Establish a clear policy that prohibits employees from plugging unknown USB drives into company computers. Provide secure alternatives for file sharing (e.g., encrypted email, company‑approved cloud storage).
- **Managerial controls:** Conduct regular security awareness training on the risks of USB bashing and social engineering. Implement encryption and password protection for all corporate USB drives, and enforce a strict separation between personal and business USB drives.

By combining these controls, organizations can significantly reduce the risk of USB bashing attacks and protect sensitive data from exposure.

---

## Reflection

This exercise highlighted the importance of physical security awareness and the risks associated with removable media. Even without malicious code, the USB drive contained enough sensitive information to launch a variety of attacks against Jorge or Rhetorical Hospital. Best practices such as never plugging in unknown devices, keeping personal and work drives separate, and using encryption are essential safeguards in any security program.

---

## Tools Used

| Tool / Concept | Purpose |
| :--- | :--- |
| **Virtualization software** | Safely inspect unknown USB drives without risking network infection |
| **USB bashing awareness** | Recognize and mitigate the risk of strategically placed malicious USB drives |
| **Access controls** | Enforce policies for handling removable media |
| **Security awareness training** | Educate employees on the risks of USB bashing and social engineering |
| **Encryption** | Protect data on USB drives in case of loss or theft |