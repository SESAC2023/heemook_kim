'''
# 오답인 코드
import sys
sys.setrecursionlimit(1e6)

# dfs 정의
def dfs(visited, graph, start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for i in graph[start]:
        if not visited[i]:
            visited[i] = cnt
            dfs(visited, graph, i)

# 정점, 간선, 시작노드 입력 받기
n, m, r = map(int, sys.stdin.readline().split())

# 간선 정보 입력 받기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in graph:
    _.sort(reverse=True)

# 정점 방문 정보
visited = [0] * (n + 1)
cnt = 1

# 함수 호출
dfs(visited, graph, r)

# 출력
for _ in visited[1:]:
    print(_)

'''

# 출력만 다른데 정답인 코드
import sys
sys.setrecursionlimit(10**6)

# dfs 정의
def dfs(visited, graph, start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for i in graph[start]:
        if not visited[i]:
            visited[i] = cnt
            dfs(visited, graph, i)

# 정점, 간선, 시작노드 입력 받기
n, m, r = map(int, sys.stdin.readline().split())

# 간선 정보 입력 받기
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in graph:
    _.sort(reverse=True)

# 정점 방문 정보
visited = [0] * (n + 1)
cnt = 1

# 함수 호출
dfs(visited, graph, r)

# 출력
for i in range(1, n + 1):
    print(visited[i])
