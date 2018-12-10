import os 
import itertools
import sys
import string



# part 1
alphabet = string.ascii_lowercase + string.ascii_uppercase
lowerSet = string.ascii_lowercase
string = open('inputs.txt').read()
original = open('inputs.txt').read()

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



# part 2
def removeChar(string,char):
    found = True
    newString = string

    while (found == True):
        found = False
        posLower = newString.find(char)
        posUpper = newString.find(char.upper())

        if (posLower > -1):
            found = True
            newString = newString.replace(char,'')

        elif (posUpper > -1):
            found = True
            newString = newString.replace(char.upper(),'')

    return newString

for c in lowerSet:
    newstring = removeChar(original,c)
    
    found = True
    while (found == True):
        found = False

        for i in alphabet:
            checkChar = i + checkCase(i)
            startPos = newstring.find(checkChar)
        
            if (startPos > -1):            
                newstring = newstring[:startPos] + newstring[startPos+2:]
                found = True

    print(c + ': ' + str(len(newstring)))

