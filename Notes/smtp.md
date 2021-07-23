
# SMTP
* simple mail transfer protocol
* used to send emails
* normally used with pop or imap to let user save messages
  * smtp for sending
  * POP or IMAP for receiving

## NMAP Scripts
* smtp-commands
* smtp-enum-users
* smtp-vuln*
* smtp-ntlm-info

## smtp (25, 4555)
+ not vulnerable to basic vulns

  $> nmap -p25 --script smtp-commands 10.10.10.51
  25/tcp open  smtp
  |_smtp-commands: solidstate Hello nmap.scanme.org (10.10.14.25 [10.10.14.25]), 
 
  $> nmap -p25 --script smtp-enum-users 10.10.10.51
  | smtp-enum-users: 
  |_  root

  $> telnet 10.10.10.51 4555
    > help
    > listusers
    > setpassword mindy mindy

  $> 

## pop (110) 
 
  $> telnet 10.10.10.51 110 
    > USER mindy
    > PASS mindy
    > LIST
    > RETR 2



