# Cybernerddd Path Traversal Fuzzer

A lightweight Python tool for detecting **path traversal vulnerabilities** using payload fuzzing and response analysis.

> ⚠️ For **authorized testing only**

---

## Features

- Parameter-based path traversal fuzzing
- Multiple encoding techniques:
  - Raw
  - URL encoded
  - Double encoded
  - Slash encoded
  - Dot encoded
- Smart response analysis (Linux + Windows indicators)
- Clean output (only successful hits shown)
- Duplicate request filtering
- Lightweight & fast

---

## 📦 Installation

```bash
git clone https://github.com/cybernerddd/Cybernerddd-PathTraversal-Fuzzer.git
cd Cybernerddd-PathTraversal-Fuzzer
pip install -r requirements.txt
```

##  Usage

```
python path_traversal_fuzzer.py -u "http://target.com/page?file=INJECT"
```
<img width="1070" height="318" alt="Screenshot 2026-05-04 043113" src="https://github.com/user-attachments/assets/906e4be3-c1bd-45f0-9d24-6afd2b831c21" />

## ✅ Example Output
```
[+] SUCCESSFUL MATCHES
------------------------------------------------------------
[200] len=2700 | payload=../../../../etc/passwd | url=http://target/...
```
<img width="1350" height="525" alt="Screenshot 2026-05-04 043353" src="https://github.com/user-attachments/assets/a4d35e1d-2786-4074-91a5-afff30698d66" />

## 🧠 How It Works
1. Replaces INJECT with traversal payloads
2. Applies encoding techniques
3. Sends HTTP requests
4. Checks response for known indicators
5. Displays only successful matches

<img width="1597" height="769" alt="Screenshot 2026-05-04 043505" src="https://github.com/user-attachments/assets/982ce1fd-2c6d-4d17-b404-f9147eba752e" />

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized security testing only**.
The author is not responsible for misuse.

### 👤 Author

### Cybernerddd
