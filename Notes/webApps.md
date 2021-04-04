
# Web Applications
- **Can run on any port, normally on 80 or 8080**

## What are they?
- they are a variety of applications running 

## Enumeration
- there are a number of tools for enumerating web applications
- some of them are listed here, but there are probably more

  ### General things to notice from tools, manual exploration
    - look at paths that have logins, or seem like they are only meant for restricted access
    - look at the headers defined in the user requests, and confidential info that may be in reponses
    - these tools only work well if you have good wordlists.  I recommend using SecList for oscp

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





