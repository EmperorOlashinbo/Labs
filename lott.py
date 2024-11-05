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

# Paths to the files
file1_path = "lott_1.txt"
file2_path = "lott_2.txt"

# Read the first file with numbers (1 to 35)
numbers1 = read_numbers_from_file(file1_path)

# Read the second file with numbers (0 to 9)
numbers2 = read_numbers_from_file(file2_path)

# Check if there are at least 7 numbers in the first file and 7 numbers in the second file
if len(numbers1) < 7 or len(numbers2) < 7:
    print("Error: Not enough numbers in one or both files to play Lotto.")
else:
    # Generate 7 random numbers from the first file
    random_numbers1 = random.sample(numbers1, 7)

    # Generate 1 random number from the second file (as the second set seems to be used for an additional number)
    random_numbers2 = random.sample(numbers2, 1)

    # Print the selected numbers
    print("Random numbers from the first file:", random_numbers1)
    print("Random number from the second file:", random_numbers2)
