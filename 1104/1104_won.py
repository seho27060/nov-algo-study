def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            tmp[r1][c1] -= degree
            tmp[r1][c2 + 1] += degree
            tmp[r2 + 1][c1] += degree
            tmp[r2 + 1][c2 + 1] -= degree
        else:
            tmp[r1][c1] += degree
            tmp[r1][c2 + 1] -= degree
            tmp[r2 + 1][c1] -= degree
            tmp[r2 + 1][c2 + 1] += degree
    for i in range(len(tmp) - 1):
        for k in range(len(tmp[0]) - 1):
            tmp[i][k + 1] += tmp[i][k]
    for k in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][k] += tmp[i][k]
    for i in range(len(board)):
        for k in range(len(board[i])):
            board[i][k] += tmp[i][k]
            if board[i][k] > 0:
                answer += 1
    return answer