# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.
 
# One possible solution, using the 
# mathematical notion a powerset
def subsets(l):
    if not l: return [[]]
    return subsets(l[1:]) + [[l[0]] + x for x in subsets(l[1:])]
 

# Another possible solution:
def sublists(big_list, selected_so_far):
    '''
    big_lists shrinks
    selected_so_far may get bigger
    '''
    # Base case:
    if big_list == []:
        print selected_so_far
    else:
        current = big_list[0]
        rest_of_big_list = big_list[1:]
        sublists(rest_of_big_list, selected_so_far + [current])
        sublists(rest_of_big_list, selected_so_far)
        
        
# Same as second solution
# but returning the result instead
def sublists(big_list, selected_so_far):
    '''
    big_lists shrinks
    selected_so_far may get bigger
    '''
    # Base case:
    if big_list == []:
        return [selected_so_far]
    else:
        current = big_list[0]
        rest_of_big_list = big_list[1:]
        return sublists(rest_of_big_list, selected_so_far + [current]) + \
        sublists(rest_of_big_list, selected_so_far)