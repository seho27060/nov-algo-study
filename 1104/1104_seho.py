# 221104 파괴되지 않은 건물
# 멀고도 먼 알고리즘의 길
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
def solution(board, skill):
    answer = 0
    cumulative = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for active in skill:
        degree = active[5]
        if active[0] == 1:
            degree*=-1
        cumulative[active[1]][active[2]] += degree
        cumulative[active[3]+1][active[4]+1] += degree
        cumulative[active[1]][active[4]+1] += -degree
        cumulative[active[3]+1][active[2]] += -degree

    for col in range(len(board[0])+1):
        for row in range(1,len(board)+1):
            cumulative[row][col] += cumulative[row-1][col]
    for row in range(len(board)+1):
        for col in range(1,len(board[0])+1):
            cumulative[row][col] += cumulative[row][col-1]

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] + cumulative[row][col] > 0:
                answer += 1
    return answer

print(solution(board,skill))