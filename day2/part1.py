import os

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = [(line.strip().split()) for line in f.readlines()]
    f.close()

    for i, _ in enumerate(data): data[i][1] = int(data[i][1])

    horizontal_distance = 0 # Increments with "forward"
    depth = 0 # Increments with "down", decrements with "up"
    for _, line in enumerate(data):
        match line[0]:
            case "up":
                depth -= line[1]
            case "down":
                depth += line[1]
            case "forward":
                horizontal_distance += line[1]
    return depth * horizontal_distance

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(process_input(inputFile))