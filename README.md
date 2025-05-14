To install the dependencies, run the install.py script:

python install.py

This script will automatically install the required packages.

    Note: If you can’t use pip directly, the script will attempt installation through subprocesses.

3. Run JoshRecon

After installation, you can start using JoshRecon to detect the tech stack of any website.

python joshrecon.py <url>

Example

To detect the technology stack of example.com, run:

python joshrecon.py example.com

Sample Output:

[*] Scanning: http://example.com
[+] Technologies Detected:

  Servers:
    - Apache
  Web Frameworks:
    - Django
  CMS:
    - WordPress
  JS Libraries:
    - jQuery
  Analytics:
    - Google Analytics
  CDN:
    - Cloudflare


To Use:

    Step 1: Run install.py:

python install.py

Step 2: Follow the output instructions to activate the virtual environment:

source ./joshrecon_venv/bin/activate

Step 3: Once the environment is activated, run JoshRecon:

python joshrecon.py example.com
