def solution(board, skill):
    answer = 0
    v = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        v[r1][c1] += d
        v[r1][c2+1] -= d
        v[r2+1][c1] -= d
        v[r2+1][c2+1] += d
    for i in range(len(v)-1):
        for j in range(len(v[0]) -1):
            v[i][j+1] += v[i][j]
    for j in range(len(v[0])-1):
        for i in range(len(v) -1):
            v[i+1][j] += v[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += v[i][j]
            if board[i][j] > 0:
                answer+= 1
    return answer