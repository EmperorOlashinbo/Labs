import os
import pickle
import sys


class FileNotFundException(Exception):
    pass


def display_menu():
    print()
    print("1. Add file")
    print("2. Calculate")
    print()


def cross_reference(files):
    numbers = set()
    for file in files:
        with open(file, "r") as crime_file:
            file_numbers = set(line.strip() for line in crime_file)
            if not numbers:
                numbers = file_numbers
            else:
                numbers &= file_numbers
    return numbers


def map_numbers_to_names(numbers, filename):
    if not os.path.exists(filename):
        raise FileNotFundException(
            f"Error: There was a problem with at least one of the files."
        )

    with open(filename, "rb") as crime_file:
        mapping = pickle.load(crime_file)

    names = []
    for number in numbers:
        name = mapping.get(number, f"Unknown ({number})")
        names.append(name)
    return names


def display_suspects(names):
    print()
    print("The following persons was present on all crime scenes:")
    print("-" * 54)

    if names:
        for name in names:
            print(name)
    else:
        print("No matches")


def main():
    if len(sys.argv) != 2:
        print("Error: There was a problem with at least one of the files.")
        return

    mapping_filename = sys.argv[1]
    # display_menu()
    files = []

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            file_path = input("Enter a filename (include full path): ")
            print()
            if not os.path.exists(file_path):
                print(f"Error: There was a problem with at least one of the files.")
                files.append(file_path)
                return files
            else:
                files.append(file_path)
        elif choice == "2":
            break
        else:
            print("Invalid choise. Please select 1 to add a file or 2 to calculate.")

    if not files:
        print("Error: There was a problem with at least one of the files.")
        return

    try:
        numbers = cross_reference(files)
        names = map_numbers_to_names(numbers, mapping_filename)
        display_suspects(names)
    except FileNotFundException:
        print("Error: There was a problem with at least one of the files.")


if __name__ == "__main__":
    main()
