import copy

def solution(n, info):
    global maxV, answer
    answer = []
    maxV = 0

    def dfs(res, j, n):
        global maxV, answer
        if len(res) == 11:
            if n != 0:
                res[-1] = n
            v1 = 0
            v2 = 0
            for i in range(11):
                if res[i] > info[i]:
                    v1 += 10 - i
                elif info[i] >= res[i]:
                    if info[i] != 0 or res[i] != 0:
                        v2 += 10 - i
            if v1 > v2 and v1-v2 > maxV:
                answer = copy.deepcopy(res)
                maxV = v1-v2
            elif v1 > v2 and v1-v2 == maxV:
                if answer:
                    for k in range(10, -1, -1):
                        if res[k] > answer[k]:
                            answer = copy.deepcopy(res)
                            break
                        elif res[k] == answer[k]:
                            continue
                        else:
                            break
                else:
                    answer = copy.deepcopy(res)
            return
        if info[j] < n:
            res.append(info[j] + 1)
            dfs(res, j + 1, n - info[j] - 1)
            res.pop()
        res.append(0)
        dfs(res, j + 1, n)
        res.pop()

    dfs([], 0, n)
    if answer == []:
        answer.append(-1)
    return answer