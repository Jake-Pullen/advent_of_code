with open(r'2024/01/input.txt', 'r') as file:
    input = file.read()

test_input = '''3   4
4   3
2   5
1   3
3   9
3   3'''


# first split the input into two lists, left and right
left_list = []
right_list = []

for line in input.split('\n'):
    left, right = line.split('   ')
    left_list.append(int(left))
    right_list.append(int(right))

# now sort each list acecnding
left_list.sort()
right_list.sort()
# print('left ',left_list)
# print('right',right_list)

# now compare each element in the left list with the corresponding element in the right list
# we need to get the difference between the two elements
diff_list = []
for i in range(len(left_list)):
    diff_list.append(abs(left_list[i] - right_list[i]))

# print(diff_list)

# now we sum up all the items in the list

print(sum(diff_list))
