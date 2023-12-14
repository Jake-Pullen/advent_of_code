with open(r'advent_of_code\2023\day_14\input.txt', 'r') as file:
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


# show(grid)
# print('moving rocks')
grid = move_north(grid)
# show(grid)

print(score(grid))

