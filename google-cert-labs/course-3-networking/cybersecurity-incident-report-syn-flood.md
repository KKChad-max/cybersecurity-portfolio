# Cybersecurity Incident Report: Network Attack Analysis

**Date:** August 15, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 3  

---

## Section 1: Identify the type of attack that may have caused this network interruption

**One potential explanation for the website’s connection timeout error message is:**

A Denial of Service (DoS) attack.

**The logs show that:**

The logs show a high volume of TCP SYN requests originating from a single unfamiliar IP address (`203.0.113.0`) directed at the company's web server (`192.0.2.1`). The web server attempts to respond with SYN-ACK packets but becomes overwhelmed by the volume of incoming requests. As the attack continues, the server is unable to complete the three‑way handshake for legitimate visitors, and some legitimate connection attempts receive a `RST` packet or a `504 Gateway Time-out` error.

**This event could be:**

A type of DoS attack called a **SYN flood attack**, where a malicious actor sends a flood of SYN packets to exhaust the server's resources.

---

## Section 2: Explain how the attack is causing the website to malfunction

**When website visitors try to establish a connection with the web server, a three‑way handshake occurs using the TCP protocol. The three steps of the handshake are:**

1. **SYN:** The client sends a SYN (synchronize) packet to the server, requesting to establish a connection.  
2. **SYN-ACK:** The server replies with a SYN-ACK (synchronize-acknowledge) packet, accepting the request and reserving system resources for the connection.  
3. **ACK:** The client sends a final ACK (acknowledge) packet to confirm the connection, completing the handshake.

**Explain what happens when a malicious actor sends a large number of SYN packets all at once:**

When a malicious actor sends an overwhelming number of SYN packets to the server, the server's available resources are consumed by the incomplete half‑open connections. The server reserves memory and processing power for each SYN request, waiting for the final ACK that never arrives. As the number of half‑open connections exceeds the server's capacity, the server becomes unable to accept or process new legitimate connection requests.

**Explain what the logs indicate and how that affects the server:**

The Wireshark log shows repeated SYN packets from the attacker's IP address (`203.0.113.0`) directed at the web server on port 443. Initially, the server responds to the attacker's SYN requests with SYN-ACK packets (log items 52–54). However, the attacker continues sending SYN requests at a high frequency, which is abnormal network behavior.

As the attack progresses:
- Legitimate visitors (e.g., `198.51.100.14`, `198.51.100.5`) are still able to connect in the early stage of the attack.
- Over time, the server becomes overloaded. Legitimate connection attempts are met with `RST` packets (log item 73) or `HTTP 504 Gateway Time-out` responses (log item 77), indicating that the server can no longer process legitimate requests.
- The repeated SYN requests from `203.0.113.0` continue uninterrupted, confirming that the server is under a sustained SYN flood attack.

**Result:** The server is unable to establish new connections with legitimate users, causing the website to load slowly or return a connection timeout error for customers and employees alike.

---

## Summary of Actions Taken

- **Detection:** The incident was detected through an automated monitoring system alert and confirmed by analyzing the web server's response times.
- **Investigation:** A packet sniffer (Wireshark/tcpdump) was used to capture network traffic, revealing a high volume of TCP SYN requests from a suspicious IP address.
- **Containment:** The web server was taken offline temporarily to allow it to recover. The suspicious IP address was blocked at the firewall.
- **Next Steps:** Continue monitoring for new attack vectors (as the attacker may spoof IPs) and consider implementing rate limiting or SYN cookies to mitigate future SYN flood attacks.

---

> *This report was completed as part of the Google Cybersecurity Certificate – Course 3: Connect and Protect (Networks).*