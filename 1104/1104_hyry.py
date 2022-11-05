
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
def solution(board, skill):
    '''
    N * M 행렬 모양 게임 맵 [1, 1000]
    내구도가 0 이하가 되면 파괴 
    파괴되지 않은 건물 개수 return
    skill [1, 250_000]  # bruteforce하면 3중 for인데 스킬이 너무 많음
    type, r1, c1, r2, c2, degree
    1 = 적, 2 = 회복
    '''
    R, C = len(board), len(board[0])
    accBoard = [[0] * (C + 2) for _ in range(R + 2)]

    for type, r1, c1, r2, c2, degree in skill:
        weight = -1 if type == 1 else 1
        accBoard[r1 + 1][c1 + 1] += degree * weight
        accBoard[r1 + 1][c2 + 2] += degree * -weight
        accBoard[r2 + 2][c1 + 1] += degree * -weight
        accBoard[r2 + 2][c2 + 2] += degree * weight

    for row in range(1, R + 2):
        for col in range(1, C + 2):
            accBoard[row][col] +=  accBoard[row][col - 1]

    for col in range(1, C + 2):
        for row in range(1, R + 2):
            accBoard[row][col] +=  accBoard[row - 1][col]

    cnt = 0
    for row in range(R):
        for col in range(C):
            if board[row][col] + accBoard[row + 1][col + 1] > 0:
                cnt += 1

    return cnt

# BruteForce
#     R, C = len(board), len(board[0])

#     for type, r1, c1, r2, c2, degree in skill:
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 board[r][c] += degree * (-1 if type == 1 else 1)

#     cnt = 0
#     for row in range(R):
#         for col in range(C):
#             if board[row][col] > 0:
#                 cnt += 1

#     return cnt
