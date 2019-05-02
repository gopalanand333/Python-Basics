#!/usr/bin/env python3

# this is a code sample of printing fibonacci series in python 
# a fibonacci series is made by summing the first two numbers to generate the next number(the first two can be called is previous two)

a,b = 0,1 # this is to say that we are starting from 1 the 0th element is 0 and first is 1
while b < 1000: 
    print(b,end = " ", flush = True) # flush clears the memory buffer
    a,b = b, a+b   # here a is assigned value of b which is now the previous number, b is assigned with the summation of a+b to act as the 2nd number 
    