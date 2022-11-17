def parseTime(strTime):
    hour = strTime[:2]
    minute = strTime[3:]
    return int(hour) * 60 + int(minute) 
    

def solution(m, musicinfos):
    thatSong = '(None)'
    maxTimeDiff = 0
    for info in musicinfos:
        start, end, name, note = info.split(',')
        
        for a, b in (('C#', 'H'), ('D#', 'I'), ('F#', 'J'), ('G#', 'K'), ('A#', 'L')):
            note = note.replace(a, b)
            m = m.replace(a, b)

        N, M = len(note), len(m)
        timeDiff = parseTime(end) - parseTime(start)
        
        newNote = note * (timeDiff // N) + note[: timeDiff % N]
        for i in range(len(newNote) - M + 1):
            if m == newNote[i:i + M]:
                if maxTimeDiff < timeDiff:
                    maxTimeDiff = timeDiff
                    thatSong = name
                break

    return thatSong
