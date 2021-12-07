import os

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        positions = [int(num) for num in f.read().split(',')]

    fuel_sum = 1000000000000000000000000
    pos = 0
    # Fuel consumption is optimized at the list's average position
    average_pos = sum(positions) // len(positions) # Floor of average position
    for i in range(average_pos, average_pos + 2): # Check position on either side of average
        print(i)
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