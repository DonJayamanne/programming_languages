# Bonus Practice: Find Max

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Given a list l and a function f, return the element of l that maximizes f.

# Assume:
#    l is not empty
#    f returns a number

# Example:

l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len

# Here I have implemented this function in a smany ways as I could think of

def f_maximiser(f, l):
    return max(l,key=f)

def f_maximiser_first(f, l):
    d =  {i: f(i) for i in l for i in l}
    return max(d, key=d.get)
  

def f_maximiser_third(f, l):
    return max(map(f, l))

def f_maximiser_fourth(f, l):
    return max([f(i) for i in l])

def f_maximiser_fifth(f, l):
    return (filter(lambda el: el == max(l,key=f), l))[0]

def f_maximiser_wes(f, l):
    best_element_sofar = None
    best_f_value_sofar = None
    for i in range(len(l)):
        elt = l[i]
        f_value = f(elt)
        if best_f_value_sofar == None or f_value > best_f_value_sofar:
            best_element_sofar = elt
            best_f_value_sofar = f_value
    return best_element_sofar
    
def lpos(word):
    return word.find('l')

print f-maximiser(lpos, l)

# A better way than lines 47 - 50 is:
print f_maximiser(lambda(word): word.find('l'), l)
    
print f_maximiser(f, l)


# Test cases (order, reverse order, random and empty)
print f_maximiser(f, [1, 2, 3, 4, 5])
print f_maximiser(f, [5, 4, 3, 2, 1])
print f_maximiser(f, [6, 3, 7, 1, 2])
print f_maxisiser(f, [])
