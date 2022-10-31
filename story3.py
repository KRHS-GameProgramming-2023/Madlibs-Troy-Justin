from Getter import*

def Story3(debug = False):
    if debug: print ("Story3 Function")
    
    print ("\n")
    season1 = getSeason("Enter a season: ", debug)
    friendName1 = getWord("Enter a name: ", debug)
    pet1 = getPet("Enter a pet: ", debug)
    age1 = getAge("Enter an age: ", debug)
    genre1 = getGenre("Enter a music genre: ", debug)
    holiday1 = getHoliday("Enter a holiday: ", debug)
    familymember1 = getfamilymember("Enter a family honerific like Dad or Cousin: ", debug)
    Fish1 = getFish("Enter a fish species: ", debug)
    
    
    
    out = "\n"
    out += " It was a beautiful " + season1
    out += " day,"
    out += " my friend " + friendName1
    out += " and I were taking a walk in the park with our pet " + pet1
    out += " he was " + age1 
    out += " years old and loved walks"
    out += " each time we took a walk we listened to our favorite " + genre1 + " music "
    out += "my favorite holiday " + holiday1 + " was coming up and I was super excited about it" 
    out += " each year my " + familymember1 + " and I go fishing for " + Fish1
    
    
    return out
