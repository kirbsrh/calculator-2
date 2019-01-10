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
        elif str(tokens[0]) == ("-"):
            subtract_answer=subtract(int(tokens[1]),int(tokens[2]))
            print(subtract_answer)
        elif str(tokens[0]) == ("*"):
            multiply_answer=multiply(int(tokens[1]),int(tokens[2]))
            print(multiply_answer)
        elif str(tokens[0]) == ("/"):
            divide_answer=divide(int(tokens[1]),int(tokens[2]))
            print(divide_answer)
        elif str(tokens[0]) == ("square"):
            square_answer=square(int(tokens[1]))
            print(square_answer)
                





            

# Your code goes here
