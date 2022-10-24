from Getter import *

def Story1(debug = False):
    if debug: print ("Story1 Function")
    
    print ("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    neighborName1 = getWord("Enter a different name: ", debug)
    State1 = getState("Enter a state: ", debug)

    
    out = "\n"
    out += "One day me and my friend " + friendName1
    out += " were out playing " + sport1
    out += " Then we saw our neighbor " + neighborName1 
    out += " and they decided to come play with us "
    out += " we all just happened to live in " + State1
    out += " and we were the best of friends "
    
    
    return out
