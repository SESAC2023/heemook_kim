# 틀린 답
"""
# BOJ 1012번
import sys
sys.setrecursionlimit(int(1e6))
from collections import deque

# 테스트 케이스 개수
t = int(input())

while t:
    # 행, 열, 배추 수
    n, m, k = map(int, input().split())
    # 그래프 생성
    graph = [[0] * m for _ in range(n)]
    # 배추 위치 입력
    for i in range(k):
        u, v = map(int, input().split())
        if graph[u][v] == 0:
            graph[u][v] = 1
        else:
            raise NameError('oops')            
            
    # 방문 정보 초기화
    visited = [[False] * m for _ in range(n)]
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 밭 전체 탐색
    def bfs(x, y):
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))        
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx > (n - 1) or ny < 0 or ny > (m - 1):
                    continue
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    continue
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    dfs(x, y)
        
        answer = sum([i.count(1) for i in graph]) # 연결된 배추들은 모두 1부터 시작하므로
        return answer
    
    # 배추를 발견하면 연결된 배추 다 찾기
    def dfs(x, y):
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > (n - 1) or ny < 0 or ny > (m - 1):
                continue
            if not visited[nx][ny] and graph[nx][ny] >= 1:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1 # 처음 배추만 1이고 나머지 이어진 배추들은 순차적으로 2, 3, 4... 
                dfs(nx, ny)
    
    print(bfs(0, 0))
    t -= 1
    """
# 정답
import sys
sys.setrecursionlimit(int(1e6))
t = int(input())

while t:
    n, m, k = map(int, input().split())
    
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u][v] = 1
    
    visited = [[False] * m for _ in range(n)]
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if not visited[x][y] and graph[x][y] == 1:
            visited[x][y] = True
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    
    print(result)    
    t -= 1
