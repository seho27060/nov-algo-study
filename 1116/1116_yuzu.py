import re

def solution(m, musicinfos):
    answer = "(None)"
    res = -1
    m = m.replace('C#', 'V')
    m = m.replace('D#', 'W')
    m = m.replace('F#', 'X')
    m = m.replace('G#', 'Y')
    m = m.replace('A#', 'Z')
    for musicinfo in musicinfos:
        musicInfoSplit = musicinfo.split(',')
        musicInfoSplit[-1] = musicInfoSplit[-1].replace('C#', 'V')
        musicInfoSplit[-1] = musicInfoSplit[-1].replace('D#', 'W')
        musicInfoSplit[-1] = musicInfoSplit[-1].replace('F#', 'X')
        musicInfoSplit[-1] = musicInfoSplit[-1].replace('G#', 'Y')
        musicInfoSplit[-1] = musicInfoSplit[-1].replace('A#', 'Z')
        timeDiff = (int(musicInfoSplit[1][:2]) * 60 + int(musicInfoSplit[1][3:])) - (
                    int(musicInfoSplit[0][:2]) * 60 + int(musicInfoSplit[0][3:]))
        matchM = re.search(m, musicInfoSplit[-1][:timeDiff] * 10000)
        if matchM != None:
            if res < timeDiff:
                res = timeDiff
                answer = musicInfoSplit[2]

    return answer