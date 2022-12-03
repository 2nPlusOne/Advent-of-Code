import os
import numpy as np

def main():
    with open(os.path.join(os.path.dirname(__file__), 'sample.txt'), 'r') as f:
        input = [part for part in f.read().partition("\n\n") if part != "\n\n"]
        f.close()

    dots = [[int(pos) for pos in coord.split(',')] for coord in input[0].split("\n")]
    folds = [line.strip().split('=') for line in input[1].split("\n")]
    folds = [[line[0][-1], int(line[1])] for line in folds]

    size_x, size_y = max(dots, key=lambda x: x[0])[0] + 1, max(dots, key=lambda x: x[1])[1] + 1
    grid = np.zeros((size_x, size_y), dtype=int)
    for dot in dots:
        grid[dot[0], dot[1]] = 1

    print(grid)
    grid = fold_x(grid, 6)
    print(f"\n{grid}")

    for fold in folds:
        if fold[0] == 'x':
            grid = fold_x(grid, fold[1])
        elif fold[0] == 'y':
            grid = fold_y(grid, fold[1])
        else:
            raise ValueError("Unknown fold type: {}".format(fold[0]))

def fold_x(grid, fold_x):
    left = grid[:, :fold_x]
    right = grid[:, fold_x + 1:]

    return left

def fold_y(grid, fold_y):
    grid = np.rot90(grid, fold_y)
    grid = np.fliplr(grid)
    grid = np.rot90(grid, fold_y)
    return grid




if __name__ == "__main__":
    main()