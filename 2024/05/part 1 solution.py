testing = 0
if not testing:
    with open(r"2024/05\input.txt", "r") as file:
        input = file.read()
else:
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# first we split the input into the two parts
# the first part is the "rules" and the second part is the "updates"
rules, updates = input.split("\n\n")
# print(rules)
# print('^v^v^v^')
# print(updates)
# for each rule the left side is the page that must come before the right side
# to check the updates are correct we need to check that the left side of the update is before the right side
# if all updatesare correct then the rules are correct and we need to store the 'middle' number

# lets assign each update to a list of numbers
update_lists = []
for update in updates.split("\n"):
    update_lists.append(list(map(int, update.split(","))))
#print(update_lists)

# lets also assign the rules to a list of tuples of numbers
rule_tuples = []
for rule in rules.split("\n"):
    rule_tuples.append(tuple(map(int, rule.split("|"))))
#print(rule_tuples)

valid_updates = []
# now for each update we need to check that it follows the rules
for update in update_lists:
    valid = True
    # we need to check that the update is ordered correctly based on the rules
    for rule in rule_tuples:
        # if the update does not contain the any number in the rules we can ignore that rule
        if rule[0] not in update or rule[1] not in update:
            continue
        # if the left side is before the right side then we can break out of the loop
        if update.index(rule[0]) < update.index(rule[1]):
            continue
        # if the right side is before the left side then we can break out of the loop
        if update.index(rule[0]) > update.index(rule[1]):
            valid = False
            break
    if valid:
        valid_updates.append(update)

print('The valid updates are',valid_updates)

numbers_to_sum = []
for update in valid_updates:
    update_len = len(update)
    # we need to find the middle number
    middle = update_len // 2
    numbers_to_sum.append(update[middle])

print('The numbers to sum are',numbers_to_sum)
print('The sum of the numbers is',sum(numbers_to_sum))
