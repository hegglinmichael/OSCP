
# rdp (Remote Desktop protocol)
- with this you can get a vncviewer type login
- normally runs on port 3389

## Enumeration
  - rdesktop  -u [uname] -p [pasword] [ip] -g 50%
    - the above will try to login for you
  - ncrack -vv --user Administrator -P [password list] rdp://[ip]
    - the above will try to brute force it's way in


