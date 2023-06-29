# BOJ 1260번
import sys
input = sys.stdin.readline
from collections import deque

# 정점, 간선, 시작점
n, m, v = map(int, input().split())

# 간선 정보
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for _ in graph:
    _.sort()

# 방문 정보
visited = [False] * (n + 1)

# dfs 함수
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for _ in graph[start]:
        if not visited[_]:
            visited[_] = True
            dfs(graph, _, visited)

# dfs 호출 및 수행
dfs(graph, v, visited)
print()

# 방문 정보 초기화
visited = [False] * (n + 1)

# bfs 시작
q = deque()
visited[v] = True
q.append(v)
while q:
    current = q.popleft()
    print(current, end=' ')
    for _ in graph[current]:
        if not visited[_]:
            visited[_] = True
            q.append(_)
