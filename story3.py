from Getter import*

def Story3(debug = False):
    if debug: print ("Story3 Function")
    
    print ("\n")
    season1 = getSeason("Enter a season: ", debug)
    friendName1 = getWord("Enter a name: ", debug)
    pet1 = getPet("Enter a pet: ", debug)
    age1 = getAge("Enter an age: ", debug)
    
    
    
    
    
    
    out = "\n"
    out += " It was a beautiful " + season1
    out += " day,"
    out += " me and my friend " + friendName1
    out += " were taking a walk in the park with our pet " + pet1
    out += " he was " + age1 
    out += " years old and loved walks "
    
    
    return out
