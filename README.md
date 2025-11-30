# 40X-FUZZER

> Batch fuzzing tool to discover hidden paths and bypass 403/401 restrictions using ffuf

## Features

- Batch process multiple URLs from a file
- Live progress counter
- Clean output with full URLs
- Customizable wordlist and output file

## Requirements

- [ffuf](https://github.com/ffuf/ffuf) installed and in PATH
- Python 3.6+

## Installation

```bash
git clone https://github.com/buggedout-1/40x-fuzzer.git
cd 40x-fuzzer
pip install -r requirements.txt
```

## Usage

```bash
python 40x-fuzzer.py -l <url_list.txt> -w <wordlist.txt> -o <output_file.txt>
```

| Flag | Description |
|------|-------------|
| `-l` | Path to file containing target URLs (one per line) |
| `-w` | Path to wordlist file |
| `-o` | Output file for results (default: `403-bypassed.txt`) |

## Recommended Workflow

```bash
# 1. Find subdomains
subfinder -d target.com -o subs.txt

# 2. Filter for 40x responses
httpx -l subs.txt -mc 401,402,403,404 -o 40x.txt

# 3. Fuzz for bypasses
python 40x-fuzzer.py -l 40x.txt -w fuzz.txt -o bypassed.txt
```

## License

MIT
