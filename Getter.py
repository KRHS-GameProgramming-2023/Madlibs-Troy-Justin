def getMenuOption(debug = False):
    if debug: print ("getMenuOption Function")

    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or 
            option == "exit"): 
                option = "q"
                goodInput = True 
        elif (option == "1" or 
            option == "one" or 
            option == "story 1" or 
            option == "Story"): 
                option = "1"
                goodInput = True 
        elif (option == "2" or 
            option == "two" or 
            option == "story 2" or 
            option == "Story"): 
                option = "2"
                goodInput = True 
        else:
            print("Please make a valid choice")
            
    return option
        



def getWord(promt, debug = False):
    if debug: print ("getWord Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
    
def getSport(promt, debug = False):
    if debug: print ("getSport Function")

    goodInput = False
    
    sports = ["soccer",
              "baseball", 
              "hockey",
              "football"]
    
    while not goodInput:
        word = input(promt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
def getNumbertime(promt, debug = False):
    if debug: print ("getNumbertime Function")

    goodInput = False
    
    Time = ["1",
            "2", 
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            ]
    
    while not goodInput:
        word = input(promt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in Time:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
def getTimeofday(promt, debug = False):
    if debug: print ("getTimeofday Function")

    goodInput = False
    
    Timeofday = ["morning",
                 "noon", 
                 "afternoon",
                 "midnight",
                 
            ]
    
    while not goodInput:
        word = input(promt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in Timeofday:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False
    
    
    
swearList = ["poop",
             "pee",
             "pp",
             "poopy",
             "bitch",
             "pussy",
             "dick",
             "hoe",
             "fuck",
             "cunt",
             "dick"
             "ass",
             "asshole",
             "cunt",
             "dick wad",
             "mother fucker",
             "cock",
             "cock sucker",
             "fucker",
]
        
