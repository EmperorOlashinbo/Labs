import sys
import os


def read_lines(filename):
    if os.path.exists(filename):
        with open(filename, "r") as cars_file:
            file_lines = cars_file.readlines()
            return [line.strip() for line in file_lines]
    else:
        raise FileNotFoundError("An error occurred while trying to read the file.")


def parse_cars(list_of_strings):
    cars = []
    for line in list_of_strings:
        name, max_range = line.split(":")
        max_range = int(max_range)
        cars.append((name, max_range))
    return cars


def calculate_percentage(distance, cars):
    percentages = []
    for car in cars:
        name, max_range = car
        if max_range == 0:
            formatted_percentage = f"{name} -->  Distance exceeds max range (100%)"
        elif distance > max_range:
            percentage = round((distance / max_range) * 100)
            formatted_percentage = (
                f"{name.ljust(36)} -->  Distance exceeds max range ({percentage}%)"
            )
        else:
            percentage = round(100 * (distance / max_range))
            formatted_percentage = f"{name.ljust(36)} -->  {percentage}%"
        percentages.append((formatted_percentage))
    return percentages


def display_result(percentages):
    print("To drive the specified distance would correspond to this many")
    print("percent of each cars specified max range.")
    for percentage in percentages:
        print(percentage)


def main():
    if len(sys.argv) != 2:
        return

    lab2_3 = sys.argv[1]

    if os.path.exists(lab2_3):
        file_lines = read_lines(lab2_3)
        cars = parse_cars(file_lines)
        distance = int(input())
        percentages = calculate_percentage(distance, cars)
        display_result(percentages)
    else:
        print("An error occurred while trying to read the file.")


if __name__ == "__main__":
    main()
