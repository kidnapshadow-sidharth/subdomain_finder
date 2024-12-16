#!/bin/bash

clear

#define color 
red='\e[1;31m'
green='\e[1;32m'
blue='\e[1;34m'
blink='\e[5m'
stop_blink='\e[25m'
stop_color='\e[0m'


echo -e "$red**********************************************************************$stop_color"
echo -e  """ $green  

 ____ _  _ ___  ___  ____ _  _ ____ _ __ _     ____ _ __ _ ___  ____ ____
 ==== |__| |==] |__> [__] |\/| |--| | | \| ___ |--- | | \| |__> |=== |--<

------------------------------------------------------------------------------------
                                                        Crafted by sidharth
                                                        Twitter: kidnapshadow_kd
------------------------------------------------------------------------------------
 $stop_color """

echo -e "$red**********************************************************************$stop_color"


echo -e "Getting Things Ready For You..... :) \n"

apt-get install python3

apt-get install python3-pip

pip3 install requests

pip3 install threading

pip3 install queue

pip3 install os

pip3 install time

pip3 install colorama

chmod +x subdomain_finder.py

echo -e "\ndone...\n"

clear

python3 subdomain_finder.py --help