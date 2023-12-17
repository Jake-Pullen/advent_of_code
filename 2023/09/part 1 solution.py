with open(r'advent_of_code\2023\09\input.txt', 'r') as file:
    input = file.readlines()

# print(input)

test_input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


#input = test_input.split('\n')

def predict_next_number(line):
    numbers = [int(number) for number in line.split(' ')]
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    if len(set(differences)) == 1:  # The sequence is simple arithmetic
        #print('simple')
        next_number = numbers[-1] + differences[0]
    else:  # The sequence might be quadratic or more complex rule
        second_differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
        if len(set(second_differences)) == 1:  # The sequence is quadratic
            #print('quadratic')
            next_difference = differences[-1] + second_differences[0]
            next_number = numbers[-1] + next_difference
        else: 
            # The sequence follows a more complex rule
            # we need to break this down into a series of arithmetic sequences
            # # Keep finding differences until all differences are 0
            #print('complex')
            # Keep finding differences until all differences are 0
            differences_stack = [differences]
            while set(differences) != {0}:
                differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
                differences_stack.append(differences)

            # Now, work our way back up to predict the next number
            next_number = numbers[-1]
            for differences in reversed(differences_stack):
                next_number += differences[-1]  # Add the last difference in the list
                differences.append(next_number)  # Add the predicted number to the end of the list
    return next_number

all_predictions = []
for line in input:
    prediction = predict_next_number(line)
    all_predictions.append(prediction)
    #print(f'line: {line}  ({prediction})')

sum_of_predictions = sum(all_predictions)
print(f'Sum of predictions: {sum_of_predictions}')