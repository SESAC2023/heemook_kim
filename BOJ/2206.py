# BOJ 2206번
import sys
from collections import deque
input = sys.stdin.readline

# 행, 열
n, m = map(int, input().split())

# 그래프 정보
graph = [[int(i) for i in input().rstrip()] for j in range(n)]

# 벽 좌표 체크
chk = deque()
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            chk.append((a, b))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

# 정답 저장
answer = deque()
# BFS 정의
def bfs(x, y):
    # 큐 생성
    queue = deque()
    # 벽 하나씩 부시기
    for j in chk:
        a, b = j[0], j[1]
        graph[a][b] = 0        
        # 방문 정보 초기화
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        # 시작 점 입력
        queue.append((0, 0))
        # 큐가 빌 때까지 수행
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        
        # 최단 거리 저장
        if visited[n - 1][m - 1]:
            answer.append(visited[n - 1][m - 1])
        else:
            answer.append(-1)        
        
        # 다시 벽으로 채우기
        graph[a][b] = 1        

# bFS 수행
bfs(0, 0)

# 저장된 값들 중에서 최최단 거리 찾기
min_val = int(1e6)
for k in answer:
    if k != -1:
        min_val = min(min_val, k)

# 벽 부시고도 도달 못하는지 확인
if min_val != int(1e6):
    print(min_val)
else:
    print(-1)

