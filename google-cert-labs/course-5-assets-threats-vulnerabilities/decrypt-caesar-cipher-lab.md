# Decryption Lab: Caesar Cipher & OpenSSL Recovery

**Date:** August 24, 2026  
**Author:** Chadrack Kalongo Kabinda  
**Course:** Google Cybersecurity Certificate – Course 5  

---

## Scenario

In this lab activity, all files in my home directory were encrypted. I needed to use Linux commands to break a Caesar cipher and decrypt the files to recover the hidden message. The goal was to practice decryption techniques and understand how basic cryptography can be used to protect (or restrict access to) data.

---

## Step 1: Initial Investigation

I started by listing the contents of my home directory:

---

```bash
analyst@e40e264877f8:~$ ls
01.encrypted  README.txt  caesar
```

**The `README.txt` file contained the following message:**

```text
Hello,
All of your data has been encrypted. To recover your data, you will need to solve a cipher.
To get started look for a hidden file in the caesar subdirectory.
```

---

## Step 2: Finding the Hidden File

**I navigated to the `caesar` directory and listed all files, including hidden ones:**

```bash
analyst@e40e264877f8:~$ ls -la caesar
total 12
drwxr-xr-x  2 root    root    4096 Aug 24 07:17 .
drwxr-xr-x  3 analyst analyst 4096 Aug 24 07:40 ..
-rw-------  1 root    root     160 Aug 24 07:17 .leftShift3
```

The hidden file `.leftShift3` was the ciphertext I needed to decode.

---

## Step 3: Reading the Ciphertext

**I read the hidden file using `cat`:**

```bash
analyst@e40e264877f8:~$ cat caesar/.leftShift3
lq rughu wr uhfryhu brxu ilohv brx zloo qhhg wr hqwhu wkh iroorz
lqj frppdqg:

rshqvvo dhv-256-fe5 -sengi2 -d -g -lq T1.hqfubswhg -rxw T1.uhfryh
huhg -n hwwxeuxwh
```

---

## Step 4: Decoding the Caesar Cipher

**The filename `.leftShift3` indicated that the text was encrypted using a left shift of 3. To decode it, I applied a right shift of 3 using the `tr` command:**

```bash
analyst@e40e264877f8:~$ cat caesar/.leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```

Decoded output:

``text
In order to recover your files you will need to enter the following command:

openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettbutre
```

(The `-k ettbutre` is the decryption key.)

---

## Step 5: Recovering the Encrypted File

**I ran the `openssl` command with the recovered key:**

```bash
analyst@e40e264877f8:~$ openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettbutre
```

---

## Step 6: Verification

**I listed the directory to confirm the recovered file was created:**

```bash
analyst@e40e264877f8:~$ ls
Q1.encrypted  Q1.recovered  README.txt  caesar
```

**I then read the recovered file:**

```bash
analyst@e40e264877f8:~$ cat Q1.recovered
If you are able to read this, then you have successfully decrypted the classic cipher text. You recovered the encryption key that was used to encrypt this file. Great work!
```

Success! The file was successfully decrypted and the data was recovered.

---

## Tools Used

| Tool / Command | Purpose |
| :--- | :--- |
| `ls -la` | List all files, including hidden ones |
| `cat` | Read file contents |
| `tr` | Perform letter substitution (Caesar cipher decoding) |
| `openssl` | Decrypt the AES-256-CBC encrypted file |

---

## Reflection

**This lab demonstrated how basic cryptographic techniques (Caesar cipher) and symmetric encryption (AES-256-CBC) can be used to secure data. Key takeaways:**

- **Caesar cipher:** Understanding shift values is essential for decoding simple encrypted messages.

- **OpenSSL:** A powerful command-line tool for encryption and decryption.

- **Linux command-line proficiency:** Used 'ls -la', 'cat', 'tr', and 'openssl' to complete the task.

- **Following instructions:** The README provided a clear path to recovery, reinforcing the importance of documentation.

This lab reinforced the value of encryption as a security control – both for protecting data and, in this simulated scenario, for understanding how to recover it.