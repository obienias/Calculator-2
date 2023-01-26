"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#read input


while True:
    input_String = input("What equation do you want to do?")
    tokens = input_String.split(' ')
    valid_inputs = ["pow", "+", "-", "*", "/", "square", "cube", "mod", "q"]
 
    # tokens[0] = 'pow'
    # tokens[1] = 'hi'
    # tokens[2] = '3'
    if tokens[0] == "q":
        break

    if tokens[0] not in valid_inputs:
        print("Your command is invalid")
        continue
    elif tokens[1].isnumeric()==False or tokens[2].isnumeric()==False:
        print("you should input numbers")
        continue
    elif tokens[1].isnumeric()==True and tokens[2].isnumeric()==True:
        for i in range(1, len(tokens)):
            #return int(tokens[i])
            tokens[i] = int(tokens[i])
            
    print(tokens)        

    if tokens[0] == "pow":
        print(power(tokens[1], tokens[2]))
    elif tokens[0] == "+":
        print(add(tokens[1], tokens[2]))
    elif tokens[0] == "-":
        print(substract(tokens[1], tokens[2]))
    elif tokens[0] == "*":
        print(multiply(tokens[1], tokens[2]))
    elif tokens[0] == "/":
        print(divide(tokens[1], tokens[2]))
    elif tokens[0] == "square":
        print(square(tokens[1]))
    elif tokens[0] == "cube":
        print(cube(tokens[1]))
    elif tokens[0] == "mod":
        print(mod(tokens[1], tokens[2]))
    
#    tokenize input
#        if the first token is "q":
#            quit
#        else:
#            (decide which math function to call based on first token)
#            if the first token is 'pow':
#                  call the power function with the other two tokens
#
#            (...etc.)