from os import path
import numpy as np

def main():
    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        energy_grid = np.array([[int(energy) for energy in line] for line in f.read().splitlines()])
    f.close()
    
    num_flashes = simulate_steps(energy_grid, 100)
    sync_step = get_sync_step(energy_grid)
    print(f'Part 1: The total number of flashes after 100 steps is {num_flashes}.')
    print(f"Part 2: The step on which all the octopuses flash simultaneously is {sync_step}.")

def simulate_steps(grid: np.ndarray, steps: int) -> int:
    """Simulate for the given number of steps, and return the total number of flashes."""
    _grid = grid.copy()
    return sum([step(_grid) for _ in range(steps)])

def get_sync_step(grid: np.ndarray) -> int:
    """Return the step on which all the cells flash simultaneously."""
    _grid = grid.copy()
    steps = 0
    flashes = 0

    cell_count = len(_grid) * len(_grid[0])
    while flashes < cell_count:
        steps += 1
        flashes = step(_grid)
    return steps

def step(grid: np.ndarray) -> int:
    """Perform a single step of the simulation."""
    flashes = 0
    grid += 1 # Phase 1: Add 1 energy to all cells
    flashing = get_flashing(grid) # Note all flashing cells
    while flashing:
        flashes += len(flashing) # Increment the number of flashed cells this turn
        for i, j in flashing: # Phase 2: Increment all cells adjacent to flashing cells
            for k, l in get_adjacent(grid, i, j):
                if grid[k][l] > 0: # Only increment if the cell hasn't flashed this step
                    grid[k][l] += 1
        flashing = get_flashing(grid) # Note all flashing cells
    return flashes

def get_flashing(grid: np.ndarray) -> list:
    """Return a list of index positions of all flashing cells."""
    flashing = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9:
                grid[i][j] = 0
                flashing.append((i, j))
    return flashing

def get_adjacent(grid: np.ndarray, i: int, j: int) -> list:
    """Return a list of index positions of all adjacent cells, including diagonals."""
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return [(i+delta[0], j+delta[1]) for delta in deltas if 0 <= i+delta[0] < len(grid) and 0 <= j+delta[1] < len(grid[i])]

def get_adjacent_naive(grid: np.ndarray, i: int, j: int) -> list:
    """Return a list of index positions of all adjacent cells, including diagonals."""
    if i == 0:
        if j == 0:
            return [(i, j+1), (i+1, j), (i+1, j+1)]
        elif j == len(grid[i])-1:
            return [(i, j-1), (i+1, j-1), (i+1, j)]
        else:
            return [(i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    elif i == len(grid)-1:
        if j == 0:
            return [(i-1, j), (i-1, j+1), (i, j+1)]
        elif j == len(grid[i])-1:
            return [(i-1, j-1), (i-1, j), (i, j-1)]
        else:
            return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1)]
    else:
        if j == 0:
            return [(i-1, j), (i, j+1), (i+1, j), (i-1, j+1), (i+1, j+1)]
        elif j == len(grid[i])-1:
            return [(i-1, j), (i, j-1), (i+1, j), (i-1, j-1), (i+1, j-1)]
        else:
            return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]


if __name__ == '__main__':
    main()