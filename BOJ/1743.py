# BOJ 1743번
import sys
sys.setrecursionlimit(int(1e6))
# 행, 열, 개수
n, m, k = map(int, input().split())
# 그래프 초기화
graph = [[0] * m for _ in range(n)]
# 그래프 정보
for i in range(k):
    u, v = map(int, input().split())
    graph[u - 1][v - 1] = 1
# 방문 정보
visited = [[False] * m for _ in range(n)]
# dfs 수행
def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if not visited[x][y] and graph[x][y]:
        visited[x][y] = True
        cnt += 1 # 최대 깊이 계산
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result, cnt = 0, 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result = max(cnt, result) # 가장 큰 값을 결과로 선택
        cnt = 0 # 카운트 초기화

print(result)
