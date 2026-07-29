# Home Lab Setup (VirtualBox + Ubuntu)

## Environment
- **Host OS:** Windows 10
- **Hypervisor:** Oracle VirtualBox 7.2.x
- **Guest OS:** Ubuntu 26.04 LTS (Latest LTS)

## VM Specifications
- **RAM:** 4096 MB (4 GB)
- **CPU:** 2 cores
- **Storage:** 25 GB (dynamically allocated)
- **Network:** NAT (default)
- **Guest Additions:** Installed & Shared Clipboard (Bidirectional) enabled

## Setup Process
1. Downloaded Ubuntu LTS ISO (~5GB).
2. Installed VirtualBox and the Extension Pack.
3. Created the VM with the specs above.
4. Installed Ubuntu (selected "Erase disk" on the virtual drive).
5. Installed Guest Additions to enable full-screen mode and shared clipboard.
6. Enabled Bidirectional Clipboard in Devices > Shared Clipboard.

## Post-Installation Checks
- [x] Internet connectivity confirmed (`ping -c 4 google.com`)
- [x] System updated (`sudo apt update && sudo apt upgrade`)
- [x] Guest Additions installed and auto-resize working
- [x] Shared clipboard (copy/paste) working between host and guest

## Next Steps for this Lab
- [ ] Install Kali Linux (for offensive security testing)
- [ ] Install vulnerable VMs (like Metasploitable 2)
- [ ] Set up a NAT network for internal VM communication