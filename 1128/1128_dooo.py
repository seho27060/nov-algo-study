def solution(stones, k):
    answer = 0
    start = 0
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        flag = 0
        max_cnt = -1
        for s in stones:
            st = s-mid
            if st <= 0:
                if flag == 0:
                    cnt += 1
                else:
                    max_cnt = max(cnt, max_cnt)
                    cnt = 1
                    flag = 0
            else:
                flag = 1
        max_cnt = max(cnt, max_cnt)
        if max_cnt < k:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
    return answer