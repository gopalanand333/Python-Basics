# using python modules

import  sys  # this imports the sys module
import random  # module to import random module

def main():
    v = sys.platform   # the imported module is used here
    print(v)
    r =random.randint(1000,25000)
    print(r)
    
if __name__ == "__main__": main()