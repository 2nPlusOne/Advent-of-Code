import os

scoreMap = {
    "A X": 4, # rock v. rock(me) -> draw(3) + rock(1) = 4            GOOD
    "A Y": 8, # rock v. paper(me) -> win(6) + paper(2) = 8          GOOD
    "A Z": 3, # rock v. scissors(me) -> loss(0) + scissors(3) = 3  GOOD
    "B X": 1, # paper v. rock(me) -> loss(0) + rock(1) = 1          GOOD
    "B Y": 5, # paper v. paper(me) -> draw(3) + paper(2) = 5        GOOD
    "B Z": 9, # paper v. scissors(me) -> win(6) + scissors(3) = 9   GOOD
    "C X": 7, # scissors v. rock(me) -> win(6) + rock(1) = 7        GOOD
    "C Y": 2, # scissors v. paper(me) -> loss(0) + paper(2) = 2     GOOD
    "C Z": 6, # scissors v. scissors(me) -> draw(3) + scissors(3) = 6 GOOD
}

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = f.readlines()
        return [line.strip() for line in data]

def part1(inputFile):
    rounds = process_input(inputFile)
    
    total = 0
    for round in rounds:
        total += scoreMap[round]

    return total

def part2(inputFile):
    pass

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(f"Part 1: {part1(inputFile)}")
    print(f"Part 2: {part2(inputFile)}")
