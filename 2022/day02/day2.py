import os

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = f.readlines()
        return [line.strip() for line in data]

# For both parts:
# A = rock
# B = paper
# C = scissors
def part1(inputFile):
    # X = rock
    # Y = paper
    # Z = scissors
    scoreMap = {
        "A X": 4, # rock v. rock(me) -> draw(3) + rock(1) = 4
        "A Y": 8, # rock v. paper(me) -> win(6) + paper(2) = 8
        "A Z": 3, # rock v. scissors(me) -> loss(0) + scissors(3) = 3
        "B X": 1, # paper v. rock(me) -> loss(0) + rock(1) = 1
        "B Y": 5, # paper v. paper(me) -> draw(3) + paper(2) = 5
        "B Z": 9, # paper v. scissors(me) -> win(6) + scissors(3) = 9
        "C X": 7, # scissors v. rock(me) -> win(6) + rock(1) = 7
        "C Y": 2, # scissors v. paper(me) -> loss(0) + paper(2) = 2
        "C Z": 6, # scissors v. scissors(me) -> draw(3) + scissors(3) = 6
    }
    
    rounds = process_input(inputFile)
    
    total = 0
    for round in rounds:
        total += scoreMap[round]

    return total

def part2(inputFile):
    # X means I should lose
    # Y means I should draw
    # Z means I should win
    scoreMap = {
        "A X": 3, # LOSE: rock v. scissors(me) -> lose(0) + scissors(3) = 3
        "A Y": 4, # DRAW: rock v. rock(me) -> draw(3) + rock(1) = 4
        "A Z": 8, # WIN: rock v. paper(me) -> win(6) + paper(2) = 8
        "B X": 1, # LOSE: paper v. rock(me) -> loss(0) + rock(1) = 1
        "B Y": 5, # DRAW: paper v. paper(me) -> draw(3) + paper(2) = 5
        "B Z": 9, # WIN: paper v. scissors(me) -> win(6) + scissors(3) = 9
        "C X": 2, # LOSE: scissors v. paper(me) -> lose(0) + paper(2) = 2
        "C Y": 6, # DRAW: scissors v. scissors(me) -> draw(3) + scissors(3) = 6
        "C Z": 7, # WIN: scissors v. rock(me) -> win(6) + rock(1) = 7
    }
    
    rounds = process_input(inputFile)
    
    total = 0
    for round in rounds:
        total += scoreMap[round]

    return total

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(f"Part 1: {part1(inputFile)}")
    print(f"Part 2: {part2(inputFile)}")
