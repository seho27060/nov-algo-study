def solution(files):
    answer = []
    res = []
    for file in files:
        head = 0
        number = 0
        tail = 0
        h, n, t = '', '', ''
        for f in file:
            if f.isdigit():
                if number == 0:
                    head = 1
                    n += f
                else:
                    t += f
            else:
                if head == 0:
                    h += f
                else:
                    number = 1
                    t += f

        res.append([h, n, t])
    res.sort(key=lambda x: (x[0].upper(), int(x[1])))

    for r in res:
        answer.append(''.join(r))
    return answer