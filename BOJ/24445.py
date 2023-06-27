# BOJ 24445번
import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 정점, 간선, 시작점
n, m, r = map(int, input().split())

# 간선 정보
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in graph:
    _.sort(reverse=True)

# 방문 정보
visited = [False] * (n + 1)

# BFS 시작
queue = deque()
queue.append(r)

answer = [0] * (n + 1)

order = 1
while queue:
    x = queue.popleft()
    visited[x] = True
    answer[x] = order
    order += 1
    
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            queue.append(y)

for _ in range(1, n + 1):
    print(answer[_])
