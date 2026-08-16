# Cybersecurity Incident Report: Network Traffic Analysis

**Date:** August 14, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 3  

---

## Part 1: Summary of the Problem Found in the tcpdump Log

As part of the DNS protocol, the **UDP protocol** was used to contact the DNS server to retrieve the IP address for the domain name of `yummyrecipesforme.com`. The **ICMP protocol** was used to respond with an error message, indicating issues contacting the DNS server.

The UDP message going from your browser to the DNS server is shown in the first two lines of every log event. The ICMP error response from the DNS server to your browser is displayed in the third and fourth lines of every log event with the error message:

> **"udp port 53 unreachable"**

Since port 53 is associated with DNS protocol traffic, we know this is an issue with the DNS server.

Issues with performing the DNS protocol are further evident because:
- The **plus sign (`+`)** after the query identification number `35084` indicates flags with the UDP message.
- The **"A?"** symbol indicates flags with performing DNS protocol operations (requesting an A record, which maps a domain name to an IP address).

Due to the ICMP error response message about port 53, it is highly likely that the **DNS server is not responding**. This assumption is further supported by the flags associated with the outgoing UDP message and domain name retrieval.

---

## Part 2: Explanation and Analysis of the Data and the Cause of the Incident

### Time Incident Occurred

The incident occurred today at **1:24 p.m.** (13:24:32 in 24‑hour format), based on the tcpdump timestamps.

### How the IT Team Became Aware

Customers notified the organization that they received the message **"destination port unreachable"** when they attempted to visit the website `yummyrecipesforme.com`.

### Current Status

The cybersecurity team providing IT services to their client organization is currently investigating the issue so customers can access the website again.

### Actions Taken to Investigate

In our investigation into the issue, we conducted **packet sniffing tests using `tcpdump`**. In the resulting log file, we found that **DNS port 53 was unreachable**.

### Key Findings

- The local computer (`192.51.100.15`) sent a UDP DNS query to the DNS server (`203.0.113.2`) requesting the IP address for `yummyrecipesforme.com`.
- The DNS server responded with an ICMP error message indicating **"udp port 53 unreachable"**.
- This error was repeated multiple times over a 4‑minute period (13:24:32, 13:26:32, 13:27:15, 13:28:32, 13:28:50), confirming that the issue was persistent.
- Port 53 is the standard port used for DNS services. The error indicates that the DNS server is not listening on port 53 or that UDP traffic to that port is being blocked.

### Next Steps

The next step is to identify whether:
- The **DNS server is down**, or
- **Traffic to port 53 is blocked by the firewall**.

Firewalls offer the ability to block network traffic on specific ports. Port blocking can be used to stop or prevent an attack.

### Likely Cause of the Incident

The DNS server might be down due to:
- A successful **Denial of Service (DoS) attack** that flooded the server with traffic, crashing it or making it unable to respond to legitimate requests, or
- A **misconfiguration** – someone from the team could have made a configuration change on the firewall that blocked port 53.

---

## Lessons Learned & Next Steps

- **Detection:** The incident was detected through customer reports and confirmed using `tcpdump` network analysis.
- **Investigation:** The error logs pointed directly to a DNS resolution failure on port 53.
- **Resolution Plan:** Next steps include checking the DNS server status, reviewing firewall rules, and testing connectivity to port 53 from the local network.

---

> *This report was completed as part of the Google Cybersecurity Certificate – Course 3: Connect and Protect (Networks).*