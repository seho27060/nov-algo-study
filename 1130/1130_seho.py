# 221130 n^2배열 자르기
# 구현?
# 아니 뭐야 쉬운거였ㄴ

def solution(n, left, right):
    answer = []

    idx = left

    while idx < right + 1:
        row, col = divmod(idx,n)
        result = col
        if col < row:
            result = row + 1
        else:
            result += 1
        answer.append(result)

        idx += 1

    return answer

