#221109 [3차] 파일명 정렬
# 껄껄 파싱만 하면되는문제

def solution(files):
    answer = []
    numbers = [str(i) for i in range(10)]

    headNumberTails = []
    for file in files:
        head = ""
        idx = 0
        for cut in range(0,len(file)):
            idx = cut
            if file[idx] in numbers:
                break
            else:
                head = head + file[idx].upper()

        number = ""
        for cut in range(idx,len(file)):
            idx = cut
            if file[idx] not in numbers:
                break
            else:
                number = number + file[idx]
        tail = files[idx:]

        headNumberTails.append([head,int(number),tail,file])
    # print(headNumberTails)
    headNumberTails.sort(key=lambda x:(x[0],x[1]))
    # print(headNumberTails)
    for headNumberTail in headNumberTails:
        answer.append(headNumberTail[3])
    return answer
