# Whitespace

# Suppose a WORD is any number of characters EXCEPT < > or space. 
# A WORD token should leave its value unchanged.

# Submit a definition for t_WORD.
import re

def t_WORD(token):
    r'(?:[^(?:<|>| )])+' #could also be: r'[^\<\> ]+'
    return token