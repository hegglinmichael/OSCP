
# SNMP
+ you can normally find this on port: 161

## tools for cloning information
+ https://github.com/dheiland-r7/snmp.git

## Commands to help
+ nmap --script snmp-brute [ip] -p [port]
+ snmpwalk -v X -c public <IP> NET-SNMP-EXTEND-MIB::nsExtendOutputFull
+ snmpwalk -v X -c public <IP> 

