# Data Leak Worksheet: Least Privilege & NIST SP 800-53

**Date:** August 24, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Incident Summary

A sales manager shared access to a folder of internal-only documents with their team during a meeting. The folder contained files associated with a new product that has not been publicly announced, including customer analytics and promotional materials. After the meeting, the manager did not revoke access to the internal folder, but warned the team to wait for approval before sharing the promotional materials with others.

During a video call with a business partner, a member of the sales team forgot the warning from their manager. The sales representative intended to share a link to the promotional materials so that the business partner could circulate the materials to their customers. However, the sales representative accidentally shared a link to the internal folder instead. Later, the business partner posted the link on their company's social media page assuming that it was the promotional materials.

---

## Data Leak Worksheet

| Section | Response |
| :--- | :--- |
| **Issue(s)** | The data leak was caused by a combination of excessive access privileges (the internal folder remained accessible to the sales team after the meeting) and human error (the representative accidentally shared the wrong link). The principle of least privilege was violated because the team retained access to the entire folder beyond the meeting, and there was no restriction on external sharing. |
| **Review** | NIST SP 800-53 AC-6 (Least Privilege) ensures that users are only granted the minimal access necessary to perform their job functions. It discusses enforcing processes, user accounts, and roles to prevent users from operating at privilege levels higher than required to accomplish business objectives. |
| **Recommendation(s)** | 1. **Automatically revoke access** to sensitive folders after a set period (e.g., 24 hours after the meeting) or at the conclusion of the relevant project. <br><br> 2. **Implement role‑based access controls** that restrict sharing of internal‑only links to authorized personnel (e.g., managers) and enforce separate, time‑limited links for external partners. <br><br> 3. **Conduct regular audits** of user privileges and shared folder permissions to identify and remove unnecessary access. |
| **Justification** | Automating revocation and restricting role‑based sharing would have prevented the sales team from having long‑term access to the internal folder and stopped the accidental external sharing of the wrong link. These improvements directly address the root causes – excessive privileges and human error – by adding technical controls that reduce reliance on manual warnings and individual discretion. |

---

## Reflection

This incident highlights the importance of **least privilege** and **access control automation** in protecting sensitive information. The manager's failure to revoke access after the meeting, combined with a representative's accidental link sharing, led to a publicly exposed internal document leak.

Implementing NIST SP 800-53 AC-6 enhancements – such as automatic revocation, role‑based sharing, and regular audits – would create a defense‑in‑depth approach that reduces human error and ensures that access is granted only for as long as it is needed.

---

## Next Steps

- **Short‑term (7–14 days):** Implement automatic expiration for shared folders and enforce role‑based sharing policies.
- **Medium‑term (30–60 days):** Deploy a data loss prevention (DLP) tool to detect and block external sharing of internal‑only links.
- **Long‑term (3–6 months):** Conduct regular user privilege audits and provide security awareness training on safe data sharing practices.