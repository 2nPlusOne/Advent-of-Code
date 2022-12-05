import os
from collections import namedtuple

Knapsack = namedtuple("Knapsack", "items left right")
issubclass(Knapsack, tuple)

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = []
        for line in f.readlines():
            line = line.strip()
            data.append(Knapsack(line, line[:len(line)//2], line[len(line)//2:]))
    
    return data

# used for both parts
azPriority = lambda c : 26 - (122-ord(c))
AZPriority = lambda c : 52 - (90 - ord(c))

def part1(knapsacks):
    def mapFunc(knap):
        item = set(knap.left).intersection(knap.right).pop()
        return azPriority(item) if ord(item) > 90 else AZPriority(item)
    
    return sum(map(mapFunc, knapsacks))

def part2(knapsacks):    
    count = 0
    for i in range(0, len(knapsacks), 3):
        badge = set(knapsacks[i].items).intersection(knapsacks[i+1].items).intersection(knapsacks[i+2].items).pop()
        count += azPriority(badge) if ord(badge) > 90 else AZPriority(badge)
    
    return count

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    knapsacks = process_input(filename)
    print(f"Part 1: {part1(knapsacks)}")
    print(f"Part 2: {part2(knapsacks)}")
