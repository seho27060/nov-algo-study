import re

def solution(msg):
    answer = []
    LZW = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
           "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
           "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
           "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    num = 26
    while msg:
        res = 0
        for l in LZW:
            matchString = re.match(l, msg)
            if matchString != None:
                if res < matchString.span()[1]:
                    res = matchString.span()[1]
        answer.append(LZW[msg[:res]])
        num += 1
        LZW[msg[:res + 1]] = num
        msg = msg[res:]

    return answer