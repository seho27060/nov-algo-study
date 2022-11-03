#221102 양궁대회
# 백트래킹
# 쏘고 지나가는거/ 안쏘고 지나가는거/ 쏘고 안 지나가는거
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
# n = 9
# info = 	[0,0,1,2,0,1,1,1,1,1,1]
# n = 10
# info = 	[0,0,0,0,0,0,0,0,3,4,3]
def solution(n, info):
    global score, result, answer
    answer = []
    result = [0]*11
    checkedAnswer = set()
    score = 0

    def backtrack(now, cnt):
        global score, result, answer
        if cnt == 0 and tuple(result) not in checkedAnswer:
            compareScore = whoIsWinner(info, result)
            if answer:
                if compareScore > score:
                    score = compareScore
                    answer = result.copy()
                    checkedAnswer.add(tuple(answer))
                elif compareScore == score:
                    for idx in range(10,-1,-1):
                        if answer[idx] == result[idx]:
                            continue
                        elif answer[idx] > result[idx]:
                            break
                        elif answer[idx] < result[idx]:
                            answer = result.copy()
                            checkedAnswer.add(tuple(answer))
                            break
            else:
                answer = result.copy()
                checkedAnswer.add(tuple(answer))
            return
        else:
            if now < 10:
                backtrack(now+1,cnt)
                result[now] += 1
                backtrack(now+1,cnt-1)
                backtrack(now,cnt-1)
                result[now] -= 1
            elif now == 10:
                result[now] += cnt
                backtrack(now,0)
                result[now] -= cnt
        return
    def whoIsWinner(apeach, rian):
        apeachScore, rianScore = 0, 0
        # print("Apeach",apeach," Rian",rian)
        for idx in range(11):
            if apeach[idx] >= rian[idx] and apeach[idx] > 0:
                apeachScore += 10 - idx
            else:
                if rian[idx] > 0:
                    rianScore += 10 - idx
        return rianScore - apeachScore

    backtrack(0,n)
    if score == 0:
        answer = [-1]
    return answer

print(solution(n,info))