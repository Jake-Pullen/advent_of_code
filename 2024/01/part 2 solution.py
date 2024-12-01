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

# for every item in the left list we need to count how many times it appears in the right list

score = []
for i in left_list:
    if i in right_list:
        score.append(i * right_list.count(i))


#print(score)
print(sum(score))