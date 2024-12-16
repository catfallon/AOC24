#takes a String starting with a number and returns the first whole number 
def getFirstNum(text):
    newStr = ""
    haveDigit = text[0].isdigit()
    while haveDigit:
        if (len(text) > 0) and (text[0].isdigit()):
            newStr += text[0]
            text = text[1:] #remove first character
        else:
            haveDigit = False
    return newStr

file = open(".\\Day3\\input.txt")
text = file.read()

#print(text)
sum = 0
while len(text) > 0 and text.find("mul(") >= 0:
    if text.find("don't()") < 0 or text.find("don't()") > text.find("mul("): 
        #should only come through if there is no don't() instruction or it hasn't been reached yet
        indx = text.find("mul(") + 4
        text = text[slice(indx, len(text))]
        if len(text) > 0 and text[0].isdigit:
            num1 = getFirstNum(text)
            text = text[len(num1):] #eats digit we've just found
            if len(text) and text[0] == ',':
                text = text[1:] #eats comma
                num2 = getFirstNum(text)
                text = text[len(num2):] #eats digit we've just found
                if len(text) > 0 and text[0] == ')':
                    sum = sum + (int(num1) * int(num2))
    elif len(text) > 0 and text.find("do()") > 0:
        #we wanna eat everything until we get a do() that reenables the multiplication operations
        text = text[text.find("do()") + 4:]
    else: #we're done
        text = ""
print(sum)


