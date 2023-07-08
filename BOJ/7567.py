# BOJ 7576번
import sys
input = sys.stdin.readline
from collections import deque

# 열, 행
m, n = map(int, input().split())

# 그래프 정보
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 방문 정보
visited = [[0] * m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어난 경우
                continue
            
            if graph[nx][ny] == -1: # 토마토가 들어있지 않은 경우
                continue
            
            if visited[nx][ny]: # 방문한 적이 있는 경우
                min_val = min(visited[nx][ny], visited[x][y] + 1) # 현재까지의 최단 경로와 비교
                if visited[nx][ny] == min_val: # 현재까지의 최단 경로가 최단 경로인 경우
                    continue
                else: # 새로운 경로가 더 짧은 경로인 경우
                    visited[nx][ny] = min_val # 최단 경로 갱신
                    queue.append((nx, ny)) # queue 에 추가
            
            if not visited[nx][ny]: # 방문한 적이 없는 경우
                visited[nx][ny] = visited[x][y] + 1 # 최단 경로 갱신
                queue.append((nx, ny)) # queue 에 추가
    return True

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 익은 토마토인 경우
            visited[i][j] = 1 # 방문 정보 갱신
            bfs(i, j) # BFS 탐색 수행
        if graph[i][j] == -1: # 토마토가 들어있지 않은 경우
            cnt += 1 # 토마토가 들어있지 않은 경우 카운트

answer = 0
val = 0
for row in visited:
    row_max = max(row) # 창고를 다 채우는 경우의 수 찾기
    answer = max(answer, row_max) # 정답 갱신
    val += row.count(0) # 익지 않은 토마토 수 카운트

if val == cnt: # 토마토가 들어있지 않은 경우와 익지 않은 토마토 수가 같다면
    print(answer - 1) # 처음 익은 토마토를 1로 시작했으므로
else:
    print(-1) # 고립되어 익지 않은 토마토가 있는 경우
