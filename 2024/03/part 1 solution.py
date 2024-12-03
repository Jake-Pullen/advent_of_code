
testing = 0
if testing ==0:
    with open(r'2024/03\input.txt', 'r') as file:
        input = file.read()
else:
    input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'


# find every exact instance of mul() and multiply the two numbers together 

import re

# Regular expression to find all instances of mul() with its arguments
pattern = r'mul\((\d+),(\d+)\)'

matches = re.findall(pattern, input)

numbers = [(int(x), int(y)) for x, y in matches]

print(numbers)
answer = 0
for x, y in numbers:
    answer += x*y

print(answer)