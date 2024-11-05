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
file1_path = "game-1.txt"
file2_path = "game-2.txt"

# Read the first file with numbers (1 to 50)
numbers1 = read_numbers_from_file(file1_path)

# Read the second file with numbers (1 to 12)
numbers2 = read_numbers_from_file(file2_path)

# Check if there are at least 5 numbers in the first file and 2 numbers in the second file
if len(numbers1) < 5 or len(numbers2) < 2:
    print("Error: Not enough numbers in one or both files to play Euro Jackpot lotto.")
else:
    # Generate 5 random numbers from the first file
    random_numbers1 = random.sample(numbers1, 5)

    # Generate 2 random numbers from the second file
    random_numbers2 = random.sample(numbers2, 2)

    # Print the selected numbers
    print("Random numbers from the first file:", random_numbers1)
    print("Random numbers from the second file:", random_numbers2)
