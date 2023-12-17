with open(r'advent_of_code\2023\14\input.txt', 'r') as file:
    input = file.read()

test_input = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

#input = test_input.split('\n')
input = input.split('\n')

# Convert each line into a list of characters
grid = [[char for char in row] for row in input]

def move_north(grid):
    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over each column
    for col in range(cols):
        # Iterate over each row
        for _ in range(rows):
            for row in range(rows):
                # If there's an 'O' above a '.', swap them
                if grid[row][col] == 'O' and row > 0 and grid[row-1][col] == '.':
                    grid[row][col] = '.'
                    grid[row-1][col] = 'O'
    return grid

def score(grid):
    # Initialize score to 0
    score = 0
    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # If the cell contains an 'O', add the number of rows minus the current row to the score
            if grid[row][col] == 'O':
                score += len(grid) - row
    return score

def show(grid):
    # Print each row of the grid
    for row in range(len(grid)):
        print(''.join(grid[row]))

def rotate(grid):
    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a new grid with '?' characters
    new_grid = [['?' for _ in range(rows)] for _ in range(cols)]
    
    # Rotate the original grid 90 degrees clockwise
    for row in range(rows):
        for col in range(cols):
            new_grid[col][rows-1-row] = grid[row][col]
    
    return new_grid

# Dictionary to store previously seen grid states
grid_history = {}

# Set target to 1 Billion
target = 1000000000
time = 0

# Keep rolling and rotating the grid until time reaches target
while time < target:
    time += 1
    
    for move_count in range(4):
        grid = move_north(grid)
        
        # Print the score after the first roll
        # Part 1 answer is printed here
        if time == 1 and move_count == 0:
            score_after_first_roll = score(grid)
            print(f'Part 1 answer: {score_after_first_roll}')
        
        # Rotate the grid
        grid = rotate(grid)
    
    # Convert the grid to a hashable format (tuple of tuples)
    grid_hash = tuple(tuple(row) for row in grid)
    
    # If we've seen this grid state before, we've found a cycle
    if grid_hash in grid_history:
        # Calculate the length of the cycle
        cycle_length = time - grid_history[grid_hash]
        
        # Skip ahead as many full cycles as we can
        cycles_to_skip = (target - time) // cycle_length
        time += cycles_to_skip * cycle_length
    
    # Store the current time for this grid state
    grid_history[grid_hash] = time

# Print the final score
final_score = score(grid)
print(f'Part 2 answer: {final_score}')