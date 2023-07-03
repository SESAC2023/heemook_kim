# BOJ 2667번
from collections import deque
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 지도 크기
n = int(input())

# 지도 정보
graph = [[] for _ in range(n)]
for _ in range(n):
    graph[_] = [int(i) for i in input().rstrip()]

# 방문 정보
visited = [[False] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            continue
        if not visited[nx][ny]:
            dfs(nx, ny)

answer = 0
answer_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        
        if not visited[i][j]:
            answer += 1
            cnt = 0
            dfs(i, j)
            answer_list.append(cnt)

print(answer)
answer_list.sort()
for x in answer_list:
    print(x)
