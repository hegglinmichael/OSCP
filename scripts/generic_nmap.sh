#!/bin/bash

# created by Michael Hegglin
#   used to help on oscp exploitation

if [ $# -eq 0 ]
then
    echo "usage: auto_nmap.sh <target ip>"
    exit 1
fi

echo "==================================="
echo "= 	Starting NMAP		 "
echo "==================================="
echo "useful locations:"
echo "    /usr/share/nmap/scripts/"
echo " "
echo " "


echo "==================================="
echo "= 	Simple Scan		 "
echo "= 	nmap -T4 $1	  	 "
echo "==================================="
nmap -T4 $1


echo "==================================="
echo "= 	All Ports		 "
echo "= 	nmap -T4 -p- $1		 "
echo "==================================="
all_ports=$(nmap -T4 -p- $1)
echo "$all_ports"

ports=$(echo $all_ports | awk -F "SERVICE" '{print $2}')
ports=$(echo $ports | awk -F "Nmap done" '{print $1}')
ports=$(echo $ports | tr '\n' ' ' | sed -e 's/[^0-9]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' ' | sed 's/ /,/g')
echo "$ports"

echo "==================================="
echo "= 	More Intrusive Scan	 "
echo "= 	nmap -sV -T4 $1 -p $ports"
echo "==================================="
nmap -sV -T4 $1 -p $ports


echo "==================================="
echo "= 	Version Grabbing	 "
echo "= 	nmap -A -T4 $1 -p	 "
echo "==================================="
nmap -A -T4 $1 -p $ports

echo "==================================="
echo "= 	Simple UDP Ports	 "
echo "= 	nmap -sU $1		 "
echo "==================================="
sudo nmap -T4 -sU $1 

echo "==================================="
echo "= 	ALL UDP Ports		 "
echo "= 	nmap -sU $1		 "
echo "==================================="
sudo nmap -T4 -sU -p- $1

