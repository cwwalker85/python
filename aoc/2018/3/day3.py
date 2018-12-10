import os 
import itertools
import sys
import string

# sample = """#1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2"""

data = []

with open('inputs.txt') as f:
    for line in f:
        data.append(line)

# sampleArr = sample.split('#')
# for line in sampleArr:
#     data.append(line)

# data.pop(0)

allData = []

for i in data:
    areaArr = i.split(' ')
    areaLen = len(areaArr)

    # starting coordinate
    starting = areaArr[2].split(',')
    startingX = int(starting[0])
    startingY = int(starting[1].replace(':',''))

    dimensions = areaArr[3].split('x')
    dimX = int(dimensions[0])
    dimY = int(dimensions[1].replace('\n',''))

    # ending coorindate
    endingX = startingX + dimX
    endingY = startingY + dimY

    print(areaArr)
    print(str(startingX) + ',' + str(startingY) + ' through ' + str(endingX) + ',' + str(endingY))
    
    # building matrix for plot overlaps
    if (len(allData) == 0):
        for a in range(1000): # Vertical Rows
            col = []
            for b in range(1000): # Horizontal Columns
                col.append(0)
            allData.append(col)

    for c in range(len(allData)):
        if (startingY >= c and c <= endingY):
            
            for d in range(len(allData[c])):
                if (startingX >= d and d <= endingX):
                    allData[c][d] += 1

print(allData)
