#! /usr/bin/env python3

# classes in pyton

class Duck:  # defining a calss 
    sound = "Quackkkkkkkkkkkkkkkkkkkkkk!" #defining variables in a class
    walking = "Quack walk quack walk!"
    
    def quack(self):  #defining functions in a class, here self is reference to the class. WE should prefer to use self for making code more redable
        print(self.sound)
    
    def walk(self):
        print(self.walking)
        

def main():
    mrDuck = Duck() # here we assign the duck class to mrDuck and now mrDuck acts as a object of Duck class
    mrDuck.walk()
    mrDuck.quack()
    
    
main() # calling the main method 