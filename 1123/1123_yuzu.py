from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = []
    for p in permutations(user_id, len(banned_id)):
        cnt = 0
        for i in range(len(banned_id)):
            if not re.match(banned_id[i].replace('*', '.'), p[i]):
                break
            if len(banned_id[i]) != len(p[i]):
                break
            else:
                cnt += 1
        if cnt == len(banned_id):
            p = sorted(list(p))
            if p not in answer:
                answer.append(p)
    return len(answer)