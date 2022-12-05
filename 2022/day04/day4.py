import os
from collections import namedtuple

Pair = namedtuple("Pair", "left right")
issubclass(Pair, tuple)

Range = namedtuple("Range", "start end")
issubclass(Range, tuple)

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = []
        for line in f.readlines():
            line = line.strip().split(',')
            leftRange = line[0].split('-')
            rightRange = line[1].split('-')
            
            leftRange = Range(start=int(leftRange[0]), end=int(leftRange[1]))
            rightRange = Range(start=int(rightRange[0]), end=int(rightRange[1]))
            data.append(Pair(left=leftRange, right=rightRange))
    
    return data

def containsRange(a: Range, b: Range):
    """ Returns True if range a contains range b or vice versa."""
    if (a.start <= b.start and a.end >= b.end):
        return True
    if (a.start >= b.start and a.end <= b.end):
        return True
    
    return False

def part1(data: list[Pair]):
    """Count the number of times a pair consists of ranges such that 
        one range contains the other."""
    count = 0
    for pair in data:
        if containsRange(pair.left, pair.right): count += 1
        
    return count

def rangesOverlap(a: Range, b: Range):
    """Return True if range a overlaps with range b."""
    if (containsRange(a, b)): return True
    
    if b.start <= a.start <= b.end: 
        return True
    if a.start <= b.start <= a.end:
        return True
    
    return False

def part2(data):
    """Count the number of times a pair consists of overlapping ranges."""  
    count = 0
    for pair in data:
        if rangesOverlap(pair.left, pair.right): 
            count += 1
        
    return count

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    data = process_input(filename)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
