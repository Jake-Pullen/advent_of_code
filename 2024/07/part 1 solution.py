import logging

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


testing = 1
if not testing:
    with open(r"2024/07/input.txt", "r") as file:
        input = file.read()
else:
    input = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

# first we organise the input to something more usable
input = input.split('\n')
#print(input)
input = [x.split(': ') for x in input if x.strip()]
#print(input)
input = [(int(x[0]), list(map(int, x[1].split()))) for x in input]
#print(input)

# # Find and print the largest target number
# largest_target = max(input.keys())
# print(f'The largest target number is: {largest_target}')

OPERATORS = ['+', '*']

def generate_expressions(numbers, current_expr=""):
    if len(numbers) == 1:
        yield current_expr + str(numbers[0])
    else:
        for operator in OPERATORS:
            new_expr = current_expr + str(numbers[0]) + operator
            yield from generate_expressions(numbers[1:], new_expr)

def evaluate_left_to_right(expr):
    tokens = expr.split()
    total = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = int(tokens[i + 1])
        if operator == '+':
            total += next_number
        elif operator == '*':
            total *= next_number
        i += 2
    return total

correct_results = []
for target, numbers in input:
    logging.info(f'Processing target: {target} with numbers: {numbers}')
    for expr in generate_expressions(numbers):
        expr_with_spaces = expr.replace('+', ' + ').replace('*', ' * ')
        result = evaluate_left_to_right(expr_with_spaces)
        if int(result) == int(target):
            correct_results.append(target)
            logging.info(f'Tried {expr} = {result} matches {target}')
            # we can break here because we only need to find one correct expression
            break
        else:
            pass
            logging.info(f'Tried {expr} = {result}, but target is {target}')

print(f'Sum of correct results: {sum(correct_results)}')

# too low 2501605300634
# print(2501605300634 - 2501605301465)