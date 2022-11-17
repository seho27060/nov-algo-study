# 221116
# 파싱 + 구현 문제

def solution(m, musicinfos):
    answer = "(None)"
    musicTime = 0

    other = ["C#","D#","F#","G#","A#"]

    playedMusic = []
    for idx in range(len(m)):
        check = False
        if m[idx] != "#":
            if idx < len(m) - 1:
                if m[idx:idx + 2] in other:
                    playedMusic.append(m[idx:idx+2])
                    check =True
            if check == False:
                playedMusic.append(m[idx])

    for musicinfo in musicinfos:
        start,end,name,sheet = musicinfo.split(",")
        hour = int(end[:2]) - int(start[:2])
        minutes = hour*60 + (int(end[3:5]) - int(start[3:5]))
        idx = 0
        music = []
        tictok = minutes
        # 시간만큼의 재생음악 생성
        while tictok > 0:
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
            tictok -= 1

        for soundIdx in range(len(music)):
            if music[soundIdx] == playedMusic[0] and soundIdx + len(playedMusic) <= len(music):
                if "".join(playedMusic) == "".join(music[soundIdx:soundIdx+len(playedMusic)]):
                    if minutes > musicTime:
                        answer = name
                        musicTime = minutes
                        break

    return answer










