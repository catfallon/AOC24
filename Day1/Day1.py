file = open(".\\Day1\\input day 1 aoc.txt")

list1 = []
list2 = []

for x in file:
    #split into two ints
    nums = x.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1.sort()
list2.sort()

distance = 0
for x in range(len(list1)): #assume both lists are same length
    distance += abs(list2[x] - list1[x])

print(distance)

file.close()