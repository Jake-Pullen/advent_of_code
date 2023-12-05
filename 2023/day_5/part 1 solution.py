from collections import defaultdict

with open(r'advent_of_code\2023\day_5\input.txt', 'r') as file:
    input = file.readlines()

with open(r'advent_of_code\2023\day_5\test_input.txt', 'r') as file:
    test_input = file.readlines()

#input = test_input

# print(input)

# find the seed numbers
seed_numbers = input[0].split(':')[1].strip().split(' ')
print(seed_numbers)


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


def build_instructions_map(instructions, instructions_map):
    for instruction in instructions:
        instruction = instruction.strip()  # remove newline character
        if instruction:  # check if instruction is not empty
            destination_start, source_start, length = map(int, instruction.split())
            for i in range(length):
                source = source_start + i
                destination = destination_start + i
                instructions_map[source] = destination

# build the seed to soil map using the instructions from the input
seed_to_soil_map = defaultdict(lambda: seed_to_soil_map)
soil_to_fertilizer_map = defaultdict(lambda: soil_to_fertilizer_map)
fertilizer_to_water_map = defaultdict(lambda: fertilizer_to_water_map)
water_to_light_map = defaultdict(lambda: water_to_light_map)
light_to_temperature_map = defaultdict(lambda: light_to_temperature_map)
temperature_to_humidity_map = defaultdict(lambda: temperature_to_humidity_map)
humidity_to_location_map = defaultdict(lambda: humidity_to_location_map)


build_instructions_map(seed_to_soil_map_instructions, seed_to_soil_map)
build_instructions_map(soil_to_fertilizer_map_instructions, soil_to_fertilizer_map)
build_instructions_map(fertilizer_to_water_map_instructions, fertilizer_to_water_map)
build_instructions_map(water_to_light_map_instructions, water_to_light_map)
build_instructions_map(light_to_temperature_map_instructions, light_to_temperature_map)
build_instructions_map(temperature_to_humidity_map_instructions, temperature_to_humidity_map)
build_instructions_map(humidity_to_location_map_instructions, humidity_to_location_map)

locations = []
# now we run the seed number through the maps 1 by 1 to get the final location
for seed_number in seed_numbers:
    soil = seed_to_soil_map[int(seed_number)]
    fertilizer = soil_to_fertilizer_map[soil]
    water = fertilizer_to_water_map[fertilizer]
    light = water_to_light_map[water]
    temperature = light_to_temperature_map[light]
    humidity = temperature_to_humidity_map[temperature]
    location = humidity_to_location_map[humidity]
    locations.append(location)

#print lowest location 
print(min(locations))


