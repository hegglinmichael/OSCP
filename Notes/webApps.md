
# Web Applications
- **Can run on any port, normally on 80 or 8080**
- if you know the username, just brute it with hydra
  - hydra -l admin -P /usr/share/wordlists/rockyou.txt [ip] http-post-form /department/login.php:"username=^USER^&password=^PASS^:Invalid Password"
 
## What are they?
- they are a variety of applications running 

## Enumeration
- there are a number of tools for enumerating web applications
- some of them are listed here, but there are probably more

  ### General things to notice from tools, manual exploration
    - look at paths that have logins, or seem like they are only meant for restricted access
    - look at the headers defined in the user requests, and confidential info that may be in reponses
    - these tools only work well if you have good wordlists.  I recommend using SecList for oscp
    - look for setting files once a low level shell is obtained, could have creds for databases or users
    - use webappalyzer and look up all website infra

  ### Burpsuite
    - use burpsutie to look at requests and reponses
    - use repeater to modify request
    - attempt to achieve common web app exploits like XSS, path traversal, etc

  ### Nikto
    - nikto -host [ip]
    - great general tool to start scanning web application
    - can run with ssl 
      - nikto -host [ip] -ssl
      
    - look at outputs of nikto specifically at the paths it reports
    - look at ssl information
    
  ### gobuster
    - **Note: you need wordlists for this**
    - gobuster -dir -u http://[ip] -w [you're word list] -s '[responses you want, ie 200, 300, 204, etc]' -e
    - great for using large wordlists that you can find online
      - I recommend SecLists
    - can filter out responses you want as well which can be very helpful
    - for kali
      - gobuster dir -u [ip] -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,cnf,conf -k
    
  ### wfuzz
    - wfuzz --hc 404 -c -w [wordlist] -u http://[ip]/FUZZ
    - the above can filter out respones (specifically 404 in this case)
    - tries to fuzz on specific path where you put "FUZZ" in url path
## Subdomain Enumeration
* gobuster dns -d schooled.htb -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -i
 

## Wordpress
* wpscan --url http://[ip] -P /usr/share/wordlists/rockyou.txt --username sean
* look at the common path for plugins: /wp-content/plugins

## JWT
* in some cases, a jwt can be modified to get root priveliges.  Make sure to look in burp

## sqlmap for login injections
* EX: sqlmap -u http://10.10.10.230:80/login --data="login=iron&password=man" --method POST --dbs --batch
* will need burp to look up request params

# Links Table

| Description | Link |
| Reverse Shell through Wordpress plugin upload | https://sevenlayers.com/index.php/179-wordpress-plugin-reverse-shell |














