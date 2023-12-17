with open(r'advent_of_code\2023\15\input.txt', 'r') as file:
    input_data = file.read()

test_input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
#input_data = test_input

# Function to calculate hash value
def calculate_hash(s):
    hash_value = 0
    for char in s:
        hash_value = ((hash_value + ord(char)) * 17) % 256
    return hash_value

# Function to process commands
def process_commands(commands, box):
    for command in commands:
        if command[-1] == '-':
            name = command[:-1]
            hash_value = calculate_hash(name)
            # Initialize an empty list for the updated box values
            updated_box_values = []

            # Iterate over each tuple in the box at the hash_value index
            for tuple_in_box in box[hash_value]:
                # Unpack the tuple into name (n) and value (v)
                n, v = tuple_in_box

                # If the name does not match the name to be removed, add it to the updated list
                if n != name:
                    updated_box_values.append((n, v))

            # Assign the updated list back to the box at the hash_value index
            box[hash_value] = updated_box_values
        elif command[-2] == '=':
            name = command[:-2]
            hash_value = calculate_hash(name)
            length = int(command[-1])
            # Initialize an empty list for the updated box values
            updated_box_values = []

            # Iterate over each tuple in the box at the hash_value index
            for tuple_in_box in box[hash_value]:
                # Unpack the tuple into name (n) and value (v)
                n, v = tuple_in_box

                # Check if the name matches the name in the command
                if name == n:
                    # If it matches, update the value to the new length
                    updated_value = length
                else:
                    # If it doesn't match, keep the original value
                    updated_value = v

                # Add the tuple with the name and updated value to the list
                updated_box_values.append((n, updated_value))

            # Assign the updated list back to the box at the hash_value index
            box[hash_value] = updated_box_values


# Split the commands
commands = input_data.split(',')

# Calculate the sum of hash values
sum_hash_values = 0
for command in commands:
    sum_hash_values += calculate_hash(command)
print(sum_hash_values)

# Initialize the box
box = [[] for _ in range(256)]

# Process the commands
process_commands(commands, box)