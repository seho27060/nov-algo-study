def solution(info, edges):
    ans = []
    visited = [0] * len(info)
    visited[0] = 1
    def dfs(sheep, wolf):
        if sheep > wolf:
            ans.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]
            if visited[parent] and visited[child] == 0:
                visited[child] = 1
                dfs(sheep + (isWolf == 0), wolf + (isWolf == 1))
                visited[child] = 0
    dfs(1, 0)
    return max(ans)