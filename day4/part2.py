import os

# This doesn't work quite yet...
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
    winning_scores = bingo(boards, draw_order) 

    last_score = winning_scores.pop()
    print(f"Score of last board: {last_score}\n")

def bingo(boards, draw_order):
    """Plays bingo with a list of boards and a list of draws."""
    winning_scores = []
    for draw in draw_order:
        for board in boards:
            mark_board(board, draw)
            if has_bingo(board):
                winning_scores.append(calculate_score(board, draw))
                print(f"Bingo! {board} wins with a score of {calculate_score(board, draw)}.\n")
                boards.pop(boards.index(board))
                if len(boards) <= 0:
                    print(f"All boards have bingo!\n")
                    return winning_scores
    return winning_scores

def mark_board(board: list[list[chr]], draw: str) -> list[list[chr]]:
    """Marks a board if it contains draw."""
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == draw:
                board[i][j] = 'X'
    return board

def has_bingo(board: list[list[chr]]) -> bool:
    """Returns True if board has bingo."""
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
    """Calculates the score of a board board (board sum * draw)."""
    score = 0
    for row in board:
        for num in row:
            if num == 'X': continue
            score += int(num) * int(draw)
    return score

if __name__ == "__main__":
    main()

    #     print(f"Draw: {draw}")
    #     for i, board in enumerate(boards):
    #         _board = ''
    #         for j, row in enumerate(board):
    #             for k, col in enumerate(row):
    #                 if col == draw:
    #                     boards[i][j][k] = 'X'
    #                 _board += boards[i][j][k] + ' '
    #             _board += '\n'
    #         print(_board)