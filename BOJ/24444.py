import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 노드 수, 간선 수, 시작 노드
n, m, r = map(int, input().split())

# 간선 정보
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in graph:
    _.sort()

# 방문 정보
visited = [False] * (n + 1)

# bfs 수행
# 시작할 때
queue = deque()
queue.append(r)
visited[r] = True
# 방문 순서
answer = [0] * (n + 1) 
order = 1
while queue:
    v = queue.popleft()
    answer[v] = order
    order += 1
    # 인접 노드 확인
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

for i in range(1, n + 1):
    print(answer[i])
