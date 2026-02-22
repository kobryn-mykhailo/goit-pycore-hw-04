# hw.04 Task 1: Extract aggregated and average salary for the employees

def total_salary(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                parts = line.split(',')
                salary = int(parts[1])
                total = total + salary
                count = count + 1
            average = total / count
            return (total, average)
                

    except FileNotFoundError:
        print(f"File {path} not found.")
        return None
    

total, average = total_salary("data/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # verification of the function result


# hw.04 Task 2: Extract informatin about cats from the external file and present it in dictionary

def get_cats_info(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            cats = []
            for line in file:
                cat = line.strip()
                cat_parameters = cat.split(',')
                cat_dictionary = ({
                    "id": cat_parameters[0],
                    "name": cat_parameters[1],
                    "age": cat_parameters[2]
                })
                cats.append(cat_dictionary)
            return cats
        
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None

# print(get_cats_info("data/cats.txt")) # verification of the function result


# hw.04 Task 3: Setting up virtual environment

import sys
from pathlib import Path
from colorama import init, Fore

# initialize colorama so colors work on Windows
init()

def print_directory_structure(path, level=0):
    # create indent string using dashes, more dashes = deeper level
    indent = "-" * level

    # go through all items in the folder, sorted alphabetically
    for item in sorted(path.iterdir()):
        if item.is_dir():
            # if it's a folder - print in blue color
            print(f"{indent}{Fore.BLUE}{item.name}{Fore.RESET}")
            # call the same function for this subfolder, increasing indent by 2
            print_directory_structure(item, level + 2)
        else:
            # if it's a file - print in green color
            print(f"{indent}{Fore.GREEN}{item.name}{Fore.RESET}")


# check if user provided a path as command line argument
if len(sys.argv) < 2:
    print("Usage: python homework_04.py <directory_path>")
    sys.exit(1)

# convert the string argument to a Path object
directory = Path(sys.argv[1])

# check if the path actually exists
if not directory.exists():
    print(f"Error: path '{directory}' does not exist.")
    sys.exit(1)

# check if it's a directory and not a file
if not directory.is_dir():
    print(f"Error: '{directory}' is not a directory.")
    sys.exit(1)

# print the root folder name and start the recursive function
print(f"{Fore.BLUE}{directory.name}{Fore.RESET}")
print_directory_structure(directory)

# test sample to run in terminal: "python homework_04.py venv\Lib\site-packages\colorama"