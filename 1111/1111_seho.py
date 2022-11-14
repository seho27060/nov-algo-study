# 221113 양과 늑대
# bfs? 
# 이동하고 나서 양과 늑대 값은 해당 시점에서 지나온 모든 지점이 공유한다.

def solution(info, edges):
    global answer
    answer = 0
    graphs = [[] for _ in range(len(info))]
    for edge in edges:
        graphs[edge[0]].append(edge[1])

    def bfs(sheep,wolf,visited):
        global answer
        if sheep <= wolf:
            return
        answer = max(answer,sheep)

        for now in visited:
            for nxt in graphs[now]:
                if nxt not in visited:
                    nxtVisted = visited.copy()
                    nxtVisted.append(nxt)
                    if info[nxt] == 0:
                        bfs(sheep+1,wolf,nxtVisted)
                    else:
                        bfs(sheep,wolf+1,nxtVisted)
    bfs(1,0,[0])
    return answer
