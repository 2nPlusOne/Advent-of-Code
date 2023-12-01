import os


def process_input(inputFile: str) -> int:
    with open(inputFile, "r") as f:
        ...


def part1(inputFile):
    ...


def part2(inputFile):
    ...


if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), "input.txt")
    print(f"Part 1: {part1(inputFile)}")
    print(f"Part 2: {part2(inputFile)}")
