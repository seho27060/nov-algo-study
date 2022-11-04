# 221104
n = 5
info = 	[2,1,1,1,0,0,0,0,0,0,0]
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
def solution(n, info):
    global score, answer, result

    answer = [0]*11
    result = [0]*11
    score = 0

    def backtrack(now,chance):
        global score, answer, result
        # print(now, chance, answer,result,score)
        if chance == 0:
            compareScore = whoIsWinner(info,result)
            # if compareScore >= score:
            #     print("result",score, answer,compareScore, result)
            if compareScore > score:
                answer = result.copy()
                score = compareScore
            elif compareScore == score:
                for idx in range(10,-1,-1):
                    if result[idx] > answer[idx]:
                        answer = result.copy()
                    elif answer[idx] > result[idx]:
                        break
                    else:
                        continue
            return
        else:
            for arrow in range(chance+1):
                result[now] += arrow
                if now < 10:
                    backtrack(now + 1, chance - arrow)
                elif now == 10:
                    backtrack(now,0)
                result[now] -= arrow

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
    # print(answer)
    if score == 0:
        answer = [-1]
    return answer

print(solution(n,info))