import sys
from collections import defaultdict, deque
import math

with open(r'advent_of_code\2023\20\input.txt', 'r') as file:
    input = file.read()

test_input = r'''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''

another_test_input = r'''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output''' 

# input = test_input
# input = another_test_input

# Read input
input_data = input
lines = input_data.split('\n')

# Function to calculate least common multiple
def least_common_multiple(numbers):
    result = 1
    for num in numbers:
        result = (result * num) // math.gcd(num, result)
    return result

# Initialize dictionaries
type_dict = {}
rules_dict = {}

# Parse input lines
for line in lines:
    source, destination = line.split('->')
    source = source.strip()
    destination = destination.strip().split(', ')
    rules_dict[source] = destination
    type_dict[source[1:]] = source[0]

# Function to adjust type
def adjust_type(type):
    if type in type_dict:
        return type_dict[type] + type
    else:
        return type

# Initialize more dictionaries
from_dict = {}
inverse_dict = defaultdict(list)

# Adjust types and fill dictionaries
for x, ys in rules_dict.items():
    rules_dict[x] = [adjust_type(y) for y in ys]
    for y in rules_dict[x]:
        if y[0] == '&':
            if y not in from_dict:
                from_dict[y] = {}
            from_dict[y][x] = 'lo'
        inverse_dict[y].append(x)

# Initialize variables
watch = inverse_dict[inverse_dict['rx'][0]]
low_count = 0 
high_count = 0
queue = deque()
on_set = set()
previous_dict = {}
count_dict = defaultdict(int)
to_lcm = []

# Main loop
for timestamp in range(1, 10**8):
    queue.append(('broadcaster', 'button', 'lo'))

    while queue:
        x, from_, typ = queue.popleft()

        if typ == 'lo':
            if x in previous_dict and count_dict[x] == 2 and x in watch:
                to_lcm.append(timestamp - previous_dict[x])
            previous_dict[x] = timestamp
            count_dict[x] += 1
        if len(to_lcm) == len(watch):
            print(least_common_multiple(to_lcm))
            sys.exit(0)

        if x == 'rx' and typ == 'lo':
            print(timestamp + 1)

        if typ == 'lo':
            low_count += 1
        else:
            high_count += 1

        if x not in rules_dict:
            continue
        if x == 'broadcaster':
            for y in rules_dict[x]:
                queue.append((y, x, typ))
        elif x[0] == '%':
            if typ == 'hi':
                continue
            else:
                if x not in on_set:
                    on_set.add(x)
                    new_typ = 'hi'
                else:
                    on_set.discard(x)
                    new_typ = 'lo'
                for y in rules_dict[x]:
                    queue.append((y, x, new_typ))
        elif x[0] == '&':
            from_dict[x][from_] = typ
            new_typ = ('lo' if all(y == 'hi' for y in from_dict[x].values()) else 'hi')
            for y in rules_dict[x]:
                queue.append((y, x, new_typ))
        else:
            assert False, x
    if timestamp == 1000:
        print(low_count * high_count)