import os

def process_input(inputFile: str):
    with open(inputFile, 'r') as f:
        return f.readline().strip()

def isUnique(xs: list[str]) -> bool: 
    return len(set(xs)) == len(xs)

def part1(data: str) -> int:
    """Find the index i of the last character of 
    a sequence of four non-repeating characters."""
    
    seq = list()
    
    for i in range(len(data)):
        if i <= 3:
            seq.append(data[i])
            continue
        
        if (isUnique(seq)):
            return i
        
        # otherwise, move forward
        seq.pop(0)
        seq.append(data[i])
        
    return -1


def part2(data: str, k: int) -> int:
    """Find the index i of the last character of 
    a sequence of k non-repeating characters."""  
    seq = list()
    
    for i in range(len(data)):
        if i <= k-1:
            seq.append(data[i])
            continue
        
        if (isUnique(seq)):
            return i
        
        # otherwise, move forward
        seq.pop(0)
        seq.append(data[i])
        
    return -1

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    data = process_input(filename)
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data, 14)}")