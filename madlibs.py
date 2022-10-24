#troywashere
from screens import *
from Getter import *
from story1 import *


def Madlibs (debug = False):
    if debug: print ("Welcome to Debug")
    
    print (TitleScreen(debug))
    input ("Press Enter to Continue")
    
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
    
        if choice == "q":
            exit()
        elif choice == "1":
            print (Story1())
            print("\n")
            input ("Press Enter to Continue")
    
    
    
    
    
    
    
    
Madlibs (False)
