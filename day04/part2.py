import os

def main():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file, 'r') as f:
        boards = f.read().split("\n\n")
    f.close()

    draws = boards.pop(0).split(',')
    for i in range(len(boards)):
        boards[i] = [boards[i].split() for boards[i] in boards[i].split('\n')]

    scores = bingo(boards, draws)
    print(f"Scores in winning order: {scores}")

def bingo(boards, draws):
    scores = []
    for draw in draws:
        for board in boards:
            mark_board(board, draw)
            if (has_bingo(board)):
                scores.append(calculate_score(board, draw))
                boards.remove(board)
                print(f"{board} has bingo with {draw}! Score: {calculate_score(board, draw)}\n")
            if len(boards) < 1:
                return scores

def mark_board(board, draw):
    for i in range(len(board)):
        board[i] = ['X' if num == draw else num for num in board[i]]

def has_bingo(board):
    for row in board: 
        if all(num == 'X' for num in row):
            return True
    for col in zip(*board): 
        if all(num == 'X' for num in col):
            return True
    return False

def calculate_score(board, draw):
    return int(draw) * sum(sum(int(num) for num in row if num != 'X') for row in board)

main()