
# Windows Shell Commands
- if you're like me, you mostly use windows for development so you may need help when cmds like "whoami" don't work
- great guides with more in depth knowledge
- help escalating: https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html

## Simple tricks
  - use the below if commands aren't working.  Basically, the process you're currently running has certain restrictions and you want to switch to a more stable one
  - ps
    - migrate [pid]

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
