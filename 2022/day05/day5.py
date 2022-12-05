import os
from typing import NamedTuple
import re
from itertools import zip_longest

class Instruction(NamedTuple):
    """Represents a single instruction (move x crates from stack a to stack b)."""
    quantity: int
    fromStack: int
    toStack: int
    
    def crate_mover_9000(self, stacks: list[list[str]]):
        _stacks = [stack.copy() for stack in stacks]
        for _ in range(self.quantity):
            _stacks[self.toStack-1].append(_stacks[self.fromStack-1].pop())
        return _stacks
    
    def crate_mover_9001(self, stacks: list[list[str]]):
        _stacks = [stack.copy() for stack in stacks]
        stack = _stacks[self.fromStack-1]
        grabbed = stack[len(stack) - self.quantity:]
        _stacks[self.fromStack-1] = stack[:len(stack) - self.quantity]
        _stacks[self.toStack-1].extend(grabbed)
        return _stacks
    
def process_instruction(line):
    line = line.strip()
    line = re.sub(r"move |from |to ", "", line).split()
    return Instruction(int(line[0]), int(line[1]), int(line[2]))

def process_input(filename: str) -> int:
    instructions = []
    stacks_drawing = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if "move" not in line: # make sure it's not a line of instructions
                if '1' in line: continue # skip if it's the stack numbering
                line = line.replace("\n", "")
                stacks_drawing.append(list(line))
            
            else: # otherwise it's an instruction
                instructions.append(process_instruction(line))
                
    
    transposed_drawing = [list(filter(None,i)) for i in zip_longest(*stacks_drawing)]
    stacks = []
    for row in transposed_drawing:
        row = ''.join(row).strip(' []')
        if row == '': continue
        stacks.append(list(row)[::-1])
    
    return stacks, instructions


def part1(stacks: list[list[str]], instructions: list[Instruction]):
    for instruction in instructions:
        stacks = instruction.crate_mover_9000(stacks)
    
    return ''.join([stack.pop() for stack in stacks])

def part2(stacks: list[list[str]], instructions: list[Instruction]):
    for instruction in instructions:
        stacks = instruction.crate_mover_9001(stacks)
    
    return ''.join([stack.pop() for stack in stacks])

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    stacks, instructions = process_input(filename)
    print(f"Part 1: {part1(stacks, instructions)}")
    print(f"Part 2: {part2(stacks, instructions)}")
