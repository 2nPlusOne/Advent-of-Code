import os

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        positions = [int(num) for num in f.read().split(',')]

    # NOTE: This is a very (the most) inefficient way to do this. 
    #       Could be much faster with dynamic programming.
    fuel_sum = 1000000
    pos = 0
    for i in range(len(positions)):
        _pos = positions[i]
        _sum = 0
        for j in range(len(positions)):
            if positions[i] == positions[j]:
                continue
            _sum += abs(_pos - positions[j])
        if _sum < fuel_sum:
            fuel_sum = _sum
            pos = _pos
            
    print(f"Fuel required for position {pos}: {fuel_sum}")

if __name__ == '__main__':
    main()