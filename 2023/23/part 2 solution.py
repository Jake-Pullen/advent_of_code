import sys
from collections import deque

with open(r'advent_of_code\2023\23\input.txt', 'r') as file:
    input = file.read()

test_input = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''

# Set recursion limit
sys.setrecursionlimit(10**6)

# Read input
input_data = input
lines = input_data.split('\n')

# Create grid from input
grid = [[char for char in row] for row in lines]
num_rows = len(grid)
num_cols = len(grid[0])

# Directions for navigation
directions = [['^',-1,0],['v', 1,0],['<', 0,-1],['>',0,1]]

def solve(is_part1):
    # Set of vertices
    vertices = set()

    # Identify vertices
    for row in range(num_rows):
        for col in range(num_cols):
            num_neighbors = 0
            for char,dr,dc in directions:
                if (0<=row+dr<num_rows and 0<=col+dc<num_cols and grid[row+dr][col+dc]!='#'):
                    num_neighbors += 1
            if num_neighbors>2 and grid[row][col]!='#':
                vertices.add((row,col))

    # Identify start and end points
    start, end = None, None
    for col in range(num_cols):
        if grid[0][col]=='.':
            vertices.add((0,col))
            start = (0,col)
        if grid[num_rows-1][col]=='.':
            vertices.add((num_rows-1,col))
            end = (num_rows-1,col)

    # Create edges
    edges = {}
    for vertex in vertices:
        edges[vertex] = []
        queue = deque([(vertex[0],vertex[1],0)])
        seen = set()
        while queue:
            r,c,d = queue.popleft()
            if (r,c) in seen:
                continue
            seen.add((r,c))
            if (r,c) in vertices and (r,c) != vertex:
                edges[vertex].append(((r,c),d))
                continue
            for char,dr,dc in directions:
                if (0<=r+dr<num_rows and 0<=c+dc<num_cols and grid[r+dr][c+dc]!='#'):
                    if is_part1 and grid[r][c] in ['<', '>', '^', 'v'] and grid[r][c]!=char:
                        continue
                    queue.append((r+dr,c+dc,d+1))

    # Depth-first search
    count = 0
    max_distance = 0
    seen_grid = [[False for _ in range(num_cols)] for _ in range(num_rows)]
    def dfs(v,d):
        nonlocal count
        nonlocal max_distance
        count += 1
        r,c = v
        if seen_grid[r][c]:
            return
        seen_grid[r][c] = True
        if r==num_rows-1:
            max_distance = max(max_distance, d)
        for (next_vertex,next_distance) in edges[v]:
            dfs(next_vertex,d+next_distance)
        seen_grid[r][c] = False

    # Start DFS from start point
    dfs(start,0)

    return max_distance

# Print results
print(solve(True))
print(solve(False))