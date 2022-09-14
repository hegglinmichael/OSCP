
# ssh
- **normally on port 22**
- basically hope that it's an old outdated version
  - look for outdated vulns with searchsploit or google
- could use nmap to look at the algorithms

## information gathering
- nc -nv [ip] [port]
  - could get the ssh version

## Misc.
- sometimes you must specify the type of algorithm used to communicate
- ssh -t [user]@[ip] bash --norc --noprofile

