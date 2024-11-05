import os


def file_exists(filename):
    return os.path.exists(filename)


def read_file(filename):
    numbers = []
    if file_exists(filename):
        with open(filename, "r") as numbers_file:
            for line in numbers_file:
                numbers.extend([int(num) for num in line.split()])
    else:
        print(f"File '{filename}' not exist.")
    return numbers


def filter_odd_or_even(numbers, keep_odd):
    return (
        [num for num in numbers if num % 2 == 1]
        if keep_odd
        else [num for num in numbers if num % 2 == 0]
    )


def reversed_bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def main():
    import sys

    if len(sys.argv) != 3:
        return

    lab2_5_1 = sys.argv[1]
    lab2_5_2 = sys.argv[2]

    odd_numbers = filter_odd_or_even(read_file(lab2_5_1), True)
    even_numbers = filter_odd_or_even(read_file(lab2_5_2), False)

    combined_numbers = odd_numbers + even_numbers
    reversed_bubble_sort(combined_numbers)

    print(combined_numbers)


if __name__ == "__main__":
    main()
