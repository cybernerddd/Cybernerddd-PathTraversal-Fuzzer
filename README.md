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

## ✅ Example Output
```
[+] SUCCESSFUL MATCHES
------------------------------------------------------------
[200] len=2700 | payload=../../../../etc/passwd | url=http://target/...
```

## 🧠 How It Works
1. Replaces INJECT with traversal payloads
2. Applies encoding techniques
3. Sends HTTP requests
4. Checks response for known indicators
5. Displays only successful matches

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized security testing only**.

The author is not responsible for misuse.

### 👤 Author

### Cybernerddd
