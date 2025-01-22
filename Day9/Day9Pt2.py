#should find how long a 
def findLength(list, indx, forward):
    length = 0
    value = list[indx]
    while list[indx] == value:
        length += 1
        if forward:
            indx += 1
        else:
            indx -= 1
    return length

file = open(".\\Day9\\input2.txt")
count = 0
fileAsString = file.read()
list = []
fileLengths = {} #dictionary that stores file IDs and their length, should save time
for x in fileAsString:
    num = int(x)
    if count % 2 == 0: #then its a file block
        for z in range(num):
            fileID = int(count / 2) #needs to be cast to int because of int division
            list.append(fileID)
            fileLengths.update({fileID:z})
    else: #then its a blank block
        for z in range(num):
            list.append('.')
    count += 1

listCopy = list.copy() #I just like to keep the original list around just in case I dont wanna hear it
reversedIndx = len(listCopy) - 1 #keeps track of index as we traverse backwards through the list

print(reversedIndx)
while reversedIndx > 0:
    print(listCopy)
    fwdIndx = 0
    fileID = listCopy[reversedIndx]
    if fileID != '.': # and fwdIndx <= reversedIndx <-this shouldnt matter
        print("reversedIndx is " + str(reversedIndx))
        lengthOfFile = findLength(listCopy, reversedIndx, False)
        print("reversedIndx is " + str(reversedIndx))
        print()
        print("lengthOfFile is " + str(lengthOfFile))
        while fwdIndx < reversedIndx and :
            lengthOfDots = 0
            while listCopy[fwdIndx] != '.' and fwdIndx < reversedIndx: # i feel like this suckssss
                fwdIndx += 1
            startOfDots = fwdIndx
            while fwdIndx < reversedIndx and listCopy[fwdIndx] == '.':
                lengthOfDots += 1
                fwdIndx += 1
            print("lengthOfDots is " + str(lengthOfDots))
            print("number trying to move is " + str(fileID))
            if lengthOfDots >= lengthOfFile:
                #swap blank blocks with numbered blocks
                while listCopy[reversedIndx] == fileID:
                    listCopy[startOfDots] = listCopy[reversedIndx]
                    listCopy[reversedIndx] = '.'
                    reversedIndx -= 1
                    startOfDots += 1
                print(listCopy)
            fwdIndx += 1
        #im actually not sure i understand the instructions       
        
        #find next numbered block from end of the list
        #while listCopy[reversedIndx] == '.':
        #    reversedIndx -= 1
    print(listCopy)
    reversedIndx -= 1
print(listCopy)
print()
checkSum = 0
for x in range(len(listCopy) - 1):
    if listCopy[x] != '.':
        checkSum += x * int(listCopy[x])
print("checkSum is: " + str(checkSum))
file.close()