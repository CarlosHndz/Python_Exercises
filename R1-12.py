'''
Python's random module includes a function choice(data) that returns a random
element from a non-empty sequence. The random module includes a more basic 
function "randrange", with parameterization similar to the built-in range
function, that return a random choice from the given range. Using only the 
"randrange" function, implement your own version of the choice function.
'''

import random

def new_choice(data):
    seq_length = len(data)
    return random.randrange(0, seq_length)

# Compare the new_choice function to the choice function
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(data))
print(new_choice(data))
    