# 221114
# 맹~?
def solution(msg):
    answer = []
    alphabets = [chr(i) for i in range(65,65+26)]

    idx = 0

    while idx <= len(msg)-1:
        for add in range(1,len(msg)-idx+1):
            if msg[idx:idx+add] in alphabets:
                findIdx = alphabets.index(msg[idx:idx+add])
                if idx+add == len(msg):
                    answer.append(findIdx + 1)
                    idx = len(msg)
                    break
            else:
                answer.append(findIdx+1)
                alphabets.append(msg[idx:idx+add])
                idx += add - 1
                break
    return answer

print(solution(msg))
