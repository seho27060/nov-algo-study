# 221121
# 구현구현
import copy

# 슥 훑고, 2*2 찾아서 담기
# 지우고 -> 지워진거 카운트
# 빈곳 아래로 채우기

m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
def solution(m, n, board):
    answer = 0
    board = [list(line) for line in board]
    # print(len(board),len(board[0]))
    def checkBoard(nowBoard):
        result = set()

        for row in range(len(nowBoard)-1):
            for col in range(len(nowBoard[0])-1):
                if nowBoard[row][col] != "0":
                    if nowBoard[row][col] == nowBoard[row][col+1] == nowBoard[row+1][col] == nowBoard[row+1][col+1]:
                        result.add((row,col))
                        result.add((row,col+1))
                        result.add((row+1,col))
                        result.add((row+1,col+1))
        return list(result)

    while 1:
        removeFriends = checkBoard(board)
        # for b in board:
        #     print(b)
        # print(len(removeFriends))
        if len(removeFriends) <= 0:
            break
        # remove
        for rR, rC in removeFriends:
            board[rR][rC] = "0"
            answer += 1

        nxtBoard =[["0"]*n for _ in range(m)]

        for col in range(n):
            line = ""
            for row in range(m):
                if board[row][col] != "0":
                    line += board[row][col]
            line = "0"*(m-len(line))+line

            for row in range(m):
                if line[row] != "0":
                    nxtBoard[row][col] = line[row]
        board = copy.deepcopy(nxtBoard)
    return answer

print(solution(m,n,board))