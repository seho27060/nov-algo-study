# 221116
# 맹~?

m ="ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF","12:50,13:01,A,BBBB"]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

def solution(m, musicinfos):
    answer = "(None)"
    musicTime = 0

    origin = ["C","D","E","F","G","A","B"]
    other = ["C#","D#","F#","G#","A#"]
    for musicinfo in musicinfos:
        start,end,name,sheet = musicinfo.split(",")
        hour = int(end[:2]) - int(start[:2])
        minutes = hour*60 + (int(end[3:5]) - int(start[3:5]))
        print(musicinfo,minutes)
        idx = 0
        music = []
        # 시간만큼의 재생음악 생성
        while minutes > 0:
            check = False
            if idx >= len(sheet):
                idx = 0
            if idx + 1 < len(sheet):
                if sheet[idx:idx+2] in other:
                    music.append(sheet[idx:idx+2])
                    idx += 2
                    check = True
            if check == False:
                music.append(sheet[idx])
                idx += 1
            minutes -= 1

        print(len(music),music)

    return answer

print(solution(m, musicinfos))