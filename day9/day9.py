import os, math

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        heightmap = f.read().splitlines()

    low_points = get_low_points(heightmap)
    basins = get_basins(low_points, heightmap)
    three_largest = sorted(basins, key=len, reverse=True)[:3]
    part2 = math.prod([len(basin) for basin in three_largest])
    print(f"Part 2: The product of the sizes of the three largest basins is {part2}.")

def get_low_points(heightmap):
    """Return the points whose heights are lower than the adjacent points."""
    risk_sum = 0
    low_points = []
    for i, line in enumerate(heightmap):
        for j, height in enumerate(line):
            if height < min(adjacent_heights(heightmap, i, j)):
                risk_sum += 1 + int(height)
                low_points.append([i, j])
    print(f"Part 1: The sum of the risk levels of all low points on the heightmap is {risk_sum}.")
    return low_points

def get_basins(low_points, heightmap):
    """Return a list of the basin for each low point. A basin is all points with heights 
       less than 9 that flow downward to the low point"""
    basins = []
    for i, j in low_points:
        basin = []
        get_basin_recursive(heightmap, i, j, basin)
        basins.append(basin)
    return basins

def get_basin_recursive(heightmap, i, j, basin):
    """Recursively find each point in the basin."""
    basin.append([i, j])
    points = adjacent_points(heightmap, i, j)
    for k, l in points:
        if [k, l] in basin: continue
        if 9 > int(heightmap[k][l]) > int(heightmap[i][j]):
            get_basin_recursive(heightmap, k, l, basin)
                    
def adjacent_heights(heightmap, i, j):
    """Return the heights of the adjacent points."""
    if i == 0:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i+1][j]]
        elif j == len(heightmap[i]) - 1:
            return [heightmap[i][j-1], heightmap[i+1][j]]
        else:
            return [heightmap[i][j-1], heightmap[i][j+1], heightmap[i+1][j]]
    elif i == len(heightmap) - 1:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i-1][j]]
        elif j == len(heightmap[i]) - 1:
            return [heightmap[i][j-1], heightmap[i-1][j]]
        else:
            return [heightmap[i][j-1], heightmap[i][j+1], heightmap[i-1][j]]
    else:
        if j == 0:
            return [heightmap[i][j+1], heightmap[i-1][j], heightmap[i+1][j]]
        elif j == len(heightmap[i]) - 1:
            return [heightmap[i][j-1], heightmap[i-1][j], heightmap[i+1][j]]
        else:
            return [heightmap[i][j-1], heightmap[i][j+1], heightmap[i-1][j], heightmap[i+1][j]]

def adjacent_points(heightmap, i, j):
    """Return the points adjacent to the point at (i, j)."""
    if i == 0:
        if j == 0:
            return [[i, j+1], [i+1, j]]
        elif j == len(heightmap[i]) - 1:
            return [[i, j-1], [i+1, j]]
        else:
            return [[i, j-1], [i, j+1], [i+1, j]]
    elif i == len(heightmap) - 1:
        if j == 0:
            return [[i, j+1], [i-1, j]]
        elif j == len(heightmap[i]) - 1:
            return [[i, j-1], [i-1, j]]
        else:
            return [[i, j-1], [i, j+1], [i-1, j]]
    else:
        if j == 0:
            return [[i, j+1], [i-1, j], [i+1, j]]
        elif j == len(heightmap[i]) - 1:
            return [[i, j-1], [i-1, j], [i+1, j]]
        else:
            return [[i, j-1], [i, j+1], [i-1, j], [i+1, j]]

if __name__ == '__main__':
    main()