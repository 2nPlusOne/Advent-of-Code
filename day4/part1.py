import os

def main():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file, 'r') as f:
        boards = f.read().split("\n\n")

    for i in range(len(boards)):
        if i == 0:
            boards[i] = boards[i].split(',')
        else:
            boards[i] = [[num for num in row.split(' ') if num != ''] for row in boards[i].split('\n')]
    draw_order = boards.pop(0)

    # Test if input is processed correctly
    for draw in draw_order:
        print(f"\n\nDraw: {draw}")
        for i, board in enumerate(boards):
            _board = ''
            for j, row in enumerate(board):
                for k, col in enumerate(row):
                    if col == draw:
                        boards[i][j][k] = 'X'
                    _board += boards[i][j][k] + ' '
                _board += '\n'
            print(_board)
            if look_for_bingo(board):
                print(f"Bingo! {draw} is in the {i+1}th board")
                print(f"Score: {calculate_score(boards[i], draw)}")
                return
            
def look_for_bingo(board: list[list[chr]]) -> bool:
    # Check rows
    for row in board:
        if all(num == 'X' for num in row):
            return True

    # Check columns
    for i in range(len(board[0])):
        if all(num == 'X' for num in [row[i] for row in board]):
            return True

    return False

def calculate_score(board: list[list[chr]], draw: str) -> int:
    score = 0
    for row in board:
        for num in row:
            if num != 'X':
                score += int(num)
    return score * int(draw)

if __name__ == "__main__":
    main()