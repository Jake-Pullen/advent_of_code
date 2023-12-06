import os
from advent_of_code.get_puzzle_text import save_puzzle_text

year = 2022
day = 7
save_puzzle_text(year, day)

with open(r'advent_of_code\2022\day_7\input.txt', 'r') as file:
    input = file.read()

print(input)
