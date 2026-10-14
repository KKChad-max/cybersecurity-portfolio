# LetsDefend Lab Report: More Details About Document File Analysis 2

**Platform:** LetsDefend  
**Date Completed:** October 14, 2026  
**Role:** SOC Analyst / Malware Analyst  
**Difficulty:** Medium  
**MITRE ATT&CK:** T1204.002 (User Execution: Malicious File), T1059.005 (Visual Basic), T1071.001 (Web Protocols)  
**Result:** True Positive / Malware Confirmed (VBA Macro Downloader)  

## 📌 Lab Overview
Conducted static analysis on two malicious documents: a DOCX file with an embedded VBA macro (`PO-465514-180820.docx`) and an XLS file that attempts to download a secondary payload (`Siparis_17.xls`). The objective was to identify macro presence, extract author metadata, determine the download domain, and count the IOCs embedded in the malicious spreadsheet.

## 🛠️ Lab Environment & Tools Used

| Tool | Suite | Purpose in Analysis |
| :--- | :--- | :--- |
| **`oleid.py`** | Oletools | Identified file type, macro presence, and external relationships at a high level. |
| **`olevba.py`** | Oletools | Extracted VBA macro code, identified suspicious keywords, and enumerated IOCs (URLs, executable filenames). |
| **`olemeta.py`** | Oletools | Extracted metadata including author, last saved time, and creating application. |
| **Remnux** | Linux Distro | Pre-configured malware analysis environment for safe static analysis. |

**Installation command:**
```bash
sudo -H pip install -U oletools
```

## 🔍 Investigation Steps & Findings

### 1. Initial Triage with `oleid.py`

Running `oleid.py` on the DOCX file provided a high-level snapshot before diving into the macro code:

```bash
oleid PO-465514-180820.docx
```

**Key findings:**
- **File format:** MS Word 2007+ (DOCX)
- **VBA Macros:** **Yes** (with suspicious keywords)
- **XLM Macros:** No
- **External Relationships:** Yes

This confirmed the file was malicious and used VBA macros rather than the external OLE exploit seen in CVE-2021-40444.

### 2. VBA Macro Extraction with `olevba.py`

Next, I extracted the actual macro code using `olevba.py`:

```bash
olevba PO-465514-180820.docx
```

**Key findings from the extracted macro:**
- **AutoExec Keyword:** `Document_open` — This tells the macro to execute automatically when the document is opened and macros are enabled.
- **Suspicious Functions Identified:**
    - `Create` — Creates a file or a system command.
    - `ExecuteExcel4Macro` — Executes Excel 4.0 macros from VBA (a common evasion technique).
    - `CreateObject` — May create a WScript.Shell object for command execution.
    - `Write` — Writes bytes to a file.
    - `Chr` — Encodes strings to evade static detection.
    - `Print` — May be used to write files.
    - `InputBox` — May prompt the user for input.
- **Strings Detection:** Hex-encoded strings were detected, indicating obfuscation.

### 3. Metadata Extraction with `olemeta.py`

The author and last-saved timestamp of the file were extracted using `olemeta.py`:

```bash
olemeta PO-465514-180820.docx
```

**Properties extracted:**

| Property | Value |
| :--- | :--- |
| **Author** | `Alexandre Riviere` |
| **Last Saved By** | `Normal.dotm` |
| **Create Time** | `2020-08-18 08:19:00` |
| **Last Saved Time** | `2020-08-18 08:19:00` |
| **Creating Application** | `Microsoft Office Word` |

### 4. IOC Extraction from the XLS File with `olevba.py`

The second file, `Siparis_17.xls`, was analyzed for embedded IOCs (URLs and executables):

```bash
olevba Siparis_17.xls | grep http
```

or

```bash
olevba Siparis_17.xls
```

**Key findings:**
- **Malicious URL:** `http://hocoso.mobi/file.jpg`
- **Dropped Executable:** `RegAsm` (a legitimate .NET tool abused by the malware)
- **Total IOCs detected:** **2**

The URL uses a `.jpg` extension to disguise itself as an image, but it is actually an executable that the macro downloads and runs.

## 📊 Lab Questions & Answers

| Question | Answer |
| :--- | :--- |
| **Does the file `PO-465514-180820.docx` contain a VBA macro?** | `Y` |
| **What is the macro keyword that enables this?** | `Document_open` |
| **Who is the author of the file?** | `Alexandre Riviere` |
| **What is the last saved time of the file?** | `2020-08-18 08:19:00` |
| **From which domain is `Siparis_17.xls` trying to download files?** | `hocoso.mobi` |
| **How many IOCs are in `Siparis_17.xls` according to Olevba?** | `2` |

## 📦 Indicators of Compromise (IOCs)

| Type | Value | Source File |
| :--- | :--- | :--- |
| **Malicious URL** | `http://hocoso.mobi/file.jpg` | `Siparis_17.xls` |
| **Dropped Executable** | `RegAsm` | `Siparis_17.xls` |
| **AutoExec Keyword** | `Document_open` | `PO-465514-180820.docx` |
| **Malicious Author** | `Alexandre Riviere` | `PO-465514-180820.docx` |

## 🧠 Key Takeaways & Lessons Learned

1. **`Document_open` is a Red Flag:** Any VBA macro that uses `Document_open` as its AutoExec keyword runs automatically when the document is opened and macros are enabled. This is the most common persistence and execution trigger in malicious Office documents.

2. **Obfuscation is Common in VBA:** The presence of `Chr()` calls and hex-encoded strings indicates the author intentionally obfuscated their code to evade string-based detection. Deobfuscation would be the next step for deeper analysis.

3. **Legitimate Tools are Abused by Attackers:** The malware downloads `RegAsm` (a legitimate .NET Assembly Registration tool) as part of its attack chain. This is a form of "Living off the Land" (LotL) — using trusted binaries to avoid detection.

4. **File Extension Spoofing:** The malicious URL ends in `.jpg`, which may trick a user or a basic filter into thinking it is an image. In reality, it is an executable. Always verify content type, not extension.

5. **Static Metadata is Intelligence:** Author names, creating applications, and timestamps can reveal attacker infrastructure or TTPs. In this case, the author's name (`Alexandre Riviere`) and timestamp provide attribution clues.

## 🛡️ Defensive Recommendations

- **Disable Macros by Default:** Enforce Group Policy to block macros in Office documents originating from the internet.
- **Enable Protected View:** Ensure all downloaded documents open in Protected View.
- **Block Outbound Traffic from Office:** Firewall rules should prevent `WINWORD.EXE` and `EXCEL.EXE` from initiating outbound HTTP/HTTPS connections to unapproved destinations.
- **Monitor for `Document_open`:** Deploy EDR/SIEM detection rules that alert when Office processes execute VBA macros containing the `Document_open` keyword.
- **Block Known IOCs:** Add `hocoso.mobi` and the URL pattern to DNS and proxy blocklists.

---
*This report was completed as part of the LetsDefend SOC Analyst training platform.*