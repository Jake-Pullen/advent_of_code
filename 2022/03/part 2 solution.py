with open(r'D:\repos\advent_of_code\2022\03\input.txt', 'r') as file:
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

def task_2(file):
    # group 3 lines together, find the common item between all 3 lines
    # using ASCII
    priority = 0
    #take the input and split it into groups of 3 lines
    lines = file.split('\n')
    grouped_lines = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    for group in grouped_lines:
        common_items_set = set(group[0]).intersection(group[1], group[2])
        common_item = common_items_set.pop()
        ascii_start = 96 if common_item.islower() else 38
        priority += ord(common_item) - ascii_start
    print("Task 2 result: " + str(priority))
task_2(input)