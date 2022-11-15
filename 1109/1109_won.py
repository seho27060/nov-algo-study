import re

def solution(files):
    tmp = []
    for file in files:
        tmp.append(re.split(r"([0-9]+)", file))

    tmp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    ans = []
    for i in tmp:
        ans.append("".join(i))
    return ans