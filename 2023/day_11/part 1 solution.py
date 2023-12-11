from queue import Queue
# import os

with open(r'advent_of_code\2023\day_11\input.txt', 'r') as file:
    input = file.readlines()

# print(input)

test_input = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

#print(test_input)
#input = test_input.split('\n')

def expand_universe(input):
    '''add an extra row or column of empty spaces to each row or column that has no # in it'''
    print('Expanding universe')
    # expand empty rows
    new_input = []
    for row in input:
        if '#' in row:
            new_input.append(row)
        else:
            new_input.append(row)
            new_input.append(row)
    
    # expand empty columns

    # Transpose the input
    transposed_input = list(map(list, zip(*new_input)))

    new_input = []
    for row in transposed_input:
        if '#' in row:
            new_input.append(row)
        else:
            new_input.append(row)
            new_input.append(row)

    # Transpose the input back
    new_input = list(map(list, zip(*new_input)))

    # Convert rows back to strings
    new_input = [''.join(row) for row in new_input]
    
    return new_input

input = expand_universe(input)

def number_galaxies(input):
    '''gives a unique number to each galaxy(#) in the input grid'''
    print('Numbering galaxies')
    # make a copy of the input
    input_copy = [list(row) for row in input]  # Convert strings to lists
    # replace the galaxies with their numbers
    galaxy_number = 1
    galaxy_coordinates = {}  # This dictionary will store the coordinates of each galaxy
    for i in range(len(input_copy)):
        for j in range(len(input_copy[i])):
            if input_copy[i][j] == '#':
                input_copy[i][j] = str(galaxy_number)  # Convert number back to string
                galaxy_coordinates[galaxy_number] = (i, j)  # Store the coordinates of the galaxy
                galaxy_number += 1  # Increment the galaxy number
    # Convert lists back to strings
    input_copy = [''.join(row) for row in input_copy]
    return input_copy, galaxy_coordinates

input, galaxy_coordinates = number_galaxies(input)
#print(galaxy_coordinates)

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# find the shortest path between each pair of galaxies
print('Finding the shortest path between each pair of galaxies')
galaxy_distances = {}
for galaxy in galaxy_coordinates:
    galaxy_distances[galaxy] = {}
    for other_galaxy in galaxy_coordinates:
        if galaxy != other_galaxy:
            galaxy_distances[galaxy][other_galaxy] = manhattan_distance(galaxy_coordinates[galaxy], galaxy_coordinates[other_galaxy])
#print(galaxy_distances)

# remove the duplicate distances ie 1->2 and 2->1
print('Removing the duplicate distances')
for galaxy in galaxy_distances:
    for other_galaxy in galaxy_distances[galaxy]:
        if other_galaxy in galaxy_distances:
            del galaxy_distances[other_galaxy][galaxy]
#print(galaxy_distances)

# sum up all the distances
print('Summing up all the distances')
total_distance = 0
for galaxy in galaxy_distances:
    for other_galaxy in galaxy_distances[galaxy]:
        total_distance += galaxy_distances[galaxy][other_galaxy]
print(total_distance)