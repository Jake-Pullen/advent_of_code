import os

with open(r'd:\repos\advent_of_code\2022\04\input.txt', 'r') as file:
    input = file.read()

# print(input)


test_input = '''29-73,2-5
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

lines = input.split('\n')
contained_pairs = 0
for line in lines:
    #print(line)
    line = line.split(',')
    left_pair = line[0]
    right_pair = line[1]
    left_pair = left_pair.split('-')
    right_pair = right_pair.split('-')
    #print(left_pair)
    #print(right_pair)
    # right pair starts inbetween left pair
    if int(left_pair[0]) <= int(right_pair[0]) <= int(left_pair[1]):
        print('1',line)
        contained_pairs += 1
        continue
    # right pair ends inbetween left pair
    if int(left_pair[1]) >= int(right_pair[1]) >= int(left_pair[0]):
        print('2',line)
        contained_pairs += 1
        continue
    # left pair starts inbetween right pair
    if int(right_pair[0]) <= int(left_pair[0]) <= int(right_pair[1]):
        print('3',line)
        contained_pairs += 1
        continue
    # left pair ends inbetween right pair
    if int(right_pair[1]) >= int(left_pair[1]) >= int(right_pair[0]):
        print('4',line)
        contained_pairs += 1
        continue
    else:
        contained_pairs += 0

print(contained_pairs)
