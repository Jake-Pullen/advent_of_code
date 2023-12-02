import os

with open(r'd:\repos\advent_of_code\2022\day_4\input.txt', 'r') as file:
    input = file.read()

# print(input)


test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

lines = input.split('\n')
contained_pairs = 0
for line in lines:
    print(line)
    line = line.split(',')
    left_pair = line[0]
    right_pair = line[1]
    left_pair = left_pair.split('-')
    right_pair = right_pair.split('-')
    #print(left_pair)
    #print(right_pair)
    left_range = int(left_pair[1]) - int(left_pair[0]) +1
    right_range = int(right_pair[1]) - int(right_pair[0]) +1
    #print(left_range)
    #print(right_range)
    if (left_range == right_range) and (left_pair[1] == right_pair[1]):
        #print('valid')
        contained_pairs += 1
    elif (left_range > right_range):
        # check to see if the right range starts and finishes within the left range
        if int(right_pair[0]) >= int(left_pair[0]) and int(right_pair[1]) <= int(left_pair[1]):
            contained_pairs += 1
        else:
            contained_pairs += 0
    elif (right_range > left_range):
        # check to see if the left range starts and finishes within the right range
        if int(left_pair[0]) >= int(right_pair[0]) and int(left_pair[1]) <= int(right_pair[1]):
            contained_pairs += 1
        else:
            contained_pairs += 0
    else:
        contained_pairs += 0
print(contained_pairs)