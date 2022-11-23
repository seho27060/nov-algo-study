def check(uid, ban):
    N, M = len(uid), len(ban)
    if N != M:
        return False
    for i in range(N):
        if ban[i] != '*' and uid[i] != ban[i]:
            return False
    return True


def solution(user_id, banned_id):
    '''
    user_id [1, 8]
    제재 아이디 별로 제재 아이디로 가능한 것을 일단 구해 set에 넣어 둔다
    
    이후 제재 아이디 순으로 그래프처럼 가능한 조합 구하기
    '''
    N, M = len(user_id), len(banned_id)
    banLst = [[] for _ in range(M)]
    
    for bIdx in range(M):
        for uIdx in range(N):
            if check(user_id[uIdx], banned_id[bIdx]):
                banLst[bIdx].append(uIdx)
    
    possible = []
    used = [False] * N
    
    def comb(depth, curLst):
        nonlocal possible, used
        if depth == M:
            possible.append(set(curLst))
            return
        
        for i in banLst[depth]:
            if not used[i]:
                used[i] = True
                comb(depth + 1, curLst + [user_id[i]])
                used[i] = False
    
    comb(0, [])
    
    tmp = []
    ans = 0
    for p in possible:
        if p not in tmp:
            ans += 1
            tmp.append(p)
            
    return ans
