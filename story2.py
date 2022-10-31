from Getter import*

def Story2(debug = False):
    if debug: print ("Story2 Function")
    
    print ("\n")
    sport1 = getSport("Enter a sport: ", debug)
    friendName1 = getWord("Enter a name: ", debug)
    numbertime1 = getNumbertime("Enter a time: ", debug)
    timeofday1 = getTimeofday("Enter a word time of day: ", debug)
    familymember1 = getfamilymember("Enter a family honerific like Dad or Cousin: ", debug)
    nameoffamilymember1 = getnameoffamilymember("Enter Name of family member: ", debug)
    petspeicesname1 = getpetspeicesname ("Enter pet spices name: ", debug)
    petname1 = getpetname ("Enter pet name: ", debug)
    object1 = getObject ("Please Enter name of object: ", debug)
    
    
    
    
    
    out = "\n"
    out += "We were out playing " + sport1
    out += " One day, my friend " + friendName1 + " and I! " 
    out += " It was around " + numbertime1 + " in the " + timeofday1 + " when something tragic happened. "
    out += " We, or I should say I, got a call from my " + familymember1 + " " + nameoffamilymember1 + "."
    out += " Letting me know my " + petspeicesname1 + " " + petname1 + " had just passed away..."
    out += " I hung up the phone and just stared at a " + object1 + " " + friendName1 + " came over and gently shook me."
    # ~ out += " The weeks leading up to the baril
    # ~ out += "
    # ~ out += "
    # ~ out += "

    
    return out

