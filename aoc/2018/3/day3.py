import os 
import itertools
import sys
import string

data = []

with open('inputs.txt') as f:
    for line in f:
        data.append(line)


# part 1
allData = []
counter = 0

# building matrix for plot overlaps
if (len(allData) == 0):
    for a in range(1000): # Vertical Rows
        col = []
        for b in range(1000): # Horizontal Columns
            col.append(0)
        allData.append(col)

for i in data:
    areaArr = i.split(' ')
    areaLen = len(areaArr)

    starting = areaArr[2].split(',')
    startingX = int(starting[0])
    startingY = int(starting[1].replace(':',''))

    dimensions = areaArr[3].split('x')
    dimX = int(dimensions[0])
    dimY = int(dimensions[1].replace('\n',''))

    for y in range(startingY,startingY+dimY):
        for x in range(startingX,startingX+dimX):
            allData[y][x] += 1

for a in allData:
    for b in a:
        if (b >= 2):
            counter += 1

print(allData)
print(counter)




# part 2
for i in data:
    areaArr = i.split(' ')
    areaLen = len(areaArr)

    starting = areaArr[2].split(',')
    startingX = int(starting[0])
    startingY = int(starting[1].replace(':',''))

    dimensions = areaArr[3].split('x')
    dimX = int(dimensions[0])
    dimY = int(dimensions[1].replace('\n',''))

    flag = True

    for y in range(startingY,startingY+dimY):
        for x in range(startingX,startingX+dimX):
            if (allData[y][x] > 1):
                flag = False

    if (flag == True):
        print(i)