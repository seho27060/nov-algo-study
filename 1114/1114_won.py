def solution(msg):
    ans = []
    dic = {}
    for i in range(0, 26):
        dic[chr(ord("A") + i)] = i + 1

    idx = 27
    s, e = 0, 1

    while e < len(msg) + 1:
        tmp = msg[s:e]
        if tmp in dic:
            e += 1
        else:
            ans.append(dic[tmp[:-1]])
            dic[tmp] = idx
            idx += 1
            s = e - 1
    ans.append(dic[tmp])
    return ans