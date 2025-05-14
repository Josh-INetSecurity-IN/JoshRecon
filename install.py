import os
import subprocess
import sys

def install_via_apt(package):
    """Try installing via system package manager (apt)"""
    try:
        print(f"[+] Trying to install {package} using apt...")
        subprocess.check_call(["sudo", "apt", "install", f"python3-{package}", "-y"])
        print(f"[+] Successfully installed {package} using apt.")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {package} using apt. Proceeding with virtualenv setup...")

def install_via_virtualenv():
    """Set up and use a virtual environment to install dependencies."""
    try:
        print("[+] Setting up a virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", "joshrecon_venv"])
        print("[+] Virtual environment created successfully.")
        
        print("[+] Installing dependencies in the virtual environment...")
        subprocess.check_call(["./joshrecon_venv/bin/pip", "install", "builtwith", "colorama"])
        print("[+] Installation successful within virtual environment.")

        print("\n[*] To activate your virtual environment and use JoshRecon, run the following commands:")
        print("  source ./joshrecon_venv/bin/activate")
        print("  python joshrecon.py <url>")

    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to install in virtual environment: {str(e)}")

def main():
    print("[*] Installing requirements for JoshRecon...\n")
    
    # Try installing via apt first
    install_via_apt("builtwith")
    
    # If apt installation fails, attempt to use virtual environment
    if not os.path.exists("/usr/bin/python3-builtwith"):  # Example check, adjust as needed
        install_via_virtualenv()

if __name__ == "__main__":
    main()
