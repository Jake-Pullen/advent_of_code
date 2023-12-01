with open(r'advent_of_code\2022\day_3\input.txt', 'r') as file:
    input = file.read()

test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

def task_1(file):
    # Iterate over rucksacks, separate each in half and find out the priority of the common item between both halves
    # using ASCII
    priority = 0
    for line in file.split('\n'):
        middle_index = int(len(line) / 2)
        common_items_set = set(line[:middle_index]).intersection(line[middle_index:])
        common_item = common_items_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 1 result: " + str(priority))
task_1(input)