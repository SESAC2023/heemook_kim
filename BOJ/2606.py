# BOJ 2606번
num_computers = int(input())
connected = int(input())

graph = [[] for _ in range(num_computers + 1)]
for _ in range(connected):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for _ in graph:
    _.sort()

visited = [False] * 101

def dfs(graph, start, visited):
    visited[start] = True
    for _ in graph[start]:
        if not visited[_]:
            visited[_] = True
            dfs(graph, _, visited)

dfs(graph, 1, visited)

print(sum(visited) - 1)
