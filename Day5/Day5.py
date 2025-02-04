file = open(".\\Day5\\input.txt")
text = file.read().split("\n\n")

#retrieving rules from file
rules = []
rulesText = text[0].split()
for x in range(len(rulesText)):
    rulePair = rulesText[x].split("|")
    rules.append(rulePair)

#retrieving updates from file
updates = []
updatesText = text[1].split()
for x  in range(len(updatesText)):
    updateNums = updatesText[x].split(",")
    updates.append(updateNums)

#determine if updates follow rules
validUpdates = updates.copy()
for update in updates:
    valid = True
    for page in update:
        #find if there's a rule for each page number in the update
        for x in rules:
            if page == x[0]:
                if update.count(x[1]) > 0:
                    if update.index(x[1]) < update.index(page):
                        valid = False
    if valid == False:
        validUpdates.remove(update)

#add up middle number of each valid update
sum = 0;
for update in validUpdates:
    sum += int(update[int(len(update) / 2)])

print(sum)