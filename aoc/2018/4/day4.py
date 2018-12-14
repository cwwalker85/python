import os 
import sys
import string
import datetime
import re

sample = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

dataset = sample.split('\n')

# Sort list of all entries by date
newSet = sorted(dataset, key=lambda x: re.search(r"(?<=\[)(.*)(?=\])",x).group(0))

allGuards = [] # All guard objects
seen = [] # All unique guard ids
idRegex = r"(?<=Guard #)(.*)(?= begins)"

# finds each unique guard and adds them to the allguards list
for entry in newSet:
    if (entry.find('Guard') > -1):
        guardID = re.search(idRegex,entry).group(0)
        if (guardID not in seen):

            class Guard(object):
                id = guardID
                entries = []
                timeAwake = []

            allGuards.append(Guard)
            seen.append(guardID)

# id of guard in allguards by id found in the loop
def findGuard(id):
    for i in range(len(allGuards)):
        if (allGuards[i].id == id):
            return i

currentGuard = ''

# loops through all entries and adds them to their respective guard objects
for line in newSet:
    if (line.find('Guard') > -1):
        guardID = re.search(idRegex,line).group(0)
        currentGuard = findGuard(guardID)
        continue
    else:
        if (currentGuard != ''):
            allGuards[currentGuard].entries.append(line)

print(str(allGuards[0].id) + ': ' + str(allGuards[0].entries))
print(str(allGuards[1].id) + ': ' + str(allGuards[1].entries))

# loop through all guard time entries and finds the time awake and the overlap
# for j in range(len(allGuards)):

