# 구글링 참고
from collections import deque

def bfs(n, info):
    res = []
    q = deque([(0, [0]*11)])
    maxV = 0

    while q:
        score, arrow = q.popleft()

        # 경기 끝날때
        # 1) 화살 = 10 2) 화살 10+ 3) 화살 10-
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:
                gap = lion - apeach
                if maxV > gap:
                    continue
                if maxV < gap:
                    maxV = gap
                    res.clear()
                res.append(arrow)

        elif sum(arrow) > n:
            continue

        elif score == 10:
            tmp = arrow.copy()
            tmp[score] = n - sum(tmp)
            q.append((-1, tmp))

        else:
            tmp = arrow.copy()
            tmp[score] = info[score] + 1
            q.append((score + 1, tmp))
            tmp2 = arrow.copy()
            tmp2[score] = 0
            q.append((score + 1, tmp2))
    return res

def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]