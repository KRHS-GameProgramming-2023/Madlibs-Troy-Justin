from Getter import *

def Story2(debug = False):
    if debug: print ("Story2 Function")
    
    print ("\n")
    sport1 = getSport("Enter a sport: ", debug)
    friendName1 = getWord("Enter a name: ", debug)
    numbertime1 = getNumbertime("Enter a time: ", debug)
    timeofday1 = getTimeofday("Enter a word time of day: ", debug)
    
    
    out = "\n"
    out += " We were out playing " + sport1
    out += " One day, my friend " + friendName1 + " and I! " 
    out += " It was around " + numbertime1 + " in the " + timeofday1 + " when shit hit the fan. "
    
    
    
    return out

