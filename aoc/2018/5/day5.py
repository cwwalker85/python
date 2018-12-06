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


# part 2

lower = []
upper = []
results = []

for i in alphabet:
    
    part2 = open('inputs.txt').read()
    found = True

    while (found == True):
    
        found = False
        checkChar = i + checkCase(i)
        startPosition = part2.find(checkChar)
        
        if (startPosition > -1):            
            part2 = part2[:startPosition] + part2[startPosition+2:]
            found = True

    if (i.islower() == True):
        lower.append(len(part2))
    else:
        upper.append(len(part2))
    
union = zip(lower,upper)

for pair in union:
    results.append(pair[0] + pair[1])

print(results)
print(min(results))