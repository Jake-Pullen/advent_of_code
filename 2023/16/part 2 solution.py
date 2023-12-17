# Open and read the file
with open(r'advent_of_code\2023\16\input.txt', 'r') as file:
    input_data = file.read()

test_input = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

# Assign the input data to a variable
data = input_data
#data = test_input

# Split the input data into lines
lines = data.split('\n')

# Create a grid from the lines
grid = [[char for char in row] for row in lines]

# Get the number of rows and columns in the grid
num_rows = len(grid)
num_columns = len(grid[0])

# Define the directions for row and column
direction_row = [-1, 0, 1, 0]
direction_column = [0, 1, 0, -1]

# Function to calculate the next step
def calculate_next_step(row, column, direction):
    return (row + direction_row[direction], column + direction_column[direction], direction)

# Function to calculate the score
def calculate_score(start_row, start_column, start_direction):
    positions = [(start_row, start_column, start_direction)]
    seen_positions = set()
    seen_positions_2 = set()

    while True:
        new_positions = []
        if not positions:
            break
        for (row, column, direction) in positions:
            if 0 <= row < num_rows and 0 <= column < num_columns:
                seen_positions.add((row, column))
                if (row, column, direction) in seen_positions_2:
                    continue
                seen_positions_2.add((row, column, direction))
                char = grid[row][column]
                if char == '.':
                    new_positions.append(calculate_next_step(row, column, direction))
                elif char == '/':
                    new_positions.append(calculate_next_step(row, column, {0: 1, 1: 0, 2: 3, 3: 2}[direction]))
                elif char == '\\':
                    new_positions.append(calculate_next_step(row, column, {0: 3, 1: 2, 2: 1, 3: 0}[direction]))
                elif char == '|':
                    if direction in [0, 2]:
                        new_positions.append(calculate_next_step(row, column, direction))
                    else:
                        new_positions.append(calculate_next_step(row, column, 0))
                        new_positions.append(calculate_next_step(row, column, 2))
                elif char == '-':
                    if direction in [1, 3]:
                        new_positions.append(calculate_next_step(row, column, direction))
                    else:
                        new_positions.append(calculate_next_step(row, column, 1))
                        new_positions.append(calculate_next_step(row, column, 3))
        positions = new_positions
    return len(seen_positions)

score = calculate_score(0,0,1)
print(score)

# Initialize the maximum score
max_score = 0

# Iterate over each row
for row in range(num_rows):
    # Calculate the score for the current row starting from the first column moving right
    score_from_start = calculate_score(row, 0, 1)
    # Calculate the score for the current row starting from the last column moving left
    score_from_end = calculate_score(row, num_columns - 1, 3)

    # Update the maximum score
    max_score = max(max_score, score_from_start, score_from_end)

# Iterate over each column
for column in range(num_columns):
    # Calculate the score for the current column starting from the first row moving down
    score_from_top = calculate_score(0, column, 2)
    # Calculate the score for the current column starting from the last row moving up
    score_from_bottom = calculate_score(num_rows - 1, column, 0)

    # Update the maximum score
    max_score = max(max_score, score_from_top, score_from_bottom)

# Print the maximum score
print(max_score)