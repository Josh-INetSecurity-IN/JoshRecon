import builtwith
import sys
from colorama import Fore, Style, init
from urllib.parse import urlparse

init(autoreset=True)

def normalize_url(url):
    """Normalize the URL by adding http:// if missing"""
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url

def detect_tech(url):
    """Detect technologies used by the given URL"""
    try:
        tech = builtwith.parse(url)
        return tech
    except Exception as e:
        print(f"{Fore.RED}[!] Error detecting technology: {str(e)}")
        return {}

def print_results(tech):
    """Pretty print the results with a nice format"""
    if not tech:
        print(f"{Fore.YELLOW}[!] No technology detected.")
        return

    print(f"\n{Fore.GREEN}[+] Technologies Detected:\n")
    
    # Enhance printing by adding more detail to each category
    for category, items in tech.items():
        print(f"{Fore.CYAN}{category}:")
        if isinstance(items, list):
            for item in items:
                print(f"  {Fore.WHITE}- {item}")
        elif isinstance(items, dict):  # Some categories may have dicts with more info
            for sub_category, sub_items in items.items():
                print(f"    {Fore.YELLOW}{sub_category}:")
                for sub_item in sub_items:
                    print(f"      {Fore.WHITE}- {sub_item}")
        print()

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Usage: python joshrecon.py <url>")
        sys.exit(1)

    url = normalize_url(sys.argv[1])
    print(f"{Fore.BLUE}[*] Scanning: {url}")
    tech = detect_tech(url)
    print_results(tech)

if __name__ == "__main__":
    main()
