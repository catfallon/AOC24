#I am just completely skipping around let's go
import time
start_time = time.time()
file = open(".\\Day11\\input.txt")
blinks = 25
rocks = file.read().split()

for x in range(blinks):
    rockCount = 0
    rocksCopy = rocks.copy()
    for y in rocks:
        if int(y) == 0:
            if rockCount >= len(rocksCopy):
                rocksCopy.append("1")
            else:
                rocksCopy[rockCount] = "1"
        elif len(str(y)) % 2 == 0:
            firstString = y[:int(len(y) / 2)]
            secondString = y[int(len(y) / 2):]
            rocksCopy.insert(rockCount, firstString)
            rockCount += 1
            if rockCount >= len(rocksCopy):
                rocksCopy.append(str(int(secondString)))
            else:
                rocksCopy[rockCount] = str(int(secondString))
            
        else:
            if rockCount >= len(rocksCopy):
                rocksCopy.append(str(int(y) * 2024))
            else:
                rocksCopy[rockCount] = str(int(y) * 2024)
        
        rockCount += 1
    rocks = rocksCopy


#print(rocksCopy)
#print(rocks)
print(len(rocks))

print("Process finished --- %s seconds ---" % (time.time() - start_time))