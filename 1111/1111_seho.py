# 221113 양과 늑대
# bfs? 

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
