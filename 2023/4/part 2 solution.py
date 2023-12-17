import os

with open(r'advent_of_code\2023\4\input.txt', 'r') as file:
    input = file.readlines()

# print(input)
test_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

#input = test_input.split('\n')

card_count = {}
for card in range(1,len(input)+1):
    card_count[card] = 1

for line in input:
    winning_numbers = []
    my_numbers = []
    line = line.split('|')
    card_number = line[0].split(':')[0].split()[1]
    winning_numbers = line[0].split(':')[1].split()
    my_numbers = line[1].split()
    print(f'card number: {card_number}')
    #print(f'my numbers are: {my_numbers}')
    #print(f'winning numbers are: {winning_numbers}')
    
    # loop for the amount of times we have a duplciate card
    for i in range(card_count[int(card_number)]):
        wins = 0
        for number in my_numbers:
            if number in winning_numbers:
                wins += 1
            else:
                pass 
        if wins > 0:
            #print(f'wins: {wins}')
            # add 1 duplicate card for each card following this one
            for win in range(int(wins)):
                add_duplicates = int(card_number) + 1 + win
                #print(f'add duplicates: {add_duplicates}')
                if add_duplicates in card_count:
                    card_count[add_duplicates] += 1
                else:
                    card_count[add_duplicates] += 0
                #print(f'card_count: {card_count}')

print(f'card_count: {card_count}')
#sum up all the values in the dictionary
total_cards = sum(card_count.values())
print(f'total cards: {total_cards}')

