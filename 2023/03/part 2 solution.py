with open(r'advent_of_code\2023\03\input.txt', 'r') as file:
    input = file.readlines()

# print(input)

test_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

## remove when not test 
## input = test_input
## remove when not test 

def get_directions(x_offset, y_offset):
    for y in range(-1, 2):
        for x in range(-1, 2):
            yield x + x_offset, y + y_offset

valid_map = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]

for i, row in enumerate(input[1:-1]):
    for j, char in enumerate(row[1:-1]):
        if not (char == "." or char.isnumeric()):
            for x, y in get_directions(j + 1, i + 1):
                valid_map[y][x] = 1

current_number = '0'
num_valid = False
sm = 0

for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char.isnumeric():
            num_valid = num_valid or valid_map[i][j]
            current_number += char
        else:
            if num_valid:
                sm += int(current_number)
            num_valid = False
            current_number = '0'

print(sm)


# Part 2
def h_flood(x: int, y: int, m: int) -> str:
    if not input[y][x].isnumeric():
        return ""
    flood = h_flood(x + m, y, m)
    return f'{flood if m < 0 else ""}{input[y][x]}{flood if m > 0 else ""}'

def get_surrounding(x: int, y: int) -> list:
    return list(map(int, filter(lambda _: _,
                                {h_flood(_x, _y, -1)[:-1] + h_flood(_x, _y, 1) for _x, _y in get_directions(x, y) if
                                 input[_y][_x] != '*'})))


total = 0

for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == '*':
            if len(nums := get_surrounding(j, i)) == 2:
                total += nums[0] * nums[1]

print(total)