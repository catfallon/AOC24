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

sum = 0
while text.find("mul(") >= 0 and len(text) > 0:
    indx = text.find("mul(") + 4
    text = text[slice(indx, len(text))]
    if len(text) > 0 and text[0].isdigit:
        num1 = getFirstNum(text)
        text = text[len(num1):] #eats digit we've just found
        if len(text) > 0 and text[0] == ',':
            text = text[1:] #eats comma
            num2 = getFirstNum(text)
            text = text[len(num2):] #eats digit we've just found
            if len(text) > 0 and text[0] == ')':
                sum = sum + (int(num1) * int(num2))
print(sum)


