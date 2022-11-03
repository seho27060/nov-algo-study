# 조건이 많아서 코드가 더러워진 문제
# 조건 정리를 잘 해놓으면 깔끔히 풀 수 있으려나??

# 정답 리스트의 점수
ansV = 0
# 정답 리스트의 최소 점수
minV = 11
# 어피치 점수 저장용
Peach = 0
# 리턴용
answer = [-1]
def solution(n, info):
    global Peach
    # 어피치 점수 먼저 구하기
    for i in range(11):
        if info[i]:
            Peach += 10-i
    # 재귀함수에 사용할 라이언의 점수 리스트
    Lion = [0] * 11

    def check(n, lst, idx):
        global Peach, ansV, answer, minV
        # 화살을 다 쏜 경우
        if n == 0:
            # 점수 측정용 변수
            score = 0
            # 어피치 점수 뺄 용도의 변수
            minusV = 0
            # 최소 점수 기록할 변수
            V = 0
            # 리스트를 돌며 각 변수값을 갱신해주자
            for i in range(11):
                if lst[i]:
                    V = 10 - i
                    if lst[i] > info[i]:
                        score += 10-i
                        if info[i]:
                            minusV += 10-i
            # 점수가 갱신된 어피치 점수보다 높을 때
            if score > Peach - minusV:
                # 기존 저장한 정답의 점수보다 높다면 교체
                if not ansV or score - (Peach - minusV) > ansV:
                    minV = V
                    answer = lst[::]
                    ansV = score  - (Peach - minusV)
                # 둘이 점수차가 같다면 가장 낮은 점수를 맞춘 기록으로 교체
                elif score - (Peach - minusV) == ansV:
                    if V < minV:
                        answer = lst[::]
                        ansV = score - (Peach - minusV)
            return
        # n이 0이 아니면 또 리스트를 순회하며 넣어주자
        for i in range(idx, 11):
            if lst[i] <= info[i]:
                lst[i] += 1
                check(n-1, lst, i)
                lst[i] -= 1

    # 처음 시작은 그냥 전체 리스트 순환하며 1넣고 시작
    for i in range(11):
        Lion[i] += 1
        check(n-1, Lion, i)
        Lion[i] -= 1
    print(answer)

solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])