import os

# Plan: process each line of input into a list of points on that line.
#       Create a 2D array of 0's.
#       For each point on line, add 1 to that grid position.

Line = tuple[int, int, int, int]

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        line_segments = f.readlines()
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for line in line_segments:
        line = process_segment(line)
        grid = mark_grid(grid, line)

    print(f"\nPoints with at least two overlaps: {overlaps_over_threshold(grid, 2)}\n")

def process_segment(segment):
    """Return a tuple with starting and ending coordinates of line segment."""
    segment = segment.split('->')
    segment = [segment[0].strip(), segment[1].strip()]
    segment = [x.split(',') for x in segment]
    x1, y1 = int(segment[0][0]), int(segment[0][1])
    x2, y2 = int(segment[1][0]), int(segment[1][1])
    return x1, y1, x2, y2

def delta_xy(line: Line):
    """Return dx and dy as direction of line on x and y axis."""
    x1, y1, x2, y2 = line
    dx = 1 if (x2 - x1) > 0 else -1
    dy = 1 if (y2 - y1) > 0 else -1
    if x1 == x2: 
        return 0, dy
    elif y1 == y2: 
        return dx, 0
    else: return dx, dy

def mark_grid(grid, line: Line):
    """Increment grid values for each coordinate in line segment."""
    dx, dy = delta_xy(line)
    x1, y1, x2, y2 = line

    while (x1, y1) != (x2, y2):
        grid[x1][y1] += 1
        x1 += dx 
        y1 += dy
    grid[x1][y1] += 1
    return grid

def overlaps_over_threshold(grid, threshold):
    """Return the number of points with number of overlaps over threshold."""
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] >= threshold:
                count += 1
    return count

if __name__ == '__main__':
    main()