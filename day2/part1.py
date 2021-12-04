import os

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        instructions = [(line.strip().split()) for line in f.readlines()]
    f.close()

    for instruction in instructions: instruction[1] = int(instruction[1])

    horizontal_distance = 0 # Increments with "forward"
    depth = 0 # Increments with "down", decrements with "up"
    for instruction in instructions:
        value = instruction[1]
        match instruction[0]:
            case "up":
                depth -= value
            case "down":
                depth += value
            case "forward":
                horizontal_distance += value
    return depth * horizontal_distance

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(process_input(inputFile))