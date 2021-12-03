import os

def main():
    process_input("input.txt")

def process_input(inputFile: str):
    with open(inputFile, 'r') as f:
        data = f.readlines()
    f.close()
    
    data = [int(line.strip()) for line in data]
    total = 0
    for (i, x) in enumerate(data):
        if i < 1: return
        if x > data[i-1]:
            total += 1
    print(total)

if __name__ == "__main__":
    main()