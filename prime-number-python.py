#! /usr/bin/env python3

# this program will check for a given number is prime or not 

def isPrime(number):  # funcation declearation which recieves a number as argument
    if number <= 1:              #to validate the input 
        return False        
    for x in range(2,number): # this for loop test the number if its divisible by any other number than itself and 1, for efficeiency i have checked till half the range of number
        if number % x == 0:
            return False #the function returns true or false
    else:
        return True
    
    
n = 6
if(isPrime(n)):   # function to check prime is called and passed the number, it will return true/ false based  on the value of number
    print(f"the number: {n} is prime")
else:
    print(f"the number: {n} is not prime")

# re-using the functions
def list_Primes():  # this function will return prime numbers below 1000
    for n in range(1000): # range provices range of numbers . that is from range(1000)= 0-1000, range(10,20)= 10 to 20
        if isPrime(n):
            print(n, end =" ", flush=True)  # enters the number followed by white space and clears the memory buffer
    print()     # this prints a new line
        
        
# calling the list prime  method
list_Primes()