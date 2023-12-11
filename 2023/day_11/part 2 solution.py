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
    empty_rows = []
    for i, row in enumerate(input):
        if '#' in row:
            new_input.append(row)
        else:
            new_input.append(row)
            #new_input.append(row)
            empty_rows.append(i)
    
    # expand empty columns
    empty_columns = []
    # Transpose the input
    transposed_input = list(map(list, zip(*new_input)))

    new_input = []
    for i, row in enumerate(transposed_input):
        if '#' in row:
            new_input.append(row)
        else:
            new_input.append(row)
            #new_input.append(row)
            empty_columns.append(i)

    # Convert rows back to strings
    new_input = [''.join(row) for row in new_input]
    
    return new_input, empty_rows, empty_columns

def number_galaxies(input):
    '''gives a unique number to each galaxy(#) in the input grid'''
    print('Numbering galaxies')
    # make a copy of the input
    input_copy = [list(row) for row in input]  # Convert strings to lists
    # replace the galaxies with their numbers
    galaxy_coordinates = []  # This list will store the coordinates of each galaxy
    for i in range(len(input_copy)):
        for j in range(len(input_copy[i])):
            if input_copy[i][j] == '#':
                galaxy_coordinates.append((i, j))  # Store the coordinates of the galaxy
    # Convert lists back to strings
    input_copy = [''.join(map(str, row)) for row in input_copy]
    return input_copy, galaxy_coordinates

def calculate_distance(point1, point2, empty_rows, empty_columns):
    # Calculate Manhattan distance
    total_distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    length_to_add = 1000000-1  # The additional length to add when passing through an empty row or column

    # Check each empty row
    for row in empty_rows:
        if min(point1[1], point2[1]) <= row <= max(point1[1], point2[1]):
            total_distance += length_to_add

    # Check each empty column
    for column in empty_columns:
        if min(point1[0], point2[0]) <= column <= max(point1[0], point2[0]):
            total_distance += length_to_add

    return total_distance


def find_shortest_path(galaxy_coordinates, empty_rows, empty_columns):
    # find the shortest path between each pair of galaxies
    print('Finding the shortest path between each pair of galaxies')
    galaxy_distances = []
    for i, point1 in enumerate(galaxy_coordinates):
        for point2 in galaxy_coordinates[:i]:

            distance = calculate_distance(point1, point2, empty_rows, empty_columns)
            galaxy_distances.append(distance)
    return galaxy_distances

def sum_up_distances(galaxy_distances):
    # sum up all the distances
    print('Summing up all the distances')
    total_distance = 0
    for distance in galaxy_distances:
        total_distance += distance
    return total_distance


input,empty_rows,empty_columns = expand_universe(input)
input, galaxy_coordinates = number_galaxies(input)
galaxy_distances = find_shortest_path(galaxy_coordinates, empty_rows, empty_columns)
total_distance = sum_up_distances(galaxy_distances)
print(total_distance)