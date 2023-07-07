# BOJ 1697번
from collections import deque

n, k = map(int, input().split())

arr = [_ for _ in range((int(1e5) + 1))]
visited = [0] * (int(1e5) + 1)

dx = [lambda x : x - 1, lambda x : x + 1, lambda x : x * 2]

def bfs(x):
    if x < 0 or x > int(1e5):
        return False
    queue = deque()
    queue.append(x)
    while queue:    
        x = queue.popleft()
        for i in range(3):
            nx = dx[i](x)
            if nx < 0 or nx > int(1e5):
                continue
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)
            # 뭔가 여러 방법 중에서 최소 경우만 뽑아야 될 것 같은데 bfs는 자동으로 되나봅니다..?
            # else: 
            #     min_val = min(visited[nx], visited[x] + 1)
            #     if min_val != visited[nx]:
            #         visited[nx] = min_val
            #         queue.append(nx)

visited[n] = 1
bfs(n, k)
print(visited[k] - 1)
