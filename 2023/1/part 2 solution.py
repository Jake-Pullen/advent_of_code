import re

with open(r'advent_of_code\2023\1\input.txt', 'r') as file:
    input = file.read()

def text_to_num(line: str) -> str:
    '''Returns the line with the text numbers replaced with digits
    input: line - string of characters 
    output: a string
    
    example:
    input: 'eightwothree'
    output: '8wo3'
    '''
    text_to_num = {
    "zero": "0",
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
    }
    #replace a text number with a digit surrounded by the same text numberm to resolve overlaps
    for key, value in text_to_num.items():
        if key in line:
            line = line.replace(key, value)
    return line

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
        line = text_to_num(line)
        list.append(grab_first_and_last_digit(line))

    return sum(list)


test_input = 'two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'
day_1_test = day_1_solution(test_input)
print(day_1_test)
assert day_1_test == 281

day_1_answer = day_1_solution(input)
print(day_1_answer)

