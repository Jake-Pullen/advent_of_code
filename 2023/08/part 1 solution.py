import os

with open(r'advent_of_code\2023\08\input.txt', 'r') as file:
    input = file.read()

#print(input)

# test_input = '''RL
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)'''

test_input = '''LLR
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

input = input.split('\n')

top_line = input[0]
#print(top_line)
# change L to 0 and R to 1 and split into list
top_line = list(top_line)
top_line = [s.replace('L', '0').replace('R', '1') for s in top_line]
#print(top_line)

# create a dictionary of instructions, where is the key is a range of numbers and the value is a number from the top line
instructions = {}
for i in range(0, len(top_line)):
    instructions[i] = top_line[i]

#print(instructions)

# now we need to take the rest of the input and and split it into a dictionary where the key is left of the = sign 
# and the value is a list of the right of the = sign split by commas and stripped of whitespace and brackets

guide = input[1:]
#print(guide)
if guide[0] == '':
    guide.pop(0)
for i in range(0, len(guide)):
    if '=' in guide[i]:
        guide[i] = guide[i].replace(' ', '').replace('(', '').replace(')', '').split('=')
        guide[i][1] = guide[i][1].split(',')
        guide[i][1] = [x.strip() for x in guide[i][1]]

# now we need to create a dictionary where the key is the left of the = sign and the value is a list of the right of the = sign split by commas and stripped of whitespace and brackets
guide_dict = {}
for i in range(0, len(guide)):
    guide_dict[guide[i][0]] = guide[i][1]

print(guide_dict)

# starting at 'AAA' we need to follow the instructions to get to the bottom of the tree
# we need to follow the instructions until we get to ZZZ
# if we run out of instructions before we get to ZZZ then we need to repeat the instructions from where we are
# Convert the dictionary to a list


# Perform the operation

current_node = 'AAA'
step = 0
while current_node != 'ZZZ':
    print(current_node)
    # Use modulo to wrap step around if it's greater than the length of instructions
    choose_items = int(instructions[step % len(instructions)])
    next_node = guide_dict[current_node][choose_items]    
    current_node = next_node
    step += 1

print(f'finished in {step} steps, current node is {current_node}')
print(current_node)
