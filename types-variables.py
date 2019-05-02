#!/usr/bin/env python3

# we have various data types, lets see how the different type of datatypes/ built-in datatype works
x = 4
print(type(x)) # the output will be : <class 'int'>
y = 2.0
print(type(y))
z= "5.6"
print(type(z))
##########################################
# string object patterns, here string is a "Object" amd we can run methods on it
a = "Data type"  # there is no difference between '' or "" on python
print(type(a))
print(a.lower())
print(a.upper())
print("lets have positional arguments {}, {}".format(4,5)) # positional args placement