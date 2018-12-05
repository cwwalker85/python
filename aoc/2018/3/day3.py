import os 
import itertools
import sys
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
string = open('inputs.txt').read()

def checkCase(c):
    val = ''
    if (c.isupper()): val = c.lower()
    else: val = c.upper()
    return val

found = True
while (found == True):
    found = False

    for i in alphabet:
        checkChar = i + checkCase(i)
        startPosition = string.find(checkChar)
        
        if (startPosition > -1):            
            string = string[:startPosition] + string[startPosition+2:]
            found = True


print(len(string))