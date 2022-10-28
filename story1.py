from Getter import*

def Story1(debug = False):
    if debug: print ("Story1 Function")
    
    print ("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    neighborName1 = getWord("Enter a different name: ", debug)
    State1 = getState("Enter a state: ", debug)
    Class1 = getClass("Enter a class: ", debug)
    Candy1 = getCandy("Enter a candy bar: ", debug)
    FastFood1 = getFastFood("Enter a fast food chain: ", debug)
    Color1 = getColor("Enter a color: ", debug)

    
    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += " Then we saw our neighbor " + neighborName1 
    out += " and they decided to come play with us "
    out += "we all just happened to live in " + State1
    out += " and we were the best of friends "
    out += "one day we were all walking to our favorite class which was " + Class1
    out += " on our way to class we stopped at a vending machine and I got my favorite candy bar which is obviously " + Candy1
    out += " after class we all went and got food at " + FastFood1
    out += " on the drive to " + FastFood1
    out += " we almost hit another car we only saw it because of its bright " + Color1 
    out += " color"
    
    return out
