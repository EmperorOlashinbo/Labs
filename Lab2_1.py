import sys
import os


def read_file(filename):
    with open(filename, "r") as log_file:
        file_lines = log_file.readlines()
        entries = []
        i = 0
        while i < len(file_lines):
            name = file_lines[i].strip()
            message = file_lines[i + 1].strip()
            entries.append((name, message))
            i += 2
        return entries


def display_entry(name, message):
    print(f"[{name}] --> {message}")


def search_and_display(name, entries):
    found_entries = [(n, m) for n, m in entries if n == name]
    if found_entries:
        # print(f'{name}:')
        for n, m in found_entries:
            display_entry(n, m)
    else:
        print(f"No messages found for {name} in the log file.")


def main():
    if len(sys.argv) != 2:
        return

    lab2_1 = sys.argv[1]

    if not os.path.exists(lab2_1):
        print(f"Error: The file '{lab2_1}' could not be found.")

    try:
        entries = read_file(lab2_1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: ")
        return

    while True:
        search_name = input()
        search_and_display(search_name, entries)
        return search_name


if __name__ == "__main__":
    main()
