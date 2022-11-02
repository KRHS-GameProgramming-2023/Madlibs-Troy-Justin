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
    number1 = getnumber ("Enter number between 1 and 24: ", debug)
    heorshe1 = getHeorshe ("Enter pets gender: ", debug)
    
    
    
    out = "\n"
    out += "We were out playing " + sport1
    out += " One day, my friend " + friendName1 + " and I! " 
    out += " It was around " + numbertime1 + " in the " + timeofday1 + " when something tragic happened. "
    out += " We, or I should say I, got a call from my " + familymember1 + " " + nameoffamilymember1 + "."
    out += " Letting me know my " + petspeicesname1 + " " + petname1 + " had just passed away..."
    out += " I hung up the phone and just stared at a " + object1 + " " + friendName1 + " came over and gently shook me."
    out += " The " + number1 + "weeks after the funeral was held," 
    out += " I ended up getting another pet named " + petname1 + " " + heorshe1 + " is a " + petspeicesname1 + " ."
    out += " My new pet will never fill the viod the other one left but it cures the lonlyness " + heorshe1 + " to worry about."

    
    return out

