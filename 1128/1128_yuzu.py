def solution(stones, k):
    answer = 0
    l, r = 1, 1e10
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                r = mid - 1
                break
        if cnt < k:
            l = mid + 1
    answer = l
    return answer