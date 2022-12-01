# 221128 징검다리 건너기
# while 문안에 갈수있는지 없는지 이분탐색으로 반복적으로 찾기?

def solution(stones, k):
    answer = 0

    start = 0
    end = max(stones)

    while start <= end:
        cnt = 0
        mid = (start + end)//2

        check = True
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                end = mid - 1
                check = False
                break
        if check:
            answer = max(answer,mid)
            start = mid + 1

    return answer

