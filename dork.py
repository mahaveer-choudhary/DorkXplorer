from __future__ import print_function
import sys
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

## Checking Python version
if sys.version_info[0] < 3:
    print("\n\033[91m[ERROR] This tool requires Python 3.x\033[0m\n")
    sys.exit(1)

def logo():
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + r"""
________                __    ____  ___      .__                              
\______ \   ___________|  | __\   \/  /_____ |  |   ___________   ___________ 
 |    |  \ /  _ \_  __ \  |/ / \     /\____ \|  |  /  _ \_  __ \_/ __ \_  __ \
 |    `   (  <_> )  | \/    <  /     \|  |_> >  |_(  <_> )  | \/\  ___/|  | \/
/_______  /\____/|__|  |__|_ \/___/\  \   __/|____/\____/|__|    \___  >__|   
        \/                  \/      \_/__|                           \/       
    """+ Style.RESET_ALL)
## Color codes
class colors:
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"

    ## Default output filename
    log_file = "dorks_output.txt"

    @staticmethod
    def logger(data):
        """Logs data to a file."""
        with open(colors.log_file, "a", encoding="utf-8") as file:
            file.write(data + "\n")

    @staticmethod
    def dorks():
        """Main function for handling Google Dorking."""
        global log_file  # Log file is accessible globally
        try:
            logo()
            
            while True :
                dork = input(f"{colors.CYAN}\n[+] Enter the Dork Search Query: {colors.RESET}")
                if dork :
                    break
                else :
                    print(f"{colors.RED}[Error] You didn't enter dork, please enter it first !")

            user_choice = input(f"{colors.CYAN}[+] Enter Total Number of Results you want (or type 'all' to fetch everything): {colors.RESET}").strip().lower()
            if not user_choice :
                print(f"{colors.RED}[-] By default it selects 'all'! ")

            if not user_choice or user_choice == "all":
                total_result = float("inf")  # Fetch until no more results
            else:
                try:
                    total_result = int(user_choice)
                    if total_result <= 0:
                        raise ValueError("Number must be greater than zero.")

                except ValueError:
                    print(f"{colors.RED}[ERROR] Invalid number entered! Please enter a positive number or 'all'. {colors.RESET}")
                    sys.exit(1)

            save_output = input(f"{colors.CYAN}\n[+] Do you want to save the output? (Y/N): {colors.RESET}").lower().strip()
            if save_output == "y":
                log_file = input(f"{colors.CYAN}[+] Enter Output filename: {colors.RESET}").strip()
                if not log_file:
                    log_file = "dorks_output.txt"
                if not log_file.endswith(".txt"):
                    log_file += ".txt"

            print(f"\n{colors.GREEN}[INFO] Searching! Please wait... {colors.RESET}\n")

            fetched = 0
            start = 0

            # Google Custom Search API credentials
            api_key = "AIzaSyB-T44kLFdLVsVWgYlX2L9HdZeRC6gBNq4"
            search_engine_id = "d40f55b2c555643ec"

            while fetched < total_result:
                if total_result != float("inf"):
                    remaining = min(10, total_result - fetched)  # Fetch in batches of 10
                else:
                    remaining = 10

                try:
                    # Perform the search request
                    response = requests.get(
                        f"https://www.googleapis.com/customsearch/v1",
                        params={
                            "key": "AIzaSyB-T44kLFdLVsVWgYlX2L9HdZeRC6gBNq4",
                            "cx": "d40f55b2c555643ec",
                            "q": dork,
                            "num": remaining,
                            "start": start
                        }
                    )
                    response.raise_for_status()
                    results = response.json()

                    # Extract and print URLs
                    for item in results.get("items", []):
                        url = item.get("link")
                        print(f"{colors.MAGENTA}[+] {colors.RESET}{url}")
                        if save_output == "y":
                            colors.logger(url)

                    fetched += remaining
                    start += remaining
                    time.sleep(1)  # Delay between requests

                except Exception as e:
                    print(f"{colors.RED}[ERROR] {str(e)} {colors.RESET}")
                    sys.exit(1)

        except KeyboardInterrupt:
            print(f"\n{colors.RED}[!] User interruption detected! Exiting... {colors.RESET}\n")
            sys.exit(1)
        except Exception as e:
            print(f"{colors.RED}[ERROR] {str(e)} {colors.RESET}")
            sys.exit(1)

if __name__ == "__main__":
    colors.dorks()
