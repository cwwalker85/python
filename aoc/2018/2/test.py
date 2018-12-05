data = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

dataList = data.splitlines()

for line in dataList:
    print(line)
    for line2 in dataList:
        if (line != line2):
            print(line2)
            for i in range(len(line)-1):
                if(line[i] == line2[i]):
                    print(line[i])

    print('---')
    print('---')
    print('---')