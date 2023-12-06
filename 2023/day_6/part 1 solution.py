with open(r'advent_of_code\2023\day_6\input.txt', 'r') as file:
    input = file.readlines()
with open(r'advent_of_code\2023\day_6\test_input.txt', 'r') as file:
    test_input = file.readlines()

#input = test_input

times_string = input[0].replace('Time:', '').split()
times = [int(time) for time in times_string if time]

distances_string = input[1].replace('Distance:', '').split()
distances = [int(distance) for distance in distances_string if distance]

time_and_distance = zip(times, distances)

def calculate_distances(race_time):
    max_distances = []
    for button_hold_time in range(race_time + 1):
        travel_time = race_time - button_hold_time
        distance_travelled = button_hold_time * travel_time
        max_distances.append(distance_travelled)
    return max_distances

count_valid_distances = []
for time, distance in time_and_distance:
    max_distances = calculate_distances(time)
    valid_distances = [max_distance for max_distance in max_distances if max_distance > distance]
    count_valid_distances.append(len(valid_distances))

#multiply the count of valid distances together 
print(count_valid_distances)
result = 1
for num in count_valid_distances:
    result *= num
print(result)