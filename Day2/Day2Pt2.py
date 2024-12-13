"""Function takes a list of numbers and returns a number of possible indexes of mistakes
based on whether the numbers are not all increasing or decreasing or doing so too rapidly"""
def findIfSafe(nums, increasingBool):
    lastNum = int(nums[0])
    mistakes = []
    for y in range(1, len(nums)): #skipping first num
        if (lastNum <= int(nums[y])) != increasingBool:
            mistakes.append(y) #add both indexes to check if either of them can be removed to fix the mistake
            mistakes.append(y - 1)
        difference = int(nums[y]) - lastNum
        if (abs(difference) > 3) or (abs(difference) < 1):            
            mistakes.append(y - 1) 
            mistakes.append(y) 
        lastNum = int(nums[y])
    return mistakes

file = open(".\\Day2\\input.txt")
count = 0
for x in file:
    nums = x.split()
    safe = True
    increasing = 0
    decreasing = 0
    lastNum = int(nums[0])
    for y in range(1, len(nums)):
        if lastNum <= int(nums[y]):
            increasing += 1
        else:
            decreasing += 1
    increasingBool = increasing > decreasing
    mistakes = findIfSafe(nums, increasingBool)
    if len(mistakes) > 0:
        #then check while removing something
        safe = False
        #check removing all possible mistakes and see if any of those work
        for y in range(len(mistakes)):
            numsCopy = nums.copy()
            numsCopy.pop(mistakes[y])
            mistakesInNumsCopy = findIfSafe(numsCopy, increasingBool)
            if len(mistakesInNumsCopy) == 0:
                safe = True
    if safe:
        count += 1
    print(str(nums) + " is " + str(safe))
print("count is " + str(count))
