# 파싱 후 조건에 맞춰 정렬하는 문제
# 람다식이랑 sort정렬하는 거 기억안나서 결국 답 참고해버림 ㅠ...

def solution(files):
    answer = []
    lst = []
    for file in files:
        head = 0
        for i in range(head, len(file)):
            if file[i].isdigit():
                break
            head += 1
        num = head
        for i in range(num, len(file)):
            if not file[i].isdigit():
                break
            num += 1
        HEAD = file[:head]
        NUMBER = file[head:num]
        TAIL = file[num:]
        lst.append((HEAD, NUMBER, TAIL))

    lst.sort(key=lambda  x:(x[0].lower(), int(x[1])))
    for i in lst:
        answer.append("".join(i))
    print(answer)

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])