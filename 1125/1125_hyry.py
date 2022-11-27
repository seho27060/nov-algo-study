def parseTime(strTime):  # str time -> seconds
    hour = int(strTime[:2])
    minute = int(strTime[3:5])
    second = int(strTime[6:])
    return hour * 3600 + minute * 60 + second


def constructTime(numTime):
    hour = str(numTime // 3600)
    numTime %= 3600
    minute = str(numTime // 60)
    second = str(numTime % 60)
    if len(hour) == 1: hour = '0' + hour
    if len(minute) == 1: minute = '0' + minute
    if len(second) == 1: second = '0' + second
    return hour + ':' + minute + ':' + second


def solution(play_time, adv_time, logs):
    playTime = parseTime(play_time)
    adTime = parseTime(adv_time)

    N = len(logs)
    timeAcc = [0] * (playTime + 2)
    for i in range(N):
        _startTime, _endTime = logs[i].split('-')
        startTime = parseTime(_startTime)
        endTime = parseTime(_endTime)
        # 누적이 무조건 1부터 시작하니까
        timeAcc[startTime + 1] += 1
        timeAcc[endTime + 1] -= 1
        # 시간 초과
        # for j in range(startTime, endTime + 1):
        #     timeAcc[j] += j - startTime

    # 누적합 만들기
    for i in range(playTime + 1):
        timeAcc[i + 1] += timeAcc[i]
    for i in range(playTime + 1):
        timeAcc[i + 1] += timeAcc[i]

    maxIdx = maxV = 0
    for i in range(adTime, playTime + 1):
        tmp = timeAcc[i] - timeAcc[i - adTime]
        if tmp > maxV:
            maxV = tmp
            maxIdx = i - adTime

    return constructTime(maxIdx)
