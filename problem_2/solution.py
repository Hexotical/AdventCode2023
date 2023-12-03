RED = 12
BLUE = 14
GREEN = 13

import sys
inFile = sys.argv[1]
with open(inFile, 'r') as i:
    lines = i.readlines()

#Split on semi colons, then split on space

toRet = 0
gameCount = 0
for line in lines:
    gameCount += 1
    check = line.strip().split(':')
    check = check[1].split(';')
    gameFlag = True
    for round in check:
        round = round.split(',')
        for reveal in round:
            reveal = reveal.split(' ')
            #print(reveal)
            #index 1 is number, index 2 is color
            if reveal[2] == 'blue':
                if int(reveal[1]) > BLUE:
                    gameFlag = False
            elif reveal[2] == 'green':
                if int(reveal[1]) > GREEN:
                    gameFlag = False
            elif reveal[2] == 'red':
                if int(reveal[1]) > RED:
                    gameFlag = False
    if gameFlag:
        #print(gameCount)
        toRet += gameCount

print(toRet)

## Part 2 
powerRet = 0
for line in lines:
    minRed = 0
    minBlue = 0
    minGreen = 0
    check = line.strip().split(':')
    check = check[1].split(';')
    gameFlag = True
    for round in check:
        round = round.split(',')
        for reveal in round:
            reveal = reveal.split(' ')
            #print(reveal)
            #index 1 is number, index 2 is color
            if reveal[2] == 'blue':
                if int(reveal[1]) > minBlue:
                    minBlue = int(reveal[1])
            elif reveal[2] == 'green':
                if int(reveal[1]) > minGreen:
                    minGreen = int(reveal[1])
            elif reveal[2] == 'red':
                if int(reveal[1]) > minRed:
                    minRed = int(reveal[1])
    print(minRed, minBlue, minGreen)
    powerRet += minRed * minBlue * minGreen
print(powerRet)
        #print(gameCount)
