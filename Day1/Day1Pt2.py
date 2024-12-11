file = open(".\\Day1\\input day 1 aoc.txt")

list1 = []
list2 = []

for x in file:
    #split into two ints
    nums = x.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

similarity = 0
for x in list1: #assume both lists are same length
    similarity += x * list2.count(x)
    print(similarity)

print(similarity)

file.close()