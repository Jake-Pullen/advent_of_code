with open(r'advent_of_code\2022\02\input.txt', 'r') as file:
    input = file.read()

# print(input)

letter_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}
decision_map = {
    'X': 'loose',
    'Y': 'draw',
    'Z': 'win'
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
rounds = ['A Y', 'B X', 'C Z']
points = 0

# first we need to decide if we need to win / loose or draw
for round in input.split('\n'):
    if round[2] == 'X':
        points += 0
        # we need to loose
        if round[0] == 'A':
            # they played rock
            # to loose we need to play scissors
            points += 3
        if round[0] == 'B':
            # they played paper
            # to loose we need to play rock
            points += 1
        if round[0] == 'C':
            # they played scissors
            # to loose we need to play paper
            points += 2
    if round[2] == 'Y':
        points += 3
        # we need to draw
        if round[0] == 'A':
            # they played rock
            # we need to play rock
            points += 1
        if round[0] == 'B':
            # they played paper
            # we need to play paper
            points += 2
        if round[0] == 'C':
            # they played scissors
            # we need to play scissors
            points += 3
    if round[2] == 'Z':
        points += 6
        # we need to win
        if round[0] == 'A':
            # they played rock
            # we need to play paper
            points += 2
        if round[0] == 'B':
            # they played paper
            # we need to play scissors
            points += 3
        if round[0] == 'C':
            # they played scissors
            # we need to play rock
            points += 1

print(points)