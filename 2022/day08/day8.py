import os
from typing import List

def process_input(inputFile: str):
    trees = []
    with open(inputFile, 'r') as f:
        for line in f.readlines():
            trees.append(line.strip())
    return trees

def check_tree(row: int, col: int, trees: List[str]) -> bool:
    tree_height = int(trees[row][col])
    
    # check north visibility
    north_heights = []
    for _row in range(row-1, -1, -1):
        north_heights.append(int(trees[_row][col]))
    if all([height < tree_height for height in north_heights]):
        return True
    
    # check south visibility
    south_heights = []
    for _row in range(row+1, len(trees)):
        south_heights.append(int(trees[_row][col]))
    if all([height < tree_height for height in south_heights]):
        return True
    
    # check east visibility
    east_heights = []
    for _col in range(col+1, len(trees[0])):
        east_heights.append(int(trees[row][_col]))
    if all([height < tree_height for height in east_heights]):
        return True
    
    # check west visibility
    west_heights = []
    for _col in range(col-1, -1, -1):
        west_heights.append(int(trees[row][_col]))
    if all([height < tree_height for height in west_heights]):
        return True
    
    return False
        
def part1(trees: List[str]) -> int:
    """Count the number of trees visible from outside the grid.
    A tree is visible if all of the other trees between it and an edge of 
    the grid are shorter than it. Only consider trees in the same row or 
    column; that is, only look up, down, left, or right from any given tree."""
    
    length = len(trees)
    width = len(trees[0])
    
    # initialize count to the perimeter of grid
    count = (2 * length + 2 * width) - 4
    
    # iterate over each tree in the interior of the grid
    
    for row in range(1, length-1):
        for col in range(1, width-1):
            # increment count if tree in cell is visible from any cardinal direction
            count += check_tree(row, col, trees)
            
    return count

def part2():
    """>.<"""  
    pass

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    trees = process_input(filename)
    print(f"Part 1: {part1(trees)}")
    print(f"Part 2: {part2()}")