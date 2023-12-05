with open(r'advent_of_code\2023\day_5\input.txt', 'r') as file:
    input = file.readlines()

with open(r'advent_of_code\2023\day_5\test_input.txt', 'r') as file:
    test_input = file.readlines()

#input = test_input

# print(input)

# find the seed numbers
seed_numbers = input[0].split(':')[1].strip().split(' ')
#print(seed_numbers)

#first we need to split the seed map into lists of 2 numbers
seed_map = []
for i in range(0, len(seed_numbers), 2):
    seed_map.append(seed_numbers[i:i+2])
#print(seed_map)

# find the instructions
line_seed_to_soil_map = input.index('seed-to-soil map:\n')
line_soil_to_fertilizer_map = input.index('soil-to-fertilizer map:\n')
line_fertilizer_to_water_map = input.index('fertilizer-to-water map:\n')
line_water_to_light_map = input.index('water-to-light map:\n')
line_light_to_temperature_map = input.index('light-to-temperature map:\n')
line_temperature_to_humidity_map = input.index('temperature-to-humidity map:\n')
line_humidity_to_location_map = input.index('humidity-to-location map:\n')

# get the instructions for each map
seed_to_soil_map_instructions = input[line_seed_to_soil_map+1:line_soil_to_fertilizer_map]
soil_to_fertilizer_map_instructions = input[line_soil_to_fertilizer_map+1:line_fertilizer_to_water_map]
fertilizer_to_water_map_instructions = input[line_fertilizer_to_water_map+1:line_water_to_light_map]
water_to_light_map_instructions = input[line_water_to_light_map+1:line_light_to_temperature_map]
light_to_temperature_map_instructions = input[line_light_to_temperature_map+1:line_temperature_to_humidity_map]
temperature_to_humidity_map_instructions = input[line_temperature_to_humidity_map+1:line_humidity_to_location_map]
humidity_to_location_map_instructions = input[line_humidity_to_location_map+1:]

def map_value(value, instructions):
    for instruction in instructions:
        instruction = instruction.strip()  # remove newline character
        if instruction:  # check if instruction is not empty
            destination_start, source_start, length = map(int, instruction.split())
            if source_start <= value < source_start + length:
                return destination_start + (value - source_start)
    return value  # if value is not in any range, it maps to itself


# Initialize the smallest location to a large number
smallest_location = float('inf')

for seed in seed_map:
    start = int(seed[0])
    count = int(seed[1])
    for seed_number in range(start, start + count):
        soil = map_value(seed_number, seed_to_soil_map_instructions)
        fertilizer = map_value(soil, soil_to_fertilizer_map_instructions)
        water = map_value(fertilizer, fertilizer_to_water_map_instructions)
        light = map_value(water, water_to_light_map_instructions)
        temperature = map_value(light, light_to_temperature_map_instructions)
        humidity = map_value(temperature, temperature_to_humidity_map_instructions)
        location = map_value(humidity, humidity_to_location_map_instructions)
        
        # Update smallest_location if a smaller location is found
        if location < smallest_location:
            smallest_location = location

# Print the smallest location
print(smallest_location)


