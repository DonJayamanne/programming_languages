# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

# My first answer:
def fsmsim_first(string, current, edges, accepting):
        if string == "":
            return current in accepting
        else:
            letter = string[0]
            if (current, letter) in edges:
                #print "The letter is %s" % letter
                #print "The string is %s" % string
                current = edges[(current, letter)]
                #print "Current is %d" % current
                string = string[1:]
                return fsmsim(string, current, edges, accepting)
            else:
                return False
 
def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        if (current, letter) in edges:
            return fsmsim(string[1:], edges[(current, letter)], edges, accepting)
        return False


# Wes's answer (pretty much the same):
def fsmsim_wes(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            destination = edges[(current, letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string, destination, edges, accepting)
        else:
            return False
        
print fsmsim("aaa111", 1, edges, accepting)
# >>> True
