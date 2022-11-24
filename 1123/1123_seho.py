# 221123 불량사용자
# 구현?

from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    result = []

    candiList = list(permutations(user_id,len(banned_id)))

    for candi in candiList:
        check = True
        for idx in range(len(candi)):
            if len(candi[idx]) == len(banned_id[idx]):
                for alphaIdx in range(len(candi[idx])):
                    if banned_id[idx][alphaIdx] == "*" or candi[idx][alphaIdx] == banned_id[idx][alphaIdx]:
                        pass
                    else:
                        check = False
                        break
            else:
                check = False
            if check == False:
                break
        if check:
            if sorted(candi) not in result:
                result.append(sorted(candi))
            answer += 1
    return len(result)
