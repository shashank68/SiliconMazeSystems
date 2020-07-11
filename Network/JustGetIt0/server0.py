FLAG = "flag_goes_here"
MENU = "\nauthenticate\ngetflag\nhelp\nquit\n\n> "
AUTHENTICATED = False

print(MENU, end='')
option = input()
while(option != "quit"):
    if(option == "authenticate"):
        AUTHENTICATED = True
        print("Authentication successful.\n> ", end='')
    elif(option == "getflag"):
        if(AUTHENTICATED == True):
            print(FLAG + "\n", end='')
            break
        else:
            print("You don't have the required permissions.\n> ", end='')
    elif(option == "help"):
        print("No help here.\n> ", end='')
    elif(option == "quit"):
        break
    else:
        print("Invalid command.\n> ", end='')
    option = input()