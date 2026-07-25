# OverTheWire Bandit — Levels 0-10

## Objective
Build foundational Linux command-line skills through OverTheWire's Bandit wargame.

## Tools Used
- SSH
- Linux commands: `ls`, `cat`, `cd`, `find`, `grep`, `file`, `sort`, `uniq`, `strings`, `base64`

## Walkthrough

### Level 0 → 1
- **Command:** `ls` then `cat readme`
- **Password:** 6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR
- **Reflection:** Basic navigation and file reading.

### Level 1 → 2
- **Command:** `cat ./-`
- **Password:** PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
- **Reflection:** Filenames starting with `-` need `./` prefix.

### Level 2 → 3
- **Command:** `cat ./--spaces\ in\ this\ filename--`
- **Password:** 7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
- **Reflection:** Filenames with spaces need `\` to escape them, and `./` prevents `--` from being read as a command flag.

### Level 3 → 4
- **Command:** `cd inhere`, `ls -la`, `cat ...Hiding-From-You`
- **Password:** xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
- **Reflection:** Hidden files start with `.` and need `ls -la` to see.

### Level 4 → 5
- **Command:** `cd inhere`, `file ./*`, `cat ./-file07`
- **Password:** 6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
- **Reflection:** Use `file` to identify readable files.

### Level 5 → 6
- **Command:** `find . -type f -size 1033c ! -executable`, `cat ./maybehere07/.file2`
- **Password:** pXa26xhMWaC2SvDotA4r9EgZkulOeSBW
- **Reflection:** Find files by size and permission.

### Level 6 → 7
- **Command:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`, `cat /var/lib/dpkg/info/bandit7.password`
- **Password:** Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3
- **Reflection:** Global search with specific ownership.

### Level 7 → 8
- **Command:** `grep "millionth" data.txt`
- **Password:** VR1ljMayciFxbnUokuQmJFw6QC9VKtub
- **Reflection:** `grep` finds specific strings in files.

### Level 8 → 9
- **Command:** `sort data.txt | uniq -u`
- **Password:** EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
- **Reflection:** `uniq -u` finds unique lines.

### Level 9 → 10
- **Command:** `strings data.txt | grep "="`
- **Password:** B0s2khmbT9u0geKuOoVGW3JZKhndE3BG
- **Reflection:** `strings` extracts readable text.

### Level 10 → 11
- **Command:** `base64 -d data.txt`
- **Password:** pYfOY6HwUsDj5rL9UvyhU7MCmv8vN5Ro
- **Reflection:** Decoding Base64 with `-d` flag.

## What I Learned
- Linux file navigation and manipulation
- File permissions and hidden files
- Searching with `find`, `grep`, and piping
- Decoding Base64
- SSH remote connections# OverTheWire Bandit — Levels 0-10
