def solution(n, k, cmd):
    left = [i for i in range(-1, n - 1)]
    right = [i for i in range(1, n + 1)]
    removed = [False for _ in range(n)]
    trashCan = []
    
    left[0] = right[-1] = None
    curIdx = k
    
    for c in cmd:
        if c[0] == 'U':
            X = int(c[2:])
            for _ in range(X):
                curIdx = left[curIdx]
        elif c[0] == 'D':
            X = int(c[2:])
            for _ in range(X):
                curIdx = right[curIdx]
            
        elif c[0] == 'C':
            removed[curIdx] = True
            trashCan.append(curIdx)
            l, r = left[curIdx], right[curIdx]
            if l or l == 0: right[l] = r
            if r: left[r] = l
            curIdx = r if r else l
            
            
        elif c[0] == 'Z':
            tmp = trashCan.pop()
            removed[tmp] = False
            l = left[tmp]
            r = right[tmp]
            if l or l == 0: right[l] = tmp
            if r: left[r] = tmp
    
    ans = ''
    for i in range(n):
        if removed[i]:
            ans += 'X'
        else:
            ans += 'O'
    return ans
