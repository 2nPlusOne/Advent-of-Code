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
    for draw in draw_order:
        print(f"\n\nDraw: {draw}")
        for i, board in enumerate(boards):
            _board = ''
            for j, row in enumerate(board):
                for k, col in enumerate(row):
                    if col == draw:
                        boards[i][j][k] = "X "
                    _board += boards[i][j][k] + ' '
                _board += '\n'
            print(_board)

if __name__ == "__main__":
    main()