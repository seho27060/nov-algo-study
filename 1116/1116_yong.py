# 조건에 맞게 구현하는 문제
# #이 들어가는 음을 치환하여 하나의 문자로 변경하고 처리하면 편안함

def solution(m, musicinfos):
    m=m.replace("C#", "c")
    m=m.replace("D#", "d")
    m=m.replace("F#", "f")
    m=m.replace("G#", "g")
    m=m.replace("A#", "a")

    answer = '(None)'
    play = -1
    for musicinfo in musicinfos:
        song = ''
        s, e, t, r = musicinfo.split(",")
        r=r.replace("C#", "c")
        r=r.replace("D#", "d")
        r=r.replace("F#", "f")
        r=r.replace("G#", "g")
        r=r.replace("A#", "a")
        # print(r)
        startH = int(s[:2])
        startM = int(s[3:])
        endH = int(e[:2])
        endM = int(e[3:])
        diffM = (endH - startH) * 60 + (endM - startM)
        again = diffM // len(r)
        re = diffM % len(r)
        song += r * again
        song += r[:re+1]
        # print(song)
        print(diffM)
        if m in song:
            if play == -1:
                answer = t
                play = diffM
            else:
                if play < diffM:
                    answer = t
                    play = diffM

    print(answer)


solution("ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"])