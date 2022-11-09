def parseFileName(fileName):
    N = len(fileName)
    
    head = number = tail = ''
    firstNumOccur = False
    lastNumOccur = False
    for idx in range(N):
        if not firstNumOccur:
            if not fileName[idx].isdigit():
                head += fileName[idx].lower()
            else:
                firstNumOccur = True
                number += fileName[idx]
        else:
            if not lastNumOccur:
                if fileName[idx].isdigit():
                    number += fileName[idx]
                else:
                    lastNumOccur = True
                    tail = fileName[idx:]
                    break
    return [head, int(number), tail]

        
def solution(files):
    fileDic = []
    for file in files:
        fileNameArr = parseFileName(file)
        fileDic.append((file, fileNameArr))
    
    newFileDic = sorted(fileDic, key=lambda x: (x[1][0], x[1][1]))
    
    answer = [fileTuple[0] for fileTuple in newFileDic]
    return answer
