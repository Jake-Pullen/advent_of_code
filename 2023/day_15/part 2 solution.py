with open(r'advent_of_code\2023\day_15\input.txt', 'r') as file:
    input_data = file.read()

test_input = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
# input_data = test_input

# Function to calculate hash value
def calculate_hash(string):
    hash_value = 0
    for char in string:
        hash_value = ((hash_value + ord(char)) * 17) % 256
    return hash_value

# Function to process commands
def process_commands(commands, box):
    # Iterate over each command in the list of commands
    for command in commands:
        # Check if the last character of the command is '-'
        if command[-1] == '-':
            # If it is, the command is to remove a name from the box
            # Extract the name from the command by removing the last character
            name_to_remove = command[:-1]
            # Calculate the hash value for the name
            hash_value = calculate_hash(name_to_remove)
            # Create a new list for the box at the hash value index, excluding the name to remove
            box[hash_value] = [(name, value) for (name, value) in box[hash_value] if name != name_to_remove]
        elif command[-2] == '=':
            # If the second last character of the command is '=', the command is to add or update a name in the box
            # Extract the name and the length from the command
            name_to_add_or_update = command[:-2]
            length = int(command[-1])
            # Calculate the hash value for the name
            hash_value = calculate_hash(name_to_add_or_update)
            # Check if the name is already in the box at the hash value index
            if name_to_add_or_update in [name for (name, value) in box[hash_value]]:
                # If it is, update the length for the name
                box[hash_value] = [(name, length if name == name_to_add_or_update else value) for (name, value) in box[hash_value]]
            else:
                # If it's not, add the name and length to the box at the hash value index
                box[hash_value].append((name_to_add_or_update, length))

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

# Function to calculate the product of indices and value
def calculate_product(index1, index2, value):
    return (index1 + 1) * (index2 + 1) * value

# Initialize the total sum
total_sum = 0

# Iterate over each box with its index
for box_index, box in enumerate(box):
    # Iterate over each tuple in the box with its index
    for tuple_index, (name, value) in enumerate(box):
        # Calculate the product using the function
        product = calculate_product(box_index, tuple_index, value)

        # Add the product to the total sum
        total_sum += product

# Print the total sum
print(total_sum)