# 접근할 방향이 안보여서 일단 구현으로 갔는데 정답;;;
# 숫자목록을 리스트로 관리하면 시초 날까봐 모두 문자열로 처리했다.

def solution(n, t, m, p):
    dic = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    answer = ''
    w = '0'
    goal = t * (m+1)
    val = 0
    while len(w) < goal:
        word = ''
        num = val
        while num != 0:
            quo, rem = divmod(num, n)
            if rem < 10:
                word = str(rem) + word
            else:
                word = dic[rem] + word
            num = quo
        w += word
        val += 1
    cnt = 0
    print(w)
    for i in range(p, goal, m):
        answer += w[i-1]
        print(i-1)
        cnt += 1
        if cnt == t:
            return answer

solution(16, 16, 2, 2)