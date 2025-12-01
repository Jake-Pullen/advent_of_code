testing = False

if not testing:
    with open(r"2025/01/input.txt", "r") as file:
        input = file.read()
else:
    input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

answer:int = 0
TEST_EXPECTED_ANSWER:int = 6

# make a list to simulate dial?
dial = [i for i in range(100)]

position:int = 50
zero_count: int = 0 

def move_dial_with_zero_count(current_position, movement):
    direction_to_move = movement[0]
    amount_to_move = int(movement[1:])
    
    # Determine the direction
    if direction_to_move == 'L':
        step = -1
    elif direction_to_move == 'R':
        step = 1
    else:
        raise ValueError("Invalid direction")
    
    # Count how many times we hit 0 during this rotation
    count = 0
    current = current_position
    
    # Go through each step of the rotation
    for _ in range(amount_to_move):
        current = (current + step) % 100
        if current == 0:
            count += 1

    return current, count

# Process each step
for step in input.strip().split('\n'):
    #print(f"Before: {position}")
    position, zero_count_increment = move_dial_with_zero_count(position, step)
    zero_count += zero_count_increment
    #print(f"After:  {position} (zero hits: {zero_count_increment})")

answer = zero_count

if testing:
    if answer == TEST_EXPECTED_ANSWER:
        print('test successful')
    else:
        print(f'wrong... expected {TEST_EXPECTED_ANSWER} received {answer}')
else:
    print(answer)

