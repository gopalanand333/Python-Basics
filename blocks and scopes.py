#! /usr/bin/env python3

# using blocks and scope. Here we can see how indentation works as a scope for function

x = 10
y = 33

if x < y:
    print(f"x>y: x is {x} and y is {y}")
    print("indentation is working still in if")
    
    
    print("white spae dont make much difference in python. Scope will be same")
    
print("since we are out of the indentation from if's level we will be out of if scope")

# check the terminal, try changing the conditions and check the output 