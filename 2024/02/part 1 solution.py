with open(r'2024/02\input.txt', 'r') as file:
    input = file.read()

test_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

# for each line we want to compare the current number to the next number
# if the number is between 1 and 3 difference it is valid
# we also need to know and store if it is ascending or descending
# because all numbers need to be ascending or descending and not mixed
# this will mean the line is valid

valid_list_count = 0

for line in input.split('\n'):
    safe = False
    line = line.split()
    list_line = [int(i) for i in line]

    # check all numbers in the line are ascending or descending
    if list_line == sorted(list_line) or list_line == sorted(list_line, reverse=True):
        #print(list_line, 'ascending or descending')
        safe = True
        print(list_line, 'steady')
    else:
        safe = False
        print(list_line, 'unsteady')
        continue

    for i, num in enumerate(list_line):
        if i == 0:
            continue
        check = abs(num - list_line[i-1])
        if check >= 4 or check == 0:
            #print(check)
            safe = False
        else:
            #print(check)
            safe = True
        if not safe:
            print(list_line, 'unsafe, big jumps')
            break

    if safe:
        print(list_line, 'safe')
        valid_list_count += 1



print(valid_list_count)

#print(valid_list_count)