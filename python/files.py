#!/usr/bin/python
#Handling files
#From Google's python class
import sys

def Cat(filename):
    f = open(filename, 'rU')
    lines = f.read()
    print lines,
    f.close()

def main():
    Cat(sys.argv[1])

#Run the main function
if __name__ == '__main__':
    main()
