import os

# Plan: process input of line segments into a list of grid coordinates
# Create a 2D array of 0's
# For each coordinate, add 1 to that grid position

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        line_segments = f.readlines()
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for segment in line_segments:
        start_x, start_y, end_x, end_y = process_segment(segment)
        grid = mark_grid(grid, start_x, start_y, end_x, end_y)
    print(count_positions_over_threshold(grid, 2))

def process_segment(segment):
    start_end = segment.split('->')
    start_end = [start_end[0].strip(), start_end[1].strip()]
    start_end = [x.split(',') for x in start_end]
    start_x, start_y = int(start_end[0][0]), int(start_end[0][1])
    end_x, end_y = int(start_end[1][0]), int(start_end[1][1])
    return start_x, start_y, end_x, end_y

def mark_grid(grid, start_x, start_y, end_x, end_y):
    # Mark all grid points on line segment
    if (start_x > end_x):
        start_x, end_x = end_x, start_x
    if (start_y > end_y):
        start_y, end_y = end_y, start_y

    print(f"Marking grid from {start_x},{start_y} to {end_x},{end_y}")
    if (start_x == end_x):
        for y in range(start_y, end_y + 1):
            grid[start_x][y] += 1
    elif (start_y == end_y):
        for x in range(start_x, end_x + 1):
            grid[x][start_y] += 1
    return grid

def count_positions_over_threshold(grid, threshold):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] >= threshold:
                count += 1
    return count

if __name__ == '__main__':
    main()