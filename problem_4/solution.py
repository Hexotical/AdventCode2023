import sys
inFile = sys.argv[1]

with open(inFile, 'r') as i:
    lines = [line.strip() for line in i]
#print(lines)
toRet = 0
cards = {}
for i in range(len(lines)):
    cards[i] = 1

def scoreCalc(line):
    #for line in lines:
    line = line.split(':')[1:]
    #print(line)
    line = line[0].split('|')
    winningNumbers = line[0].split(' ')
    myNumbers = line[1].split(' ')
    #print(winningNumbers, myNumbers)
    myNumbers = set(myNumbers)
    winner = False
    score = 0
    for number in myNumbers:
        if number.isdigit() and number in winningNumbers:
            #print(number)
            if winner:
                score += 1
            else:
                score = 1
                winner = True
    #print(score)
    return score 

#Looking for total scratchers

for i in range(len(lines)):
    winnings = scoreCalc(lines[i])
    #print(winnings)
    if winnings == 0:
        continue

    for j in range(i+1, i+winnings+1):
        if j>=len(lines):
            continue
        cards[j] += 1 * cards[i]
    print(i, cards)
print(cards)

toSum = 0
for i in range(len(lines)):
    toSum += cards[i]
    
print(toSum)
#print(toRet)

