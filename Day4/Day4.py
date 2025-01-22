file = open(".\\Day4\\input.txt")
text = file.read().split()

count = 0
for y in range(len(text)): #im reversing x and y convention here on purpose so that y indicates height and x indicates length like the axes
    line = text[y]
    for x in range(len(line)):
        if line[x] == 'X':
            #booleans to indicate whether there's enough space in each direction for XMAS
            forwardSpace = False
            backwardSpace = False
            downSpace = False
            upSpace = False
            if x < len(line) - 3:
                forwardSpace = True
            if y < len(text) - 3:
                downSpace = True
            if x - 3 >= 0:
                backwardSpace = True
            if y - 3 >= 0:
                upSpace = True
            #across
            if forwardSpace and line[x + 1] == 'M' and line[x + 2] == 'A' and line[x + 3] == 'S':
                count += 1
            #down
            if downSpace and text[y + 1][x] == 'M' and text[y + 2][x] == 'A' and text[y + 3][x] == 'S':
                count += 1
            #backwards
            if backwardSpace and line[x - 1] == 'M' and line[x - 2] == 'A' and line[x - 3] == 'S':
                count += 1
            #up
            if upSpace and text[y - 1][x] == 'M' and text[y - 2][x] == 'A' and text[y - 3][x] == 'S':
                count += 1
            if forwardSpace and downSpace and text[y + 1][x + 1] == 'M' and text[y + 2][x + 2] == 'A' and text[y + 3][x + 3] == 'S':
                count += 1
            if backwardSpace and downSpace and text[y + 1][x - 1] == 'M' and text[y + 2][x - 2] == 'A' and text[y + 3][x - 3] == 'S':
                count += 1
            if forwardSpace and upSpace and text[y - 1][x + 1] == 'M' and text[y - 2][x + 2] == 'A' and text[y - 3][x + 3] == 'S':
                count += 1
            if backwardSpace and upSpace and text[y - 1][x - 1] == 'M' and text[y - 2][x - 2] == 'A' and text[y - 3][x - 3] == 'S':
                count += 1
print(count)
