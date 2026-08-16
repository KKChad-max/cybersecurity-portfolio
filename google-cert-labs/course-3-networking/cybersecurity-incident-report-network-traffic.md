# Cybersecurity Incident Report: Network Traffic Analysis

**Date:** August 14, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 3  

---

## Part 1: Summary of the Problem Found in the DNS and ICMP Traffic Log

The UDP protocol reveals that a DNS query was sent from the local computer (IP: `192.51.100.15`) to the DNS server (IP: `203.0.113.2`) requesting the IP address for the domain `yummyrecipesforme.com`.

This is based on the results of the network analysis, which show that the **ICMP echo reply** returned the error message:

> **"udp port 53 unreachable"**

in response to the DNS query.

The port noted in the error message is used for **DNS (Domain Name System)** services.

### Most Likely Issue

The DNS server is not responding to queries on port 53, either because:

- The DNS service is down,
- The server is misconfigured, or
- A firewall is blocking UDP traffic to port 53.

---

## Part 2: Explanation and Analysis of the Data and the Cause of the Incident

### Time Incident Occurred

Between **13:24:32** and **13:28:50** (1:24 PM – 1:28 PM), based on the tcpdump timestamps.

### How the IT Team Became Aware

Several customers reported that they were unable to access the website `yummyrecipesforme.com` and received the error **"destination port unreachable"** when attempting to load the page. The IT team then attempted to load the webpage and received the same error.

### Actions Taken to Investigate

The IT team used the network protocol analyzer tool **tcpdump** to capture and analyze network traffic while attempting to load the webpage again. The tcpdump logs were then reviewed to identify the source of the error.

### Key Findings

- The local computer (`192.51.100.15`) sent a **UDP DNS query** to the DNS server (`203.0.113.2`) requesting the IP address for `yummyrecipesforme.com`.
- The DNS server responded with an **ICMP error message** indicating **"udp port 53 unreachable"**.
- This error was repeated multiple times over a 4‑minute period (13:24:32, 13:26:32, 13:27:15, 13:28:32, 13:28:50), confirming that the issue was persistent.
- Port 53 is the standard port used for DNS services. The error indicates that **the DNS server is not listening on port 53** or that **UDP traffic to that port is being blocked**.

### Likely Cause of the Incident

The DNS server is either:

- **Offline** – the server is down or unreachable,
- **Misconfigured** – the DNS service is not running or is bound to a different port, or
- **Blocked by a firewall rule** – UDP traffic to port 53 is being dropped or rejected.

This prevents the DNS server from resolving domain names to IP addresses, which stops users from accessing the website.

---

## Lessons Learned & Next Steps

- **Detection:** The incident was detected through customer reports and confirmed using `tcpdump` network analysis.
- **Investigation:** The error logs pointed directly to a DNS resolution failure on port 53.
- **Resolution Plan:** Next steps include checking the DNS server status, reviewing firewall rules, and testing connectivity to port 53 from the local network.

---

> *This report was completed as part of the Google Cybersecurity Certificate – Course 3: Connect and Protect (Networks).*