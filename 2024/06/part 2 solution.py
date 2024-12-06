testing = 0
if not testing:
    with open(r"2024/06\input.txt", "r") as file:
        input = file.read()
else:
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

OBSTACLE = "#"
# first we should turn the input into a list of lists so we can use grid references

split_input = input.split("\n")
grid = [list(x) for x in split_input]
ROWS = len(grid)
COLUMNS = len(grid[0])

# for x in grid:
#     print(x)

# we need to find the starting position
# our starting position is the only '^' in the grid
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == "^":
            position = (x, y)
            break
#print('start at',position)

# We start by travelling north until we hit an obstacle '#'
# then we turn right and travel east until we hit an obstacle
# we keep turning right and travelling until we hit an obstacle
# once we make it off the grid we stop
# count how many unique squares we visit

loops = 0
for row in range(ROWS):
    for col in range(COLUMNS):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
        direction_index = 0  # Start by moving north
        x, y = position
        visited = set()
        visited_with_direction = set() # used for loop detection
        while True:
            visited.add((x, y))
            if (x, y, direction_index) in visited_with_direction:
                #print(f"Loop detected at ({x}, {y}) in direction {directions[direction_index]}")
                loops += 1
                break
            visited_with_direction.add((x, y, direction_index))
            dx, dy = directions[direction_index]
            new_x, new_y = x + dx, y + dy
            # if new position is off the grid, we stop
            if (new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0])):
                #print(f"Moved off the grid to ({new_x}, {new_y}), stopping")
                break
            # if we hit an obstacle, we turn right
            elif (grid[new_x][new_y] == OBSTACLE or (new_x, new_y) == (row,col)):
                direction_index = (direction_index + 1) % 4  # Turn right
                #print(f"Hit obstacle at ({new_x}, {new_y}), turning right to direction {directions[direction_index]}")
            
            else:
                x, y = new_x, new_y
                #print(f"Moved to ({x}, {y})")

print('part 1 answer',len(visited))
print('part 2 answer',loops)
