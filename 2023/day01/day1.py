import os
import re

spelled_digits = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def process_input(inputFile: str) -> int:
    with open(inputFile, "r") as f:
        return [line.strip() for line in f.readlines()]


def part1(inputFile):
    """Combines the first and last digits of each line into a number, and sums them."""
    lines = process_input(inputFile)
    numbers = []
    for line in lines:
        digits = re.findall(r"\d", line)
        numbers.append(int(digits[0] + digits[-1]))

    return sum(numbers)


def part2(inputFile):
    """Also handles spelled-out digits."""
    lines = process_input(inputFile)
    numbers = []  # the numbers from each line
    for line in lines:
        line_digits = []  # the digits from this line
        for i in range(len(line)):
            if line[i].isdigit():  # Check for digits
                line_digits.append(line[i])
                continue
            for word in spelled_digits.keys():  # Check for spelled-out digits
                if line[i:].startswith(word):
                    line_digits.append(spelled_digits[word])
                    break
        numbers.append(int(line_digits[0] + line_digits[-1]))

    return sum(numbers)


if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), "input.txt")
    testFile = os.path.join(os.path.dirname(__file__), "test2.txt")
    print(f"Part 1: {part1(inputFile)}")
    print(f"Part 2: {part2(inputFile)}")
