with open(r'advent_of_code\2023\day_13\test_input.txt', 'r') as file:
    test_input = file.read()

with open(r'advent_of_code\2023\day_13\input.txt', 'r') as file:
    input = file.read()

#input = test_input

def calculate_symmetry(grid) -> int:
    """
    Calculate the symmetry of a grid.

    This function checks for vertical and horizontal symmetry in the given grid.
    For vertical symmetry, it compares each column with its mirror image.
    For horizontal symmetry, it compares each row with its mirror image.
    The symmetry score is calculated based on the number of symmetric columns and rows.

    Parameters:
    grid (list of list of str): The grid to check for symmetry. Each inner list represents a row, and each string in the inner list represents a cell.

    Returns:
    int: The symmetry score of the grid.
    """
    num_rows = len(grid)
    num_columns = len(grid[0])
    symmetry_score = 0

    # Check for vertical symmetry
    for column_index in range(num_columns - 1):
        num_mismatches = 0
        for offset in range(num_columns):
            left_column = column_index - offset
            right_column = column_index + 1 + offset
            if 0 <= left_column < right_column < num_columns:
                for row_index in range(num_rows):
                    if grid[row_index][left_column] != grid[row_index][right_column]:
                        num_mismatches += 1
        if num_mismatches == 0:
            symmetry_score += column_index + 1

    # Check for horizontal symmetry
    for row_index in range(num_rows - 1):
        num_mismatches = 0
        for offset in range(num_rows):
            upper_row = row_index - offset
            lower_row = row_index + 1 + offset
            if 0 <= upper_row < lower_row < num_rows:
                for column_index in range(num_columns):
                    if grid[upper_row][column_index] != grid[lower_row][column_index]:
                        num_mismatches += 1
        if num_mismatches == 0:
            symmetry_score += 100 * (row_index + 1)

    return symmetry_score

# Split the input into grids
grids = input.split('\n\n')

# Initialize the total symmetry score
total_symmetry = 0

# Calculate the symmetry for each grid
for grid in grids:
    grid = [[char for char in row] for row in grid.split('\n')]
    total_symmetry += calculate_symmetry(grid)

print(total_symmetry)