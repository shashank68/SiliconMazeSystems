FLAG = "MAZ3{H4rry_P00tt3r_i5_m1n3}"
MENU = "\nauthenticate\ngetflag\nhelp\nquit\n\n> "
AUTHENTICATED = False

print(MENU, end='')
option = input().lower()
while(option != "quit"):
    if(option == "authenticate"):
        print("Identify yourself: ", end='')
        identity = input().lower()
        if(identity == "half blood prince" or identity == "half-blood prince" or identity == "the half blood prince" or identity == "the half-blood prince"):
            AUTHENTICATED = True
            print("Authentication successful.\n> ", end='')
        else:
            print("Authentication failed.\n> ", end='')
    elif(option == "getflag"):
        if(AUTHENTICATED == True):
            print(FLAG + "\n", end='')
            break
        else:
            print("Please authenticate yourself first.\n> ", end='')
    elif(option == "help"):
        print("No help here.\n> ", end='')
    elif(option == "quit"):
        break
    else:
        print("Invalid command.\n> ", end='')
    option = input().lower()
