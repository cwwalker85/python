import os
import sys

dataSet = set()




#part 1
twos = 0
threes = 0

with open('inputs.txt') as f:
    for line in f:
        dataSet.add(line)

for line in dataSet:
    seen = set()
    results = set()

    for i in range(len(line)):
        if (line[i]) in seen:
            count = line.count(line[i])
            if count == 3: results.add(3)
            if count == 2: results.add(2)

        else:
            seen.add(line[i])

    if 3 in results: threes += 1
    if 2 in results: twos += 1

print(threes * twos)




#part 2
for entry in dataSet: # grabs entry from the dataset to begin comparison
    
    for newEntry in dataSet: # for each letter in entry loop through all entries for difference
        if entry != newEntry:
            difference = 0
            for i in range(len(entry) - 1): # loop through by letter    
                if entry[i] != newEntry[i]:
                    difference += 1

            if difference < 2:
                print(entry) 
                print(newEntry)
                print('---')