def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        stand = (i//n) + 1
        indata = i%n + 1
        if stand < indata:
            answer.append(indata)
        else:
            answer.append(stand)
    return answer