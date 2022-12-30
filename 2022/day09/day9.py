from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List

@dataclass
class Position:
    x: int
    y: int
    
    def is_adjacent(self, other_pos: Position):
        return abs(other_pos.x - self.x) < 2 and abs(other_pos.y - self.y) < 2
    
    def as_tuple(self): return (self.x, self.y)

def process_input(inputFile: str) -> List[str]:
    moves = []
    with open(inputFile, 'r') as f:
        for line in f.readlines():
            line = line.strip().split()
            for _ in range (int(line[1])):
                moves.append(line[0])
    return moves

def part1(moves: list[str]) -> int:
    """Count the number of unique positions visited by the tail 
    after the sequence of movements (the input)."""
    head = Position(0,0)
    tail = Position(0,0)
    
    positions = set()
    positions.add(tail.as_tuple())
    
    for move in moves:
        # move the head
        if move == 'U':
            head.y += 1
        elif move == 'D':
            head.y -= 1
        elif move == 'L':
            head.x -= 1
        elif move == 'R':
            head.x += 1
            
        # only move tail if it's not adjacent to the head        
        if not tail.is_adjacent(head):
            # handle moving the tail towards the head
            if head.y - tail.y > 0:
                tail.y += 1
            elif head.y - tail.y < 0:
                tail.y -= 1
                
            if head.x - tail.x > 0:
                tail.x += 1
            elif head.x - tail.x < 0:
                tail.x -= 1
                
            positions.add(tail.as_tuple()) # tuples are hashable into the set
            
    return len(positions)

def part2(moves: list[str], n: int) -> int:
    """Count the number of unique positions visited by the tail 
    after the sequence of movements (the input). Part 2 extends
    the length of the rope to have n segments."""
    segments = [Position(0,0) for _ in range(n)]
    head = segments[0]
    tail = segments[-1]
    
    positions = set()
    positions.add(tail.as_tuple())
    
    for move in moves:
        # move the head
        if move == 'U':
            head.y += 1
        elif move == 'D':
            head.y -= 1
        elif move == 'L':
            head.x -= 1
        elif move == 'R':
            head.x += 1
        
        # iterate over all segments after the head
        for i in range(1, len(segments)):
            segment = segments[i]
            prev_segment = segments[i-1]
            
            # only move a segment if it's not adjacent to the previous segment        
            if not segment.is_adjacent(prev_segment):
                # handle moving the segment towards the previous one
                if prev_segment.y - segment.y > 0:
                    segment.y += 1
                elif prev_segment.y - segment.y < 0:
                    segment.y -= 1
                    
                if prev_segment.x - segment.x > 0:
                    segment.x += 1
                elif prev_segment.x - segment.x < 0:
                    segment.x -= 1
                
        positions.add(tail.as_tuple()) # tuples are hashable into the set
            
    return len(positions)

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    moves = process_input(filename)
    print(f"Part 1: {part1(moves)}")
    print(f"Part 2: {part2(moves, 10)}")