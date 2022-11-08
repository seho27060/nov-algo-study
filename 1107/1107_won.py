def convert(num, base):
    tmp = "0123456789ABCDEF"
    res = ""
    mok, na = divmod(num, base)
    res = tmp[na] + res
    while mok > 0:
        mok, na = divmod(mok, base)
        res = tmp[na] + res
    return res

def solution(n, t, m, p):
    answer = ''
    tmp = ""

    for i in range(m * t):
        tmp += str(convert(i, n))

    while len(answer) < t:
        answer += tmp[p - 1]
        p += m
    return answer