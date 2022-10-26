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
        



def getWord(prompt, debug = False):
    if debug: print ("getWord Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word

def getClass(prompt, debug = False):
    if debug: print ("getClass Function")

    goodInput = False
    
    classes = ["english",
              "math", 
              "spanish",
              "history",
              "science",
              "gym",
              "programming"]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in classes:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word

    
def getCandy(prompt, debug = False):
    if debug: print ("getCandy Function")

    goodInput = False
    candy = ["reeses",
              "snickers", 
              "twix",
              "baby ruth",
              "milky way",
              "butterfinger",
              "crunch",
              "hershey",
              "almond joy",
              ]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in candy:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word

def getFastFood(prompt, debug = False):
    if debug: print ("getFastFood Function")

    goodInput = False
    
    Places = ["mcdonalds",
              "wendys", 
              "dairy queen",
              "canes",
              "taco bell",
              "subway",
              "pizza chef",
              "dominos",
              "pizza hut"
              ]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in Places:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word

def getColor(prompt, debug = False):
    if debug: print ("getColor Function")

    goodInput = False
    
    colors = ["red",
              "yellow", 
              "blue",
              "green",
              "purple",
              "black",
              "white",
              "orange",
              ]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in colors:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word

def getSport(prompt, debug = False):
    if debug: print ("getSport Function")

    goodInput = False
    
    sports = ["soccer",
              "baseball", 
              "hockey",
              "football"]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in sports:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
def getfamilymember(promt, debug = False):
    if debug: print ("getfamilymember Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
def getnameoffamilymember(promt, debug = False):
    if debug: print ("getnameoffamilymember Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
def getpetspeicesname(promt, debug = False):
    if debug: print ("getpetspeicesname Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
def getObject(promt, debug = False):
    if debug: print ("getObject Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
    
def getpetname(promt, debug = False):
    if debug: print ("getpetname Function")

    goodInput = False
    
    
    while not goodInput:
        word = input(promt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
            
    return word
    
def getNumbertime(promt, debug = False):
    if debug: print ("getNumbertime Function")

    goodInput = False
    
    numberTime = ["1",
                 "2",
                 "3", 
                 "4",
                 "5",
                 "6",
                 "7",
                 "8",
                 "9",
                 "10",
                 "12",
            ]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in numberTime:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word
    
def getTimeofday(prompt, debug = False):
    if debug: print ("getTimeofday Function")

    goodInput = False
    
    Timeofday = ["morning",
                 "day",
                 "noon", 
                 "afternoon",
                 "midnight",
                 "night",
            ]
    
    while not goodInput:
        word = input(prompt)
        
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Don't use laguage like that")
        elif word.lower() not in Timeofday:
            goodInput = False
            print("Sorry, I don't know that one.")
            
    return word

def getState(prompt, debug = False):
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
        word = input(prompt)
        
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
