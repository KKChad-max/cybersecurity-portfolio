# AI Prompting Activity: Phishing & Malware Reference Guide

> **Course:** Google Cybersecurity Certificate — Course 8: Put It to Work  
> **Date:** September 2026  
> **Author:** Chadrack Kalongo

---

## Activity Overview

In this activity, I used a generative AI tool (Gemini) and the **TCREI prompting framework** (Task, Context, References, Evaluate, Iterate) to create a reference guide for employees on identifying phishing emails and signs of malware. The goal was to produce a practical, easy-to-understand document that non-technical staff could use daily.

---

## Step 1: Initial Prompt

I started with a very simple prompt, focusing only on the task:

**PROMPT:**

`Write a reference guide on phishing emails and malware.`

**Initial Output (summary):**  
The AI produced a generic list of definitions and tips, but it was too vague, lacked structure, and didn't consider the audience or company context.

---

## Step 2: Evaluation of Initial Output

I reviewed the first draft and identified several shortcomings:

- No specific audience – it could be for technical or non-technical readers.
- No format – paragraphs without bullet points or tables.
- Tone was inconsistent – sometimes formal, sometimes casual.
- No real-world examples.
- No context about the company's tools or reporting procedures.
- No actionable "what to do" section.

This evaluation guided my refinements.

---

## Step 3: Revised and Refined Prompt

I applied the full TCREI framework to create a detailed prompt:


### Phishing & Malware Reference Guide — Prompt

You are a cybersecurity analyst at a mid-sized company. Create a comprehensive but easy‑to‑understand reference guide for all employees (non‑technical audience) on how to identify phishing emails and signs of malware.

**The guide should include:**

- A clear definition of phishing and malware.
- A list of at least 5 common signs of a phishing email (with examples).
- A list of at least 5 common signs that a computer may be infected with malware.
- A "What to do if you suspect an attack" section with clear action steps.
- A table summarizing phishing vs. malware for quick reference.

**Format:**

- Use bullet points for readability.
- Keep the tone professional but approachable — not overly technical.
- Include placeholders for images (e.g., `[Insert screenshot of suspicious email here]`).
- Aim for about 500 words total.

**Context:**

- Our company uses Google Workspace (Gmail, Drive, Docs).
- We have an IT support team that handles reported incidents.
- Employees should forward suspicious emails to `it-security@company.com`.


---

## Step 4: Final Output — The Reference Guide

# Employee Cybersecurity Guide: Spotting Phishing and Malware

Welcome to our cybersecurity quick-reference guide! As part of our team, you are our first line of defense against cyber threats. This guide will help you identify the two most common types of attacks—phishing and malware—and explain exactly what to do if you spot them.

---

## 1. What Are Phishing and Malware?

**Phishing:** A digital con game. Attackers send fraudulent emails or messages disguised as legitimate communications (like an alert from Google Workspace or a text from a "delivery company") to trick you into revealing sensitive information or clicking a malicious link.

**Malware (Malicious Software):** Harmful software designed to secretly install itself on your computer or phone. Once installed, it can steal company data, spy on your activity, or lock you out of your files until a ransom is paid.

---

## 2. Five Common Signs of a Phishing Email

Cybercriminals are getting smarter, but they usually leave clues. Watch out for these red flags in your Gmail inbox:

- **A False Sense of Urgency or Threats:** Messages that demand immediate action to avoid negative consequences.  
  *Example:* "Action Required: Your Google Workspace account will be deactivated in 2 hours if you do not verify your password."

- **Suspicious Sender Addresses:** The sender's name might look real, but the actual email address is slightly off.  
  *Example:* The display name says "IT Support," but the email address is `admin-update@company-support.com` instead of an internal `@company.com` address.  
  `[Insert screenshot of a mismatched email address in Gmail here]`

- **Unexpected Links or Attachments:** Be highly suspicious of unprompted links or unexpected Google Drive sharing notifications from people you don't know (or even from colleagues if the context is weird).  
  *Example:* An email with a PDF attached titled `Q3_Bonus_Payout_List.pdf`.

- **Generic Greetings and Sign-offs:** Scammers often blast thousands of emails at once and don't know your name.  
  *Example:* "Dear Valued Employee" or "Dear Customer."

- **Requests for Sensitive Information:** We will never ask you for your password over email. Legitimate companies won't either.  
  *Example:* An email directing you to a login page to "update your billing information."

---

## 3. Spotting Phishing on Mobile Devices

Mobile devices present unique challenges because smaller screens make it harder to spot fake URLs or sender details. Watch out for:

- **Smishing (SMS Phishing):** Urgent text messages claiming you have a missed package delivery, a locked bank account, or a mandatory security update.

- **Hidden URLs:** On a phone, you can't just "hover" over a link. **Tip:** Press and hold a link (without tapping to open it) to see a preview of the actual web address before you decide to visit it.

- **Fake App Notifications:** Pop-ups or text messages that look like system alerts telling you to download a "security patch." Always update apps directly through your device's official app store.  
  `[Insert screenshot of a fake package delivery text message here]`

---

## 4. Five Signs Your Computer May Be Infected with Malware

If you accidentally click a bad link, malware might install itself in the background. Look out for these warning signs:

- **Sudden Sluggishness:** Your computer, browser, or Google Workspace apps are running incredibly slow or freezing frequently.

- **Unexpected Pop-ups:** You see strange error messages, warnings, or advertisements popping up on your screen, even when you aren't browsing the web.

- **Browser Redirects:** When you try to search for something, your web browser takes you to a completely different, strange-looking website.

- **Disabled Security Tools:** Your antivirus software is suddenly turned off, and you cannot turn it back on.

- **Unusual Account Activity:** Friends or colleagues tell you they are receiving strange emails or shared Google Docs from your account that you never sent.  
  `[Insert screenshot of an unexpected system pop-up here]`

---

## 5. What to Do If You Suspect an Attack

If something feels off, trust your gut. Take these exact steps to protect yourself and the company:

1. **Do Not Click:** Never click links, download attachments, or reply to a suspicious email or text.

2. **Report the Email:** Forward the suspicious email directly to our IT support team at `it-security@company.com`.

3. **Use the Gmail Tool:** After forwarding, use the native Gmail feature by clicking the three dots in the top right corner of the email and selecting **"Report phishing."**

4. **Disconnect and Call (For Malware):** If you suspect your computer is already infected (e.g., you clicked a link and strange things are happening), disconnect from the Wi-Fi immediately and call the IT helpdesk from your phone. Do not turn the computer off unless instructed by IT.

---

## 6. Quick Reference: Phishing vs. Malware

| Feature | Phishing | Malware |
|---------|----------|---------|
| **What is it?** | A fake message designed to trick you. | Harmful software that infects your device. |
| **How does it arrive?** | Email, text messages, or direct messages. | Hidden in email attachments, malicious links, or infected websites. |
| **Primary Goal** | To steal your passwords, data, or money. | To damage your system, steal files, or hold your computer hostage. |
| **Your Defense** | Skepticism, verifying senders, and reporting to IT. | Not clicking suspicious links and keeping your system updated. |

---

## Step 5: Iterative Improvements

After reviewing the final output, I considered further iterations:

- Could add a printable checklist for desks.
- Could include mobile-specific phishing signs.
- Could add accessibility features (larger font, plain language).

However, the current version already met the core goals: it is comprehensive, audience-appropriate, actionable, and well-structured.

---
## Reflection Question

### What do you think?

The final guide is practical and ready to share. It balances technical accuracy with plain language, includes clear examples, and gives employees a straightforward action plan. It demonstrates how generative AI can accelerate content creation when guided by a thoughtful prompt.


### How did evaluating and iterating affect the final output? Write 1-2 sentences.

Evaluating the initial output revealed that it lacked audience awareness, structure, and practical examples. Iterating by adding context (company tools, audience, format) transformed a generic list into a targeted, user-friendly reference guide that employees can actually use.


### What do you think?

This exercise reinforced the value of structured prompting. By systematically applying the TCREI framework, I turned a vague AI response into a polished, professional document. I am now more confident using generative AI to support my cybersecurity tasks efficiently.

---

## 📁 Portfolio Addition

This activity demonstrates:
- Effective use of generative AI with a proven prompting framework.
- Ability to create security awareness materials for diverse audiences.
- Critical evaluation and iteration skills.
- Documentation of the learning process for professional portfolios.

---

*Written as part of the Google Cybersecurity Certificate — Course 8: Put It to Work*
