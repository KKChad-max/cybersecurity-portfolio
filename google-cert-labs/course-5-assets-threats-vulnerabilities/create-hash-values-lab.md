# Lab: Create Hash Values (File Integrity Verification)

**Date:** August 24, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Scenario

In this lab, I investigated whether two files (`file1.txt` and `file2.txt`) were identical or different. Although the contents appeared similar when viewed with `cat`, I needed to generate SHA‑256 hashes for each file to definitively determine if they were the same. This is a core security task – hashing allows analysts to verify file integrity and detect unauthorized modifications.

---

## Step 1: Exploring the Files

I started by listing the contents of my home directory:

```bash
analyst@17ad2958f70e:~$ ls
file1.txt  file2.txt
```

**I viewed the contents of both files:**

```bash
analyst@17ad2958f70e:~$ cat file1.txt
X50!P%@AP[4\PZX54(P^)7CC]7]$SEICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

```bash
analyst@17ad2958f70e:~$ cat file2.txt
X50!P%@AP[4\PZX54(P^)7CC]7]$SEICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
9sxa5Yq20R
```

At first glance, the contents looked almost identical. However, a closer inspection revealed a subtle difference: `file2.txt` contained an extra string (`9sxa5Yq20R`) at the end.

---

## Step 2: Generating SHA‑256 Hashes

**I generated a SHA‑256 hash for each file using the `sha256sum` command:**

```bash
analyst@17ad2958f70e:~$ sha256sum file1.txt
131f95c51cc819465fa1797f6ccacf9d494aaaff46a3eac73ae63ffbdfd8267  file1.txt
```

```bash
analyst@17ad2958f70e:~$ sha256sum file2.txt
2558ba9a4cad169804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt
```

The **hashes were completely different.** This confirmed that the files were not identical, even though the text appeared similar at first glance.

---

## Step 3: Writing Hashes to Files

**To compare the hashes more easily, I saved them to separate files:**

```bash
analyst@17ad2958f70e:~$ sha256sum file1.txt > file1hash
analyst@17ad2958f70e:~$ sha256sum file2.txt > file2hash
```

**I verified the contents of each hash file:**

```bash
analyst@17ad2958f70e:~$ cat file1hash
131f95c51cc819465fa1797f6ccacf9d494aaaff46a3eac73ae63ffbdfd8267  file1.txt
```

```bash
analyst@17ad2958f70e:~$ cat file2hash
2558ba9a4cad169804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt
```

---

## Step 4: Comparing the Hashes

**I used the `cmp` command to compare the two hash files:**

```bash
analyst@17ad2958f70e:~$ cmp file1hash file2hash
file1hash file2hash differ: char 1, line 1
```

The `cmp` command confirmed that the files differed at the very first character of the first line, proving that `file1.txt` and `file2.txt` were not identical.

---

## Tools Used

| Tool / Command | Purpose |
| :--- | :--- |
| `ls` | List files in the current directory |
| `cat` | Display file contents |
| `sha256sum` | Generate a SHA‑256 hash value for a file |
| `>` | Redirect command output to a new file |
| `cmp` | Compare two files byte by byte |

## Reflection

This lab demonstrated the importance of **hashing** as a security control for verifying file integrity. Key takeaways:

- **Hashing is not reversible:** Unlike encryption, hashing is a one‑way function – you cannot derive the original data from the hash.
- **Integrity verification:** Even a tiny change in a file (like one extra line) produces a completely different hash value.
- **Practical application:** Security analysts use hashing to:
  - Verify that downloaded software hasn't been tampered with.
  - Detect unauthorized file modifications.
  - Identify malicious files that mimic legitimate ones.
  - Ensure data integrity during backups and transfers.

This lab reinforced the importance of hashing in maintaining the integrity of critical assets – a core concept in the **CIA triad** and a fundamental security control.