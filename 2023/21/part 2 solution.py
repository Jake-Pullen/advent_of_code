from collections import deque

with open(r'advent_of_code\2023\21\input.txt', 'r') as file:
    input = file.read()

test_input = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''

#input = test_input

# Input data
data = input
lines = data.split('\n')

# Grid of characters
grid = [[char for char in row] for row in lines]
rows = len(grid)
cols = len(grid[0])

# Find the start position
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'S':
            start_row, start_col = row, col

# Function to find distances
def find_distances(start_row, start_col):
    distances = {}
    queue = deque([(0, 0, start_row, start_col, 0)])
    while queue:
        temp_row, temp_col, row, col, distance = queue.popleft()
        row, temp_row = adjust_position(row, temp_row, rows)
        col, temp_col = adjust_position(col, temp_col, cols)
        if not is_valid_position(row, col):
            continue
        if (temp_row, temp_col, row, col) in distances:
            continue
        if abs(temp_row) > 4 or abs(temp_col) > 4:
            continue
        distances[(temp_row, temp_col, row, col)] = distance
        for delta_row, delta_col in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            queue.append((temp_row, temp_col, row + delta_row, col + delta_col, distance + 1))
    return distances

# Function to adjust position
def adjust_position(position, temp_position, max_position):
    if position < 0:
        temp_position -= 1
        position += max_position
    if position >= max_position:
        temp_position += 1
        position -= max_position
    return position, temp_position

# Function to check if a position is valid
def is_valid_position(row, col):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'

# Calculate distances
distances = find_distances(start_row, start_col)

# Cache for the solve function
solve_cache = {}

# Function to calculate the number of ways to reach a point
def calculate_ways(distance, value, limit):
    amount = (limit - distance) // rows
    if (distance, value, limit) in solve_cache:
        return solve_cache[(distance, value, limit)]
    result = 0
    for x in range(1, amount + 1):
        if distance + rows * x <= limit and (distance + rows * x) % 2 == (limit % 2):
            result += ((x + 1) if value == 2 else 1)
    solve_cache[(distance, value, limit)] = result
    return result

# Function to solve the problem
def solve_problem(part1):
    limit = (64 if part1 else 26501365)
    result = 0
    for row in range(rows):
        for col in range(cols):
            if (0, 0, row, col) in distances:
                result += calculate_result(row, col, part1, limit)
    return result

# Function to calculate the result
def calculate_result(row, col, part1, limit):
    result = 0
    options = [-3, -2, -1, 0, 1, 2, 3]
    for temp_row in options:
        for temp_col in options:
            if part1 and (temp_row != 0 or temp_col != 0):
                continue
            distance = distances[(temp_row, temp_col, row, col)]
            if distance % 2 == limit % 2 and distance <= limit:
                result += 1
            if temp_row in [min(options), max(options)] and temp_col in [min(options), max(options)]:
                result += calculate_ways(distance, 2, limit)
            elif temp_row in [min(options), max(options)] or temp_col in [min(options), max(options)]:
                result += calculate_ways(distance, 1, limit)
    return result

print(solve_problem(True))
print(solve_problem(False))