import sys
inFile = sys.argv[1]

with open(inFile, 'r') as i:
    lines = [line.strip() for line in i]
#print(lines)
def findLocation(seed):
    found = False
    cur_val = int(seed)
    #print(seed)
    for line in lines[1:]:

        if 'map' in line:
            #print(line)
            found = False
            continue
        if not line or found:
            continue
        possible = line.split(" ")
        #Destination, Source, Amount
        if int(possible[1]) + int(possible[2]) >= cur_val and cur_val >= int(possible[1]):
            #Then This is the mapping i want
            #print(cur_val, line)
            found = True
            mapped_to = cur_val - int(possible[1]) + int(possible[0])
            cur_val = mapped_to
            #print(cur_val)
        #else:
            #print(line, "Cur val not found ", cur_val)
    return cur_val


    #for line in lines
#Lowest location number that corresponds to any initial seed
seeds = lines[0].split(':')[1:][0].split(" ")[1:]
#print(seeds)
def partOne():
    min_location = findLocation(seeds[0])
    for seed in seeds:
        location = findLocation(seed) 
        if location < min_location:
            min_location = location
    print(min_location)



def buildMap():
    toRet = []
    curDict = {}
    for line in lines[1:]:
        if 'map' in line:
            toRet.append(curDict)
            curDict = {}
        elif line:
            #Destination, Source, Amount
            possible = line.split(" ")
            for i in range(int(possible[2])):
                curDict[int(possible[1]) + i] = int(possible[0]) + i
    return toRet


def buildMapReverse():
    toRet = []
    curDict = {}
    for line in lines[1:]:
        if 'map' in line:
            toRet.append(curDict)
            curDict = {}
        elif line:
            #Destination, Source, Amount
            possible = line.split(" ")
            for i in range(int(possible[2])):
                curDict[int(possible[0]) + i] = int(possible[1]) + i
    return toRet

def findLocationSmart(seed, mapList):
    #print("Original seed: ", seed)
    for map in mapList:
        #print(seed, map)
        if seed in map:
            seed = map[seed]
    return seed

'''
def partTwo():
    mapList = buildMap()
   # print(findLocationSmart(13, mapList))
    min_location = findLocationSmart(int(seeds[0]), mapList)
    #print(mapList)
    #print(seeds)
    
    for i in range(0, len(seeds)-1, 2):
        print(seeds[i])
        for j in range(int(seeds[i+1])):
            location = findLocationSmart(int(seeds[i]) + j, mapList)
            if location < min_location:
                print(int(seeds[i]) + j, min_location)
                min_location = location
    print(min_location)
    
'''
#partOne()
#partTwo()
#Don't be dumb and just index the map, that'll be faster or multithread, hashmap is the way to go though

#Part two is dumb as fuck because the map is impossibly big
#What else should I do?
def partTwoRev():

