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
    pass

def part2(inputFile):
    pass

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(input)
