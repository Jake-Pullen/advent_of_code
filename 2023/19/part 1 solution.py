with open(r'advent_of_code\2023\19\input.txt', 'r') as file:
    input = file.read()

test_input = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

# Split the input into two blocks
# input = test_input
block1, block2 = input.split("\n\n")

# Initialize a dictionary to store workflows
workflows_dict = {}

# Process the first block of input
for line in block1.splitlines():
    workflow_name, remaining = line[:-1].split("{")
    rules = remaining.split(",")
    workflows_dict[workflow_name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        comparison_key = comparison[0]
        comparison_operator = comparison[1]
        comparison_value = int(comparison[2:])
        workflows_dict[workflow_name][0].append((comparison_key, comparison_operator, comparison_value, target))

# Define a dictionary of operations
operations = {
    ">": int.__gt__,
    "<": int.__lt__
}

# Define a function to check if an item is accepted by a workflow
def is_item_accepted(item, workflow_name = "in"):
    if workflow_name == "R":
        return False
    if workflow_name == "A":
        return True

    rules, fallback = workflows_dict[workflow_name]
    
    for comparison_key, comparison_operator, comparison_value, target in rules:
        if operations[comparison_operator](item[comparison_key], comparison_value):
            return is_item_accepted(item, target)
    
    return is_item_accepted(item, fallback)

# Initialize a variable to store the total
total = 0

# Process the second block of input
for line in block2.splitlines():
    item = {}
    for segment in line[1:-1].split(","):
        character, number = segment.split("=")
        item[character] = int(number)
    if is_item_accepted(item):
        total += sum(item.values())

# Print the total
print(total)