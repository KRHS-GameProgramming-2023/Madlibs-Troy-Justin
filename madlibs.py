from screens import*
from Getter import*
from story1 import*
from story2 import*
from story3 import*

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
        elif choice == "2":
            print (Story2())
            print("\n")
            input ("Press Enter to Continue")
        elif choice == "3":
            print (Story3())
            print("\n")
            input ("Press Enter to Continue")
        elif choice == "gp":
            print ("i like game programming too")
            print("\n")
            input ("Press Enter to Continue")
    
        elif choice == "word":
            print ("bird is the word")
            print("\n")
            input ("Press Enter to Continue")
    
    
    
    
    
Madlibs (False)
