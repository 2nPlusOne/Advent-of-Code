import os
from typing import List

def process_input(inputFile: str):
    trees = []
    with open(inputFile, 'r') as f:
        for line in f.readlines():
            trees.append([int(num) for num in list(line.strip())])
    return trees

def check_tree_visibility(row: int, col: int, trees: List[List[int]]) -> bool:
    tree_height = trees[row][col]
    
    # check north visibility
    north_heights = []
    for _row in range(row-1, -1, -1):
        north_heights.append(trees[_row][col])
    if all([height < tree_height for height in north_heights]):
        return True
    
    # check south visibility
    south_heights = []
    for _row in range(row+1, len(trees)):
        south_heights.append(trees[_row][col])
    if all([height < tree_height for height in south_heights]):
        return True
    
    # check east visibility
    east_heights = []
    for _col in range(col+1, len(trees[0])):
        east_heights.append(trees[row][_col])
    if all([height < tree_height for height in east_heights]):
        return True
    
    # check west visibility
    west_heights = []
    for _col in range(col-1, -1, -1):
        west_heights.append(trees[row][_col])
    if all([height < tree_height for height in west_heights]):
        return True
    
    return False
        
def part1(trees: List[List[int]]) -> int:
    """Count the number of trees visible from outside the grid.
    A tree is visible if all of the other trees between it and an edge of 
    the grid are shorter than it. Only consider trees in the same row or 
    column; that is, only look up, down, left, or right from any given tree."""
    
    length = len(trees)
    width = len(trees[0])
    
    # initialize count to the perimeter of the grid
    count = (2 * length + 2 * width) - 4
    
    # iterate over each tree in the interior of the grid
    for row in range(1, length-1):
        for col in range(1, width-1):
            # increment count if tree in cell is visible from any cardinal direction
            count += check_tree_visibility(row, col, trees)
            
    return count

def get_scenic_score(row: int, col: int, trees: List[List[int]]):
    tree_height = trees[row][col]
    
    # get north viewing distance
    north_dist = 0
    for _row in range(row-1, -1, -1):
        if trees[_row][col] < tree_height:
            north_dist += 1
        else:
            north_dist += 1
            break
    
    # Get south viewing distance
    south_dist = 0
    for _row in range(row+1, len(trees)):
        if trees[_row][col] < tree_height:
            south_dist += 1
        else:
            south_dist += 1
            break
    
    # get east viewing distance
    east_dist = 0
    for _col in range(col+1, len(trees[0])):
        if trees[row][_col] < tree_height:
            east_dist += 1
        else:
            east_dist += 1
            break
    
    # Get west viewing distance
    west_dist = 0
    for _col in range(col-1, -1, -1):
        if trees[row][_col] < tree_height:
            west_dist += 1
        else:
            west_dist += 1
            break
    
    return north_dist * south_dist * east_dist * west_dist

def part2(trees: List[List[int]]) -> int:
    """Calculates the highest scenic score among all trees in the grid.
    
    A tree's scenic score is found by multiplying together its viewing 
    distance in each of the four directions. 
    
    To measure the viewing distance from a given tree, look up, down, left, 
    and right from that tree; stop if you reach an edge or at the first 
    tree that is the same height or taller than the tree under 
    consideration. (If a tree is right on the edge, at least one of its 
    viewing distances will be zero.)"""  
    
    length = len(trees)
    width = len(trees[0])
    
    # initialize the highest scenic score to zero
    highest_score = 0
    
    # iterate over each tree in the interior of the grid
    for row in range(1, length-1):
        for col in range(1, width-1):
            score = get_scenic_score(row, col, trees)
            # Update highest score if necessary
            if score > highest_score:
                highest_score = score
            
    return highest_score

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    trees = process_input(filename)
    print(f"Part 1: {part1(trees)}")
    print(f"Part 2: {part2(trees)}")