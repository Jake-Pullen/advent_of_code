import os

with open(r'advent_of_code\2023\day_4\input.txt', 'r') as file:
    input = file.readlines()

# print(input)
test_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

#input = test_input.split('\n')
points = 0
for line in input:
    #print(line)
    winning_numbers = []
    my_numbers = []
    line = line.split('|')
    winning_numbers = line[0].split(':')[1].split()
    my_numbers = line[1].split()
    #print(f'my numbers are: {my_numbers}')
    #print(f'winning numbers are: {winning_numbers}')
    wins = 0
    for number in my_numbers:
        if number in winning_numbers:
            wins += 1
        else:
            pass 
    if wins > 0:
        add_to_points = 2**wins/2
        #print(f'add to points: {add_to_points}')
        points += add_to_points
    else:
        pass
    #print(f'wins: {wins} & points: {points}')
print(f'points: {points}')