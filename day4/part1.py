import os

def main():
    input_file = os.path.join(os.path.dirname(__file__), 'example_input.txt')
    with open(input_file, 'r') as f:
        boards = f.read().split("\n\n")

    for i in range(len(boards)):
        if i == 0:
            boards[i] = boards[i].split(',')
        else:
            boards[i] = [[num for num in row.split(' ') if num != ''] for row in boards[i].split('\n')]
    draw_order = boards.pop(0)

    # Test if input is processed correctly
    _draw_order = ''
    for num in draw_order:
        _draw_order += f"{num} "
    print(f"\nDraw Order: {_draw_order}\n")

    for board in boards:
        _board = ''
        for row in board:
            for num in row:
                _board += f"{num} "
            _board += '\n'
        print(_board)

if __name__ == "__main__":
    main()