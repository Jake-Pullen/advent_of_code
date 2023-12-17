with open(r'advent_of_code\2023\5\input.txt', 'r') as file:
    input = file.readlines()

with open(r'advent_of_code\2023\5\test_input.txt', 'r') as file:
    test_input = file.readlines()

# input = test_input

# print(input)

lines = [line.strip('\r\n') for line in input]

seed_numbers = input[0].split(':')[1].strip().split(' ')
seeds = [int(num) for num in seed_numbers]

maps = {}
for line in lines[1:]:
    if line.endswith(' map:'):
        k = line.split()[0].split('-')
        k = (k[0], k[2])
        maps[k] = map = []
    elif line:
        # Split the line into parts
        parts = line.split()

        # Convert each part to an integer
        int_parts = [int(part) for part in parts]

        # Create a tuple from the list of integer parts
        x = tuple(int_parts)

        # Calculate the start and end of the range
        range_start = x[1]
        range_end = x[1] + x[2] - 1

        # Calculate the mapped start of the range
        mapped_start = x[0] - x[1]

        # Create a tuple representing the range and its mapped start
        range_tuple = ((range_start, range_end), mapped_start)

        # Append the tuple to the map
        map.append(range_tuple)
for map in maps.values():
    map.sort()


def map_range(rng, map):
    # Initialize a list with the input range
    ranges = [rng]
    # Initialize an empty list to store the result ranges
    result_range = []

    # Process each range in the list
    while ranges:
        # Flag to check if a match was found in the map
        matched = False
        # Get the current range
        start, end = rng = ranges.pop()

        # Check each entry in the map
        for src, delta in map:
            # Case 1: The end of the current range is within the source range
            if start < src[0] <= end <= src[1]:
                matched = True
                # Add the remaining part of the current range to the list
                ranges.append((start, src[0] - 1))
                # Add the mapped range to the result
                result_range.append((src[0] + delta, end + delta))

            # Case 2: The start of the current range is within the source range
            elif src[0] <= start <= src[1] < end:
                matched = True
                # Add the remaining part of the current range to the list
                ranges.append((src[1] + 1, end))
                # Add the mapped range to the result
                result_range.append((start + delta, src[1] + delta))

            # Case 3: The current range is entirely within the source range
            elif src[0] <= start <= end <= src[1]:
                matched = True
                # Add the mapped range to the result
                result_range.append((start + delta, end + delta))

            # Case 4: The current range entirely contains the source range
            elif start < src[0] <= src[1] < end:
                matched = True
                # Add the parts of the current range outside the source range to the list
                ranges.append((start, src[0] - 1))
                ranges.append((src[1] + 1, end))
                # Add the mapped range to the result
                result_range.append((src[0] + delta, src[1] + delta))

        # If no match was found in the map, add the current range to the result
        if not matched:
            result_range.append(rng)

    # Sort the result ranges
    result_range.sort()

    return result_range


ranges = []
for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = seeds[i] + seeds[i+1] - 1
    ranges.append((start, end))
k = 'seed'
# The loop continues until 'k' is equal to 'location'
while k != 'location':
    # Iterate over each item in the 'maps' dictionary
    for key, map in maps.items():
        # Check if the first element of the key matches 'k'
        if key[0] == k:
            # Initialize an empty list to store the new ranges
            new_range = []
            # Iterate over each range in the current list of ranges
            for item in ranges:
                # Map the current range using the current map
                # and add the resulting ranges to the new list
                new_range.extend(map_range(item, map))
            # Replace the current list of ranges with the new list
            ranges = new_range
            # Update 'k' to the second element of the key
            k = key[1]
            # Break out of the loop over the 'maps' dictionary
            break

print(min([result[0] for result in ranges]))
