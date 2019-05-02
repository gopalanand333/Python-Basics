#! /usr/bin/env python03
# a dictionary is searchable item with key-value pair
x = {"one": 1, "two":2, "three":3, "four":4,"five":5} # a  dictionary
for key in x:
    print(key)  # this will print the keys
    
for key, v in x.items():
    print('key: {} , value:{}'.format(key, v)) # this will return the key value pair
    