import os 
import sys
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

data_set = sample.split('\n')

# Sort list of all entries by date
new_set = sorted(data_set, key=lambda x: re.search(r"(?<=\[)(.*)(?=\])", x).group(0))

all_guards = []  # All guard objects
seen = []  # All unique guard ids
idRegex = r"(?<=Guard #)(.*)(?= begins)"

# finds each unique guard and adds them to the all guards list
for entry in new_set:
    if entry.find('Guard') > -1:
        guard_id = re.search(idRegex, entry).group(0)
        if guard_id not in seen:

            class Guard(object):
                id = guard_id
                entries = []
                timeAwake = []

            all_guards.append(Guard)
            seen.append(guard_id)


# id of guard in all guards by id found in the loop
def find_guard(gid):
    for i in range(len(all_guards)):
        if all_guards[i].id == gid:
            return i


current_guard = ''

# loops through all entries and adds them to their respective guard objects
for line in new_set:
    if line.find('Guard') > -1:
        guard_id = re.search(idRegex, line).group(0)
        current_guard = find_guard(guard_id)
        continue
    else:
        if current_guard != '':
            all_guards[current_guard].entries.append(line)

# loop through all guard time entries and finds the time awake and the overlap

highest = 0
laziest = 0

for j in range(len(all_guards)):

    awake = [0] * 60
    range_start = -1
    range_end = -1

    for k in all_guards[j].entries:
        this_minute = int(k[15:17])

        if k.find('falls') > -1:
            range_start = this_minute

        elif k.find('wakes') > -1:
            range_end = this_minute

            for l in range(range_start,range_end):
                awake[l] += 1

                if awake[l] > highest:
                    highest = awake[l]
                    laziest = all_guards[j].id

    print(awake)

print(str(laziest) + ': ' + str(highest))
