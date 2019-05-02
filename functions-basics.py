#!/usr/bin/env python3 
#example of using functions in python 

def theFunctionName(args): # here def is used to define a funcation, the function can accept arguments specified in parenthisis which can be used as variable later
    print(args) # here args is the function argument which can now be used as a variable 

def theFuncationNameTwo( n = 1):  # assigning default value to the function's argument 
    print(n)

# All functions in python return a value. 
def theRetrnValue():
    a = 10
    print(a)
    return a

# let's call the function
theFunctionName("argument") #we are passing value 333 from the funcation  all, this will be recieved as a argument in the function and then the function's codeblock is executed
theFuncationNameTwo() # passing no argument, the default value is used the the function

b = theRetrnValue() # the function is called that will return the value assigned in return statement of theReurnValue() method and stored in b
print(f"the returned value {b}")
