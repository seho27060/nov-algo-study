def changeToN(num, n):
    numToAlp = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    if num == 0: return '0'
    
    ans = ''
    while num > 0:
        ans = (str(num % n) if num % n < 10 else numToAlp[num % n]) + ans
        num //= n
    return ans


def solution(n, t, m, p):
    '''
    n [2, 16]
    t [0, 1000]
    m [2, 100]
    p [1, m] # 순서 = p + m * (횟수)
    '''
    totalCnt = p + (t - 1) * m
    
    num = -1  # 10진수 숫자
    strV = ''
    
    turn = 1
    tube = p
    answer = ''
    while turn <= totalCnt:
        if len(strV) < turn:
            num += 1
            strV += changeToN(num, n)
        
        if turn == tube:
            tube += m
            answer += strV[turn - 1]
        turn += 1
    
    return answer
