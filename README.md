This is a suddomain finder tool made with python

In this tool we use multithreading functionality for fast subdomain scan 

also we use requests to get respone and save subdomain in recon folder and we use time for print current scanning time and also print how much time it get to sacn all subdomain 

and import colorama for change color and import argparse for tool description.

# Installation:

sudo git clone https://github.com/kidnapshadow-sidharth/subdomain_finder.git

cd subdomain_finder/

sudo chmod +x setup.sh

sudo bash setup.sh

# Usage:

python3 python3 suddomain_finder.py -u <host> -w <wordlist> -t <threads>

example : python3 -u google.com -w wordlist.txt -t 25

# Requirement:

pip install requests

pip install threading

pip install time

pip install queue

pip install colorama

pip install argparse
