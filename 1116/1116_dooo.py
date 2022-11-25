def solution(m, musicinfos):
    answer = ''
    val = [m[0]]
    for i in range(1, len(m)):
        if m[i] == '#':
            s = val.pop()
            val.append(s.lower())
        else:
            val.append(m[i])
    m = ''.join(val)
    dic = dict()
    for i in musicinfos:
        lst = i.split(',')
        start = lst[0].split(':')
        end = lst[1].split(':')

        s_m = int(start[0]) * 60 + int(start[1])
        e_m = int(end[0]) * 60 + int(end[1])
        music = lst[3]
        val = [music[0]]
        c = ''
        for i in range(1, len(music)):
            if music[i] == '#':
                c = val.pop()
                val.append(c.lower())
            else:
                val.append(music[i])
        music = ''.join(val)
        ss = ''
        idx = 0
        for i in range(e_m - s_m):

            if idx == len(music):
                idx = 0
            ss += music[idx]
            idx += 1
        dic[lst[2]] = ss
    flag = 0
    max_val = -1
    for i in dic.keys():
        if m in dic[i]:
            if len(dic[i]) > max_val:
                max_val = len(dic[i])
                answer = i
                flag = 1
    if flag == 1:
        return answer
    else:
        return '(None)'

    return answer