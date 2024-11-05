import sys
import pickle
import os

TRANSLATION = {
    "1": " ",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "*": " ",
    "0": " ",
    "#": " ",
}


def read_orders(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(
            "Error: There was a problem with at least one of the files."
        )
    with open(filename, "rb") as orders_file:
        return pickle.load(orders_file)


def read_words(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(
            "Error: There was a problem with at least one of the files."
        )
    with open(filename, "r") as words_file:
        return [word.strip() for word in words_file]


def find_all_possible_combinations(order_number):
    if not order_number:
        return []

    combinations = [""]
    for digit in order_number:
        combinations = add_digit(digit, combinations)
    return combinations


def add_digit(digit, combinations):
    if not combinations:
        return [letter for letter in TRANSLATION[digit]]

    new_combination = [""]
    letters = TRANSLATION[digit]

    for combination in combinations:
        for letter in letters:
            new_combination.append(combination + letter)
    return new_combination


def filter_valid_words(possible_combinations, valid_words):
    valid_combinations = [word for word in possible_combinations if word in valid_words]
    return valid_combinations


def display_possible_words(order_number, words):
    possible_combinations = find_all_possible_combinations(order_number)
    valid_words = filter_valid_words(possible_combinations, words)

    if valid_words:
        print(f"{order_number} : {valid_words[0]}")
        for word in valid_words[1:]:
            print(f"        {word}")
    else:
        print(f"{order_number} : No real word found.")


def main():
    if len(sys.argv) != 3:
        return

    orders_file = sys.argv[1]
    words_file = sys.argv[2]

    try:
        order_numbers = read_orders(orders_file)
        words = read_words(words_file)
    except FileNotFoundError:
        print("Error: There was a problem with at least one of the files.")
        return
    for order_number in order_numbers:
        display_possible_words(order_number, words)


if __name__ == "__main__":
    main()
