import os
import numpy as np

# This solution doesn't work yet.
def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    f.close()

    O2_rating, CO2_rating = data, data
    for i in range(12):
        m = most_common([row[i] for row in O2_rating])
        l = least_common([row[i] for row in CO2_rating])

        if len(O2_rating) > 1:
            O2_rating = [row for row in O2_rating if m == row[i]]
        
        if len(CO2_rating) > 1:
            CO2_rating = [row for row in CO2_rating if l == row[i]]
        
        print(f"i: {i}")
        print("O2 Ratings: ", O2_rating)
        print("CO2 Ratings: ", CO2_rating)
    return int(O2_rating[0], base=2) * int(CO2_rating[0], base=2)

def most_common(l: list) -> str:
    l = [int(n) for n in l]
    if sum(l) // len(l) >= 0.5:
        return '1'
    else: return '0'

def least_common(l: list) -> str:
    l = [int(n) for n in l]
    if sum(l) // len(l) <= 0.5:
        return '0'
    else: return '1'

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(f"Result: {process_input(inputFile)}")