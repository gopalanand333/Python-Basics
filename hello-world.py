#! /usr/bin/env python3
# here to comment we use '#' followed by the comment message

print ("Hello World!") # this will write Hello World In console
# let's format and run again .format is method of string object
x = 42
print("hey this is var= {}".format(x)); # This will write hey this is var= 42 in console
# since format is method of string object. Let's see what happens
s = "hey this is var= {}".format(x)
print(s) # this will give the same output- hey this is var= 42
# another way to print 
print(f"var x = {x}") # Here f is the format string function and does the same thing as done in line number 7 or 9
