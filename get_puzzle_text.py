import os
import requests
from datetime import datetime

def get_puzzle_text(year, day):
    with open(r'advent_of_code/session_cookie.txt', 'r') as file:
        session_cookie = file.read().strip()
    url = f"https://adventofcode.com/{year}/day/{day}"
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text

def get_puzzle_input(year, day):
    with open(r'advent_of_code/session_cookie.txt', 'r') as file:
        session_cookie = file.read().strip()
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    # Remove the trailing newline
    puzzle_input = response.text.strip()
    return puzzle_input

def save_puzzle_text(year, day):
    folder = rf"advent_of_code\{year}\day_{day}"
    os.makedirs(folder, exist_ok=True)
    input_file = os.path.join(folder, "puzzle_text.md")
    puzzle_text = get_puzzle_text(year, day)
    puzzle_text = puzzle_text.split('<main>')[1]
    puzzle_text = puzzle_text.split('</article>')[0]
    print(f'Saving puzzle text to {input_file}')
    with open(input_file, "w") as file:
        file.write(puzzle_text)

def save_puzzle_input(year, day):
    folder = rf"advent_of_code\{year}\day_{day}"
    os.makedirs(folder, exist_ok=True)
    input_file = os.path.join(folder, "input.txt")
    puzzle_input = get_puzzle_input(year, day)
    print(f'Saving puzzle input to {input_file}')
    with open(input_file, "w") as file:
        file.write(puzzle_input)

def save_part_2_puzzle_text(year, day):
    folder = rf"advent_of_code\{year}\day_{day}"
    input_file = os.path.join(folder, "puzzle_text.md")
    # grab the existing puzzle text
    with open(input_file, "r") as file:
        existing_puzzle_text = file.read()
    # Check if part 2 has already been added
    if "part2" in existing_puzzle_text:
        print("There is nothing more to add... Idiot.")
        return
    puzzle_text = get_puzzle_text(year, day)
    puzzle_text = puzzle_text.split('<main>')[1]
    #get all the text after the first </article> tag
    puzzle_text = puzzle_text.split('</article>')[1]
    # Remove everything after the puzzle text which is all the things after the </article> tag
    puzzle_text = puzzle_text.split('</article>')[0]
    # Add the existing puzzle text back in
    puzzle_text = existing_puzzle_text + puzzle_text
    print(f'Saving puzzle text to {input_file}')
    with open(input_file, "w") as file:
        file.write(puzzle_text)

def get_puzzle_part(year, day):
    # Check if the puzzle text for the day equals "# Day {day} Puzzle Text."
    folder = rf"advent_of_code\{year}\day_{day}"
    input_file = os.path.join(folder, "puzzle_text.md")
    # Create the file if it doesn't exist
    if not os.path.isfile(input_file):
        with open(input_file, "w") as file:
            pass
    # grab the existing puzzle text
    with open(input_file, "r") as file:
        existing_puzzle_text = file.read()
    if not existing_puzzle_text: # == f"# Day {day} Puzzle Text.":
        return 1
    else:
        return 2

# Usage example
current_year = datetime.now().year
current_day = datetime.now().day

def populate_data(year = current_year, day=current_day):
    """
    Populates data for the Advent of Code puzzle.
    Requires a session cookie to be saved in advent_of_code/session_cookie.txt

    This function checks if the puzzle text for the day equals "# Day {day} Puzzle Text."
    If it does, it saves the puzzle text and input for part 1.
    If not, it checks if part 2 has already been added to the puzzle text.
    If part 2 has not been added, it saves the puzzle text for part 2.

    Args:
        year (int): The year of the Advent of Code puzzle. Defaults to the current year.
        day (int): The day of the Advent of Code puzzle. Defaults to the current day.

    Returns:
        None
    """
    part_check = get_puzzle_part(year, day)
    if part_check == 1:
        save_puzzle_text(year, day)
        save_puzzle_input(year, day)
    elif part_check == 2:
        save_part_2_puzzle_text(year, day)
    else:
        print("Something went wrong. Check the puzzle text.")

populate_data()
