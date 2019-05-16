
# file handling in python

def main():
    f = open("file.txt","r")  # this opens the file in read mode by default, the scond arg can be used to chagne the mode open("filename","r")
    for line in f:
        print(line.rstrip()) # removes any white line

if __name__ == "__main__": main()