import subprocess
import argparse
import re
import sys

print(f"[*][*][*] 40X-FUZZER started ! [*][*][*]")
def run_ffuf(url, wordlist, output_file, counter, total_urls):
    try:
        command = ["ffuf", "-w", wordlist, "-u", url + "/FUZZ", "-mc", "200"]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Filter and display only the relevant lines, showing full URL
        for line in result.stdout.splitlines():
            if "Status: 200" in line:  # Only show lines with "Status: 200"
                # Extract the directory name (e.g., 'archives/') from the line
                parts = line.split()
                directory = parts[0] if parts else ""
                
                # Show the full URL with the domain and the directory
                if directory:
                    full_url = f"{url}/{directory}"
                    # Clean the line by removing any terminal escape sequences
                    cleaned_url = re.sub(r'\x1b\[[0-9;]*[mGKHJ]', '', full_url)
                    # Write the cleaned full URL to the output file
                    with open(output_file, "a") as f:
                        f.write(cleaned_url + "\n")
        
        # Update and show the live counter with [current / total]
        counter[0] += 1
        sys.stdout.write(f"\rProcessed URLs: [ {counter[0]} / {total_urls} ]")
        sys.stdout.flush()  # Manually flush the output after writing
    
    except subprocess.CalledProcessError as e:
        print(f"Error running ffuf for {url}: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run ffuf on a list of URLs with a specified wordlist.")
    parser.add_argument("-l", "--list", required=True, help="Path to the list of URLs.")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist.")
    parser.add_argument("-o", "--output", default="403-bypassed.txt", help="Path to the output file (default: 403-bypassed.txt).")
    
    args = parser.parse_args()

    # Read list of URLs from the file
    with open(args.list, "r") as file:
        urls = file.readlines()

    # Initialize counter and total URLs
    total_urls = len(urls)
    counter = [0]

    # Run ffuf for each URL
    for url in urls:
        url = url.strip()  # Remove any extra whitespace or newline
        run_ffuf(url, args.wordlist, args.output, counter, total_urls)

    # Final message after completion
    print(f"\nProcessing completed. Total URLs processed: {counter[0]}")

if __name__ == "__main__":
    main()
