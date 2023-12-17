import numpy as np
from queue import Queue

with open(r'advent_of_code\2023\10\input.txt', 'r') as file:
    input = file.read()

simple_test_input = '''.....
.S-7.
.|.|.
.L-J.
.....'''

complex_test_input = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''

last_test_input = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''

# print(simple_test_input)
# print(complex_test_input)

#input = simple_test_input.split('\n')
#input = complex_test_input.split('\n')
#input = last_test_input.split('\n')
input = input.split('\n')
#print(input)


NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

pipe_directions = {
    '|': (NORTH, SOUTH),
    '-': (WEST, EAST),
    'L': (NORTH, EAST),
    'J': (NORTH, WEST),
    '7': (WEST, SOUTH),
    'F': (SOUTH, EAST),
    '.': (),
}


def performLeeAlgorithm(pipe_map: list[list], distance_map: list[list], start_position: tuple[int]) -> None:
    # Initialize a queue and add the start position to it
    queue = Queue()
    queue.put(start_position)
    # Set the distance of the start position to 0
    distance_map[start_position[0]][start_position[1]] = 0

    # Continue until the queue is empty
    while not queue.empty():
        # Get the next position from the queue
        current_row, current_col = queue.get()
        # Iterate over the directions that the pipe at the current position allows
        for delta_row, delta_col in pipe_directions[pipe_map[current_row][current_col]]:
            # Calculate the next position
            next_row, next_col = current_row + delta_row, current_col + delta_col
            # If the next position is a pipe and its distance has not been set yet
            if pipe_map[next_row][next_col] != '.' and distance_map[next_row][next_col] == -1:
                # Set the distance of the next position
                distance_map[next_row][next_col] = distance_map[current_row][current_col] + 1
                # Add the next position to the queue
                queue.put((next_row, next_col))


def fill_seq(distance_map: list[list]) -> None:
    # Initialize a queue with the starting position (0, 0)
    positions_queue = Queue()
    start_row, start_col = 0, 0
    positions_queue.put((start_row, start_col))
    distance_map[start_row][start_col] = -2

    # Define the possible movements in the grid (right, left, down, up)
    row_directions = [0, 0, 1, -1]
    col_directions = [1, -1, 0, 0]

    # While there are positions in the queue
    while not positions_queue.empty():
        # Get the next position from the queue
        current_row, current_col = positions_queue.get()

        # Try moving in each direction from the current position
        for direction in range(4):
            next_row = current_row + row_directions[direction]
            next_col = current_col + col_directions[direction]

            # If the next position is inside the grid and its distance is -1
            if (0 <= next_row < len(distance_map) and 0 <= next_col < len(distance_map[0]) 
                and distance_map[next_row][next_col] == -1):
                # Set the distance at the next position to -2
                distance_map[next_row][next_col] = -2
                # Add the next position to the queue
                positions_queue.put((next_row, next_col))


def insert_between(input_array: np.array, fill_value) -> np.array:
    # Calculate the shape of the output array, which is twice the shape of the input array minus 1
    output_shape = 2 * np.array(input_array.shape) - 1
    # Create an output array filled with the fill value and with the calculated shape
    output_array = np.full(output_shape, dtype=input_array.dtype, fill_value=fill_value)
    # Copy the values from the input array to the output array, skipping every other row and column
    output_array[::2, ::2] = input_array
    return output_array

# Convert each row in the input to a list and store them in a list
pipe_map = [list(row) for row in input]

# Pad the pipe_map with '.' on all sides
pipe_map = np.pad(pipe_map, 1, constant_values='.')

# Create a distance_map with the same shape as pipe_map, filled with -1
distance_map = np.full_like(pipe_map, -1, dtype=np.int32)

# Convert pipe_map and distance_map to lists
pipe_map = pipe_map.tolist()
distance_map = distance_map.tolist()

# find start location
START = None
for i, row in enumerate(pipe_map):
    for j, x in enumerate(row):
        if x == 'S':
            START = (i, j)
            break
    if START:
        break
    
# Initialize the directions for the start ('S') pipe as an empty list
pipe_directions['S'] = []

# Define the start position
start_row, start_col = START

# Check the pipe in each direction from the start position
# If the pipe in that direction allows movement towards the start position, add the opposite direction to pipe_directions['S']

# Check the pipe to the north
north_pipe = pipe_map[start_row + NORTH[0]][start_col + NORTH[1]]
if SOUTH in pipe_directions[north_pipe]:
    pipe_directions['S'].append(NORTH)

# Check the pipe to the south
south_pipe = pipe_map[start_row + SOUTH[0]][start_col + SOUTH[1]]
if NORTH in pipe_directions[south_pipe]:
    pipe_directions['S'].append(SOUTH)

# Check the pipe to the east
east_pipe = pipe_map[start_row + EAST[0]][start_col + EAST[1]]
if WEST in pipe_directions[east_pipe]:
    pipe_directions['S'].append(EAST)

# Check the pipe to the west
west_pipe = pipe_map[start_row + WEST[0]][start_col + WEST[1]]
if EAST in pipe_directions[west_pipe]:
    pipe_directions['S'].append(WEST)
    
performLeeAlgorithm(pipe_map, distance_map, START)
    
for row_index in range(len(pipe_map)):
    for col_index in range(len(pipe_map[row_index])):
        if distance_map[row_index][col_index] == -1:
            pipe_map[row_index][col_index] = '.'

distance_map = insert_between(np.array(distance_map), -1).tolist()
pipe_map = insert_between(np.array(pipe_map), '.').tolist()
    

for row_index in range(len(pipe_map)):
    for col_index in range(1, len(pipe_map[row_index]), 2):
        if EAST in pipe_directions[pipe_map[row_index][col_index-1]] and WEST in pipe_directions[pipe_map[row_index][col_index+1]]:
            pipe_map[row_index][col_index] = '-'
            distance_map[row_index][col_index] = 0

for row_index in range(1, len(pipe_map), 2):
    for col_index in range(len(pipe_map[row_index])):
        if SOUTH in pipe_directions[pipe_map[row_index-1][col_index]] and NORTH in pipe_directions[pipe_map[row_index+1][col_index]]:
            pipe_map[row_index][col_index] = '|'
            distance_map[row_index][col_index] = 0

fill_seq(distance_map)

distance_map = np.array(distance_map)
distance_map = np.delete(distance_map, list(range(1, distance_map.shape[0], 2)), axis=0)
distance_map = np.delete(distance_map, list(range(1, distance_map.shape[1], 2)), axis=1)
    
unique, counts = np.unique(distance_map, return_counts=True)
print(dict(zip(unique, counts))[-1])