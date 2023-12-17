import heapq

with open(r'advent_of_code\2023\day_17\input.txt', 'r') as file:
    input = file.read()

test_input = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

# Read the input data from the file
#input_data = test_input
input_data = input


# Split the input data into lines
lines = input_data.split('\n')

# Create a grid from the lines
grid = [[char for char in row] for row in lines]

# Get the number of rows and columns in the grid
num_rows = len(grid)
num_columns = len(grid[0])

# Function to solve the problem
def solve():
    queue = [(0, 0, 0, -1, -1)]
    # Initialize the dictionary to store the minimum distance to each position
    min_distance = {}

    # While the queue is not empty
    while queue:
        # Pop the position with the smallest distance from the queue
        distance, row, column, direction, in_direction = heapq.heappop(queue)

        # If the position has already been visited
        if (row, column, direction, in_direction) in min_distance:
            continue

        # Update the minimum distance to the current position
        min_distance[(row, column, direction, in_direction)] = distance

        # For each possible move
        for i, (delta_row, delta_column) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            # Calculate the new position and direction
            new_row = row + delta_row
            new_column = column + delta_column
            new_direction = i
            new_in_direction = 1 if new_direction != direction else in_direction + 1

            # Check if the move is not a reverse move
            is_not_reverse = ((new_direction + 2) % 4 != direction)

            # Check if the move is valid
            is_valid = (new_in_direction <= 3)

            # If the new position is inside the grid and the move is not a reverse move and the move is valid
            if 0 <= new_row < num_rows and 0 <= new_column < num_columns and is_not_reverse and is_valid:
                # Calculate the cost of the move
                cost = int(grid[new_row][new_column])
                # Add the new position to the queue
                heapq.heappush(queue, (distance + cost, new_row, new_column, new_direction, new_in_direction))

    # Initialize the answer with a large number
    answer = 1e9

    # For each position in the dictionary
    for (row, column, direction, in_direction), value in min_distance.items():
        # If the position is the bottom right corner of the grid
        if row == num_rows - 1 and column == num_columns - 1:
            # Update the answer
            answer = min(answer, value)

    # Return the answer
    return answer

# Print the solution for part 1
print(solve())