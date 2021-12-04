import os
import numpy as np

def process_input(inputFile: str) -> int:
    with open(inputFile, 'r') as f:
        data = [split_word(line.strip()) for line in f.readlines()]
    f.close()
    bit_list = np.transpose(data).tolist()

    gamma, epsilon = [], []
    for i in bit_list:
        gamma.append(most_common(i))
        epsilon.append(least_common(i))
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)

    return gamma * epsilon

def split_word(word: str) -> list:
    return [char for char in word]

def most_common(list: list) -> str: return max(set(list), key=list.count)
def least_common(list: list) -> str: return min(set(list), key=list.count)

if __name__ == "__main__":
    inputFile = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(process_input(inputFile))