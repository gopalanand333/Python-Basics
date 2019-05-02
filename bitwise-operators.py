# bitwise operators

x = 0x0a # hex value
y = 0x02

z = x&y
print(f"hex is {x:02x}, z is {z:02x}") # prints hex output
print(f"(bianry) x is {x:08b}, y={y:08b}") # prints binary output

####### Bitwise
z = x | y
print(f"(bianry) x is {x:08b}, y={y:08b}, z = {z:08b}") # prints binary output
z = x >> y
print(f"(bianry) x is {x:08b}, y={y:08b}, z = {z:08b}") # prints binary output
z = x << y
print(f"(bianry) x is {x:08b}, y={y:08b}, z = {z:08b}") # prints binary output