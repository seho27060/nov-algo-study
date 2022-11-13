# bfs맞나...?
# 그냥 갈 수 있는 모든 노드 탐색해서 가장 많이 나오는 양의 수 저장했습니다.
answer = 1
def solution(info, edges):
    G = [[] for _ in range(len(info))]
    visited = [-1] * len(info)
    visited[0] = 1
    for p, c in edges:
        G[p].append(c)
    for c in G[0]:
        visited[c] = 0

    def bfs(idx, visited, s, w):
        global answer
        if s == w:
            return
        if s > answer:
            answer = s
        for c in G[idx]:
            visited[c] = 0
        for idx in range(len(visited)):
            if visited[idx] == 0:
                visited[idx] = 1
                if info[idx] == 0:
                    bfs(idx, visited[::], s+1, w)
                else:
                    bfs(idx, visited[::], s, w+1)
                visited[idx] = 0

    for idx in range(len(visited)):
        if visited[idx] == 0:
            visited[idx] = 1
            if info[idx] == 0:
                bfs(idx, visited[::], 2, 0)
            visited[idx] = 0
    print(answer)

solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])