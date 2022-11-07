def solution(board, skill):
    answer = 0
    arr = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1
        arr[r1][c1] += degree
        arr[r2 + 1][c2 + 1] += degree
        arr[r1][c2 + 1] -= degree
        arr[r2 + 1][c1] -= degree

    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[i][j + 1] += arr[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[i + 1][j] += arr[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer