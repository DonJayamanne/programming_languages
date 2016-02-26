# Learning Regular Expressions

# Define a variable regexp that matches the left 3 strings but not the right 3.

#   Yes     No
#   aaa    aabbb
#   abb    aaccc
#   acc     bc


regexp = r"a(?:(?:aa)|(?:bb)|(?:cc))"

# Slightly better:
regexp2 = r"a*(?:(?:bb)|(?:cc))"

import re 

tests = [("aaa", True), ("abb", True), ("acc", True), ("aabbb", False), ("aaccc", False), ("bc", False)]

for r, ans in tests:
    print (re.findall(regexp, r) == [r]) == ans
