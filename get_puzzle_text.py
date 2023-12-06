import os
import requests

def get_puzzle_text(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def get_puzzle_input(year, day):
    session_cookie = ''
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {'session': session_cookie}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text

def save_puzzle_text(year, day):
    folder = rf"advent_of_code\{year}\day_{day}"
    os.makedirs(folder, exist_ok=True)
    input_file = os.path.join(folder, "puzzle_text.md")
    puzzle_text = get_puzzle_text(year, day)
    # Remove everything before the puzzle text which is all the things inside the <main> tag
    puzzle_text = puzzle_text.split('<main>')[1]
    # Remove everything after the puzzle text which is all the things after the </article> tag
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


# Usage example
year = 2022
day = 7
save_puzzle_text(year, day)
save_puzzle_input(year, day)





