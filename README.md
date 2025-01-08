# 40X-FUZZER Tool

This is a Python-based tool for running **ffuf** fuzzing on multiple URLs using a wordlist. It processes a list of URLs with the **ffuf** tool and checks for valid responses, outputting results to a file. The tool also supports showing progress with a live URL counter.

### Description

40X-FUZZER is designed to automate the process of running **ffuf** across a list of URLs and a wordlist, making it easier for users to perform directory or parameter fuzzing on multiple websites at once. The results are saved to an output file, with only relevant information displayed (e.g., URLs that return 200 status codes).

### Requirements

Before running the tool, you must install **ffuf** and the required Python libraries.

- **ffuf**: [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf)
- Python 3.6+ (ensure that Python and pip are installed)

### Installation

1. **Install ffuf**:
   - Follow the installation instructions on the [ffuf GitHub page](https://github.com/ffuf/ffuf) to install `ffuf` on your system.

2. **Clone the repository**:
   ```bash
   git clone https://github.com/buggedout-1/40x-fuzzer.git
   cd 40x-fuzzer
   pip install -r requirements.txt

3. **Usage**:
   `python ffuf.py -l <url_list.txt> -w <wordlist.txt> -o <output_file.txt>`

   -l <url_list.txt>: Path to the file containing URLs to test (one URL per line).  
   -w <wordlist.txt>: Path to the wordlist file (one word per line).  
   -o <output_file.txt>: Path to the output file to save the results (e.g., 400-bypassed.txt).


**Best way to use**:  
`subfinder -d domain.com -o subs.txt`  
`httpx -l subs.txt -mc 401,402,403,404 -o 400.txt`  
`python 40x-fuzzer.py -l subs.txt -w fuzz.txt -o 400-bypassed.txt`
