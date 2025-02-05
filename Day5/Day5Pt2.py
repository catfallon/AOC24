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
invalidUpdates = []
for update in updates:
    valid = True
    for page in update:
        #find if there's a rule for each page number in the update
        for rule in rules:
            if page == rule[0] and update.count(rule[1]) > 0: #if both numbers in rule are in update
                if update.index(rule[1]) < update.index(rule[0]): #if rule is violated
                    valid = False
                    #rule[1] needs to go before rule[0]
                    index = update.index(rule[0])
                    update.insert(update.index(rule[1]), rule[0])
                    update.pop(index + 1)
                        
    if not valid:
        invalidUpdates.append(update)

#add up middle number of each valid update
sum = 0;
for update in invalidUpdates:
    sum += int(update[int(len(update) / 2)])

print(sum)