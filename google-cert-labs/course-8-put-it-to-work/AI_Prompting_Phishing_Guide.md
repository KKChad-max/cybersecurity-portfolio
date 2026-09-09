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
Write a reference guide on phishing emails and malware.

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

Here is the complete guide generated after the refined prompt:

---

### 📧 Phishing & Malware Reference Guide

#### What is Phishing?
Phishing is a type of cyberattack where attackers send fraudulent messages (usually via email) that appear to come from a trusted source. The goal is to trick you into:
- Revealing sensitive information (passwords, credit card numbers).
- Clicking malicious links.
- Downloading infected attachments.

#### Common Signs of a Phishing Email

| Sign | Example |
|------|---------|
| Urgent or threatening language | "Your account will be suspended in 24 hours. Click here to verify." |
| Suspicious sender address | `support@arnazon.com` (instead of `support@amazon.com`) |
| Generic greetings | "Dear Customer" or "Hello User" instead of your full name. |
| Unexpected attachments | An invoice you weren't expecting, especially `.exe`, `.zip`, `.html`. |
| Spelling and grammar errors | "We are writing too inform you of a urgent secuirity update." |
| Requests for personal information | "Please reply with your password to verify your identity." |
| Mismatched URLs | Hover over the link — it says `https://g00gle.com` instead of `https://google.com`. |

#### Common Signs of a Malware Infection

| Sign | What to look for |
|------|------------------|
| Slow performance | Computer takes much longer to start up or open programs. |
| Unexpected pop-ups | Ads or warning windows appear even when you're not browsing. |
| Files being modified or deleted | Documents become corrupted or disappear. |
| Browser homepage changes | Your homepage is changed to an unfamiliar site without your permission. |
| Unauthorized emails sent | Coworkers receive emails from you that you didn't send. |
| Security software disabled | Your antivirus is turned off and you can't re-enable it. |

#### What to Do If You Suspect an Attack

| Step | Action |
|------|--------|
| 1 | **Do not click any links or download any attachments.** |
| 2 | **Report it immediately:** Forward the suspicious email to `it-security@company.com`. |
| 3 | **If you clicked something:** Disconnect from the network (turn off Wi-Fi or unplug Ethernet). |
| 4 | **Contact IT Support:** Call or submit a ticket to let them know. |
| 5 | **Change your password** if you entered it on a suspicious site. |

#### Quick Reference: Phishing vs. Malware

| | Phishing | Malware |
|------|----------|---------|
| **What is it?** | Deceptive messages trying to steal info. | Malicious software that infects your device. |
| **How does it get in?** | Email, text, or phone call. | Downloads, attachments, or malicious links. |
| **What's the goal?** | Steal credentials or financial info. | Steal data, encrypt files, or take control. |
| **What do I do?** | Report the email. Don't click anything. | Contact IT. Scan with antivirus. |

#### Final Tips
- **When in doubt, throw it out.** If an email seems suspicious, don't interact with it.
- **Verify before trusting.** Check with the sender via a different communication channel (e.g., call them).
- **Keep software updated.** Regular updates patch known vulnerabilities.
- **Use multi-factor authentication (MFA).** Even if your password is stolen, MFA adds an extra layer of protection.

[Insert screenshot of a suspicious email example here]

#### Need Help?
If you're unsure whether an email is legitimate, contact IT Security at `it-security@company.com` or call the help desk at [Insert phone number].

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
