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
TEST_EXPECTED_ANSWER:int = 3

# make a list to simulate dial?
dial = [i for i in range(100)]
#print(dial)

direction = {
    'L':'-=',
    'R':'+='
}

position:int = 50

def perform_operation(value, operator, operand):
    if operator == "+=":
        return value + operand
    elif operator == "-=":
        return value - operand
    else:
        raise ValueError("Unsupported operator")

def move_dial(position, movement):
    #print(movement)
    direction_to_move = movement[0]
    amount_to_move = movement[1:]
    #print(direction_to_move)
    #print(amount_to_move)
    decide = direction[direction_to_move]
    #print(decide)
    new_position = perform_operation(int(position), decide, int(amount_to_move))
    return new_position % 100

win_counter:int = 0
for step in input.split('\n'):
    #print(position)
    position = move_dial(position, step)
    #print(position)
    #print(dial[position])
    if dial[position] == 0:
        win_counter += 1

answer = win_counter

if testing:
    if answer == TEST_EXPECTED_ANSWER:
        print('test successful')
    else:
        print(f'wrong... expected {TEST_EXPECTED_ANSWER} received {answer}')
else:
    print(answer)

