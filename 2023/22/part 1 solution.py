from copy import deepcopy

with open(r'advent_of_code\2023\22\input.txt', 'r') as file:
    input = file.read()

test_input = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''

def parse_input(input_data):
    # Split the input data into lines
    lines = input_data.split('\n')

    # Initialize the list of bricks
    bricks = []

    # Parse each line into a brick
    for line in lines:
        start, end = line.split('~')
        start_x, start_y, start_z = map(int, start.split(','))
        end_x, end_y, end_z = map(int, end.split(','))

        # Initialize the current brick
        current_brick = []

        # Add all points in the brick to the current brick
        if start_x == end_x and start_y == end_y:
            assert start_z <= end_z
            for z in range(start_z, end_z + 1):
                current_brick.append((start_x, start_y, z))
        elif start_x == end_x and start_z == end_z:
            assert start_y <= end_y
            for y in range(start_y, end_y + 1):
                current_brick.append((start_x, y, start_z))
        elif start_y == end_y and start_z == end_z:
            assert start_x <= end_x
            for x in range(start_x, end_x + 1):
                current_brick.append((x, start_y, start_z))
        else:
            assert False

        # Add the current brick to the list of bricks
        bricks.append(current_brick)

    return bricks

def move_bricks_down(bricks):
    # Initialize the set of seen points
    seen_points = set()

    # Add all points in the bricks to the set of seen points
    for brick in bricks:
        for point in brick:
            seen_points.add(point)

    # Move all bricks down until they can't move anymore
    while True:
        moved = False
        for i, brick in enumerate(bricks):
            can_move = True
            for x, y, z in brick:
                if z == 1 or ((x, y, z - 1) in seen_points and (x, y, z - 1) not in brick):
                    can_move = False
            if can_move:
                moved = True
                for point in brick:
                    seen_points.discard(point)
                    seen_points.add((point[0], point[1], point[2] - 1))
                bricks[i] = [(x, y, z - 1) for x, y, z in brick]
        if not moved:
            break

    return bricks, seen_points

def count_stable_bricks(bricks, seen_points):

    # Initialize the counts of stable bricks and fallen bricks
    stable_bricks_count = 0

    # Check each brick
    for i, brick in enumerate(bricks):
        # Make a copy of the seen points and bricks
        current_seen_points = deepcopy(seen_points)
        current_bricks = deepcopy(bricks)

        # Remove the current brick from the seen points
        for point in brick:
            current_seen_points.discard(point)

        # Initialize the set of fallen bricks
        fallen_bricks = set()

        # Move all other bricks down until they can't move anymore
        while True:
            moved = False
            for j, other_brick in enumerate(current_bricks):
                if j == i:
                    continue
                can_move = True
                for x, y, z in other_brick:
                    if z == 1 or ((x, y, z - 1) in current_seen_points and (x, y, z - 1) not in other_brick):
                        can_move = False
                if can_move:
                    fallen_bricks.add(j)
                    for point in other_brick:
                        current_seen_points.discard(point)
                        current_seen_points.add((point[0], point[1], point[2] - 1))
                    current_bricks[j] = [(x, y, z - 1) for x, y, z in other_brick]
                    moved = True
            if not moved:
                break

        # Update the counts of stable bricks and fallen bricks
        if len(fallen_bricks) == 0:
            stable_bricks_count += 1

    return stable_bricks_count

def main():
    input_data = input
    bricks = parse_input(input_data)
    bricks, seen_points = move_bricks_down(bricks)
    stable_bricks_count = count_stable_bricks(bricks, seen_points)
    print(stable_bricks_count)

main()