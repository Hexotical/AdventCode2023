import sys
inFile = sys.argv[1]
with open(inFile, 'r') as i:
    #lines = i.readlines()
    lines = [line.strip() for line in i]

#Line 1 is a special case where I look down, otherwise, i should
#just look up don't really need other ways to look
'''
toRet = 0
#Line one is a special case, make a new array that only has symbols

lines = lines[0:2]
for lineNum, line in  enumerate(lines):
    curNum = ''
    isValid = False
    newPrev = []
    for index, character in enumerate(line):
        if character.isdigit():
            curNum += character
            isValid = checkAdjacency(lineNum, index, lines)
        else:
            if isValid:
                toRet += int(curNum)
                isValid = False
            curNum = ''
print(toRet)
'''




def checkAdjacency(lineNum, index, lines):
    #print(lines[lineNum][index], lineNum, index)
    #Check left
    if index > 0:
        toCheck = lines[lineNum][index-1]
        if not toCheck.isdigit() and toCheck != '.':
            print('left')
            return True #Left

    #Check above
    if lineNum > 0:
        toCheck = lines[lineNum-1][index]
        if not toCheck.isdigit() and toCheck != '.':
            print("above")
            return True
        

    #Check below
    if lineNum < len(lines)-1:
        #print("Checks below")
        toCheck = lines[lineNum+1][index]
        if not toCheck.isdigit() and toCheck != '.':
            print('below')
            return True
    
    #Check right
    if index < len(lines[0])-1:
        toCheck = lines[lineNum][index+1]
        if not toCheck.isdigit() and toCheck != '.':
            print('right')
            return True

    #Upper left
    if index > 0 and lineNum > 0:
        toCheck = lines[lineNum-1][index-1]
        if not toCheck.isdigit() and toCheck != '.':
            print('u left')
            return True
    
    #Upper right
    if index < len(lines[0])-1 and lineNum > 0:
        toCheck = lines[lineNum-1][index+1]
        if not toCheck.isdigit() and toCheck != '.':
            print("u right")
            return True

    #lower right
    if index < len(lines[0])-1 and lineNum < len(lines) -1:
        toCheck = lines[lineNum+1][index+1]
        if not toCheck.isdigit() and toCheck != '.':
            print('l right')
            return True

    #Lower left 
    if index > 0 and lineNum < len(lines) -1:
        toCheck = lines[lineNum+1][index-1]
        if not toCheck.isdigit() and toCheck != '.':
            print('l left')
            return True
    
    return False


        



toRet = 0
#Line one is a special case, make a new array that only has symbols

#print(lines)
for lineNum, line in  enumerate(lines):
    curNum = ''
    isValid = False
    newPrev = []
    for index, character in enumerate(line):
        if character.isdigit():
            curNum += character
            if not isValid:
                isValid = checkAdjacency(lineNum, index, lines)
            #print(curNum, isValid)
            if index == len(line)-1 and isValid:
                toRet += int(curNum)
                isValid = False
                print(curNum)
        else:
            if isValid:
                toRet += int(curNum)
                isValid = False
                print(curNum)
            curNum = ''
if isValid:
    toRet += int(curNum)
print(toRet)

#Part 2

#asterisks that are adjacent to two numbers

#I mean i should just find the asterisks and then check right?
def connectTheNum(lineNum, index, lines):
    #Guaranteed that lineNum, index is a digit
    toRet = []

    while index > 0 and lines[lineNum][index-1].isdigit():
        index -= 1
        #Gets me to the beginning of the digit
    #print(lineNum, index, len(lines), len(lines[0]))
    while index < len(lines[0]) and lines[lineNum][index].isdigit(): 
        toRet.append((lineNum, index))
        index += 1 
    print(toRet)
    return tuple(toRet)

def isValid(i, v, lines):
    if i >= 0 and i < len(lines[0]) and v >= 0 and v < len(lines):
        return True
    else:
        return False
#DICTIONARY WOOOO


def calculateGearRatio(lineNum, index, lines):
    dirs = [(1,1),(1,0), (0,1), (1, -1), (0, -1), (-1,1), (-1,0), (-1,-1)]
    gearsAdjacent = set()
    for dir in dirs:
        if isValid(lineNum+dir[0], index+dir[1], lines):
            if lines[lineNum+dir[0]][index+dir[1]].isdigit():
                print(lineNum+dir[0], index+dir[1])
                gearsAdjacent.add(connectTheNum(lineNum+dir[0], index+dir[1], lines))
    gearRatio = 1
    print(gearsAdjacent)
    if len(gearsAdjacent) == 2:
        for indices in gearsAdjacent:
            if not indices:
                continue
            #Otherwise buildNum
            num = ''
            for index in indices:
                num += lines[index[0]][index[1]]
            print(num)
            gearRatio *= int(num)

       # for val in gearsAdjacent:

            #gearRatio *= val
        return gearRatio 
    else:
        return 0

toRet = 0
for lineNum in range(len(lines)):
    for index in range(len(lines[0])):
        if lines[lineNum][index] == '*':
            toRet += calculateGearRatio(lineNum, index, lines)
print(toRet)





