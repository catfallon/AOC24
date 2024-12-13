#I actually messed this up trying to do Part 2 because I forgot to make a new file
#and I can't get it back to the right answer so Im just gonna leave it for now
file = open(".\\Day2\\input.txt")
count = 0
for x in file:
    nums = x.split()
    safe = True
    increasing = nums[0] < nums[1] #assumes that nums has a length of at least 2
    lastNum = int(nums[0])
    for y in range(1, len(nums)): #skipping first num
        if (lastNum <= int(nums[y])) != increasing: #not sure if this should be equal to or just not
            safe = False
            #print("creasing doesnt match " + str(nums))
        difference = int(nums[y]) - lastNum
        if (abs(difference) > 3) or (abs(difference) < 1):
            print("not gradual enough" + str(nums))
            #print(difference)
            #print(int(nums[y]))
            #print(int(lastNum))
            safe = False
        lastNum = int(nums[y])
        print("y is " + str(y))
    if safe:
        count += 1
        print(str(nums) + " is " + str(safe))
print(count)
