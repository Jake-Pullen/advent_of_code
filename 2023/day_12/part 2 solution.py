with open(r'advent_of_code\2023\day_12\input.txt', 'r') as file:
    input = file.readlines()

test_input = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1''' 
test_input = test_input.split('\n')
#input = test_input

# Initialize the total number of arrangements
total_arrangements = 0
# Dictionary for memoization
memo = {}

def count_arrangements(springs:str, blocks:list, spring_index:int, block_index:int, current_block_length:int) -> int:
    """
    This function calculates the number of valid arrangements of springs and blocks.

    Parameters:
    springs (str): A string of characters, each of which is either '.', '#' or '?'.
    blocks (list): A list of integers representing the blocks.
    spring_index (int): The current index in `springs`.
    block_index (int): The current index in `blocks`.
    current_block_length (int): The current number of consecutive '#' characters.

    Returns:
    int: The number of valid arrangements for the current state.

    """
    # Create a key for the current state
    state_key = (spring_index, block_index, current_block_length)

    # If the result for the current state is already computed, return it
    if state_key in memo:
        return memo[state_key]

    # If all springs are processed
    if spring_index == len(springs):
        # If all blocks are used and there's no current block, or the last block is of correct size
        if (block_index == len(blocks) and current_block_length == 0) or \
           (block_index == len(blocks) - 1 and blocks[block_index] == current_block_length):
            return 1
        else:
            return 0

    # Initialize the number of arrangements for the current state
    arrangements = 0

    # Try both possibilities for the current spring ('.' or '#')
    for spring in ['.', '#']:
        # If the current spring can be the current possibility
        if springs[spring_index] == spring or springs[spring_index] == '?':
            # If the current spring is '.' and there's no current block
            if spring == '.' and current_block_length == 0:
                arrangements += count_arrangements(springs, blocks, spring_index + 1, block_index, 0)
            # If the current spring is '.' and the current block is of correct size
            elif spring == '.' and current_block_length > 0 and block_index < len(blocks) and blocks[block_index] == current_block_length:
                arrangements += count_arrangements(springs, blocks, spring_index + 1, block_index + 1, 0)
            # If the current spring is '#'
            elif spring == '#':
                arrangements += count_arrangements(springs, blocks, spring_index + 1, block_index, current_block_length + 1)

    # Store the result for the current state in the memoization dictionary
    memo[state_key] = arrangements

    # Return the number of arrangements for the current state
    return arrangements

# Process each line in the input
for line in input:
    # Split the line into springs and blocks
    springs, blocks_string = line.split()
    # add in 5 copies of the spring separated by a '?'
    springs = '?'.join([springs,springs,springs,springs,springs])
    # add in 5 copies of the block_string separated by a ','
    blocks_string = ','.join([blocks_string,blocks_string,blocks_string,blocks_string,blocks_string])
    # Convert the blocks string into a list of integers
    blocks = [int(x) for x in blocks_string.split(',')]
    # Clear the memoization dictionary
    memo.clear()
    # Calculate the number of arrangements for the current line
    line_arrangements = count_arrangements(springs, blocks, 0, 0, 0)
    # Add the number of arrangements for the current line to the total number of arrangements
    total_arrangements += line_arrangements

# Print the total number of arrangements
print(total_arrangements)