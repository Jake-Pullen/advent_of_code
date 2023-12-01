
with open(r'advent_of_code\2022\day_1\input.txt', 'r') as file:
    input = file.read()

# print(input)

test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

# Split the data into groups
groups = input.split('\n\n')

# Now, each element of `groups` is a string containing the numbers in one group
# You can further split each group into individual numbers if needed
groups = [group.split('\n') for group in groups]

print(groups)

# sum up each group
sums = [sum(int(num) for num in group) for group in groups]

print(sums)

# show only largest sum
print(max(sums))