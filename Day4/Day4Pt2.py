file = open(".\\Day4\\input.txt")
text = file.read().split()

count = 0
for y in range(len(text)): #im reversing x and y convention here on purpose so that y indicates height and x indicates length like the axes
    line = text[y]
    for x in range(len(line)):
        if line[x] == 'A':
            enoughSpace = False #checks if there's enough space for an X-MAS
            if y - 1 >= 0 and x - 1 >= 0 and y < len(text) - 1 and x < len(line) - 1:
                enoughSpace =  True

            if enoughSpace:
                #and one mas
                if (text[y - 1][x - 1] == 'M' and text[y + 1][x + 1] == 'S') or (text[y - 1][x - 1] == 'S' and text[y + 1][x + 1] == 'M'):
                    #second mas
                    if (text[y + 1][x - 1] == 'M' and text[y - 1][x + 1] == 'S') or (text[y + 1][x - 1] == 'S' and text[y - 1][x + 1] == 'M'):
                        count += 1

print(count)
