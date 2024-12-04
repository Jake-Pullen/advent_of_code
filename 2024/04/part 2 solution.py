testing = 0
if not testing:
    with open(r'2024/04\input.txt', 'r') as file:
        input = file.read()
else:
    input = '''.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........'''

# word search, 
# allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words
# test input has 18 words

# part 2 calls for looking for 2x 'MAS' in the shape of an 'X'
# we can now ignore the NESW directions
# we should just check the diagonals of any 'A' we find
# if it has 2 'MAS' in the diagonals, we have a match

# turn the input into a list of lists so we can grid reference it

lines = input.split('\n')
grid = [list(line) for line in lines]
directions = {
    'north_east': (1, -1),
    'south_west': (-1, 1),

    'south_east': (1, 1),
    'north_west': (-1, -1),
}
grid_x_len = len(grid[0])
grid_y_len = len(grid)

# print(grid)
xmas_count = 0

# search for 'A's
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != 'A':
            continue
        # we found an 'A', check diagonals for 'M' and 'S'
        if not (0 <= x + 1 < grid_x_len and 0 <= y + 1 < grid_y_len and
                0 <= x - 1 < grid_x_len and 0 <= y - 1 < grid_y_len):
            # we are at the edge of the grid, no need to check
            continue
        
        # take the character from the diagonal, including the middle 'A'

        word_to_check = grid[y + 1][x + 1] + grid[y][x] + grid[y - 1][x - 1]
        if word_to_check == 'MAS' or word_to_check == 'SAM':
            # one diagonal has 'MAS', check the other
            word_to_check = grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1]
            if word_to_check == 'MAS' or word_to_check == 'SAM':
                xmas_count += 1
            #print(word_to_check)

            
print(xmas_count)
