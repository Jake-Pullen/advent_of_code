import os 


def delete_specific_files(directory, file_names):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename in file_names:
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)
                print(f'Deleted {file_path}')

# delete_specific_files('advent_of_code', ['input.txt', 'puzzle_text.md'])
                

import pathlib

def rename_folders_and_update_files(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        base_foldername = os.path.basename(foldername)
        if base_foldername.isdigit() and len(base_foldername) == 1:
            new_foldername = '0' + base_foldername
            new_full_path = os.path.join(os.path.dirname(foldername), new_foldername)
            os.rename(foldername, new_full_path)
            print(f'Renamed {foldername} to {new_full_path}')
            
            for filename in filenames:
                if filename.endswith('solution.py'):
                    file_path = pathlib.Path(new_full_path) / filename
                    content = file_path.read_text()
                    updated_content = content.replace(foldername, new_full_path)
                    file_path.write_text(updated_content)
                    print(f'Updated file reference in {file_path}')

rename_folders_and_update_files('advent_of_code')
