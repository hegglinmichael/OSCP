
# ldap
- normally on port 389

## What is it?
  - Lightweight directory access protocol
  - used to authenticate/authorize users
  
## Enumeration
  - a few nmap scripts, with the most important being below
    - nmap --script ldap-search.nse -p [port] [ip]
  - ldap tooling
    - ldapsearch -h [host] -p [port] -x -s base


