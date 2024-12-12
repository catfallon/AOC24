#I am just completely skipping around let's go

file = open(".\\Day11\\inputexample.txt")
blinks = 3;
rocks = file.read().split()
rocksCopy = rocks.copy()
for x in range(blinks):
    #then do stuff
    rockCount = 0
    
    for y in rocks: # wait this doesnt make sense because I have to do it again
        print("start of inside loop")
        print("rocksCount is " + str(rockCount))
        print("rocks is " + str(rocks))
        print("being turned into " + str(rocksCopy))
        print()
        if int(y) == 0:
            rocksCopy[rockCount] = "1"
        elif len(str(y)) % 2 == 0:
            #this is pretty crazy actually
            firstString = y[:int(len(y) / 2)]
            secondString = y[int(len(y) / 2):]
            #print(firstString)
            #print(secondString)
            print("before insertion, rocksCopy is " + str(rocksCopy))
            rocksCopy.insert(rockCount, firstString)
            #print("str is " + str(int(secondString)))
            
            print(rocksCopy)
            print("rockCount is " + str(rockCount))
            rocksCopy[rockCount] = str(int(secondString))
            rockCount += 1
            #not sure what to do about this actually
        else:
            rocksCopy[rockCount] = str(int(y) * 2024)
        rockCount += 1

    rocks = rocksCopy
    print(rocks)

    x += 1

print(rocksCopy)