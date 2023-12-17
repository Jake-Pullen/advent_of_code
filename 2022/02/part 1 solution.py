with open(r'advent_of_code\2022\02\input.txt', 'r') as file:
    input = file.read()

# print(input)

letter_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}
score_map = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}
win_map = {
    'win': 6,
    'tie': 3,
    'lose': 0
}
rounds= ['A Y', 'B X', 'C Z']

points = 0
for round in input.split('\n'): 
    if round == 'A X':
        # Rock vs Rock
        points += 4
    if round == 'A Y':
        # Rock vs Paper
        points += 8
    if round == 'A Z':
        # Rock vs Scissors
        points += 3
    if round == 'B X':
        # Paper vs Rock
        points += 1
    if round == 'B Y':
        # Paper vs Paper
        points += 5
    if round == 'B Z':
        # Paper vs Scissors
        points += 9
    if round == 'C X':
        # Scissors vs Rock
        points += 7
    if round == 'C Y':
        # Scissors vs Paper
        points += 2
    if round == 'C Z': 
        # Scissors vs Scissors
        points += 6

print(points)