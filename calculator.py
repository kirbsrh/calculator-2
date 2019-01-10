"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

    #read input
    #tokenize input
    #if the first token is "q":
        #quit
    #else:
        #decide which math function to call based on first token

while True:
    user_entry = input("Please enter your calculation")
    tokens = user_entry.split(" ")
    if tokens[0] == tokens[0].startswith("q"):
        break
    else:
        if str(tokens[0]) == ("+"):
            add_answer=add(int(tokens[1]),int(tokens[2]))
            print(add_answer)

            

# Your code goes here
