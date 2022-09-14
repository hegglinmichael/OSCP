
# ftp
- **normally on port 21**
- look around at all the files
- look at what directory you are in
- try to download files and look at them
- try to upload shell code that could be used for an attack
- remember to mess with the settings (ie put in passive mode, etc)

## What is it?
- it's a file transfer protocol

## information gathering
- nc -nv [ip] [port]
  - this could grap the version of ftp being used
- openssl s_client -connect [ip]:[port] -starttls ftp
  - grabs the ftp certificate

## simple ftp cmd
- $> ftp [ip]
  - connects to the remote ftp and gives cmdline
- ftp$> ls [dir]
  - lists all the files in the ftp dir
- ftp$> get [file]
  - gets a file from the server
- ftp$> put [file]
  - put your own file onto the server (**This could be shell code**)

# enumeration
* nmap --script ftp-vuln* [ip] -p [ports]
* nmap --script ftp-enum* [ip] -p [ports]

## connection with ssl certificate






