import os 
import itertools
import sys

# part 1
data = []
with open('inputs.txt') as f:
    for line in f:
        data.append(int(line))

print(sum(data)) # printing the result for part 1

# part 2
start, seen = (0, set())

for item in itertools.cycle(data):
    start += item

    if start in seen:
        print(start) # printing the result of part 2
        sys.exit(0) # exit script
    else:
        seen.add(start)
