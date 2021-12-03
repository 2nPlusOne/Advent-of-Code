import os

def process_input_aggregated(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = f.readlines()
    f.close()
    
    data = [int(line.strip()) for line in data]
    sliding_window = [sum(data[i:i+3]) for i, _ in enumerate(data)]

    total = 0
    for i in range (1, len(sliding_window)):
        if sliding_window[i] > sliding_window[i-1]:
            total += 1
    return total

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(process_input_aggregated(inputFile))