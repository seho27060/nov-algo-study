# python에서는 nonlocal을 써야 nested function에서 사용 가능

def solution(info, edges):
    V = len(info)
    parentToChild = [[] for _ in range(V)]
    
    for p, c in edges:
        parentToChild[p].append(c)
    
    maxSheepCnt = 0
        
    def dfs(curV, sheepCnt, wolfCnt, nextVSet):
        nonlocal maxSheepCnt
        if sheepCnt <= wolfCnt: return
        
        tmp = nextVSet.copy()
        tmp.remove(curV)
        for nextV in parentToChild[curV]:
            tmp.add(nextV)
        
        maxSheepCnt = max(maxSheepCnt, sheepCnt)
        
        for nextV in tmp:
            if info[nextV]:
                dfs(nextV, sheepCnt, wolfCnt + 1, tmp.copy())
            else:
                dfs(nextV, sheepCnt + 1, wolfCnt, tmp.copy())
    
    dfs(0, 1, 0, {0, *parentToChild[0]})
    
    return maxSheepCnt
