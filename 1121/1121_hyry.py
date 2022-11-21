def organize(R, C, lst):
    _lst = []
    
    for col in range(C):
        tmp = []
        for row in range(R):
            if lst[row][col]: tmp.append(lst[row][col])
        _lst.append(([None] * (R - len(tmp)) + tmp))
    
    return list(list(i) for i in zip(*_lst))


def solution(m, n, board):
    board = [list(b) for b in board]
    cnt = 0
    while True:
        toRemove = set()
        for row in range(m - 1):
            for col in range(n - 1):
                if not board[row][col]: continue
                friend = board[row][col]
                for dr, dc in ((1, 0), (0, 1), (1, 1)):
                    newR, newC = row + dr, col + dc
                    if board[newR][newC] != friend:
                        break
                else:
                    toRemove.add((row, col))
                    toRemove.add((row + 1, col))
                    toRemove.add((row, col + 1))
                    toRemove.add((row + 1, col + 1))
                        
        for r, c in toRemove:
            cnt += 1
            board[r][c] = None
        board = organize(m, n, board)
        if not len(toRemove): break
    
    return cnt
