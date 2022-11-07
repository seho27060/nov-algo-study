# 원리는 알았으니 복습용 풀기
# 원리 아는게 더 어려웠다
# 이게 카카오...?

def solution(board, skill):
    answer = 0
    arr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for s in skill:
        t, r1, c1, r2, c2, v = s
        v = v if t == 2 else v * (-1)
        arr[r1][c1] += v
        arr[r2+1][c2+1] += v
        arr[r1][c2+1] += v *(-1)
        arr[r2+1][c1] += v * (-1)

    for i in range(len(board)+1):
        for j in range(1, len(board[0])+1):
            arr[i][j] += arr[i][j-1]

    for i in range(1, len(board)+1):
        for j in range(len(board[0]) + 1):
            arr[i][j] += arr[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])