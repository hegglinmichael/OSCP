'''
This is a tool meant for my OSCP notes.  By typing in certain 
topics, it'll help you by printing out the related information 
that I currently know about the topic
'''

command_list = ["scripts", "README","bufferOverflow","dns","ftp","ipp","ldap","metasploit","misc","oneliners","oracleDB","pcap","privEsc","rdp","shellCode","smb","smtp","snmp","ssh","webApps","windowsShellCmd"]
notes_knowledge = {"README","bufferOverflow","dns","ftp","ipp","ldap","metasploit","misc","oneliners","oracleDB","pcap","privEsc","rdp","shellCode","smb","smtp","snmp","ssh","webApps","windowsShellCmd"}
scripts_list = ["Mike_Czumak.py","generic_nmap.sh","heartbleed_SSLTLS.py","linpeas.sh","linuxExploitSuggester.sh","more_linux_enum.sh","pattern.py","rpcdump.py","timeclock.py"]

def help_me():
    print("\n")
    print("=========================")
    print("TOPICS")
    print("=========================") 
    for cmd in sorted(command_list):
        print(cmd)
    print("\n")

def print_knowledge(cmd):
    f = open("../Notes/" + cmd + ".md", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

def print_scripts_help():
    print("\n") 
    print("=========================")
    print("AVAILABLE SCRIPTS")
    print("=========================")
    for script in scripts_list:
        print(script)
    print("\n")

def scripts_prompt():
    '''
    we want this to be a new prompt,
    in here we want to be able to launch
    a server to be able to copy scripts
    from.  This way I don't have to go
    through the pain of copy and pasting
    '''
    print_scripts_help()

    while (True):
        cmd = input("Enter script to copy: ")
        if (cmd == "quit"):
            break

def main():
    
    while(True):
        cmd = input("Enter something to lookup: ")
        if (cmd == "quit"):
            print("\n\nEXITING\n\n")
            break
        elif (cmd == "help"):
            help_me()
        elif (cmd in notes_knowledge):
            print_knowledge(cmd)
        elif (cmd == "scripts"):
            scripts_prompt()


if __name__ == "__main__":
    main()



