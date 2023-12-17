import math

with open(r'advent_of_code\2023\8\input.txt', 'r') as file:
    input = file.read()

#print(input)

test_input = '''LR
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''

#test_input = '''LLR
#AAA = (BBB, BBB)
#BBB = (AAA, ZZZ)
#ZZZ = (ZZZ, ZZZ)'''

input = input.split('\n')
#input = test_input.split('\n')

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

# Initialize current_nodes as a list of starting nodes
current_nodes = [node for node in guide_dict.keys() if node.endswith('A')]

solve_steps = []
# Perform the operation
# for each start node we found that ends in A
# we need to work out how many steps it takes to get to a node that ends in Z
for current_node in current_nodes:
    step = 0
    #while current node does not end with z
    while current_node:
        # Use modulo to wrap step around if it's greater than the length of instructions
        choose_items = int(instructions[step % len(instructions)])
        next_node = guide_dict[current_node][choose_items]    
        current_node = next_node
        step += 1
        if current_node.endswith('Z'):
            break
    solve_steps.append(step)

print(solve_steps)
# once we find out how many steps it takes to get to Z we need to find the lowest common denominator of all the steps
lcm_value = solve_steps[0]
for number in solve_steps[1:]:
  lcm_value = lcm_value * number // math.gcd(lcm_value, number)

print(lcm_value)