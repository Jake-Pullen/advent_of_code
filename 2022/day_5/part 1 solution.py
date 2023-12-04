with open(r'2022\day_5\input.txt', 'r') as file:
    input = file.read()

# print(input)

pile_map = {
    1: 1,
    2: 5,
    3: 9,
    4: 13,
    5: 17,
    6: 21,
    7: 25,
    8: 29,
    9: 33
}
test_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

# input = test_input

line_first_move = input.find('move')
loading_area = input[:(line_first_move-2)]
# print(loading_area)
instructions = input[line_first_move:]
# print(instructions)
print(loading_area)
# test1 = loading_area[5][0]
# print(test1)

def get_top_letter(pile_number, loading_area):
    column = pile_map[pile_number]
    lines = loading_area.split('\n')
    for line in lines:
        if line[column] != ' ':
            value = line[column]
            return value
    return None

def add_to_pile(value, pile_number, loading_area):
    column = pile_map[pile_number]
    lines = [list(line) for line in loading_area.split('\n')]
    for line in reversed(lines):
        if line[column] == ' ':
            line[column] = value
            break
    loading_area = '\n'.join(''.join(line) for line in lines)
    return loading_area

test = add_to_pile('X',3, loading_area)
print(test)

def move_box(from_pile, to_pile):
    # find the box on the top of the pile
    letter_to_move = get_top_letter(from_pile, loading_area)
    # move it to the top of the other pile
    add_to_pile(letter_to_move, to_pile, loading_area)
    # return the new loading area
    return loading_area


for line in instructions.split('\n'):
    line = line.split(' ')
    counter = int(line[1])
    for repeat in range(counter):
        move_box(line[3], line[5])
    #print(line)

print(loading_area)