#!/usr/bin/env python3

# how the for loops work in python and the syntax

words = ["one", "two", "three", "four", "five"] # array of words

for i in words: 
    print(i) # this will print the value of words 

# let's try another example
for letters in "Python":
    print("the current letter is : ",letters) # this will print p,y,t,h,o,n in console
    
# now let's see how to print the index of loop(the current value of i as it is used frequently)

for index,letters in enumerate(words):  # you can either use extra variable to store the count or use the python's inbuild function
    print(index, " " ,letters)          # enumerate reduces the visual cutter by hiding the accounting for the indexes
    