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
            print ("Don't use language like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
def getState(promt, debug = False):
    if debug: print ("getState Function")

    goodInput = False
#list from https://capitalizemytitle.com/50-us-states-in-alphabetical-order/
    states = ["Alabama",
            "Alaska",
            "Arizona", 
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"]
    
    while not goodInput:
        word = input(promt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use language like that")
        elif word.capitalize() not in states:
            goodInput = False
            if " " in word:
                words=word.split(" ")
                if len(words) == 2:
                    word=words[0].capitalize()+" "+words[1].capitalize()
                    if word in states:
                        return word
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
   
   
# ~ while True:
    # ~ getState(">")
