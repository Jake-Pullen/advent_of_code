import os

with open(r'advent_of_code\2023\day_7\input.txt', 'r') as file:
    input = file.read()

#print(input)

test_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''' 

#input = test_input

# Split the input into lines
lines = input.split('\n')

# Process each line
processed_lines = []
for line in lines:
    # Strip leading/trailing whitespace and split the line into parts
    parts = line.strip().split()
    # Convert the second part to an integer and add the processed line to the list
    processed_lines.append((parts[0], int(parts[1])))

# Convert the list of processed lines to a tuple
hands = tuple(processed_lines)

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 'K', 'A']


def score(hand, joker=None):
    # Count the number of jokers in the hand
    jokers = 0 if joker is None else hand.count(joker)

    # Count the occurrences of each unique character in the hand, excluding jokers
    char_counts = [hand.count(x) for x in set(hand) if x != joker]

    # Sort the counts in descending order
    sorted_counts = sorted(char_counts, reverse=True)

    # If there are no counts (i.e., the hand was empty or contained only jokers), use [5] as the default
    sorted_counts = [5] if sorted_counts == [] else sorted_counts

    # Distribute the jokers among the counts
    for i, count in enumerate(sorted_counts):
        # The number of jokers to add to this count is the minimum of the number of jokers left and the number needed to reach 5
        jokers_to_add = min(5 - count, jokers)
        # Subtract the number of jokers added from the total number of jokers left
        jokers -= jokers_to_add
        # Add the jokers to the count
        sorted_counts[i] += jokers_to_add

    # Convert the counts to strings, join them into a single string, and pad it with zeros on the right
    count_str = ''.join(str(c) for c in sorted_counts).ljust(5, '0')

    # For each character in the hand, add its index in the 'cards' list (plus 1) to the string, treating jokers as 0
    for x in hand:
        count_str += str(0 if x == joker else cards.index(x) + 1).zfill(2)

    # Convert the final string to an integer and return it
    return int(count_str)


def total_winnings(hands, joker=None):
    # Sort the hands based on their score
    sorted_hands = sorted(hands, key=lambda x: score(x[0], joker))

    # Initialize the total winnings to 0
    total = 0

    # Process each hand
    for i, hand in enumerate(sorted_hands):
        # The winnings for a hand is its rank (i + 1) times its bet (hand[1])
        hand_winnings = (i + 1) * hand[1]
        # Add the winnings for this hand to the total
        total += hand_winnings

    # Return the total winnings
    return total


print(total_winnings(hands, joker='J'))