import math


def solution(m, musicinfos):
    ans = None
    m = m.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
    for misicinfo in musicinfos:
        s, e, title, code = misicinfo.split(",")
        h, min = map(int, s.split(":"))
        start = h * 60 + min
        h, min = map(int, e.split(":"))
        end = h * 60 + min
        dur = end - start
        code = code.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")

        code *= math.ceil(dur / len(code))
        code = code[:dur]

        if m not in code:
            continue
        if ans == None or ans[0] < dur or (ans[0] == dur and ans[1] > start):
            ans = [dur, start, title]
    if ans:
        return ans[-1]

    return "(None)"