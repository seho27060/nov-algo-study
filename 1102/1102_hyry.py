def compare(firstLion, secondLion):
    for idx in range(10, -1, -1):
        if firstLion[idx] > secondLion[idx]:
            return firstLion
        elif firstLion[idx] < secondLion[idx]:
            return secondLion
    return firstLion


def solution(n, info):
    apeachScore = lionScore = 0
    maxScoreDiff = 0
    maxLionInfo = [0] * 11

    ST = [([0] * 11, n, n, -1, apeachScore, lionScore)]
    while ST:
        curLionInfo, leftArrow, apeachLeftArrow, curIdx, curApeachScore, curLionScore = ST.pop()
        newIdx = curIdx + 1

        if leftArrow < 0:
            continue
        if newIdx == 11 and leftArrow > 0:
            curLionInfo[-1] = leftArrow
            leftArrow = 0
        if leftArrow == 0 and apeachLeftArrow == 0:
            scoreDiff = curLionScore - curApeachScore
            if maxScoreDiff < scoreDiff:
                maxScoreDiff = scoreDiff
                maxLionInfo = curLionInfo[::]
            elif maxScoreDiff == scoreDiff:
                biggerDiffInfo = compare(maxLionInfo, curLionInfo)
                maxLionInfo = biggerDiffInfo[::]

        if newIdx == 11:
            continue

        requiredArrow = info[newIdx] + 1
        curScore = 10 - newIdx
        newLionInfo = curLionInfo[::]
        newLionInfo[newIdx] = requiredArrow
        if leftArrow:
            ST.append((newLionInfo, leftArrow - requiredArrow, apeachLeftArrow - info[newIdx], newIdx, curApeachScore,
                       curLionScore + curScore))
        ST.append((curLionInfo[::], leftArrow, apeachLeftArrow - info[newIdx], newIdx,
                   curApeachScore + (curScore if info[newIdx] else 0), curLionScore))

    return maxLionInfo if maxScoreDiff != 0 else [-1]
