import random
import os

def read_numbers_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            numbers = [int(num) for line in file for num in line.split() if num.isdigit()]
            return numbers
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except ValueError:
        print(f"Error: The file {file_path} contains non-numeric values.")
        return []

# Path to the file and the number of numbers to draw
file1_path = "ken70.txt"
numbers_to_draw = 11  # Adjust this number as needed for your Keno game

# Read the file with numbers (1 to 70)
numbers1 = read_numbers_from_file(file1_path)

# Check if there are enough numbers in the file
if len(numbers1) < numbers_to_draw:
    print(f"Error: Not enough numbers in the file to draw {numbers_to_draw} numbers.")
else:
    # Generate the specified number of random numbers from the file
    random_numbers1 = random.sample(numbers1, numbers_to_draw)

    # Print the selected numbers
    print(f"Random numbers from the file ({numbers_to_draw}):", random_numbers1)
