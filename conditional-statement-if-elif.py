#! usr/bin/env python3
# let's see how the print statement works here on python.

x =  43
y = 33

if x < y :              # the if is executed
    print(f"x < y")
elif x > y:             # here elif works likge else-if
    print("elif block is executed")
elif x == y:
    print(" x = y")
else: 
    print("the if condition failed")