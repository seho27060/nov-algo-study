def solution(msg):
    N = len(msg)
    
    '''
    KAKAO
    i = 0) 있다는 것에서 시작
        1. tmp = msg[i] = K => tmp in wordDic (true)
            if j + 1 < N:
                j += 1 / tmp += msg[j] : KA
            else:
                answer.append(wordDic[tmp])
        2. 없다
            tmp in wordDic (false)
            answer.append(wordDic[tmp[:-2]])
            wordDic[tmp] = nextIndex
            tmp = tmp[:-2]
            i = j
    '''
    wordDic = {chr(idx + 64): idx for idx in range(1, 26 + 1)}
    
    i = j = 0
    lastIdx = 26
    tmp = msg[i]
    answer = []
    
    while i < N and j < N:
        if tmp in wordDic:
            if j + 1 < N:
                j += 1
                tmp += msg[j]
            else:
                answer.append(wordDic[tmp])
                break
        else:
            answer.append(wordDic[tmp[:-1]])
            lastIdx += 1
            wordDic[tmp] = lastIdx
            tmp = tmp[-1]
            i = j
    return answer
