from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    ans = []
    for lst in permutations(user_id, len(banned_id)):
        ans_lst = []
        for i in range(len(lst)):
            flag = 0
            if len(lst[i]) != len(banned_id[i]):
                continue
            else:
                for k in range(len(lst[i])):
                    if banned_id[i][k] != '*' and lst[i][k] != banned_id[i][k]:
                        flag = 1
            if flag == 0:
                ans_lst.append(lst[i])
        if len(ans_lst) == len(banned_id):
            ans_lst.sort()
            if ans_lst not in ans:
                ans.append(ans_lst)
    answer = len(ans)
    return answer