import os
from statistics import median

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        positions = [int(num) for num in f.read().split(',')]

    # Fuel is optimized at the median position in list
    median_pos = int(median(positions))
    print(median_pos)
    fuel_sum = sum(abs(median_pos - num) for num in positions)
            
    print(f"Fuel required for position {median_pos}: {fuel_sum}")

if __name__ == '__main__':
    main()