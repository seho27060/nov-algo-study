from collections import deque

def bfs(n, info):
    res = []
    qu = deque()
    qu.append([0, [0] * 11])
    maxDiff = 0
    while qu:
        cur, arrow = qu.popleft()

        if sum(arrow) == n:
            a, l = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        a += 10 - i
                    else:
                        l += 10 - i
            if a < l:
                diff = l - a
                if maxDiff > diff:
                    continue
                if maxDiff < diff:
                    maxDiff = diff
                    res.clear()
                res.append(arrow)
        elif sum(arrow) > n:
            continue
        elif cur == 10:
            arr = arrow[:]
            arr[cur] = n - sum(arr)
            qu.append([-1, arr])
        else:
            arr1 = arrow[:]
            arr1[cur] = info[cur] + 1
            qu.append([cur + 1, arr1])

            arr2 = arrow[:]
            arr2[cur] = 0
            qu.append([cur + 1, arr2])
    return res

def solution(n, info):
    arr = bfs(n, info)

    if not arr:
        return [-1]
    elif len(arr) == 1:
        return arr[0]
    return arr[-1]
