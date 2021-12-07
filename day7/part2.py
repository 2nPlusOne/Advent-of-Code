import os

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        positions = [int(num) for num in f.read().split(',')]

    fuel_sum = 1000000000000000000000000
    pos = 0
    average_pos = sum(positions) // len(positions)
    # Best position will be close to the average position in the list
    for i in range(average_pos - 1, average_pos + 2):
        _fuel_sum = 0
        for j in range(len(positions)):
            _fuel_sum += sum_range(abs(i - positions[j]))
        if _fuel_sum < fuel_sum:
            fuel_sum = _fuel_sum
            pos = i

    print(f"Fuel required for position {pos}: {fuel_sum}")

def sum_range(n):
    return sum(range(1, n + 1))

if __name__ == '__main__':
    main()