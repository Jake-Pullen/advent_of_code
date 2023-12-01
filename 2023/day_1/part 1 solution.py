import re

with open('advent_of_code_2023\day_1\input.txt', 'r') as file:
    input = file.read()

def grab_first_and_last_digit(line: str) -> (int):
    '''Returns the first and last digit of the given line
    input: line - string of characters 
    output: a 2 digit integer
    
    example:
    input: 'pqr3stu8vwx'
    output: 38
    '''
    first_digit = re.findall(r'\d', line)[0]
    last_digit = re.findall(r'\d', line)[-1]
    return int(first_digit + last_digit)

def day_1_solution(input:str) -> int:
    '''Returns the sum of the first and last digit of each line
    input: input - string of characters
    output: an integer
    
    example:
    input: '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'
    output: 48
    '''
    list = []
    for line in input.split('\n'):
        list.append(grab_first_and_last_digit(line))

    return sum(list)


test_input = '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'
day_1_test = day_1_solution(test_input)
print(day_1_test)
assert day_1_test == 142

day_1_answer = day_1_solution(input)
print(day_1_answer)

