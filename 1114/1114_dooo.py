def solution(msg):
    answer = []
    dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J':10,'K' : 11, 'L' : 12, 'M' :13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' :20, 'U' : 21, 'V' : 22, 'W':23, 'X' : 24, 'Y' : 25, 'Z' : 26}

    idx = 0
    val = ''
    lst = []
    cnt = 26
    pidx = 1
    while True:

        if msg == val:
            break
        if msg[idx:idx+pidx] in dic.keys():
            pidx += 1
            if idx + pidx-1 > len(msg):
                lst.append(dic[msg[idx:idx+pidx]])
                break
        else:
            cnt += 1
            dic[msg[idx:idx+pidx]] = cnt
            val += msg[idx:idx+pidx-1]
            lst.append(dic[msg[idx:idx+pidx-1]])
            idx += pidx-1
            pidx = 1

    return lst