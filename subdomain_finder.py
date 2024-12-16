import requests
import threading
import queue
import argparse
import os
import time
from colorama import Fore, init

init()

# define color
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
# it show help for subdomain finder tool

argparse = argparse.ArgumentParser(description="Subdomain finder tool",
                                   usage="python3 subdomain_finder.py -u URL -w WORDLIST -t THREADS")

argparse.add_argument("-u", "--url", help="Enter the full url (ex: -d http://example.com)", required=True)
argparse.add_argument("-w", "--wordlist", help="Enter wordlist path full path", required=True)
argparse.add_argument("-t", "--threads", help="Enter thread for fast scan")

args = argparse.parse_args()
host = args.url
wordlist = args.wordlist
threads = int(args.threads)

usage = f"{green} python3 suddomain_finder.py -u <host> -w <wordlist> -t <threads>  {reset} "


print(f"{red}*{reset}" * 75)
ascii_banner = ''' {} 
 ____ _  _ ___  ___  ____ _  _ ____ _ __ _     ____ _ __ _ ___  ____ ____
 ==== |__| |==] |__> [__] |\/| |--| | | \| ___ |--- | | \| |__> |=== |--<

'''.format(green)
print(ascii_banner)
print(f"{red}*{reset}" * 75)

if not host or not wordlist or not threads:
    print(usage)
    exit()


#to store output in recon directory
recon_dir = 'recon'

#check recon directory is exist or not
# if it's not exist make it

if not os.path.exists(recon_dir):
    os.mkdir(recon_dir)

# then we make a host directory under recon directory

recon_dir_path = 'recon/' + host

# if it's not exist make it

if not os.path.exists(recon_dir_path):
    os.mkdir(recon_dir_path)

# write first domain
with open(recon_dir_path + '/subdomain', 'a') as file:
    file.write(host + '\n')


q = queue.Queue()

# print starting line

print(f"start finding subdomain for host : {host}")
start_time = time.time()
#define a subbrute function
def subbrute():
    while not q.empty():
        subdomain = q.get()
        url = f"https://{subdomain}.{host}"
        try:
            response = requests.get(url, allow_redirects=False, timeout=2)
            if response.status_code == 200:
                sub = response.url.split('/')[2]
                #http: / / example.com (example.com at index 2)
                print("[+] Subdomain found : {} ".format(sub))
                with open (recon_dir_path + '/subdomain', 'a') as file:
                    file.write(sub + '\n')
        except:
            pass
        q.task_done()


# wordlist file open

with open(wordlist, 'r') as file:
    subdomains = file.read().splitlines()
    for subdomain in subdomains:
        q.put(subdomain)

#defining threads for fast scan


for i in range(threads):
    t = threading.Thread(target=subbrute, daemon=True)
    t.start()

q.join()
end_time = time.time()

# calculate time
print("Time taken : {}".format(end_time - start_time))
print("                           --kidnapshadow(sidharth)")