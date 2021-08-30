def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for idx in range(1, len(graph[v])):
        if not visited[idx]:
            if graph[v][idx] == 1:
                visited[v] = True
                dfs(graph, idx, visited)


def bfs(graph, v, visited2):
    import collections
    queue = collections.deque([])
    visited2[v] = True
    queue.append(v)
    print(v, end=' ')

    while queue:
        node = queue.popleft()
        for idx in range(1, len(graph[node])):
            if not visited2[idx] and graph[node][idx] == 1:
                visited2[idx] = True
                queue.append(idx)
                print(idx, end=' ')


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
visited2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(graph, v, visited)
print()
bfs(graph, v, visited2)