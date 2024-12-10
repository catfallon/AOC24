print("hello world")
file = open(".\\Day9\\input.txt")
count = 0
fileAsString = file.read()
list = []

for x in fileAsString:
    num = int(x)
    if count % 2 == 0: #then its a file block
        for z in range(num):
            list.append(int(count / 2))
    else: #then its a blank block
        for z in range(num):
            list.append('.')
        
    count += 1

listCopy = list.copy() #I just like to keep the original list around
reversedIndx = len(listCopy) - 1 #keeps track of index as we traverse backwards through the list
for x in range(len(listCopy) - 1):
    if x >= reversedIndx: #list should be done if we're meeting in the middle here
        break
    if listCopy[x] == '.' and x <= reversedIndx:
        #swap blank block with numbered block
        listCopy[x] = listCopy[reversedIndx]
        listCopy[reversedIndx] = '.'

        #find next numbered block from end of the list
        while listCopy[reversedIndx] == '.':
            reversedIndx -= 1

checkSum = 0
for x in range(len(listCopy) - 1):
    if listCopy[x] != '.':
        checkSum += x * int(listCopy[x])
print("checkSum is: " + str(checkSum))
file.close()