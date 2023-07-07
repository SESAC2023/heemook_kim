# BOJ 7562번
from collections import deque

t = int(input())

while t:
    
    l = int(input())
        
    graph = [[0] * l for _ in range(l)]
    
    visited = [[0] * l for _ in range(l)]
    
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int ,input().split())
    
    visited[start_x][start_y] = 1
    
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    def bfs(x, y):
        if x < 0 or x >= l or y < 0 or y >= l:
            return False
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return True
    
    bfs(start_x, start_y)
    print(visited[end_x][end_y] - 1)
    
    t -= 1
