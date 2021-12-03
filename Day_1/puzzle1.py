import os

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = f.readlines()
    f.close()
    
    data = [int(line.strip()) for line in data]
    total = 0
    for i in range (1, len(data)):
        if data[i] > data[i-1]:
            total += 1
    return total

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(process_input(inputFile))