testing = 0

if testing ==0:
    with open(r'2024/03\input.txt', 'r') as file:
        input = file.read()
else:
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


# find every exact instance of mul() and multiply the two numbers together 

import re

# Regular expression to find all instances of mul() with its arguments
pattern = r'mul\((\d+),(\d+)\)'
disable_pattern = r"don't\(\)"
enable_pattern = r"do\(\)"

enabled_list = []
disabled_list = []

is_active = True

# Split the input string by mul() to handle the state switching
parts = re.split(r'(mul\(\d+,\d+\))', input)
#print(parts)

for part in parts:
    if re.search(disable_pattern, part):
        is_active = False
    elif re.search(enable_pattern, part):
        is_active = True
    elif re.match(pattern, part):
        match = re.match(pattern, part)
        numbers = (int(match.group(1)), int(match.group(2)))
        if is_active:
            enabled_list.append(numbers)
        else:
            disabled_list.append(numbers)

print("Enabled list:", enabled_list)
print("Disabled list:", disabled_list)

answer = 0
for x, y in enabled_list:
    answer += x*y

print(answer)