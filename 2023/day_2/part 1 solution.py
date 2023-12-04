with open(r'advent_of_code\2023\day_2\input.txt', 'r') as file:
    input = file.read()

# print(input)
test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

amount_of_cubes = '12 red, 13 green, 14 blue'
amount_of_cubes = amount_of_cubes.split(', ')
# create a dictionary to store the amount of cubes
amount_of_cubes_dict = {}
for cube in amount_of_cubes:
    # split the string into the amount and the colour
    # first 2 characters are the amount
    cube = [int(cube[:2]), cube[3:]]
    amount_of_cubes_dict[cube[1]] = cube[0]
print(f'control: {amount_of_cubes_dict}')

def check_round(round_dict):
    # Check if the keys exist in the dictionary, if not assign 0
    red = round_dict.get('red', 0)
    green = round_dict.get('green', 0)
    blue = round_dict.get('blue', 0)

    # Now compare with the amount_of_cubes_dict
    if red > amount_of_cubes_dict['red'] or green > amount_of_cubes_dict['green'] or blue > amount_of_cubes_dict['blue']:
        print('round', round_counter, 'is invalid')
        return False
    else:
        print('round', round_counter, 'is valid')
        return True

# break out each game to check if any of the games are valid
#games = test_input.split('\n')
games = input.split('\n')
game_counter = 0
score = 0
for game in games:
    game_counter += 1
    game = game.split(': ')[1]
    print('game', game_counter)
    round_counter = 0
    rounds = game.split('; ')
    for round in rounds:
        round_counter += 1
        round = round.split(', ')
        round_dict = {}
        for cube in round:
            cube = [int(cube[:2]), cube[2:]]
            cube[1] = cube[1].replace(' ', '')
            round_dict[cube[1]] = cube[0]
        #print(round_dict)
        
        if check_round(round_dict) == False:
            break
        else:
            continue
    else:
        score += game_counter
        print('game', game_counter, 'is valid')
        continue
else:
    print('score:', score)
