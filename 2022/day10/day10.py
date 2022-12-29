import os

def process_input(inputFile: str):
    with open(inputFile, 'r') as f:
        pass

def part1():
    """>.<"""
    pass

def part2():
    """>.<"""  
    pass

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    data = process_input(filename)
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")