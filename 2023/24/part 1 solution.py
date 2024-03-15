with open(r'advent_of_code\2023\24\input.txt', 'r') as file:
    input_data = file.read()

test_input = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

#input_data = test_input
input_lines = input_data.split('\n')

class Hailstone:
    def __init__(self, start_x, start_y, start_z, velocity_x, velocity_y, velocity_z):
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z
        
        self.a = velocity_y
        self.b = -velocity_x
        self.c = velocity_y * start_x - velocity_x * start_y
    
    def __repr__(self):
        return "Hailstone{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"

# Parse input lines into Hailstone objects
hailstones = [Hailstone(*map(int, line.replace("@", ",").split(","))) for line in input_lines]

total_intersections = 0

# Check each pair of hailstones for intersection
for i, hailstone1 in enumerate(hailstones):
    for hailstone2 in hailstones[:i]:
        a1, b1, c1 = hailstone1.a, hailstone1.b, hailstone1.c
        a2, b2, c2 = hailstone2.a, hailstone2.b, hailstone2.c
        # If lines are parallel, they do not intersect
        if a1 * b2 == b1 * a2:
            continue
        # Calculate intersection point
        x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
        # Check if intersection point is within bounds
        if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
            # Check if intersection point is in the same direction as the hailstones' velocities
            if all((x - hs.start_x) * hs.velocity_x >= 0 and (y - hs.start_y) * hs.velocity_y >= 0 for hs in (hailstone1, hailstone2)):
                total_intersections += 1

print(total_intersections)