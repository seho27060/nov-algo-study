# 단어별 넘버링을 지정
# 조건에 맞춰 구현한 문제

def solution(msg):
    answer = []
    dicN = 27
    dic = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8,
        'I' : 9,
        'J' : 10,
        'K' : 11,
        'L' : 12,
        'M' : 13,
        'N' : 14,
        'O' : 15,
        'P' : 16,
        'Q' : 17,
        'R' : 18,
        'S' : 19,
        'T' : 20,
        'U' : 21,
        'V' : 22,
        'W' : 23,
        'X' : 24,
        'Y' : 25,
        'Z' : 26
    }
    idx = 0
    while idx < len(msg):
        word = ''
        num = 0
        for i in range(idx, len(msg)):
            word += msg[i]
            if word not in dic.keys():
                dic[word] = dicN
                dicN += 1
                break
            idx += 1
            num = dic[word]
        answer.append(num)
    return answer

solution("KAKAO")