testing = 0
if not testing:
    with open(r'2024/04\input.txt', 'r') as file:
        input = file.read()
else:
    input = '''....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX'''

# word search, 
# allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words
# test input has 18 words

def count_occurance(input, WORD = 'XMAS'):
    rows = len(input)
    cols = len(input[0])
    word_len = len(WORD)
    directions = {
            'north': (0, -1),
            'north_east': (1, -1),
            'east': (1, 0), 
            'south_east': (1, 1),
            'south': (0, 1), 
            'south_west': (-1, 1),
            'west': (-1, 0),
            'north_west': (-1, -1),
        }

    def am_i_still_in_grid(x,y):
        'Returns True if the coordinates are within the grid'
        return 0 <= x < rows and 0 <= y < cols
    

    def search_from(start_x, start_y, delta_x, delta_y):
        """
        Check if the word can be found starting from (start_x, start_y) 
        in the direction specified by (delta_x, delta_y).
        """
        for i in range(word_len):
            # Calculate the new coordinates
            new_x = start_x + i * delta_x
            new_y = start_y + i * delta_y
            
            # Check if the new coordinates are within the grid and match the word
            if not am_i_still_in_grid(new_x, new_y) or input[new_x][new_y] != WORD[i]:
                return False
        
        # If all characters match, return True
        return True

    word_count = 0
    for x in range(rows):
        for y in range(cols):
            for direction in directions.values():
                if search_from(x, y, direction[0], direction[1]):
                    word_count += 1

    return word_count

lines = input.split('\n')
print(count_occurance(lines))

