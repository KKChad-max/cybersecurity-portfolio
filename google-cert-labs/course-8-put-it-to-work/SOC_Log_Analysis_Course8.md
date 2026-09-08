# 🕵️ SOC Log Analysis — Incident Prioritization

> **Course:** Google Cybersecurity Certificate — Course 8: Put It to Work  
> **Date:** September 2026  
> **Tool:** Gemini Notebook (AI-powered log analysis)

---

## 📋 Scenario

As a junior security analyst, I reviewed a system activity log to identify potential threats or policy violations. I used **Gemini Notebook** to help sift through the data and find anomalies.

---

## 📊 Log Data (Simplified)

| TIMESTAMP | USER | SOURCE_IP | EVENT_TYPE | DETAILS |
|:---|:---|:---|:---|:---|
| 2025-07-30 08:00:15 | admin | 192.168.1.1 | Login_Success | Internal network login |
| 2025-07-30 08:05:30 | John.Doe | 192.168.1.5 | File_Access | Opened report_draft.docx |
| 2025-07-30 08:10:45 | jane.smith | 192.168.1.10 | Email_Sent | Internal company email |
| 2025-07-30 08:15:05 | guest | 10.0.0.100 | Login_Failed | Attempt 1 |
| 2025-07-30 08:15:10 | guest | 10.0.0.100 | Login_Failed | Attempt 2 |
| 2025-07-30 08:20:20 | John.Doe | 192.168.1.5 | File_Access | **Copied /finance/budget_2026_final.xlsx to /public_share** |
| 2025-07-30 08:25:35 | system | N/A | Service_Status | Apache running |
| 2025-07-30 08:30:40 | admin | 203.0.113.25 | Login_Success | **External IP (unusual location)** |
| 2025-07-30 08:35:50 | mary.jones | 192.168.1.12 | File_Deletion | Deleted vacation_photos.jpg |
| 2025-07-30 08:40:05 | system | N/A | Software_Update | Antivirus update |

---

## 🔍 Analysis & Findings

### 1. Most Suspicious Event (Requires Immediate Escalation)

**Event:** `John.Doe` copied `/finance/budget_2026_final.xlsx` to `/public_share`.

**Why?**
- A sensitive financial document was moved to a publicly accessible location.
- This is a confirmed data exfiltration attempt — not just a failed attempt.
- It represents a potential insider threat or compromised user account.

### 2. Combined Events Indicating Account Compromise

**Pair:** Admin login from `203.0.113.25` (external IP) + John.Doe file copy.

**Why?**
- Admin account logging in from an unusual external location suggests possible credential theft.
- Combined with John.Doe exfiltrating sensitive data, this could indicate:
  - An attacker using compromised admin credentials to cover their tracks.
  - A malicious insider copying data while admin access is being abused.

### 3. Failed Login Attempts

**User:** `guest` | **IP:** `10.0.0.100`

Three consecutive failed login attempts in rapid succession indicate a brute-force or password-spraying attempt against a low-privilege account.

---

## 🛠️ Tools Used

- **Gemini Notebook** — AI assistant for pattern identification and log interrogation.
- **Manual log review** — cross-referencing timestamps and user activity.

---

## ✅ Key Takeaways

| Priority | Rule |
|:---|:---|
| **Critical** | External admin logins → escalate immediately. |
| **High** | Sensitive files moved to public locations → investigate for data theft. |
| **Medium** | Multiple failed logins → block IP and monitor. |

---

## 📚 Reflection

This exercise taught me to:
- Distinguish between *attempts* (failed logins) and *successful actions* (data transfers).
- Combine seemingly separate events to uncover a larger attack pattern.
- Use AI tools as a force multiplier, not a replacement for human judgment.

---

*Written as part of the Google Cybersecurity Certificate — Course 8.*