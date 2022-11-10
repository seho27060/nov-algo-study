def solution(n, t, m, p):
    answer = ''

    def convert(i, n):
        num = "0123456789ABCDEF"
        x, y = divmod(i, n)
        if x == 0:
            return num[y]
        else:
            return convert(x, n) + num[y]

    s = ''
    for i in range(t * m):
        s += str(convert(i, n))

    for i in range(p - 1, t * m, m):
        answer += s[i]

    return answer