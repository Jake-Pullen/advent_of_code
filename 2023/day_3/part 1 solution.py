# with open(r'advent_of_code\2023\day_3\input.txt', 'r') as file:
#     input = file.read()

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

input = test_input

# find every special character in the input
# at the special character, look at every space around it (including diagonals)
# if there is a number, add it to the list of numbers
# at the end, add up all the numbers in the list

# find every special character in the input
special_characters = ['$', '*', '+', '#']
special_character_positions = []
for row_index, row in enumerate(input.split('\n')):
    for column_index, character in enumerate(row):
        if character in special_characters:
            special_character_positions.append((row_index, column_index))

print(special_character_positions)
