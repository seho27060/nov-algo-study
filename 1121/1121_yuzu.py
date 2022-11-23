def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        visited = []
        for x in range(m - 1):
            for y in range(n - 1):
                cnt = 0
                visit = [(x, y)]
                for dx, dy in (1, 0), (0, 1), (1, 1):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[x][y] == board[nx][ny] and board[x][y] != 0:
                            cnt += 1
                            visit.append((nx, ny))
                if cnt == 3:
                    visited += visit

        if len(set(visited)) == 0:
            break

        for sx, sy in set(visited):
            board[sx][sy] = 0
            answer += 1

        for a in range(m - 1, -1, -1):
            for b in range(n):
                if board[a][b] == 0:
                    for c in range(a - 1, -1, -1):
                        if board[c][b] != 0:
                            board[a][b], board[c][b] = board[c][b], board[a][b]
                            break

    return answer