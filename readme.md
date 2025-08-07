![ByakkuScanner](./Resources/banner.jpg)
<h1 align="center">ByakuScanner</h1>

<p align="center">
  <i>A lightweight CLI tool for recursively scanning directories for sensitive secrets like API keys, tokens, and credentials.</i>
</p>

---

## 🔍 Features

- Scans files in a target directory recursively
- Detects sensitive information using regex (e.g., AWS keys, JWT tokens, private keys, etc.)
- Generates a detailed report (plain text format)
- Optional masking of secrets in report output [🛠️]
- Optional ZIP compression of the final report [🛠️]
- Logs runtime duration of scan
- Modular, readable Python codebase

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- No external libraries required

### Installation

```bash
git clone https://github.com/yourusername/ByakuScanner.git
cd ByakuScanner
python Scanner.py /path/to/target
```

### Usage

python Scanner.py <target_directory> [--target] [--report]

Options
- --report/--r : specify location to save script output.
- --target/--t : specify location for recursive scan to start.

Example
```bash
python Scanner.py ./test_dir --target ./folder_secrets --report ./output_here
```
--- 

### Regex Patterns Used
ByakuScanner currently detects:

 - AWS Access Keys (AKIA...)

 - JWT Tokens

 - Generic API keys (e.g., api_key=..., apikey: ...)

 - Private Keys (-----BEGIN PRIVATE KEY-----)

 - Custom developer-defined patterns

Regex patterns are stored in patterns.py and are easily extendable. Feel free to clone and craft your own regex!

---
### How does it work?
ByakuScanner uses os.walk() to recursively crawl through directories, checking each file with defined regular expressions. Detected secrets are logged into a report.

--- 
### WHY did I make this? 
I made this tool to:
  > Practice regex-based pattern scanning
    
  > Improve CLI tool design skills

  > Demonstrate understanding of modular Python, file I/O, and subprocesses

  > Impress my friends. XD

---
## 📄 License

MIT License.  
See [LICENSE](LICENSE) file for details.

---

## 👨🏽‍💻 Author

**Jinmi-Codes (Koji)**  
Security+ Certified | I LOVE PEANUTS AND I AM SEVERELY SLEEP DEPRIVED.
🔗 [GitHub @Jinmi-codes](https://github.com/Jinmi-codes)

---