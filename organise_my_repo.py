import os

# Define the base directory where you want to create the folders
base_dir = 'advent_of_code_2023'

# Loop over the range 1 to 25 (inclusive)
for i in range(1, 26):
    # Construct the folder name
    folder_name = f"day_{i}"
    
    # Construct the full path to the folder
    folder_path = os.path.join(base_dir, folder_name)
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)

    # Construct the full path to the placeholder file
    input_file_path = os.path.join(folder_path, "input.txt")
    puzzle_file_path = os.path.join(folder_path, "puzzle_text.md")
    solution_file_path = os.path.join(folder_path, "solution.py")

    # Create the placeholder file
    with open(input_file_path, "w") as file:
        file.write("Paste any inputs into this file.")
    
    # Create the puzzle file
    with open(puzzle_file_path, "w") as file:
        file.write( f"# Day {i} Puzzle Text.")
    
    # Create the solution file
    with open(solution_file_path, "w") as file:
        file.write("import os\n\n")
