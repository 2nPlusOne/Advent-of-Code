import os

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = f.readlines()
    
    elves = []
    sum = 0
    for line in data:
        line = line.strip()
        if line == '':
            elves.append(sum)
            sum = 0
            continue
        sum+=int(line)          
    return elves

def part1(inputFile):
    input = process_input(inputFile=inputFile)
    sortedInput = sorted(input)
    return sortedInput[-1]

def part2(inputFile):
    input = process_input(inputFile=inputFile)
    sortedInput = sorted(input)
    return sum(sortedInput[::-1][:3])

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(f"Part 1: {part1(inputFile)}")
    print(f"Part 2: {part2(inputFile)}")