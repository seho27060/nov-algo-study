# 이진탐색으로 푼 문제
# l을 최소값 r을 200000000로 설정했는데 시초가나서 min max를 썼는데 통과...??? 이거 맞나
def solution(stones, k):
    answer = 0
    l = min(stones)
    r = max(stones)

    def find(mid):
        cnt = 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                cnt += 1
                if cnt == k:
                    return True
            else:
                cnt = 0
        return False

    while l <= r:
        mid = (l + r) // 2
        if find(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    print(answer)

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)