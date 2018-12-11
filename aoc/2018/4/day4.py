import os 
import sys
import string
import datetime
import re

sample = """[1518-10-31 00:58] wakes up
[1518-02-27 00:57] wakes up
[1518-04-05 00:03] falls asleep
[1518-06-03 00:18] falls asleep
[1518-08-06 00:39] falls asleep
[1518-08-15 00:54] falls asleep
[1518-03-07 00:00] falls asleep
[1518-05-01 00:12] falls asleep
[1518-06-17 00:53] wakes up
[1518-03-13 00:13] falls asleep
[1518-08-05 00:34] wakes up
[1518-11-23 00:57] wakes up
[1518-07-01 23:59] Guard #1301 begins shift
[1518-02-08 00:51] wakes up
[1518-11-10 00:59] wakes up
[1518-07-06 00:01] falls asleep
[1518-07-08 00:11] falls asleep
[1518-04-04 00:40] wakes up
[1518-04-26 00:04] wakes up
[1518-03-26 00:35] falls asleep
[1518-06-05 00:33] falls asleep
[1518-07-25 23:56] Guard #433 begins shift
[1518-10-20 00:33] wakes up
[1518-02-05 00:44] falls asleep
[1518-02-15 00:58] wakes up
[1518-03-20 00:51] wakes up
[1518-11-02 00:36] wakes up
[1518-03-05 23:46] Guard #401 begins shift
[1518-05-31 00:39] wakes up
[1518-09-11 00:09] falls asleep
[1518-04-15 00:39] wakes up
[1518-09-20 23:58] Guard #1877 begins shift"""

dataset = sample.split('\n')

for line in dataset:
    print(re.search(r"(?<=\[)(.*)(?=\])",line).group(0))

newSet = sorted(dataset, key=lambda x: re.search(r"(?<=\[)(.*)(?=\])",x).group(0))

print(newSet)