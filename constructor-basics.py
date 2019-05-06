#! /usr/bin/env pyton3
# using constructors in python

class Animal:
    def __init__(self, type, name,sound):   # here self is the reference to the class object
        self._type = type  # _type refers to the treditional way of writing objects
        self._name = name
        self._sound = sound
        
    def type(self):
        return self._type
    
    def name(self):
        return self._name
    
    def sound(self):
        return self._sound
    
def print_animal(o):
        if not isinstance(o,Animal):
            raise TypeError("pring_animal(): requires an Animal")
        print("the {} is named {} and says {}  ." .format(o.type(),o.name(),o.sound()))   

def main():
    a0 =  Animal("kitten", "fluppy", "mewooow")
    a1 = Animal("duck", "skinny", "quack quack")
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal("human","meshed-up","slang"))
    
if __name__ == "__main__" : main()       
        