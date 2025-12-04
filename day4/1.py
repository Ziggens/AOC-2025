example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def accessible(board, x, y):
    M = len(board)
    N = len(board[0])
    count = 0
    for i in range(x-1, x+2):
        if i < 0 or i >= M:
            continue
        for j in range(y-1, y+2):
            if j < 0 or j >= N:
                continue
            if i == x and j == y:
                continue
            if board[i][j] == '@':
                count += 1

    return count < 4



with open("input.txt", 'r') as f:
    input = f.read().strip()
    # input = example
    board = input.split('\n')
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '@' and accessible(board, i, j):
                total += 1

    print(total)
