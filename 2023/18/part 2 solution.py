with open(r'advent_of_code\2023\18\input.txt', 'r') as file:
    input = file.read()

test_input = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

# input = test_input
input = input.split('\n')

# Initialize a list of points with the origin (0, 0)
points = [(0, 0)]

# Define the directions for "Up", "Down", "Left", "Right"
directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

# Initialize a variable to keep track of the total distance moved
total_distance = 0

# Read each line from the input
for line in input:
    # Ignore the first two parts of the line, get the third part
    _, _, third_part = line.split()
    
    # Remove the first two characters and the last character from the third part
    third_part = third_part[2:-1]
    
    # Get the direction and number of steps from the third part
    direction, num_steps = directions["RDLU"[int(third_part[-1])]], int(third_part[:-1], 16)
    
    # Add the number of steps to the total distance
    total_distance += num_steps
    
    # Get the last point we moved to
    last_point = points[-1]
    
    # Calculate the new point after moving in the current direction
    new_point = (last_point[0] + direction[0] * num_steps, last_point[1] + direction[1] * num_steps)
    
    # Add the new point to the list of points
    points.append(new_point)

# Calculate the area of the polygon formed by the points
area = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2

# Calculate the number of interior points
interior_points = area - total_distance // 2 + 1

# Print the total number of points covered
print(interior_points + total_distance)
