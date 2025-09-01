
file = open(".\\Day5\\input.txt")
text = file.read().split("\n")

direction = ""
xPosition = 0
yPosition = 0
for line in file:
    if line.find("^") or line.find(">") or line.find("<") or line.find("v"):
        #then its up
        direction = "^"
        yPosition = text.index(line)
        xPosition = line.index("^")
    elif line.find(">"):
        direction = ">"
        yPosition = text.index(line)
        xPosition = line.index(">")
    elif line.find("<"):
        direction = "<"
        yPosition = text.index(line)
        xPosition = line.index("<")
    elif line.find("v"):
        direction = "v"
        yPosition = text.index(line)
        xPosition = line.index("v")

print(str(direction.index()))
inPuzzle = True
while inPuzzle:
    #if something is in front, turn 90 degrees
    if text[yPosition][xPosition] == "#":
        if direction == "^":
            direction = ">"
        elif direction == ">":
            direction = "v"
        elif direction =="v":
            direction = "<"
        elif direction == "<":
            direction = "^"

    #if exiting lab, 
    elif yPosition
    inPuzzle = False