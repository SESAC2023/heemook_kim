# BOJ 1303번
n, m = map(int, input().split())

graph = [list(input()) for _ in range(m)]

visited = [[0] * n for _ in range(m)]

def dfs(x, y, color):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n: # 가로 세로 잘 확인하자!
        return False
    
    if not visited[x][y] and graph[x][y] == color:
        visited[x][y] = 1
        cnt += 1
        dfs(x - 1, y, color)
        dfs(x + 1, y, color)
        dfs(x, y - 1, color)
        dfs(x, y + 1, color)
        return True
    return True

result_w = 0
result_b = 0
for i in range(m): # 가로 세로 잘 확인하자!
    for j in range(n): # 가로 세로 잘 확인하자!
        cnt = 0
        if not visited[i][j] and dfs(i, j, 'W'):
            result_w += cnt ** 2
        
        cnt = 0
        if not visited[i][j] and dfs(i, j, 'B'):
            result_b += cnt ** 2

print(result_w, result_b)
# print(visited)
