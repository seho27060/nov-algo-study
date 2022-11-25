def solution(m, n, board):
    answer = 0

    new_board = []
    for i in range(m):
        lst = []
        for j in range(n):
            lst.append(board[i][j])
        new_board.append(lst)
    while True:
        arr = [[1] * n for _ in range(m)]
        nflag = 0
        for i in range(m - 1):
            for j in range(n - 1):
                flag = 0
                if new_board[i][j] == 0:
                    continue
                for r, c in ((1, 0), (0, 1), (1, 1)):
                    if new_board[i][j] != new_board[i + r][j + c]:
                        flag = 1
                        break
                if flag == 0:
                    nflag = 1
                    for r, c in ((0, 0), (1, 0), (0, 1), (1, 1)):
                        arr[i + r][j + c] = 0
        if nflag == 0:
            break
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    new_board[i][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if new_board[i][j] == 0:
                    idx = i - 1
                    while idx >= 0:
                        if new_board[idx][j] != 0:
                            new_board[i][j] = new_board[idx][j]
                            new_board[idx][j] = 0
                            break
                        idx -= 1
    for i in range(m):
        for j in range(n):
            if new_board[i][j] == 0:
                answer += 1

    return answer