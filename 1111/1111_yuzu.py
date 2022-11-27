import collections

def solution(info, edges):
    global answer
    answer = 0

    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])

    def dfs(x, s, w, path):
        global answer
        if info[x] == 0:
            s += 1
            answer = max(answer, s)
        else:
            w += 1

        if w >= s:
            return

        path.update(graph[x])

        for i in path:
            dfs(i, s, w, path-{i})

    dfs(0, 0, 0, set())
    return answer