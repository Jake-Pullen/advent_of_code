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

input = input.split("\n")
grid = [list(x) for x in input]

# for x in grid:
#     print(x)

# we need to find the starting position
# our starting position is the only '^' in the grid
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == "^":
            position = (x, y)
            break
print('start at',position)

# We start by travelling north until we hit an obstacle '#'
# then we turn right and travel east until we hit an obstacle
# we keep turning right and travelling until we hit an obstacle
# once we make it off the grid we stop
# count how many unique squares we visit

def count_unique_squares(grid, start):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # North, East, South, West
    direction_index = 0  # Start by moving north
    x, y = start
    visited = set()

    while True:
        visited.add((x, y))
        dx, dy = directions[direction_index]
        new_x, new_y = x + dx, y + dy
        # if new position is off the grid, we stop
        if (new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0])):
            print(f"Moved off the grid to ({new_x}, {new_y}), stopping")
            break
        # if we hit an obstacle, we turn right
        elif grid[new_x][new_y] == OBSTACLE:
            direction_index = (direction_index + 1) % 4  # Turn right
            print(f"Hit obstacle at ({new_x}, {new_y}), turning right to direction {directions[direction_index]}")
        
        else:
            x, y = new_x, new_y
            print(f"Moved to ({x}, {y})")

    return len(visited)

print(count_unique_squares(grid, position))