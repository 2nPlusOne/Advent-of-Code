import os
from statistics import median

bracket_dict = {'{': '}', '[': ']', '(': ')', '<': '>'}
points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

def main():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        lines = [Line(line) for line in f.read().splitlines()]
    f.close()

    total_syntax_error_score = sum([line.point_value for line in lines])
    median_completion_score = median([line.completion_score for line in lines if line.completion_score])

    print(f"Part 1: The total syntax error score is {total_syntax_error_score}.")
    print(f"Part 2: The median completion score is {median_completion_score}.")

class Line:
    
    def __init__(self, line):
        self.line = line
        self.point_value = 0
        self.completion_score = 0
        self.is_incomplete = True

        bracket_dict = {'{': '}', '[': ']', '(': ')', '<': '>'}
        illegal_points_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
        completion_points_dict = {')': 1, ']': 2, '}': 3, '>': 4}
        parse = []
        for bracket in self.line:
            if bracket in bracket_dict:
                parse.append(bracket)
            elif bracket != bracket_dict[parse.pop()]:
                self.point_value = illegal_points_dict[bracket]
                self.is_incomplete = False # Line is corrupt, not incomplete
                break
        if self.is_incomplete:
            while len(parse) > 0:
                self.completion_score *= 5
                self.completion_score += completion_points_dict[bracket_dict[parse.pop()]]


if __name__ == '__main__':
    main()