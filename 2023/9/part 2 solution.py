with open(r'advent_of_code\2023\9\input.txt', 'r') as file:
    input = file.readlines()

# print(input)

test_input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

#input = test_input.split('\n')

def predict_next_number(line, is_reversed=True):
    numbers = [int(number) for number in line.split(' ')]
    if is_reversed == True:
        numbers.reverse()  # Reverse the list of numbers
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    if len(set(differences)) == 1:  
    # The sequence is simple arithmetic
        previous_number = numbers[-1] + differences[0]
    else:
    # The sequence might be quadratic or more complex rule
        second_differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
        if len(set(second_differences)) == 1:  # The sequence is quadratic
            previous_difference = differences[-1] + second_differences[0]
            previous_number = numbers[-1] + previous_difference
        else: 
    # The sequence follows a more complex rule
            differences_stack = [differences]
            while not all(difference == 0 for difference in differences):
                differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
                differences_stack.append(differences)

            # Now, work our way back up to predict the previous number
            previous_number = numbers[-1]
            for differences in reversed(differences_stack):
                previous_number += differences[-1]  # Add the last difference in the list
                differences.append(previous_number)  # Add the predicted number to the end of the list
    return previous_number

all_predictions = []
for line in input:
    prediction = predict_next_number(line)
    all_predictions.append(prediction)

total = 0
for prediction in all_predictions:
    total += prediction

print(f'Sum of predictions: {total}')