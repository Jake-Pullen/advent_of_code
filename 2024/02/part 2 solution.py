testing = 0

if testing == 0: 
    with open(r'2024/02\input.txt', 'r') as file:
        input = file.read()
else:
    input = '''7 6 4 2 1
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
retest_list = []

    
def test_line(line):
    safe = False

    # check all numbers in the line are ascending or descending
    if line == sorted(line) or line == sorted(line, reverse=True):
        #print(line, 'ascending or descending')
        safe = True
        print(line, 'steady')
    else:
        safe = False
        print(line, 'unsteady')
        #retest_list.append(line)
        return 0

    for i, num in enumerate(line):
        if i == 0:
            continue
        check = abs(num - line[i-1])
        if check >= 4 or check == 0:
            #print(check)
            safe = False
        else:
            #print(check)
            safe = True
        if not safe:
            print(line, 'unsafe, big jumps')
            #retest_list.append(line)
            return 0
    return 1

reports = []
# convert the input to a list of lists
for line in input.split('\n'):
    data = line.split()
    reads = [int(i) for i in data]
    reports.append(reads)

#print(reports)

for report in reports:
    safe = test_line(report)
    if safe:
        print(report, 'safe')
        valid_list_count += 1
    else:
        #add the list to the retest list
        retest_list.append(report)

print(retest_list)

# # we need to iterate over the retest list
# but this time removing one number and doing the test again, 
# if it is safe we can add it to our safe count and move on
# if it is unsafe, we need to add back in our removed number and remove the next number
for list in retest_list:
    for i, num in enumerate(list):
        # remove the number
        test_list = list.copy()
        test_list.pop(i)
        safe = test_line(test_list)
        if safe:
            print(test_list, 'safe')
            valid_list_count += 1
            break

print(valid_list_count)