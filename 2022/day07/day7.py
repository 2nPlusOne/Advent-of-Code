from __future__ import annotations
import os
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    """ A class for representing a directory in a file system."""
    name: str
    parent: Optional[Directory] = None
    children: List[Directory] = field(default_factory=list)
    files: List[File] = field(default_factory=list)
    
    def get_parent(self) -> Optional[Directory]: return self.parent
    
    def get_children(self) -> List[Directory]: return self.children
    
    def get_child(self, name: str) -> Optional[Directory]:
        return next(filter(lambda child: child.name == name, self.children), None)
    
    def add_child(self, name: str):
        child_dir = Directory(name)
        child_dir.parent = self
        self.children.append(child_dir)
    
    def add_file(self, name: str, size: int):
        self.files.append(File(name, size))
        
    def get_size(self) -> int:
        """Returns the size of the directory."""
        # Add the sizes of all the files in the directory
        size = sum(f.size for f in self.files)
    
        # Recursively add the sizes of all the child directories
        size += sum(child.get_size() for child in self.children)    
        
        return size
    
    def pre_traverse(self):
        """Performs a pre-order traversal. Self -> files -> children directories."""
        print("Directory: " + self.name)
        for file in sorted(self.files, key=lambda f: f.name):
            print('File: ' + file.name)
        for child in sorted(self.children, key=lambda c: c.name):
            child.pre_traverse()

def process_input(inputFile: str):
    with open(inputFile, 'r') as f:
        f.readline(); f.readline # skip first two lines
        
        # initialize root directory node
        root = Directory('/')
        
        currDir = root
        for line in f.readlines():
            line = line.strip().split()
            
            if line[0] == 'dir':
                currDir.add_child(line[1])
        
            elif line[0].isnumeric():
                currDir.add_file(line[1], int(line[0]))
                
            elif line[0] == '$':
                if line[1] == 'ls': continue # skip ls lines
                # go up a directory if we encounter '$ cd ..'
                if line[2] == '..':
                    currDir = currDir.get_parent()
                # otherwise, mount to the next child of the current directory specified in the line
                else:
                    currDir = currDir.get_child(line[2])
        return root

def part1(dir: Directory, maxDirSize: int) -> int:
    """Part 1: Sum the directories in the filesystem whose size is 
    less than or equal to 100000."""
    total = 0
    
    # Recursively visit all child directories
    for child in dir.get_children():
        total += part1(child, maxDirSize)
    
    # If the current directory's size is less than or equal 
    # to the max, add it to the total
    size = dir.get_size()
    if size <= maxDirSize:
        total += size
        
    return total

def part2(root: Directory) -> int:
    """Finds the size of the smallest directory which, if deleted, would
    make enough space for the update (30,000,000 bytes) to be installed."""  
    total_space = 70000000
    required_by_update = 30000000
    # Calculate free space by subtracting total used from total space
    free_space = total_space - root.get_size()
    # Calculate space need by subtracting free space from the amount required by update
    remainder_needed = required_by_update - free_space
    
    # Iterate over every directory to find the answer
    smallest = root.get_size()
    stack = root.get_children()
    while stack != []:
        dir = stack.pop()
        dir_size = dir.get_size()
        
        # check current size
        if remainder_needed <= dir_size < smallest:
            smallest = dir_size
            
        # add all children to stack
        for child in dir.get_children(): 
            stack.append(child)
            
    return smallest

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    root = process_input(filename)
    print(f"Part 1: {part1(root, 100000)}")
    print(f"Part 2: {part2(root)}")