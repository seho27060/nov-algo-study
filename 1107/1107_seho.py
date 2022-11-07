# 221107 [3차] n진수 게임
# n의 진수로 m명이 참가하는 게임에서 p번째 순서일때 내 차례 일때의 t개의 숫자를 붙여서출력

# n*t? 로 만들어놓고 세어보자

n,t,m,p = 2,4,2,1
n,t,m,p = 16,16,2,1
n,t,m,p = 16,16,2,2

def solution(n, t, m, p):
    answer = ''
    def makeNthNum(num, div):
        getNum = num
        result = ""
        upperCount = {"10":"A", "11":"B" , "12":"C", "13":"D", "14":"E", "15":"F"}
        while num >= div:
            num, rest = divmod(num,div)
            if rest >= 10:
                rest = upperCount[str(rest)]
            result += str(rest)
        if int(num) >= 10:
            num = upperCount[str(num)]
        result += str(num)
        if result[-1] == "0" and len(result) > 1 and getNum != int(num):
            result = result[1:]
        return result
    # print(makeNthNum(16,16))
    numString = ""
    for now in range(m*t):
        numString =makeNthNum(now,n)+numString
    # print(numString)
    stand = p
    if p == m:
        stand = 0
    for idx in range(len(numString)-1,-1,-1):

        if (len(numString)-idx)%m in [stand]:
            answer += numString[idx]
        if len(answer) == t:
            break
    return answer

print(solution(n, t, m, p))