import sys
inFile = sys.argv[1]

sol = 0
with open(inFile, 'r') as i:
    lines = i.readlines()
#print(lines)
nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
lolDict = {'one':'1', 'two':'2','three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7','nine':'9', 'eight':'8'}
stringNums = ['two', 'one','three','four','five','six','seven','nine', 'eight']

for line in lines:
    print(line)
    #Stupid circular thing where one needs to be before eight, eight needs to be before two, two needs to be before one
    #The really stupid thing to do is just compare the next characters that would appear, do the stupid easy way back at home or desk, away from the shitty lacroix
    #newLine = ''
    
    #for key in stringNums:
        #order matters in replacement so how do I check for that
        #one three eight nine
        #seven nine
        
        #line = line.replace(key, lolDict[key])
        

    #print(line)

    #This is infuriating, theres an edge case where i have 1twone where Im dumb as fuck and do 12ne as the thing which means i should condition the stupid cases
    #oneight
    #twone
    #threeight
    #fiveight
    #sevenine
    #eightwo
    #nineight
    first = -1
    flag = False
    mostRecent = -1
    c = 0
    while c < len(line):
        val = -1
        char = line[c]
        if line[c] in nums:
            val = line[c]
        elif char == 't':
            if line[c:c+5] == 'twone':
                if flag:
                    val = '1'
                else:
                    val = '2'
                c += 4
            elif line[c:c+3] == 'two':
                val = '2'
                c += 2
            elif line[c:c+5] == 'three':
                val = '3'
                c += 4
        elif char == 'o':
            if line[c:c+7] == 'oneight':
                if flag:
                    val = '8'
                else:
                    val = '1'
                c += 6
            elif line[c:c+3] == 'one':
                val = '1'
                c += 2
        elif char == 'f':
            if line[c:c+8] == 'fiveight':
                if flag:
                    val = '8'
                else:
                    val = '5'
                c += 7
            elif line[c:c+4] == 'four':
                val ='4'
                c += 3
            elif line[c:c+4] == 'five':
                val = '5'
                c += 3
        elif char == 'n':
            if line[c:c+8] == 'nineight':
                if flag:
                    val = '8'
                else:
                    val = '9'
                c += 7
            elif line[c:c+4] == 'nine':
                val = '9'
                c += 3
        elif char == 's':

            if line[c:c+3] == 'six':
                val = '6'
                c += 2
            elif line[c:c+8] == 'sevenine':
                if flag:
                    val = '9'
                else:
                    val = '7'
                c += 7
            elif line[c:c+5] == 'seven':
                c +=4
                val = '7'
        elif char == 'e':
            if line[c:c+7] == 'eightwo':
                if flag:
                    val = '2'
                else:
                    val = '8'
                c += 6
            elif line[c:c+5] == 'eight':
                c += 4
                val = '8'

        #print(line[c], val)
        if val == -1:
            c += 1
            continue
        if not flag:
            first = val
            flag = True
        mostRecent = val
        c += 1
        
    toAdd = int(first + mostRecent)
    #print(toAdd)
    sol += toAdd
    print(toAdd)


print(sol)
